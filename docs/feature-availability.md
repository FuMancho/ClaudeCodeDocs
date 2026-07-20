# Feature-Availability

The Claude Code CLI and everything that runs locally work on every provider. For setup instructions per provider, see the [Enterprise deployment overview](./third-party-integrations "._third-party-integrations".md). To skip straight to what is missing on your provider, see the [summary by provider](#summary-by-provider "#summary-by-provider") tabs.
In the tables below, ✓ means available, ✗ means not available, and “See note” links to a footnote for partial support. A qualifier after ✓ narrows availability to that subset, and “Admin-enabled” means the feature is off until an organization admin turns it on.

## [​](#availability-by-model-provider "#availability-by-model-provider") Availability by model provider

How you authenticate determines which features Claude Code can reach. For a single list of what is missing on your provider, see the [summary by provider](#summary-by-provider "#summary-by-provider") tabs. To find your column in the tables:

* **Claude subscription**: you sign in with a claude.ai account on the Pro, Max, Team, or Enterprise plan
* **Anthropic Console**: you authenticate with an Anthropic API key
* **Amazon Bedrock**: you use Claude models from the Amazon Bedrock model catalog and set `CLAUDE_CODE_USE_BEDROCK`. The [Mantle endpoint](./amazon-bedrock#use-the-mantle-endpoint "._amazon-bedrock#use-the-mantle-endpoint".md) (`CLAUDE_CODE_USE_MANTLE`) is covered by this column
* **Claude Platform on AWS**: you bought Claude through AWS Marketplace but call the Anthropic API, and set `CLAUDE_CODE_USE_ANTHROPIC_AWS`
* **Google Cloud’s Agent Platform**: Google-operated; you set `CLAUDE_CODE_USE_VERTEX`
* **Microsoft Foundry**: Anthropic-operated on Azure; you set `CLAUDE_CODE_USE_FOUNDRY`

### [​](#features-available-on-every-provider "#features-available-on-every-provider") Features available on every provider

These work on every provider:

* [CLI](./quickstart "._quickstart".md) and [Agent SDK](./agent-sdk_overview "._agent-sdk_overview".md)
* [VS Code](./vs-code "._vs-code".md) and [JetBrains](./jetbrains "._jetbrains".md) extensions
* [Subagents](./sub-agents "._sub-agents".md), [hooks](./hooks-guide "._hooks-guide".md), [commands](./commands "._commands".md), and [skills](./skills "._skills".md)
* [CLAUDE.md memory](./memory "._memory".md), [plugins](./plugins "._plugins".md), and [MCP servers](./mcp "._mcp".md)
* [Checkpoints](./checkpointing "._checkpointing".md), [sandboxing](./sandboxing "._sandboxing".md), and [Workflows](./workflows "._workflows".md)
* [OpenTelemetry metrics](./monitoring-usage "._monitoring-usage".md) and the [managed settings file](./settings#settings-files "._settings#settings-files".md)

Three of these have provider-specific differences:

* **MCP servers**: [connectors from claude.ai](./mcp#use-mcp-servers-from-claude-ai "._mcp#use-mcp-servers-from-claude-ai".md) load only when your claude.ai subscription is the active authentication method, and [tool search](./mcp#configure-tool-search "._mcp#configure-tool-search".md) is off by default on Google Cloud’s Agent Platform and when `ANTHROPIC_BASE_URL` points to a non-first-party host
* **Subagents**: the built-in [Explore subagent](./sub-agents#built-in-subagents "._sub-agents#built-in-subagents".md) caps its inherited model at Opus on the Claude API, and inherits the main conversation’s model directly on any other provider, including Claude Platform on AWS
* **[Commands](./commands#all-commands "._commands#all-commands".md)**: `/design-sync` and `/radio` are unavailable on Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, and Claude Platform on AWS, and `/voice` requires a claude.ai account

### [​](#features-that-require-a-claude-subscription "#features-that-require-a-claude-subscription") Features that require a Claude subscription

These require signing in with a claude.ai account and are not reachable with an Anthropic Console API key or from a third-party provider:

* [Claude Code on the web](./claude-code-on-the-web "._claude-code-on-the-web".md), Claude Code on mobile, and [Claude Code in Slack](./slack "._slack".md)
* [Claude Code Desktop](./desktop "._desktop".md)
* [Routines](./routines "._routines".md) (`/schedule`)
* [Ultraplan](./ultraplan "._ultraplan".md) and [Ultrareview](./ultrareview "._ultrareview".md)
* [Code Review](./code-review "._code-review".md): Team and Enterprise plans
* [Remote Control](./remote-control "._remote-control".md)
* [Chrome extension](./chrome "._chrome".md)
* [Computer use](./computer-use "._computer-use".md): Pro and Max plans
* [Artifacts](./artifacts "._artifacts".md): Pro, Max, Team, and Enterprise plans
* [Voice dictation](./voice-dictation "._voice-dictation".md)

Desktop is the partial exception: [gateway routing can be configured in the app or by an administrator](./llm-gateway-connect#desktop-app "._llm-gateway-connect#desktop-app".md), Enterprise deployments can route Desktop to Google Cloud’s Agent Platform or a gateway provider via [managed settings](https://claude.com/docs/third-party/claude-desktop/configuration "https://claude.com/docs/third-party/claude-desktop/configuration"), and [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview "https://claude.com/docs/third-party/claude-desktop/overview") runs the Code tab on Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, or a self-hosted LLM gateway. For per-plan availability of these features, see [Availability by subscription plan](#availability-by-subscription-plan "#availability-by-subscription-plan").

### [​](#cli-capabilities-that-vary-by-provider "#cli-capabilities-that-vary-by-provider") CLI capabilities that vary by provider

These features work in the local CLI but depend on a server-side capability that not every provider exposes.

| Feature | Claude subscription | Anthropic Console | Amazon Bedrock | Claude Platform on AWS | Google Cloud’s Agent Platform | Microsoft Foundry |
| --- | --- | --- | --- | --- | --- | --- |
| [Web search](./tools-reference#websearch-tool-behavior "._tools-reference#websearch-tool-behavior".md) | ✓ | ✓ | ✗ | ✓ | See note [1](#fn1 "#fn1") | ✓ |
| [Fast mode](./fast-mode "._fast-mode".md) | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| [Auto mode](./auto-mode-config "._auto-mode-config".md) | ✓ | ✓ | See note [2](#fn2 "#fn2") | ✓ | See note [2](#fn2 "#fn2") | See note [2](#fn2 "#fn2") |
| [Advisor](./advisor "._advisor".md) | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| [Channels](./channels "._channels".md) | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| [`/loop` scheduled tasks](./scheduled-tasks "._scheduled-tasks".md) | ✓ | ✓ | See note [3](#fn3 "#fn3") | See note [3](#fn3 "#fn3") | See note [3](#fn3 "#fn3") | See note [3](#fn3 "#fn3") |
| [GitHub Actions](./github-actions "._github-actions".md) and [GitLab CI/CD](./gitlab-ci-cd "._gitlab-ci-cd".md) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |

### [​](#admin-and-analytics "#admin-and-analytics") Admin and analytics

Organization-level controls and usage visibility.

| Feature | Claude subscription | Anthropic Console | Amazon Bedrock | Claude Platform on AWS | Google Cloud’s Agent Platform | Microsoft Foundry |
| --- | --- | --- | --- | --- | --- | --- |
| [Analytics dashboard and API](./analytics "._analytics".md) | ✓ (dashboard: Team and Enterprise; API: Enterprise) | ✓ [5](#fn5 "#fn5") | ✗ | ✗ | ✗ | ✗ |
| [Server-managed settings](./server-managed-settings "._server-managed-settings".md) | ✓ (Team and Enterprise) | ✓ (Team and Enterprise) | ✗ | ✗ | ✗ | ✗ |
| [Zero Data Retention](./zero-data-retention "._zero-data-retention".md) | ✓ (qualified Enterprise accounts) | ✓ (qualified accounts) | See note [4](#fn4 "#fn4") | ✓ (qualified accounts) | See note [4](#fn4 "#fn4") | See note [4](#fn4 "#fn4") |

1 On Google Cloud’s Agent Platform, web search is available for Claude 4 models and later.
2 On these providers, auto mode supports only Claude Sonnet 5, Opus 4.7, Opus 4.8, and Fable 5. See [Auto mode configuration](./auto-mode-config "._auto-mode-config".md). In v2.1.158 through v2.1.206, auto mode on these providers also required setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`; v2.1.207 removed the requirement.
3 Explicit intervals such as `/loop every 2 hours` work on every provider. On Amazon Bedrock, Claude Platform on AWS, Google Cloud’s Agent Platform, and Microsoft Foundry, `/loop` cannot pick its own interval or supply the default maintenance prompt, so a prompt with no interval runs every 10 minutes, and `/loop` with no arguments shows the usage message. See [Scheduled tasks](./scheduled-tasks "._scheduled-tasks".md).
4 Subject to your agreement with the cloud provider.
5 Dashboard and API only. [Contribution metrics](./analytics#enable-contribution-metrics "._analytics#enable-contribution-metrics".md) requires a claude.ai Team or Enterprise organization.

If you authenticate through an [LLM gateway](./llm-gateway "._llm-gateway".md), feature availability matches the underlying provider the gateway forwards to. Some Anthropic-only features such as the [Advisor](./advisor "._advisor".md) work only if the gateway forwards requests intact to the Anthropic API.

### [​](#summary-by-provider "#summary-by-provider") Summary by provider

Each tab lists what is unavailable or partially supported on that provider, with alternatives where one exists. Everything not listed works the same as on a Claude subscription, apart from the [provider-specific differences](#features-available-on-every-provider "#features-available-on-every-provider") noted above. On Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, and Claude Platform on AWS, error reporting and telemetry to Anthropic are off by default. See [default behaviors by API provider](./data-usage#default-behaviors-by-api-provider "._data-usage#default-behaviors-by-api-provider".md) for what traffic still reaches Anthropic and how to opt out.

* Amazon Bedrock
* Claude Platform on AWS
* Google Cloud's Agent Platform
* Microsoft Foundry
* Anthropic Console

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription "#features-that-require-a-claude-subscription"), plus [web search](./tools-reference#websearch-tool-behavior "._tools-reference#websearch-tool-behavior".md), [fast mode](./fast-mode "._fast-mode".md), [Advisor](./advisor "._advisor".md), [Channels](./channels "._channels".md), the [analytics dashboard](./analytics "._analytics".md), [server-managed settings](./server-managed-settings "._server-managed-settings".md), and the [`/design-sync` and `/radio` commands](./commands#all-commands "._commands#all-commands".md).**Partial support:**

* [Desktop](./desktop "._desktop".md): only via [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview "https://claude.com/docs/third-party/claude-desktop/overview")
* [Auto mode](./auto-mode-config "._auto-mode-config".md): Sonnet 5, Opus 4.7, Opus 4.8, and Fable 5 only
* [`/loop`](./scheduled-tasks "._scheduled-tasks".md): explicit intervals only
* [Zero Data Retention](./zero-data-retention "._zero-data-retention".md): subject to your AWS agreement

**Alternatives:** for scheduling, use [`/loop`](./scheduled-tasks "._scheduled-tasks".md) with an explicit interval instead of `/schedule`. For cloud sessions, use [GitHub Actions](./github-actions "._github-actions".md) or [GitLab CI/CD](./gitlab-ci-cd "._gitlab-ci-cd".md). For web lookups, use the [WebFetch tool](./tools-reference#webfetch-tool-behavior "._tools-reference#webfetch-tool-behavior".md) with a specific URL.

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription "#features-that-require-a-claude-subscription"), plus [fast mode](./fast-mode "._fast-mode".md), [Advisor](./advisor "._advisor".md), [Channels](./channels "._channels".md), the [analytics dashboard](./analytics "._analytics".md), [server-managed settings](./server-managed-settings "._server-managed-settings".md), and the [`/design-sync` and `/radio` commands](./commands#all-commands "._commands#all-commands".md).**Available where Amazon Bedrock is not:** [web search](./tools-reference#websearch-tool-behavior "._tools-reference#websearch-tool-behavior".md).**Partial support:**

* [`/loop`](./scheduled-tasks "._scheduled-tasks".md): explicit intervals only

**Alternatives:** for scheduling, use [`/loop`](./scheduled-tasks "._scheduled-tasks".md) with an explicit interval instead of `/schedule`. For cloud sessions, use [GitHub Actions](./github-actions "._github-actions".md) or [GitLab CI/CD](./gitlab-ci-cd "._gitlab-ci-cd".md).

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription "#features-that-require-a-claude-subscription"), plus [fast mode](./fast-mode "._fast-mode".md), [Advisor](./advisor "._advisor".md), [Channels](./channels "._channels".md), the [analytics dashboard](./analytics "._analytics".md), [server-managed settings](./server-managed-settings "._server-managed-settings".md), and the [`/design-sync` and `/radio` commands](./commands#all-commands "._commands#all-commands".md).**Partial support:**

* [Desktop](./desktop "._desktop".md): via [managed settings](https://claude.com/docs/third-party/claude-desktop/configuration "https://claude.com/docs/third-party/claude-desktop/configuration") or [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview "https://claude.com/docs/third-party/claude-desktop/overview")
* [Web search](./tools-reference#websearch-tool-behavior "._tools-reference#websearch-tool-behavior".md): Claude 4 models and later
* [Auto mode](./auto-mode-config "._auto-mode-config".md): Sonnet 5, Opus 4.7, Opus 4.8, and Fable 5 only
* [`/loop`](./scheduled-tasks "._scheduled-tasks".md): explicit intervals only
* [Zero Data Retention](./zero-data-retention "._zero-data-retention".md): subject to your Google Cloud agreement

**Alternatives:** for scheduling, use [`/loop`](./scheduled-tasks "._scheduled-tasks".md) with an explicit interval instead of `/schedule`. For cloud sessions, use [GitHub Actions](./github-actions "._github-actions".md) or [GitLab CI/CD](./gitlab-ci-cd "._gitlab-ci-cd".md).

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription "#features-that-require-a-claude-subscription"), plus [fast mode](./fast-mode "._fast-mode".md), [Advisor](./advisor "._advisor".md), [Channels](./channels "._channels".md), [GitHub Actions](./github-actions "._github-actions".md) and [GitLab CI/CD](./gitlab-ci-cd "._gitlab-ci-cd".md), the [analytics dashboard](./analytics "._analytics".md), [server-managed settings](./server-managed-settings "._server-managed-settings".md), and the [`/design-sync` and `/radio` commands](./commands#all-commands "._commands#all-commands".md).**Partial support:**

* [Desktop](./desktop "._desktop".md): only via [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview "https://claude.com/docs/third-party/claude-desktop/overview")
* [Auto mode](./auto-mode-config "._auto-mode-config".md): Sonnet 5, Opus 4.7, Opus 4.8, and Fable 5 only
* [`/loop`](./scheduled-tasks "._scheduled-tasks".md): explicit intervals only
* [Zero Data Retention](./zero-data-retention "._zero-data-retention".md): subject to your Azure agreement

**Alternatives:** for scheduling, use [`/loop`](./scheduled-tasks "._scheduled-tasks".md) with an explicit interval instead of `/schedule`.

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription "#features-that-require-a-claude-subscription").Everything in [CLI capabilities that vary by provider](#cli-capabilities-that-vary-by-provider "#cli-capabilities-that-vary-by-provider") is available, as are [server-managed settings](./server-managed-settings "._server-managed-settings".md) when the API key belongs to a Team or Enterprise organization.

## [​](#availability-by-subscription-plan "#availability-by-subscription-plan") Availability by subscription plan

If you authenticate through Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, or an Anthropic Console API key, this section does not apply to you. When you sign in with a claude.ai account, your plan determines which of the features below are available.


| Feature | Pro | Max | Team | Enterprise |
| --- | --- | --- | --- | --- |
| [Claude Code on the web](./claude-code-on-the-web "._claude-code-on-the-web".md) | ✓ | ✓ | ✓ | ✓ [6](#fn6 "#fn6") |
| [Routines](./routines "._routines".md) | ✓ | ✓ | ✓ | ✓ |
| [Remote Control](./remote-control "._remote-control".md) | ✓ | ✓ | Admin-enabled | Admin-enabled |
| [Channels](./channels "._channels".md) | ✓ | ✓ | Admin-enabled | Admin-enabled |
| [Computer use](./computer-use "._computer-use".md) | ✓ | ✓ | ✗ | ✗ |
| Dispatch ([Desktop](./desktop#sessions-from-dispatch "._desktop#sessions-from-dispatch".md)) | ✓ | ✓ | ✗ | ✗ |
| [Code Review](./code-review "._code-review".md) | ✗ | ✗ | ✓ | ✓ |
| [Artifacts](./artifacts "._artifacts".md) | ✓ | ✓ | ✓ | Admin-enabled |
| [Analytics dashboard and contribution metrics](./analytics "._analytics".md) | ✗ | ✗ | ✓ | ✓ |
| [Enterprise Analytics API](./analytics#access-data-programmatically "._analytics#access-data-programmatically".md) | ✗ | ✗ | ✗ | ✓ |
| [Server-managed settings](./server-managed-settings "._server-managed-settings".md) | ✗ | ✗ | ✓ | ✓ |
| [SSO](https://support.claude.com/en/articles/9266767-what-is-the-team-plan "https://support.claude.com/en/articles/9266767-what-is-the-team-plan") | ✗ | ✗ | ✓ | ✓ |
| SCIM | ✗ | ✗ | ✗ | ✓ |
| [Compliance API](https://platform.claude.com/docs/en/api/compliance "https://platform.claude.com/docs/en/api/compliance") | ✗ | ✗ | ✗ | ✓ |
| [Zero Data Retention](./zero-data-retention "._zero-data-retention".md) | ✗ | ✗ | ✗ | ✓ [7](#fn7 "#fn7") |

6 On Enterprise, requires a premium seat or a Chat + Claude Code seat. See [Claude Code on the web](./claude-code-on-the-web "._claude-code-on-the-web".md).
7 Not included in the standard Enterprise plan. Requires separate enablement by Anthropic for qualified accounts. See [Zero Data Retention](./zero-data-retention "._zero-data-retention".md).
For pricing and the full plan comparison, see [Team plans](https://support.claude.com/en/articles/9266767-what-is-the-team-plan "https://support.claude.com/en/articles/9266767-what-is-the-team-plan") and [Enterprise plans](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan "https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan").

## [​](#model-availability "#model-availability") Model availability

For which Claude models and context-window sizes are available per provider and region, see [Model configuration](./model-config "._model-config".md) and the [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview "https://platform.claude.com/docs/en/about-claude/models/overview"). Vision, PDF input, and extended thinking are model capabilities rather than Claude Code features and work on every provider that offers the model. [Prompt caching](./prompt-caching "._prompt-caching".md) works the same way on most providers; on Amazon Bedrock, support varies by model.

## [​](#related-resources "#related-resources") Related resources

* [Enterprise deployment overview](./third-party-integrations "._third-party-integrations".md): compare authentication, billing, and regions across providers
* Provider setup guides: [Amazon Bedrock](./amazon-bedrock "._amazon-bedrock".md), [Claude Platform on AWS](./claude-platform-on-aws "._claude-platform-on-aws".md), [Google Cloud’s Agent Platform](./google-vertex-ai "._google-vertex-ai".md), [Microsoft Foundry](./microsoft-foundry "._microsoft-foundry".md)
* [Platforms and integrations](./platforms "._platforms".md): where Claude Code runs, including the CLI, Desktop, IDE extensions, web, mobile, and CI/CD