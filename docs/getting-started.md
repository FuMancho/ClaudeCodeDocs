# Getting Started with Claude Code

The Anthropic Claude Code CLI brings the power of Claude directly to your terminal. It acts as an agentic AI assistant capable of analyzing projects, generating code, and executing tools on your behalf.

> [!IMPORTANT]
> To use Claude Code, you must have an active **Claude Pro** or **Claude Max** subscription. 

## Prerequisites
- **Node.js**: Version 18 or newer is required.
- **npm**: Included with Node.js.

## Installation

You can install Claude Code depending on your primary operating system and package manager preference.

### npm (Global Install)
The most common approach across all platforms since it relies on Node.js:
```bash
npm install -g @anthropic-ai/claude-code
```

### macOS / Linux (Native Script)
For a straightforward installation that supports auto-updating:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows (Native Script)
Using Windows PowerShell:
```powershell
irm https://claude.ai/install.ps1 | iex
```

### macOS (Homebrew)
> [!WARNING]
> If you install via Homebrew, the CLI will not auto-update. You must manually run `brew upgrade claude-code`.
```bash
brew install --cask claude-code
```

### Windows (WinGet)
> [!WARNING]
> Like Homebrew, WinGet installations require manual updates with `winget upgrade Anthropic.ClaudeCode`.
```powershell
winget install Anthropic.ClaudeCode
```

## Authentication

Once installed, you must authenticate the CLI with your Anthropic account.

Navigate to any directory in your terminal and run:

```bash
claude
```

On your first run, this will prompt a browser window to open. Log in using your Claude Pro/Max credentials to authorize the CLI.

> [!NOTE]
> You can manage your authentication status at any time using `claude auth login`, `claude auth logout`, or `claude auth status`.

## Next Steps
Now that you are installed and authenticated, try launching Claude in your project directory:
```bash
claude "Analyze this repository and summarize what it does."
```
