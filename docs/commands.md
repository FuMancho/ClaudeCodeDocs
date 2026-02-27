# CLI Command Reference

This is a comprehensive reference guide for the `@anthropic-ai/claude-code` CLI based on official documentation.

## Core Commands

*   `claude`: Start an interactive agent session in the current directory.
*   `claude "query"`: Start an interactive session and bypass the initial empty prompt by providing your first request immediately.
*   `claude -p "query"`: Run a single query via the CLI and exit immediately. Perfect for piping into other tools.
*   `claude -c`: Continue the most recent conversation in the current directory.
*   `claude -r`: Open the **Session Picker** menu. This allows you to select and resume a specific previous conversation.
*   `claude commit`: Use Claude's generative AI to automatically write a descriptive commit message based on your staged Git changes.
*   `claude update`: Updates the CLI to the latest npm version.

## Chat Interface Commands (Slash Commands)

Inside an active interactive session, you can use built-in slash commands:

*   `/help`: View documentation on how to use Claude Code or ask a specific meta-question (e.g. `/help how do I manage context?`).
*   `/clear`: Wipes the current session history and starts a fresh context window. 

## Command Flags

### Context and Prompts
*   `--system-prompt-file <path>`: Load a custom set of rules dynamically without permanently modifying the project `CLAUDE.md`.
*   `-p` or `--print`: Non-interactive mode. Useful for `cat logs.txt | claude -p "Find errors"`.

### Automation and Formatting
*   `--output-format json`: Force Claude to output its final response in raw JSON. Useful for integrating Claude Code into a larger shell script.
*   `--dangerously-skip-permissions`: 
    > [!WARNING]
    > Forces Claude to execute terminal commands (like file edits or builds) without prompting the user for confirmation. Use this with extreme caution and primarily in isolated VMs or Docker containers.

## Best Practices for Command Usage

1.  **Manage Context Aggressively**: If your session is growing too long and slowing down, use `/clear`.
2.  **Course-Correct Early**: Don't wait for Claude to finish a 10-minute task if you see it modifying the wrong file. Hit `Ctrl+C` to interrupt the agentic loop, refine your prompt, and try again.
3.  **Use Shortcuts**:
    *   Press `?` inside a session to see all keyboard shortcuts.
    *   Press `↑` for command history.
    *   Press `Tab` for completion.
