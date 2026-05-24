<!--
title: distDir
section: App Router/Pages — API Reference
source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir
raw: https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir.md
description: Set a custom build directory to use instead of the default .next directory.
-->

---
title: distDir
description: Set a custom build directory to use instead of the default .next directory.
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "Configuration: /docs/pages/api-reference/config"
  - "next.config.js Options: /docs/pages/api-reference/config/next-config-js"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
You can specify a name to use for a custom build directory to use instead of `.next`.

Open `next.config.js` and add the `distDir` config:

```js filename="next.config.js"
module.exports = {
  distDir: 'build',
}
```

Now if you run `next build` Next.js will use `build` instead of the default `.next` folder.

> `distDir` **should not** leave your project directory. For example, `../build` is an **invalid** directory.
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)