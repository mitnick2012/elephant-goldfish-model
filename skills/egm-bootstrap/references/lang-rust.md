<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# Rust Language Pack

## Detection

- `Cargo.toml`.

## Source Extensions

- `.rs`.

## Ignored Paths

- `target/`.

## Test Conventions

- Directories `tests/` and `benches/` next to `Cargo.toml`.
- Inside a source file, skip `#[cfg(test)] mod tests { ... }` blocks and
  `#[test]` functions.

## Public Interface

- `pub` items reachable from the crate root (`lib.rs`) through `pub mod`
  and `pub use`. `pub(crate)`, `pub(super)`, and `pub(in ...)` items are not
  interface.
- Give each scout the crate root's `mod` and `pub use` lines so it can judge
  reachability.
- `#[macro_export] macro_rules!` items are interface at the crate root.
- Binary-only crates: list clap `#[command]` and `#[arg]` items instead of
  `pub` items.
- List public trait implementations (`impl Trait for Type`) under the type.
- Record `[features]` from `Cargo.toml` and the `#[cfg(feature = ...)]`
  items they gate as invariants.
- Routes: cite the exact path from axum `.route("/x", ...)`, actix
  `#[get("/x")]`, and similar macros.

## Definition Patterns

- Lines declaring `fn`, `struct`, `enum`, `trait`, `type`, `const`,
  `static`, `mod`, `union`, `impl`, or `macro_rules!`, with any `pub(...)` and `async`
  prefixes.

## Read Order

- Contracts: `Cargo.toml` (dependencies and features) and trait
  definitions.
- Entry points: `lib.rs`, `main.rs`, `mod.rs`, and `src/bin/*.rs`.

## Signals

- Invariants: `assert!`, `debug_assert!`, `panic!`, `unreachable!`,
  `unsafe` blocks with their `// SAFETY:` comments, and newtype
  constructors that validate input.
- Side effects: `std::fs`, `std::net`, `std::process`, `std::env`,
  `tokio::spawn`, `reqwest`, database clients, and `static` items with
  interior mutability (`Mutex`, `OnceLock`, atomics).

## Verification

- Crate inside a workspace: `cargo test -p <name>` with `<name>` from the
  nearest `Cargo.toml` `[package]`.
- Workspace root: `cargo test --workspace`.
- Single crate (no `[workspace]`): `cargo test`.
