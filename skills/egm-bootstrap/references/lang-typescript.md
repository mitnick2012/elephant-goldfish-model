<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# TypeScript and JavaScript Language Pack

## Detection

- `package.json`, `tsconfig.json`, `jsconfig.json`, `deno.json`,
  `deno.jsonc`, `angular.json`.

## Source Extensions

- `.ts`, `.tsx`, `.mts`, `.cts`, `.js`, `.jsx`, `.mjs`, `.cjs`, `.vue`,
  `.svelte`, `.astro`.

## Ignored Paths

- `node_modules/`, `dist/`, `build/`, `out/`, `coverage/`, `.next/`,
  `.nuxt/`, `.svelte-kit/`, `.turbo/`, `.output/`.
- Generated or minified files: `*.min.js`, `*.map`.

## Test Conventions

- Files `*.test.*`, `*.spec.*`, `*.e2e.*`, `*.stories.*`.
- Directories `__tests__/`, `__mocks__/`, `e2e/`, `cypress/`.

## Public Interface

- `export` declarations, including `export default` and re-exports. In
  CommonJS: `module.exports` and `exports.<name>` assignments.
- A package's interface is its `package.json` `exports`, `main`, `module`,
  and `types` entry points and the barrel files they name (`index.ts`),
  and `bin` entries (CLI interface).
- Hand-written `.d.ts` files define the interface for their module.
- Routes: Express / Koa / Fastify calls (`app.get`, `router.post`), NestJS
  decorators (`@Get`, `@Post` with their path), and file-based routes only
  when `next`, `nuxt`, or `@sveltejs/kit` is a `package.json` dependency.
  Cite the exported handler (`[app/orders/[id]/route.ts:GET]`,
  `[src/routes/+server.ts:GET]`) and derive the path by the framework
  convention: `(group)` segments and `@slot` folders are not in the URL.
- Framework components: Vue `defineProps`, `defineEmits`, `defineModel`;
  Svelte `export let` / `$props`; React component props types; Angular
  `@Component` `selector`, `@Input` / `input()`, `@Output` / `output()`.

## Definition Patterns

- Top-level `export` lines, and unindented `function`, `async function`,
  `class`, `interface`, `type`, `enum`, and `const` declarations.

## Read Order

- Contracts: `.d.ts` files, schema files (zod, `prisma/schema.prisma`,
  GraphQL SDL), and `package.json` `exports` and `dependencies`.
- Entry points: `index.*`, `main.*`, `server.*`, `app.*`.

## Signals

- Invariants: zod / yup / valibot schemas, guard clauses that `throw`,
  `readonly` members, `as const`, `Object.freeze`.
- Side effects: `fetch`, `axios`, `fs` / `node:fs`, `child_process`,
  `process.env`, `localStorage` / `sessionStorage`, ORM calls, and
  module-level mutable state.

## Verification

- Use `package.json` `scripts.test` with the lockfile's package manager:
  `pnpm-lock.yaml` -> `pnpm test`, `yarn.lock` -> `yarn test`,
  `bun.lockb` / `bun.lock` -> `bun run test`, otherwise `npm test`. The
  `packageManager` field wins over lockfile detection.
- Workspace packages (`<name>` is the nearest `package.json` `name`):
  `pnpm --filter <name> test`, `yarn workspace <name> test`,
  `bun run --filter <name> test`, or `npm test -w <name>`.
- Deno: `deno task test` when `deno.json` defines it, otherwise
  `deno test path/to/D`.
- No `scripts.test`: `<test-command>`.
