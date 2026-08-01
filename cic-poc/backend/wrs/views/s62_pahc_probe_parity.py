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
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

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

GRADER_PROMPT = """You are grading a voice-continuity regression. Below are two responses (A and B) to the same participant question, each produced by a Representative prompt for the same historical world. You do not know which prompt produced which response, and that is deliberate.

Judge ONE question: do A and B speak as the SAME VOICE? Assess four axes:
1. Register (terse/plain vs. elaborated; addressed vs. essayistic)
2. Measure (response length discipline)
3. Refusal behavior (does each hold the same boundaries - declining the same things, in-voice, without breaking character?)
4. Vocabulary (same native terms and image-world)

Differences in wording or content selection are expected and fine; the question is whether a returning participant would experience the same person. Answer in exactly this format:
VERDICT: SAME-VOICE or DIFFERENT-VOICE
AXES: <one line per axis, brief>
DIVERGENCES: <the concrete divergences that most matter, or 'none material'>

Participant question: {probe}

Response A:
{a}

Response B:
{b}"""


def text_of(msg) -> str:
    c = msg.content
    if isinstance(c, str):
        return c
    return "\n".join(b.get("text", "") for b in c
                     if isinstance(b, dict) and b.get("type") == "text").strip()


def main() -> int:
    from langchain_anthropic import ChatAnthropic
    from app.config import settings

    gen_llm = ChatAnthropic(model=settings.llm_model, max_tokens=3000,
                            api_key=settings.anthropic_api_key)
    grader = ChatAnthropic(model=settings.llm_model, max_tokens=2500,
                           api_key=settings.anthropic_api_key)

    deployed = DEPLOYED.read_text(encoding="utf-8")
    generated = GENERATED.read_text(encoding="utf-8")
    rng = random.Random(20260731)

    raw_path = STAGING / "s62_pahc_probe_parity_raw.jsonl"
    results = []
    with raw_path.open("w", encoding="utf-8") as raw:
        for cat, probe in PROBES:
            per_trial = []
            for trial in (1, 2):
                resp = {}
                for label, prompt in (("deployed", deployed),
                                      ("generated", generated)):
                    out = ""
                    for _attempt in range(3):
                        out = text_of(gen_llm.invoke(
                            [("system", prompt), ("human", probe)]))
                        if len(out.split()) >= 30:
                            break
                    resp[label] = out
                flip = rng.random() < 0.5
                a, b = ((resp["generated"], resp["deployed"]) if flip
                        else (resp["deployed"], resp["generated"]))
                g = grader.invoke([("human", GRADER_PROMPT.format(
                    probe=probe, a=a, b=b))])
                gtext = text_of(g)
                verdict = ("SAME-VOICE" if "VERDICT: SAME-VOICE" in gtext
                           else "DIFFERENT-VOICE"
                           if "VERDICT: DIFFERENT-VOICE" in gtext
                           else "UNPARSED")
                per_trial.append(verdict)
                raw.write(json.dumps({
                    "category": cat, "probe": probe, "trial": trial,
                    "a_is": "generated" if flip else "deployed",
                    "responses": resp, "grading": gtext,
                    "verdict": verdict}, ensure_ascii=False) + "\n")
                print(f"{cat} trial {trial}: {verdict}")
            results.append({"category": cat, "trials": per_trial,
                            "fails_both": per_trial.count("DIFFERENT-VOICE") == 2})
    n_fail = sum(1 for r in results if r["fails_both"])
    summary = {"probes": results, "probes_failing_both_trials": n_fail,
               "parity": "PASS" if n_fail == 0 else "FAIL"}
    (STAGING / "s62_pahc_probe_parity_result.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"\nprobe parity: {summary['parity']} "
          f"({n_fail} probe(s) DIFFERENT-VOICE on both trials)")
    print(f"raw: {raw_path}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
