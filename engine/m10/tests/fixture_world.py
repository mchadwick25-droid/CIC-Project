"""A complete fixture world under a temporary root, and no-op dependencies."""
from __future__ import annotations

import json
from pathlib import Path

from engine.m10.handoff import Deps
from engine.m10.reviewfile import HEADER_FIELDS, SIMULATED_REVIEW_LABEL

CODE = "fx"
SLUG = "fx-tradition"
TEXT_FILE = "fxvol01_test.txt"
QUOTE = "the bishop gathered his monks at dawn and read them the whole letter aloud"

TEXT = f"""Title: Test Volume
Rights: Public domain

Chapter one. In that year {QUOTE}, and none of them spoke.
"""


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def review_text(round_number: int = 1, *, cleared: bool = True) -> str:
    fields = {
        "Reviewer model": "claude-opus-5-5",
        "Drafter model": "claude-sonnet-5-5",
        "Reviewer agent": "review-session-1",
        "Drafter agent": "draft-session-1",
        "Round": str(round_number),
        "Truncation check, method 1": "final line of every section read",
        "Truncation check, method 2": "section count against the table of contents",
    }
    assert tuple(fields) == HEADER_FIELDS
    header = "\n".join(f"{k}: {v}" for k, v in fields.items())
    verdict = "Approved to proceed." if cleared else "Substantial revision required."
    return f"{SIMULATED_REVIEW_LABEL}\n\n{header}\n\n# Review\n\n{verdict}\n"


def build_world(root: Path) -> Path:
    write(root, f"records/worlds/{CODE}.yaml", f"kind: formation\nworld_id: fx-world\ncensus_id: {SLUG}\nsafety_adjacent: false\n")
    write(root, "cic-website/data/world-census.json", json.dumps({"movements": [{"id": SLUG, "status": "Possible Future World"}]}))
    write(root, f"cic/texts/{TEXT_FILE}", TEXT)
    write(root, "cic/texts/REGISTRY.yaml", f"- filename: {TEXT_FILE}\n  supplied_by: Mark\n  date_added: '2026-09-01'\n")
    write(
        root,
        f"cic/corpus-map/{SLUG}.yaml",
        f"atlas_id: {SLUG}\nworks:\n- row_id: {SLUG}--test-volume-letters\n  work: Test Volume Letters\n  author: test_author\n  locus: div1\n  role: tradition\n  confidence: assigned\n  source_file: {TEXT_FILE}\n",
    )
    base = f"Build/worlds/{CODE}"
    write(root, f"{base}/Step0_Movement_Scope_Confirmation.md", "# Step 0\n\nThe movement's status in world-census.json was checked.\n")
    write(root, f"{base}/Doc_01_World_Identification.md", f'# Doc 1\n\nThe letter says "{QUOTE}" in `cic/texts/{TEXT_FILE}`.\n')
    write(root, f"{base}/Doc_02_Source_Ecology.md", "# Doc 2\n\nSee the Source Registry.\n")
    write(root, f"{base}/Source_Registry.md", f"# Source Registry\n\n| row | work | file |\n|---|---|---|\n| 1 | Test Volume Letters | `{TEXT_FILE}` |\n")
    for name in ("Step0_Review_Round1.md", "Doc_01_Review_Round1.md", "Doc_02_Review_Round1.md"):
        write(root, f"{base}/{name}", review_text())
    write(root, f"{base}/Open_Gaps_Tracking.md", "# Open Gaps\n\n- 2026-09-01: the dating of the letter is disputed among editors.\n")
    write(root, "Build/worlds/_cross-world/NEEDS-RULING.md", "# Needs ruling\n\n- Whether the northern collection belongs to a sibling world.\n")
    write(
        root,
        f"Build/worlds/_cross-world/dossiers/{SLUG}_Source_Readiness_Dossier.md",
        "# Source Readiness Dossier\n\n"
        f"**Atlas ID:** I.99\n**Corpus-map slug:** {SLUG}\n**Time window:** 300-400\n\n"
        "## 1. Already assigned\n\n| work | author | role | confidence | approx. scale | source file |\n|---|---|---|---|---|---|\n"
        f"| Test Volume Letters | test_author | tradition | assigned | small | {TEXT_FILE} |\n\n"
        "## 2. Cross-link opportunities\n\n- —\n\n## 3. Verified acquisition leads\n\n| title | author |\n|---|---|\n| — | — |\n\n"
        "## 4. Checked and closed\n\n| candidate | why |\n|---|---|\n| — | — |\n\n"
        "## 5. Open cross-world questions\n\n- Whether the northern collection belongs to a sibling world.\n",
    )
    write(
        root,
        f"{base}/build/{CODE}_Handoff_Manifest.md",
        "# Handoff manifest: world `fx`\n\n| Field | Entry |\n|---|---|\n| World code | fx |\n| Handoff date | 2026-09-29 |\n\n"
        "## Paths\n\n| Item | Path |\n|---|---|\n"
        f"| Step 0 Movement-Scope Confirmation | `{base}/Step0_Movement_Scope_Confirmation.md` |\n"
        f"| Step 1 World Identification | `{base}/Doc_01_World_Identification.md` |\n"
        f"| Step 2 Source Ecology | `{base}/Doc_02_Source_Ecology.md` |\n"
        f"| Source Readiness Dossier | `Build/worlds/_cross-world/dossiers/{SLUG}_Source_Readiness_Dossier.md` |\n"
        f"| Corpus-map assignments | `cic/corpus-map/{SLUG}.yaml` |\n"
        f"| Open gaps | `{base}/Open_Gaps_Tracking.md` |\n\n"
        "## Review round per step\n\n| Step | Review round it cleared in | Review file | Date |\n|---|---|---|---|\n"
        "| Step 0 | 1 | Step0_Review_Round1.md | 2026-09-20 |\n"
        "| Step 1 | 1 | Doc_01_Review_Round1.md | 2026-09-21 |\n"
        "| Step 2 | 1 | Doc_02_Review_Round1.md | 2026-09-22 |\n",
    )
    return root


def quiet_deps(root: Path) -> Deps:
    return Deps(
        root=root,
        holdings=lambda code: [],
        corpus_merge_check=lambda r: (True, ""),
        corpus_index_build=lambda r: (True, ""),
        commentary=lambda r, paths: [],
    )
