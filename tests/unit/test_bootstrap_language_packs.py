# Copyright 2026 Google LLC.
# SPDX-License-Identifier: Apache-2.0

"""Keep the egm-bootstrap language router and its packs in sync."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / "skills" / "egm-bootstrap"
REFERENCES = SKILL_DIR / "references"
ROUTER = REFERENCES / "language-router.md"
SECTIONS = ("Detection", "Source Extensions", "Ignored Paths",
            "Test Conventions", "Public Interface", "Definition Patterns",
            "Read Order", "Signals", "Verification")
# Source extensions listed in egm-bootstrap Step 2 before language packs.
LEGACY_EXTENSIONS = (
    ".c .cc .cpp .cxx .h .hh .hpp .rs .go .zig .lean .f .f90 .f95 .f03 .f08 "
    ".hs .java .kt .scala .cs .razor .cshtml .fs .vb .py .rb .php .lua .sh "
    ".bash .ps1 .psm1 .psd1 .r .R .ex .exs .ts .tsx .js .jsx .mjs .cjs .swift "
    ".m .dart .sql .proto .graphql .gql .thrift .prisma .tf .hcl .cue"
).split()


def _router_rows() -> list[tuple[str, str]]:
  rows = []
  for line in ROUTER.read_text(encoding="utf-8").splitlines():
    match = re.match(r"^\|(.+)\|.*\|\s*`references/(lang-[a-z0-9-]+\.md)`\s*\|$",
                     line)
    if match:
      rows.append((match.group(2), match.group(1)))
  return rows


def _section(text: str, name: str) -> str:
  match = re.search(rf"^## {name}\n(.*?)(?=^## |\Z)", text,
                    flags=re.MULTILINE | re.DOTALL)
  assert match, f"missing section {name}"
  return match.group(1)


def test_skill_routes_through_router() -> None:
  skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
  assert "(references/language-router.md)" in skill


def test_router_table_matches_pack_files() -> None:
  routed = [pack for pack, _ in _router_rows()]
  assert "lang-generic.md" in routed, "the generic fallback pack must be routed"
  assert len(routed) == len(set(routed)), "a pack is routed more than once"
  assert sorted(routed) == sorted(p.name for p in REFERENCES.glob("lang-*.md"))


@pytest.mark.parametrize("pack, manifests", _router_rows(),
                         ids=lambda value: value if value.endswith(".md") else "")
def test_router_manifests_listed_in_pack_detection(pack: str,
                                                   manifests: str) -> None:
  detection = _section((REFERENCES / pack).read_text(encoding="utf-8"),
                       "Detection")
  for manifest in re.findall(r"`([^`]+)`", manifests):
    if not manifest.startswith("."):
      assert f"`{manifest}`" in detection, f"{pack} Detection lacks {manifest}"


@pytest.mark.parametrize("pack", sorted(p.name for p in REFERENCES.glob("lang-*.md")))
def test_pack_defines_every_section_in_order(pack: str) -> None:
  text = (REFERENCES / pack).read_text(encoding="utf-8")
  assert "SPDX-License-Identifier: Apache-2.0" in text
  headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
  assert headings == list(SECTIONS), f"{pack}: sections must be {SECTIONS}"


def test_generic_pack_keeps_legacy_extensions() -> None:
  extensions = _section(
      (REFERENCES / "lang-generic.md").read_text(encoding="utf-8"),
      "Source Extensions")
  for ext in LEGACY_EXTENSIONS:
    assert f"`{ext}`" in extensions, f"lang-generic.md lost {ext}"
