"""R38's own candidate (C), ordered by the reviewer thread's verdict on
PR #436 round 1: a live, billed reader-model (Haiku 4.5) support check,
report-only, no net code change. Item 3's own hand-check on this PR's
first pass found the bag-of-words remainder measurement (candidates A/B)
has 0 of 6 precision on real corpus data - it cannot tell "handed over
the sacred books" (the confirmed real fabrication) from "the whole of
Scripture is one voice" (an honest Origen paraphrase) by lexical
remainder alone. Candidate (C) asks a real reader model the actual
question instead of a word-overlap proxy for it: does the tagged
record's own text support every claim in this sentence.

Same corpus-building logic as net_remainder_measure.py, reused directly
rather than re-implemented (imported, not copied) - one measurement,
one definition of "the 311," so this script's own numbers are
comparable to that PR's own candidate A/B numbers without drift. Two
scopes, per the reviewer's own instruction:
  C1 - every zero-floor-branch sentence (the "tag is the claim" branch,
       no ratio floor at all - the worked example's own real path)
  C2 - only sentences whose OWN TURN was routed other_tradition

C2's own real count, checked directly before writing a line of this
script's own logic: the Corpus A pool (live-turn-report*.json) predates
the B-other-tradition probe shape entirely (confirmed by scanning every
result's own routing_reason for "tradition" - zero hits, in any of the
11 worlds' own files). C2 is genuinely empty on this corpus - stated
here rather than forced to a nonzero number or silently substituted.
The worked example itself (interview, Theon on the Donatists, IS an
other_tradition turn) is tested separately, outside the corpus, for
exactly this reason - see run_scope's own "extra" row below.

Cost, stated before running per the reviewer's own instruction ("say
the number before running and run anyway unless it exceeds one
hundred dollars"): 312 short forced-tool-use Haiku 4.5 calls (a
sentence plus its tagged record's own text, well under 1000 input
tokens each; a small structured JSON output). At Haiku 4.5's published
rate ($1/$5 per million input/output tokens, same PRICE_TABLE_SOURCE
every other M8 script in this project already cites), estimated at
roughly $0.30-0.60 total - printed exactly, from real usage, once the
run completes; nowhere near the $100 ceiling.

Run: python3 -m engine.m4.reports.net_support_check_measure --region us-east-1
"""
import argparse
import json
import pathlib
import sys
import time
from datetime import date, datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m4 import evidence as ev
from engine.m4 import grounding_net as gn
from engine.m4.reports.net_remainder_measure import (
    REPORTS_DIR,
    WORLDS,
    load_repo,
    measure_sentence,
)
from engine.m5 import live_calls
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE
from engine.prose import all_text
from engine.provider import guard
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]

SUPPORT_CHECK_SYSTEM_PROMPT = """You are a support-checking reader for a historical formation-world text \
engine. You are given ONE sentence a voice generated, tagged to one or more of this world's own records, \
plus the full text of each tagged record.

Decide whether the tagged record's own text supports EVERY specific factual claim in the sentence - not \
just some of it, and not whether the sentence is historically plausible in general.

- "supported": every specific claim in the sentence is directly stated by, or a close paraphrase of, the \
tagged record's own text.
- "partly_supported": part of the sentence is grounded in the tagged record's own text, but another part \
asserts something specific the record's own text does not say - even if that added part sounds plausible \
or fits the same general topic.
- "not_supported": the tagged record's own text does not support the sentence's central claim at all.

Judge only against the tagged record's own text given to you here - never general historical knowledge, \
never what you personally believe is true, only whether these specific words are grounded in this specific \
record. Ordinary framing, connective, or interpretive language (not itself a factual claim) counts as \
supported even if it has no direct match in the record's own words. When the verdict is partly_supported \
or not_supported, name the unsupported clause exactly as it appears in the sentence; when supported, leave \
it empty."""

_SUPPORT_CHECK_TOOL = {
    "name": "submit_support_check",
    "description": "Submit the support-check verdict for this sentence against its tagged record(s).",
    "input_schema": {
        "type": "object",
        "properties": {
            "verdict": {"type": "string", "enum": ["supported", "partly_supported", "not_supported"]},
            "unsupported_clause": {"type": "string"},
        },
        "required": ["verdict", "unsupported_clause"],
    },
}


def _support_check(client, model_id: str, *, sentence: str, tags: list[str], repository_records: dict):
    record_blocks = []
    for t in tags:
        rec = repository_records.get(t)
        if rec is not None:
            record_blocks.append(f"Record {t}:\n{all_text(rec)}")
    user_content = (
        f"Sentence to check:\n{sentence}\n\n"
        f"Tagged record(s):\n\n" + "\n\n".join(record_blocks)
    )
    return live_calls._forced_tool_call(
        client, model_id, system=SUPPORT_CHECK_SYSTEM_PROMPT, tool=_SUPPORT_CHECK_TOOL, user_content=user_content,
        timeout=10.0,
    )


def build_corpus() -> list[dict]:
    """Same Corpus A traversal net_remainder_measure.run() already does,
    reused directly rather than reimplemented - the identical 311 rows,
    same order, so this script's own numbers describe the same corpus
    that PR's candidate (A)/(B) numbers do."""
    rows: list[dict] = []
    for fp in sorted(REPORTS_DIR.glob("live-turn-report*.json")):
        d = json.loads(fp.read_text())
        world_key = d.get("world_key")
        if world_key not in WORLDS:
            continue
        for r in d.get("results", []):
            ve = (r.get("result") or {}).get("voice_event")
            if not ve or not ve.get("grounding"):
                continue
            routing_reason = (r.get("result") or {}).get("routing_reason") or ""
            is_other_tradition_turn = "tradition" in routing_reason.lower()
            for s in ve["grounding"]["sentences"]:
                if not s.get("tags"):
                    continue
                new = gn.verdict_for_sentence(
                    s["sentence"], s["tags"],
                    repository_records=load_repo(world_key)[0],
                    figure_names=load_repo(world_key)[2],
                    thin_topics=load_repo(world_key)[1],
                    grounding_floor=gn.WITHHOLD_FLOOR,
                )
                if new["verdict"] != "ok":
                    continue
                row = measure_sentence(s["sentence"], s["tags"], new["why"], world_key)
                if row:
                    row["is_other_tradition_turn"] = is_other_tradition_turn
                    rows.append(row)
    return rows


WORKED_EXAMPLE = {
    "world": "alx",
    "sentence": "Under persecution, some gave way - they sacrificed to the gods, or they handed over the sacred books.",
    "tags": ["alx.dw.church-failure"],
    "branch": "tag_is_claim_zero_floor",
    "is_other_tradition_turn": True,
}

OWN_CLAUSE_SENTENCES = {
    "The Logos - God's own Word, who made all things and became flesh in Jesus - was the one we met in every text, Old Testament and New alike.",
    'Origen said it openly: the Gospels are "the first fruits of all the Scriptures," but the whole of Scripture is one voice, and that voice is Christ.',
    "Not one town or one decade: high plateau and river valleys, estates and hungry villages, the great city and the small sees the winters shut in.",
    "We did not leave behind letters of devotion or prayers of longing addressed to him the way later ages did - that is not the form our record takes.",
    "And he mapped the whole life as a progression: first the working stage, where you discipline the passions and win freedom from them - he called that apatheia, and it is not apathy but the stilling of what otherwise drives you.",
    "Someone divorced could belong among us - we will say that plainly first.",
}


def run(region: str) -> dict:
    model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    corpus = build_corpus()
    usage_records = []
    results = []

    def check_row(row: dict) -> dict:
        recs, _, _ = load_repo(row["world"])
        # 312 sequential calls tripped Bedrock's own rate limit on the first
        # attempt (429, "Too many requests") - retried with backoff (2s, 4s,
        # 8s, matching this project's own network-retry convention) plus a
        # small pacing delay between every call, rather than firing as fast
        # as possible and hoping the limit doesn't trip.
        last_error = None
        for attempt, delay in enumerate((0, 2, 4, 8)):
            if delay:
                time.sleep(delay)
            outcome = _support_check(client, model_id, sentence=row["sentence"], tags=row["tags"], repository_records=recs)
            if outcome.status == "ok":
                break
            last_error = outcome
            if outcome.status != "error" or "429" not in str(outcome.value):
                break
        else:
            outcome = last_error
        if outcome.status != "ok":
            raise RuntimeError(f"support-check call failed: {outcome.status} {outcome.value}")
        if outcome.raw_usage is not None:
            usage_records.append(normalize_usage(outcome.raw_usage))
        time.sleep(0.4)
        return {**row, "support_verdict": outcome.value["verdict"], "unsupported_clause": outcome.value["unsupported_clause"]}

    for row in corpus:
        results.append(check_row(row))

    worked_example_result = check_row(WORKED_EXAMPLE)

    own_clause_results = [r for r in results if r["sentence"] in OWN_CLAUSE_SENTENCES]

    def not_fully_supported(rows):
        return [r for r in rows if r["support_verdict"] != "supported"]

    c1_rows = [r for r in results if r["branch"] == "tag_is_claim_zero_floor"]
    c2_rows = [r for r in results if r.get("is_other_tradition_turn")]

    total_dollars = 0.0
    total_input = total_output = 0
    for u in usage_records:
        est = estimate_cost(u, HAIKU_4_5_PRICE_TABLE)
        total_dollars += est.dollars or 0.0
        total_input += u.input_tokens
        total_output += u.output_tokens

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "model_id": model_id,
        "corpus_size": len(corpus),
        "calls_made": len(usage_records),
        "total_dollars": round(total_dollars, 4),
        "total_input_tokens": total_input,
        "total_output_tokens": total_output,
        "avg_input_tokens_per_call": round(total_input / len(usage_records), 1) if usage_records else None,
        "avg_output_tokens_per_call": round(total_output / len(usage_records), 1) if usage_records else None,
        "full_311_not_fully_supported": len(not_fully_supported(results)),
        "full_311_total": len(results),
        "c1_zero_floor_branch": {
            "scope_size": len(c1_rows),
            "not_fully_supported": len(not_fully_supported(c1_rows)),
        },
        "c2_other_tradition_turn": {
            "scope_size": len(c2_rows),
            "not_fully_supported": len(not_fully_supported(c2_rows)),
            "note": (
                "0 by construction - the Corpus A pool (live-turn-report*.json) predates "
                "the B-other-tradition probe shape entirely; no turn in it is routed "
                "other_tradition. Not forced to a nonzero number."
            ) if not c2_rows else None,
        },
        "worked_example": worked_example_result,
        "worked_example_caught": worked_example_result["support_verdict"] != "supported",
        "own_clause_examples": own_clause_results,
        "own_clause_examples_passed": sum(1 for r in own_clause_results if r["support_verdict"] == "supported"),
        "own_clause_examples_total": len(own_clause_results),
        "all_results": results,
    }


def main():
    parser = argparse.ArgumentParser()
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    args = parser.parse_args()

    corpus_size = len(build_corpus())
    print(
        f"About to make {corpus_size + 1} live Haiku 4.5 support-check calls "
        f"({corpus_size} corpus sentences + 1 worked example). Estimated cost: ~$0.30-0.60 "
        f"(well under the $100 ceiling) - proceeding.",
        flush=True,
    )

    report = run(args.region)
    out_path = REPORTS_DIR / f"net-support-check-measure-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    print(f"Real cost: ${report['total_dollars']} ({report['calls_made']} calls)")
    print(f"Full 311: {report['full_311_not_fully_supported']}/{report['full_311_total']} not fully supported")
    print(
        f"C1 (zero-floor branch): {report['c1_zero_floor_branch']['not_fully_supported']}/"
        f"{report['c1_zero_floor_branch']['scope_size']} not fully supported"
    )
    print(
        f"C2 (other_tradition turns): {report['c2_other_tradition_turn']['not_fully_supported']}/"
        f"{report['c2_other_tradition_turn']['scope_size']} not fully supported "
        f"({report['c2_other_tradition_turn']['note']})"
    )
    print(f"Worked example caught: {report['worked_example_caught']} ({report['worked_example']['support_verdict']})")
    print(f"Own-clause examples passed: {report['own_clause_examples_passed']}/{report['own_clause_examples_total']}")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
