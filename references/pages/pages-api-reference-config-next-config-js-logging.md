<!--
title: logging
section: App Router/Pages — API Reference
source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/logging
raw: https://nextjs.org/docs/pages/api-reference/config/next-config-js/logging.md
description: Configure logging behavior in the terminal when running Next.js in development mode.
-->

---
title: logging
description: Configure logging behavior in the terminal when running Next.js in development mode.
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/logging"
docs_index: /docs/pages/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
router: Pages Router
prerequisites:
  - "Configuration: /docs/pages/api-reference/config"
  - "next.config.js Options: /docs/pages/api-reference/config/next-config-js"
---


> For an index of all Next.js documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt).
## Options

### Incoming Requests

By default all the incoming requests will be logged in the console during development. You can use the `incomingRequests` option to decide which requests to ignore.
Since this is only logged in development, this option doesn't affect production builds.

```js filename="next.config.js"
module.exports = {
  logging: {
    incomingRequests: {
      ignore: [/\api\/v1\/health/],
    },
  },
}
```

Or you can disable incoming request logging by setting `incomingRequests` to `false`.

```js filename="next.config.js"
module.exports = {
  logging: {
    incomingRequests: false,
  },
}
```

### Browser Console Logs

You can forward browser console logs (such as `console.log`, `console.warn`, `console.error`) to the terminal during development. This is useful for debugging client-side code without needing to check the browser's developer tools.

```js filename="next.config.js"
module.exports = {
  logging: {
    browserToTerminal: true,
  },
}
```

#### Options

The `browserToTerminal` option accepts the following values:

| Value     | Description                                         |
| --------- | --------------------------------------------------- |
| `'warn'`  | Forward only warnings and errors, by default        |
| `'error'` | Forward only errors                                 |
| `true`    | Forward all console output (log, info, warn, error) |
| `false`   | Disable browser log forwarding                      |

```js filename="next.config.js"
module.exports = {
  logging: {
    browserToTerminal: 'warn',
  },
}
```

#### Source Location

When enabled, browser logs include source location information (file path and line number) by default. For example:

```tsx filename="pages/index.tsx" highlight={6}
export default function Home() {
  return (
    <button
      type="button"
      onClick={() => {
        console.log('Hello World')
      }}
    >
      Click me
    </button>
  )
}
```

Clicking the button prints this message to the terminal:

```bash filename="Terminal"
[browser] Hello World (pages/index.tsx:6:17)
```

### Disabling Logging

In addition, you can disable the development logging by setting `logging` to `false`.

```js filename="next.config.js"
module.exports = {
  logging: false,
}
```

## Version History

| Version   | Changes                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| `v16.2.0` | `browserToTerminal` added (moved from `experimental.browserDebugInfoInTerminal`) |
| `v15.4.0` | `experimental.browserDebugInfoInTerminal` introduced                             |
| `v15.2.0` | `incomingRequests` added                                                         |
| `v15.0.0` | `logging: false` option added, `fetches.hmrRefreshes` added for App Router       |
| `v14.0.0` | `logging.fetches` moved to stable for App Router                                 |
---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/pages/llms.txt](/docs/pages/llms.txt)