# Commands

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt "https://code.claude.com/docs/llms.txt")
>
> Use this file to discover all available pages before exploring further.

Commands control Claude Code from inside a session. They provide a quick way to switch models, manage permissions, clear context, run a workflow, and more.
Type `/` to see every command available to you, or type `/` followed by letters to filter.
A command is only recognized at the start of your message. Text that follows the command name is passed to it as arguments.

## [​](#commands-across-a-typical-workflow "#commands-across-a-typical-workflow") Commands across a typical workflow

Most commands are useful at a specific point in a session, from setting up a project to shipping a change.
**First session in a repo.** Run `/init` to generate a starter `CLAUDE.md`, then `/memory` to refine it. Use `/mcp` and `/agents` to set up any servers or subagents the project needs, and `/permissions` to set the approval rules you want.
**During a task.** `/plan` switches into plan mode before a large change. `/model` and `/effort` adjust how much reasoning you’re spending. When the conversation gets long, `/context` shows where the window is going and `/compact` summarizes it down; use `/btw` for a quick aside that shouldn’t bloat history.
**Running work in parallel.** `/agents` opens the manager for the [subagents](./sub-agents "_sub-agents".md) Claude can delegate side tasks to, and `/tasks` lists what’s running in the background of the current session. `/background` detaches the whole session to keep running as a [background agent](./agent-view "_agent-view".md) and frees your terminal. For a large change that spans the codebase, `/batch` decomposes it into independent units and runs each in its own [worktree](./worktrees "_worktrees".md). See [Run agents in parallel](./agents "_agents".md) for how these approaches relate.
**Before you ship.** `/diff` shows what changed, `/code-review` checks the diff for correctness bugs, and `/review` or `/security-review` give a deeper read-only pass.
**Between sessions.** `/clear` starts fresh on a new task while keeping project memory. `/resume` and `/branch` let you return to or fork an earlier conversation. `/teleport` pulls a web session into this terminal, and `/remote-control` lets you continue this local session from another device.
**When something is wrong.** `/rewind` rolls code and conversation back to a checkpoint, or summarizes part of the conversation. `/doctor` and `/debug` diagnose install and runtime issues, and `/feedback` reports a bug with session context attached.

## [​](#all-commands "#all-commands") All commands

The table below lists all the commands included in Claude Code. Entries marked **[Skill](./skills#bundled-skills "_skills#bundled-skills".md)** are bundled skills. They use the same mechanism as skills you write yourself: a prompt handed to Claude, which Claude can also invoke automatically when relevant. Everything else is a built-in command whose behavior is coded into the CLI. To add your own commands, see [skills](./skills "_skills".md).
In the table below, `<arg>` indicates a required argument and `[arg]` indicates an optional one.

Not every command appears for every user. Availability depends on your platform, plan, and environment. For example, `/desktop` only shows on macOS and Windows when signed in with a Claude subscription, and `/upgrade` only shows on Pro and Max plans.

| Command | Purpose |
| --- | --- |
| `/add-dir <path>` | Add a working directory for file access during the current session. Most `.claude/` configuration is [not discovered](./permissions#additional-directories-grant-file-access-not-configuration "_permissions#additional-directories-grant-file-access-not-configuration".md) from the added directory. You can later resume the session from the added directory with `--continue` or `--resume` |
| `/agents` | Manage [agent](./sub-agents "_sub-agents".md) configurations |
| `/autofix-pr [prompt]` | Spawn a [Claude Code on the web](./claude-code-on-the-web#auto-fix-pull-requests "_claude-code-on-the-web#auto-fix-pull-requests".md) session that watches the current branch’s PR and pushes fixes when CI fails or reviewers leave comments. Detects the open PR from your checked-out branch with `gh pr view`; to watch a different PR, check out its branch first. By default the remote session is told to fix every CI failure and review comment; pass a prompt to give it different instructions, for example `/autofix-pr only fix lint and type errors`. Requires the `gh` CLI and access to [Claude Code on the web](./claude-code-on-the-web#who-can-use-claude-code-on-the-web "_claude-code-on-the-web#who-can-use-claude-code-on-the-web".md) |
| `/background [prompt]` | Detach the current session to run as a [background agent](./agent-view "_agent-view".md) and free this terminal. Pass a prompt to send one more instruction before detaching. Monitor the session with `claude agents`. Alias: `/bg` |
| `/batch <instruction>` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Orchestrate large-scale changes across a codebase in parallel. Researches the codebase, decomposes the work into 5 to 30 independent units, and presents a plan. Once approved, spawns one [background subagent](./sub-agents#run-subagents-in-foreground-or-background "_sub-agents#run-subagents-in-foreground-or-background".md) per unit in an isolated [git worktree](./worktrees "_worktrees".md). Each subagent implements its unit, runs tests, and opens a pull request. Requires a git repository. Example: `/batch migrate src/ from Solid to React` |
| `/branch [name]` | Create a branch of the current conversation at this point. Switches you into the branch and preserves the original, which you can return to with `/resume`. Alias: `/fork`. When [`CLAUDE_CODE_FORK_SUBAGENT`](./env-vars "_env-vars".md) is set, `/fork` instead spawns a [forked subagent](./sub-agents#fork-the-current-conversation "_sub-agents#fork-the-current-conversation".md) and is no longer an alias for this command |
| `/btw <question>` | Ask a quick [side question](./interactive-mode#side-questions-with-%2Fbtw "_interactive-mode#side-questions-with-%2Fbtw".md) without adding to the conversation |
| `/chrome` | Configure [Claude in Chrome](./chrome "_chrome".md) settings |
| `/claude-api [migrate|managed-agents-onboard]` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Load Claude API reference material for your project’s language (Python, TypeScript, Java, Go, Ruby, C#, PHP, or cURL) and Managed Agents reference. Covers tool use, streaming, batches, structured outputs, and common pitfalls. Also activates automatically when your code imports `anthropic` or `@anthropic-ai/sdk`. Run `/claude-api migrate` to upgrade existing Claude API code to a newer model: Claude asks which files to scan and which model to target, then updates model IDs, thinking configuration, and other parameters that changed between versions. Run `/claude-api managed-agents-onboard` for an interactive walkthrough that creates a new Managed Agent from scratch |
| `/clear [name]` | Start a new conversation with empty context. The previous conversation stays available in `/resume`. Pass a name to label the previous conversation in the `/resume` picker. To free up context while continuing the same conversation, use `/compact` instead. Aliases: `/reset`, `/new` |
| `/code-review [low|medium|high|xhigh|max] [--comment] [target]` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Review the current diff for correctness bugs and report findings without editing files. Lower [effort levels](./model-config#adjust-effort-level "_model-config#adjust-effort-level".md) return fewer, higher-confidence findings, while `high` through `max` give broader coverage and may include uncertain findings. Without an effort argument, the review uses the session’s current effort. Pass `--comment` to post findings as inline comments on the current GitHub PR. Pass a path or PR reference to review a specific target. Formerly `/simplify`, which still works as an alias |
| `/color [color|default]` | Set the prompt bar color for the current session. Available colors: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`. Use `default` to reset, or run with no argument to pick a random color. When [Remote Control](./remote-control "_remote-control".md) is connected, the color syncs to claude.ai/code |
| `/compact [instructions]` | Free up context by summarizing the conversation so far. Optionally pass focus instructions for the summary. See [how compaction handles rules, skills, and memory files](./context-window#what-survives-compaction "_context-window#what-survives-compaction".md) |
| `/config` | Open the [Settings](./settings "_settings".md) interface to adjust theme, model, [output style](./output-styles "_output-styles".md), and other preferences. Alias: `/settings` |
| `/context [all]` | Visualize current context usage as a colored grid. Shows optimization suggestions for context-heavy tools, memory bloat, and capacity warnings. In [fullscreen mode](./fullscreen "_fullscreen".md) the per-item breakdown is collapsed to keep the grid visible. Pass `all` to expand it |
| `/copy [N]` | Copy the last assistant response to clipboard. Pass a number `N` to copy the Nth-latest response: `/copy 2` copies the second-to-last. When code blocks are present, shows an interactive picker to select individual blocks or the full response. Press `w` in the picker to write the selection to a file instead of the clipboard, which is useful over SSH |
| `/cost` | Alias for `/usage` |
| `/debug [description]` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Enable debug logging for the current session and troubleshoot issues by reading the session debug log. Debug logging is off by default unless you started with `claude --debug`, so running `/debug` mid-session starts capturing logs from that point forward. Optionally describe the issue to focus the analysis |
| `/desktop` | Continue the current session in the Claude Code Desktop app. Requires macOS or Windows and a Claude subscription. Alias: `/app` |
| `/diff` | Open an interactive diff viewer showing uncommitted changes and per-turn diffs. Use left/right arrows to switch between the current git diff and individual Claude turns, and up/down to browse files |
| `/doctor` | Diagnose and verify your Claude Code installation and settings. Results show with status icons. Press `f` to have Claude fix any reported issues |
| `/effort [level|auto]` | Set the model [effort level](./model-config#adjust-effort-level "_model-config#adjust-effort-level".md). Accepts `low`, `medium`, `high`, `xhigh`, or `max`; available levels depend on the model and `max` is session-only. `auto` resets to the model default. Without an argument, opens an interactive slider; use left and right arrows to pick a level and `Enter` to apply. Takes effect immediately without waiting for the current response to finish |
| `/exit` | Exit the CLI. In an attached [background session](./agent-view#attach-to-a-session "_agent-view#attach-to-a-session".md), this detaches and the session keeps running. Alias: `/quit` |
| `/export [filename]` | Export the current conversation as plain text. With a filename, writes directly to that file. Without, opens a dialog to copy to clipboard or save to a file |
| `/fast [on|off]` | Toggle [fast mode](./fast-mode "_fast-mode".md) on or off |
| `/feedback [report]` | Submit feedback, report a bug, or share your conversation. Aliases: `/bug`, `/share` |
| `/fewer-permission-prompts` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project `.claude/settings.json` to reduce permission prompts |
| `/focus` | Toggle the focus view, which shows only your last prompt, a one-line tool-call summary with edit diffstats, and the final response. The selection persists across sessions; set [`viewMode`](./settings#available-settings "_settings#available-settings".md) in settings to override it. Only available in [fullscreen rendering](./fullscreen "_fullscreen".md) |
| `/goal [condition|clear]` | Set a [goal](./goal "_goal".md): Claude keeps working across turns until the condition is met. With no argument, shows the current or most recently achieved goal. `clear`, `stop`, `off`, `reset`, `none`, or `cancel` removes an active goal early |
| `/heapdump` | Write a JavaScript heap snapshot and a memory breakdown to `~/Desktop`, or your home directory on Linux without a Desktop folder, for diagnosing high memory usage. See [troubleshooting](./troubleshooting#high-cpu-or-memory-usage "_troubleshooting#high-cpu-or-memory-usage".md) |
| `/help` | Show help and available commands |
| `/hooks` | View [hook](./hooks "_hooks".md) configurations for tool events |
| `/ide` | Manage IDE integrations and show status |
| `/init` | Initialize project with a `CLAUDE.md` guide. Set `CLAUDE_CODE_NEW_INIT=1` for an interactive flow that also walks through skills, hooks, and personal memory files |
| `/insights` | Generate a report analyzing your Claude Code sessions, including project areas, interaction patterns, and friction points |
| `/install-github-app` | Set up the [Claude GitHub Actions](./github-actions "_github-actions".md) app for a repository. Walks you through selecting a repo and configuring the integration |
| `/install-slack-app` | Install the Claude Slack app. Opens a browser to complete the OAuth flow |
| `/keybindings` | Open or create your keybindings configuration file |
| `/login` | Sign in to your Anthropic account |
| `/logout` | Sign out from your Anthropic account |
| `/loop [interval] [prompt]` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Run a prompt repeatedly while the session stays open. Omit the interval and Claude self-paces between iterations. Omit the prompt and, [where available](./scheduled-tasks#run-the-built-in-maintenance-prompt "_scheduled-tasks#run-the-built-in-maintenance-prompt".md), Claude runs an autonomous maintenance check or the prompt in `.claude/loop.md`. Example: `/loop 5m check if the deploy finished`. See [Run prompts on a schedule](./scheduled-tasks "_scheduled-tasks".md). Alias: `/proactive` |
| `/mcp` | Manage MCP server connections and OAuth authentication |
| `/memory` | Edit `CLAUDE.md` memory files, enable or disable [auto-memory](./memory#auto-memory "_memory#auto-memory".md), and view auto-memory entries |
| `/mobile` | Show QR code to download the Claude mobile app. Aliases: `/ios`, `/android` |
| `/model [model]` | Set the AI model for the current session. For models that support it, use left/right arrows to [adjust effort level](./model-config#adjust-effort-level "_model-config#adjust-effort-level".md). With no argument, opens a picker; press `d` on a row to also save that model as the default for new sessions. The picker asks for confirmation when the conversation has prior output, since the next response re-reads the full history without cached context. Once confirmed, the change applies without waiting for the current response to finish |
| `/passes` | Share a free week of Claude Code with friends. Only visible if your account is eligible |
| `/permissions` | Manage allow, ask, and deny rules for tool permissions. Opens an interactive dialog where you can view rules by scope, add or remove rules, manage working directories, and review [recent auto mode denials](./auto-mode-config#review-denials "_auto-mode-config#review-denials".md). Alias: `/allowed-tools` |
| `/plan [description]` | Enter plan mode directly from the prompt. Pass an optional description to enter plan mode and immediately start with that task, for example `/plan fix the auth bug` |
| `/plugin` | Manage Claude Code [plugins](./plugins "_plugins".md) |
| `/powerup` | Discover Claude Code features through quick interactive lessons with animated demos |
| `/pr-comments [PR]` | Removed in v2.1.91. Ask Claude directly to view pull request comments instead. On earlier versions, fetches and displays comments from a GitHub pull request; automatically detects the PR for the current branch, or pass a PR URL or number. Requires the `gh` CLI |
| `/privacy-settings` | View and update your privacy settings. Only available for Pro and Max plan subscribers |
| `/radio` | Open Claude FM lo-fi radio in your browser. Prints the stream URL when no browser is available. Not available on Bedrock, Vertex, or Foundry |
| `/recap` | Generate a one-line summary of the current session on demand. See [Session recap](./interactive-mode#session-recap "_interactive-mode#session-recap".md) for the automatic recap that appears after you’ve been away |
| `/release-notes` | View the changelog in an interactive version picker. Select a specific version to see its release notes, or choose to show all versions |
| `/reload-plugins` | Reload all active [plugins](./plugins "_plugins".md) to apply pending changes without restarting. Reports counts for each reloaded component and flags any load errors |
| `/remote-control` | Make this session available for [remote control](./remote-control "_remote-control".md) from claude.ai. Alias: `/rc` |
| `/remote-env` | Configure the default remote environment for [web sessions started with `--remote`](./claude-code-on-the-web#configure-your-environment "_claude-code-on-the-web#configure-your-environment".md) |
| `/rename [name]` | Rename the current session and show the name on the prompt bar. Without a name, auto-generates one from conversation history |
| `/resume [session]` | Resume a conversation by ID or name, or open the session picker. As of v2.1.144, [background sessions](./agent-view "_agent-view".md) appear in the picker marked with `bg`. Alias: `/continue` |
| `/review [PR]` | Review a pull request locally in your current session. For a deeper cloud-based review, see [`/ultrareview`](./ultrareview "_ultrareview".md) |
| `/rewind` | Rewind the conversation and/or code to a previous point, or summarize from a selected message. See [checkpointing](./checkpointing "_checkpointing".md). Aliases: `/checkpoint`, `/undo` |
| `/run` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Launch and drive your project’s app to see a change working in the running app, not just in tests. See [Run and verify your app](./skills#run-and-verify-your-app "_skills#run-and-verify-your-app".md). Requires Claude Code v2.1.145 or later |
| `/run-skill-generator` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Teach `/run` and `/verify` how to build, launch, and drive your project’s app from a clean environment by writing a per-project [skill](./skills#run-and-verify-your-app "_skills#run-and-verify-your-app".md). Requires Claude Code v2.1.145 or later |
| `/sandbox` | Toggle [sandbox mode](./sandboxing "_sandboxing".md). Available on supported platforms only |
| `/schedule [description]` | Create, update, list, or run [routines](./routines "_routines".md), which execute on Anthropic-managed cloud infrastructure. Claude walks you through the setup conversationally. Alias: `/routines` |
| `/scroll-speed` | Adjust mouse wheel [scroll speed](./fullscreen#mouse-wheel-scrolling "_fullscreen#mouse-wheel-scrolling".md) interactively, with a ruler you can scroll while the dialog is open to preview the change. Available in [fullscreen rendering](./fullscreen "_fullscreen".md) only and not in the JetBrains IDE terminal |
| `/security-review` | Analyze pending changes on the current branch for security vulnerabilities. Reviews the git diff and identifies risks like injection, auth issues, and data exposure |
| `/setup-bedrock` | Configure [Amazon Bedrock](./amazon-bedrock "_amazon-bedrock".md) authentication, region, and model pins through an interactive wizard. Only visible when `CLAUDE_CODE_USE_BEDROCK=1` is set. First-time Bedrock users can also access this wizard from the login screen |
| `/setup-vertex` | Configure [Google Vertex AI](./google-vertex-ai "_google-vertex-ai".md) authentication, project, region, and model pins through an interactive wizard. Only visible when `CLAUDE_CODE_USE_VERTEX=1` is set. First-time Vertex AI users can also access this wizard from the login screen |
| `/skills` | List available [skills](./skills "_skills".md). Press `t` to sort by token count. Press `Space` to [hide a skill from Claude or the `/` menu](./skills#override-skill-visibility-from-settings "_skills#override-skill-visibility-from-settings".md), then `Enter` to save |
| `/stats` | Alias for `/usage`. Opens on the Stats tab |
| `/status` | Open the Settings interface (Status tab) showing version, model, account, and connectivity. Works while Claude is responding, without waiting for the current response to finish |
| `/statusline` | Configure Claude Code’s [status line](./statusline "_statusline".md). Describe what you want, or run without arguments to auto-configure from your shell prompt |
| `/stickers` | Order Claude Code stickers |
| `/stop` | Stop the current [background session](./agent-view "_agent-view".md). Only available while attached to a background session; the transcript and any worktree are kept. To detach without stopping, use `/exit` or press `←` |
| `/tasks` | List and manage background tasks. Also available as `/bashes` |
| `/team-onboarding` | Generate a team onboarding guide from your Claude Code usage history. Claude analyzes your sessions, commands, and MCP server usage from the past 30 days and produces a markdown guide a teammate can paste as a first message to get set up quickly. For claude.ai subscribers on Pro, Max, Team, and Enterprise plans, also returns a share link teammates can open directly in Claude Code |
| `/teleport` | Pull a [Claude Code on the web](./claude-code-on-the-web#from-web-to-terminal "_claude-code-on-the-web#from-web-to-terminal".md) session into this terminal: opens a picker, then fetches the branch and conversation. Also available as `/tp`. Requires a claude.ai subscription |
| `/terminal-setup` | Configure terminal keybindings for Shift+Enter and other shortcuts. Only visible in terminals that need it, like VS Code, Cursor, Windsurf, Alacritty, or Zed |
| `/theme` | Change the color theme. Includes an `auto` option that matches your terminal’s light or dark background, light and dark variants, colorblind-accessible (daltonized) themes, ANSI themes that use your terminal’s color palette, and any [custom themes](./terminal-config#create-a-custom-theme "_terminal-config#create-a-custom-theme".md) from `~/.claude/themes/` or plugins. Select **New custom theme…** to create one |
| `/tui [default|fullscreen]` | Set the terminal UI renderer and relaunch into it with your conversation intact. `fullscreen` enables the [flicker-free alt-screen renderer](./fullscreen "_fullscreen".md). With no argument, prints the active renderer |
| `/ultraplan <prompt>` | Draft a plan in an [ultraplan](./ultraplan "_ultraplan".md) session, review it in your browser, then execute remotely or send it back to your terminal |
| `/ultrareview [PR]` | Run a deep, multi-agent code review in a cloud sandbox with [ultrareview](./ultrareview "_ultrareview".md). Includes 3 free runs on Pro and Max, then requires [usage credits](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans "https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans") |
| `/upgrade` | Open the upgrade page to switch to a higher plan tier |
| `/usage` | Show session cost, plan usage limits, and activity stats. See the [cost tracking guide](./costs#using-the-%2Fusage-command "_costs#using-the-%2Fusage-command".md) for subscription-specific details. `/cost` and `/stats` are aliases |
| `/usage-credits` | Configure usage credits to keep working when you hit a limit. Previously `/extra-usage` |
| `/verify` | **[Skill](./skills#bundled-skills "_skills#bundled-skills".md).** Confirm a code change does what it should by building your project’s app, running it, and observing the result, rather than relying on tests or type checks. See [Run and verify your app](./skills#run-and-verify-your-app "_skills#run-and-verify-your-app".md). Requires Claude Code v2.1.145 or later |
| `/vim` | Removed in v2.1.92. To toggle between Vim and Normal editing modes, use `/config` → Editor mode |
| `/voice [hold|tap|off]` | Toggle [voice dictation](./voice-dictation "_voice-dictation".md), or enable it in a specific mode. Requires a Claude.ai account |
| `/web-setup` | Connect your GitHub account to [Claude Code on the web](./web-quickstart#connect-from-your-terminal "_web-quickstart#connect-from-your-terminal".md) using your local `gh` CLI credentials. `/schedule` prompts for this automatically if GitHub isn’t connected |

## [​](#mcp-prompts "#mcp-prompts") MCP prompts

MCP servers can expose prompts that appear as commands. These use the format `/mcp__<server>__<prompt>` and are dynamically discovered from connected servers. See [MCP prompts](./mcp#use-mcp-prompts-as-commands "_mcp#use-mcp-prompts-as-commands".md) for details.

## [​](#see-also "#see-also") See also

* [Skills](./skills "_skills".md): create your own commands
* [Interactive mode](./interactive-mode "_interactive-mode".md): keyboard shortcuts, Vim mode, and command history
* [CLI reference](./cli-reference "_cli-reference".md): launch-time flags