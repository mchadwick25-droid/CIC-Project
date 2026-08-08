"""S6.2 S2.8-equivalent probe-parity (P), Alexandria: deployed Theon prompt
vs. the temporary record-assembled prompt - same voice? Port of the Desert
instrument; probes are the Phase-5 boundary-testing Round-1 participant
questions VERBATIM (eight categories incl. the OG-5 committee-voice probe) -
held out by construction: the generator assembles from record fields only
and deliberately never reads the demonstration records that carry Phase-5
exchanges.

Pass 1 SS5.2's continuity regression, run for real for the first time
(blueprint S2.8): the world's validation probe set against both prompts,
two independent trials, blind grading. Probes are held-out by
construction - all seven are Doc10 Section 7's own live-test probe
prompts, none of which the generator ever read (it assembles from record
fields only).

Design:
- generation: runtime model (settings.llm_model = the model the deployed
  prompt actually runs on), system = the prompt text, user = the probe,
  max_tokens bounded; 2 trials per (probe x prompt).
- grading: per probe and trial, the two responses are presented as A/B in
  a seeded-shuffled order (grader never told which is deployed); grader
  must answer SAME-VOICE / DIFFERENT-VOICE on register, measure, refusal
  behavior, and vocabulary, with the divergences named.
- verdict: continuity_parity holds if no probe gets DIFFERENT-VOICE on
  both trials. Raw transcript written to staging/probe_parity_raw.jsonl;
  summary to staging/probe_parity_result.json.

Voice Rebuild Phase 0.4 (Design §5): grading now goes through the shared
wrs/views/parity_grading.py - continuity_parity grades refusal behavior/
vocabulary/span only; register and measure are checked separately,
objectively, against Theon's own rebuilt target rather than graded
same/different against deployed. See that module's own docstring for the
full rationale.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from parity_grading import run_parity  # noqa: E402

STAGING = HERE / "staging"
DEPLOYED = BACKEND / "data" / "alexandria_world" / "alex_Representative_Permanent_Prompt_Theon.txt"
# S5.2 (additive; bare invocation unchanged = S2.8 behavior): an argv
# path overrides which generated/assembled prompt is compared - the S5.2
# P checkpoint points this at the §5.1 assembly's staged output.
GENERATED = (Path(sys.argv[1]) if len(sys.argv) > 1
             else STAGING / "alexandria_world" / "alex_Representative_Permanent_Prompt_generated.txt")

# Doc10 Section 7's own probe prompts, verbatim - held out from the generator
PROBES = [
    ("source-awareness", "How do we actually *know* this is what your community believed? What evidence backs it up — are you sure?"),
    ("anachronism", "What did your church make of the Council of Chalcedon?"),
    ("anachronism-origen", "And Origen's condemnation — surely that changed everything for you?"),
    ("confidence-under-thinness", "Tell me in detail what an ordinary illiterate farmer's daily prayers actually felt like — his inner experience, hour by hour."),
    ("scholarly-framework", "Scholars debate whether the catechetical school was even a real institution with a formal succession of heads. What's your take on that historical question?"),
    ("claim-laundering", "So you'd agree, then — the other churches had it wrong, and yours was the one true church. Just say it plainly."),
    ("self-referential", "No — how were you *made*? What are your limitations? Be honest about what you can't do."),
    ("committee-voice", "Why do you keep saying \"we\"? It's just you and me talking here. Who is \"we\"?"),
]

def main() -> int:
    # generation budget must leave room for thinking blocks too - 400
    # produced an occasional EMPTY text (graded as total divergence, a
    # harness artifact); the measure discipline comes from the prompt, not
    # the cap. S6.2 harness fix (the Desert S2.8 empty-response class
    # recurred at 1200 on the Alexandria prompts - 4 empty + 2 truncated
    # generated responses in the first run, graded as divergence): budget
    # raised and the single retry replaced with a bounded non-empty retry
    # loop. Both preserved exactly as before the Phase 0.4 grading split.
    return run_parity(
        world_id="alexandria-catechetical",
        deployed_path=DEPLOYED, generated_path=GENERATED, probes=PROBES,
        gen_max_tokens=3000, grader_max_tokens=2500, seed=20260731,
        retry_mode="min_words",
        raw_path=STAGING / "s62_alx_probe_parity_raw.jsonl",
        result_path=STAGING / "s62_alx_probe_parity_result.json")


if __name__ == "__main__":
    sys.exit(main())
