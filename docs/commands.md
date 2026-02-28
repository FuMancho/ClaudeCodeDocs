# CLI Reference

Complete reference for the Claude Code command-line interface. For an introduction and guided setup, see the [Getting Started](./getting-started.md) guide.

## CLI Commands

| Command | Description | Example |
|---|---|---|
| `claude` | Start an interactive session | `claude` |
| `claude "query"` | Start with an initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Print mode — query, then exit | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continue in print mode | `claude -c -p "Check for type errors"` |
| `claude -r "<session>" "query"` | Resume session by ID or name | `claude -r "auth-refactor" "Finish this PR"` |
| `claude update` | Update to the latest version | `claude update` |
| `claude auth login` | Sign in (supports `--email` and `--sso`) | `claude auth login --email user@co.com --sso` |
| `claude auth logout` | Log out | `claude auth logout` |
| `claude auth status` | Show auth status as JSON (`--text` for readable) | `claude auth status` |
| `claude agents` | List all configured [sub-agents](https://code.claude.com/docs/en/sub-agents) | `claude agents` |
| `claude mcp` | Configure [MCP](https://code.claude.com/docs/en/mcp) servers | `claude mcp` |
| `claude remote-control` | Start a [Remote Control](https://code.claude.com/docs/en/remote-control) session | `claude remote-control` |
| `claude commit` | Create a Git commit | `claude commit` |
| `claude doctor` | Run a diagnostic check | `claude doctor` |

## CLI Flags

| Flag | Description | Example |
|---|---|---|
| `--add-dir` | Add extra working directories | `claude --add-dir ../apps ../lib` |
| `--agent` | Specify an agent for the session | `claude --agent my-custom-agent` |
| `--agents` | Define sub-agents dynamically via JSON | See [Agents Flag Format](#agents-flag-format) |
| `--allowedTools` | Tools that execute without prompting | `"Bash(git log *)" "Read"` |
| `--append-system-prompt` | Append text to the default system prompt | `claude --append-system-prompt "Use TypeScript"` |
| `--chrome` | Enable Chrome browser integration | `claude --chrome` |
| `--continue`, `-c` | Load the most recent conversation | `claude -c` |
| `--dangerously-skip-permissions` | Skip all permission prompts | `claude --dangerously-skip-permissions` |
| `--debug` | Enable debug mode with optional filtering | `claude --debug "api,mcp"` |
| `--disallowedTools` | Remove tools from the model's context | `"Edit" "Bash(rm *)"` |
| `--fallback-model` | Fallback model if default is overloaded (print mode) | `claude -p --fallback-model sonnet "query"` |
| `--from-pr` | Resume sessions linked to a GitHub PR | `claude --from-pr 123` |
| `--json-schema` | Return validated JSON matching a schema (print mode) | `claude -p --json-schema '{...}' "query"` |
| `--max-budget-usd` | Maximum API spend before stopping (print mode) | `claude -p --max-budget-usd 5.00 "query"` |
| `--max-turns` | Limit agentic turns (print mode) | `claude -p --max-turns 3 "query"` |
| `--mcp-config` | Load MCP servers from JSON files | `claude --mcp-config ./mcp.json` |
| `--model` | Set the model (`sonnet`, `opus`, or full name) | `claude --model claude-sonnet-4-6` |
| `--output-format` | Output format: `text`, `json`, `stream-json` | `claude -p --output-format json "query"` |
| `--permission-mode` | Start in a specific permission mode | `claude --permission-mode plan` |
| `--print`, `-p` | Print mode (non-interactive) | `claude -p "query"` |
| `--remote` | Create a new web session on claude.ai | `claude --remote "Fix the login bug"` |
| `--resume`, `-r` | Resume a session by ID or pick interactively | `claude -r auth-refactor` |
| `--system-prompt` | Replace the entire system prompt | `claude --system-prompt "You are a Python expert"` |
| `--tools` | Restrict available tools | `claude --tools "Bash,Edit,Read"` |
| `--verbose` | Enable verbose logging | `claude --verbose` |
| `--version`, `-v` | Output the version number | `claude -v` |
| `--worktree`, `-w` | Start in an isolated Git worktree | `claude -w feature-auth` |

> [!TIP]
> The `--output-format json` flag is particularly useful for scripting and automation, allowing you to parse Claude's responses programmatically.

## Agents Flag Format

The `--agents` flag accepts a JSON object defining one or more custom [sub-agents](https://code.claude.com/docs/en/sub-agents):

```json
{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "debugger": {
    "description": "Debugging specialist for errors and test failures.",
    "prompt": "You are an expert debugger. Analyze errors, identify root causes, and provide fixes."
  }
}
```

| Field | Required | Description |
|---|---|---|
| `description` | Yes | When the sub-agent should be invoked |
| `prompt` | Yes | System prompt guiding the sub-agent |
| `tools` | No | Array of tools (inherits all if omitted) |
| `disallowedTools` | No | Tools to deny for this sub-agent |
| `model` | No | Model alias: `sonnet`, `opus`, `haiku`, or `inherit` |
| `skills` | No | Skills to preload into the sub-agent |
| `mcpServers` | No | MCP servers for this sub-agent |
| `maxTurns` | No | Maximum agentic turns before stopping |

## System Prompt Flags

| Flag | Behavior | Modes | Use Case |
|---|---|---|---|
| `--system-prompt` | **Replaces** entire default prompt | Interactive + Print | Complete control over instructions |
| `--system-prompt-file` | **Replaces** with file contents | Print only | Reproducible, version-controlled prompts |
| `--append-system-prompt` | **Appends** to default prompt | Interactive + Print | Add instructions while keeping defaults |
| `--append-system-prompt-file` | **Appends** file contents | Print only | Version-controlled additions |

> [!NOTE]
> `--system-prompt` and `--system-prompt-file` are mutually exclusive. The append flags can be combined with either replacement flag. For most use cases, **`--append-system-prompt` is recommended** as it preserves Claude Code's built-in capabilities.

## See Also

- [Interactive Mode](https://code.claude.com/docs/en/interactive-mode) — Shortcuts, input modes, and interactive features
- [Settings](https://code.claude.com/docs/en/settings) — Configuration options
- [Hooks Reference](https://code.claude.com/docs/en/hooks) — Event-driven automation
- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference) — Extending Claude Code
