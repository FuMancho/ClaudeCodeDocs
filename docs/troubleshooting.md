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
If you're using Claude Code on WSL2 with JetBrains IDEs and getting "No available IDEs detected" errors, this is likely due to WSL2's networking configuration or Windows Firewall blocking the connection.

WSL2 uses NAT networking by default, which can prevent IDE detection. You have two options:

**Option 1: Configure Windows Firewall (recommended)**
1. Find your WSL2 IP address: `wsl hostname -I` (e.g. 172.21.123.45)
2. Open PowerShell as Administrator and create a firewall rule:
   ```powershell
   New-NetFirewallRule -DisplayName "Allow WSL2 Internal Traffic" -Direction Inbound -Protocol TCP -Action Allow -RemoteAddress 172.21.0.0/16 -LocalAddress 172.21.0.0/16
```
   *(Adjust the IP range based on your WSL2 subnet from step 1)*
3. Restart both your IDE and Claude Code.

**Option 2: Switch to mirrored networking**
Add to `.wslconfig` in your Windows user directory:
```ini
[wsl2]
networkingMode=mirrored
```
Then restart WSL with `wsl --shutdown` from PowerShell.

*(Note: These networking issues only affect WSL2. WSL1 uses the host's network directly.)*

## Authentication and Tokens

### 403 Forbidden After Login
If `claude auth login` succeeds in the browser but the CLI throws a 403 Forbidden:
1. Ensure your Claude Pro or Claude Max subscription is currently active at `claude.com`. Pay-as-you-go API credits do not grant access to Claude Code.
2. Ensure you are not connected to a corporate VPN that blocks Anthropic IP addresses.

### OAuth Error: Invalid code
If you see `OAuth error: Invalid code. Please make sure the full code was copied`, the login code expired or was truncated during copy-paste.
**Fix:**
- Press Enter to retry and complete the login quickly after the browser opens.
- Type `c` to copy the full URL if the browser doesn't open automatically.
- If using a remote/SSH session, copy the URL displayed in the terminal and open it in your local browser instead.

### OAuth login fails in WSL2
Browser-based login in WSL2 may fail if WSL can't open your Windows browser.
**Fix:** Set the `BROWSER` environment variable:
```bash
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
claude
```
Or copy the URL manually: when the login prompt appears, press `c` to copy the OAuth URL, then paste it into your Windows browser.

### Repeated Permission Prompts / Token Expired
If Claude constantly asks you to re-authenticate or loses its OAuth token:
**Fix:** Your global configuration file may have incorrect permissions.
*   **Mac/Linux:** `rm -rf ~/.claude.json && claude auth login`
*   **Windows:** Delete `%USERPROFILE%\.claude.json` and re-authenticate.

## General Usage Bugs

### Escape Key Not Working (JetBrains Terminal)
The Escape key might not exit the Session Picker or autocomplete menus when running the `claude` CLI inside a JetBrains terminal tab.
**Fix:** This is caused by a keybinding clash with JetBrains' default shortcuts. To fix:
1. Go to Settings → Tools → Terminal
2. Either:
   - Uncheck "Move focus to the editor with Escape", or
   - Click "Configure terminal keybindings" and delete the "Switch focus to Editor" shortcut
3. Apply the changes
This allows the `Esc` key to properly interrupt Claude Code operations.

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