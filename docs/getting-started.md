# Getting Started with Claude Code

The Anthropic Claude Code CLI brings the power of Claude directly to your terminal. It acts as an agentic AI assistant capable of analyzing projects, generating code, and executing tools on your behalf through an Agentic Loop.

> [!IMPORTANT]
> To use Claude Code, you must have an active **Claude Pro** or **Claude Max** subscription. 

## Prerequisites
- **Node.js**: Version 18 or newer is required.
- **npm**: Included with Node.js.

### Validating Prerequisites
Before installing, verify your environment meets the requirements:
```bash
node -v # Should output v18.x.x or higher
npm -v  # Should output 9.x.x or higher
```

## Installation

Claude Code can be installed natively for the best experience across all platforms. 

### macOS / Linux (Native Script - Recommended)
The native script automatically handles setting up the environment and supports auto-updating:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows (Native Script - Recommended)
Using Windows PowerShell:
```powershell
irm https://claude.ai/install.ps1 | iex
```

### IDE Extensions
Claude Code functionality is also rolling out as official integrations for IDEs rather than just a terminal client:
- **VS Code / Cursor:** Install the extension from the marketplace (`Ctrl+Shift+X` and search `anthropic.claude-code`).
- **JetBrains:** Available via the plugin marketplace.

## Authentication

Once installed, navigate to your project directory and run:

```bash
claude
```

On your first run, this will prompt a browser window to open. Log in using your Claude Pro/Max credentials to authorize the CLI.

> [!NOTE]
> You can manage your authentication status at any time using `claude auth login`, `claude auth logout`, or `claude auth status`.

## Core Philosophy for Beginners

To get the best out of Claude Code, approach the prompt from a "Delegate, don’t dictate" perspective:

1. **Explore first, then code:** Ask Claude to analyze the existing app structure before throwing a huge refactor at it. (`"Analyze the database schema and summarize it"`)
2. **Be specific upfront:** Use step-by-step instructions for what you want.
3. **Give Claude a way to verify its work:** If you ask it to build a feature, tell it how it can test the code via a shell command when it finishes (e.g. `"Build the login page, then run npm run test to verify it passes rules."`)

## Next Steps
Now that you are installed and authenticated, start your first interactive session:
```bash
claude "Analyze this repository and summarize what it does."
```

If you encounter issues during installation or authentication, refer to the [Troubleshooting Guide](./troubleshooting.md).
