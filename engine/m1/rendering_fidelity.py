"""Does a quote record's
`modern_rendering` actually TRANSLATE its `text`, rather than summarize or
expand it? The standard: "the
representitive translates it into modern english, this is translation, not
summation." A rendering that silently drops a clause the
original states, or adds a clause the original never states, fails this
standard regardless of how natural or well-written it reads - the same
"no invented ... no invented ..." discipline CLAUDE.md's Source fidelity
section applies to a record's own `text`, extended to what a Representative
would actually say from it.

REPORT-ONLY. Not registered in gates.GATES: this is about build quality,
not fix on fix. It names this gate as `modern_rendering`'s own future
birth condition (build-process doc V1.6, Phase B), not a repair pass to
run today. This script is the measurement that decision will act on, not
yet the gate itself.

HOW A BIRTH CONDITION USES THIS: a single live model call is not
deterministic enough to gate on by
itself - this session's own two fleet runs, and the transparency thread's
reader check the same day, both saw real run-to-run variance on the same
input. So the birth-condition use is: the builder authoring a
`modern_rendering` runs this grader at authoring time; a person reads the
verdict's own `reasoning`, not just its enum value; the record is revised
until the verdict reads "translation" on two consecutive runs of the same
input, not accepted on one clean pass. This module itself stays
report-only - it is not registered in gates.GATES as a blocking check.

SCOPE, decided here rather than left implicit: every quote record with a
non-empty `modern_rendering` is graded, regardless of its own
`confidence.verification_state`. Rendering fidelity (does the modern
English carry every clause of `text`?) is a different question from
source-verbatim fidelity (does `text` itself match the vendored source? -
quote_verbatim.py's own question) - a record already escalated below
verified-direct for a source-fidelity reason still needs its rendering
checked, and vice versa. Each finding below carries the record's own
`verification_state` for context, never as a filter. There is no
per-record field or instruction anywhere in this module - one general
grading standard, applied the same way to every world.

GRADER: Haiku 4.5 (Bedrock, resolved through engine.provider.bedrock -
never a hand-typed model ID), forced tool-use so the verdict is validated
structure, never salvage-parsed prose - the same idiom engine.m5.live_calls
already uses for the Facilitator's own gate calls. The installed Anthropic
SDK's Messages API (confirmed by reading its own create() signature - no
`temperature`/`top_p`/`top_k` parameter exists on it) exposes no sampling
control at all here, so - like every other caller in this codebase
(engine.m5.live_calls, engine.m4.turn_selector, etc., none of which sets
one either) - determinism rests on the forced-tool-use + closed-enum
schema alone, not on a temperature setting this API does not offer.
"""
import argparse
import json
import sys
import time
from pathlib import Path

from anthropic import APIError, APITimeoutError, RateLimitError

from engine.m1.loader import load_world_records
from engine.m5.failure import CallOutcome

# A sequential fleet sweep of ~80 live calls ran into this account's real
# Bedrock rate limit mid-run (21 of 100 calls hit a 429 with no retry, an
# incomplete sweep silently reported as though it were the whole fleet).
# The SDK client's own default retry budget was not enough on its own;
# retry here explicitly, with real exponential backoff, rather than accept
# a partial report - RateLimitError only, since that is the actual
# observed failure mode, not any transient error class.
_RATE_LIMIT_MAX_RETRIES = 5
_RATE_LIMIT_BASE_DELAY_SECONDS = 2.0

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "rendering-fidelity-report-2026-09-23.json"

MODEL_PATTERN = "us.anthropic.claude-haiku-4-5"

VERDICTS = ("translation", "summary", "expansion", "mixed")

SYSTEM_PROMPT = """You are grading whether a modern-English rendering of a historical quotation is a \
TRANSLATION of the original, not a summary or an expansion. This is the standard this project's own \
lead ruled directly: "the representative translates it into modern english, this is translation, not \
summation." A translation carries every clause of the original into modern English - nothing left out, \
nothing added, nothing compressed into a shorter paraphrase that drops real content. It may reorder for \
natural modern syntax, and it may render an idiom or period phrase in its modern equivalent, but it may \
not silently omit a clause, combine two distinct claims into one and lose one of them, or add anything - \
an explanation, a qualification, a claim - that is not present in the original.

Classify the modern rendering as exactly one of:
- "translation": every clause of the original is present in the rendering; nothing added, nothing \
compressed away.
- "summary": the rendering compresses, shortens, or drops real content that the original states.
- "expansion": the rendering adds content, explanation, or claims not present in the original.
- "mixed": the rendering both drops some real content of the original AND adds content not present in it.

Judge only whether the rendering is a full, faithful translation of every clause - not whether it reads \
well, and not whether you personally find it historically accurate (the original text is assumed \
correct as given; you are not fact-checking it, only checking whether the rendering carries it whole). \
State your reasoning in one or two sentences, naming the specific clause(s) dropped or added if the \
verdict is not "translation"."""

_VERDICT_TOOL = {
    "name": "submit_rendering_fidelity_verdict",
    "description": "Submit the rendering-fidelity verdict for one quote's modern_rendering against its original text.",
    "input_schema": {
        "type": "object",
        "properties": {
            "verdict": {"type": "string", "enum": list(VERDICTS)},
            "reasoning": {"type": "string"},
        },
        "required": ["verdict", "reasoning"],
    },
}


def grade_rendering(client, model_id: str, *, original: str, modern_rendering: str, timeout: float = 8.0) -> CallOutcome:
    user_content = f"Original:\n{original}\n\nModern rendering:\n{modern_rendering}"
    delay = _RATE_LIMIT_BASE_DELAY_SECONDS
    for attempt in range(_RATE_LIMIT_MAX_RETRIES + 1):
        try:
            response = client.messages.create(
                model=model_id,
                max_tokens=512,
                system=SYSTEM_PROMPT,
                tools=[_VERDICT_TOOL],
                tool_choice={"type": "tool", "name": _VERDICT_TOOL["name"]},
                messages=[{"role": "user", "content": user_content}],
                timeout=timeout,
            )
            break
        except APITimeoutError:
            return CallOutcome(status="timeout")
        except RateLimitError as e:
            if attempt == _RATE_LIMIT_MAX_RETRIES:
                return CallOutcome(status="error", value={"error": f"rate limited after {_RATE_LIMIT_MAX_RETRIES} retries: {e}"})
            time.sleep(delay)
            delay *= 2
        except APIError as e:
            return CallOutcome(status="error", value={"error": str(e)})

    tool_uses = [b for b in response.content if b.type == "tool_use" and b.name == _VERDICT_TOOL["name"]]
    if not tool_uses:
        return CallOutcome(status="parse_failure", value={"raw": [b.model_dump() for b in response.content]})
    return CallOutcome(status="ok", value=tool_uses[0].input, raw_usage=getattr(response, "usage", None))


def sweep_world(world_key: str, client, model_id: str) -> dict:
    records = load_world_records(world_key)
    quotes = {rid: r for rid, r in records.items() if r.get("record_type") == "quote"}
    no_rendering: list[str] = []
    errors: list[dict] = []
    findings: list[dict] = []
    verdict_counts = {v: 0 for v in VERDICTS}
    graded_count = 0

    for rid, rec in sorted(quotes.items()):
        rendering = rec.get("modern_rendering")
        if not rendering:
            no_rendering.append(rid)
            continue
        outcome = grade_rendering(client, model_id, original=rec["text"], modern_rendering=rendering)
        if outcome.failed:
            errors.append({"id": rid, "status": outcome.status, "detail": outcome.value})
            continue
        graded_count += 1
        verdict = outcome.value["verdict"]
        verdict_counts[verdict] += 1
        if verdict != "translation":
            findings.append(
                {
                    "id": rid,
                    "verdict": verdict,
                    "reasoning": outcome.value["reasoning"],
                    "verification_state": (rec.get("confidence") or {}).get("verification_state"),
                }
            )

    return {
        "world": world_key,
        "total_quotes": len(quotes),
        "graded_count": graded_count,
        "no_modern_rendering_count": len(no_rendering),
        "no_modern_rendering": no_rendering,
        "error_count": len(errors),
        "errors": errors,
        "verdict_counts": verdict_counts,
        "findings": findings,
    }


def fleet_report(region: str) -> dict:
    from engine.m1.quote_verbatim import REPORT_WORLDS
    from engine.provider.bedrock import make_client, resolve_model_id

    model_id = resolve_model_id(MODEL_PATTERN, region)
    client = make_client(region)
    worlds = {w: sweep_world(w, client, model_id) for w in REPORT_WORLDS}
    return {
        "model_id": model_id,
        "region": region,
        "worlds": worlds,
        "totals": {
            "total_quotes": sum(w["total_quotes"] for w in worlds.values()),
            "graded_count": sum(w["graded_count"] for w in worlds.values()),
            "no_modern_rendering_count": sum(w["no_modern_rendering_count"] for w in worlds.values()),
            "error_count": sum(w["error_count"] for w in worlds.values()),
            "verdict_counts": {v: sum(w["verdict_counts"][v] for w in worlds.values()) for v in VERDICTS},
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", required=True)
    args = parser.parse_args(argv)

    report = fleet_report(args.region)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    t = report["totals"]
    print(
        f"rendering-fidelity sweep: {t['graded_count']}/{t['total_quotes']} graded "
        f"({t['no_modern_rendering_count']} no modern_rendering, {t['error_count']} errors), "
        f"verdicts={t['verdict_counts']}"
    )
    for w in report["worlds"].values():
        print(f"  {w['world']:12} graded={w['graded_count']:4} verdicts={w['verdict_counts']}")
    print(f"\nfull report written to {REPORT_PATH.relative_to(REPO_ROOT)}")
    return 0  # report-only this PR: never fails the run regardless of findings


if __name__ == "__main__":
    sys.exit(main())
