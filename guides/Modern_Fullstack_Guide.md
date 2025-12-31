# Modern Fullstack Development: Complete Guide (Next.js 16)

A comprehensive guide to building production-ready fullstack applications using **Next.js 16**, TypeScript, Firebase/Supabase, Prisma ORM, and modern deployment strategies. This guide covers the latest App Router patterns, Cache Components, and React 19 integration.

## Table of Contents

1. [Modern Fullstack Architecture](#modern-fullstack-architecture)
2. [Tech Stack Overview](#tech-stack-overview)
3. [What's New in Next.js 16](#whats-new-in-nextjs-16)
4. [Project Setup](#project-setup)
5. [Next.js 16 App Router](#nextjs-16-app-router)
6. [Cache Components & New Caching Model](#cache-components--new-caching-model)
7. [Authentication Systems](#authentication-systems)
8. [Database & ORM (Prisma)](#database--orm-prisma)
9. [API Routes & Server Actions](#api-routes--server-actions)
10. [Proxy System (Replaces Middleware)](#proxy-system-replaces-middleware)
11. [File Upload & Storage](#file-upload--storage)
12. [State Management](#state-management)
13. [Real-time Features](#real-time-features)
14. [SEO & Metadata](#seo--metadata)
15. [Performance Optimization](#performance-optimization)
16. [Testing Strategy](#testing-strategy)
17. [Deployment](#deployment)
18. [Best Practices for Next.js 16](#best-practices-for-nextjs-16)

---

## Modern Fullstack Architecture

### Application Layers

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (Next.js 16)                  │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────────┐ │
│  │   Pages    │  │ Components │  │  Server Components     │ │
│  │  (Client)  │  │   (RSC)    │  │   (App Router)         │ │
│  │            │  │            │  │   + Cache Components   │ │
│  └────────────┘  └────────────┘  └────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                    API Layer (Next.js 16)                   │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────────┐ │
│  │ API Routes │  │   Server   │  │   Proxy System         │ │
│  │            │  │  Actions   │  │   (proxy.ts)           │ │
│  └────────────┘  └────────────┘  └────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                    Business Logic Layer                     │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────────┐ │
│  │  Services  │  │   Cache    │  │    Validation          │ │
│  │            │  │   Control  │  │    (Zod)               │ │
│  └────────────┘  └────────────┘  └────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Data Layer                             │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────────┐ │
│  │   Prisma   │  │  Firebase  │  │    External APIs       │ │
│  │   (ORM)    │  │ Firestore  │  │                        │ │
│  └────────────┘  └────────────┘  └────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Why Layers Matter

A layered architecture helps you separate responsibilities so changes stay local. UI changes should not require touching database logic, and data schema changes should not force a UI rewrite. It also improves testing: services and data access can be unit-tested, while routes and pages are tested at integration or E2E levels.

### Typical Request Flow (High Level)

1. The browser requests a route; `proxy.ts` handles early routing, redirects, and access gates.
2. The App Router resolves the route and renders Server Components.
3. Server Components call services, which call the data layer (Prisma, Firebase, external APIs).
4. The response streams HTML/flight data; Client Components hydrate to handle interactivity.

### Use Cases Mapped to Layers

- Marketing pages: mostly Server Components with caching, minimal client JavaScript.
- Authenticated dashboards: Server Components for data + Client Components for filters, forms, and charts.
- Webhooks: API routes receive events, services validate and process, data layer writes.

---

## Tech Stack Overview

### Frontend Stack

| Technology | Purpose | Version | Why? |
| --- | --- | --- | --- |
| **Next.js 16** | React framework | 16.1+ | Turbopack (stable), Cache Components, React 19 |
| **React 19.2** | UI library | 19.2+ | React Compiler, improved Server Components |
| **TypeScript** | Type safety | 5.0+ | Catch errors early, better DX |
| **Tailwind CSS** | Styling | 3.4+ | Utility-first, consistent design |
| **shadcn/ui** | Component library | Latest | Beautiful, accessible, customizable |

### Backend Stack

| Technology | Purpose | Version | Why? |
| --- | --- | --- | --- |
| **Prisma** | ORM | 6.0+ | Type-safe database access, migrations |
| **PostgreSQL** | Database | 14+ | Relational, ACID compliant, scalable |
| **Supabase/Firebase** | BaaS | Latest | Auth, real-time, storage |
| **NextAuth.js** | Authentication | 5.0+ | Multiple providers, secure |
| **Zod** | Validation | 3.0+ | Type-safe schema validation |

### Development Tools

| Tool | Purpose | Key Feature |
| --- | --- | --- |
| **Turbopack** | Bundler | 2-5x faster builds (stable in 16) |
| **Vercel** | Deployment | Zero-config deployments |
| **GitHub Actions** | CI/CD | Automated testing & deployment |
| **Playwright** | E2E testing | Modern testing framework |
| **Vitest** | Unit testing | Fast, Vite-powered |

### Picking Supabase vs Firebase (Quick Guide)

- Supabase: SQL/Postgres, strong relational queries, and row-level security on the server.
- Firebase: document model, great mobile SDKs, and offline-first workflows.
- Hybrid: use Supabase for core relational data and Firebase for real-time, user-facing features.

### When to Add Specialized Services

- Search: add a dedicated search service when you need fast, fuzzy text search.
- Background jobs: queue long-running tasks (emails, reports, media processing).
- Analytics: separate event tracking to keep the app database focused on product data.

---

## What's New in Next.js 16

### Major Features

#### 1. **Cache Components with `use cache`**
Explicit control over caching with the new `use cache` directive:

```typescript
'use cache';

export default async function ProductList() {
  const products = await fetchProducts();
  return <div>{/* ... */}</div>;
}
```

#### 2. **Turbopack (Stable)**
Default bundler with 2-5x faster builds and up to 10x faster Fast Refresh:

```bash
# Now default - no configuration needed
npm run dev  # Uses Turbopack automatically
```

#### 3. **Proxy System (`proxy.ts`)**
Replaces `middleware.ts` for clearer network boundaries:

```typescript
// proxy.ts
export default async function proxy(request: Request) {
  // Handle routing, rewrites, redirects
  return NextResponse.next();
}
```

#### 4. **Enhanced Caching APIs**
New methods for precise cache control:

```typescript
import { updateTag, revalidateTag, refresh } from 'next/cache';

// Update cache tags
updateTag('products');

// Revalidate specific tags
revalidateTag('user-profile');

// Force refresh
refresh();
```

#### 5. **React Compiler (Stable)**
Automatic memoization without manual `useMemo` or `useCallback`:

```typescript
// No need for useMemo anymore!
function ProductCard({ product }) {
  // Automatically optimized by React Compiler
  const price = calculatePrice(product);
  return <div>{price}</div>;
}
```

#### 6. **DevTools MCP Integration**
Model Context Protocol for AI-powered debugging:

```bash
# Enhanced debugging with AI assistance
npm run dev
```

#### 7. **File System Caching (Stable in 16.1)**
Faster startup times for large applications:

```bash
# Automatically enabled in 16.1
next dev  # Faster startup with FS caching
```

### Breaking Changes

| Change | Impact | Migration |
| --- | --- | --- |
| **Caching now opt-in** | All content dynamic by default | Add `'use cache'` where needed |
| **Middleware -> Proxy** | `middleware.ts` deprecated | Rename to `proxy.ts` |
| **Parallel routes** | Require explicit `default.js` | Add `default.js` files |
| **Modern Sass API** | sass-loader v16 | Update Sass syntax if needed |

### Why These Changes Matter

- Opt-in caching reduces stale data bugs; you choose what is safe to cache.
- The proxy system clarifies edge boundaries and makes routing behavior explicit.
- React Compiler removes a lot of manual performance tuning boilerplate.

### Migration Checklist

- Replace `middleware.ts` with `proxy.ts` and verify your matchers.
- Add `'use cache'` to routes that should be static or shared across users.
- Add `default.js` in parallel routes to avoid runtime errors.
- Audit Sass usage if you have legacy `@import` syntax.

---

## Project Setup

### Initialize Next.js 16 Project

```bash
# Create Next.js 16 app with TypeScript
npx create-next-app@latest my-fullstack-app --typescript --tailwind --app --turbopack

cd my-fullstack-app
```

### Install Core Dependencies

```bash
# Database & ORM
npm install @prisma/client
npm install -D prisma

# Authentication
npm install next-auth@beta @auth/prisma-adapter
npm install bcryptjs
npm install -D @types/bcryptjs

# Validation
npm install zod

# State Management
npm install zustand

# Forms
npm install react-hook-form @hookform/resolvers

# UI Components
npx shadcn@latest init

# Upload
npm install uploadthing @uploadthing/react

# Real-time (if using Pusher)
npm install pusher pusher-js

# Utilities
npm install date-fns clsx class-variance-authority
```

### Project Structure (Next.js 16)

```
my-fullstack-app/
├── app/
│   ├── (auth)/              # Auth route group
│   │   ├── login/
│   │   └── register/
│   ├── (dashboard)/         # Protected route group
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── settings/
│   ├── api/                 # API routes
│   │   ├── auth/
│   │   └── webhooks/
│   ├── layout.tsx           # Root layout
│   ├── page.tsx             # Home page
│   └── globals.css
│
├── components/
│   ├── ui/                  # shadcn/ui components
│   ├── forms/
│   └── shared/
│
├── lib/
│   ├── auth.ts              # NextAuth config
│   ├── prisma.ts            # Prisma client
│   ├── cache.ts             # Cache utilities
│   ├── utils.ts             # Utility functions
│   └── validations.ts       # Zod schemas
│
├── prisma/
│   ├── schema.prisma
│   └── migrations/
│
├── proxy.ts                 # NEW: Replaces middleware.ts
├── public/
├── types/
│   └── index.ts
│
└── next.config.ts           # TypeScript config
```

### Setup Notes (How and Why)

- `--app` opts into the App Router so you can use Server Components and streaming.
- `--turbopack` keeps local dev aligned with the default Next.js 16 bundler.
- `.env.local` keeps secrets out of git while enabling runtime configuration.
- Consider a `src/` directory once the project grows to keep the root tidy.

### First-Run Checklist

1. Create your database and set `DATABASE_URL`.
2. Run `npx prisma migrate dev` to create tables.
3. Start the dev server and verify the auth flow before building features.

---

## Next.js 16 App Router

### Understanding Server & Client Components

#### Server Components with Caching (NEW)

```typescript
// app/posts/page.tsx
'use cache'; // Opt-in to caching

import { prisma } from '@/lib/prisma';

export default async function PostsPage() {
  // This page is cached by default
  const posts = await prisma.post.findMany({
    include: { author: true },
    orderBy: { createdAt: 'desc' },
  });

  return (
    <div>
      <h1>Posts</h1>
      {posts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
          <span>By {post.author.name}</span>
        </article>
      ))}
    </div>
  );
}
```

#### Partial Pre-Rendering (PPR)

```typescript
// app/dashboard/page.tsx
import { Suspense } from 'react';

// Static shell loads instantly
export default function Dashboard() {
  return (
    <div>
      <header>Dashboard</header>

      {/* Dynamic content streams in */}
      <Suspense fallback={<Skeleton />}>
        <DynamicStats />
      </Suspense>

      <Suspense fallback={<Skeleton />}>
        <RecentActivity />
      </Suspense>
    </div>
  );
}

// This component can use 'use cache'
async function DynamicStats() {
  'use cache';
  const stats = await getStats();
  return <div>{/* ... */}</div>;
}
```

#### Client Components

```typescript
'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function LikeButton({ postId }: { postId: string }) {
  const [liked, setLiked] = useState(false);
  const router = useRouter();

  const handleLike = async () => {
    await fetch(`/api/posts/${postId}/like`, { method: 'POST' });
    setLiked(true);
    router.refresh(); // Refresh server components
  };

  return (
    <button onClick={handleLike}>
      {liked ? '❤️' : '🤍'} Like
    </button>
  );
}
```

### Server vs Client: Rules of Thumb

- Server Components: data fetching, auth checks, secrets, and heavy computation.
- Client Components: local UI state, event handlers, and browser-only APIs.
- If you need `useState`, `useEffect`, or `useRouter`, it must be a Client Component.

### Hybrid Example (Server + Client)

```typescript
// app/products/page.tsx
import { prisma } from '@/lib/prisma';
import { ProductFilter } from './product-filter';

export default async function ProductsPage() {
  const products = await prisma.product.findMany();

  return (
    <div>
      <ProductFilter initialCount={products.length} />
      <ProductGrid products={products} />
    </div>
  );
}
```

```typescript
// app/products/product-filter.tsx
'use client';

import { useState } from 'react';

export function ProductFilter({ initialCount }: { initialCount: number }) {
  const [query, setQuery] = useState('');

  // Client-only state drives UI without refetching server data.
  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <span>{initialCount} items</span>
    </div>
  );
}
```

### Session Strategy: JWT vs Database Sessions

- JWT: stateless and fast, good for edge usage, but harder to revoke instantly.
- Database sessions: easy to revoke and audit, but require database reads.

### Protecting Server Actions

```typescript
// app/actions/profile.ts
'use server';

import { auth } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function updateProfile(data: { name: string }) {
  const session = await auth(); // Re-export the NextAuth auth() helper
  if (!session?.user) throw new Error('Unauthorized');

  return prisma.user.update({
    where: { id: session.user.id },
    data: { name: data.name },
  });
}
```

---

## Cache Components & New Caching Model

### Understanding the New Caching Model

**Next.js 16 makes caching explicit and opt-in**:

- **Default**: All content is dynamic (runs at request time).
- **Opt-in**: Use `'use cache'` to cache specific components/pages.
- **Control**: New APIs for fine-grained cache management.

### Using `use cache` Directive

```typescript
// Cache an entire page
'use cache';

export default async function ProductsPage() {
  const products = await fetchProducts();
  return <ProductList products={products} />;
}

// Cache a specific component
async function ProductCard({ id }: { id: string }) {
  'use cache';
  const product = await getProduct(id);
  return <div>{product.name}</div>;
}

// Cache a function
async function getExpensiveData() {
  'use cache';
  // Expensive computation or API call
  return await complexCalculation();
}
```

### Cache Tag Management

```typescript
// lib/cache.ts
import { prisma } from '@/lib/prisma';
import {
  revalidateTag,
  updateTag,
  unstable_cacheTag as cacheTag,
} from 'next/cache';

export async function getCachedProducts() {
  'use cache';

  // Tag this cache entry
  cacheTag('products');

  return await prisma.product.findMany();
}

export async function updateProduct(id: string, data: any) {
  await prisma.product.update({ where: { id }, data });

  // Update the cache tag
  updateTag('products');
  // Or revalidate to refetch
  revalidateTag('products');
}
```

### Advanced Cache Patterns

```typescript
// app/actions/products.ts
'use server';

import { updateTag, refresh, unstable_cacheTag as cacheTag } from 'next/cache';

// Fine-grained cache control
export async function updateProductCache(productId: string) {
  // Update specific product cache
  updateTag(`product-${productId}`);

  // Also update the products list
  updateTag('products');

  // Force a full refresh if needed
  refresh();
}

// Component with cache tags
async function ProductDetails({ id }: { id: string }) {
  'use cache';

  // Tag with specific product ID
  cacheTag(`product-${id}`);

  const product = await getProduct(id);
  return <div>{/* ... */}</div>;
}
```

### How to Decide What to Cache

1. Identify data that is shared across users and changes infrequently.
2. Cache the smallest component that gives you reuse without over-caching.
3. Tag entries and revalidate those tags after mutations.

### Use Cases

- Product listings, docs, or marketing pages with periodic updates.
- Expensive aggregations like analytics summaries that refresh on a schedule.

### Common Pitfalls

- Caching user-specific data without a per-user tag.
- Forgetting to revalidate after writes, leaving stale UI.

```typescript
import { prisma } from '@/lib/prisma';
import { unstable_cacheTag as cacheTag } from 'next/cache';

// Example: cache per user safely
async function getUserDashboard(userId: string) {
  'use cache';
  cacheTag(`dashboard-${userId}`); // isolate by user
  return await prisma.dashboard.findMany({ where: { userId } });
}
```

---

## Authentication Systems

### NextAuth.js v5 Setup (Next.js 16)

#### Configuration (lib/auth.ts)

```typescript
import { NextAuthOptions } from 'next-auth';
import { PrismaAdapter } from '@auth/prisma-adapter';
import CredentialsProvider from 'next-auth/providers/credentials';
import GoogleProvider from 'next-auth/providers/google';
import { prisma } from './prisma';
import { compare } from 'bcryptjs';

export const authOptions: NextAuthOptions = {
  adapter: PrismaAdapter(prisma),
  session: {
    strategy: 'jwt',
  },
  pages: {
    signIn: '/login',
    error: '/login',
  },
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
    CredentialsProvider({
      name: 'credentials',
      credentials: {
        email: { label: 'Email', type: 'email' },
        password: { label: 'Password', type: 'password' },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) {
          throw new Error('Invalid credentials');
        }

        const user = await prisma.user.findUnique({
          where: { email: credentials.email },
        });

        if (!user || !user.hashedPassword) {
          throw new Error('Invalid credentials');
        }

        const isCorrectPassword = await compare(
          credentials.password,
          user.hashedPassword
        );

        if (!isCorrectPassword) {
          throw new Error('Invalid credentials');
        }

        return {
          id: user.id,
          email: user.email,
          name: user.name,
          image: user.image,
        };
      },
    }),
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.id = user.id;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string;
      }
      return session;
    },
  },
};
```

#### Protected Routes with Proxy

```typescript
// proxy.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { getToken } from 'next-auth/jwt';

export default async function proxy(request: NextRequest) {
  const token = await getToken({ req: request });
  const { pathname } = request.nextUrl;

  // Protected routes
  if (pathname.startsWith('/dashboard') && !token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Admin routes
  if (pathname.startsWith('/admin') && token?.role !== 'ADMIN') {
    return NextResponse.redirect(new URL('/unauthorized', request.url));
  }

  return NextResponse.next();
}
```

### Login Form with Server Actions

```typescript
// app/(auth)/login/page.tsx
'use client';

import { useState } from 'react';
import { signIn } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

const loginSchema = z.object({
  email: z.string().email('Invalid email'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
});

type LoginFormData = z.infer<typeof loginSchema>;

export default function LoginPage() {
  const [error, setError] = useState('');
  const router = useRouter();

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginFormData) => {
    setError('');

    const result = await signIn('credentials', {
      email: data.email,
      password: data.password,
      redirect: false,
    });

    if (result?.error) {
      setError('Invalid credentials');
      return;
    }

    router.push('/dashboard');
    router.refresh();
  };

  return (
    <div className="max-w-md mx-auto mt-12 p-6 bg-white rounded-lg shadow">
      <h1 className="text-2xl font-bold mb-6">Login</h1>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <div>
          <Input
            {...register('email')}
            type="email"
            placeholder="Email"
            className={errors.email ? 'border-red-500' : ''}
          />
          {errors.email && (
            <p className="text-red-500 text-sm mt-1">{errors.email.message}</p>
          )}
        </div>

        <div>
          <Input
            {...register('password')}
            type="password"
            placeholder="Password"
            className={errors.password ? 'border-red-500' : ''}
          />
          {errors.password && (
            <p className="text-red-500 text-sm mt-1">{errors.password.message}</p>
          )}
        </div>

        {error && <p className="text-red-500 text-sm">{error}</p>}

        <Button type="submit" disabled={isSubmitting} className="w-full">
          {isSubmitting ? 'Loading...' : 'Login'}
        </Button>
      </form>

      <div className="mt-6">
        <Button
          variant="outline"
          onClick={() => signIn('google', { callbackUrl: '/dashboard' })}
          className="w-full"
        >
          Continue with Google
        </Button>
      </div>
    </div>
  );
}
```

---

## Database & ORM (Prisma)

### Prisma Schema (Same as before - remains compatible)

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id             String    @id @default(cuid())
  name           String?
  email          String    @unique
  emailVerified  DateTime?
  image          String?
  hashedPassword String?
  createdAt      DateTime  @default(now())
  updatedAt      DateTime  @updatedAt

  accounts Account[]
  sessions Session[]
  posts    Post[]
  comments Comment[]
  likes    Like[]

  @@map("users")
}

model Post {
  id        String    @id @default(cuid())
  title     String
  content   String    @db.Text
  published Boolean   @default(false)
  authorId  String    @map("author_id")
  createdAt DateTime  @default(now())
  updatedAt DateTime  @updatedAt

  author   User      @relation(fields: [authorId], references: [id], onDelete: Cascade)
  comments Comment[]
  likes    Like[]

  @@index([authorId])
  @@map("posts")
}

// ... (rest of schema same as before)
```

### Database Operations with Cache Tags

```typescript
// lib/db/posts.ts
import { prisma } from '@/lib/prisma';
import { unstable_cacheTag as cacheTag } from 'next/cache';

export async function getCachedPosts(userId?: string) {
  'use cache';

  // Tag this query
  cacheTag('posts');
  if (userId) cacheTag(`user-posts-${userId}`);

  return await prisma.post.findMany({
    where: userId ? { authorId: userId } : { published: true },
    include: {
      author: { select: { name: true, image: true } },
      _count: { select: { likes: true, comments: true } },
    },
    orderBy: { createdAt: 'desc' },
  });
}
```

### Why Prisma Works Well Here

Prisma gives you type-safe queries, predictable migrations, and a single source of truth for your data model. The biggest win for teams is that schema changes surface TypeScript errors in code that still assumes the old shape.

### Migration Workflow (Local Development)

```bash
npx prisma migrate dev --name init
npx prisma generate
```

### Transaction Example

```typescript
import { prisma } from '@/lib/prisma';

export async function publishPost(postId: string, userId: string) {
  return prisma.$transaction(async (tx) => {
    const post = await tx.post.update({
      where: { id: postId, authorId: userId },
      data: { published: true },
    });

    await tx.activity.create({
      data: { type: 'POST_PUBLISHED', userId, postId },
    });

    return post;
  });
}
```

---

## API Routes & Server Actions

### When to Use Which

- API routes: external clients, webhooks, file uploads, OAuth callbacks.
- Server actions: internal form submissions, mutations triggered by your UI, tight cache control.

### API Route Example (REST-style)

```typescript
// app/api/posts/route.ts
import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import { z } from 'zod';

const createPostSchema = z.object({
  title: z.string().min(1),
  content: z.string().min(1),
});

export async function GET() {
  const posts = await prisma.post.findMany({ where: { published: true } });
  return NextResponse.json(posts);
}

export async function POST(request: Request) {
  const body = await request.json();
  const input = createPostSchema.parse(body); // validate before DB write

  const post = await prisma.post.create({ data: input });
  return NextResponse.json(post, { status: 201 });
}
```

### Server Action Example (Form Submission)

```typescript
// app/actions/posts.ts
'use server';

import { revalidateTag } from 'next/cache';
import { z } from 'zod';
import { prisma } from '@/lib/prisma';

const postSchema = z.object({
  title: z.string().min(1),
  content: z.string().min(1),
});

export async function createPostAction(formData: FormData) {
  const input = postSchema.parse({
    title: formData.get('title'),
    content: formData.get('content'),
  });

  await prisma.post.create({ data: input });
  revalidateTag('posts'); // keep cached lists fresh
}
```

### Use Cases

- API routes for integrations and webhooks.
- Server actions for app-owned forms and mutations.

---

## Proxy System (Replaces Middleware)

### New `proxy.ts` File

The `proxy.ts` file replaces `middleware.ts` for clearer network boundaries:

```typescript
// proxy.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export default async function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Authentication check
  const token = request.cookies.get('session')?.value;

  if (pathname.startsWith('/dashboard') && !token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Add custom headers
  const response = NextResponse.next();
  response.headers.set('x-custom-header', 'value');

  // Rewrite URLs
  if (pathname.startsWith('/blog')) {
    return NextResponse.rewrite(new URL('/news', request.url));
  }

  return response;
}

export const config = {
  matcher: [
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
};
```

### What Belongs in `proxy.ts`

- Auth gates, redirects, and rewrites.
- Simple header manipulation (locale, AB tests, tracing).
- Lightweight, fast logic that can run at the edge.

### What to Avoid in `proxy.ts`

- Slow database queries and large body parsing.
- Expensive computation or long-running network calls.

### Migrating from Middleware to Proxy

```typescript
// OLD: middleware.ts
export function middleware(request: NextRequest) {
  // ...
}

// NEW: proxy.ts (same functionality)
export default async function proxy(request: NextRequest) {
  // Same logic works here
}
```

---

## File Upload & Storage

### Why Direct-to-Storage

Sending large files through your app server increases latency and memory pressure. The typical flow is: create a signed upload URL, upload directly to storage, then save metadata in the database.

### Signed Upload Example (API Route)

Create a small helper that talks to your storage provider (S3, Supabase Storage, or UploadThing) and returns the upload URL and fields.

```typescript
// app/api/uploads/route.ts
import { NextResponse } from 'next/server';
import { createPresignedUpload } from '@/lib/uploads';

export async function POST() {
  const upload = await createPresignedUpload({
    folder: 'avatars',
    maxSizeMb: 5,
  });

  return NextResponse.json(upload);
}
```

### Client Upload Example

```typescript
'use client';

export async function uploadAvatar(file: File) {
  const { url, fields } = await fetch('/api/uploads', { method: 'POST' })
    .then((response) => response.json());

  const form = new FormData();
  Object.entries(fields).forEach(([key, value]) => form.append(key, String(value)));
  form.append('file', file);

  await fetch(url, { method: 'POST', body: form });
}
```

### Use Cases

- Profile images, documents, and media assets.
- Large imports or user-generated content.

### Security Tips

- Validate MIME type and size server-side.
- Store only the file URL and metadata in your database.

---

## State Management

### Server State vs UI State

Server state is data from the backend; prefer Server Components and revalidate after mutations. UI state is local (filters, modals); keep it in Client Components or a small Zustand store.

### Zustand Example (UI State)

```typescript
// lib/store/ui.ts
import { create } from 'zustand';

type UiState = {
  isSidebarOpen: boolean;
  toggleSidebar: () => void;
};

export const useUiStore = create<UiState>((set) => ({
  isSidebarOpen: false,
  toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),
}));
```

```typescript
// app/components/sidebar-toggle.tsx
'use client';

import { useUiStore } from '@/lib/store/ui';

export function SidebarToggle() {
  const { isSidebarOpen, toggleSidebar } = useUiStore();

  return (
    <button onClick={toggleSidebar}>
      {isSidebarOpen ? 'Hide' : 'Show'} Sidebar
    </button>
  );
}
```

### Use Cases

- Modals, toasts, theme toggles, and client-only filters.

---

## Real-time Features

### When Real-time Makes Sense

Use real-time updates for chat, notifications, live dashboards, and collaborative editing.

### Pusher Example (Client)

```typescript
'use client';

import { useEffect, useState } from 'react';
import Pusher from 'pusher-js';

export function Notifications() {
  const [messages, setMessages] = useState<string[]>([]);

  useEffect(() => {
    const pusher = new Pusher(process.env.NEXT_PUBLIC_PUSHER_KEY!, {
      cluster: 'us2',
    });

    const channel = pusher.subscribe('notifications');

    channel.bind('new-message', (data: { text: string }) => {
      setMessages((prev) => [data.text, ...prev]);
    });

    return () => {
      channel.unbind_all();
      pusher.disconnect();
    };
  }, []);

  return (
    <ul>
      {messages.map((message, index) => (
        <li key={index}>{message}</li>
      ))}
    </ul>
  );
}
```

---

## SEO & Metadata

### Static Metadata

```typescript
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Acme Docs',
  description: 'Guides, API references, and tutorials for Acme.',
};
```

### Dynamic Metadata

```typescript
import type { Metadata } from 'next';
import { prisma } from '@/lib/prisma';

export async function generateMetadata(
  { params }: { params: { slug: string } }
): Promise<Metadata> {
  const post = await prisma.post.findUnique({ where: { slug: params.slug } });

  return {
    title: post?.title ?? 'Post',
    description: post?.excerpt ?? 'Read the latest post.',
    openGraph: {
      title: post?.title ?? 'Post',
      description: post?.excerpt ?? 'Read the latest post.',
    },
  };
}
```

### SEO Tips

- Generate Open Graph images for social previews.
- Provide clean, descriptive titles and meta descriptions.
- Use stable, readable URLs and avoid query-heavy paths.

---

## Performance Optimization

### Turbopack Configuration

```typescript
// next.config.ts
import type { NextConfig } from 'next';

const config: NextConfig = {
  // Turbopack is now default in Next.js 16
  experimental: {
    turbo: {
      // Additional Turbopack configuration if needed
    },
  },
};

export default config;
```

### Image Optimization

```typescript
import Image from 'next/image';

export function OptimizedImage({ src, alt }: { src: string; alt: string }) {
  return (
    <Image
      src={src}
      alt={alt}
      width={800}
      height={600}
      priority={false}
      placeholder="blur"
      blurDataURL="data:image/..."
      className="rounded-lg"
    />
  );
}
```

### Route Caching with `use cache`

```typescript
// Static page with caching
'use cache';

export default async function StaticPage() {
  const data = await fetchData();
  return <div>{/* ... */}</div>;
}

// Dynamic page (default in Next.js 16)
export default async function DynamicPage() {
  // No 'use cache' = dynamic at request time
  const data = await fetchData();
  return <div>{/* ... */}</div>;
}
```

### Quick Performance Wins

- Prefer Server Components for data to reduce the client bundle.
- Split heavy client-only widgets with `next/dynamic`.
- Use `next/font` to avoid layout shift from late-loading fonts.

```typescript
import dynamic from 'next/dynamic';

const Chart = dynamic(() => import('@/components/chart'), {
  ssr: false,
  loading: () => <div>Loading chart...</div>,
});
```

---

## Testing Strategy

### Test Pyramid (Practical)

- Unit tests: pure functions, validation, formatting.
- Integration tests: API routes and server actions with a test database.
- E2E tests: full user flows with Playwright.

### Unit Test Example (Vitest)

```typescript
import { describe, it, expect } from 'vitest';
import { formatPrice } from '@/lib/pricing';

describe('formatPrice', () => {
  it('formats USD values', () => {
    expect(formatPrice(1299)).toBe('$12.99');
  });
});
```

### E2E Example (Playwright)

```typescript
import { test, expect } from '@playwright/test';

test('login flow', async ({ page }) => {
  await page.goto('/login');
  await page.fill('input[type="email"]', 'demo@example.com');
  await page.fill('input[type="password"]', 'password123');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});
```

---

## Deployment

### Vercel Deployment with Next.js 16

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### Environment Variables

```bash
# .env.local
DATABASE_URL="postgresql://..."
NEXTAUTH_SECRET="your-secret"
NEXTAUTH_URL="http://localhost:3000"
GOOGLE_CLIENT_ID="..."
GOOGLE_CLIENT_SECRET="..."
```

### Deployment Checklist

- Run `prisma migrate deploy` to apply production migrations.
- Set `NEXTAUTH_URL` to your production domain.
- Use `NEXT_PUBLIC_` prefixes for browser-exposed variables only.
- Verify storage, webhooks, and OAuth callback URLs in production.

### Edge vs Node Runtime (When It Matters)

- Edge: fast cold starts, good for routing, headers, and lightweight logic.
- Node: required for heavy libraries, database drivers, and long-running tasks.

---

## Best Practices for Next.js 16

### 1. Embrace the New Caching Model

- Start with dynamic rendering (default).
- Add `'use cache'` only where needed.
- Use cache tags for fine-grained control.

### 2. Use Turbopack Features

- Leverage faster builds automatically.
- Enable file system caching for large apps.

### 3. Migrate to Proxy System

- Replace `middleware.ts` with `proxy.ts`.
- Clarify network boundaries.

### 4. Leverage React Compiler

- Remove manual `useMemo` and `useCallback`.
- Let the compiler optimize automatically.

### 5. Security

- Validate all inputs server-side.
- Use NextAuth for authentication.
- Implement proper authorization in proxy.ts.

### 6. Observability

- Add structured logging for errors and slow queries.
- Track core user flows with analytics and traces.
- Set up alerts for auth failures and webhook errors.

---

## Summary

Next.js 16 brings significant improvements:

- **Explicit Caching**: Opt-in with `'use cache'`.
- **Turbopack (Stable)**: 2-5x faster builds.
- **Cache Components**: Fine-grained control.
- **Proxy System**: Replace `middleware.ts`.
- **React 19.2**: Compiler and better Server Components.
- **Enhanced DX**: Better logging, debugging, tooling.

This modern stack enables rapid development of production-ready applications with excellent performance and developer experience.

---

## Resources

- **Next.js 16 Announcement**: https://nextjs.org/blog/next-16
- **Next.js 16.1 Update**: https://nextjs.org/blog/next-16-1
- **Prisma Documentation**: https://www.prisma.io/docs
- **NextAuth.js**: https://next-auth.js.org/
- **shadcn/ui**: https://ui.shadcn.com/
- **Vercel**: https://vercel.com/docs

