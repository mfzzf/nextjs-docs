<!--
title: cacheTag
section: API Reference
source: https://nextjs.org/docs/app/api-reference/functions/cacheTag
raw: https://nextjs.org/docs/app/api-reference/functions/cacheTag.md
description: Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.
-->

---
title: cacheTag
description: Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.
url: "https://nextjs.org/docs/app/api-reference/functions/cacheTag"
docs_index: /docs/llms.txt
version: 16.2.6
lastUpdated: 2026-05-19
prerequisites:
  - "API Reference: /docs/app/api-reference"
  - "Functions: /docs/app/api-reference/functions"
related:
  - app/api-reference/config/next-config-js/cacheComponents
  - app/api-reference/directives/use-cache
  - app/api-reference/functions/revalidateTag
  - app/api-reference/functions/updateTag
  - app/api-reference/functions/cacheLife
---


> For an index of all Next.js documentation, see [/docs/llms.txt](/docs/llms.txt).
The `cacheTag` function allows you to tag cached data for on-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidate specific cache entries without affecting other cached data.

## Usage

To use `cacheTag`, enable the [`cacheComponents` flag](/docs/app/api-reference/config/next-config-js/cacheComponents) in your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

```js filename="next.config.js" switcher
const nextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

The `cacheTag` function takes one or more string values.

```tsx filename="app/data.ts" switcher
import { cacheTag } from 'next/cache'

export async function getData() {
  'use cache'
  cacheTag('my-data')
  const data = await fetch('/api/data')
  return data
}
```

```jsx filename="app/data.js" switcher
import { cacheTag } from 'next/cache'

export async function getData() {
  'use cache'
  cacheTag('my-data')
  const data = await fetch('/api/data')
  return data
}
```

You can then purge the cache on-demand from a [Server Function](/docs/app/getting-started/mutating-data) or [Route Handler](/docs/app/api-reference/file-conventions/route):

* Use [`updateTag`](/docs/app/api-reference/functions/updateTag) inside a Server Function for read-your-own-writes scenarios, where a user makes a change and the next read should fetch fresh data immediately.
* Use [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag) when it is acceptable to serve stale data while revalidation happens in the background, or when revalidating from a route handler.

The example below uses `revalidateTag`:

```tsx filename="app/action.ts" switcher
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('my-data')
}
```

```jsx filename="app/action.js" switcher
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('my-data')
}
```

## Good to know

* **Idempotent Tags**: Applying the same tag multiple times has no additional effect.
* **Multiple Tags**: You can assign multiple tags to a single cache entry by passing multiple string values to `cacheTag`.

```tsx
cacheTag('tag-one', 'tag-two')
```

* **Limits**: A single `cacheTag()` call accepts up to 128 tags, each with a maximum length of 256 characters. Tags longer than 256 characters are skipped, and any tags past the 128th in one call are dropped. Both cases log a console warning.

## Examples

### Tagging components or functions

Tag your cached data by calling `cacheTag` within a cached function or component:

```tsx filename="app/components/bookings.tsx" switcher
import { cacheTag } from 'next/cache'

interface BookingsProps {
  type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
  'use cache'
  cacheTag('bookings-data')

  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }

  return //...
}
```

```jsx filename="app/components/bookings.js" switcher
import { cacheTag } from 'next/cache'

export async function Bookings({ type = 'haircut' }) {
  'use cache'
  cacheTag('bookings-data')

  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }

  return //...
}
```

### Creating tags from external data

You can use the data returned from an async function to tag the cache entry.

```tsx filename="app/components/bookings.tsx" switcher
import { cacheTag } from 'next/cache'

interface BookingsProps {
  type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
  async function getBookingsData() {
    'use cache'
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    cacheTag('bookings-data', data.id)
    return data
  }
  return //...
}
```

```jsx filename="app/components/bookings.js" switcher
import { cacheTag } from 'next/cache'

export async function Bookings({ type = 'haircut' }) {
  async function getBookingsData() {
    'use cache'
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    cacheTag('bookings-data', data.id)
    return data
  }
  return //...
}
```

### Invalidating tagged cache

Using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag), you can invalidate the cache for a specific tag when needed:

```tsx filename="app/actions.ts" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function updateBookings() {
  await updateBookingData()
  revalidateTag('bookings-data')
}
```

```jsx filename="app/actions.js" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function updateBookings() {
  await updateBookingData()
  revalidateTag('bookings-data')
}
```
## Related

View related API references.

- [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents)
  - Learn how to enable the cacheComponents flag in Next.js.
- [use cache](/docs/app/api-reference/directives/use-cache)
  - Learn how to use the "use cache" directive to cache data in your Next.js application.
- [revalidateTag](/docs/app/api-reference/functions/revalidateTag)
  - API Reference for the revalidateTag function.
- [updateTag](/docs/app/api-reference/functions/updateTag)
  - API Reference for the updateTag function.
- [cacheLife](/docs/app/api-reference/functions/cacheLife)
  - Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.

---

For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)

For an index of all available documentation, see [/docs/llms.txt](/docs/llms.txt)