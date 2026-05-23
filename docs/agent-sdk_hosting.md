# Agent Sdk Hosting

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt "https://code.claude.com/docs/llms.txt")
>
> Use this file to discover all available pages before exploring further.

The Claude Agent SDK differs from traditional stateless LLM APIs in that it maintains conversational state and executes commands in a persistent environment. This guide covers the architecture, hosting considerations, and best practices for deploying SDK-based agents in production.

For security hardening beyond basic sandboxing (including network controls, credential management, and isolation options), see [Secure Deployment](./agent-sdk_secure-deployment "_agent-sdk_secure-deployment".md).

## [​](#hosting-requirements "#hosting-requirements") Hosting Requirements

### [​](#container-based-sandboxing "#container-based-sandboxing") Container-Based Sandboxing

For security and isolation, the SDK should run inside a sandboxed container environment. This provides process isolation, resource limits, network control, and ephemeral filesystems.
The SDK also supports [programmatic sandbox configuration](./agent-sdk_typescript#sandboxsettings "_agent-sdk_typescript#sandboxsettings".md) for command execution.

### [​](#system-requirements "#system-requirements") System Requirements

Each SDK instance requires:

* **Runtime dependencies**
  + Python 3.10+ for the Python SDK, or Node.js 18+ for the TypeScript SDK
  + Both SDK packages bundle a native Claude Code binary for the host platform, so no separate Claude Code or Node.js install is needed for the spawned CLI
* **Resource allocation**
  + Recommended: 1GiB RAM, 5GiB of disk, and 1 CPU (vary this based on your task as needed)
* **Network access**
  + Outbound HTTPS to `api.anthropic.com`
  + Optional: Access to MCP servers or external tools

## [​](#understanding-the-sdk-architecture "#understanding-the-sdk-architecture") Understanding the SDK Architecture

Unlike stateless API calls, the Claude Agent SDK operates as a **long-running process** that:

* **Executes commands** in a persistent shell environment
* **Manages file operations** within a working directory
* **Handles tool execution** with context from previous interactions

## [​](#sandbox-provider-options "#sandbox-provider-options") Sandbox Provider Options

Several providers specialize in secure container environments for AI code execution:

* **[Modal Sandbox](https://modal.com/docs/guide/sandbox "https://modal.com/docs/guide/sandbox")** - [demo implementation](https://modal.com/docs/examples/claude-slack-gif-creator "https://modal.com/docs/examples/claude-slack-gif-creator")
* **[Cloudflare Sandboxes](https://github.com/cloudflare/sandbox-sdk "https://github.com/cloudflare/sandbox-sdk")**
* **[Daytona](https://www.daytona.io/ "https://www.daytona.io/")**
* **[E2B](https://e2b.dev/ "https://e2b.dev/")**
* **[Fly Machines](https://fly.io/docs/machines/ "https://fly.io/docs/machines/")**
* **[Vercel Sandbox](https://vercel.com/docs/functions/sandbox "https://vercel.com/docs/functions/sandbox")**

For self-hosted options (Docker, gVisor, Firecracker) and detailed isolation configuration, see [Isolation Technologies](./agent-sdk_secure-deployment#isolation-technologies "_agent-sdk_secure-deployment#isolation-technologies".md).

## [​](#production-deployment-patterns "#production-deployment-patterns") Production Deployment Patterns

### [​](#pattern-1-ephemeral-sessions "#pattern-1-ephemeral-sessions") Pattern 1: Ephemeral Sessions

Create a new container for each user task, then destroy it when complete.
Best for one-off tasks, the user may still interact with the AI while the task is completing, but once completed the container is destroyed.
**Examples:**

* Bug Investigation & Fix: Debug and resolve a specific issue with relevant context
* Invoice Processing: Extract and structure data from receipts/invoices for accounting systems
* Translation Tasks: Translate documents or content batches between languages
* Image/Video Processing: Apply transformations, optimizations, or extract metadata from media files

### [​](#pattern-2-long-running-sessions "#pattern-2-long-running-sessions") Pattern 2: Long-Running Sessions

Maintain persistent container instances for long running tasks. Often times running *multiple* Claude Agent processes inside of the container based on demand.
Best for proactive agents that take action without the users input, agents that serve content or agents that process high amounts of messages.
**Examples:**

* Email Agent: Monitors incoming emails and autonomously triages, responds, or takes actions based on content
* Site Builder: Hosts custom websites per user with live editing capabilities served through container ports
* High-Frequency Chat Bots: Handles continuous message streams from platforms like Slack where rapid response times are critical

### [​](#pattern-3-hybrid-sessions "#pattern-3-hybrid-sessions") Pattern 3: Hybrid Sessions

Ephemeral containers that are hydrated with history and state, possibly from a database or from the SDK’s session resumption features.
Best for containers with intermittent interaction from the user that kicks off work and spins down when the work is completed but can be continued.
**Examples:**

* Personal Project Manager: Helps manage ongoing projects with intermittent check-ins, maintains context of tasks, decisions, and progress
* Deep Research: Conducts multi-hour research tasks, saves findings and resumes investigation when user returns
* Customer Support Agent: Handles support tickets that span multiple interactions, loads ticket history and customer context

### [​](#pattern-4-single-containers "#pattern-4-single-containers") Pattern 4: Single Containers

Run multiple Claude Agent SDK processes in one global container.
Best for agents that must collaborate closely together. This is likely the least popular pattern because you will have to prevent agents from overwriting each other.
**Examples:**

* **Simulations**: Agents that interact with each other in simulations such as video games.

## [​](#faq "#faq") FAQ

### [​](#how-do-i-communicate-with-my-sandboxes "#how-do-i-communicate-with-my-sandboxes") How do I communicate with my sandboxes?

When hosting in containers, expose ports to communicate with your SDK instances. Your application can expose HTTP/WebSocket endpoints for external clients while the SDK runs internally within the container.

### [​](#what-is-the-cost-of-hosting-a-container "#what-is-the-cost-of-hosting-a-container") What is the cost of hosting a container?

The dominant cost of serving agents is the tokens; containers vary based on what you provision, but a minimum cost is roughly 5 cents per hour running.

### [​](#when-should-i-shut-down-idle-containers-vs-keeping-them-warm "#when-should-i-shut-down-idle-containers-vs-keeping-them-warm") When should I shut down idle containers vs. keeping them warm?

This is likely provider dependent, different sandbox providers will let you set different criteria for idle timeouts after which a sandbox might spin down.
You will want to tune this timeout based on how frequent you think user response might be.

### [​](#how-often-should-i-update-the-claude-code-cli "#how-often-should-i-update-the-claude-code-cli") How often should I update the Claude Code CLI?

The Claude Code CLI is versioned with semver, so any breaking changes will be versioned.

### [​](#how-do-i-monitor-container-health-and-agent-performance "#how-do-i-monitor-container-health-and-agent-performance") How do I monitor container health and agent performance?

Since containers are just servers the same logging infrastructure you use for the backend will work for containers.

### [​](#how-long-can-an-agent-session-run-before-timing-out "#how-long-can-an-agent-session-run-before-timing-out") How long can an agent session run before timing out?

An agent session will not timeout, but consider setting a ‘maxTurns’ property to prevent Claude from getting stuck in a loop.

## [​](#next-steps "#next-steps") Next Steps

* [Secure Deployment](./agent-sdk_secure-deployment "_agent-sdk_secure-deployment".md) - Network controls, credential management, and isolation hardening
* [TypeScript SDK - Sandbox Settings](./agent-sdk_typescript#sandboxsettings "_agent-sdk_typescript#sandboxsettings".md) - Configure sandbox programmatically
* [Sessions Guide](./agent-sdk_sessions "_agent-sdk_sessions".md) - Learn about session management
* [Permissions](./agent-sdk_permissions "_agent-sdk_permissions".md) - Configure tool permissions
* [Cost Tracking](./agent-sdk_cost-tracking "_agent-sdk_cost-tracking".md) - Monitor API usage
* [MCP Integration](./agent-sdk_mcp "_agent-sdk_mcp".md) - Extend with custom tools