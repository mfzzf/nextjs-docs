---
name: nextjs-docs
description: 'Bundled offline mirror of the **Next.js 16.2.6 documentation** (`nextjs.org/docs/llms.txt` index + nested `pages/llms.txt` → 406 raw markdown pages, ~4.4 MB). Covers App Router *and* Pages Router — Getting Started (installation, project structure, layouts, RSC, fetching, mutating, caching, revalidating, ISR), every Guide (auth, forms, MDX, testing with Cypress/Playwright/Vitest/Jest, OpenTelemetry, PWA, migrations, multi-zone, view transitions), full API Reference (directives `use cache` / `use cache: private` / `use cache: remote` / `use client` / `use server`, components Font/Form/Image/Link/Script, every file convention layout.js/page.js/route.js/error.js/loading.js/template.js/proxy.js/middleware/metadata, every function cookies/headers/redirect/revalidatePath/revalidateTag/updateTag/cacheLife/cacheTag/after/connection/draftMode/forbidden/notFound/generateMetadata/…, every `next.config.js` option, CLI `create-next-app`/`next`, Adapters API, Edge Runtime, Turbopack), Architecture (Compiler, Fast Refresh, accessibility, browsers), Community. Use whenever you need an authoritative Next.js detail — config option, hook, file convention, App↔Pages migration, RSC/Server Action semantics, caching/revalidation model, Turbopack flag, route segment config. Trigger on `next.config.js`, `app/`, `pages/`, `use server`, `use client`, `use cache`, `revalidateTag`, `generateMetadata`, `next/image`, `next/link`, `next/font`, `create-next-app`, Server Actions, RSC, ISR, PPR, Turbopack, Edge Runtime, `proxy.js`, `instrumentation.js`, "Next.js 16", "App Router", "Pages Router", "according to Next.js docs". Also Chinese — "Next.js 文档", "Next.js 配置", "App Router 文档", "查一下 Next.js".'
---

# nextjs-docs

Offline mirror of [nextjs.org/docs](https://nextjs.org/docs) (Next.js 16.2.6). Whenever a question hinges on Next.js behavior — a config option, a file convention, a hook, the caching/revalidation model, an App↔Pages difference, `next.config.js` shape, Server Action wire-up, Turbopack flag — **read `references/INDEX.md` first** and then the relevant `references/pages/<slug>.md` rather than guessing or web-searching. Stays in sync via `scripts/crawl.py`.

## Layout

```
nextjs-docs/
├── SKILL.md                  # this file
├── scripts/
│   ├── crawl.py              # recursive llms.txt walker + per-page .md fetch
│   └── update-docs.sh        # crawl + commit + push (one-shot updater)
└── references/
    ├── INDEX.md              # grouped, clickable table of contents
    ├── llms.txt              # verbatim upstream root index
    └── pages/
        ├── _overview.md      # the leading Next.js blurb
        ├── app-getting-started-installation.md
        ├── app-getting-started-server-and-client-components.md
        ├── app-getting-started-caching.md
        ├── app-api-reference-functions-cookies.md
        ├── app-api-reference-config-next-config-js-images.md
        ├── app-api-reference-file-conventions-route.md
        ├── app-api-reference-directives-use-cache.md
        ├── app-guides-self-hosting.md
        ├── architecture-nextjs-compiler.md
        ├── …                  # 406 pages total
        └── pages-api-reference-…   # Pages Router pages live here too
```

## How to consume

1. Always start with `references/INDEX.md` — it groups every page by section
   (Getting Started / Guides / API Reference / Architecture / Community / Pages Router).
   App Router pages have section names like `Getting Started`, `Guides`, `API Reference`.
   Pages Router pages are tagged with a `Pages — ` prefix in the same INDEX
   so you can tell which router a section refers to.
2. Then open the matching `pages/<slug>.md`. Slugs are the URL path with the
   leading `docs/` stripped and `/` replaced by `-`, e.g.
   - `docs/app/api-reference/functions/cookies` → `app-api-reference-functions-cookies.md`
   - `docs/app/api-reference/config/next-config-js/cacheLife` → `app-api-reference-config-next-config-js-cachelife.md`
   - `docs/app/getting-started/server-and-client-components` → `app-getting-started-server-and-client-components.md`
3. Each page file begins with an HTML comment block carrying `title`, `section`,
   `source`, `raw` and `description` — useful when grepping.

Useful grep recipes:

```bash
# every page that talks about a topic
grep -lin "Server Action" references/pages/*.md
grep -lin "cacheTag" references/pages/*.md

# outline (title + section) of every page
for f in references/pages/*.md; do
  awk 'NR<=6 && /title:|section:/ {print FILENAME":"$0}' "$f"
done | head -40

# list every next.config.js option page
ls references/pages/app-api-reference-config-next-config-js-*.md

# read just the “When to use” / “Examples” of a function
sed -n '/^## /,/^## /p' references/pages/app-api-reference-functions-revalidatetag.md
```

## Refreshing the mirror

```bash
scripts/update-docs.sh                  # crawl + show diff (no commit)
scripts/update-docs.sh --commit         # crawl + commit if anything changed
scripts/update-docs.sh --commit --push  # also push origin/main
```

Override the index URL with `INDEX_URL=...`; default is `https://nextjs.org/docs/llms.txt`. Run when Next.js ships a new minor (the `@doc-version` line in the upstream index ticks), a new file convention, or you see a stale answer (the `_last synced:_` line in `INDEX.md` tells you how old it is).

Implementation notes for the crawler:

- The root index advertises a nested `https://nextjs.org/docs/pages/llms.txt` under its **Optional** section. The crawler follows it (and any other `*llms.txt` it discovers) so both routers are captured in one pass.
- Each `- [Title](URL)` link whose URL is on `nextjs.org` and is *not* an llms.txt
  is fetched as `<url>.md`. nextjs.org serves the original markdown source
  (frontmatter + MDX components) when you append `.md`; `.mdx` is a fallback.
- Pages discovered through the nested Pages Router index get their section
  prefixed with `Pages — ` so App vs Pages don't collide in INDEX.md.
- Duplicate URLs across indexes are de-duplicated by URL.
- Fetches run in a small thread pool (default 12 workers). 404s are listed in
  `INDEX.md` under a `## Failed` section instead of failing the run.

## Companion skills

- For **building a Next.js app end-to-end with the full 2026 stack** (Tailwind v4,
  shadcn/ui, AI Elements, Vercel AI SDK 5, testing) → **`frontend-build-2026`**.
- For **shadcn/ui component anatomy & install commands** → **`shadcn-ui-docs`**.
- For high-design **frontend visuals & layouts** that sit on top of Next.js →
  **`frontend-design`**.
- For **OpenAI / Anthropic / Gemini API** specifics referenced from AI examples
  → **`openai-docs`**, **`anthropic-docs`**, **`gemini-docs`**.

## Licensing / attribution

Content under `references/` is © Vercel and the Next.js contributors, fetched from the public `nextjs.org` docs site and redistributed for offline LLM-context use. Treat it as a cache, not original work. If the URL moves or terms change, update `crawl.py` and re-fetch.
