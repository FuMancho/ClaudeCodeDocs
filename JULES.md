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

### 1. Crawl

```bash
python3 scripts/crawler.py \
  --start-url https://code.claude.com/docs/en/cli-reference \
  --base-path /docs/en/ \
  --output-repo .
```

This saves raw scraped text into `scraped_docs/`.

### 2. Review & Update

- Compare `scraped_docs/` content against existing files in `docs/`.
- Update any `docs/*.md` files where the official documentation has changed.
- Add new documentation files for any newly discovered pages.
- Remove documentation for pages that no longer exist upstream.

### 3. Validate

- Ensure all internal relative links resolve correctly.
- Ensure all external links point to `docs.anthropic.com` or `code.claude.com`.
- Verify heading hierarchy (`#` → `##` → `###`, no skipped levels).
- Code blocks must specify a language (e.g., ` ```bash `).

### 4. Commit

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

## Files to Ignore

Do not modify:
- `JULES.md` (this file)
- `scripts/crawler.py`
- `.gitignore`
