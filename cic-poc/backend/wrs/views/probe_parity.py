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
- grading: per probe and trial, the two responses are presented as A/B in
  a seeded-shuffled order (grader never told which is deployed); grader
  must answer SAME-VOICE / DIFFERENT-VOICE on register, measure, refusal
  behavior, and vocabulary, with the divergences named.
- verdict: parity holds if no probe gets DIFFERENT-VOICE on both trials.
  Raw transcript written to staging/probe_parity_raw.jsonl; summary to
  staging/probe_parity_result.json.
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
DEPLOYED = BACKEND / "data" / "desert_world" / "desert_Representative_Permanent_Prompt_Papnoute.txt"
GENERATED = STAGING / "desert_world" / "desert_Representative_Permanent_Prompt_generated.txt"

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
    gen_llm = ChatAnthropic(model=settings.llm_model, max_tokens=1200,
                            api_key=settings.anthropic_api_key)
    # grader max_tokens must leave room for thinking blocks - 500 produced
    # empty text fields (UNPARSED) when thinking consumed the budget
    grader = ChatAnthropic(model=settings.llm_model, max_tokens=1500,
                           api_key=settings.anthropic_api_key)

    deployed = DEPLOYED.read_text(encoding="utf-8")
    generated = GENERATED.read_text(encoding="utf-8")
    rng = random.Random(20260727)

    raw_path = STAGING / "probe_parity_raw.jsonl"
    results = []
    with raw_path.open("w", encoding="utf-8") as raw:
        for cat, probe in PROBES:
            per_trial = []
            for trial in (1, 2):
                resp = {}
                for label, prompt in (("deployed", deployed),
                                       ("generated", generated)):
                    r = gen_llm.invoke([("system", prompt), ("human", probe)])
                    out = text_of(r)
                    if not out:  # one retry on empty (thinking-only) output
                        out = text_of(gen_llm.invoke(
                            [("system", prompt), ("human", probe)]))
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
    (STAGING / "probe_parity_result.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"\nprobe parity: {summary['parity']} "
          f"({n_fail} probe(s) DIFFERENT-VOICE on both trials)")
    print(f"raw: {raw_path}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
