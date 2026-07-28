"""CO-P2-16 (Mark, 2026-07-28) - story.confidence_line: schema home +
verbatim backfill for the deployed story chunks' Confidence front-matter
line.

The S2.8 render parity found the line had no record home (10 defects);
the decision check found it is LIVE metadata - the story retriever
injects "Confidence: ..." into the generation context on every story
retrieval (app/rag/story_retriever.py:237), so dropping it at swap would
silently change runtime behavior (NOT the CO-P2-09 Tags case, which was
verified dead before retiring).

Backfill is mechanical: the Confidence value parsed from each deployed
chunk's fenced front matter, stored verbatim. Idempotent; asserts all 10
stories receive a value; fence-asserting reader.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from s62_alx_source_rows import emit_record
from s62_alx_s25 import read_record

STORY_DIR = BACKEND / "wrs" / "records" / "alexandria_world" / "story"
DEPLOYED = BACKEND / "data" / "alexandria_world" / "story_chunks"

BODY_NOTE = ("\n\nCO-P2-16 (2026-07-28): confidence_line backfilled verbatim "
             "from the deployed chunk's Confidence front-matter line (live "
             "retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.")


def main():
    lines = {}
    for p in DEPLOYED.glob("*.md"):
        rid = p.stem.split("_")[0]
        m = re.search(r"^Confidence:\s*(.+)$", p.read_text(encoding="utf-8"),
                      re.M)
        assert m, f"{p.name}: no Confidence line in deployed chunk"
        lines[rid] = m.group(1).strip()
    assert len(lines) == 10, lines

    changed = 0
    for rid, val in sorted(lines.items()):
        path = STORY_DIR / f"{rid}.md"
        rec, body = read_record(path)
        if rec.get("confidence_line") == val:
            continue  # idempotent re-run
        assert "confidence_line" not in rec, f"{rid}: unexpected existing value"
        rec["confidence_line"] = val
        if "CO-P2-16" not in body:
            body += BODY_NOTE
        emit_record(rec, body, path)
        changed += 1
    print(f"CO-P2-16: confidence_line backfilled on {len(lines)} stories "
          f"({changed} written this run)")


if __name__ == "__main__":
    main()
