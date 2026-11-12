<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# C and C++ Language Pack

## Detection

- `CMakeLists.txt`, `meson.build`, `conanfile.txt`, `conanfile.py`,
  `vcpkg.json`, `*.vcxproj`. `BUILD` / `BUILD.bazel` follow the Bazel rules in SKILL.md.

## Source Extensions

- `.c`, `.cc`, `.cpp`, `.cxx`, `.h`, `.hh`, `.hpp`, `.hxx`, `.ipp`,
  `.inl`, `.cu`, `.cuh`.

## Ignored Paths

- `build/`, `out/`, `cmake-build-*/`, `_deps/`, `CMakeFiles/`.

## Test Conventions

- Files `*_test.cc`, `*_test.cpp`, `*_unittest.cc`, `test_*.c`, and
  directories `test/` and `tests/`.

## Public Interface

- Declarations in headers are interface; headers under `include/` are the
  installed interface.
- Not interface: `static` functions and anonymous-namespace symbols in
  source files, and `detail` / `internal` / `impl` namespaces.
- C: functions and types declared in headers without `static`.
- Class members: only `public:` members, and `protected:` members of
  non-`final` classes. `class` members default to private and `struct`
  members to public.
- Record exported library targets (`add_library`, `install(TARGETS ...)`)
  as interface.

## Definition Patterns

- Lines declaring `class`, `struct`, `enum`, `union`, `namespace`,
  `template`, `typedef`, `using`, `#define`, and function signatures at
  namespace scope.

## Read Order

- Contracts: headers first (`.h`, `.hh`, `.hpp`), then `CMakeLists.txt` /
  `meson.build` targets and dependencies.
- Entry points: files defining `main`, and files named after the directory.

## Signals

- Invariants: `assert`, `static_assert`, `CHECK` / `DCHECK`, thread-safety
  annotations (`ABSL_GUARDED_BY`, `GUARDED_BY`), `const` and `noexcept`
  contracts.
- Side effects: file and socket I/O, `getenv`, global or static mutable
  state, singletons, and threads (`std::thread`, `pthread_create`).

## Verification

- CMake with `enable_testing()` or `add_test`: `ctest --preset <name>` when
  `CMakePresets.json` has `testPresets`, otherwise
  `cmake -B build && cmake --build build && ctest --test-dir build`.
- Meson: `meson setup builddir && meson test -C builddir`.
- Make: `make test` or `make check`, whichever target exists.
- `*.vcxproj` only: `<test-command>` unless the repository has a test
  script.
- Otherwise `<test-command>`.
