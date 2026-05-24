<!--
title: Rendering
section: App Router/Pages — Building Your Application
source: https://nextjs.org/docs/pages/building-your-application/rendering
raw: https://nextjs.org/docs/pages/building-your-application/rendering.md
description: Learn the fundamentals of rendering in React and Next.js.
-->

---
title: Rendering
description: Learn the fundamentals of rendering in React and Next.js.
url: "https://nextjs.org/docs/pages/building-your-application/rendering"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "Building Your Application: /docs/pages/building-your-application"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
By default, Next.js **prerenders** every page. This means that Next.js generates HTML for each page in advance, instead of having it all done by client-side JavaScript. Prerendering can result in better performance and SEO.

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive (this process is called [hydration](https://react.dev/reference/react-dom/client/hydrateRoot) in React).

### Prerendering

Next.js has two forms of prerendering: **Static Generation** and **Server-side Rendering**. The difference is in **when** it generates the HTML for a page.

* Static Generation: The HTML is generated at **build time** and will be reused on each request.
* Server-side Rendering: The HTML is generated on **each request**.

Importantly, Next.js lets you choose which prerendering form you'd like to use for each page. You can create a "hybrid" Next.js app by using Static Generation for most pages and using Server-side Rendering for others.

We recommend using Static Generation over Server-side Rendering for performance reasons. Statically generated pages can be cached by CDN with no extra configuration to boost performance. However, in some cases, Server-side Rendering might be the only option.

You can also use client-side data fetching along with Static Generation or Server-side Rendering. That means some parts of a page can be rendered entirely by clientside JavaScript. To learn more, take a look at the [Data Fetching](/docs/pages/building-your-application/data-fetching/client-side) documentation.

- [Server-side Rendering (SSR)](/docs/pages/building-your-application/rendering/server-side-rendering)
  - Use Server-side Rendering to render pages on each request.
- [Static Site Generation (SSG)](/docs/pages/building-your-application/rendering/static-site-generation)
  - Use Static Site Generation (SSG) to prerender pages at build time.
- [Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization)
  - Next.js automatically optimizes your app to be static HTML whenever possible. Learn how it works here.
- [Client-side Rendering (CSR)](/docs/pages/building-your-application/rendering/client-side-rendering)
  - Learn how to implement client-side rendering in the Pages Router.

---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)