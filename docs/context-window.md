# Context Window

Claude Code’s context window holds everything Claude knows about your session: your instructions, the files it reads, its own responses, and content that never appears in your terminal. The timeline below walks through what loads and when. See [the written breakdown](#what-the-timeline-shows) for the same content as a list.


## [​](#what-the-timeline-shows) What the timeline shows

The session walks through a realistic flow with representative token counts:

* **Before you type anything**: CLAUDE.md, auto memory, MCP tool names, and skill descriptions all load into context. Your own setup may add more here, like an [output style](./output-styles.md) or text from [`--append-system-prompt`](./cli-reference.md), which both go into the system prompt the same way.
* **As Claude works**: each file read adds to context, [path-scoped rules](./memory.md#path-specific-rules) load automatically alongside matching files, and a [PostToolUse hook](./hooks-guide.md) fires after each edit.
* **The follow-up prompt**: a [subagent](./sub-agents.md) handles the research in its own separate context window, so the large file reads stay out of yours. Only the summary and a small metadata trailer come back.
* **At the end**: `/compact` replaces the conversation with a structured summary. Most startup content reloads automatically. The [skill](./skills.md) listing is the one exception.

## [​](#check-your-own-session) Check your own session

The visualization uses representative numbers. To see your actual context usage at any point, run `/context` for a live breakdown by category with optimization suggestions. Run `/memory` to check which CLAUDE.md and auto memory files loaded at startup.

## [​](#related-resources) Related resources

For deeper coverage of the features shown in the timeline, see these pages:

* [Extend Claude Code](./features-overview.md): when to use CLAUDE.md vs skills vs rules vs hooks vs MCP
* [Store instructions and memories](./memory.md): CLAUDE.md hierarchy and auto memory
* [Subagents](./sub-agents.md): delegate research to a separate context window
* [Best practices](./best-practices.md): managing context as your primary constraint
* [Reduce token usage](./costs.md#reduce-token-usage): strategies for keeping context usage low