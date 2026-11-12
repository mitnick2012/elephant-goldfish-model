<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# Generic Language Pack

Always loaded. It covers every language without a dedicated pack. A dedicated
pack adds to these rules for its language and replaces them where the two
disagree.

## Detection

- Always loaded.

## Source Extensions

- Systems & Compiled: `.c`, `.cc`, `.cpp`, `.cxx`, `.h`, `.hh`, `.hpp`, `.rs`,
  `.go`, `.zig`, `.lean`, `.f`, `.f90`, `.f95`, `.f03`, `.f08`, `.hs`
- Managed & Enterprise: `.java`, `.kt`, `.scala`, `.cs`, `.razor`, `.cshtml`,
  `.fs`, `.vb`
- Scripting & Dynamic: `.py`, `.rb`, `.php`, `.lua`, `.sh`, `.bash`, `.ps1`,
  `.psm1`, `.psd1`, `.r`, `.R`, `.ex`, `.exs`
- Web & Mobile: `.ts`, `.tsx`, `.js`, `.jsx`, `.mjs`, `.cjs`, `.swift`, `.m`,
  `.dart`
- Data & Schemas / IDLs: `.sql`, `.proto`, `.graphql`, `.gql`, `.thrift`,
  `.prisma`
- Infrastructure / Declarative Code: `.tf`, `.hcl`, `.cue`
- Never source: build manifests, lockfiles, test fixtures, documentation, and
  data dumps such as `.csv`, `.tsv`, `.parquet`.

## Ignored Paths

- None beyond the SKILL.md list, `.gitignore`, and `.egmignore`.

## Test Conventions

- Directories named `tests`, `testing`, or `testdata`.
- Files matching `*_test.*`, `*Test.*`, `test_*.*`, or `*.spec.*`.

## Public Interface

- Treat top-level declarations that the language exports by default as
  public. When the language has a visibility keyword or naming rule, follow it.
  If visibility cannot be determined from code, list the symbol and do not
  guess its visibility.

## Definition Patterns

- Lines that start a top-level `class`, `def`, `func`, `fn`, `function`,
  `interface`, `struct`, `enum`, `trait`, `module`, or `type` declaration.

## Read Order

- Contracts: headers (`.h`, `.hh`, `.hpp`), `.proto`, `.graphql`, `.gql`,
  `.thrift`, `.prisma`, `.sql` DDL, and interface or protocol declarations.
- Entry points: `main.*`, `index.*`, `lib.*`, `mod.*`, `__init__.py`, or a
  file named after the directory.

## Signals

- Invariants: explicit assertions, guard clauses that throw or return errors,
  locks, and declared constraints.
- Side effects: file, network, database, process, and environment access, and
  writes to module-level or global state.

## Verification

- `Makefile` with a `test` target: `make test`. Otherwise `<test-command>`.
