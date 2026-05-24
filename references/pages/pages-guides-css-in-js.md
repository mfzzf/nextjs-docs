<!--
title: CSS-in-JS
section: App Router/Pages — Guides
source: https://nextjs.org/docs/pages/guides/css-in-js
raw: https://nextjs.org/docs/pages/guides/css-in-js.md
description: Use CSS-in-JS libraries with Next.js
-->

---
title: How to use CSS-in-JS libraries
description: Use CSS-in-JS libraries with Next.js
url: "https://nextjs.org/docs/pages/guides/css-in-js"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "Guides: /docs/pages/guides"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
<details>
<summary>Examples</summary>

* [Styled JSX](https://github.com/vercel/next.js/tree/canary/examples/with-styled-jsx)
* [Styled Components](https://github.com/vercel/next.js/tree/canary/examples/with-styled-components)
* [Emotion](https://github.com/vercel/next.js/tree/canary/examples/with-emotion)
* [Linaria](https://github.com/vercel/next.js/tree/canary/examples/with-linaria)
* [Styletron](https://github.com/vercel/next.js/tree/canary/examples/with-styletron)
* [Cxs](https://github.com/vercel/next.js/tree/canary/examples/with-cxs)
* [Fela](https://github.com/vercel/next.js/tree/canary/examples/with-fela)
* [Stitches](https://github.com/vercel/next.js/tree/canary/examples/with-stitches)

</details>

It's possible to use any existing CSS-in-JS solution. The simplest one is inline styles:

```jsx
function HiThere() {
  return <p style={{ color: 'red' }}>hi there</p>
}

export default HiThere
```

We bundle [styled-jsx](https://github.com/vercel/styled-jsx) to provide support for isolated scoped CSS.
The aim is to support "shadow CSS" similar to Web Components, which unfortunately [do not support server-rendering and are JS-only](https://github.com/w3c/webcomponents/issues/71).

See the above examples for other popular CSS-in-JS solutions (like Styled Components).

A component using `styled-jsx` looks like this:

```jsx
function HelloWorld() {
  return (
    <div>
      Hello world
      <p>scoped!</p>
      <style jsx>{`
        p {
          color: blue;
        }
        div {
          background: red;
        }
        @media (max-width: 600px) {
          div {
            background: blue;
          }
        }
      `}</style>
      <style global jsx>{`
        body {
          background: black;
        }
      `}</style>
    </div>
  )
}

export default HelloWorld
```

Please see the [styled-jsx documentation](https://github.com/vercel/styled-jsx) for more examples.

### Disabling JavaScript

Yes, if you disable JavaScript the CSS will still be loaded in the production build (`next start`). During development, we require JavaScript to be enabled to provide the best developer experience with [Fast Refresh](https://nextjs.org/blog/next-9-4#fast-refresh).
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)