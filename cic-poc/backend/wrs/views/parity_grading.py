"""Voice Rebuild Phase 0.4 (Design §5, Research q5) - probe_parity's
redefined split grading, shared by all six per-world variants
(probe_parity.py/Desert + the five s62_<world>_probe_parity.py scripts).

Design §5's own spec: "split the four graded dimensions - identity/fact/
boundary continuity (refusal behavior, vocabulary ownership, span) must
grade SAME-VOICE; register/measure are *expected* to change and are
graded instead against the rebuilt targets (the world's recorded measure
and floor), with the old prompt kept as reference so the change is
visible and named, not silent."

Before this phase, probe_parity's single grader call folded all four axes
(register, measure, refusal behavior, vocabulary) into one SAME-VOICE /
DIFFERENT-VOICE verdict, measured against the DEPLOYED prompt as the
target. That was right for a continuity regression across incidental code
changes, and wrong for a deliberate rebuild: a rebuilt world's register
and measure are SUPPOSED to move (toward its own recorded native_measure
and the fleet-wide reading_floor, wrs/parameters.yaml), and grading that
change as a DIFFERENT-VOICE failure would punish the rebuild for doing
its job. Post-rebuild, the assembly-identity check (wrs/views/
assembly_identity.py, Phase 0.3) takes over parity's drift-alarm role for
incidental changes; this script becomes the returning-participant
continuity read for whatever changes come after that.

Split, concretely:
- CONTINUITY_GRADER_PROMPT below drops register and measure from the
  SAME-VOICE question entirely - it grades only refusal behavior,
  vocabulary ownership, and span (does the response stay inside the same
  temporal/factual boundaries the deployed voice holds). These three are
  NOT expected to move in a rebuild and a DIFFERENT-VOICE verdict on them
  is a real regression.
- register_measure_check() below is NOT an LLM grade at all - it reuses
  the same objective instruments Phase 0.1/0.3 already built
  (wrs.gates.core.readability_check, app.graph.repair_classifier.
  ceiling_words_map) to check the GENERATED response against the world's
  OWN recorded target, and reports the DEPLOYED response's own numbers
  alongside as reference - visible and named, per Design §5, never
  silently dropped.

Deliberately a shared module rather than six more copy-pasted copies:
unlike the per-world S52 assemblers (genuinely different record paths
and record-id keys per world - a real case for copy-and-adapt), the six
probe_parity variants' grading logic is byte-identical already; only
DEPLOYED/GENERATED paths, PROBES, output filenames, and a couple of
already-per-world generation parameters differ (preserved via run_parity's
own arguments below, not silently unified - see each call site).
"""
from __future__ import annotations

import json
import random
from pathlib import Path

CONTINUITY_GRADER_PROMPT = """You are grading a voice-continuity regression. Below are two responses (A and B) to the same participant question, each produced by a Representative prompt for the same historical world. You do not know which prompt produced which response, and that is deliberate.

Judge ONE question: do A and B speak as the SAME VOICE on the axes below? Register and measure (terseness, response length) are DELIBERATELY EXCLUDED from this judgment - a rebuilt voice is expected to change register and measure, and that expected change must never be graded as a continuity failure. Assess only:
1. Refusal behavior (does each hold the same boundaries - declining the same things, in-voice, without breaking character?)
2. Vocabulary ownership (same native terms and image-world - not the same sentence length or elaboration)
3. Span (does each stay inside the same temporal horizon and factual boundaries the world holds - no claim, era, or figure one response reaches for that the other world would not recognize as its own)

Differences in wording, content selection, register, or length are expected and fine on their own; the question is narrower than "read the same" - it is whether a returning participant would recognize the same person's boundaries and vocabulary. Answer in exactly this format:
VERDICT: SAME-VOICE or DIFFERENT-VOICE
AXES: <one line per axis (refusal behavior / vocabulary ownership / span), brief>
DIVERGENCES: <the concrete divergences that most matter on these three axes only, or 'none material'>

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


def register_measure_check(world_id: str, deployed_text: str,
                           generated_text: str) -> dict:
    """The register/measure half of the split (Design §5): not an LLM
    grade, an objective check of the GENERATED response against the
    world's own rebuilt targets - word count against its recorded
    ceiling_words (voice_profile.native_measure, wired in Phase 0.1's
    ceiling_words_map), and the fleet-wide reading_floor (Phase 0.3's
    check_readability wiring reuses the same wrs.gates.core instrument).
    The deployed response's own numbers are reported alongside, never
    dropped - "kept as reference so the change is visible and named."
    """
    from wrs.gates.core import readability_check
    from app.graph.repair_classifier import ceiling_words_map

    ceiling = ceiling_words_map().get(world_id)
    deployed_words = len(deployed_text.split())
    generated_words = len(generated_text.split())
    deployed_read = (readability_check(deployed_text)
                     if len(deployed_text.split()) > 30 else None)
    generated_read = (readability_check(generated_text)
                      if len(generated_text.split()) > 30 else None)
    return {
        "world_id": world_id,
        "ceiling_words": ceiling,
        "deployed_words": deployed_words,
        "generated_words": generated_words,
        "generated_within_ceiling": (
            generated_words <= ceiling if ceiling is not None else None),
        "deployed_readability": deployed_read,
        "generated_readability": generated_read,
        "generated_meets_floor": (
            not generated_read["violations"] if generated_read else None),
    }


def run_parity(*, world_id: str, deployed_path: Path, generated_path: Path,
               probes: list[tuple[str, str]], gen_max_tokens: int,
               grader_max_tokens: int, seed: int, retry_mode: str,
               raw_path: Path, result_path: Path) -> int:
    """Shared orchestration for all six variants. retry_mode preserves
    each script's own pre-existing generation-retry behavior exactly
    (never unified silently):
      "empty"     - Desert's original: one retry only on totally empty
                    (thinking-only) output.
      "min_words" - the five later ports' fix: up to 3 attempts, retry
                    while output is under 30 words.
    """
    from langchain_anthropic import ChatAnthropic
    from app.config import settings

    gen_llm = ChatAnthropic(model=settings.llm_model, max_tokens=gen_max_tokens,
                            api_key=settings.anthropic_api_key)
    grader = ChatAnthropic(model=settings.llm_model, max_tokens=grader_max_tokens,
                           api_key=settings.anthropic_api_key)

    deployed = deployed_path.read_text(encoding="utf-8")
    generated = generated_path.read_text(encoding="utf-8")
    rng = random.Random(seed)

    results = []
    register_measure_by_probe = {}
    with raw_path.open("w", encoding="utf-8") as raw:
        for cat, probe in probes:
            per_trial = []
            resp = {}
            for label, prompt in (("deployed", deployed), ("generated", generated)):
                if retry_mode == "empty":
                    out = text_of(gen_llm.invoke(
                        [("system", prompt), ("human", probe)]))
                    if not out:
                        out = text_of(gen_llm.invoke(
                            [("system", prompt), ("human", probe)]))
                else:
                    out = ""
                    for _attempt in range(3):
                        out = text_of(gen_llm.invoke(
                            [("system", prompt), ("human", probe)]))
                        if len(out.split()) >= 30:
                            break
                resp[label] = out
            # register/measure: objective check, not graded same/different
            register_measure_by_probe[cat] = register_measure_check(
                world_id, resp["deployed"], resp["generated"])
            for trial in (1, 2):
                flip = rng.random() < 0.5
                a, b = ((resp["generated"], resp["deployed"]) if flip
                        else (resp["deployed"], resp["generated"]))
                g = grader.invoke([("human", CONTINUITY_GRADER_PROMPT.format(
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
                            "fails_both": per_trial.count("DIFFERENT-VOICE") == 2,
                            "register_measure": register_measure_by_probe[cat]})
    n_fail = sum(1 for r in results if r["fails_both"])
    summary = {"probes": results, "probes_failing_both_trials": n_fail,
               "continuity_parity": "PASS" if n_fail == 0 else "FAIL",
               "note": "continuity_parity grades refusal behavior/vocabulary/"
                       "span only (Design §5 split); each probe's own "
                       "register_measure block is the objective register/"
                       "measure check against this world's rebuilt target, "
                       "not a same-voice grade."}
    result_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"\ncontinuity parity: {summary['continuity_parity']} "
          f"({n_fail} probe(s) DIFFERENT-VOICE on both trials)")
    print(f"raw: {raw_path}")
    return 0 if n_fail == 0 else 1
