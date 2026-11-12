<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# Python Language Pack

## Detection

- `pyproject.toml`, `setup.py`, `setup.cfg`, `pytest.ini`, `tox.ini`,
  `noxfile.py`, `Pipfile`, `requirements*.txt`.

## Source Extensions

- `.py`, `.pyi`, `.pyx`, `.pxd`.

## Ignored Paths

- `__pycache__/`, `.venv/`, `venv/`, `.tox/`, `.nox/`, `.mypy_cache/`,
  `.pytest_cache/`, `.ruff_cache/`, `*.egg-info/`, `site-packages/`.

## Test Conventions

- Files `test_*.py`, `*_test.py`, and `conftest.py`.
- Directories `tests/` and `test/`.

## Public Interface

- A literal `__all__` list or tuple alone defines a module's interface.
- Otherwise list top-level `def`, `class`, and assignments without a leading
  underscore. Imported names count only as `__init__.py` re-exports or
  `from x import Y as Y`.
- Modules and packages whose names start with `_` are not interface.
- Per directory: list each module's interface and mark `__init__.py`
  re-exports as the package interface.
- When a `.pyi` stub exists, it defines the interface for its module.
- Routes: cite the exact path from FastAPI or Flask decorators
  (`@app.get`, `@router.post`, `@app.route`) and Django `urls.py`
  `path()` / `re_path()` calls.
- CLI: `argparse` `add_argument` flags, `click` / `typer` commands, and
  `[project.scripts]` in `pyproject.toml`.

## Definition Patterns

- Unindented `def`, `async def`, and `class` lines, plus unindented
  `UPPER_CASE =` constants.

## Read Order

- Contracts: `.pyi` stubs, ORM models (SQLAlchemy `__tablename__`, Django
  `models.Model`), Pydantic models, and `pyproject.toml` dependencies.
- Entry points: `__init__.py`, `__main__.py`, `main.py`, `app.py`, `cli.py`.

## Signals

- Invariants: `assert`, `raise ValueError` / `TypeError` guard clauses,
  Pydantic validators, `@dataclass(frozen=True)`, `typing.Final`, and
  `threading.Lock` / `asyncio.Lock`.
- Side effects: `open()`, `pathlib` writes, `requests` / `httpx` /
  `aiohttp`, `subprocess`, `os.environ`, database `commit()`, and mutable
  module-level state.

## Verification

- pytest is configured by `[tool.pytest.ini_options]` in `pyproject.toml`,
  `pytest.ini`, `[tool:pytest]` in `setup.cfg`, or `[pytest]` in `tox.ini`.
- Run from the project root: `pytest tests/<path mirroring D>` when that
  directory exists, otherwise `pytest`.
- Prefix `uv run` when `uv.lock` exists, or `poetry run` when
  `poetry.lock` exists.
- No pytest config: `tox` or `nox` if configured, otherwise
  `<test-command>`.
- Prefix `cd <project_dir> &&` when the project root is not the repository
  root.
