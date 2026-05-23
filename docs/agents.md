# Agents

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt "https://code.claude.com/docs/llms.txt")
>
> Use this file to discover all available pages before exploring further.

[Subagents](./sub-agents "_sub-agents".md), [agent view](./agent-view "_agent-view".md), [agent teams](./agent-teams "_agent-teams".md), and [worktrees](./worktrees "_worktrees".md) each parallelize work in a different way. The right one depends on whether you want to stay in each conversation yourself, hand tasks off and check back later, or have Claude coordinate a group of workers for you.

| Approach | What it gives you | Use it when |
| --- | --- | --- |
| [Subagents](./sub-agents "_sub-agents".md) | Delegated workers inside one session that do a side task in their own context and return a summary | A side task would flood your main conversation with search results, logs, or file contents you won’t reference again |
| [Agent view](./agent-view "_agent-view".md) | One screen to dispatch and monitor sessions running in the background, opened with `claude agents`. Research preview | You have several independent tasks and want to hand them off, check status at a glance, and step in only when one needs you |
| [Agent teams](./agent-teams "_agent-teams".md) | Multiple coordinated sessions with a shared task list and inter-agent messaging, managed by a lead. Experimental and disabled by default | You want Claude to split a project into pieces, assign them, and keep the workers in sync |
| [Worktrees](./worktrees "_worktrees".md) | Separate git checkouts so parallel sessions never touch each other’s files | You’re running several sessions yourself, or your subagents edit overlapping files |
| [`/batch`](./commands "_commands".md) | A planned split of one large change into 5 to 30 worktree-isolated subagents that each open a pull request | A repo-wide migration or mechanical refactor you can describe in one instruction |

In every approach the workers are Claude sessions. To involve a different tool, expose it to Claude as an [MCP server](./mcp "_mcp".md).
You can combine these approaches. Agent view automatically moves each dispatched session into its own worktree when it needs to edit files, and a session you’re working in can spawn subagents that each get their own worktree.

Running several sessions or subagents at once multiplies token usage. See [Costs](./costs "_costs".md) for usage and rate-limit details.

## [​](#choose-an-approach "#choose-an-approach") Choose an approach

The right approach depends on who coordinates the work, whether the workers need to communicate, and whether they edit the same files:

* **Who coordinates the work?** If you want Claude to delegate and collect results inside one conversation, use [subagents](./sub-agents "_sub-agents".md). If you’re handing off independent tasks and checking back on them, use [agent view](./agent-view "_agent-view".md). If you want Claude to plan, assign, and supervise a group of workers, use [agent teams](./agent-teams "_agent-teams".md), which are experimental and disabled by default.
* **Do the workers need to talk to each other?** Subagents report results back to the conversation that spawned them, and agent view sessions report only to you. Teammates in an agent team share a task list and message each other directly.
* **Do the tasks touch the same files?** Isolate the work with [worktrees](./worktrees "_worktrees".md). Subagents and sessions you run yourself can each use a separate worktree. Agent teams don’t isolate teammates in worktrees, so [partition the work](./agent-teams#avoid-file-conflicts "_agent-teams#avoid-file-conflicts".md) so each teammate owns a different set of files.

## [​](#check-on-running-work "#check-on-running-work") Check on running work

The command for checking on running work depends on which approach you used:

* For background sessions, `claude agents` opens [agent view](./agent-view "_agent-view".md): one screen showing every session, its state, and which ones need your input.
* For subagents in the current session, `/agents` opens a panel with a **Running** tab listing live subagents and a **Library** tab where you [create and edit custom subagents](./sub-agents#use-the-%2Fagents-command "_sub-agents#use-the-%2Fagents-command".md). Despite the similar name, this is separate from `claude agents`.
* For anything running in the background of the current session, `/tasks` lists each item and lets you check on, attach to, or stop it.

For a desktop view of all your sessions, see [parallel sessions in the desktop app](./desktop#work-in-parallel-with-sessions "_desktop#work-in-parallel-with-sessions".md).

## [​](#learn-more "#learn-more") Learn more

Each guide below covers setup and configuration for one approach:

* [Create custom subagents](./sub-agents "_sub-agents".md): define reusable specialists and control which tools they can use.
* [Manage agents with agent view](./agent-view "_agent-view".md): dispatch sessions, watch their state, and attach when one needs you.
* [Orchestrate agent teams](./agent-teams "_agent-teams".md): set up a lead and teammates, assign tasks, and review their work.
* [Run parallel sessions with worktrees](./worktrees "_worktrees".md): start Claude in an isolated checkout, control what gets copied in, and clean up afterward.