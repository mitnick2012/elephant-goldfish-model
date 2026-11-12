<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# Go Language Pack

## Detection

- `go.mod`, `go.work`.

## Source Extensions

- `.go`.
- Generated, never source: files whose header contains
  `// Code generated ... DO NOT EDIT.`, such as `*.pb.go`.

## Ignored Paths

- `vendor/`, `testdata/`.

## Test Conventions

- Files `*_test.go` and the `testdata/` directory.

## Public Interface

- Exported identifiers (names starting with an upper-case letter):
  functions, types, methods, constants, and variables.
- Packages under an `internal/` directory are importable only from their
  parent tree. Record this as an invariant.
- `package main`: list its CLI flags and commands, not its identifiers.
  Skip exported methods of unexported types unless an exported API returns
  those types.
- Routes: cite the exact pattern from `http.HandleFunc`, `mux.Handle`, and
  router calls such as `r.GET`, `r.Post`, or `e.GET`.
- CLI: `flag.*` definitions and `cobra.Command` `Use` fields.

## Definition Patterns

- Unindented `func`, `type`, `var`, and `const` lines.

## Read Order

- Contracts: `doc.go`, interface type declarations, and `go.mod`
  requirements.
- Entry points: `main.go` in `package main`, and `cmd/*/main.go`.

## Signals

- Invariants: `panic`, sentinel errors (`var Err... = errors.New`), guard
  returns of `error`, and `sync.Mutex` / `sync.RWMutex` guarded fields.
- Side effects: `os`, `io/fs`, `net/http`, `database/sql`, `exec.Command`,
  `os.Getenv`, goroutines started with `go`, and package-level `var` state
  written after `init`.

## Verification

- `go -C <module_dir> test ./<path from module>/...`, where `<module_dir>`
  holds the nearest `go.mod`. Use `./...` at the module root.
