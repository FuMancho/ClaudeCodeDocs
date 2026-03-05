# Claude Code Changelog

> Curated changelog sourced from the [official Claude Code releases](https://github.com/anthropics/claude-code/releases).
> This file is maintained by Jules and updated automatically when new releases are detected.

## v2.1.69 (Latest)

- Added the `/claude-api` skill for building applications with the Claude API and Anthropic SDK
- Added `Ctrl+U` on an empty bash prompt (`!`) to exit bash mode, matching escape and backspace
- Added numeric keypad support for selecting options in Claude's interview questions
- Added optional name argument to `/remote-control` and `claude remote-control` to set a custom session title
- Added Voice STT support for 10 new languages (20 total)
- Added effort level display (e.g., "with low effort") to the logo and spinner
- Added agent name display in terminal title when using `claude --agent`
- Added `sandbox.enableWeakerNetworkIsolation` setting (macOS only) to allow Go programs like `gh`, `gcloud`, and `terraform` to verify TLS certificates
- Added `includeGitInstructions` setting to remove built-in commit and PR workflow instructions from Claude's system prompt
- Added `/reload-plugins` command to activate pending plugin changes without restarting
- Added a one-time startup prompt suggesting Claude Code Desktop on macOS and Windows
- Added `${CLAUDE_SKILL_DIR}` variable for skills to reference their own directory in SKILL.md content
- Added `InstructionsLoaded` hook event that fires when CLAUDE.md or .claude/rules/*.md files are loaded into context
- Added `agent_id` (for subagents) and `agent_type` (for subagents and `--agent`) to hook events
- Fixed a security issue where nested skill discovery could load skills from gitignored directories
- Fixed trust dialog silently enabling all `.mcp.json` servers on first run
- Fixed macOS keychain corruption when using multiple OAuth MCP servers
- Fixed ghost dotfiles appearing as untracked files in the working directory after sandboxed Bash commands on Linux
- Fixed Shift+Enter printing `[27;2;13~` instead of inserting a newline in Ghostty over SSH

## v2.1.68

- Opus 4.6 now defaults to medium effort for Max and Team subscribers. Medium effort works well for most tasks — it's the sweet spot between speed and thoroughness. You can change this anytime with
- /model
- Re-introduced the "ultrathink" keyword to enable high effort for the next turn
- Removed Opus 4 and 4.1 from Claude Code on the first-party API — users with these models pinned are automatically moved to Opus 4.6

## v2.1.66

- Reduced spurious error logging

## v2.1.63

### New Features
- Added `/simplify` and `/batch` bundled slash commands
- Project configs & auto memory now shared across git worktrees of the same repository
- Added `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var to opt out from making claude.ai MCP servers available
- Improved `/model` command to show the currently active model in the slash command menu
- Added HTTP hooks — POST JSON to a URL and receive JSON instead of running a shell command
- Added manual URL paste fallback during MCP OAuth authentication
- Added "Always copy full response" option to the `/copy` picker
- VS Code: Added session rename and remove actions to the sessions list

### Bug Fixes
- Fixed local slash command output (e.g. `/cost`) appearing as user-sent messages instead of system messages
- Fixed listener leak in bridge polling loop
- Fixed listener leak in MCP OAuth flow cleanup
- Fixed memory leak when navigating hooks configuration menu
- Fixed listener leak in interactive permission handler during auto-approvals
- Fixed file count cache ignoring glob ignore patterns
- Fixed memory leak in bash command prefix cache
- Fixed MCP tool/resource cache leak on server reconnect
- Fixed IDE host IP detection cache incorrectly sharing results across ports
- Fixed WebSocket listener leak on transport reconnect
- Fixed memory leak in git root detection cache (unbounded growth in long-running sessions)
- Fixed memory leak in JSON parsing cache (grew unbounded over long sessions)
- Fixed memory leak where long-running teammates retained all messages after compaction
- Fixed MCP server fetch caches not cleared on disconnect
- Improved memory usage in long sessions with subagents by stripping heavy progress message payloads during context compaction
- Fixed `/clear` not resetting cached skills (stale skill content could persist)
- Fixed race condition in REPL bridge where new messages interleaved with historical messages during initial connection flush
- VS Code: Fixed remote sessions not appearing in conversation history

---

## v2.1.62

### Bug Fixes
- Fixed prompt suggestion cache regression that reduced cache hit rates

---

## v2.1.61

### Bug Fixes
- Fixed concurrent writes corrupting config file on Windows

---

## v2.1.59

### New Features
- Claude automatically saves useful context to auto-memory (manage with `/memory`)
- Added `/copy` command — interactive picker for selecting individual code blocks or full response
- Improved "always allow" prefix suggestions for compound bash commands (e.g. `cd /tmp && git fetch && git push`)

### Improvements
- Improved ordering of short task lists
- Improved memory usage in multi-agent sessions by releasing completed subagent task state

### Bug Fixes
- Fixed MCP OAuth token refresh race condition when running multiple Claude Code instances simultaneously
- Fixed shell commands not showing a clear error message when the working directory has been deleted

---

## v2.1.58

### Changes
- Expanded Remote Control to more users

---

*See [full release history](https://github.com/anthropics/claude-code/releases) for earlier versions.*
