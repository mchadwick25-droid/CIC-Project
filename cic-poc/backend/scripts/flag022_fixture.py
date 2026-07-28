"""FLAG-022 fix fixture (deterministic, no LLM) - the term-must-appear
precondition on the modern-term bridge (Mark's fix mandate, 2026-07-28).

said -> present / unsaid -> absent, across the WHOLE dictionary, plus the
two live repro cases: the S6.2 battery's sola-scriptura misfire message
(must be suppressed) and the TRR's explicitly-said original-sin message
(must pass through). Exits nonzero on any failure.
"""
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from app.graph.modern_term_bridge import (  # noqa: E402
    _load_definitions, _term_present_in_message)


def main() -> int:
    defs = _load_definitions()
    unsaid = ("But she says the texts are full of contradictions. Didn't "
              "that bother your teachers?")
    fails = []
    for tid, d in defs.items():
        forms = d.get("display_terms") or [tid]
        said = f"What do you think about {forms[0]}?"
        if not _term_present_in_message(d, tid, said):
            fails.append(("said-missed", tid))
        if _term_present_in_message(d, tid, unsaid):
            fails.append(("unsaid-fired", tid))
    if _term_present_in_message(defs["sola-scriptura"], "sola-scriptura", unsaid):
        fails.append(("battery-repro", "sola-scriptura"))
    trr_msg = ("What about original sin - Augustine settled that question "
               "in your own lifetime, didn't he?")
    if not _term_present_in_message(defs["original-sin-developed"],
                                    "original-sin-developed", trr_msg):
        fails.append(("trr-positive", "original-sin-developed"))
    n = 2 * len(defs) + 2
    print(f"FLAG-022 fixture: {n} checks, {len(fails)} failures")
    for f in fails:
        print("  FAIL:", f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
