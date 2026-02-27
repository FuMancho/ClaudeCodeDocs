# Agentic Capabilities

Claude Code operates with an "agentic" approach, meaning it moves beyond simple inline code autocomplete. It directly navigates your file system, executes shell commands, and modifies code across multiple files.

## Sub-Agents
When faced with complex user requests, Claude Code can spawn sub-agents to parallelize work or dive deep into research (e.g., using `Task` or `Explore` tools). This helps delay context window filling and provides a modular approach to problem-solving.

## Model Context Protocol (MCP)
MCP is an open standard that allows Claude Code to securely connect to external tools and data sources.
For example, you can use MCP to:
*   Read design documents straight from Google Drive.
*   Update tickets in Jira.
*   Pull context from Slack messages.

## Custom Slash Commands (Skills)
You can teach Claude Code repeatable workflows using custom slash commands defined in the project. For example, you might create a `/review-pr` command that instructs Claude to run specific linting and formatting commands before submitting a pull request.

> [!TIP]
> Use `.gemini/rules.md` or a `CLAUDE.md` project-level file to give Claude specific instructions on how to handle these agentic workflows in your codebase.
