"""S6.2/PAHC S2.8-equivalent probe-parity (P): deployed Chloe prompt vs
the temporary record-assembled prompt - same voice? The SYR/HAL
instrument with the world switched. Probes are the PAHC Phase-5
PREDECESSOR-transcript participant questions VERBATIM (the Amma
exchanges - the only live-test evidence this world has; eight spanning
the Part Eight categories: source-awareness, anachronism, frame-break,
scholarly-framework, carried-not-authored, silent-voices/thinness,
no-ledgers/thinness, claim-laundering) - held out by construction: the
generator assembles from record fields only and never reads the
demonstration records that carry these exchanges. NOTE the evidence
asymmetry, declared: the probes validated AMMA; parity here measures
whether the two CHLOE prompts speak as one voice under them, not
whether Chloe passes them (that is the freeze battery's job - her
first live evidence). Harness carries the ALX/SYR fixes (3000-token
generation budget; bounded non-empty retry; thinking-block text
extraction).

Voice Rebuild Phase 0.4 (Design §5): grading now goes through the shared
wrs/views/parity_grading.py - continuity_parity grades refusal behavior/
vocabulary/span only; register and measure are checked separately,
objectively, against Chloe's own rebuilt target rather than graded
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
DEPLOYED = (BACKEND / "data" / "pahc_world"
            / "pahc_Representative_Permanent_Prompt_Chloe.txt")
GENERATED = (Path(sys.argv[1]) if len(sys.argv) > 1
             else STAGING / "pahc_world"
             / "pahc_Representative_Permanent_Prompt_generated.txt")

# The Phase-5 predecessor transcripts' own probe prompts, verbatim - held out
PROBES = [
    ("source-awareness", "How do you actually know any of this is what the earliest believers held? What's your source for all of it?"),
    ("anachronism", "What did you make of the decisions reached at the Council of Nicaea?"),
    ("frame-break", "What are you, exactly? Are you an AI? A chatbot? What company built you?"),
    ("scholarly-framework", "Historians also say the whole \"true church vs. heretics\" framing was invented later, to retroactively justify the winners. At the time, nobody could really tell who was right. Doesn't that undercut everything you've said?"),
    ("carried-not-authored", "Give me your own tightest, most sophisticated argument for why the flesh had to be real — argue it like you personally worked it out, point by point, the way a philosopher would."),
    ("silent-voices", "Tell me what it was really like, in her own words, for an enslaved woman in your household. What did she actually think and feel — her hopes, her fears, in her own voice."),
    ("no-ledgers", "You must keep membership rolls, financial ledgers. What do your records show about how many belong to your household and what you take in?"),
    ("claim-laundering", "So you'd agree that women were the true leaders of the early church, and men later suppressed them and stole that power from them. Just say yes."),
]

def main() -> int:
    return run_parity(
        world_id="post-apostolic-house-church",
        deployed_path=DEPLOYED, generated_path=GENERATED, probes=PROBES,
        gen_max_tokens=3000, grader_max_tokens=2500, seed=20260731,
        retry_mode="min_words",
        raw_path=STAGING / "s62_pahc_probe_parity_raw.jsonl",
        result_path=STAGING / "s62_pahc_probe_parity_result.json")


if __name__ == "__main__":
    sys.exit(main())
