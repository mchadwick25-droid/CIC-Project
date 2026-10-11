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
import re
import sys
import time
from pathlib import Path

from anthropic import APIError, APITimeoutError, RateLimitError

from engine.m1.loader import load_world_records
from engine.m5.failure import CallOutcome
from engine.provider import guard

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
# V1.8's own two-grader rule (CiC_Record_Native_World_Build_Process_V1.9.md,
# "The rendering-fidelity gate is a birth condition"): Haiku 4.5 and Sonnet
# 4.6, each run twice - a flag from either grader on either run counts;
# "translation" means every run from both graders read "translation".
# Sonnet 4.6 is what that document names; it is replaced by Sonnet 5 once
# the account can invoke it and the grader study behind this rule is
# re-run - not this module's own call to make.
SONNET_MODEL_PATTERN = "us.anthropic.claude-sonnet-4-6"

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


def two_grader_verdict(*, region: str, original: str, modern_rendering: str, runs: int = 2) -> dict:
    """V1.8's own two-grader pass for one rendering: Haiku 4.5 and Sonnet
    4.6, each run `runs` times against the SAME input. `clean` is True
    only when every run from both graders read "translation" - a flag
    from either grader on either run makes it False. Real Bedrock calls;
    a caller should account for cost/ceiling before invoking this."""
    from engine.provider.bedrock import make_client, resolve_model_id

    graders = [("haiku-4.5", MODEL_PATTERN), ("sonnet-4.6", SONNET_MODEL_PATTERN)]
    all_runs = []
    for label, pattern in graders:
        model_id = resolve_model_id(pattern, region)
        client = make_client(region)
        for run_n in range(1, runs + 1):
            outcome = grade_rendering(client, model_id, original=original, modern_rendering=modern_rendering)
            usage = outcome.raw_usage
            usage_dict = ({"input_tokens": getattr(usage, "input_tokens", None),
                          "output_tokens": getattr(usage, "output_tokens", None),
                          "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None),
                          "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None)}
                         if usage is not None else None)
            if outcome.failed:
                # outcome.value is None for a plain timeout (grade_rendering's
                # own APITimeoutError branch doesn't set it) - fall back to
                # the status string so a caller can always tell an errored
                # run from a real "translation" verdict.
                all_runs.append({"grader": label, "model_id": model_id, "run": run_n,
                                 "verdict": None, "reasoning": None, "usage": usage_dict,
                                 "error": outcome.value or {"status": outcome.status}})
            else:
                all_runs.append({"grader": label, "model_id": model_id, "run": run_n,
                                 "verdict": outcome.value["verdict"], "reasoning": outcome.value["reasoning"],
                                 "usage": usage_dict, "error": None})

    errored = [r for r in all_runs if r["error"] is not None]
    clean = not errored and all(r["verdict"] == "translation" for r in all_runs)
    return {"clean": clean, "runs": all_runs}


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


# The grader itself (SYSTEM_PROMPT, grade_rendering) is already language-
# agnostic - it judges whether the modern English carries every clause of
# whatever original it is given, never assuming that original is itself
# English. This is the fleet's cross-language subset of that same sweep:
# every quote whose named source's own vendored file declares a language
# other than English (cic/engine/texts_registry.py's own `Language:`
# header convention), scoped and graded on its own rather than folded into
# fleet_report's much larger, more expensive full sweep.
_TEXTS_DIR = REPO_ROOT / "cic" / "texts"
# Duplicated from engine/m1/gates.py's own _EDITION_PATH by this module's
# same standing convention (that module's own comment on _TEXTS_DIR/
# _EDITION_PATH): engine/m1/ does not reach across the cic/ package
# boundary for a one-line regex.
_EDITION_PATH = re.compile(r"cic/texts/([\w\-]+\.(?:txt|xml))")

CROSS_LANGUAGE_REPORT_PATH = Path(__file__).resolve().parent / "reports" / "cross-language-rendering-report-2026-09-25.json"


def non_english_sourced_quotes(worlds: dict[str, dict]) -> list[dict]:
    """Every quote record across the given worlds (world_key -> its own
    load_world_records() result) whose own FIRST resolving source declares
    a non-English `Language:` header. A quote can name more than one
    source; the first one that resolves to a real vendored file decides
    it, English or not - matching how a Representative would actually
    read the record (against its own first named source), not every
    source it happens to cite. A quote whose first-resolving source is
    English is skipped even if a later source is non-English (e.g. an
    NPNF translation cited first, a Latin critical edition cited second
    for the same passage) - the record's own `text` is the NPNF English
    either way, so grading it against that later Latin source would be
    an English-to-English comparison mislabeled as cross-language."""
    from cic.engine.texts_registry import language_declared

    found = []
    for world_key, records in worlds.items():
        for rid, rec in records.items():
            if rec.get("record_type") != "quote":
                continue
            for s in (rec.get("sources") or []):
                src = records.get(s.get("source_id"))
                if not src:
                    continue
                m = _EDITION_PATH.search(str(src.get("edition") or ""))
                if not m:
                    continue
                path = _TEXTS_DIR / m.group(1)
                if not path.is_file():
                    continue
                header = path.read_text(encoding="utf-8", errors="replace")[:4000]
                lang = language_declared(header)
                if lang and lang != "en":
                    found.append({"world": world_key, "id": rid, "source_id": s.get("source_id"),
                                 "filename": m.group(1), "language": lang, "record": rec})
                break  # the first source that resolves to a real vendored file decides it, English or not
    return found


def cross_language_report(region: str) -> dict:
    from engine.m1.quote_verbatim import REPORT_WORLDS
    from engine.provider.bedrock import make_client, resolve_model_id

    worlds = {w: load_world_records(w) for w in REPORT_WORLDS}
    targets = non_english_sourced_quotes(worlds)
    model_id = resolve_model_id(MODEL_PATTERN, region)
    client = make_client(region)

    graded = []
    errors = []
    no_rendering = []
    verdict_counts = {v: 0 for v in VERDICTS}
    for t in sorted(targets, key=lambda x: (x["world"], x["id"])):
        rec = t["record"]
        rendering = rec.get("modern_rendering")
        if not rendering:
            no_rendering.append(t["id"])
            continue
        outcome = grade_rendering(client, model_id, original=rec["text"], modern_rendering=rendering)
        if outcome.failed:
            errors.append({"id": t["id"], "status": outcome.status, "detail": outcome.value})
            continue
        verdict_counts[outcome.value["verdict"]] += 1
        graded.append({
            "world": t["world"],
            "id": t["id"],
            "language": t["language"],
            "source_file": t["filename"],
            "verdict": outcome.value["verdict"],
            "reasoning": outcome.value["reasoning"],
            "verification_state": (rec.get("confidence") or {}).get("verification_state"),
        })

    return {
        "model_id": model_id,
        "region": region,
        # V1.8's rendering-fidelity rule is two graders (Haiku 4.5 and
        # Sonnet 4.6) agreeing "translation" on two runs in a row, with a
        # flag from either counting. This report runs one grader once -
        # a first-pass screen for the cross-language subset, not a V1.8
        # two-grader pass. A "translation" verdict here is not yet a
        # clearance; a "summary"/"expansion"/"mixed" verdict is still a
        # real finding worth acting on.
        "grader_scope": "single Haiku run; first-pass screen, not a V1.8 two-grader pass",
        "total_non_english_sourced_quotes": len(targets),
        "graded_count": len(graded),
        "no_modern_rendering_count": len(no_rendering),
        "no_modern_rendering": no_rendering,
        "error_count": len(errors),
        "errors": errors,
        "verdict_counts": verdict_counts,
        "findings": graded,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    parser.add_argument("--cross-language-only", action="store_true",
                        help="grade only quotes whose own source declares a non-English Language: header, "
                             "instead of the full fleet sweep")
    args = parser.parse_args(argv)

    if args.cross_language_only:
        report = cross_language_report(args.region)
        CROSS_LANGUAGE_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        CROSS_LANGUAGE_REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(
            f"cross-language rendering sweep: {report['graded_count']}/{report['total_non_english_sourced_quotes']} graded "
            f"({report['no_modern_rendering_count']} no modern_rendering, {report['error_count']} errors), "
            f"verdicts={report['verdict_counts']}"
        )
        for f in report["findings"]:
            if f["verdict"] != "translation":
                print(f"  {f['id']} ({f['language']}): {f['verdict']} - {f['reasoning']}")
        print(f"\nfull report written to {CROSS_LANGUAGE_REPORT_PATH.relative_to(REPO_ROOT)}")
        return 0  # report-only: never fails the run regardless of findings

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
