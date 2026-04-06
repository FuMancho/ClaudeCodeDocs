# Claude Directory

Claude Code reads instructions, settings, skills, subagents, and memory from your project directory and from `~/.claude` in your home directory. Commit project files to git to share them with your team; files in `~/.claude` are personal configuration that applies across all your projects.
Most users only edit `CLAUDE.md` and `settings.json`. The rest of the directory is optional: add skills, rules, or subagents as you need them.
This page is an interactive explorer: click files in the tree to see what each one does, when it loads, and an example. For a quick reference, see the [file reference table](#file-reference) below.


## [​](#what’s-not-shown) What’s not shown

The explorer covers the files you’ll interact with most. A few things live elsewhere:

| File | Location | Purpose |
| --- | --- | --- |
| `managed-settings.json` | System-level, varies by OS | Enterprise-enforced settings that you can’t override. See [server-managed settings](./server-managed-settings.md). |
| `CLAUDE.local.md` | Project root | Your private preferences for this project, loaded alongside CLAUDE.md. Create it manually and add it to `.gitignore`. |

## [​](#file-reference) File reference

This table lists every file the explorer covers. Project-scope files live in your repo under `.claude/` (or at the root for `CLAUDE.md`, `.mcp.json`, and `.worktreeinclude`). Global-scope files live in `~/.claude/` and apply across all projects.

Several things can override what you put in these files:

* [Managed settings](./server-managed-settings.md) deployed by your organization take precedence over everything
* CLI flags like `--permission-mode` or `--settings` override `settings.json` for that session
* Some environment variables take precedence over their equivalent setting, but this varies: check the [environment variables reference](./env-vars.md) for each one

See [settings precedence](./settings.md#settings-precedence) for the full order.

Click a filename to open that node in the explorer above.

| File | Scope | Commit | What it does | Reference |
| --- | --- | --- | --- | --- |
| [`CLAUDE.md`](#ce-claude-md) | Project and global | ✓ | Instructions loaded every session | [Memory](./memory.md) |
| [`rules/*.md`](#ce-rules) | Project and global | ✓ | Topic-scoped instructions, optionally path-gated | [Rules](./memory.md#organize-rules-with-claude/rules/) |
| [`settings.json`](#ce-settings-json) | Project and global | ✓ | Permissions, hooks, env vars, model defaults | [Settings](./settings.md) |
| [`settings.local.json`](#ce-settings-local-json) | Project only |  | Your personal overrides, auto-gitignored | [Settings scopes](./settings.md#settings-files) |
| [`.mcp.json`](#ce-mcp-json) | Project only | ✓ | Team-shared MCP servers | [MCP scopes](./mcp.md#mcp-installation-scopes) |
| [`.worktreeinclude`](#ce-worktreeinclude) | Project only | ✓ | Gitignored files to copy into new worktrees | [Worktrees](./common-workflows.md#copy-gitignored-files-to-worktrees) |
| [`skills/<name>/SKILL.md`](#ce-skills) | Project and global | ✓ | Reusable prompts invoked with `/name` or auto-invoked | [Skills](./skills.md) |
| [`commands/*.md`](#ce-commands) | Project and global | ✓ | Single-file prompts; same mechanism as skills | [Skills](./skills.md) |
| [`output-styles/*.md`](#ce-output-styles) | Project and global | ✓ | Custom system-prompt sections | [Output styles](./output-styles.md) |
| [`agents/*.md`](#ce-agents) | Project and global | ✓ | Subagent definitions with their own prompt and tools | [Subagents](./sub-agents.md) |
| [`agent-memory/<name>/`](#ce-agent-memory) | Project and global | ✓ | Persistent memory for subagents | [Persistent memory](./sub-agents.md#enable-persistent-memory) |
| [`~/.claude.json`](#ce-claude-json) | Global only |  | App state, OAuth, UI toggles, personal MCP servers | [Global config](./settings.md#global-config-settings) |
| [`projects/<project>/memory/`](#ce-global-projects) | Global only |  | Auto memory: Claude’s notes to itself across sessions | [Auto memory](./memory.md#auto-memory) |
| [`keybindings.json`](#ce-keybindings) | Global only |  | Custom keyboard shortcuts | [Keybindings](./keybindings.md) |

## [​](#check-what-loaded) Check what loaded

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

## [​](#related-resources) Related resources

* [Manage Claude’s memory](./memory.md): write and organize CLAUDE.md, rules, and auto memory
* [Configure settings](./settings.md): set permissions, hooks, environment variables, and model defaults
* [Create skills](./skills.md): build reusable prompts and workflows
* [Configure subagents](./sub-agents.md): define specialized agents with their own context