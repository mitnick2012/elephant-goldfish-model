<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# egm-bootstrap Language Router

Read by Step 0 of `SKILL.md`. Language packs live next to this file.

## Routing Table

| Manifests | Extensions | Pack |
| :--- | :--- | :--- |
| `*.csproj`, `*.fsproj`, `*.vbproj`, `Directory.Build.props`, `global.json`, and `*.sln` / `*.slnx` that list one of these projects | `.cs`, `.csx`, `.fs`, `.fsi`, `.vb`, `.razor`, `.cshtml` | `references/lang-dotnet.md` |
| `pyproject.toml`, `setup.py`, `setup.cfg`, `pytest.ini`, `tox.ini`, `noxfile.py`, `Pipfile`, `requirements*.txt` | `.py`, `.pyi`, `.pyx` | `references/lang-python.md` |
| `package.json`, `tsconfig.json`, `jsconfig.json`, `deno.json`, `deno.jsonc`, `angular.json` | `.ts`, `.tsx`, `.mts`, `.cts`, `.js`, `.jsx`, `.mjs`, `.cjs`, `.vue`, `.svelte`, `.astro` | `references/lang-typescript.md` |
| `go.mod`, `go.work` | `.go` | `references/lang-go.md` |
| `Cargo.toml` | `.rs` | `references/lang-rust.md` |
| `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle`, `settings.gradle.kts`, `build.sbt` | `.java`, `.kt`, `.scala`, `.groovy` | `references/lang-jvm.md` |
| `CMakeLists.txt`, `meson.build`, `conanfile.txt`, `conanfile.py`, `vcpkg.json`, `*.vcxproj` | `.c`, `.cc`, `.cpp`, `.cxx`, `.h`, `.hh`, `.hpp`, `.hxx`, `.cu` | `references/lang-cpp.md` |
| Always | Every other extension | `references/lang-generic.md` |

## Loading

1. Always read `lang-generic.md`.
2. Read a pack as soon as Step 0 (at the root) or the Step 2 BFS (in any
   subtree) finds one of its manifests or extensions. Read it before you
   list that directory's children. Never read an unmatched pack.
3. Pass the absolute paths of loaded packs to workers as `language_packs`. A
   worker with no `language_packs` routes its own `sub_tree_root` with this
   table.
4. Bazel: when the tree has `BUILD` or `BUILD.bazel` files and a
   `MODULE.bazel` or `WORKSPACE`, verification follows the SKILL.md Bazel
   rules. Language packs still supply interface rules.

## Scope

- A pack's Ignored Paths, Test Conventions, and generated-file rules apply
  only under the directory that holds its manifest (or where its extension
  was found), and only to files of its extensions.
- File-level rules (Public Interface, Definition Patterns, Signals) come from
  the pack that matches the file's extension, otherwise from
  `lang-generic.md`.
- Directory-level rules (Read Order, Verification) come from the pack that
  matches most of `D`'s source files. Verification uses the nearest manifest
  of that pack.
- Dedicated packs override `lang-generic.md` where they disagree.

## Applying Packs in Step 4

- Workers skip loaded packs' Ignored Paths, generated files, and Test
  Conventions during traversal.
- A chunk boundary starts at the first decorator, attribute, annotation, or
  doc-comment line above a Definition Patterns match.
- Each scout's spawn prompt, not its registration, gets the matching pack's
  Public Interface, Signals, and in-file test rules, plus any context the
  pack's Public Interface asks for.

## Adding a Language

1. Create `references/lang-<name>.md` with the nine sections: Detection,
   Source Extensions, Ignored Paths, Test Conventions, Public Interface,
   Definition Patterns, Read Order, Signals, Verification.
2. Add one row to the Routing Table. Its manifests must also appear in the
   pack's Detection section.
3. Run `pytest tests/unit/test_bootstrap_language_packs.py`.
