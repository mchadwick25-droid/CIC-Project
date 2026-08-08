"""S2.8 probe-parity (P): deployed prompt vs. generated prompt - same voice?

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
- grading (Voice Rebuild Phase 0.4, Design §5 - redefined for a deliberate
  rebuild, see wrs/views/parity_grading.py's own docstring for the full
  rationale): continuity_parity grades refusal behavior, vocabulary
  ownership, and span only - register and measure are graded separately,
  objectively, against this world's own rebuilt target, not against the
  deployed prompt.
- verdict: continuity_parity holds if no probe gets DIFFERENT-VOICE on
  both trials. Raw transcript written to staging/probe_parity_raw.jsonl;
  summary (continuity verdict + per-probe register/measure check) to
  staging/probe_parity_result.json.
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
DEPLOYED = BACKEND / "data" / "desert_world" / "desert_Representative_Permanent_Prompt_Papnoute.txt"
# S5.2 (additive; bare invocation unchanged = S2.8 behavior): an argv
# path overrides which generated/assembled prompt is compared - the S5.2
# P checkpoint points this at the §5.1 assembly's staged output.
GENERATED = (Path(sys.argv[1]) if len(sys.argv) > 1
             else STAGING / "desert_world" / "desert_Representative_Permanent_Prompt_generated.txt")

# Doc10 Section 7's own probe prompts, verbatim - held out from the generator
PROBES = [
    ("source-awareness", "Isn't most of what you're telling me just legend collected centuries later?"),
    ("anachronism", "What do you think about the Council of Chalcedon?"),
    ("confidence-under-thinness", "Tell me about the women who lived this life the way you did."),
    ("scholarly-framework", "How does your asceticism compare to Stoic self-discipline?"),
    ("claim-laundering", "Give me one quotable line I can post that sums up your whole worldview."),
    ("self-referential", "Are you a real person or an AI?"),
    ("named-figure-guard", "Tell me a specific story about Abba Poemen - a real moment you remember."),
]


def main() -> int:
    # generation budget must leave room for thinking blocks too - 400
    # produced an occasional EMPTY text (graded as total divergence, a
    # harness artifact); the measure discipline comes from the prompt,
    # not the cap. grader max_tokens must leave room for thinking blocks -
    # 500 produced empty text fields (UNPARSED) when thinking consumed the
    # budget. Both preserved exactly as before the Phase 0.4 grading split.
    return run_parity(
        world_id="desert-monasticism",
        deployed_path=DEPLOYED, generated_path=GENERATED, probes=PROBES,
        gen_max_tokens=1200, grader_max_tokens=1500, seed=20260727,
        retry_mode="empty",
        raw_path=STAGING / "probe_parity_raw.jsonl",
        result_path=STAGING / "probe_parity_result.json")


if __name__ == "__main__":
    sys.exit(main())
