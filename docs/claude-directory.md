Claude Code reads instructions, settings, skills, subagents, and memory from your project directory and from `~/.claude` in your home directory. Commit project files to git to share them with your team; files in `~/.claude` are personal configuration that applies across all your projects.
If you set [`CLAUDE_CONFIG_DIR`](./env-vars.md), every `~/.claude` path on this page lives under that directory instead.
Most users only edit `CLAUDE.md` and `settings.json`. The rest of the directory is optional: add skills, rules, or subagents as you need them.
This page is an interactive explorer: click files in the tree to see what each one does, when it loads, and an example. For a quick reference, see the [file reference table](#file-reference #file-reference) below.


## [​](#what’s-not-shown #what’s-not-shown) What’s not shown

The explorer covers files you author and edit. A few related files live elsewhere:

| File | Location | Purpose |
| --- | --- | --- |
| `managed-settings.json` | System-level, varies by OS | Enterprise-enforced settings that you can’t override. See [server-managed settings](./server-managed-settings.md). |
| `CLAUDE.local.md` | Project root | Your private preferences for this project, loaded alongside CLAUDE.md. Create it manually and add it to `.gitignore`. |
| Installed plugins | `~/.claude/plugins/` | Cloned marketplaces, installed plugin versions, and per-plugin data, managed by `claude plugin` commands. Orphaned versions are deleted 7 days after a plugin update or uninstall. See [plugin caching](./plugins-reference.md#plugin-caching-and-file-resolution). |

`~/.claude` also holds data Claude Code writes as you work: transcripts, prompt history, file snapshots, caches, and logs. See [application data](#application-data #application-data) below.

## [​](#file-reference #file-reference) File reference

This table lists every file the explorer covers. Project-scope files live in your repo under `.claude/` (or at the root for `CLAUDE.md`, `.mcp.json`, and `.worktreeinclude`). Global-scope files live in `~/.claude/` and apply across all projects.

Several things can override what you put in these files:

* [Managed settings](./server-managed-settings.md) deployed by your organization take precedence over everything
* CLI flags like `--permission-mode` or `--settings` override `settings.json` for that session
* Some environment variables take precedence over their equivalent setting, but this varies: check the [environment variables reference](./env-vars.md) for each one

See [settings precedence](./settings.md#settings-precedence) for the full order.

Click a filename to open that node in the explorer above.

| File | Scope | Commit | What it does | Reference |
| --- | --- | --- | --- | --- |
| [`CLAUDE.md`](#ce-claude-md #ce-claude-md) | Project and global | ✓ | Instructions loaded every session | [Memory](./memory.md) |
| [`rules/*.md`](#ce-rules #ce-rules) | Project and global | ✓ | Topic-scoped instructions, optionally path-gated | [Rules](./.md) |
| [`settings.json`](#ce-settings-json #ce-settings-json) | Project and global | ✓ | Permissions, hooks, env vars, model defaults | [Settings](./settings.md) |
| [`settings.local.json`](#ce-settings-local-json #ce-settings-local-json) | Project only |  | Your personal overrides, auto-gitignored | [Settings scopes](./settings.md#settings-files) |
| [`.mcp.json`](#ce-mcp-json #ce-mcp-json) | Project only | ✓ | Team-shared MCP servers | [MCP scopes](./mcp.md#mcp-installation-scopes) |
| [`.worktreeinclude`](#ce-worktreeinclude #ce-worktreeinclude) | Project only | ✓ | Gitignored files to copy into new worktrees | [Worktrees](./common-workflows.md#copy-gitignored-files-to-worktrees) |
| [`skills/<name>/SKILL.md`](#ce-skills #ce-skills) | Project and global | ✓ | Reusable prompts invoked with `/name` or auto-invoked | [Skills](./skills.md) |
| [`commands/*.md`](#ce-commands #ce-commands) | Project and global | ✓ | Single-file prompts; same mechanism as skills | [Skills](./skills.md) |
| [`output-styles/*.md`](#ce-output-styles #ce-output-styles) | Project and global | ✓ | Custom system-prompt sections | [Output styles](./output-styles.md) |
| [`agents/*.md`](#ce-agents #ce-agents) | Project and global | ✓ | Subagent definitions with their own prompt and tools | [Subagents](./sub-agents.md) |
| [`agent-memory/<name>/`](#ce-agent-memory #ce-agent-memory) | Project and global | ✓ | Persistent memory for subagents | [Persistent memory](./sub-agents.md#enable-persistent-memory) |
| [`~/.claude.json`](#ce-claude-json #ce-claude-json) | Global only |  | App state, OAuth, UI toggles, personal MCP servers | [Global config](./settings.md#global-config-settings) |
| [`projects/<project>/memory/`](#ce-global-projects #ce-global-projects) | Global only |  | Auto memory: Claude’s notes to itself across sessions | [Auto memory](./memory.md#auto-memory) |
| [`keybindings.json`](#ce-keybindings #ce-keybindings) | Global only |  | Custom keyboard shortcuts | [Keybindings](./keybindings.md) |

## [​](#check-what-loaded #check-what-loaded) Check what loaded

The explorer shows what files can exist. To see what actually loaded in your current session, use these commands:

| Command | Shows |
| --- | --- |
| `/context` | Token usage by category: system prompt, memory files, skills, MCP tools, and messages |
| `/memory` | Which CLAUDE.md and rules files loaded, plus auto-memory entries |
| `/agents` | Configured subagents and their settings |
| `/hooks` | Active hook configurations |
| `/mcp` | Connected MCP servers and their status |
| `/skills` | Available skills from project, user, and plugin sources |
| `/permissions` | Current allow and deny rules |
| `/doctor` | Installation and configuration diagnostics |

Run `/context` first for the overview, then the specific command for the area you want to investigate.

## [​](#application-data #application-data) Application data

Beyond the config you author, `~/.claude` holds data Claude Code writes during sessions. These files are plaintext. Anything that passes through a tool lands in a transcript on disk: file contents, command output, pasted text.

### [​](#cleaned-up-automatically #cleaned-up-automatically) Cleaned up automatically

Files in the paths below are deleted on startup once they’re older than [`cleanupPeriodDays`](./settings.md#available-settings). The default is 30 days.

| Path under `~/.claude/` | Contents |
| --- | --- |
| `projects/<project>/<session>.jsonl` | Full conversation transcript: every message, tool call, and tool result |
| `projects/<project>/<session>/tool-results/` | Large tool outputs spilled to separate files |
| `file-history/<session>/` | Pre-edit snapshots of files Claude changed, used for [checkpoint restore](./checkpointing.md) |
| `plans/` | Plan files written during [plan mode](./permission-modes.md#analyze-before-you-edit-with-plan-mode) |
| `debug/` | Per-session debug logs, written only when you start with `--debug` or run `/debug` |
| `paste-cache/`, `image-cache/` | Contents of large pastes and attached images |
| `session-env/` | Per-session environment metadata |

### [​](#kept-until-you-delete-them #kept-until-you-delete-them) Kept until you delete them

The following paths are not covered by automatic cleanup and persist indefinitely.

| Path under `~/.claude/` | Contents |
| --- | --- |
| `history.jsonl` | Every prompt you’ve typed, with timestamp and project path. Used for up-arrow recall. |
| `stats-cache.json` | Aggregated token and cost counts shown by `/cost` |
| `backups/` | Timestamped copies of `~/.claude.json` taken before config migrations |
| `todos/` | Legacy per-session task lists. No longer written by current versions; safe to delete. |

`shell-snapshots/` holds runtime files removed when the session exits cleanly. Other small cache and lock files appear depending on which features you use and are safe to delete.

### [​](#plaintext-storage #plaintext-storage) Plaintext storage

Transcripts and history are not encrypted at rest. OS file permissions are the only protection. If a tool reads a `.env` file or a command prints a credential, that value is written to `projects/<project>/<session>.jsonl`. To reduce exposure:

* Lower `cleanupPeriodDays` to shorten how long transcripts are kept
* In non-interactive mode, pass `--no-session-persistence` alongside `-p` to skip writing transcripts entirely. In the Agent SDK, set `persistSession: false`. There is no interactive-mode equivalent.
* Use [permission rules](./permissions.md) to deny reads of credential files

### [​](#clear-local-data #clear-local-data) Clear local data

You can delete any of the application-data paths above at any time. New sessions are unaffected. The table below shows what you lose for past sessions.

| Delete | You lose |
| --- | --- |
| `~/.claude/projects/` | Resume, continue, and rewind for past sessions |
| `~/.claude/history.jsonl` | Up-arrow prompt recall |
| `~/.claude/file-history/` | Checkpoint restore for past sessions |
| `~/.claude/stats-cache.json` | Historical totals shown by `/cost` |
| `~/.claude/backups/` | Rollback copies of `~/.claude.json` from past config migrations |
| `~/.claude/debug/`, `~/.claude/plans/`, `~/.claude/paste-cache/`, `~/.claude/image-cache/`, `~/.claude/session-env/` | Nothing user-facing |
| `~/.claude/todos/` | Nothing. Legacy directory not written by current versions. |

Don’t delete `~/.claude.json`, `~/.claude/settings.json`, or `~/.claude/plugins/`: those hold your auth, preferences, and installed plugins.

## [​](#related-resources #related-resources) Related resources

* [Manage Claude’s memory](./memory.md): write and organize CLAUDE.md, rules, and auto memory
* [Configure settings](./settings.md): set permissions, hooks, environment variables, and model defaults
* [Create skills](./skills.md): build reusable prompts and workflows
* [Configure subagents](./sub-agents.md): define specialized agents with their own context