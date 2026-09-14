"""S5.4 G gate - Level 2 readability floor + rights-gating fixtures.

Two parts, per the blueprint's S5.4 checkpoint definition:

  A. readability on every Level 2 render (floor from wrs/parameters.yaml,
     computed by S1.3's instrument - this script only RUNS it, per the
     gate-integrity rule; wrs/gates/ is untouched by S5.4);
  B. rights-gating fixtures: an in-copyright text must not render
     publicly. Synthetic fixtures prove both directions of the gate
     (permitted renders / unset-or-denied withholds / embedded text
     redacts), then the REAL generated views are swept for leaks and
     byte-checked against regeneration.

Deterministic; run twice and byte-compare the report (the harness for
that is simply running this file twice).

Usage (from cic-poc/backend):
  python ../../Ministry/Technology/Pass2/gates/S5.4_levels_rights_gate.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

GATES_DIR = Path(__file__).resolve().parent
REPO_ROOT = GATES_DIR.parents[3]
BACKEND = REPO_ROOT / "cic-poc" / "backend"
for p in (str(BACKEND), str(BACKEND / "wrs" / "views")):
    if p not in sys.path:
        sys.path.insert(0, p)

from plain_explanation import render_all  # noqa: E402
from repository import (  # noqa: E402
    display_gate, gated_quote_strings, WITHHELD_MARKER, DATA_DIR)

lines: list[str] = []


def emit(s: str = "") -> None:
    lines.append(s)


# ---------------------------------------------------------------- part A

def part_a_readability() -> bool:
    emit("## Part A - readability floor on every Level 2 render")
    emit()
    renders = render_all()
    failures = 0
    for r in renders:
        chk = r["readability"]
        verdict = "PASS" if chk["ok"] else "FAIL (" + "; ".join(chk["violations"]) + ")"
        if not chk["ok"]:
            failures += 1
        emit(f"- {r['record_id']}: FK {chk['fk_grade']:.2f} / FRE {chk['fre']:.2f} - {verdict}")
    emit()
    emit(f"Result: {len(renders) - failures}/{len(renders)} renders at the floor.")
    if failures:
        emit("Part A verdict: **RED** - see FLAG-011 (the floor is "
             "unreachable by structure-only renders of the fields as "
             "authored; decision with Mark/review round).")
    else:
        emit("Part A verdict: GREEN.")
    return failures == 0


# ---------------------------------------------------------------- part B

FIXTURE_SOURCES = {
    "srcFIXpermitted": {"id": "srcFIXpermitted", "record_type": "source",
                        "display_permitted": True,
                        "work_title": "Fixture translation, permission stated"},
    "srcFIXdenied": {"id": "srcFIXdenied", "record_type": "source",
                     "display_permitted": False,
                     "work_title": "Fixture translation, permission denied"},
    "srcFIXunset": {"id": "srcFIXunset", "record_type": "source",
                    "work_title": "Fixture translation, rights unstated"},
}

PERMITTED_TEXT = "The permitted rendering of the fixture saying."
DENIED_TEXT = "The denied rendering of the fixture saying."
UNSET_TEXT = "The rights-unstated rendering of the fixture saying."
ORPHAN_TEXT = "The provenance-less rendering of the fixture saying."

FIXTURE_QUOTES = {
    "fixq-permitted": {"id": "fixq-permitted", "record_type": "quote",
                       "text_translation": PERMITTED_TEXT,
                       "translation_used": "srcFIXpermitted"},
    "fixq-denied": {"id": "fixq-denied", "record_type": "quote",
                    "text_translation": DENIED_TEXT,
                    "translation_used": "srcFIXdenied"},
    "fixq-unset": {"id": "fixq-unset", "record_type": "quote",
                   "text_translation": UNSET_TEXT,
                   "translation_used": "srcFIXunset"},
    "fixq-orphan": {"id": "fixq-orphan", "record_type": "quote",
                    "text_translation": ORPHAN_TEXT},
}


def part_b_fixtures() -> bool:
    emit("## Part B - rights-gating fixtures (fail-closed both directions)")
    emit()
    ok = True

    def case(name: str, passed: bool, detail: str) -> None:
        nonlocal ok
        ok = ok and passed
        emit(f"- {name}: {'PASS' if passed else 'FAIL'} - {detail}")

    gated = gated_quote_strings(FIXTURE_QUOTES, FIXTURE_SOURCES)

    pub, rights = display_gate(FIXTURE_QUOTES["fixq-permitted"],
                               FIXTURE_SOURCES, gated)
    case("permitted quote renders",
         pub["text_translation"] == PERMITTED_TEXT and not rights["gated_fields"],
         f"display_permitted: true -> text present (basis: {rights['basis']})")

    pub, rights = display_gate(FIXTURE_QUOTES["fixq-denied"],
                               FIXTURE_SOURCES, gated)
    case("denied quote withheld",
         pub["text_translation"] == WITHHELD_MARKER
         and "text_translation" in rights["gated_fields"],
         "display_permitted: false -> marker substituted")

    pub, rights = display_gate(FIXTURE_QUOTES["fixq-unset"],
                               FIXTURE_SOURCES, gated)
    case("rights-unstated quote withheld (fail-closed)",
         pub["text_translation"] == WITHHELD_MARKER,
         "display_permitted unset -> denied, never assumed")

    pub, rights = display_gate(FIXTURE_QUOTES["fixq-orphan"],
                               FIXTURE_SOURCES, gated)
    case("provenance-less quote withheld",
         pub["text_translation"] == WITHHELD_MARKER,
         "no translation_used row -> provenance unestablished -> denied")

    story_embedding_denied = {
        "id": "fixstory-embeds-denied", "record_type": "story",
        "text": f"A teller said: \"{DENIED_TEXT}\" and the room went quiet."}
    pub, rights = display_gate(story_embedding_denied, FIXTURE_SOURCES, gated)
    case("embedded denied text redacted in a story",
         DENIED_TEXT not in json.dumps(pub) and WITHHELD_MARKER in pub["text"],
         "the rule follows the text wherever it appears (desertstory004 class)")

    story_embedding_permitted = {
        "id": "fixstory-embeds-permitted", "record_type": "story",
        "text": f"A teller said: \"{PERMITTED_TEXT}\" and the room went quiet."}
    pub, rights = display_gate(story_embedding_permitted, FIXTURE_SOURCES, gated)
    case("embedded permitted text NOT redacted",
         PERMITTED_TEXT in pub["text"] and not rights["gated_fields"],
         "permission stated -> embedding renders")

    return ok


def part_b_real_views() -> bool:
    emit()
    emit("## Part B (continued) - the real generated views")
    emit()
    ok = True

    def case(name: str, passed: bool, detail: str) -> None:
        nonlocal ok
        ok = ok and passed
        emit(f"- {name}: {'PASS' if passed else 'FAIL'} - {detail}")

    from chunk_views import load_records
    quotes = load_records("quote")
    real_gated = gated_quote_strings(quotes, load_records("source"))
    # independent recomputation of the expected count: every populated
    # text field on every quote record (no source states display
    # permission today - FLAG-013 - so every one must be gated)
    expected = sum(1 for q in quotes.values()
                   for f in ("text_translation", "text_original")
                   if isinstance(q.get(f), str) and q[f].strip())
    case("real rights state", len(real_gated) == expected,
         f"{len(real_gated)}/{expected} populated quote text fields gated "
         f"across {len(quotes)} quotes (desertq002 carries text_original "
         "too; no source states display_permitted, FLAG-013)")

    repo_text = (DATA_DIR / "repository.json").read_text(encoding="utf-8")
    leaks = [g[:40] for g in real_gated if g in repo_text]
    case("whole-file leak sweep of repository.json", not leaks,
         "no gated string appears anywhere in the deployed view"
         + (f" (LEAKED: {leaks})" if leaks else ""))

    repo = json.loads(repo_text)
    quote_entries = [e for e in repo["records"] if e["record_type"] == "quote"]
    case("every real quote entry withheld",
         all(e["rights"]["gated_fields"] for e in quote_entries),
         f"{len(quote_entries)}/3 carry gated_fields")

    s4 = next(e for e in repo["records"] if e["id"] == "desertstory004")
    case("desertstory004 embedded rendering redacted",
         "embedded-quote-text" in s4["rights"]["gated_fields"],
         "the live case the leak check caught, held")

    searchable = " ".join(e["search_text"] for e in repo["records"])
    case("search index built after redaction",
         not any(g.lower() in searchable for g in real_gated),
         "withheld text unfindable by substring search")

    check = subprocess.run(
        [sys.executable, str(BACKEND / "wrs" / "views" / "repository.py"),
         "--check"], capture_output=True, text=True, cwd=str(BACKEND))
    case("deployed views current (--check byte-match)",
         check.returncode == 0,
         (check.stdout or check.stderr).strip().splitlines()[-1])

    return ok


def main() -> int:
    emit("# S5.4 G gate run - Level 2 readability + rights gating")
    emit()
    a = part_a_readability()
    emit()
    b1 = part_b_fixtures()
    b2 = part_b_real_views()
    emit()
    emit(f"Part A (readability): {'GREEN' if a else 'RED (FLAG-011)'}")
    emit(f"Part B (rights): {'GREEN' if (b1 and b2) else 'RED'}")
    report = "\n".join(lines) + "\n"
    sys.stdout.write(report)
    return 0 if (a and b1 and b2) else 1


if __name__ == "__main__":
    raise SystemExit(main())
