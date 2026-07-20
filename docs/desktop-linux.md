# Desktop-Linux

Linux support for the Claude desktop app is in beta. The Chat, Cowork, and Code tabs are all available.

The desktop app on Linux gives you the same Chat, Cowork, and Claude Code experience as macOS and Windows: parallel sessions, visual diff review, an integrated terminal and editor, and live app preview. See [Use Claude Code Desktop](./desktop "._desktop".md) for the full feature reference.

## [​](#requirements "#requirements") Requirements

* Ubuntu 22.04 or later, or Debian 12 or later
* x86\_64 or arm64

Other Debian-based distributions that meet these requirements may work but aren’t officially tested.

## [​](#install "#install") Install

Install from Anthropic’s apt repository so that updates arrive through your system’s regular package updates. Open a terminal and run the commands in each step.

1

Add Anthropic's apt repository

This step downloads the signing key with `curl`, which fresh Debian and Ubuntu installations may not include. If the download command fails with `sudo: curl: command not found`, install curl first:

```text
sudo apt install curl
```

Download Anthropic’s signing key:

```text
sudo curl -fsSLo /usr/share/keyrings/claude-desktop-archive-keyring.asc https://downloads.claude.ai/claude-desktop/key.asc
```

Register the repository:

```text
echo "deb [arch=amd64,arm64 signed-by=/usr/share/keyrings/claude-desktop-archive-keyring.asc] https://downloads.claude.ai/claude-desktop/apt/stable stable main" | sudo tee /etc/apt/sources.list.d/claude-desktop.list
```

2

Install the package

```text
sudo apt update && sudo apt install claude-desktop
```

3

Launch and sign in

Launch **Claude** from your application launcher, or run `claude-desktop` from a terminal, and sign in with your Anthropic account.The Linux app signs in the same way as on macOS and Windows: with a claude.ai subscription, or through your organization’s SSO. Desktop doesn’t accept a Claude Console API key directly; use the [CLI](./quickstart "._quickstart".md) for API-key authentication. For enterprise deployments that route Desktop to Google Cloud’s Agent Platform or an LLM gateway, see [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview "https://claude.com/docs/third-party/claude-desktop/overview") and [network configuration](./network-config "._network-config".md).

Verify the signing key

You can confirm the downloaded signing key belongs to Anthropic:

```text
gpg --show-keys /usr/share/keyrings/claude-desktop-archive-keyring.asc
```

The fingerprint should be `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`.

### [​](#install-from-a-downloaded-file "#install-from-a-downloaded-file") Install from a downloaded file

If you can’t install through the apt repository, download the `.deb` package directly from the repository’s package pool. This command looks up the newest package for your architecture in the repository index, then downloads it to the current directory:

```text
curl -fLO "https://downloads.claude.ai/claude-desktop/apt/stable/$(curl -s "https://downloads.claude.ai/claude-desktop/apt/stable/dists/stable/main/binary-$(dpkg --print-architecture)/Packages" | grep '^Filename: pool/main/c/claude-desktop/claude-desktop_' | sort -V | tail -n 1 | cut -d' ' -f2)"
```

If the command fails with `Remote file name has no length`, the lookup returned no package path. This can mean the repository index couldn’t be fetched, for example when your network blocks `downloads.claude.ai`, or that no package exists for your architecture. Confirm that your network can reach `downloads.claude.ai` and that `dpkg --print-architecture` prints `amd64` or `arm64`; the repository doesn’t publish packages for other architectures.
Then open the downloaded file with your software installer, such as GNOME Software, or install it with apt from the directory that contains the downloaded file:

```text
sudo apt install ./claude-desktop_*.deb
```

If apt reports `E: Unsupported file ./claude-desktop_*.deb given on commandline`, the pattern didn’t match a `.deb` file in the current directory. Confirm the download completed, then run the command again from the directory that contains the file.
A `.deb` installed this way doesn’t receive updates. To get updates through apt, register the repository from the [Add Anthropic’s apt repository](#install "#install") step. The package also writes a commented-out repository entry to `/etc/apt/sources.list.d/claude-desktop.list`; uncommenting its `deb` line is equivalent.

## [​](#update "#update") Update

The desktop app doesn’t update itself on Linux. Updates arrive with your system’s regular package updates:

```text
sudo apt update && sudo apt upgrade
```

Your distribution’s graphical software updater will also pick up new versions.

## [​](#uninstall "#uninstall") Uninstall

```text
sudo apt remove claude-desktop
```

This removes the signing key along with the app, so if you added the repository entry during install, remove it too:

```text
sudo rm /etc/apt/sources.list.d/claude-desktop.list
```

## [​](#troubleshoot "#troubleshoot") Troubleshoot

### [​](#unable-to-locate-package-claude-desktop "#unable-to-locate-package-claude-desktop") Unable to locate package claude-desktop

If `sudo apt install claude-desktop` fails with `E: Unable to locate package claude-desktop`, apt didn’t find the repository you added. Check the following:

* Confirm the repository entry was written. `cat /etc/apt/sources.list.d/claude-desktop.list` should show the `deb` line from the [Add Anthropic’s apt repository](#install "#install") step. If the file is empty or missing, run that step again.
* Confirm your architecture is supported. `dpkg --print-architecture` should print `amd64` or `arm64`. The repository doesn’t publish packages for other architectures.
* Run `sudo apt update` again and check its output for errors related to `downloads.claude.ai`. A network or key error there means the repository was added but couldn’t be reached or verified.

If the repository is in place and reachable and the package is still not found, [install from a downloaded file](#install-from-a-downloaded-file "#install-from-a-downloaded-file") instead.

## [​](#what’s-not-in-the-linux-beta-yet "#what’s-not-in-the-linux-beta-yet") What’s not in the Linux beta yet

* **Computer Use**: [app and screen control](./desktop#let-claude-use-your-computer "._desktop#let-claude-use-your-computer".md) isn’t available on Linux.
* **Dictation**: voice input isn’t available in the Linux desktop app. Use [voice dictation](./voice-dictation "._voice-dictation".md) in the CLI instead.
* **Quick Entry global hotkey**: works on X11. On native Wayland it requires your desktop environment’s GlobalShortcuts portal.
* **Fedora and RHEL**: only Debian-based distributions are supported today. Support for additional distributions is coming in the future.

For anything not yet available in the desktop app, the [CLI](./quickstart "._quickstart".md) runs the same Claude Code engine and supports a wider range of Linux distributions; see the [system requirements](./setup#system-requirements "._setup#system-requirements".md).