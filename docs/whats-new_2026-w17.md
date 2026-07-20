# Whats-New 2026-W17

Releases [v2.1.114 → v2.1.119](./changelog#2-1-114 "._changelog#2-1-114".md)4 features · April 20–24

/ultrareviewresearch preview

Now in public research preview. Ultrareview runs a fleet of bug-hunting agents in the cloud against your branch or a PR, and findings land back in the CLI or Desktop automatically. Run it before merging critical changes such as auth or data migrations.

[](https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/ultrareview.mp4?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=0fb1271365d38f414ad155aeb8edb08e)

Review the branch you’re on:

Claude Code

```text
> /ultrareview
```

Or point it at a PR:

Claude Code

```text
> /ultrareview 1234
```

[Ultrareview guide](./ultrareview "._ultrareview".md)

Session recapCLI

Switch focus away from a session and come back to a one-line recap of what happened while you were gone. Helpful for staying in flow while running several Claude sessions at once.

[](https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/session-recap.mp4?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=0a8db1470bd0161a47efeb2f322af76f)

Generate a recap on demand, or turn the automatic one off from `/config`:

Claude Code

```text
> /recap
```

[Interactive mode: session recap](./interactive-mode#session-recap "._interactive-mode#session-recap".md)

Custom themesv2.1.118

Build and switch between named color themes from `/theme`, or hand-edit JSON files in `~/.claude/themes/`. Each theme picks a base preset and overrides only the tokens you care about. Plugins can ship themes too.

Open the theme picker and create a new one:

Claude Code

```text
> /theme
```

[Terminal config: create a custom theme](./terminal-config#create-a-custom-theme "._terminal-config#create-a-custom-theme".md)

Claude Code on the webweb

A new look for [claude.ai/code](https://claude.ai/code "https://claude.ai/code") that matches the redesigned desktop app: sessions sidebar, drag-and-drop layout, and a refreshed routines view. Key parts were rebuilt for quicker responses and a more reliable experience.

!Claude Code on the web redesign overview: new UI, speed and reliability, work across web, mobile, and CLI

[Claude Code on the web](./claude-code-on-the-web "._claude-code-on-the-web".md)

Other wins

[Vim visual mode](./interactive-mode#vim-editor-mode "._interactive-mode#vim-editor-mode".md): press `v` for character selection or `V` for line selection in the prompt input, with operators and visual feedback

Hooks can now call MCP tools directly via [`type: “mcp_tool”`](./hooks#mcp-tool-hook-fields "._hooks#mcp-tool-hook-fields".md), so a hook can hit an already-connected server without spawning a process

`/cost` and `/stats` are merged into [`/usage`](./commands "._commands".md); the old names still work as typing shortcuts that open the relevant tab

`/config` changes (theme, editor mode, verbose, and similar) now persist to `~/.claude/settings.json` and follow the same project/local/policy precedence as other [settings](./settings "._settings".md)

[Forked subagents](./sub-agents#fork-the-current-conversation "._sub-agents#fork-the-current-conversation".md) can be enabled on external builds with `CLAUDE_CODE_FORK_SUBAGENT=1`: a fork inherits your full conversation context instead of starting fresh

Default [effort level](./model-config#adjust-effort-level "._model-config#adjust-effort-level".md) for Pro and Max subscribers on Opus 4.6 and Sonnet 4.6 is now `high` (was `medium`)

Native macOS and Linux builds replace the `Glob` and `Grep` tools with embedded `bfs` and `ugrep` available through Bash, for faster searches without a separate tool round-trip

`—from-pr` now accepts GitLab merge request, Bitbucket pull request, and GitHub Enterprise PR URLs in addition to github.com

Auto mode: include `“$defaults”` in [`autoMode.allow`, `soft_deny`, or `environment`](./auto-mode-config "._auto-mode-config".md) to add custom rules alongside the built-in list instead of replacing it

New [`claude plugin tag`](./plugin-dependencies#tag-plugin-releases-for-version-resolution "._plugin-dependencies#tag-plugin-releases-for-version-resolution".md) command creates release git tags for plugins with version validation

Opus 4.7 sessions now compute against the model’s native 1M context window, fixing inflated `/context` percentages and premature autocompaction

`/resume` on large sessions is up to 67% faster and now offers to summarize stale, large sessions before re-reading them

[Full changelog for v2.1.114–v2.1.119 →](./changelog#2-1-114 "._changelog#2-1-114".md)