<!--
title: serverExternalPackages
section: App Router/Pages — API Reference
source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages
raw: https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages.md
description: Opt-out specific dependencies from the dependency bundling enabled by `bundlePagesRouterDependencies`.
-->

---
title: serverExternalPackages
description: "Opt-out specific dependencies from the dependency bundling enabled by `bundlePagesRouterDependencies`."
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "Configuration: /docs/pages/api-reference/config"
  - "next.config.js Options: /docs/pages/api-reference/config/next-config-js"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
Opt-out specific dependencies from being included in the automatic bundling of the [`bundlePagesRouterDependencies`](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies) option.

These pages will then use native Node.js `require` to resolve the dependency.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['@acme/ui'],
}

module.exports = nextConfig
```

Next.js includes a [short list of popular packages](https://github.com/vercel/next.js/blob/canary/packages/next/src/lib/server-external-packages.jsonc) that currently are working on compatibility and automatically opt-ed out:

* `@alinea/generated`
* `@appsignal/nodejs`
* `@aws-sdk/client-s3`
* `@aws-sdk/s3-presigned-post`
* `@blockfrost/blockfrost-js`
* `@highlight-run/node`
* `@huggingface/transformers`
* `@jpg-store/lucid-cardano`
* `@libsql/client`
* `@mikro-orm/core`
* `@mikro-orm/knex`
* `@node-rs/argon2`
* `@node-rs/bcrypt`
* `@prisma/client`
* `@react-pdf/renderer`
* `@sentry/profiling-node`
* `@sparticuz/chromium`
* `@sparticuz/chromium-min`
* `@statsig/statsig-node-core`
* `@swc/core`
* `@xenova/transformers`
* `@zenstackhq/runtime`
* `argon2`
* `autoprefixer`
* `aws-crt`
* `bcrypt`
* `better-sqlite3`
* `canvas`
* `chromadb-default-embed`
* `config`
* `cpu-features`
* `cypress`
* `dd-trace`
* `eslint`
* `express`
* `firebase-admin`
* `htmlrewriter`
* `import-in-the-middle`
* `isolated-vm`
* `jest`
* `jsdom`
* `keyv`
* `libsql`
* `mdx-bundler`
* `mongodb`
* `mongoose`
* `newrelic`
* `next-mdx-remote`
* `next-seo`
* `node-cron`
* `node-pty`
* `node-web-audio-api`
* `onnxruntime-node`
* `oslo`
* `pg`
* `pino`
* `pino-pretty`
* `pino-roll`
* `playwright`
* `playwright-core`
* `postcss`
* `prettier`
* `prisma`
* `puppeteer-core`
* `puppeteer`
* `ravendb`
* `require-in-the-middle`
* `rimraf`
* `sharp`
* `shiki`
* `sqlite3`
* `thread-stream`
* `ts-morph`
* `ts-node`
* `typescript`
* `vscode-oniguruma`
* `webpack`
* `websocket`
* `zeromq`
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)