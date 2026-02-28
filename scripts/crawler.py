"""
DocMaintainer Web Crawler
=========================
A zero-dependency Python web crawler for scraping documentation sites.
Traverses pages within a given URL boundary and saves their text content
to a local directory for offline reference and analysis.

Usage:
    python crawler.py --start-url <URL> --base-path <PATH> --output-repo <DIR>

Examples:
    python crawler.py --start-url https://code.claude.com/docs/en/cli-reference --base-path /docs/en/ --output-repo ClaudeCodeDocs
    python crawler.py --start-url https://geminicli.com/docs/ --base-path /docs/ --output-repo GeminiDocs
    python crawler.py --start-url https://developers.openai.com/codex/cli/ --base-path /codex/cli/ --output-repo CodexDocs
"""

import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from html.parser import HTMLParser
import time
import argparse
import json
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# HTML Parser
# ---------------------------------------------------------------------------

class DocParser(HTMLParser):
    """Extracts text content and href links from an HTML page."""

    IGNORE_TAGS = frozenset({
        "script", "style", "nav", "footer", "header",
        "noscript", "svg", "iframe", "button", "form",
    })
    SKIP_SCHEMES = ("javascript:", "mailto:", "tel:", "#", "data:")

    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.links: list[str] = []
        self.text_parts: list[str] = []
        self._tag_stack: list[str] = []
        self._inside_ignored = 0  # depth counter for nested ignored tags

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        self._tag_stack.append(tag)
        if tag in self.IGNORE_TAGS:
            self._inside_ignored += 1

        if tag == "a":
            href = dict(attrs).get("href")
            if href and not href.startswith(self.SKIP_SCHEMES):
                full_url, _ = urllib.parse.urldefrag(
                    urllib.parse.urljoin(self.base_url, href)
                )
                self.links.append(full_url)

    def handle_endtag(self, tag: str):
        # Pop back to the matching tag (handles self-closing quirks)
        while self._tag_stack:
            popped = self._tag_stack.pop()
            if popped in self.IGNORE_TAGS:
                self._inside_ignored = max(0, self._inside_ignored - 1)
            if popped == tag:
                break

    def handle_data(self, data: str):
        if self._inside_ignored > 0:
            return
        text = data.strip()
        if text:
            self.text_parts.append(text)

    @property
    def text(self) -> str:
        return "\n".join(self.text_parts)


# ---------------------------------------------------------------------------
# URL helpers
# ---------------------------------------------------------------------------

def normalize_url(url: str) -> str:
    """Canonical form for comparison: lowercase scheme+host, strip trailing slash."""
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((
        parsed.scheme.lower(),
        parsed.netloc.lower(),
        parsed.path.rstrip("/") or "/",
        parsed.params,
        parsed.query,
        "",  # drop fragment
    ))


def make_filename(url: str, base_path: str) -> str:
    """Derive a safe, readable filename from a URL path."""
    path = urllib.parse.urlparse(url).path
    relative = path.replace(base_path, "", 1).strip("/")
    if not relative:
        return "index.txt"
    return relative.replace("/", "_") + ".txt"


# ---------------------------------------------------------------------------
# Crawler
# ---------------------------------------------------------------------------

def crawl_docs(
    start_url: str,
    base_path: str,
    output_dir_name: str,
    max_pages: int = 100,
    delay: float = 0.5,
) -> dict:
    """
    Crawl documentation pages starting from *start_url*, restricting
    discovered links to those whose path begins with *base_path*.

    Returns a summary dict with stats about the crawl.
    """
    parsed_start = urllib.parse.urlparse(start_url)
    base_prefix = f"{parsed_start.scheme}://{parsed_start.netloc}{base_path}"

    queue: list[str] = [start_url]
    visited: set[str] = set()          # normalized URLs
    visited_original: list[str] = []   # original URLs in visit order
    errors: list[dict] = []

    # Resolve output directory relative to the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_dir = os.path.join(project_root, output_dir_name, "scraped_docs")
    os.makedirs(output_dir, exist_ok=True)

    # Header
    print("=" * 60)
    print("  DocMaintainer Web Crawler")
    print("=" * 60)
    print(f"  Start URL   : {start_url}")
    print(f"  Boundary    : {base_prefix}")
    print(f"  Output      : {output_dir}")
    print(f"  Max pages   : {max_pages}")
    print(f"  Delay       : {delay}s")
    print("=" * 60)

    start_time = time.time()

    while queue and len(visited) < max_pages:
        url = queue.pop(0)
        norm = normalize_url(url)

        if norm in visited:
            continue
        if not url.startswith(base_prefix):
            continue

        page_num = len(visited) + 1
        remaining = len(queue)
        print(f"\n[{page_num:>3}/{page_num + remaining}] {url}")
        visited.add(norm)
        visited_original.append(url)

        success = False
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                req = urllib.request.Request(url, headers={
                    "User-Agent": "DocMaintainer-Crawler/1.0 (+https://github.com/user/DocMaintainer)",
                    "Accept": "text/html,application/xhtml+xml",
                })
                with urllib.request.urlopen(req, timeout=15) as resp:
                    ctype = resp.headers.get("Content-Type", "")
                    if "text/html" not in ctype:
                        print(f"       skip  non-HTML ({ctype})")
                        break
                    html = resp.read().decode("utf-8", errors="replace")

                parser = DocParser(url)
                parser.feed(html)

                # Save content
                fname = make_filename(url, base_path)
                fpath = os.path.join(output_dir, fname)
                with open(fpath, "w", encoding="utf-8") as fout:
                    fout.write(f"URL: {url}\n")
                    fout.write(f"Scraped: {datetime.now(timezone.utc).isoformat()}\n\n")
                    fout.write(parser.text)

                # Discover new links
                newly_added = []
                for link in parser.links:
                    link_norm = normalize_url(link)
                    if link_norm not in visited and link.startswith(base_prefix):
                        # Check queue as well
                        if not any(normalize_url(q) == link_norm for q in queue):
                            queue.append(link)
                            newly_added.append(link)

                print(f"       saved {fname}  (+{len(newly_added)} links)")
                success = True
                break  # exit retry loop

            except urllib.error.HTTPError as exc:
                errors.append({"url": url, "error": f"HTTP {exc.code}", "attempt": attempt})
                print(f"       error HTTP {exc.code}", end="")
                if exc.code in (429, 500, 502, 503, 504) and attempt < max_retries:
                    wait = delay * (2 ** attempt)
                    print(f"  → retry in {wait:.1f}s")
                    time.sleep(wait)
                else:
                    print()
                    break

            except (urllib.error.URLError, OSError) as exc:
                errors.append({"url": url, "error": str(exc), "attempt": attempt})
                print(f"       error {exc}")
                if attempt < max_retries:
                    time.sleep(delay * 2)
                else:
                    break

        time.sleep(delay)

    elapsed = time.time() - start_time

    # ---- Write outputs ----

    # 1. All discovered links
    links_path = os.path.join(output_dir, "_all_links.txt")
    with open(links_path, "w", encoding="utf-8") as fout:
        for u in sorted(visited_original):
            fout.write(f"{u}\n")

    # 2. Crawl metadata / summary
    summary = {
        "start_url": start_url,
        "base_path": base_path,
        "pages_crawled": len(visited),
        "errors": len(errors),
        "elapsed_seconds": float(f"{elapsed:.2f}"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "error_details": errors,
    }
    meta_path = os.path.join(output_dir, "_crawl_meta.json")
    with open(meta_path, "w", encoding="utf-8") as fout:
        json.dump(summary, fout, indent=2)

    # ---- Final report ----
    print("\n" + "=" * 60)
    print("  Crawl Summary")
    print("=" * 60)
    print(f"  Pages scraped : {len(visited)}")
    print(f"  Errors        : {len(errors)}")
    print(f"  Time elapsed  : {elapsed:.1f}s")
    print(f"  Links index   : {links_path}")
    print(f"  Metadata      : {meta_path}")
    print("=" * 60)

    return summary


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="DocMaintainer Web Crawler — scrape documentation sites into local text files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="See https://github.com/your-org/DocMaintainer for documentation.",
    )
    ap.add_argument("--start-url", required=True,
                     help="The URL to begin crawling from.")
    ap.add_argument("--base-path", required=True,
                     help="Only follow links whose path starts with this prefix (e.g. /docs/en/).")
    ap.add_argument("--output-repo", required=True,
                     help="Sub-directory under the project root to store scraped output (e.g. ClaudeCodeDocs).")
    ap.add_argument("--max-pages", type=int, default=100,
                     help="Maximum number of pages to crawl (default: 100).")
    ap.add_argument("--delay", type=float, default=0.5,
                     help="Seconds to wait between requests (default: 0.5).")

    args = ap.parse_args()
    summary = crawl_docs(
        args.start_url,
        args.base_path,
        args.output_repo,
        args.max_pages,
        args.delay,
    )
    sys.exit(0 if summary["errors"] == 0 else 1)


if __name__ == "__main__":
    main()
