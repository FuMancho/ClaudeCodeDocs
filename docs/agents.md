# Agents

[Subagents](./sub-agents "._sub-agents".md), [agent view](./agent-view "._agent-view".md), [agent teams](./agent-teams "._agent-teams".md), and [dynamic workflows](./workflows "._workflows".md) each parallelize work in a different way. The right one depends on whether you want to stay in each conversation yourself, hand tasks off and check back later, or have Claude coordinate a group of workers for you.


| Approach | What it gives you | Use it when |
| --- | --- | --- |
| [Subagents](./sub-agents "._sub-agents".md) | Delegated workers inside one session that do a side task in their own context and return a summary | A side task would flood your main conversation with search results, logs, or file contents you won’t reference again |
| [Agent view](./agent-view "._agent-view".md) | One screen to dispatch and monitor sessions running in the background, opened with `claude agents`. Research preview | You have several independent tasks and want to hand them off, check status at a glance, and step in only when one needs you |
| [Agent teams](./agent-teams "._agent-teams".md) | Multiple coordinated sessions with a shared task list and inter-agent messaging, managed by a lead. Experimental and disabled by default | You want Claude to split a project into pieces, assign them, and keep the workers in sync |
| [Dynamic workflows](./workflows "._workflows".md) | A script that runs many subagents and cross-checks their results, for work too big to coordinate one turn at a time or that needs more than a single pass | A job outgrows a handful of subagents, or you want findings verified against each other: a codebase-wide audit, a 500-file migration, cross-checked research, or a plan drafted from several angles |

In every approach the workers are Claude sessions. To involve a different tool, expose it to Claude as an [MCP server](./mcp "._mcp".md).
Two more tools support this work without being a way to run agents themselves:

* [Worktrees](./worktrees "._worktrees".md) give each session a separate git checkout, so parallel sessions never edit the same files. Use them for sessions you run yourself. Agent view moves each dispatched session into its own worktree automatically, and subagents you spawn can each get one too.
* [`/batch`](./commands "._commands".md) is a [skill](./skills "._skills".md) that has Claude split one large change into 5 to 30 worktree-isolated subagents that each open a pull request. It’s a packaged use of subagents and worktrees, not a separate coordination style.

A few other features run Claude without you driving each step, but they solve a different problem than splitting work across agents:

* A [background bash command](./interactive-mode#background-bash-commands "._interactive-mode#background-bash-commands".md) runs one shell command without blocking the conversation. It doesn’t spawn an agent.
* A [forked subagent](./sub-agents#fork-the-current-conversation "._sub-agents#fork-the-current-conversation".md), started with `/subtask`, is a subagent that inherits your full conversation context instead of starting fresh. It’s a way to spawn a subagent, not a separate surface. To copy the whole session into a new [background session](./agent-view#from-inside-a-session "._agent-view#from-inside-a-session".md) that runs alongside it, use `/fork`. With [agent view turned off](./agent-view#turn-off-agent-view "._agent-view#turn-off-agent-view".md), the forked-subagent command is `/fork` instead and `/subtask` isn’t available.
* A [routine](./routines "._routines".md) runs a session on a schedule in Anthropic’s cloud, not in parallel on your machine.

Running several sessions or subagents at once multiplies token usage. See [Costs](./costs "._costs".md) for usage and rate-limit details.

## [​](#choose-an-approach "#choose-an-approach") Choose an approach

The right approach depends on who coordinates the work, whether the workers need to communicate, and whether they edit the same files:

* **Who coordinates the work?**
  + Claude delegates and collects results inside one conversation: [subagents](./sub-agents "._sub-agents".md)
  + You hand off independent tasks and check back later: [agent view](./agent-view "._agent-view".md)
  + Claude plans, assigns, and supervises a group of workers: [agent teams](./agent-teams "._agent-teams".md), experimental and disabled by default
  + A script holds the plan instead of Claude’s turn-by-turn judgment: [dynamic workflows](./workflows "._workflows".md). See [how workflows compare to subagents and skills](./workflows#when-to-use-a-workflow "._workflows#when-to-use-a-workflow".md)
* **Do the workers need to talk to each other?** Subagents report results back to the conversation that spawned them, and agent view sessions report only to you. Teammates in an agent team share a task list and message each other directly.
* **Do the tasks touch the same files?** Isolate the work with [worktrees](./worktrees "._worktrees".md). Subagents and sessions you run yourself can each use a separate worktree. Agent teams don’t isolate teammates in worktrees, so [partition the work](./agent-teams#avoid-file-conflicts "._agent-teams#avoid-file-conflicts".md) so each teammate owns a different set of files.

## [​](#check-on-running-work "#check-on-running-work") Check on running work

The command for checking on running work depends on which approach you used:

* For background sessions, `claude agents` opens [agent view](./agent-view "._agent-view".md): one screen showing every session, its state, and which ones need your input.
* For subagents in the current session, named background subagents appear in the @-mention typeahead with their status. As of v2.1.198, `/agents` no longer opens a panel; it prints a notice pointing to the subagent file locations. To [create and edit custom subagents](./sub-agents#configure-subagents "._sub-agents#configure-subagents".md), ask Claude or edit the files directly. Despite the similar name, `/agents` is separate from `claude agents`.
* For anything running in the background of the current session, `/tasks` lists each item and lets you check on, attach to, or stop it. The list also includes subagents that have finished.
* For dynamic workflows, `/workflows` lists running and completed runs, the phase each is in, and how many agents have finished.

For a desktop view of all your sessions, see [parallel sessions in the desktop app](./desktop#work-in-parallel-with-sessions "._desktop#work-in-parallel-with-sessions".md).

## [​](#learn-more "#learn-more") Learn more

Each guide below covers setup and configuration for one approach:

* [Create custom subagents](./sub-agents "._sub-agents".md): define reusable specialists and control which tools they can use.
* [Manage agents with agent view](./agent-view "._agent-view".md): dispatch sessions, watch their state, and attach when one needs you.
* [Orchestrate agent teams](./agent-teams "._agent-teams".md): set up a lead and teammates, assign tasks, and review their work.
* [Orchestrate dynamic workflows](./workflows "._workflows".md): run a bundled workflow or have Claude write one that runs many subagents and verifies their findings against each other.
* [Run parallel sessions with worktrees](./worktrees "._worktrees".md): start Claude in an isolated checkout, control what gets copied in, and clean up afterward.