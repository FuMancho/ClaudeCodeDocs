# Admin Setup

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt "https://code.claude.com/docs/llms.txt")
>
> Use this file to discover all available pages before exploring further.

Claude Code enforces organization policy through managed settings that take precedence over local developer configuration. You deliver those settings from the Claude admin console, your mobile device management (MDM) system, or a file on disk. The settings control which tools, commands, servers, and network destinations Claude can reach.
This page walks through the deployment decisions in order. Each row links to the section below and to the reference page for that area.

SSO, SCIM provisioning, and seat assignment are configured at the Claude account level. See the [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide "https://claude.com/resources/tutorials/claude-enterprise-administrator-guide") and [seat assignment](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan "https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan") for those steps.

| Decision | What you’re choosing | Reference |
| --- | --- | --- |
| [Choose your API provider](#choose-your-api-provider "#choose-your-api-provider") | Where Claude Code authenticates and how it’s billed | [Authentication](./authentication.md "/docs/en/authentication"), [Bedrock](./amazon-bedrock.md "/docs/en/amazon-bedrock"), [Vertex AI](./google-vertex-ai.md "/docs/en/google-vertex-ai"), [Foundry](./microsoft-foundry.md "/docs/en/microsoft-foundry") |
| [Decide how settings reach devices](#decide-how-settings-reach-devices "#decide-how-settings-reach-devices") | How managed policy reaches developer machines | [Server-managed settings](./server-managed-settings.md "/docs/en/server-managed-settings"), [Settings files](./settings.md#settings-files "/docs/en/settings#settings-files") |
| [Decide what to enforce](#decide-what-to-enforce "#decide-what-to-enforce") | Which tools, commands, and integrations are allowed | [Permissions](./permissions.md "/docs/en/permissions"), [Sandboxing](./sandboxing.md "/docs/en/sandboxing") |
| [Set up usage visibility](#set-up-usage-visibility "#set-up-usage-visibility") | How you track spend and adoption | [Analytics](./analytics.md "/docs/en/analytics"), [Monitoring](./monitoring-usage.md "/docs/en/monitoring-usage"), [Costs](./costs.md "/docs/en/costs") |
| [Review data handling](#review-data-handling "#review-data-handling") | Data retention and compliance posture | [Data usage](./data-usage.md "/docs/en/data-usage"), [Security](./security.md "/docs/en/security") |

## [​](#choose-your-api-provider "#choose-your-api-provider") Choose your API provider

Claude Code connects to Claude through one of several API providers. Your choice affects billing, authentication, which compliance posture you inherit, and which Claude Code features your developers can use.

| Provider | Choose this when |
| --- | --- |
| Claude for Teams / Enterprise | You want Claude Code and claude.ai under one per-seat subscription with no infrastructure to run. This is the default recommendation. |
| Claude Console | You’re API-first or want pay-as-you-go billing |
| Amazon Bedrock | You want to inherit existing AWS compliance controls and billing |
| Google Vertex AI | You want to inherit existing GCP compliance controls and billing |
| Microsoft Foundry | You want to inherit existing Azure compliance controls and billing |

Some Claude Code features require a Claude.ai account. [Claude Code on the web](./claude-code-on-the-web.md "/docs/en/claude-code-on-the-web"), [Routines](./routines.md "/docs/en/routines"), [Code Review](./code-review.md "/docs/en/code-review"), [Remote Control](./remote-control.md "/docs/en/remote-control"), and the [Chrome extension](./chrome.md "/docs/en/chrome") are not available through Console API keys or cloud-provider credentials alone. If you deploy through Bedrock, Vertex, or Foundry, plan whether developers also need Claude for Teams or Enterprise seats. Each feature page lists its plan requirements.
For the full provider comparison covering authentication, regions, and feature parity, see the [enterprise deployment overview](./third-party-integrations.md "/docs/en/third-party-integrations"). Each provider’s auth setup is in [Authentication](./authentication.md "/docs/en/authentication").
Proxy and firewall requirements in [Network configuration](./network-config.md "/docs/en/network-config") apply regardless of provider. If you want a single endpoint in front of multiple providers or centralized request logging, see [LLM gateway](./llm-gateway.md "/docs/en/llm-gateway").

## [​](#decide-how-settings-reach-devices "#decide-how-settings-reach-devices") Decide how settings reach devices

Managed settings define policy that takes precedence over local developer configuration. Claude Code looks for them in four places and uses the first one it finds on a given device.

| Mechanism | Delivery | Priority | Platforms |
| --- | --- | --- | --- |
| Server-managed | Claude.ai admin console | Highest | All |
| plist / registry policy | macOS: `com.anthropic.claudecode` plist Windows: `HKLM\SOFTWARE\Policies\ClaudeCode` | High | macOS, Windows |
| File-based managed | macOS: `/Library/Application Support/ClaudeCode/managed-settings.json` Linux and WSL: `/etc/claude-code/managed-settings.json` Windows: `C:\Program Files\ClaudeCode\managed-settings.json` | Medium | All |
| Windows user registry | `HKCU\SOFTWARE\Policies\ClaudeCode` | Lowest | Windows only |

Server-managed settings reach devices at authentication time and refresh hourly during active sessions, with no endpoint infrastructure. They require a Claude for Teams or Enterprise plan, so deployments on other providers need one of the file-based or OS-level mechanisms instead.
If your organization mixes providers, configure [server-managed settings](./server-managed-settings.md "/docs/en/server-managed-settings") for Claude.ai users plus a [file-based or plist/registry fallback](./settings.md#settings-files "/docs/en/settings#settings-files") so other users still receive managed policy.
The plist and HKLM registry locations work with any provider and resist tampering because they require admin privileges to write. The Windows user registry at HKCU is writable without elevation, so treat it as a convenience default rather than an enforcement channel.
By default WSL reads only the Linux file path at `/etc/claude-code`. To extend your Windows registry and `C:\Program Files\ClaudeCode` policy to WSL on the same machine, set [`wslInheritsWindowsSettings: true`](./settings.md#available-settings "/docs/en/settings#available-settings") in either of those admin-only Windows sources.
Whichever mechanism you choose, managed values take precedence over user and project settings. Array settings such as `permissions.allow` and `permissions.deny` merge entries from all sources, so developers can extend managed lists but not remove from them.
See [Server-managed settings](./server-managed-settings.md "/docs/en/server-managed-settings") and [Settings files and precedence](./settings.md#settings-files "/docs/en/settings#settings-files").

## [​](#decide-what-to-enforce "#decide-what-to-enforce") Decide what to enforce

Managed settings can lock down tools, sandbox execution, restrict MCP servers and plugin sources, and control which hooks run. Each row is a control surface with the setting keys that drive it.

| Control | What it does | Key settings |
| --- | --- | --- |
| [Permission rules](./permissions.md "/docs/en/permissions") | Allow, ask, or deny specific tools and commands | `permissions.allow`, `permissions.deny` |
| [Permission lockdown](./permissions.md#managed-only-settings "/docs/en/permissions#managed-only-settings") | Only managed permission rules apply; disable `--dangerously-skip-permissions` | `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` |
| [Sandboxing](./sandboxing.md "/docs/en/sandboxing") | OS-level filesystem and network isolation with domain allowlists | `sandbox.enabled`, `sandbox.network.allowedDomains` |
| [Managed policy CLAUDE.md](./memory.md#deploy-organization-wide-claude-md "/docs/en/memory#deploy-organization-wide-claude-md") | Org-wide instructions loaded in every session, cannot be excluded | File at the managed policy path |
| [MCP server control](./managed-mcp.md "/docs/en/managed-mcp") | Restrict which MCP servers users can add or connect to, or deploy a fixed set | `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`, or a deployed `managed-mcp.json` file |
| [Plugin marketplace control](./plugin-marketplaces.md#managed-marketplace-restrictions "/docs/en/plugin-marketplaces#managed-marketplace-restrictions") | Restrict which marketplace sources users can add and install from | `strictKnownMarketplaces`, `blockedMarketplaces` |
| [Customization lockdown](./settings.md#strictpluginonlycustomization "/docs/en/settings#strictpluginonlycustomization") | Block skills, agents, hooks, and MCP servers from user and project sources, so they can only come from plugins or managed settings | `strictPluginOnlyCustomization` |
| [Hook restrictions](./settings.md#hook-configuration "/docs/en/settings#hook-configuration") | Only managed hooks load; restrict HTTP hook URLs | `allowManagedHooksOnly`, `allowedHttpHookUrls` |
| [Disable agent view](./agent-view.md#how-background-sessions-are-hosted "/docs/en/agent-view#how-background-sessions-are-hosted") | Turn off `claude agents`, `--bg`, `/background`, and the on-demand supervisor | `disableAgentView` |
| [Version floor](./settings.md "/docs/en/settings") | Prevent auto-update from installing below an org-wide minimum | `minimumVersion` |

Permission rules and sandboxing cover different layers. Denying WebFetch blocks Claude’s fetch tool, but if Bash is allowed, `curl` and `wget` can still reach any URL. Sandboxing closes that gap with a network domain allowlist enforced at the OS level.
For the threat model these controls defend against, see [Security](./security.md "/docs/en/security").

## [​](#set-up-usage-visibility "#set-up-usage-visibility") Set up usage visibility

Choose monitoring based on what you need to report on.

| Capability | What you get | Availability | Where to start |
| --- | --- | --- | --- |
| Usage monitoring | OpenTelemetry export of sessions, tools, and tokens | All providers | [Monitoring usage](./monitoring-usage.md "/docs/en/monitoring-usage") |
| Analytics dashboard | Per-user metrics, contribution tracking, leaderboard | Anthropic only | [Analytics](./analytics.md "/docs/en/analytics") |
| Cost tracking | Spend limits, rate limits, and usage attribution | Anthropic only | [Costs](./costs.md "/docs/en/costs") |

Cloud providers expose spend through AWS Cost Explorer, GCP Billing, or Azure Cost Management. Claude for Teams and Enterprise plans include a usage dashboard at [claude.ai/analytics/claude-code](https://claude.ai/analytics/claude-code "https://claude.ai/analytics/claude-code").

## [​](#review-data-handling "#review-data-handling") Review data handling

On Team, Enterprise, Claude API, and cloud provider plans, Anthropic does not train models on your code or prompts. Your API provider determines retention and compliance posture.

| Topic | What to know | Where to start |
| --- | --- | --- |
| Data usage policy | What Anthropic collects, how long it’s retained, what’s never used for training | [Data usage](./data-usage.md "/docs/en/data-usage") |
| Zero Data Retention (ZDR) | Nothing stored after the request completes. Available on Claude for Enterprise | [Zero data retention](./zero-data-retention.md "/docs/en/zero-data-retention") |
| Security architecture | Network model, encryption, authentication, audit trail | [Security](./security.md "/docs/en/security") |

If you need request-level audit logging or to route traffic by data sensitivity, place an [LLM gateway](./llm-gateway.md "/docs/en/llm-gateway") between developers and your provider. For regulatory requirements and certifications, see [Legal and compliance](./legal-and-compliance.md "/docs/en/legal-and-compliance").

## [​](#verify-and-onboard "#verify-and-onboard") Verify and onboard

After configuring managed settings, have a developer run `/status` inside Claude Code. The output includes a line beginning with `Enterprise managed settings` followed by the source in parentheses, one of `(remote)`, `(plist)`, `(HKLM)`, `(HKCU)`, or `(file)`. See [Verify active settings](./settings.md#verify-active-settings "/docs/en/settings#verify-active-settings").
Share these resources to help developers get started:

* [Quickstart](./quickstart.md "/docs/en/quickstart"): first-session walkthrough from install to working with a project
* [Common workflows](./common-workflows.md "/docs/en/common-workflows"): patterns for everyday tasks like code review, refactoring, and debugging
* [Claude 101](https://anthropic.skilljar.com/claude-101 "https://anthropic.skilljar.com/claude-101") and [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action "https://anthropic.skilljar.com/claude-code-in-action"): self-paced Anthropic Academy courses

For login issues, point developers to [authentication troubleshooting](./troubleshoot-install.md#login-and-authentication "/docs/en/troubleshoot-install#login-and-authentication"). The most common fixes are:

* Run `/logout` then `/login` to switch accounts
* Run `claude update` if the enterprise auth option is missing
* Restart the terminal after updating

If a developer sees “You haven’t been added to your organization yet,” their seat doesn’t include Claude Code access and needs to be updated in the admin console.

## [​](#next-steps "#next-steps") Next steps

With provider and delivery mechanism chosen, move on to detailed configuration:

* [Server-managed settings](./server-managed-settings.md "/docs/en/server-managed-settings"): deliver managed policy from the Claude admin console
* [Settings reference](./settings.md "/docs/en/settings"): every setting key, file location, and precedence rule
* [Monorepos and large repos](./large-codebases.md "/docs/en/large-codebases"): per-directory configuration patterns for organizations deploying into a monorepo
* [Amazon Bedrock](./amazon-bedrock.md "/docs/en/amazon-bedrock"), [Google Vertex AI](./google-vertex-ai.md "/docs/en/google-vertex-ai"), [Microsoft Foundry](./microsoft-foundry.md "/docs/en/microsoft-foundry"): provider-specific deployment
* [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide "https://claude.com/resources/tutorials/claude-enterprise-administrator-guide"): SSO, SCIM, seat management, and rollout playbook