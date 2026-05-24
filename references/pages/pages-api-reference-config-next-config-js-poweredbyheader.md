<!--
title: poweredByHeader
section: App Router/Pages — API Reference
source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader
raw: https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader.md
description: Next.js will add the `x-powered-by` header by default. Learn to opt-out of it here.
-->

---
title: poweredByHeader
description: "Next.js will add the `x-powered-by` header by default. Learn to opt-out of it here."
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "Configuration: /docs/pages/api-reference/config"
  - "next.config.js Options: /docs/pages/api-reference/config/next-config-js"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

```js filename="next.config.js"
module.exports = {
  poweredByHeader: false,
}
```
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)