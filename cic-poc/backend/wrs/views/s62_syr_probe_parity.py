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
    """Extract the text content from a ChatAnthropic response - with
    adaptive thinking the content is a list of blocks (thinking blocks
    carry signatures that must never reach a grader or transcript)."""
    c = msg.content
    if isinstance(c, str):
        return c
    return "\n".join(b.get("text", "") for b in c
                     if isinstance(b, dict) and b.get("type") == "text").strip()


def main() -> int:
    from langchain_anthropic import ChatAnthropic
    from app.config import settings

    # generation budget must leave room for thinking blocks too - 400
    # produced an occasional EMPTY text (graded as total divergence, a
    # harness artifact); the measure discipline comes from the prompt,
    # not the cap
    # S6.2 harness fix (the Desert S2.8 empty-response class recurred at
    # 1200 on the Alexandria prompts - 4 empty + 2 truncated generated
    # responses in the first run, graded as divergence): budget raised and
    # the single retry replaced with a bounded non-empty retry loop.
    gen_llm = ChatAnthropic(model=settings.llm_model, max_tokens=3000,
                            api_key=settings.anthropic_api_key)
    # grader max_tokens must leave room for thinking blocks - 500 produced
    # empty text fields (UNPARSED) when thinking consumed the budget
    grader = ChatAnthropic(model=settings.llm_model, max_tokens=2500,
                           api_key=settings.anthropic_api_key)

    deployed = DEPLOYED.read_text(encoding="utf-8")
    generated = GENERATED.read_text(encoding="utf-8")
    rng = random.Random(20260728)

    raw_path = STAGING / "s62_syr_probe_parity_raw.jsonl"
    results = []
    with raw_path.open("w", encoding="utf-8") as raw:
        for cat, probe in PROBES:
            per_trial = []
            for trial in (1, 2):
                resp = {}
                for label, prompt in (("deployed", deployed),
                                       ("generated", generated)):
                    out = ""
                    for _attempt in range(3):  # bounded non-empty retry
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
                           else "DIFFERENT-VOICE" if "VERDICT: DIFFERENT-VOICE" in gtext
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
    (STAGING / "s62_syr_probe_parity_result.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"\nprobe parity: {summary['parity']} "
          f"({n_fail} probe(s) DIFFERENT-VOICE on both trials)")
    print(f"raw: {raw_path}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
