# Migration Guide

> ## Documentation Index
>
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
>
> Use this file to discover all available pages before exploring further.

## [​](#overview) Overview

The Claude Code SDK has been renamed to the **Claude Agent SDK** and its documentation has been reorganized. This change reflects the SDK’s broader capabilities for building AI agents beyond just coding tasks.

## [​](#what’s-changed) What’s Changed

| Aspect | Old | New |
| --- | --- | --- |
| **Package Name (TS/JS)** | `@anthropic-ai/claude-code` | `@anthropic-ai/claude-agent-sdk` |
| **Python Package** | `claude-code-sdk` | `claude-agent-sdk` |
| **Documentation Location** | Claude Code docs | API Guide → Agent SDK section |

**Documentation Changes:** The Agent SDK documentation has moved from the Claude Code docs to the API Guide under a dedicated [Agent SDK](./overview.md) section. The Claude Code docs now focus on the CLI tool and automation features.

## [​](#migration-steps) Migration Steps

### [​](#for-typescript/javascript-projects) For TypeScript/JavaScript Projects

**1. Uninstall the old package:**

```text
npm uninstall @anthropic-ai/claude-code
```text
**2. Install the new package:**

```text
npm install @anthropic-ai/claude-agent-sdk
```text
**3. Update your imports:**
Change all imports from `@anthropic-ai/claude-code` to `@anthropic-ai/claude-agent-sdk`:

```text
// Before
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-code";

// After
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
```text
**4. Update package.json dependencies:**
If you have the package listed in your `package.json`, update it:
Before:

```text
{
  "dependencies": {
    "@anthropic-ai/claude-code": "^0.0.42"
  }
}
```text
After:

```text
{
  "dependencies": {
    "@anthropic-ai/claude-agent-sdk": "^0.2.0"
  }
}
```text
That’s it! No other code changes are required.

### [​](#for-python-projects) For Python Projects

**1. Uninstall the old package:**

```text
pip uninstall claude-code-sdk
```text
**2. Install the new package:**

```text
pip install claude-agent-sdk
```text
**3. Update your imports:**
Change all imports from `claude_code_sdk` to `claude_agent_sdk`:

```text
# Before
from claude_code_sdk import query, ClaudeCodeOptions

# After
from claude_agent_sdk import query, ClaudeAgentOptions
```text
**4. Update type names:**
Change `ClaudeCodeOptions` to `ClaudeAgentOptions`:

```text
# Before
from claude_code_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(model="claude-opus-4-7")

# After
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(model="claude-opus-4-7")
```text
**5. Review [breaking changes](#breaking-changes)**
Make any code changes needed to complete the migration.

## [​](#breaking-changes) Breaking changes

To improve isolation and explicit configuration, Claude Agent SDK v0.1.0 introduces breaking changes for users migrating from Claude Code SDK. Review this section carefully before migrating.

### [​](#python-claudecodeoptions-renamed-to-claudeagentoptions) Python: ClaudeCodeOptions renamed to ClaudeAgentOptions

**What changed:** The Python SDK type `ClaudeCodeOptions` has been renamed to `ClaudeAgentOptions`.
**Migration:**

```text
# BEFORE (claude-code-sdk)
from claude_code_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(model="claude-opus-4-7", permission_mode="acceptEdits")

# AFTER (claude-agent-sdk)
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(model="claude-opus-4-7", permission_mode="acceptEdits")
```text
**Why this changed:** The type name now matches the “Claude Agent SDK” branding and provides consistency across the SDK’s naming conventions.

### [​](#system-prompt-no-longer-default) System prompt no longer default

**What changed:** The SDK no longer uses Claude Code’s system prompt by default.
**Migration:**

TypeScript

Python

```text
// BEFORE (v0.0.x) - Used Claude Code's system prompt by default
const result = query({ prompt: "Hello" });

// AFTER (v0.1.0) - Uses minimal system prompt by default
// To get the old behavior, explicitly request Claude Code's preset:
const result = query({
  prompt: "Hello",
  options: {
    systemPrompt: { type: "preset", preset: "claude_code" }
  }
});

// Or use a custom system prompt:
const result = query({
  prompt: "Hello",
  options: {
    systemPrompt: "You are a helpful coding assistant"
  }
});
```text
**Why this changed:** Provides better control and isolation for SDK applications. You can now build agents with custom behavior without inheriting Claude Code’s CLI-focused instructions.

### [​](#settings-sources-default) Settings sources default

This default was briefly changed in v0.1.0 and then reverted, so no migration action is needed.
**Current behavior:** Omitting `settingSources` on `query()` loads user, project, and local filesystem settings, matching the CLI. This includes `~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, CLAUDE.md files, and custom commands.
To run isolated from filesystem settings, pass an empty array:

TypeScript

Python

```text
const result = query({
  prompt: "Hello",
  options: {
    settingSources: [] // No filesystem settings loaded
  }
});

// Or load only specific sources:
const result = query({
  prompt: "Hello",
  options: {
    settingSources: ["project"] // Only project settings
  }
});
```text
Isolation is especially important for CI/CD pipelines, deployed applications, test environments, and multi-tenant systems where local customizations should not leak in.

SDK v0.1.0 briefly defaulted to no settings loaded; this was reverted in subsequent releases. Python SDK 0.1.59 and earlier treated an empty list the same as omitting the option, so upgrade before relying on `setting_sources=[]`. See [What settingSources does not control](./claude-code-features.md#what-settingsources-does-not-control) for inputs that are read even when `settingSources` is `[]`.

## [​](#why-the-rename) Why the Rename?

The Claude Code SDK was originally designed for coding tasks, but it has evolved into a powerful framework for building all types of AI agents. The new name “Claude Agent SDK” better reflects its capabilities:

* Building business agents (legal assistants, finance advisors, customer support)
* Creating specialized coding agents (SRE bots, security reviewers, code review agents)
* Developing custom agents for any domain with tool use, MCP integration, and more

## [​](#getting-help) Getting Help

If you encounter any issues during migration:
**For TypeScript/JavaScript:**

1. Check that all imports are updated to use `@anthropic-ai/claude-agent-sdk`
2. Verify your package.json has the new package name
3. Run `npm install` to ensure dependencies are updated

**For Python:**

1. Check that all imports are updated to use `claude_agent_sdk`
2. Verify your requirements.txt or pyproject.toml has the new package name
3. Run `pip install claude-agent-sdk` to ensure the package is installed

## [​](#next-steps) Next Steps

* Explore the [Agent SDK Overview](./overview.md) to learn about available features
* Check out the [TypeScript SDK Reference](./typescript.md) for detailed API documentation
* Review the [Python SDK Reference](./python.md) for Python-specific documentation
* Learn about [Custom Tools](./custom-tools.md) and [MCP Integration](./mcp.md)