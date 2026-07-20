task tracking provides a structured way to manage tasks and display progress to users. The Claude Agent SDK includes built-in task functionality that helps organize complex workflows and keep users informed about task progression.

As of TypeScript Agent SDK 0.3.142 and Claude Code v2.1.142, sessions use the structured Task tools `TaskCreate`, `TaskUpdate`, `TaskGet`, and `TaskList` instead of `TodoWrite`. The Python SDK gets this change from the Claude Code CLI it launches, not from the Python package version: the switch applies once that CLI — the copy bundled inside the pip package, or one you point to with `cli_path` — is v2.1.142 or later. See [Migrate to Task tools](#migrate-to-task-tools "#migrate-to-task-tools") for how monitoring code changes. The examples on this page set `CLAUDE_CODE_ENABLE_TASKS=0` to keep showing `TodoWrite` for sessions that have not migrated yet.

### [​](#task-lifecycle "#task-lifecycle") task Lifecycle

tasks follow a predictable lifecycle:

1. **Created** as `pending` when tasks are identified
2. **Activated** to `in_progress` when work begins
3. **Completed** when the task finishes successfully
4. **Removed** when all tasks in a group are completed

### [​](#when-tasks-are-used "#when-tasks-are-used") When tasks Are Used

The SDK creates tasks for most multi-step work, such as:

* **Complex multi-step tasks** requiring 3 or more distinct actions
* **User-provided task lists** when multiple items are mentioned
* **Non-trivial operations** that benefit from progress tracking
* **Explicit requests** when users ask for task organization

It may skip tasks for very short or single-step requests.

## [​](#examples "#examples") Examples

Before running these examples, install the Claude Agent SDK by following the [quickstart](./agent-sdk_quickstart "._agent-sdk_quickstart".md).
Each example runs until the agent finishes and yields its final result message. If a session reaches its turn limit first, that result message has the `error_max_turns` subtype. Check `subtype` to detect that ending.
These examples use single-shot `query()` calls. After yielding an `error_max_turns` result, `query()` raises an error that includes `Reached maximum number of turns`. Each example wraps its loop in a try block to exit cleanly when that happens.
See [Handle the result](./agent-sdk_agent-loop#handle-the-result "._agent-sdk_agent-loop#handle-the-result".md) for the result subtypes.

### [​](#monitoring-task-changes "#monitoring-task-changes") Monitoring task Changes

TypeScript

Python

```text
import { query } from "@anthropic-ai/claude-agent-sdk";

try {
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
} catch (error) {
  // A single-shot query() throws after yielding an error result,
  // such as when the maxTurns limit is hit.
  console.log(`Session ended with an error: ${error}`);
}
```

```text
import asyncio

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock


async def main():
    try:
        async for message in query(
            prompt="Optimize my React app performance and track progress with tasks",
            # Re-enable TodoWrite, which this example monitors. Without it, the SDK uses
            # Task tools instead and these tool_use blocks never appear.
            options=ClaudeAgentOptions(max_turns=15, env={"CLAUDE_CODE_ENABLE_TASKS": "0"}),
        ):
            # task updates are reflected in the message stream
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, ToolUseBlock) and block.name == "TodoWrite":
                        tasks = block.input["tasks"]

                        print("task Status Update:")
                        for i, task in enumerate(tasks):
                            status = (
                                "✅"
                                if task["status"] == "completed"
                                else "🔧"
                                if task["status"] == "in_progress"
                                else "❌"
                            )
                            print(f"{i + 1}. {status} {task['content']}")
    except Exception as error:
        # A single-shot query() raises after yielding an error result,
        # such as when the max_turns limit is hit.
        print(f"Session ended with an error: {error}")


asyncio.run(main())
```

### [​](#real-time-progress-display "#real-time-progress-display") Real-time Progress Display

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
    try {
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
    } catch (error) {
      // A single-shot query() throws after yielding an error result,
      // such as when the maxTurns limit is hit.
      console.log(`Session ended with an error: ${error}`);
    }
  }
}

// Usage
const tracker = new TodoTracker();
await tracker.trackQuery("Build a complete authentication system with tasks");
```

```text
import asyncio

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock
from typing import List, Dict


class TodoTracker:
    def __init__(self):
        self.tasks: List[Dict] = []

    def display_progress(self):
        if not self.tasks:
            return

        completed = len([t for t in self.tasks if t["status"] == "completed"])
        in_progress = len([t for t in self.tasks if t["status"] == "in_progress"])
        total = len(self.tasks)

        print(f"\nProgress: {completed}/{total} completed")
        print(f"Currently working on: {in_progress} task(s)\n")

        for i, task in enumerate(self.tasks):
            icon = (
                "✅"
                if task["status"] == "completed"
                else "🔧"
                if task["status"] == "in_progress"
                else "❌"
            )
            text = (
                task["activeForm"]
                if task["status"] == "in_progress"
                else task["content"]
            )
            print(f"{i + 1}. {icon} {text}")

    async def track_query(self, prompt: str):
        try:
            async for message in query(
                prompt=prompt,
                # Re-enable TodoWrite, which this tracker watches for.
                options=ClaudeAgentOptions(max_turns=20, env={"CLAUDE_CODE_ENABLE_TASKS": "0"}),
            ):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, ToolUseBlock) and block.name == "TodoWrite":
                            self.tasks = block.input["tasks"]
                            self.display_progress()
        except Exception as error:
            # A single-shot query() raises after yielding an error result,
            # such as when the max_turns limit is hit.
            print(f"Session ended with an error: {error}")


# Usage
async def main():
    tracker = TodoTracker()
    await tracker.track_query("Build a complete authentication system with tasks")


asyncio.run(main())
```

## [​](#migrate-to-task-tools "#migrate-to-task-tools") Migrate to Task tools

The Task tools split the single `TodoWrite` call into `TaskCreate` for each new item and `TaskUpdate` for each status change, with `TaskList` and `TaskGet` available for the model to read back the current list. Your monitoring code still inspects `tool_use` blocks in the assistant stream, but maintains a map keyed by task ID instead of replacing the whole list on every call. The Task tools are the default as of TypeScript Agent SDK 0.3.142 and Claude Code v2.1.142, so no `options.env` change is needed.


| With `TodoWrite` | With Task tools |
| --- | --- |
| One tool call rewrites the full `tasks` array | `TaskCreate` adds one item, `TaskUpdate` patches one item by `taskId` |
| Match `block.name === "TodoWrite"` | Match `block.name === "TaskCreate"` or `"TaskUpdate"` |
| Item shape: `{ content, status, activeForm }` | `TaskCreate` input: `{ subject, description, activeForm?, metadata? }`. `TaskUpdate` input: `{ taskId, status?, subject?, description?, activeForm?, addBlocks?, addBlockedBy?, owner?, metadata? }`. `status` is `"pending"`, `"in_progress"`, or `"completed"`; set `status: "deleted"` to delete |
| Render `block.input.tasks` directly | Accumulate items across calls, or read a snapshot from a `TaskList` tool result |

The assigned task ID is not in the `TaskCreate` input. It comes back in the matching `tool_result` as `{ task: { id, subject } }`, so capture it from the result block to key your map. The following example shows the minimal change to the [Monitoring task Changes](#monitoring-task-changes "#monitoring-task-changes") loop. It reads only `tool_use` inputs and skips capturing IDs from `tool_result` blocks. To render a complete list, watch for a `TaskList` tool result in the stream or accumulate `TaskCreate` results and `TaskUpdate` inputs into a map.
The streamed `tool_use` input is the raw shape the model emitted. Claude Code repairs some close-but-incorrect key names before execution, mapping `id` or `task_id` to `taskId` and `active_form` to `activeForm`, but that repair is not reflected in the stream. Read `TaskUpdate` input fields defensively, as the samples below do, rather than assuming the canonical name is always present.

TypeScript

Python

```text
import { query } from "@anthropic-ai/claude-agent-sdk";

try {
  for await (const message of query({
    prompt: "Optimize my React app performance and track progress with tasks",
    options: { maxTurns: 15 },
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
} catch (error) {
  // A single-shot query() throws after yielding an error result.
  console.log(`Session ended with an error: ${error}`);
}
```

```text
import asyncio

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock

async def main():
    try:
        async for message in query(
            prompt="Optimize my React app performance and track progress with tasks",
            options=ClaudeAgentOptions(max_turns=15),
        ):
            if not isinstance(message, AssistantMessage):
                continue
            for block in message.content:
                if not isinstance(block, ToolUseBlock):
                    continue
                if block.name == "TaskCreate":
                    print(f"+ {block.input['subject']}")
                elif block.name == "TaskUpdate" and block.input.get("status"):
                    task_id = (
                        block.input.get("taskId")
                        or block.input.get("id")
                        or block.input.get("task_id")
                    )
                    if task_id:
                        print(f"  {task_id} -> {block.input['status']}")
    except Exception as error:
        # A single-shot query() raises after yielding an error result.
        print(f"Session ended with an error: {error}")


asyncio.run(main())
```

## [​](#related-documentation "#related-documentation") Related Documentation

* [TypeScript SDK Reference](./agent-sdk_typescript "._agent-sdk_typescript".md)
* [Python SDK Reference](./agent-sdk_python "._agent-sdk_python".md)
* [Streaming vs Single Mode](./agent-sdk_streaming-vs-single-mode "._agent-sdk_streaming-vs-single-mode".md)
* [Custom Tools](./agent-sdk_custom-tools "._agent-sdk_custom-tools".md)