# Advanced Setup and Environments

Claude Code is versatile and operates across various environments, from local terminals to cloud sandbox infrastructure.

## Configuration Settings
Settings in Claude Code operate on multiple scopes (Project Level vs. Global User Level). You can configure behavior by establishing JSON rules.

### Settings Precedence
1. Command Line Flags (Highest priority, overrides everything)
2. Project `CLAUDE.md` / `.claude.json` (Overrides global)
3. Global User `~/.claude.json`
4. Default fallback behaviors

### Environment Variables
You can bypass files entirely for containerized setups:
*   `CLAUDE_CONFIG_DIR`: The directory used to store OAuth tokens and global settings (defaults to user home).
*   `CLAUDE_LOG_LEVEL`: Set to `debug`, `info`, `warn`, or `error` to increase the verbosity of the internal agentic loop logs.

---

## Editor & Desktop Integrations

### VS Code & Cursor Extension
While the CLI offers the most power, the `anthropic.claude-code` extension brings Claude natively into your editor.
**Extension vs. CLI:**
*   **Extension:** Better for inline diffs, highlighting specific functions, and `@` mentioning open tabs visually.
*   **CLI:** Better for Safe Autonomous Mode (`--dangerously-skip-permissions`), running automated bash scripts, and parallel git worktrees. 
You can use both simultaneously. Changes made by the extension are visible to the CLI's file context automatically.

### Claude Code Desktop App
Anthropic offers a native Desktop Application (macOS and Windows) focused on dedicated windows for extended thinking tasks. If you install the desktop app, it interfaces with the same global `.claude.json` token as the terminal CLI.

---

## Claude Code on the Web (Asynchronous Cloud)

For enterprises or secure tasks that require isolated networking, you can run Claude Code "on the web."

### What is the Web Infrastructure?
Instead of executing tools locally on your Macbook, Claude Code on the Web provisions a secure, ephemeral cloud server. The Agentic Loop runs there.
*   **Default Image**: The server boots with a standard Debian image loaded with standard utilities (`curl`, `git`, `python`, `node`, `jq`).
*   **Dependency Management**: You can instruct Claude to `apt install` or `pip install` temporary dependencies inside the cloud sandbox to test code before writing it back to your repository.

### Sharing Sessions
Because the loop runs in the cloud, you can generate a shareable web link for a specific session. This allows other team members to view the exact agentic steps Claude took to fix a bug or architect a feature, vastly improving pull request reviews.
