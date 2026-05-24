<!--
title: Server-side Rendering (SSR)
section: App Router/Pages — Building Your Application
source: https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering
raw: https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering.md
description: Use Server-side Rendering to render pages on each request.
-->

---
title: Server-side Rendering (SSR)
description: Use Server-side Rendering to render pages on each request.
url: "https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "Building Your Application: /docs/pages/building-your-application"
  - "Rendering: /docs/pages/building-your-application/rendering"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
> Also referred to as "SSR" or "Dynamic Rendering".

If a page uses **Server-side Rendering**, the page HTML is generated on **each request**.

To use Server-side Rendering for a page, you need to `export` an `async` function called `getServerSideProps`. This function will be called by the server on every request.

For example, suppose that your page needs to prerender frequently updated data (fetched from an external API). You can write `getServerSideProps` which fetches this data and passes it to `Page` like below:

```jsx
export default function Page({ data }) {
  // Render data...
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}
```

As you can see, `getServerSideProps` is similar to `getStaticProps`, but the difference is that `getServerSideProps` is run on every request instead of on build time.

To learn more about how `getServerSideProps` works, check out our [Data Fetching documentation](/docs/pages/building-your-application/data-fetching/get-server-side-props).
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)