# Advanced setup - Claude Code Docs

This page covers system requirements, platform-specific installation details, updates, and uninstallation. For a guided walkthrough of your first session, see the [quickstart](./quickstart.md). If you’ve never used a terminal before, see the [terminal guide](./terminal-guide.md).

## [​](#system-requirements) System requirements

Claude Code runs on the following platforms and configurations:

* **Operating system**:
  + macOS 13.0+
  + Windows 10 1809+ or Windows Server 2019+
  + Ubuntu 20.04+
  + Debian 10+
  + Alpine Linux 3.19+
* **Hardware**: 4 GB+ RAM, x64 or ARM64 processor
* **Network**: internet connection required. See [network configuration](./network-config.md#network-access-requirements).
* **Shell**: Bash, Zsh, PowerShell, or CMD. Native Windows setups require Git for Windows. WSL setups do not.
* **Location**: Anthropic supported countries

### [​](#additional-dependencies) Additional dependencies

* **ripgrep**: usually included with Claude Code. If search fails, see [search troubleshooting](./troubleshooting.md#search-and-discovery-issues).

## [​](#install-claude-code) Install Claude Code

Prefer a graphical interface? The [Desktop app](./desktop-quickstart.md) lets you use Claude Code without the terminal. Download it for macOS or Windows.New to the terminal? See the [terminal guide](./terminal-guide.md) for step-by-step instructions.

To install Claude Code, use one of the following methods:

* Native Install (Recommended)
* Homebrew
* WinGet

**macOS, Linux, WSL:**

```
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

If you see `The token '&&' is not a valid statement separator`, you’re in PowerShell, not CMD. If you see `'irm' is not recognized as an internal or external command`, you’re in CMD, not PowerShell. Your prompt shows `PS C:\` when you’re in PowerShell and `C:\` without the `PS` when you’re in CMD.**Native Windows setups require Git for Windows.** Install it first if you don’t have it. WSL setups do not need it.

Native installations automatically update in the background to keep you on the latest version.

```
brew install --cask claude-code
```

Homebrew offers two casks. `claude-code` tracks the stable release channel, which is typically about a week behind and skips releases with major regressions. `claude-code@latest` tracks the latest channel and receives new versions as soon as they ship.

Homebrew installations do not auto-update. Run `brew upgrade claude-code` or `brew upgrade claude-code@latest`, depending on which cask you installed, to get the latest features and security fixes.

```
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

After installation completes, open a terminal in the project you want to work in and start Claude Code:

```
claude
```

If you encounter any issues during installation, see the [troubleshooting guide](./troubleshooting.md).

### [​](#set-up-on-windows) Set up on Windows

You can run Claude Code natively on Windows or inside WSL. Pick based on where your projects are located and which features you need:

| Option | Requires | [Sandboxing](./sandboxing.md) | When to use |
| --- | --- | --- | --- |
| Native Windows | Git for Windows | Not supported | Windows-native projects and tools |
| WSL 2 | WSL 2 enabled | Supported | Linux toolchains or sandboxed command execution |
| WSL 1 | WSL 1 enabled | Not supported | If WSL 2 is unavailable |

**Option 1: Native Windows with Git Bash**
Install Git for Windows, then run the install command from PowerShell or CMD. You do not need to run as Administrator.
Whether you install from PowerShell or CMD only affects which install command you run. Your prompt shows `PS C:\Users\YourName>` in PowerShell and `C:\Users\YourName>` without the `PS` in CMD. If you’re new to the terminal, the [terminal guide](./terminal-guide.md#windows) walks through each step.
After installation, launch `claude` from PowerShell, CMD, or Git Bash. Claude Code uses Git Bash internally to execute commands regardless of where you launched it. If Claude Code can’t find your Git Bash installation, set the path in your [settings.json file](./settings.md):

```
{
  "env": {
    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
  }
}
```

Claude Code can also run PowerShell natively on Windows. The PowerShell tool is rolling out progressively; set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` to opt in or `0` to opt out. See [PowerShell tool](./tools-reference.md#powershell-tool) for setup and limitations.
**Option 2: WSL**
Open your WSL distribution and run the Linux installer from the [install instructions](#install-claude-code) above. You install and launch `claude` inside the WSL terminal, not from PowerShell or CMD.

### [​](#alpine-linux-and-musl-based-distributions) Alpine Linux and musl-based distributions

The native installer on Alpine and other musl/uClibc-based distributions requires `libgcc`, `libstdc++`, and `ripgrep`. Install these using your distribution’s package manager, then set `USE_BUILTIN_RIPGREP=0`.
This example installs the required packages on Alpine:

```
apk add libgcc libstdc++ ripgrep
```

Then set `USE_BUILTIN_RIPGREP` to `0` in your [`settings.json`](./settings.md#available-settings) file:

```
{
  "env": {
    "USE_BUILTIN_RIPGREP": "0"
  }
}
```

## [​](#verify-your-installation) Verify your installation

After installing, confirm Claude Code is working:

```
claude --version
```

For a more detailed check of your installation and configuration, run [`claude doctor`](./troubleshooting.md#get-more-help):

```
claude doctor
```

## [​](#authenticate) Authenticate

Claude Code requires a Pro, Max, Team, Enterprise, or Console account. The free Claude.ai plan does not include Claude Code access. You can also use Claude Code with a third-party API provider like [Amazon Bedrock](./amazon-bedrock.md), [Google Vertex AI](./google-vertex-ai.md), or [Microsoft Foundry](./microsoft-foundry.md).
After installing, log in by running `claude` and following the browser prompts. See [Authentication](./authentication.md) for all account types and team setup options.

## [​](#update-claude-code) Update Claude Code

Native installations automatically update in the background. You can [configure the release channel](#configure-release-channel) to control whether you receive updates immediately or on a delayed stable schedule, or [disable auto-updates](#disable-auto-updates) entirely. Homebrew and WinGet installations require manual updates.

### [​](#auto-updates) Auto-updates

Claude Code checks for updates on startup and periodically while running. Updates download and install in the background, then take effect the next time you start Claude Code.

Homebrew and WinGet installations do not auto-update. For Homebrew, run `brew upgrade claude-code` or `brew upgrade claude-code@latest`, depending on which cask you installed. For WinGet, run `winget upgrade Anthropic.ClaudeCode`.**Known issue:** Claude Code may notify you of updates before the new version is available in these package managers. If an upgrade fails, wait and try again later.Homebrew keeps old versions on disk after upgrades. Run `brew cleanup` periodically to reclaim disk space.

### [​](#configure-release-channel) Configure release channel

Control which release channel Claude Code follows for auto-updates and `claude update` with the `autoUpdatesChannel` setting:

* `"latest"`, the default: receive new features as soon as they’re released
* `"stable"`: use a version that is typically about one week old, skipping releases with major regressions

Configure this via `/config` → **Auto-update channel**, or add it to your [settings.json file](./settings.md):

```
{
  "autoUpdatesChannel": "stable"
}
```

For enterprise deployments, you can enforce a consistent release channel across your organization using [managed settings](./permissions.md#managed-settings).
Homebrew installations choose a channel by cask name instead of this setting: `claude-code` tracks stable and `claude-code@latest` tracks latest.

### [​](#pin-a-minimum-version) Pin a minimum version

The `minimumVersion` setting establishes a floor. Background auto-updates and `claude update` refuse to install any version below this value, so moving to the `"stable"` channel does not downgrade you if you are already on a newer `"latest"` build.
Switching from `"latest"` to `"stable"` via `/config` prompts you to either stay on the current version or allow the downgrade. Choosing to stay sets `minimumVersion` to that version. Switching back to `"latest"` clears it.
Add it to your [settings.json file](./settings.md) to pin a floor explicitly:

```
{
  "autoUpdatesChannel": "stable",
  "minimumVersion": "2.1.100"
}
```

In [managed settings](./permissions.md#managed-settings), this enforces an organization-wide minimum that user and project settings cannot override.

### [​](#disable-auto-updates) Disable auto-updates

Set `DISABLE_AUTOUPDATER` to `"1"` in the `env` key of your [`settings.json`](./settings.md#available-settings) file:

```
{
  "env": {
    "DISABLE_AUTOUPDATER": "1"
  }
}
```

### [​](#update-manually) Update manually

To apply an update immediately without waiting for the next background check, run:

```
claude update
```

## [​](#advanced-installation-options) Advanced installation options

These options are for version pinning, migrating from npm, and verifying binary integrity.

### [​](#install-a-specific-version) Install a specific version

The native installer accepts either a specific version number or a release channel (`latest` or `stable`). The channel you choose at install time becomes your default for auto-updates. See [configure release channel](#configure-release-channel) for more information.
To install the latest version (default):

* macOS, Linux, WSL
* Windows PowerShell
* Windows CMD

```
curl -fsSL https://claude.ai/install.sh | bash
```

```
irm https://claude.ai/install.ps1 | iex
```

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

To install the stable version:

* macOS, Linux, WSL
* Windows PowerShell
* Windows CMD

```
curl -fsSL https://claude.ai/install.sh | bash -s stable
```

```
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) stable
```

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd stable && del install.cmd
```

To install a specific version number:

* macOS, Linux, WSL
* Windows PowerShell
* Windows CMD

```
curl -fsSL https://claude.ai/install.sh | bash -s 2.1.89
```

```
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 2.1.89
```

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 2.1.89 && del install.cmd
```

### [​](#install-with-npm) Install with npm

You can also install Claude Code as a global npm package. The package requires Node.js 18 or later.

```
npm install -g @anthropic-ai/claude-code
```

The npm package installs the same native binary as the standalone installer. npm pulls the binary in through a per-platform optional dependency such as `@anthropic-ai/claude-code-darwin-arm64`, and a postinstall step links it into place. The installed `claude` binary does not itself invoke Node.
Supported npm install platforms are `darwin-arm64`, `darwin-x64`, `linux-x64`, `linux-arm64`, `linux-x64-musl`, `linux-arm64-musl`, `win32-x64`, and `win32-arm64`. Your package manager must allow optional dependencies. See [troubleshooting](./troubleshooting.md#native-binary-not-found-after-npm-install) if the binary is missing after install.

Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks. If you encounter permission errors, see [troubleshooting permission errors](./troubleshooting.md#permission-errors-during-installation).

### [​](#binary-integrity-and-code-signing) Binary integrity and code signing

Each release publishes a `manifest.json` containing SHA256 checksums for every platform binary. The manifest is signed with an Anthropic GPG key, so verifying the signature on the manifest transitively verifies every binary it lists.

#### [​](#verify-the-manifest-signature) Verify the manifest signature

Steps 1-3 require a POSIX shell with `gpg` and `curl`. On Windows, run them in Git Bash or WSL. Step 4 includes a PowerShell option.

1

Download and import the public key

The release signing key is published at a fixed URL.

```
curl -fsSL https://downloads.claude.ai/keys/claude-code.asc | gpg --import
```

Display the fingerprint of the imported key.

```
gpg --fingerprint security@anthropic.com
```

Confirm the output includes this fingerprint:

```
31DD DE24 DDFA B679 F42D  7BD2 BAA9 29FF 1A7E CACE
```

2

Download the manifest and signature

Set `VERSION` to the release you want to verify.

```
REPO=https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases
VERSION=2.1.89
curl -fsSLO "$REPO/$VERSION/manifest.json"
curl -fsSLO "$REPO/$VERSION/manifest.json.sig"
```

3

Verify the signature

Verify the detached signature against the manifest.

```
gpg --verify manifest.json.sig manifest.json
```

A valid result reports `Good signature from "Anthropic Claude Code Release Signing <security@anthropic.com>"`.`gpg` also prints `WARNING: This key is not certified with a trusted signature!` for any freshly imported key. This is expected. The `Good signature` line confirms the cryptographic check passed. The fingerprint comparison in Step 1 confirms the key itself is authentic.

4

Check the binary against the manifest

Compare the SHA256 checksum of your downloaded binary with the value listed under `platforms.<platform>.checksum` in `manifest.json`.

* Linux
* macOS
* Windows PowerShell

```
sha256sum claude
```

```
shasum -a 256 claude
```

```
(Get-FileHash claude.exe -Algorithm SHA256).Hash.ToLower()
```

Manifest signatures are available for releases from `2.1.89` onward. Earlier releases publish checksums in `manifest.json` without a detached signature.

#### [​](#platform-code-signatures) Platform code signatures

In addition to the signed manifest, individual binaries carry platform-native code signatures where supported.

* **macOS**: signed by “Anthropic PBC” and notarized by Apple. Verify with `codesign --verify --verbose ./claude`.
* **Windows**: signed by “Anthropic, PBC”. Verify with `Get-AuthenticodeSignature .\claude.exe`.
* **Linux**: use the manifest signature above to verify integrity. Linux binaries are not individually code-signed.

## [​](#uninstall-claude-code) Uninstall Claude Code

To remove Claude Code, follow the instructions for your installation method.

### [​](#native-installation) Native installation

Remove the Claude Code binary and version files:

* macOS, Linux, WSL
* Windows PowerShell

```
rm -f ~/.local/bin/claude
rm -rf ~/.local/share/claude
```

```
Remove-Item -Path "$env:USERPROFILE\.local\bin\claude.exe" -Force
Remove-Item -Path "$env:USERPROFILE\.local\share\claude" -Recurse -Force
```

### [​](#homebrew-installation) Homebrew installation

Remove the Homebrew cask you installed. If you installed the stable cask:

```
brew uninstall --cask claude-code
```

If you installed the latest cask:

```
brew uninstall --cask claude-code@latest
```

### [​](#winget-installation) WinGet installation

Remove the WinGet package:

```
winget uninstall Anthropic.ClaudeCode
```

### [​](#npm) npm

Remove the global npm package:

```
npm uninstall -g @anthropic-ai/claude-code
```

### [​](#remove-configuration-files) Remove configuration files

Removing configuration files will delete all your settings, allowed tools, MCP server configurations, and session history.

The VS Code extension, the JetBrains plugin, and the Desktop app also write to `~/.claude/`. If any of them is still installed, the directory is recreated the next time it runs. To remove Claude Code completely, uninstall the [VS Code extension](./vs-code.md#uninstall-the-extension), the JetBrains plugin, and the Desktop app before deleting these files.
To remove Claude Code settings and cached data:

* macOS, Linux, WSL
* Windows PowerShell

```
# Remove user settings and state
rm -rf ~/.claude
rm ~/.claude.json

# Remove project-specific settings (run from your project directory)
rm -rf .claude
rm -f .mcp.json
```

```
# Remove user settings and state
Remove-Item -Path "$env:USERPROFILE\.claude" -Recurse -Force
Remove-Item -Path "$env:USERPROFILE\.claude.json" -Force

# Remove project-specific settings (run from your project directory)
Remove-Item -Path ".claude" -Recurse -Force
Remove-Item -Path ".mcp.json" -Force
```
