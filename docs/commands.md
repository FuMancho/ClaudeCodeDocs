# CLI Command Reference

This is a quick reference guide for the `@anthropic-ai/claude-code` CLI.

## Core Commands
*   `claude`: Start an interactive agent session in the current directory.
*   `claude "query"`: Start an interactive session bypassing the initial empty prompt by providing your first request immediately.
*   `claude -p "query"`: Run a single query via the CLI and exit immediately. Useful for CI/CD or scripting.
*   `claude -c`: Continue the most recent conversation in the current directory.
*   `claude update`: Updates the CLI to the latest npm version.

## Authentication
*   `claude auth login`: Open a browser to authenticate via your Claude Pro/Max account.
*   `claude auth logout`: Remove the current authentication token.
*   `claude auth status`: Check your current login status.

## Advanced Usage
*   **Piping Output:** You can pipe content directly into Claude Code. For example:
    ```bash
    cat error.log | claude -p "What is causing this error?"
    ```
*   **JSON Formatting:** Use the `--output-format json` flag if you want to integrate Claude's output programmatically into another script.
*   **Custom Prompts:** Use `--system-prompt-file` to load project-specific rules dynamically without modifying `CLAUDE.md`.

> [!WARNING]
> There is a flag called `--dangerously-skip-permissions` that allows Claude to execute terminal commands without prompting the user for confirmation. Use this with extreme caution and primarily in isolated virtual environments.
