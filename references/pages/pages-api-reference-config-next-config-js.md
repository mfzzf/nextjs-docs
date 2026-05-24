<!--
title: next.config.js Options
section: App Router/Pages — API Reference
source: https://nextjs.org/docs/pages/api-reference/config/next-config-js
raw: https://nextjs.org/docs/pages/api-reference/config/next-config-js.md
description: Learn about the options available in next.config.js for the Pages Router.
-->

---
title: next.config.js Options
description: Learn about the options available in next.config.js for the Pages Router.
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "API Reference: /docs/pages/api-reference"
  - "Configuration: /docs/pages/api-reference/config"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
Next.js can be configured through a `next.config.js` file in the root of your project directory (for example, by `package.json`) with a default export.

```js filename="next.config.js"
// @ts-check

/** @type {import('next').NextConfig} */
const nextConfig = {
  /* config options here */
}

module.exports = nextConfig
```

## ECMAScript Modules

`next.config.js` is a regular Node.js module, not a JSON file. It gets used by the Next.js server and build phases, and it's not included in the browser build.

If you need [ECMAScript modules](https://nodejs.org/api/esm.html), you can use `next.config.mjs`:

```js filename="next.config.mjs"
// @ts-check

/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  /* config options here */
}

export default nextConfig
```

> **Good to know**: `next.config` with the `.cjs` or `.cts` extensions are currently **not** supported.

## Configuration as a Function

You can also use a function:

```js filename="next.config.mjs"
// @ts-check

export default (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Async Configuration

Since Next.js 12.1.0, you can use an async function:

```js filename="next.config.js"
// @ts-check

module.exports = async (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Phase

`phase` is the current context in which the configuration is loaded. You can see the [available phases](https://github.com/vercel/next.js/blob/5e6b008b561caf2710ab7be63320a3d549474a5b/packages/next/shared/lib/constants.ts#L19-L23). Phases can be imported from `next/constants`:

```js filename="next.config.js"
// @ts-check

const { PHASE_DEVELOPMENT_SERVER } = require('next/constants')

module.exports = (phase, { defaultConfig }) => {
  if (phase === PHASE_DEVELOPMENT_SERVER) {
    return {
      /* development only config options here */
    }
  }

  return {
    /* config options for all phases except development here */
  }
}
```

## TypeScript

If you are using TypeScript in your project, you can use `next.config.ts` to use TypeScript in your configuration:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  /* config options here */
}

export default nextConfig
```

The commented lines are the place where you can put the configs allowed by `next.config.js`, which are [defined in this file](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/config-shared.ts).

However, none of the configs are required, and it's not necessary to understand what each config does. Instead, search for the features you need to enable or modify in this section and they will show you what to do.

> Avoid using new JavaScript features not available in your target Node.js version. `next.config.js` will not be parsed by Webpack or Babel.

This page documents all the available configuration options:

## Unit Testing (experimental)

Starting in Next.js 15.1, the `next/experimental/testing/server` package contains utilities to help unit test `next.config.js` files.

The `unstable_getResponseFromNextConfig` function runs the [`headers`](/docs/app/api-reference/config/next-config-js/headers), [`redirects`](/docs/app/api-reference/config/next-config-js/redirects), and [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites) functions from `next.config.js` with the provided request information and returns `NextResponse` with the results of the routing.

> The response from `unstable_getResponseFromNextConfig` only considers `next.config.js` fields and does not consider proxy or filesystem routes, so the result in production may be different than the unit test.

```js
import {
  getRedirectUrl,
  unstable_getResponseFromNextConfig,
} from 'next/experimental/testing/server'

const response = await unstable_getResponseFromNextConfig({
  url: 'https://nextjs.org/test',
  nextConfig: {
    async redirects() {
      return [{ source: '/test', destination: '/test2', permanent: false }]
    },
  },
})
expect(response.status).toEqual(307)
expect(getRedirectUrl(response)).toEqual('https://nextjs.org/test2')
```

- [adapterPath](/docs/pages/api-reference/config/next-config-js/adapterPath)
  - Configure a custom adapter for Next.js to hook into the build process.
- [allowedDevOrigins](/docs/pages/api-reference/config/next-config-js/allowedDevOrigins)
  - Use `allowedDevOrigins` to configure additional origins that can request the dev server.
- [assetPrefix](/docs/pages/api-reference/config/next-config-js/assetPrefix)
  - Learn how to use the assetPrefix config option to configure your CDN.
- [basePath](/docs/pages/api-reference/config/next-config-js/basePath)
  - Use `basePath` to deploy a Next.js application under a sub-path of a domain.
- [bundlePagesRouterDependencies](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)
  - Enable automatic dependency bundling for Pages Router
- [compress](/docs/pages/api-reference/config/next-config-js/compress)
  - Next.js provides gzip compression to compress rendered content and static files, it only works with the server target. Learn more about it here.
- [crossOrigin](/docs/pages/api-reference/config/next-config-js/crossOrigin)
  - Use the `crossOrigin` option to add a crossOrigin tag on the `script` tags generated by `next/script` and `next/head`.
- [deploymentId](/docs/pages/api-reference/config/next-config-js/deploymentId)
  - Configure a deployment identifier used for version skew protection and cache busting.
- [devIndicators](/docs/pages/api-reference/config/next-config-js/devIndicators)
  - Optimized pages include an indicator to let you know if it's being statically optimized. You can opt-out of it here.
- [distDir](/docs/pages/api-reference/config/next-config-js/distDir)
  - Set a custom build directory to use instead of the default .next directory.
- [env](/docs/pages/api-reference/config/next-config-js/env)
  - Learn to add and access environment variables in your Next.js application at build time.
- [exportPathMap](/docs/pages/api-reference/config/next-config-js/exportPathMap)
  - Customize the pages that will be exported as HTML files when using `next export`.
- [generateBuildId](/docs/pages/api-reference/config/next-config-js/generateBuildId)
  - Configure the build id, which is used to identify the current build in which your application is being served.
- [generateEtags](/docs/pages/api-reference/config/next-config-js/generateEtags)
  - Next.js will generate etags for every page by default. Learn more about how to disable etag generation here.
- [headers](/docs/pages/api-reference/config/next-config-js/headers)
  - Add custom HTTP headers to your Next.js app.
- [httpAgentOptions](/docs/pages/api-reference/config/next-config-js/httpAgentOptions)
  - Next.js will automatically use HTTP Keep-Alive by default. Learn more about how to disable HTTP Keep-Alive here.
- [images](/docs/pages/api-reference/config/next-config-js/images)
  - Custom configuration for the next/image loader
- [logging](/docs/pages/api-reference/config/next-config-js/logging)
  - Configure logging behavior in the terminal when running Next.js in development mode.
- [onDemandEntries](/docs/pages/api-reference/config/next-config-js/onDemandEntries)
  - Configure how Next.js will dispose and keep in memory pages created in development.
- [optimizePackageImports](/docs/pages/api-reference/config/next-config-js/optimizePackageImports)
  - API Reference for optimizePackageImports Next.js Config Option
- [output](/docs/pages/api-reference/config/next-config-js/output)
  - Next.js automatically traces which files are needed by each page to allow for easy deployment of your application. Learn how it works here.
- [pageExtensions](/docs/pages/api-reference/config/next-config-js/pageExtensions)
  - Extend the default page extensions used by Next.js when resolving pages in the Pages Router.
- [poweredByHeader](/docs/pages/api-reference/config/next-config-js/poweredByHeader)
  - Next.js will add the `x-powered-by` header by default. Learn to opt-out of it here.
- [productionBrowserSourceMaps](/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
  - Enables browser source map generation during the production build.
- [experimental.proxyClientMaxBodySize](/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize)
  - Configure the maximum request body size when using proxy.
- [reactStrictMode](/docs/pages/api-reference/config/next-config-js/reactStrictMode)
  - The complete Next.js runtime is now Strict Mode-compliant, learn how to opt-in
- [redirects](/docs/pages/api-reference/config/next-config-js/redirects)
  - Add redirects to your Next.js app.
- [rewrites](/docs/pages/api-reference/config/next-config-js/rewrites)
  - Add rewrites to your Next.js app.
- [serverExternalPackages](/docs/pages/api-reference/config/next-config-js/serverExternalPackages)
  - Opt-out specific dependencies from the dependency bundling enabled by `bundlePagesRouterDependencies`.
- [trailingSlash](/docs/pages/api-reference/config/next-config-js/trailingSlash)
  - Configure Next.js pages to resolve with or without a trailing slash.
- [transpilePackages](/docs/pages/api-reference/config/next-config-js/transpilePackages)
  - Automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`).
- [turbopack](/docs/pages/api-reference/config/next-config-js/turbopack)
  - Configure Next.js with Turbopack-specific options
- [typescript](/docs/pages/api-reference/config/next-config-js/typescript)
  - Next.js reports TypeScript errors by default. Learn to opt-out of this behavior here.
- [urlImports](/docs/pages/api-reference/config/next-config-js/urlImports)
  - Configure Next.js to allow importing modules from external URLs.
- [useLightningcss](/docs/pages/api-reference/config/next-config-js/useLightningcss)
  - Enable experimental support for Lightning CSS.
- [webpack](/docs/pages/api-reference/config/next-config-js/webpack)
  - Learn how to customize the webpack config used by Next.js
- [webVitalsAttribution](/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)
  - Learn how to use the webVitalsAttribution option to pinpoint the source of Web Vitals issues.

---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)