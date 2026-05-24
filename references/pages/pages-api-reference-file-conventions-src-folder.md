<!--
title: src Directory
section: App Router/Pages — API Reference
source: https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder
raw: https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder.md
description: Save pages under the `src` folder as an alternative to the root `pages` directory.
-->

---
title: src Directory
description: "Save pages under the `src` folder as an alternative to the root `pages` directory."
url: "https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "API Reference: /docs/pages/api-reference"
  - "File-system conventions: /docs/pages/api-reference/file-conventions"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
As an alternative to having the special Next.js `app` or `pages` directories in the root of your project, Next.js also supports the common pattern of placing application code under the `src` folder.

This separates application code from project configuration files which mostly live in the root of a project, which is preferred by some individuals and teams.

To use the `src` folder, move the `app` Router folder or `pages` Router folder to `src/app` or `src/pages` respectively.

![An example folder structure with the src folder](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-src-directory.png)

> **Good to know**:
>
> * The `/public` directory should remain in the root of your project.
> * Config files like `package.json`, `next.config.js` and `tsconfig.json` should remain in the root of your project.
> * `.env.*` files should remain in the root of your project.
> * `src/app` or `src/pages` will be ignored if `app` or `pages` are present in the root directory.
> * If you're using `src`, you'll probably also move other application folders such as `/components` or `/lib`.
> * If you're using Proxy, ensure it is placed inside the `src` folder.
> * If you're using Tailwind CSS, you'll need to add the `/src` prefix to the `tailwind.config.js` file in the [content section](https://tailwindcss.com/docs/content-configuration).
> * If you are using TypeScript paths for imports such as `@/*`, you should update the `paths` object in `tsconfig.json` to include `src/`.
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)