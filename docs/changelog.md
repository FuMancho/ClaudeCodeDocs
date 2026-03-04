# Claude Code Changelog

> Curated changelog sourced from the [official Claude Code releases](https://github.com/anthropics/claude-code/releases).
> This file is maintained by Jules and updated automatically when new releases are detected.

## v2.1.64 (Latest)

### New Features
- Added persistent session support to claude server : connections with a session_key survive WebSocket disconnects and can be resumed across server restarts. New flags: --workspace , --idle-timeout , --max-sessions .
- Added claude remote-control server for hosting multiple concurrent sessions with worktree or same-dir isolation
- Added optional name argument to /remote-control and claude remote-control ( /remote-control My Project or --name "My Project" ) to set a custom session title visible in claude.ai/code
- Added Voice STT support for 10 new languages (20 total) — Russian, Polish, Turkish, Dutch, Ukrainian, Greek, Czech, Danish, Swedish, Norwegian
- Added effort level display (e.g., "with low effort") to the logo and spinner, making it easier to see which effort setting is active
- Added agent name display in terminal title when using claude --agent
- Added sandbox.enableWeakerNetworkIsolation setting (macOS only) to allow Go programs like gh , gcloud , and terraform to verify TLS certificates when using a custom MITM proxy with httpProxyPort
- Added includeGitInstructions setting (and CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS env var) to remove built-in commit and PR workflow instructions from Claude's system prompt
- Added /reload-plugins command to activate pending plugin changes without restarting
- Added a one-time startup prompt suggesting Claude Code Desktop on macOS and Windows (max 3 showings, dismissible)
- Added ${CLAUDE_SKILL_DIR} variable for skills to reference their own directory in SKILL.md content
- Added InstructionsLoaded hook event that fires when CLAUDE.md or .claude/rules/*.md files are loaded into context
- Added agent_id (for subagents) and agent_type (for subagents and --agent ) to hook events
- Added worktree field to status line hook commands with name, path, branch, and original repo directory when running in a --worktree session
- Added scheduled skill triggers to the background tasks indicator with a detail dialog showing schedule and countdown
- Added pluginTrustMessage in managed settings to append organization-specific context to the plugin trust warning shown before installation
- Added policy limit fetching (e.g., remote control restrictions) for Team plan OAuth users, not just Enterprise
- Added pathPattern to strictKnownMarketplaces for regex-matching file/directory marketplace sources alongside hostPattern restrictions
- Added plugin source type git-subdir to point to a subdirectory within a git repo
- Added CLAUDE_CODE_AUTO_MEMORY_PATH env var to override the auto-memory directory with a direct path
- Added oauth.authServerMetadataUrl config option for
- MCP servers to specify a custom OAuth metadata discovery URL when standard discovery fails
- MCP servers with OAuth (regression from 2.1.x)
- MCP tools from a server
- MCP binary content handling: tools returning PDFs, Office documents, or audio now save decoded bytes to disk with the correct file extension instead of dumping raw base64 into the conversation context. WebFetch also saves binary responses alongside its summary.

### Improvements
- Improved memory usage in long sessions by stabilizing onSubmit across message updates
- Improved LSP tool rendering and memory context building to no longer read entire files
- Improved session upload and memory sync to avoid reading large files into memory before size/binary checks
- Improved file operation performance by avoiding reading file contents for existence checks (6 sites)
- Improved documentation to clarify that --append-system-prompt-file and --system-prompt-file work in interactive mode (the docs previously said print mode only) Changed thinking summaries in Ctrl+O to show a ✻ Thinking… stub instead of full content. Set showThinkingSummaries: true in settings.json to restore. [VSCode]

### Bug Fixes
- Fixed symlink bypass where writing new files through a symlinked parent directory could escape the working directory in acceptEdits mode
- Fixed sandbox prompting users to approve non-allowed domains when allowManagedDomainsOnly is enabled in managed settings — non-allowed domains are now blocked automatically with no bypass
- Fixed interactive tools (e.g., AskUserQuestion ) being silently auto-allowed when listed in a skill's allowed-tools, bypassing the permission prompt and running with empty answers
- Fixed multi-GB memory spike when committing with large untracked binary files in the working tree
- Fixed Escape not interrupting a running turn when the input box has draft text. Use Up arrow to pull queued messages back for editing, or Ctrl+U to clear the input line.
- Fixed Android app crash when running local slash commands ( /voice , /cost ) in Remote Control sessions
- Fixed a memory leak where old message array versions accumulated in React Compiler memoCache over long sessions
- Fixed a memory leak where REPL render scopes accumulated over long sessions (~35MB over 1000 turns)
- Fixed memory retention in in-process teammates where the parent's full conversation history was pinned for the teammate's lifetime, preventing GC after /clear or auto-compact
- Fixed a memory leak in interactive mode where hook events could accumulate unboundedly during long sessions
- Fixed hang when --mcp-config points to a corrupted file
- Fixed slow startup when many skills/plugins are installed
- Fixed cd <outside-dir> && rm/mv/cp ... permission prompt to mention the chained write command instead of only showing "allow reading from /"
- Fixed cd <outside-dir> && <cmd> permission prompt to surface the chained command instead of only showing "Yes, allow reading from /"
- Fixed conditional .claude/rules/*.md files (with paths: frontmatter) and nested CLAUDE.md files not loading in print mode ( claude -p )
- Fixed /clear not fully clearing all session caches, reducing memory retention in long sessions
- Fixed terminal flicker caused by animated elements at the scrollback boundary
- Fixed UI frame drops on macOS when using
- Fixed occasional frame stalls during typing caused by synchronous debug log flushes
- Fixed TeammateIdle and TaskCompleted hooks to support {"continue": false, "stopReason": "..."} to stop the teammate, matching Stop hook behavior
- Fixed WorktreeCreate and WorktreeRemove plugin hooks being silently ignored
- Fixed WorktreeCreate hooks registered by plugins or SDK consumers being silently ignored
- Fixed skill descriptions with colons (e.g., "Triggers include: X, Y, Z") failing to load from SKILL.md frontmatter
- Fixed project skills without a description: frontmatter field not appearing in Claude's available skills list
- Fixed /context showing identical token counts for all
- Fixed literal nul file creation on Windows when the model uses CMD-style 2>nul redirection in Git Bash
- Fixed extra blank lines appearing below each tool call in the expanded subagent transcript view (Ctrl+O)
- Fixed Tab/arrow keys not cycling Settings tabs when /config search box is focused but empty
- Fixed service key OAuth sessions (CCR containers) spamming [ERROR] logs with 403s from profile-scoped endpoints
- Fixed inconsistent color for "Remote Control active" status indicator
- Fixed Voice waveform cursor covering the first suffix letter when dictating mid-input
- Fixed Voice input showing all 5 spaces during warmup instead of capping at ~2 (aligning with the "keep holding…" hint)
- Fixed rename and remove icons showing on the current active session when it is untitled and empty [VSCode]
- Fixed blank dot appearing in the timeline for some tools

---

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
