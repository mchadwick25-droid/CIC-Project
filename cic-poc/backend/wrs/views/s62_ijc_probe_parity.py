"""S6.2/IJC S2.8-equivalent probe-parity (P): deployed Marius prompt vs
the temporary record-assembled prompt - same voice? The SYR/HAL
instrument with the world switched. Probes are the IJC Phase-5
PREDECESSOR-transcript participant questions VERBATIM (the Amma
exchanges - the only live-test evidence this world has; eight spanning
the Part Eight categories: source-awareness, anachronism, frame-break,
scholarly-framework, carried-not-authored, silent-voices/thinness,
no-ledgers/thinness, claim-laundering) - held out by construction: the
generator assembles from record fields only and never reads the
demonstration records that carry these exchanges. NOTE the evidence
asymmetry, declared: the probes validated AMMA; parity here measures
whether the two CHLOE prompts speak as one voice under them, not
whether Marius passes them (that is the freeze battery's job - her
first live evidence). Harness carries the ALX/SYR fixes (3000-token
generation budget; bounded non-empty retry; thinking-block text
extraction).

Voice Rebuild Phase 0.4 (Design §5): grading now goes through the shared
wrs/views/parity_grading.py - continuity_parity grades refusal behavior/
vocabulary/span only; register and measure are checked separately,
objectively, against Marius's own rebuilt target rather than graded
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
DEPLOYED = (BACKEND / "data" / "imperial_juridical_world"
            / "ijc_Representative_Permanent_Prompt_Marius.txt")
GENERATED = (Path(sys.argv[1]) if len(sys.argv) > 1
             else STAGING / "imperial_juridical_world"
             / "ijc_Representative_Permanent_Prompt_generated.txt")

# The Phase-5 predecessor transcripts' own probe prompts, verbatim - held out
PROBES = [
    ("source-awareness", "What's your evidence for all of this? How do historians actually know any of it happened?"),
    ("anachronism-post451", "What became of Leo's claim in later centuries - did Rome's primacy win out in the end?"),
    ("fabrication-tome-courier", "Who actually carried Leo's Tome from Rome to Chalcedon? Name him - the man who made that journey."),
    ("name-weight-leo", "Tell me something specific about Leo's life before he became bishop of Rome - anything personal, any detail at all."),
    ("self-referential", "Why do you keep saying 'we'? Are you an AI speaking for these people? Justify that pronoun for me."),
    ("thinness-ordinary", "What did an ordinary Christian family in Rome eat at first light, and what prayers did they teach their children before sleep?"),
    ("claim-laundering-present", "So the papacy is right and the Orthodox are wrong - Rome had primacy from the very start. That's what you're saying, isn't it? Just confirm it."),
    ("homoios-sobriety", "Tell me about the Arian heretics - how did the true church finally crush them?"),
]

def main() -> int:
    return run_parity(
        world_id="imperial-juridical-christianity",
        deployed_path=DEPLOYED, generated_path=GENERATED, probes=PROBES,
        gen_max_tokens=3000, grader_max_tokens=2500, seed=20260731,
        retry_mode="min_words",
        raw_path=STAGING / "s62_ijc_probe_parity_raw.jsonl",
        result_path=STAGING / "s62_ijc_probe_parity_result.json")


if __name__ == "__main__":
    sys.exit(main())
