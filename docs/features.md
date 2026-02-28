# Features

Overview of core features in the Claude Code CLI.

## Agentic Code Execution

Claude Code is a full **agentic coding assistant** — it doesn't just suggest code, it reads files, writes code, and executes tools autonomously.

- **File operations** — reads, creates, edits, and deletes files
- **Shell commands** — runs build tools, tests, linters, and git
- **Multi-file refactoring** — understands project context across files
- **Error self-correction** — reads build/test errors and fixes iteratively

## Sub-Agent Architecture

Spawn specialized sub-agents for parallel or delegated work:

```bash
# Sub-agents inherit CLAUDE.md but get fresh context windows
# Define custom agents in ~/.claude/agents/
```

| Agent Type | Purpose |
|---|---|
| **Task sub-agent** | Delegated work with scoped context |
| **Specialist agent** | Security audit, code review, testing |
| **Background agent** | Long-running tasks (headless mode) |

See [Advanced Settings](./advanced-settings.md) for agent definitions.

## CLAUDE.md — Persistent Memory

Project-level instructions that persist across sessions:

- Role and identity specification
- Technology stack constraints
- Coding conventions and architectural rules
- Approved/denied commands
- File import via `@./path/to/file.md`

## Model Context Protocol (MCP)

Extend Claude with custom tools via MCP servers:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

Built-in tool categories:
- **File tools** — read, write, edit, search
- **Shell tools** — bash command execution
- **Web tools** — URL fetching (when enabled)
- **MCP tools** — custom integrations

## Hooks System

Automate pre/post actions on tool use:

| Hook | Trigger | Use Case |
|---|---|---|
| `PreToolUse` | Before any tool | Logging, validation |
| `PostToolUse` | After any tool | Auto-formatting, checkpointing |

## Skills & Slash Commands

- **Skills** — Reusable capability definitions discovered from project files
- **Slash commands** — Custom workflows triggered via `/command`
- **Output styles** — Control response verbosity and format

## IDE Integration

Native extensions for:
- **VS Code** — Full integration with Claude sidebar
- **JetBrains** — IntelliJ, PyCharm, WebStorm support
- **Terminal** — Standalone CLI mode

## Session Management

```bash
claude -c                     # Continue last session
claude --resume               # Resume specific session
/compact                      # Summarize context to free space
```

## Key CLI Flags

| Flag | Purpose |
|---|---|
| `-p "prompt"` | Non-interactive, single prompt |
| `-c` | Continue previous session |
| `--model opus` | Select model |
| `--output-format json` | JSON output for scripting |
| `--dangerously-skip-permissions` | Skip permission prompts (⚠️) |

## See Also

- [Getting Started](./getting-started.md) — Installation and setup
- [Commands](./commands.md) — Full CLI reference
- [Advanced Settings](./advanced-settings.md) — Deep configuration
- [Experimental Settings](./experimental-settings.md) — Cutting-edge features
- [Agent Features](./agent-features.md) — Sub-agent deep dive
