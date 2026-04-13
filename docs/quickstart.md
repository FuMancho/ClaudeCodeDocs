This quickstart guide will have you using AI-powered coding assistance in a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.


## [​](#before-you-begin #before-you-begin) Before you begin

Make sure you have:

* A terminal or command prompt open
  + If you’ve never used the terminal before, check out the [terminal guide](./terminal-guide.md)
* A code project to work with
* A [Claude subscription](https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_prereq https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_prereq) (Pro, Max, Team, or Enterprise), [Claude Console](https://console.anthropic.com/ https://console.anthropic.com/) account, or access through a [supported cloud provider](./third-party-integrations.md)

This guide covers the terminal CLI. Claude Code is also available on the [web](https://claude.ai/code https://claude.ai/code), as a [desktop app](./desktop.md), in [VS Code](./vs-code.md) and [JetBrains IDEs](./jetbrains.md), in [Slack](./slack.md), and in CI/CD with [GitHub Actions](./github-actions.md) and [GitLab](./gitlab-ci-cd.md). See [all interfaces](./overview.md#use-claude-code-everywhere).

## [​](#step-1-install-claude-code #step-1-install-claude-code) Step 1: Install Claude Code

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

If you see `The token '&&' is not a valid statement separator`, you’re in PowerShell, not CMD. Use the PowerShell command above instead. Your prompt shows `PS C:\` when you’re in PowerShell.**Windows requires [Git for Windows](https://git-scm.com/downloads/win https://git-scm.com/downloads/win).** Install it first if you don’t have it.

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

## [​](#step-2-log-in-to-your-account #step-2-log-in-to-your-account) Step 2: Log in to your account

Claude Code requires an account to use. When you start an interactive session with the `claude` command, you’ll need to log in:

```
claude
# You'll be prompted to log in on first use
```

```
/login
# Follow the prompts to log in with your account
```

You can log in using any of these account types:

* [Claude Pro, Max, Team, or Enterprise](https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_login https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_login) (recommended)
* [Claude Console](https://console.anthropic.com/ https://console.anthropic.com/) (API access with pre-paid credits). On first login, a “Claude Code” workspace is automatically created in the Console for centralized cost tracking.
* [Amazon Bedrock, Google Vertex AI, or Microsoft Foundry](./third-party-integrations.md) (enterprise cloud providers)

Once logged in, your credentials are stored and you won’t need to log in again. To switch accounts later, use the `/login` command.

## [​](#step-3-start-your-first-session #step-3-start-your-first-session) Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:

```
cd /path/to/your/project
claude
```

You’ll see the Claude Code welcome screen with your session information, recent conversations, and latest updates. Type `/help` for available commands or `/resume` to continue a previous conversation.

After logging in (Step 2), your credentials are stored on your system. Learn more in [Credential Management](./authentication.md#credential-management).

## [​](#step-4-ask-your-first-question #step-4-ask-your-first-question) Step 4: Ask your first question

Let’s start with understanding your codebase. Try one of these commands:

```
what does this project do?
```

Claude will analyze your files and provide a summary. You can also ask more specific questions:

```
what technologies does this project use?
```

```
where is the main entry point?
```

```
explain the folder structure
```

You can also ask Claude about its own capabilities:

```
what can Claude Code do?
```

```
how do I create custom skills in Claude Code?
```

```
can Claude Code work with Docker?
```

Claude Code reads your project files as needed. You don’t have to manually add context.

## [​](#step-5-make-your-first-code-change #step-5-make-your-first-code-change) Step 5: Make your first code change

Now let’s make Claude Code do some actual coding. Try a simple task:

```
add a hello world function to the main file
```

Claude Code will:

1. Find the appropriate file
2. Show you the proposed changes
3. Ask for your approval
4. Make the edit

Claude Code always asks for permission before modifying files. You can approve individual changes or enable “Accept all” mode for a session.

## [​](#step-6-use-git-with-claude-code #step-6-use-git-with-claude-code) Step 6: Use Git with Claude Code

Claude Code makes Git operations conversational:

```
what files have I changed?
```

```
commit my changes with a descriptive message
```

You can also prompt for more complex Git operations:

```
create a new branch called feature/quickstart
```

```
show me the last 5 commits
```

```
help me resolve merge conflicts
```

## [​](#step-7-fix-a-bug-or-add-a-feature #step-7-fix-a-bug-or-add-a-feature) Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation.
Describe what you want in natural language:

```
add input validation to the user registration form
```

Or fix existing issues:

```
there's a bug where users can submit empty forms - fix it
```

Claude Code will:

* Locate the relevant code
* Understand the context
* Implement a solution
* Run tests if available

## [​](#step-8-test-out-other-common-workflows #step-8-test-out-other-common-workflows) Step 8: Test out other common workflows

There are a number of ways to work with Claude:
**Refactor code**

```
refactor the authentication module to use async/await instead of callbacks
```

**Write tests**

```
write unit tests for the calculator functions
```

**Update documentation**

```
update the README with installation instructions
```

**Code review**

```
review my changes and suggest improvements
```

Talk to Claude like you would a helpful colleague. Describe what you want to achieve, and it will help you get there.

## [​](#essential-commands #essential-commands) Essential commands

Here are the most important commands for daily use:

| Command | What it does | Example |
| --- | --- | --- |
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run a one-time task | `claude "fix the build error"` |
| `claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
| `claude -c` | Continue most recent conversation in current directory | `claude -c` |
| `claude -r` | Resume a previous conversation | `claude -r` |
| `/clear` | Clear conversation history | `/clear` |
| `/help` | Show available commands | `/help` |
| `exit` or Ctrl+D | Exit Claude Code | `exit` |

See the [CLI reference](./cli-reference.md) for a complete list of commands.

## [​](#pro-tips-for-beginners #pro-tips-for-beginners) Pro tips for beginners

For more, see [best practices](./best-practices.md) and [common workflows](./common-workflows.md).

Be specific with your requests

Instead of: “fix the bug”Try: “fix the login bug where users see a blank screen after entering wrong credentials”

Use step-by-step instructions

Break complex tasks into steps:

```
1. create a new database table for user profiles
2. create an API endpoint to get and update user profiles
3. build a webpage that allows users to see and edit their information
```

Let Claude explore first

Before making changes, let Claude understand your code:

```
analyze the database schema
```

```
build a dashboard showing products that are most frequently returned by our UK customers
```

Save time with shortcuts

* Press `?` to see all available keyboard shortcuts
* Use Tab for command completion
* Press ↑ for command history
* Type `/` to see all commands and skills

## [​](#what’s-next #what’s-next) What’s next?

Now that you’ve learned the basics, explore more advanced features:

## How Claude Code works

Understand the agentic loop, built-in tools, and how Claude Code interacts with your project

## Best practices

Get better results with effective prompting and project setup

## Common workflows

Step-by-step guides for common tasks

## Extend Claude Code

Customize with CLAUDE.md, skills, hooks, MCP, and more

## [​](#getting-help #getting-help) Getting help

* **In Claude Code**: Type `/help` or ask “how do I…”
* **Documentation**: You’re here! Browse other guides
* **Community**: Join our [Discord](https://www.anthropic.com/discord https://www.anthropic.com/discord) for tips and support