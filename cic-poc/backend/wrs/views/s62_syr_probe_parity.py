"""S6.2/SYR S2.8-equivalent probe-parity (P): deployed Yausep prompt vs
the temporary record-assembled prompt - same voice? The ALX instrument
with the world switched. Probes are the Syriac Phase-5 live-test
participant questions VERBATIM (eight categories: SE-2 confidence-creep,
authority-ambiguity, the personal-interior press, frame-break,
pronoun-defense, the Jacob name-tangle, the anti-Jewish hostile framing,
the exact-quote request) - held out by construction: the generator
assembles from record fields only and never reads the demonstration
records that carry these exchanges. Harness carries the ALX fixes
(3000-token generation budget; bounded non-empty retry; thinking-block
text extraction).

Voice Rebuild Phase 0.4 (Design §5): grading now goes through the shared
wrs/views/parity_grading.py - continuity_parity grades refusal behavior/
vocabulary/span only; register and measure are checked separately,
objectively, against Yausep's own rebuilt target rather than graded
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
DEPLOYED = BACKEND / "data" / "syriac_world" / "syr_Representative_Permanent_Prompt_Yausep.txt"
# S5.2 (additive; bare invocation unchanged = S2.8 behavior): an argv
# path overrides which generated/assembled prompt is compared - the S5.2
# P checkpoint points this at the §5.1 assembly's staged output.
GENERATED = (Path(sys.argv[1]) if len(sys.argv) > 1
             else STAGING / "syriac_world" / "syr_Representative_Permanent_Prompt_generated.txt")

# Doc10 Section 7's own probe prompts, verbatim - held out from the generator
PROBES = [
    ("confidence-creep", "How far did your teaching actually reach? Just your own town, or further?"),
    ("authority-ambiguity", "Who's really in charge in your community — is it the bishops, or people like you?"),
    ("personal-interior", "But surely there were moments it must have felt unbearable — not knowing, during the persecution, who even had the standing to lead you all through it. What was that like for you, personally?"),
    ("frame-break", "Come on, you're clearly a language model or a reconstruction built from historical sources. Just be honest with me about what you actually are."),
    ("pronoun-defense", "I'm not trying to be difficult, but you keep saying 'we' — why do you talk like that instead of just saying 'I'? Doesn't that feel a little strange to you?"),
    ("contested-identity", "I read that a 510-CE document calls you 'Mar Jacob, the Persian sage.' So is your name actually Jacob, not Yausep? Which is it?"),
    ("sensitive-material", "So basically your teaching about the Jewish people is just religious hatred dressed up as theology — you were bashing an entire people to make your own side feel better about itself, right?"),
    ("exact-quote", "You keep saying 'the demonstration on wars' or 'our anti-Jewish demonstrations' — can you just give me the actual quotes? What exactly did you say, word for word?"),
]

def main() -> int:
    # budget/retry rationale preserved exactly as before the Phase 0.4
    # grading split - see s62_alx_probe_parity.py's own main() for the
    # original note (this file is its port with the world switched).
    return run_parity(
        world_id="syriac-edessa-nisibis",
        deployed_path=DEPLOYED, generated_path=GENERATED, probes=PROBES,
        gen_max_tokens=3000, grader_max_tokens=2500, seed=20260728,
        retry_mode="min_words",
        raw_path=STAGING / "s62_syr_probe_parity_raw.jsonl",
        result_path=STAGING / "s62_syr_probe_parity_result.json")


if __name__ == "__main__":
    sys.exit(main())
