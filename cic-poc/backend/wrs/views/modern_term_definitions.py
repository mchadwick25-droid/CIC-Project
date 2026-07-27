"""S4.5 - the modern-term dictionary as a GENERATED VIEW.

Pass 1 §3.9's rule applied to the bridge: the modern_term records
(wrs/records/facilitator/modern_term/, §3.11) are the source of truth;
data/modern_term_bridge/definitions.json - the file the runtime reads -
is generated from them, never hand-edited again. The view is an
ENRICHED superset of the historical file: every field today's bridge
reads is carried (including the two FLAG-009-parked fields, read from
each record's body parking), plus §3.11's two additions
(distinguishing_claim, native_subject_map) the rebuilt classifier and
per-world answering consume.

Deterministic: same records -> byte-identical JSON (sorted by record id,
2-space indent, trailing newline).

Usage (from cic-poc/backend):
  python wrs/views/modern_term_definitions.py           # regenerate
  python wrs/views/modern_term_definitions.py --check   # exit 1 if stale
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

BACKEND = Path(__file__).resolve().parents[2]
RECORDS = BACKEND / "wrs" / "records" / "facilitator" / "modern_term"
OUT = BACKEND / "data" / "modern_term_bridge" / "definitions.json"

_COMMENT = (
    "GENERATED VIEW (S4.5) - do not hand-edit. Source of truth: "
    "wrs/records/facilitator/modern_term/ (Pass 1 SS3.11; regenerate with "
    "wrs/views/modern_term_definitions.py). World-AGNOSTIC modern-term "
    "dictionary for the anachronism bridge. The Facilitator SPEAKS "
    "modern_sense; the Representative is handed only underlying_subject "
    "(term-free) - or, per SS6.6, answers the term natively when the term "
    "is inside its own world's window. Whether the bridge fires is derived "
    "per seated world: origin_year vs world_core.time_window.end_year "
    "(migrated worlds) or the manifest period's parsed end year "
    "(unmigrated - compatibility classification). period_originated / "
    "contested_today are FLAG-009-parked fields read from the records' "
    "body parking."
)


def _parse_record(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    front = yaml.safe_load(parts[1])
    body = parts[2] if len(parts) > 2 else ""
    parked: dict = {}
    for line in body.splitlines():
        if line.startswith("period_originated:"):
            parked["period_originated"] = line.split(":", 1)[1].strip()
        elif line.startswith("contested_today:"):
            parked["contested_today"] = json.loads(line.split(":", 1)[1].strip())
    return {
        "term_id": front["term"],
        "display_terms": front["display_terms"],
        "modern_sense": front["modern_sense"],
        "period_originated": parked.get("period_originated", "a later period"),
        "origin_year": front["origin_year"],
        "contested_today": parked.get("contested_today", False),
        "underlying_subject": front["underlying_subject"],
        "distinguishing_claim": front["distinguishing_claim"],
        "native_subject_map": front.get("native_subject_map") or {},
        "_record_id": front["id"],
    }


def render() -> str:
    terms = [_parse_record(p) for p in sorted(RECORDS.glob("*.md"))]
    doc = {"_comment": _COMMENT, "terms": terms}
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    rendered = render()
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != rendered:
            print("STALE: definitions.json does not match the records")
            return 1
        print("definitions.json is current with the records")
        return 0
    OUT.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({len(json.loads(rendered)['terms'])} terms)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
