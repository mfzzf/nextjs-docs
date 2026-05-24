#!/usr/bin/env python3
"""crawl.py — fetch Next.js docs into references/.

Strategy
--------
1. Fetch the upstream `llms.txt` index from `https://nextjs.org/docs/llms.txt`.
   Some entries point at *nested* indexes (e.g. `https://nextjs.org/docs/pages/llms.txt`);
   those are followed recursively so we capture both App Router and Pages Router.
2. Every `- [Title](URL)` link whose URL is on `nextjs.org` and *not* itself an
   `llms.txt` file is treated as a doc page.
3. For each doc URL, fetch `<url>.md` (nextjs.org serves raw markdown source
   when you append `.md`). The script handles a small thread pool of workers.
4. Write one file per page under `references/pages/<slug>.md` and a top-level
   `references/INDEX.md` with the source URL, sync timestamp, and a clickable list.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "references"
PAGES = REF / "pages"

INDEX_URL = "https://nextjs.org/docs/llms.txt"
DOMAIN = "nextjs.org"
USER_AGENT = "Mozilla/5.0 (compatible; ucloud-modelverse-skills/1.0; +https://github.com/mfzzf/SKILLS)"

LINK_RE = re.compile(r"^\s*-\s*\[([^\]]+)\]\((https?://[^)]+)\)\s*:?\s*(.*?)\s*$")
SECTION_RE = re.compile(r"^(##+)\s+(?:\[([^\]]+)\]\([^)]+\)|(.+?))\s*$")


def fetch(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def slugify(s: str, max_len: int = 100) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:max_len] or "untitled")


def parse_index(text: str) -> tuple[list[tuple[str, str, str, str]], list[str], str]:
    """Parse one llms.txt blob.

    Returns (items, sub_indexes, header_blob):
      - items: [(section, title, url, description)] for every regular doc link
      - sub_indexes: nested llms.txt URLs to crawl recursively
      - header_blob: top-level prose before the first `## ` heading
    """
    lines = text.splitlines()
    section = ""
    header_lines: list[str] = []
    items: list[tuple[str, str, str, str]] = []
    sub_indexes: list[str] = []
    in_header = True
    for line in lines:
        m_sec = SECTION_RE.match(line)
        if m_sec:
            in_header = False
            section = (m_sec.group(2) or m_sec.group(3) or "").strip()
            continue
        if in_header:
            header_lines.append(line)
            continue
        m_link = LINK_RE.match(line)
        if not m_link:
            continue
        title, url, desc = m_link.group(1).strip(), m_link.group(2).strip(), m_link.group(3).strip()
        if DOMAIN not in url:
            continue
        if url.endswith("/llms.txt") or url.endswith("llms.txt"):
            sub_indexes.append(url)
            continue
        items.append((section, title, url, desc))
    return items, sub_indexes, "\n".join(header_lines).strip()


def doc_md_url(url: str) -> str:
    """Translate a doc page URL into its raw-markdown sibling (`<url>.md`)."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.rstrip("/")
    if path.endswith((".json", ".md", ".mdx", ".txt")):
        return url
    return urllib.parse.urlunparse(parsed._replace(path=path + ".md"))


def url_to_slug(url: str) -> str:
    """nextjs.org/docs/app/api-reference/functions/cookies → app-api-reference-functions-cookies."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/")
    path = re.sub(r"^docs/?", "", path)
    if not path:
        path = "docs-index"
    return slugify(path.replace("/", "-"))


def fetch_one(url: str) -> tuple[str, bytes | None, str | None]:
    md_url = doc_md_url(url)
    try:
        body = fetch(md_url)
    except urllib.error.HTTPError as e:
        if md_url.endswith(".md"):
            try:
                body = fetch(md_url[:-3] + ".mdx")
                return md_url, body, None
            except Exception as e2:
                return md_url, None, f"{e} / {e2}"
        return md_url, None, str(e)
    except urllib.error.URLError as e:
        return md_url, None, f"network: {e.reason}"
    return md_url, body, None


def crawl_indexes(start_url: str) -> tuple[list[tuple[str, str, str, str]], str, list[str]]:
    """Walk the index graph, return (all_items, root_header_blob, visited_indexes)."""
    seen: set[str] = set()
    queue = [start_url]
    all_items: list[tuple[str, str, str, str]] = []
    root_header = ""
    visited: list[str] = []
    seen_urls: set[str] = set()
    while queue:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u)
        try:
            body = fetch(u).decode("utf-8")
        except Exception as e:
            print(f"  ✗ index fetch failed {u}: {e}", file=sys.stderr)
            continue
        visited.append(u)
        items, subs, header = parse_index(body)
        # Tag section with the source index path so App vs Pages routers don't collide.
        parsed = urllib.parse.urlparse(u)
        scope = parsed.path.strip("/").replace("/llms.txt", "").replace("docs", "App Router").strip("/") or "App Router"
        if scope == "App Router":
            tag = ""
        else:
            tag = scope.replace("-", " ").title() + " — "  # e.g. "Pages — "
        for section, title, url, desc in items:
            if url in seen_urls:
                continue
            seen_urls.add(url)
            all_items.append((tag + section if section else tag.rstrip(" —"), title, url, desc))
        if u == start_url:
            root_header = header
        queue.extend(subs)
    return all_items, root_header, visited


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index-url", default=INDEX_URL)
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    log = (lambda *_: None) if args.quiet else (lambda *a: print(*a, file=sys.stderr))

    log(f"→ fetching index {args.index_url}")
    items, header_blob, visited = crawl_indexes(args.index_url)
    log(f"  · {len(items)} doc links across {len(visited)} index file(s)")

    if PAGES.exists():
        for old in PAGES.glob("*"):
            if old.is_file():
                old.unlink()
    PAGES.mkdir(parents=True, exist_ok=True)

    # Save the root index verbatim (useful for diffs).
    try:
        (REF / "llms.txt").write_bytes(fetch(args.index_url))
    except Exception:
        pass
    if header_blob:
        (PAGES / "_overview.md").write_text(header_blob + "\n", encoding="utf-8")

    saved: list[tuple[str, str, str, str, str, int]] = []
    failed: list[tuple[str, str, str]] = []

    seen_slugs: dict[str, int] = {}
    def claim_slug(base: str) -> str:
        n = seen_slugs.get(base, 0)
        seen_slugs[base] = n + 1
        return base if n == 0 else f"{base}-{n+1}"

    with cf.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(fetch_one, url): (section, title, url, desc)
                   for section, title, url, desc in items}
        for fut in cf.as_completed(futures):
            section, title, url, desc = futures[fut]
            md_url, body, err = fut.result()
            if err or body is None:
                log(f"  ✗ {url}  → {err}")
                failed.append((url, md_url, err or "unknown"))
                continue
            slug = claim_slug(url_to_slug(url))
            target = PAGES / f"{slug}.md"
            text = body.decode("utf-8", errors="replace")
            header = (
                f"<!--\n"
                f"title: {title}\n"
                f"section: {section}\n"
                f"source: {url}\n"
                f"raw: {md_url}\n"
                f"description: {desc}\n"
                f"-->\n\n"
            )
            target.write_text(header + text, encoding="utf-8")
            saved.append((section, title, slug, url, md_url, len(body)))

    saved.sort(key=lambda r: (r[0], r[1].lower()))
    fetched_at = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")

    lines = [
        "# Next.js Docs — Reference Mirror",
        "",
        f"_Source index:_ <{args.index_url}>",
        "",
        f"_Indexes visited:_ {len(visited)}  ·  _pages:_ {len(saved)}  ·  _failed:_ {len(failed)}  ·  _last synced:_ {fetched_at}",
        "",
        "Pages are fetched as raw markdown from `<url>.md` and written under `pages/`.",
        "Each file has a tiny HTML comment header with `title`/`section`/`source`/`raw`/`description`.",
        "App Router and Pages Router are both crawled (the latter via the nested `pages/llms.txt`).",
        "",
    ]
    last_section = None
    for section, title, slug, url, md_url, n in saved:
        if section != last_section:
            lines.append("")
            lines.append(f"## {section or 'Other'}")
            lines.append("")
            last_section = section
        lines.append(
            f"- [`pages/{slug}.md`](./pages/{slug}.md) — {title}  ({n:,} B)  "
            f"([source]({url}))"
        )

    if failed:
        lines.append("")
        lines.append("## Failed")
        lines.append("")
        for url, md_url, err in failed:
            lines.append(f"- {url}  (tried `{md_url}`) — {err}")

    (REF / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    log(f"✓ wrote {len(saved)} pages under {PAGES} ({len(failed)} failed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
