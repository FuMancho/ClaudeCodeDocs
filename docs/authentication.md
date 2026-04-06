# Authentication

Claude Code supports multiple authentication methods depending on your setup. Individual users can log in with a Claude.ai account, while teams can use Claude for Teams or Enterprise, the Claude Console, or a cloud provider like Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.

## [​](#log-in-to-claude-code) Log in to Claude Code

After [installing Claude Code](./setup.md#install-claude-code), run `claude` in your terminal. On first launch, Claude Code opens a browser window for you to log in.
If the browser doesn’t open automatically, press `c` to copy the login URL to your clipboard, then paste it into your browser.
You can authenticate with any of these account types:

* **Claude Pro or Max subscription**: log in with your Claude.ai account. Subscribe at claude.com/pricing.
* **Claude for Teams or Enterprise**: log in with the Claude.ai account your team admin invited you to.
* **Claude Console**: log in with your Console credentials. Your admin must have [invited you](#claude-console-authentication) first.
* **Cloud providers**: if your organization uses [Amazon Bedrock](./amazon-bedrock.md), [Google Vertex AI](./google-vertex-ai.md), or [Microsoft Foundry](./microsoft-foundry.md), set the required environment variables before running `claude`. No browser login is needed.

To log out and re-authenticate, type `/logout` at the Claude Code prompt.
If you’re having trouble logging in, see [authentication troubleshooting](./troubleshooting.md#authentication-issues).

## [​](#set-up-team-authentication) Set up team authentication

For teams and organizations, you can configure Claude Code access in one of these ways:

* [Claude for Teams or Enterprise](#claude-for-teams-or-enterprise), recommended for most teams
* [Claude Console](#claude-console-authentication)
* [Amazon Bedrock](./amazon-bedrock.md)
* [Google Vertex AI](./google-vertex-ai.md)
* [Microsoft Foundry](./microsoft-foundry.md)

### [​](#claude-for-teams-or-enterprise) Claude for Teams or Enterprise

Claude for Teams and Claude for Enterprise provide the best experience for organizations using Claude Code. Team members get access to both Claude Code and Claude on the web with centralized billing and team management.

* **Claude for Teams**: self-service plan with collaboration features, admin tools, and billing management. Best for smaller teams.
* **Claude for Enterprise**: adds SSO, domain capture, role-based permissions, compliance API, and managed policy settings for organization-wide Claude Code configurations. Best for larger organizations with security and compliance requirements.

1

Subscribe

Subscribe to Claude for Teams or contact sales for Claude for Enterprise.

2

Invite team members

Invite team members from the admin dashboard.

3

Install and log in

Team members install Claude Code and log in with their Claude.ai accounts.

### [​](#claude-console-authentication) Claude Console authentication

For organizations that prefer API-based billing, you can set up access through the Claude Console.

1

Create or use a Console account

Use your existing Claude Console account or create a new one.

2

Add users

You can add users through either method:

* Bulk invite users from within the Console: Settings -> Members -> Invite
* Set up SSO

3

Assign roles

When inviting users, assign one of:

* **Claude Code** role: users can only create Claude Code API keys
* **Developer** role: users can create any kind of API key

4

Users complete setup

Each invited user needs to:

* Accept the Console invite
* [Check system requirements](./setup.md#system-requirements)
* [Install Claude Code](./setup.md#install-claude-code)
* Log in with Console account credentials

### [​](#cloud-provider-authentication) Cloud provider authentication

For teams using Amazon Bedrock, Google Vertex AI, or Microsoft Foundry:

1

Follow provider setup

Follow the [Bedrock docs](./amazon-bedrock.md), [Vertex docs](./google-vertex-ai.md), or [Microsoft Foundry docs](./microsoft-foundry.md).

2

Distribute configuration

Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [manage configuration here](./settings.md).

3

Install Claude Code

Users can [install Claude Code](./setup.md#install-claude-code).

## [​](#credential-management) Credential management

Claude Code securely manages your authentication credentials:

* **Storage location**: on macOS, credentials are stored in the encrypted macOS Keychain. On Linux and Windows, credentials are stored in `~/.claude/.credentials.json`, or under `$CLAUDE_CONFIG_DIR` if that variable is set. On Linux, the file is written with mode `0600`; on Windows, it inherits the access controls of your user profile directory.
* **Supported authentication types**: Claude.ai credentials, Claude API credentials, Azure Auth, Bedrock Auth, and Vertex Auth.
* **Custom credential scripts**: the [`apiKeyHelper`](./settings.md#available-settings) setting can be configured to run a shell script that returns an API key.
* **Refresh intervals**: by default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals.
* **Slow helper notice**: if `apiKeyHelper` takes longer than 10 seconds to return a key, Claude Code displays a warning notice in the prompt bar showing the elapsed time. If you see this notice regularly, check whether your credential script can be optimized.

`apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` apply to terminal CLI sessions only. Claude Desktop and remote sessions use OAuth exclusively and do not call `apiKeyHelper` or read API key environment variables.

### [​](#authentication-precedence) Authentication precedence

When multiple credentials are present, Claude Code chooses one in this order:

1. Cloud provider credentials, when `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, or `CLAUDE_CODE_USE_FOUNDRY` is set. See [third-party integrations](./third-party-integrations.md) for setup.
2. `ANTHROPIC_AUTH_TOKEN` environment variable. Sent as the `Authorization: Bearer` header. Use this when routing through an [LLM gateway or proxy](./llm-gateway.md) that authenticates with bearer tokens rather than Anthropic API keys.
3. `ANTHROPIC_API_KEY` environment variable. Sent as the `X-Api-Key` header. Use this for direct Anthropic API access with a key from the [Claude Console](https://platform.claude.com). In interactive mode, you are prompted once to approve or decline the key, and your choice is remembered. To change it later, use the “Use custom API key” toggle in `/config`. In non-interactive mode (`-p`), the key is always used when present.
4. [`apiKeyHelper`](./settings.md#available-settings) script output. Use this for dynamic or rotating credentials, such as short-lived tokens fetched from a vault.
5. Subscription OAuth credentials from `/login`. This is the default for Claude Pro, Max, Team, and Enterprise users.

If you have an active Claude subscription but also have `ANTHROPIC_API_KEY` set in your environment, the API key takes precedence once approved. This can cause authentication failures if the key belongs to a disabled or expired organization. Run `unset ANTHROPIC_API_KEY` to fall back to your subscription, and check `/status` to confirm which method is active.
[Claude Code on the Web](./claude-code-on-the-web.md) always uses your subscription credentials. `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` in the sandbox environment do not override them.