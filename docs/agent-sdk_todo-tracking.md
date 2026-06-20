# Agent Sdk task Tracking

task tracking provides a structured way to manage tasks and display progress to users. The Claude Agent SDK includes built-in task functionality that helps organize complex workflows and keep users informed about task progression.

As of TypeScript Agent SDK 0.3.142 and Claude Code v2.1.142, sessions use the structured Task tools `TaskCreate`, `TaskUpdate`, `TaskGet`, and `TaskList` instead of `TodoWrite`. See [Migrate to Task tools](#migrate-to-task-tools) for how monitoring code changes. The examples on this page set `CLAUDE_CODE_ENABLE_TASKS=0` to keep showing `TodoWrite` for sessions that have not migrated yet.

### [​](#task-lifecycle) task Lifecycle

tasks follow a predictable lifecycle:

1. **Created** as `pending` when tasks are identified
2. **Activated** to `in_progress` when work begins
3. **Completed** when the task finishes successfully
4. **Removed** when all tasks in a group are completed

### [​](#when-tasks-are-used) When tasks Are Used

The SDK automatically creates tasks for:

* **Complex multi-step tasks** requiring 3 or more distinct actions
* **User-provided task lists** when multiple items are mentioned
* **Non-trivial operations** that benefit from progress tracking
* **Explicit requests** when users ask for task organization

## [​](#examples) Examples

### [​](#monitoring-task-changes) Monitoring task Changes

TypeScript

Python

```text
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Optimize my React app performance and track progress with tasks",
  // Re-enable TodoWrite, which this example monitors. Without it, the SDK uses
  // Task tools instead and these tool_use blocks never appear.
  options: { maxTurns: 15, env: { ...process.env, CLAUDE_CODE_ENABLE_TASKS: "0" } }
})) {
  // task updates are reflected in the message stream
  if (message.type === "assistant") {
    for (const block of message.message.content) {
      if (block.type === "tool_use" && block.name === "TodoWrite") {
        const tasks = block.input.tasks;

        console.log("task Status Update:");
        tasks.forEach((task, index) => {
          const status =
            task.status === "completed" ? "✅" : task.status === "in_progress" ? "🔧" : "❌";
          console.log(`${index + 1}. ${status} ${task.content}`);
        });
      }
    }
  }
}
```

### [​](#real-time-progress-display) Real-time Progress Display

TypeScript

Python

```text
import { query } from "@anthropic-ai/claude-agent-sdk";

class TodoTracker {
  private tasks: any[] = [];

  displayProgress() {
    if (this.tasks.length === 0) return;

    const completed = this.tasks.filter((t) => t.status === "completed").length;
    const inProgress = this.tasks.filter((t) => t.status === "in_progress").length;
    const total = this.tasks.length;

    console.log(`\nProgress: ${completed}/${total} completed`);
    console.log(`Currently working on: ${inProgress} task(s)\n`);

    this.tasks.forEach((task, index) => {
      const icon =
        task.status === "completed" ? "✅" : task.status === "in_progress" ? "🔧" : "❌";
      const text = task.status === "in_progress" ? task.activeForm : task.content;
      console.log(`${index + 1}. ${icon} ${text}`);
    });
  }

  async trackQuery(prompt: string) {
    for await (const message of query({
      prompt,
      // Re-enable TodoWrite, which this tracker watches for.
      options: { maxTurns: 20, env: { ...process.env, CLAUDE_CODE_ENABLE_TASKS: "0" } }
    })) {
      if (message.type === "assistant") {
        for (const block of message.message.content) {
          if (block.type === "tool_use" && block.name === "TodoWrite") {
            this.tasks = block.input.tasks;
            this.displayProgress();
          }
        }
      }
    }
  }
}

// Usage
const tracker = new TodoTracker();
await tracker.trackQuery("Build a complete authentication system with tasks");
```

## [​](#migrate-to-task-tools) Migrate to Task tools

The Task tools split the single `TodoWrite` call into `TaskCreate` for each new item and `TaskUpdate` for each status change, with `TaskList` and `TaskGet` available for the model to read back the current list. Your monitoring code still inspects `tool_use` blocks in the assistant stream, but maintains a map keyed by task ID instead of replacing the whole list on every call. The Task tools are the default as of TypeScript Agent SDK 0.3.142 and Claude Code v2.1.142, so no `options.env` change is needed.

| With `TodoWrite` | With Task tools |
| --- | --- |
| One tool call rewrites the full `tasks` array | `TaskCreate` adds one item, `TaskUpdate` patches one item by `taskId` |
| Match `block.name === "TodoWrite"` | Match `block.name === "TaskCreate"` or `"TaskUpdate"` |
| Item shape: `{ content, status, activeForm }` | `TaskCreate` input: `{ subject, description, activeForm?, metadata? }`. `TaskUpdate` input: `{ taskId, status?, subject?, description?, activeForm?, addBlocks?, addBlockedBy?, owner?, metadata? }`. `status` is `"pending"`, `"in_progress"`, or `"completed"`; set `status: "deleted"` to delete |
| Render `block.input.tasks` directly | Accumulate items across calls, or read a snapshot from a `TaskList` tool result |

The assigned task ID is not in the `TaskCreate` input. It comes back in the matching `tool_result` as `{ task: { id, subject } }`, so capture it from the result block to key your map. The following example shows the minimal change to the [Monitoring task Changes](#monitoring-task-changes) loop. To render a complete list, watch for a `TaskList` tool result in the stream or accumulate `TaskCreate` results and `TaskUpdate` inputs into a map.
The streamed `tool_use` input is the raw shape the model emitted. Claude Code repairs some close-but-incorrect key names before execution, mapping `id` or `task_id` to `taskId` and `active_form` to `activeForm`, but that repair is not reflected in the stream. Read `TaskUpdate` input fields defensively, as the samples below do, rather than assuming the canonical name is always present.

TypeScript

Python

```text
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Optimize my React app performance",
})) {
  if (message.type !== "assistant") continue;
  for (const block of message.message.content) {
    if (block.type !== "tool_use") continue;
    if (block.name === "TaskCreate") {
      const input = block.input as { subject: string };
      console.log(`+ ${input.subject}`);
    } else if (block.name === "TaskUpdate") {
      const input = block.input as {
        taskId?: string;
        id?: string;
        task_id?: string;
        status?: string;
      };
      const taskId = input.taskId ?? input.id ?? input.task_id;
      if (taskId && input.status) console.log(`  ${taskId} -> ${input.status}`);
    }
  }
}
```

## [​](#related-documentation) Related Documentation

* [TypeScript SDK Reference](./agent-sdk_typescript.md)
* [Python SDK Reference](./agent-sdk_python.md)
* [Streaming vs Single Mode](./agent-sdk_streaming-vs-single-mode.md)
* [Custom Tools](./agent-sdk_custom-tools.md)