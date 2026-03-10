# Quickstart

* [Quickstart](/docs/en/quickstart)
* [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

##### Core concepts

* [How Claude Code works](/docs/en/how-claude-code-works)
* [Extend Claude Code](/docs/en/features-overview)
* [Store instructions and memories](/docs/en/memory)
* [Common workflows](/docs/en/common-workflows)
* [Best practices](/docs/en/best-practices)

##### Platforms and integrations

* [Remote Control](/docs/en/remote-control)
* [Claude Code on the web](/docs/en/claude-code-on-the-web)
* [Chrome extension (beta)](/docs/en/chrome)
* [Visual Studio Code](/docs/en/vs-code)
* [JetBrains IDEs](/docs/en/jetbrains)
* [GitHub Actions](/docs/en/github-actions)
* [GitLab CI/CD](/docs/en/gitlab-ci-cd)
* [Claude Code in Slack](/docs/en/slack)

* [Before you begin](#before-you-begin)
* [Step 1: Install Claude Code](#step-1-install-claude-code)
* [Step 2: Log in to your account](#step-2-log-in-to-your-account)
* [Step 3: Start your first session](#step-3-start-your-first-session)
* [Step 4: Ask your first question](#step-4-ask-your-first-question)
* [Step 5: Make your first code change](#step-5-make-your-first-code-change)
* [Step 6: Use Git with Claude Code](#step-6-use-git-with-claude-code)
* [Step 7: Fix a bug or add a feature](#step-7-fix-a-bug-or-add-a-feature)
* [Step 8: Test out other common workflows](#step-8-test-out-other-common-workflows)
* [Essential commands](#essential-commands)
* [Pro tips for beginners](#pro-tips-for-beginners)
* [What’s next?](#what%E2%80%99s-next)
* [Getting help](#getting-help)

This quickstart guide will have you using AI-powered coding assistance in a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.

##  Before you begin

Make sure you have:

* A terminal or command prompt open
  + If you’ve never used the terminal before, check out the [terminal guide](/docs/en/terminal-guide)
* A code project to work with
* A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise), [Claude Console](https://console.anthropic.com/) account, or access through a [supported cloud provider](/docs/en/third-party-integrations)

This guide covers the terminal CLI. Claude Code is also available on the [web](https://claude.ai/code), as a [desktop app](/docs/en/desktop), in [VS Code](/docs/en/vs-code) and [JetBrains IDEs](/docs/en/jetbrains), in [Slack](/docs/en/slack), and in CI/CD with [GitHub Actions](/docs/en/github-actions) and [GitLab](/docs/en/gitlab-ci-cd). See [all interfaces](/docs/en/overview#use-claude-code-everywhere).

##  Step 1: Install Claude Code

To install Claude Code, use one of the following methods:

* Native Install (Recommended)
* Homebrew
* WinGet

**macOS, Linux, WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```
**Windows PowerShell:**

```bash
irm https://claude.ai/install.ps1 | iex
```
**Windows CMD:**

```bash
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```
**Windows requires [Git for Windows](https://git-scm.com/downloads/win).** Install it first if you don’t have it.

Native installations automatically update in the background to keep you on the latest version.

```bash
brew install --cask claude-code
```
Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.

```bash
winget install Anthropic.ClaudeCode
```
WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

##  Step 2: Log in to your account

Claude Code requires an account to use. When you start an interactive session with the `claude` command, you’ll need to log in:

```bash
claude
# You'll be prompted to log in on first use
```
```bash
/login
# Follow the prompts to log in with your account
```
You can log in using any of these account types:

* [Claude Pro, Max, Teams, or Enterprise](https://claude.com/pricing) (recommended)
* [Claude Console](https://console.anthropic.com/) (API access with pre-paid credits). On first login, a “Claude Code” workspace is automatically created in the Console for centralized cost tracking.
* [Amazon Bedrock, Google Vertex AI, or Microsoft Foundry](/docs/en/third-party-integrations) (enterprise cloud providers)

Once logged in, your credentials are stored and you won’t need to log in again. To switch accounts later, use the `/login` command.

##  Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:

```bash
cd /path/to/your/project
claude
```
You’ll see the Claude Code welcome screen with your session information, recent conversations, and latest updates. Type `/help` for available commands or `/resume` to continue a previous conversation.

After logging in (Step 2), your credentials are stored on your system. Learn more in [Credential Management](/docs/en/authentication#credential-management).

##  Step 4: Ask your first question

Let’s start with understanding your codebase. Try one of these commands:

```bash
what does this project do?
```
Claude will analyze your files and provide a summary. You can also ask more specific questions:

```bash
what technologies does this project use?
```
```bash
where is the main entry point?
```
```bash
explain the folder structure
```
You can also ask Claude about its own capabilities:

```bash
what can Claude Code do?
```
```bash
how do I create custom skills in Claude Code?
```
```bash
can Claude Code work with Docker?
```
Claude Code reads your project files as needed. You don’t have to manually add context.

##  Step 5: Make your first code change

Now let’s make Claude Code do some actual coding. Try a simple task:

```bash
add a hello world function to the main file
```
Claude Code will:

1. Find the appropriate file
2. Show you the proposed changes
3. Ask for your approval
4. Make the edit

Claude Code always asks for permission before modifying files. You can approve individual changes or enable “Accept all” mode for a session.

##  Step 6: Use Git with Claude Code

Claude Code makes Git operations conversational:

```bash
what files have I changed?
```
```bash
commit my changes with a descriptive message
```
You can also prompt for more complex Git operations:

```bash
create a new branch called feature/quickstart
```
```bash
show me the last 5 commits
```
```bash
help me resolve merge conflicts
```
##  Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation.
Describe what you want in natural language:

```bash
add input validation to the user registration form
```
Or fix existing issues:

```bash
there's a bug where users can submit empty forms - fix it
```
Claude Code will:

* Locate the relevant code
* Understand the context
* Implement a solution
* Run tests if available

##  Step 8: Test out other common workflows

There are a number of ways to work with Claude:
**Refactor code**

```bash
refactor the authentication module to use async/await instead of callbacks
```
**Write tests**

```bash
write unit tests for the calculator functions
```
**Update documentation**

```bash
update the README with installation instructions
```
**Code review**

```bash
review my changes and suggest improvements
```
Talk to Claude like you would a helpful colleague. Describe what you want to achieve, and it will help you get there.

##  Essential commands

Here are the most important commands for daily use:

| Command | What it does | Example |
| --- | --- | --- |
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run a one-time task | `claude "fix the build error"` |
| `claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
| `claude -c` | Continue most recent conversation in current directory | `claude -c` |
| `claude -r` | Resume a previous conversation | `claude -r` |
| `claude commit` | Create a Git commit | `claude commit` |
| `/clear` | Clear conversation history | `/clear` |
| `/help` | Show available commands | `/help` |
| `exit` or Ctrl+C | Exit Claude Code | `exit` |

See the [CLI reference](/docs/en/cli-reference) for a complete list of commands.

##  Pro tips for beginners

For more, see [best practices](/docs/en/best-practices) and [common workflows](/docs/en/common-workflows).

Be specific with your requests

Instead of: “fix the bug”Try: “fix the login bug where users see a blank screen after entering wrong credentials”

Use step-by-step instructions

Break complex tasks into steps:

```bash
1. create a new database table for user profiles
2. create an API endpoint to get and update user profiles
3. build a webpage that allows users to see and edit their information
```
Let Claude explore first

Before making changes, let Claude understand your code:

```bash
analyze the database schema
```
```bash
build a dashboard showing products that are most frequently returned by our UK customers
```
Save time with shortcuts

* Press `?` to see all available keyboard shortcuts
* Use Tab for command completion
* Press ↑ for command history
* Type `/` to see all commands and skills

##  What’s next?

Now that you’ve learned the basics, explore more advanced features:

[## How Claude Code works

Understand the agentic loop, built-in tools, and how Claude Code interacts with your project](/docs/en/how-claude-code-works)[## Best practices

Get better results with effective prompting and project setup](/docs/en/best-practices)[## Common workflows

Step-by-step guides for common tasks](/docs/en/common-workflows)[## Extend Claude Code

Customize with CLAUDE.md, skills, hooks, MCP, and more](/docs/en/features-overview)

##  Getting help

* **In Claude Code**: Type `/help` or ask “how do I…”
* **Documentation**: You’re here! Browse other guides
* **Community**: Join our [Discord](https://www.anthropic.com/discord) for tips and support

[Overview](/docs/en/overview)[Changelog](/docs/en/changelog)