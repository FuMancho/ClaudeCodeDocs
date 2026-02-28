# Jules Task Instructions — ClaudeCodeDocs

## Purpose

This repository contains community-maintained documentation for the **Anthropic Claude Code CLI** (`@anthropic-ai/claude-code`). Jules is responsible for keeping it up-to-date with the official source.

## Documentation Source

| Field | Value |
|---|---|
| Start URL | `https://code.claude.com/docs/en/cli-reference` |
| Base Path | `/docs/en/` |
| Official Domain | `docs.anthropic.com`, `code.claude.com` |

## Weekly Update Procedure

### 1. Setup

Clone the shared crawler (if not already present):

```bash
git clone https://github.com/FuMancho/DocMaintainer.git /tmp/DocMaintainer 2>/dev/null || true
```

### 2. Crawl

```bash
python3 /tmp/DocMaintainer/scripts/crawler.py \
  --start-url https://code.claude.com/docs/en/cli-reference \
  --base-path /docs/en/ \
  --output-repo . \
  --official-domains docs.anthropic.com,code.claude.com,platform.claude.com
```

This saves raw scraped text into `scraped_docs/`.

### 3. Review & Update

- Compare `scraped_docs/` content against existing files in `docs/`.
- Update any `docs/*.md` files where the official documentation has changed.
- Add new documentation files for any newly discovered pages.
- Remove documentation for pages that no longer exist upstream.

### 4. Validate

- Ensure all internal relative links resolve correctly.
- Ensure all external links point to `docs.anthropic.com` or `code.claude.com` (see Link Handling Policy below for third-party rules).
- Verify heading hierarchy (`#` → `##` → `###`, no skipped levels).
- Code blocks must specify a language (e.g., ` ```bash `).

### 5. Commit

Use this commit message format:

```
docs: weekly documentation update [automated]
```

## Formatting Standards

- **Markdown:** GitHub-flavored Markdown (`.md`).
- **Headings:** Strictly hierarchical — never skip levels.
- **Code:** Inline code uses single backticks. Code blocks use triple backticks with a language tag.
- **Callouts:** Use GitHub-style alerts (`> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`, etc.).
- **Links:** Internal links use relative paths. External links point to verified official domains.

## Link Handling Policy

This is the most important section for autonomous operation. Follow these rules exactly:

### Reference File

Always consult `docs/official-links.md` as the single source of truth for verified URLs before writing any links.

### Official Links

- **Allowed domains:** `docs.anthropic.com`, `code.claude.com`, `platform.claude.com`
- When a link can be replaced with an official equivalent from `docs/official-links.md`, do so.

### Third-Party Links — Decision Rules

| Domain Type | Action | Example |
|---|---|---|
| GitHub repos (`github.com`) | ✅ **Keep** | `github.com/anthropics/claude-code` |
| Package registries (`npmjs.com`, `pypi.org`) | ✅ **Keep** | `npmjs.com/package/@anthropic-ai/claude-code` |
| Cloud provider docs (`aws.amazon.com`, `cloud.google.com`) | ✅ **Keep** | Cloud setup guides |
| Personal blogs, Medium, Dev.to | ❌ **Remove** | Replace with official equivalent or remove entirely |
| Forums, Reddit, Stack Overflow | ❌ **Remove** | Not authoritative |
| Unofficial mirrors or aggregators | ❌ **Remove** | Not trustworthy |

### New Official Links

If the crawler discovers new official pages not yet in `docs/official-links.md`, add them to the file in the correct section.

### Dead Links

If a link returns 404 or is unreachable (check `scraped_docs/_link_audit.md`), remove it and note the removal in the commit message.

### Using the Link Audit Report

After crawling, the file `scraped_docs/_link_audit.md` contains a pre-classified list of all discovered links:
- ✅ **Official** — these are fine, no action needed
- ⚠️ **Third-party** — apply the decision rules table above
- ❌ **Dead** — remove from documentation

## Files to Ignore

Do not modify:
- `JULES.md` (this file)
- `.gitignore`
