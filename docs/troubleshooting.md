# Troubleshooting Claude Code

If you encounter issues while running the Anthropic Claude Code CLI or its environment integrations, refer to these official solutions.

## Installation Issues

### Windows `irm` or `&&` Not Recognized
If the PowerShell script fails because `irm` or `&&` is not recognized, you are likely running an outdated version of Windows PowerShell (v5 or older) or attempting to run the command in `CMD.exe`.
**Fix:** Run the installation command specifically in PowerShell 7+ or Git Bash.
> [!NOTE]
> Claude Code on Windows strongly recommends having `git-bash` installed and accessible in your `PATH`.

### WSL2 Errors & Permissions
WSL2 requires specific network port accessibility and sandbox setup.
If `npm install -g @anthropic-ai/claude-code` throws `EACCES` permission denied errors:
**Fix:** Do not run `sudo npm install`. Instead, configure npm to use a local directory:
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

### IDE Detection Failed (JetBrains on WSL2)
If you are running the JetBrains plugin from Windows but your codebase is inside WSL2, the plugin might fail to detect the node binary.
**Fix:** Ensure your IDE is properly running via the "WSL" remote connection feature, and the CLI is installed inside the Linux container, rather than the Windows host.

## Authentication and Tokens

### 403 Forbidden After Login
If `claude auth login` succeeds in the browser but the CLI throws a 403 Forbidden:
1. Ensure your Claude Pro or Claude Max subscription is currently active at `claude.com`. Pay-as-you-go API credits do not grant access to Claude Code.
2. Ensure you are not connected to a corporate VPN that blocks Anthropic IP addresses.

### Repeated Permission Prompts / Token Expired
If Claude constantly asks you to re-authenticate or loses its OAuth token:
**Fix:** Your global configuration file may have incorrect permissions.
*   **Mac/Linux:** `rm -rf ~/.claude.json && claude auth login`
*   **Windows:** Delete `%USERPROFILE%\.claude.json` and re-authenticate.

## General Usage Bugs

### Escape Key Not Working (JetBrains Terminal)
The Escape key might not exit the Session Picker or autocomplete menus when running the `claude` CLI inside a JetBrains terminal tab.
**Fix:** This is a known JetBrains terminal emulation bug. Use `Ctrl+C` to cancel the current prompt, or run the CLI in an external terminal application.

### Missing Language Tags in Code Blocks
Occasionally, Claude might generate a markdown code block without a language specifier (e.g. just ` ``` ` instead of ` ```python `), causing syntax highlighting plugins to fail.
**Fix:** Add a custom `CLAUDE.md` to your root directory with the strict prompt: `"Always include markdown language tags for all code snippets."`

### Search and Discovery Issues
If Search tool, `@file` mentions, custom agents, and custom skills aren't working, install system `ripgrep`:
```bash
# macOS (Homebrew)
brew install ripgrep
# Windows (winget)
winget install BurntSushi.ripgrep.MSVC
# Ubuntu/Debian
sudo apt install ripgrep
```
Then set `USE_BUILTIN_RIPGREP=0` in your environment.

### Slow Search Results on WSL
Disk read performance penalties when working across file systems on WSL may result in fewer-than-expected matches.
**Fix:** Submit more specific searches, or ensure your project is located on the Linux filesystem (`/home/`) rather than the Windows filesystem (`/mnt/c/`).

## Get More Help
Run `/doctor` to diagnose issues. It checks:
- Installation type, version, and search functionality
- Invalid settings files (malformed JSON, incorrect types)
- MCP server configuration errors
- Keybinding configuration problems
- Context usage warnings (large CLAUDE.md files, high MCP token usage)
- Plugin and agent loading errors

Use the `/bug` command within Claude Code to report problems directly to Anthropic.
