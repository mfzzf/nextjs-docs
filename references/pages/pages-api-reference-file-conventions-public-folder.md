<!--
title: public
section: App Router/Pages — API Reference
source: https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder
raw: https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder.md
description: Next.js allows you to serve static files, like images, in the public directory. You can learn how it works here.
-->

---
title: public Folder
description: Next.js allows you to serve static files, like images, in the public directory. You can learn how it works here.
url: "https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "API Reference: /docs/pages/api-reference"
  - "File-system conventions: /docs/pages/api-reference/file-conventions"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
Next.js can serve static files, like images, under a folder called `public` in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

For example, the file `public/avatars/me.png` can be viewed by visiting the `/avatars/me.png` path. The code to display that image might look like:

```jsx filename="avatar.js"
import Image from 'next/image'

export function Avatar({ id, alt }) {
  return <Image src={`/avatars/${id}.png`} alt={alt} width="64" height="64" />
}

export function AvatarOfMe() {
  return <Avatar id="me" alt="A portrait of me" />
}
```

## Caching

Next.js cannot safely cache assets in the `public` folder because they may change. The default caching headers applied are:

```jsx
Cache-Control: public, max-age=0
```

## Robots, Favicons, and others

The folder is also useful for `robots.txt`, `favicon.ico`, Google Site Verification, and any other static files (including `.html`). But make sure to not have a static file with the same name as a file in the `pages/` directory, as this will result in an error. [Read more](/docs/messages/conflicting-public-file-page).
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)