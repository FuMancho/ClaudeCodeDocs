# Agentic Capabilities

Claude Code operates with an "agentic" approach. It does not just autocomplete text; it runs through an **Agentic Loop**, which involves exploring, generating, and validating changes iteratively.

## The Agentic Loop
When you give Claude Code a complex task, it:
1. **Explores**: It reads `CLAUDE.md`, scans directory structures, and uses tools to search for relevant internal files.
2. **Plans**: It breaks down the user request into manageable steps.
3. **Executes**: It edits files or runs shell scripts.
4. **Verifies**: It checks the outcome of its actions and loops back if an error was found.

## Plan Mode
For large refactors, use **Plan Mode**. When in this mode, Claude will only analyze the codebase and generate an architectural breakdown or markdown plan, without modifying any files or running dangerous commands. This allows you to verify the logic before committing to the Execution phase.

You can set Plan Mode as your default via the CLI settings.

## Extended Thinking (Thinking Mode)
Claude Code supports extended "Thinking Mode" for highly complex reasoning tasks. It allocates more time to internal deliberation before outputting a response, resulting in significantly fewer bugs when dealing with spaghetti code or intricate mathematical architectures. You can enable this in your session preferences.

## Checkpoints and Safety
Because Claude Code runs agentically, it is possible it might accidentally format a file incorrectly or delete a needed line. 

Claude automatically generates **Checkpoints** for each major action. If Claude makes a mistake or if you change your mind about the direction of a feature, you can "Undo" the state, and Claude will automatically revert to the Git tree or backup checkpoint before the loop started.

## Model Context Protocol (MCP) & Plugins
MCP is an open standard that allows Claude Code to securely connect to external tools and data sources.

You can create an `mcp.json` file to define local servers that expose databases or internal enterprise APIs directly to Claude Code's agentic loop. 

Additionally, Claude Code supports installing community plugins (like a Figma integration or a PostgreSQL dialect adapter) to further extend its native capabilities.
