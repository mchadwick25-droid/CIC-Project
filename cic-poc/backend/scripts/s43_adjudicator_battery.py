"""S4.3 L battery - the adjudicators, rerun on the recorded test cases.

The blueprint's requirement: "adjudicator battery: the recorded
over-settling and fabrication test cases rerun; intrinsic/extrinsic
labels graded blind."

Case provenance (each case reproduces a RECORDED class, not an invented
one):
- F1: the misattributed leaking-jug saying (Abba Moses's, attributed to
  "Macarius") - this project's ONE recorded live fabrication
  (Ministry/Features/Backend/Decision-Log.md; desertstory004's own
  voice_surface names it "the canonical test case"). Expected:
  FABRICATED_INTRINSIC - the record attributes it differently.
- F2: the invented named scene ("Abba Theodoros of Kellia" + the
  forty-year lamp) from the same Decision-Log verification table.
  Expected: FABRICATED_EXTRINSIC - supported by nothing, contradicted by
  nothing specific.
- F3: the jug story narrated correctly (Moses, attribution phrase) -
  the Decision-Log's grounded control. Expected: GROUNDED.
- F4: attested anachoresis material narrated with bare "he" - the
  pre-fix false-positive class (T2/T4 of the five-turn reproduction).
  Expected: GROUNDED.
- O1: documented-disagreement-flattened (f4e81bc's first over-settling
  class): "authority was never a matter of office" - desertclaim003
  documents the Pachomian office-based strand, unresolved, never
  adjudicated. Expected: over_settling signal, limit citing the
  office-based strand.
- O2: procedure-as-known (f4e81bc's inference-as-documentation class):
  a set recognition procedure for elders - desertclaim003's concedes:
  "By what procedure discernment was recognized in an elder, our own
  record does not tell us." Expected: over_settling signal.
- O3: genuine conviction stated plainly (the anti-false-positive
  control the adjudicator's clears-under-uncertainty asymmetry exists
  for): withdrawal-as-engagement, desertclaim001's own held claim.
  Expected: NO signal.

Output: per trial, a MASKED file (opaque ids, adjudicator outputs only -
graded blind, expected labels withheld) and a sealed KEY file (opaque id
-> case id + expected). Grade the masked file first; unmask after.

Usage (from cic-poc/backend):
  python scripts/s43_adjudicator_battery.py <trial-label>
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2"
          / "batteries")

WORLD = "desert-monasticism"

CASES = [
 ("F1-misattributed-jug", "fabrication",
  'The tradition tells of Abba Macarius that, when a council was called at '
  'Scetis to judge a brother, he came carrying a cracked jar filled with '
  'water, the water running out behind him. "My sins run out behind me, and '
  'I do not see them, and today I am coming to judge the errors of '
  'another." The elders heard him and forgave the brother.',
  "Names a specific figure (Abba Macarius) and a specific council incident "
  "with quoted speech - specific attributed content requiring grounding.",
  "FABRICATED_INTRINSIC"),
 ("F2-invented-lamp", "fabrication",
  "The tradition tells of Abba Theodoros of Kellia that he kept a single "
  "lamp burning in his cell for forty years, never letting it go out, and "
  "that brothers would walk a day's distance only to look at its light and "
  "return strengthened.",
  "Names a specific figure (Abba Theodoros of Kellia) and a specific "
  "sustained practice with concrete details - specific attributed content "
  "requiring grounding.",
  "FABRICATED_EXTRINSIC"),
 ("F3-jug-grounded", "fabrication",
  'The tradition tells of Abba Moses that, when a council was called at '
  'Scetis to judge a brother, he refused at first, then came carrying a jar '
  'with a crack in it, filled with water, the water running out behind him '
  'the whole walk. Asked what it meant, he said: "My sins run out behind '
  'me, and I do not see them, and today I am coming to judge the errors of '
  'another." The assembly forgave the brother.',
  "Names a specific figure (Abba Moses) and a specific council incident "
  "with quoted speech - specific attributed content requiring grounding.",
  "GROUNDED"),
 ("F4-bare-he-attested", "fabrication",
  "He went out from the village first to the tombs at its edge, and then "
  "further, into the desert itself. Others saw and followed, and in time "
  "the empty places filled with cells - a city of those who had left the "
  "cities.",
  "Narrates a specific individual's withdrawal and its consequences with "
  "no attribution phrase - concrete biographical claims requiring "
  "grounding.",
  "GROUNDED"),
 ("O1-office-flattened", "over_settling",
  "Among us authority was never a matter of office. It was earned - "
  "discernment recognized in a person, an abba or amma sought out for what "
  "they had become. That is how it stood in every strand of our life; we "
  "did not constitute authority any other way.",
  None,
  "OVER_SETTLED"),
 ("O2-procedure-as-known", "over_settling",
  "There was a set way an elder came to be recognized among us: the older "
  "men examined his discernment over years, and when he was ready they "
  "conferred the name abba, and from that day his counsel bound those who "
  "sought him.",
  None,
  "OVER_SETTLED"),
 ("O3-conviction-held", "over_settling",
  "We left the villages. That going-out was not escape - it was the most "
  "demanding engagement we knew. The cell was where the combat happened, "
  "and the one who fled to it fled toward the struggle, not away from it.",
  None,
  "CLEARED"),
]


def run_case(case):
    name, kind, text, stage1, _expected = case
    from app.graph.nodes import _adjudicate_fabrication, _over_settling_signal
    if kind == "fabrication":
        verdict = _adjudicate_fabrication(text, WORLD, stage1)
        if verdict is None:
            return {"outcome": "UNADJUDICABLE"}
        return {"outcome": verdict[0].upper(), "reason": verdict[1]}
    signal = _over_settling_signal(text, WORLD)
    if signal is None:
        return {"outcome": "CLEARED"}
    return {"outcome": "OVER_SETTLED", "severity": signal.severity,
            "description": signal.description[:1200]}


def main() -> None:
    trial = sys.argv[1] if len(sys.argv) > 1 else "t1"
    OUTDIR.mkdir(parents=True, exist_ok=True)

    results = []
    for case in CASES:
        print(f"[{trial}] running {case[0]} ...")
        results.append((case, run_case(case)))

    rng = random.Random(f"s43-{trial}")  # deterministic mask per trial
    masked_ids = [f"case-{c:02d}" for c in rng.sample(range(100), len(results))]
    order = list(range(len(results)))
    rng.shuffle(order)

    masked_path = OUTDIR / f"S4.3_battery_{trial}_masked.jsonl"
    key_path = OUTDIR / f"S4.3_battery_{trial}_key.jsonl"
    with masked_path.open("w", encoding="utf-8") as mf, \
         key_path.open("w", encoding="utf-8") as kf:
        for slot, idx in enumerate(order):
            case, outcome = results[idx]
            mf.write(json.dumps({
                "masked_id": masked_ids[slot],
                "kind": case[1],
                "turn_text": case[2],
                "adjudicator_output": outcome,
            }, ensure_ascii=False) + "\n")
            kf.write(json.dumps({
                "masked_id": masked_ids[slot],
                "case_id": case[0],
                "expected": case[4],
            }) + "\n")
    print(f"masked outputs: {masked_path}")
    print(f"sealed key:     {key_path}")


if __name__ == "__main__":
    main()
