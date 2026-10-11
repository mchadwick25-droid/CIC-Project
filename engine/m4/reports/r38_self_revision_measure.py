"""R38, Mark's own ruling (relayed 2026-09-23): candidates A and B (the
lexical-remainder net rules) are closed - they withhold honest
paraphrase to catch a class with 0 of 6 precision (Entry 57). Candidate
C (the live support-check reader) is the fallback only if self-revision,
measured here first, does not reach near zero.

WHAT SELF-REVISION IS (Mark's own words, verbatim spec): after the voice
drafts its turn, a SECOND voice call - same model, same system prompt -
is given its own draft plus the exact, full text of every record it
tagged, and told: for each tagged sentence, keep only what that record
says or exactly paraphrases; trim any detail the record does not give,
even if believed true; do not add, do not re-tag, do not change any
untagged sentence; return the revised turn. The revised turn is what
apply_net would see and the participant would read - generation, not
correction: no withhold, no Facilitator, no regeneration loop. Scoped
to other_tradition-routed turns only (where the leak class lives), so
the extra call lands on rare turns, not every turn.

MEASURED: the same worked example, same harness and hand-reading as
Entries 59-60 (engine.m4.reports.r39_generation_side_measure /
r39_d1_d2_measure) - Theon on the Donatists, 20 runs, PROPOSED_OTHER_
TRADITION_DIRECTIVE (Entry 59's own directive fix, unchanged, imported
not retyped) for the draft, then the self-revision pass on every draft
regardless of whether it happened to leak (measuring the mechanism
itself, not gated on a pre-check of which drafts need it - matches how
it would actually run in production, where the extra call is unconditional
on every other_tradition turn, not conditional on a leak already being
known).

Reports: cost first: leaks/20 beside the three already measured (3, 2,
2, 4 - current-directive, proposed-directive-alone, D1, D2); how often
the revision pass actually changed the text (trimmed something) vs left
it untouched; and, by hand-reading revised against draft for every run,
whether any run lost a true, record-supported detail (over-trimming) -
not just whether the known leak shape disappeared.

Run: python3 -m engine.m4.reports.r38_self_revision_measure --region us-east-1
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
from engine.m4.generation import stream_voice_turn
from engine.m4.reports.r39_generation_side_measure import (
    MESSAGE,
    PROPOSED_OTHER_TRADITION_DIRECTIVE,
    build_evidence_and_message,
)
from engine.provider import guard
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import SONNET_4_5_PRICE_TABLE

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORTS_DIR = pathlib.Path(__file__).resolve().parent

REVISION_INSTRUCTION = (
    "REVISION PASS - not a new question, and not addressed to the participant. You wrote the draft answer "
    "below to the participant's question about the Donatists. Review it against the real, full text of "
    "every record you tagged in it, given in full below. For each TAGGED sentence: keep only what that "
    "record actually says, or a fair paraphrase of it - trim any specific detail the record does not give, "
    "even if you believe it to be true. Do not add anything. Do not add, remove, or change any [[tag]]. Do "
    "not touch any UNTAGGED sentence at all, even to reword it. Return the complete revised answer, in the "
    "exact same format as the draft (the same tag grammar, the same structure), and nothing else - no "
    "preamble, no explanation of what you changed.\n\n"
    "YOUR DRAFT:\n{draft}\n\n"
    "THE RECORDS YOU TAGGED, IN FULL:\n{records_block}"
)


def _full_text_for_record(record: dict) -> str:
    return ev._head_text(record)


def build_revision_message(*, draft_text: str, tagged_record_ids: list[str], repository_records: dict[str, dict]) -> str:
    lines = []
    for rid in tagged_record_ids:
        record = repository_records.get(rid)
        if record is None:
            continue
        lines.append(f"[[{rid}]]: {_full_text_for_record(record)}")
    records_block = "\n\n".join(lines)
    return REVISION_INSTRUCTION.format(draft=draft_text, records_block=records_block)


def run(region: str, n: int = 20) -> dict:
    model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    client = make_client(region)
    user_message, ctx = build_evidence_and_message("alx")
    repository_records = ctx["repository_records"]
    world = ctx["world"]

    usage_records: list = []
    runs = []
    for i in range(n):
        # Draft
        last_error = None
        for attempt, delay in enumerate((0, 2, 4, 8)):
            if delay:
                time.sleep(delay)
            draft_outcome = stream_voice_turn(
                client, model_id, system_prompt=world.prompt_text, turn_directive=PROPOSED_OTHER_TRADITION_DIRECTIVE,
                message=user_message, history=None, timeout=90.0,
            )
            if draft_outcome.status == "ok":
                break
            last_error = draft_outcome
        else:
            draft_outcome = last_error
        if draft_outcome.status != "ok":
            raise RuntimeError(f"draft call {i} failed: {draft_outcome.status} {draft_outcome.value}")
        if draft_outcome.raw_usage is not None:
            usage_records.append(normalize_usage(draft_outcome.raw_usage))
        draft_raw = draft_outcome.value.text
        draft_tagged_text, _truncated = gn._drop_truncated_tail(draft_raw)
        draft_parsed = gn.parse_tagged(draft_tagged_text)
        draft_tagged_sentences = [{"sentence": s["text"], "tags": s["tags"]} for s in draft_parsed if s["tags"]]
        tagged_record_ids = sorted({rid for s in draft_tagged_sentences for rid in s["tags"]})

        # Self-revision (unconditional - every run, not just leaking ones)
        revision_message = build_revision_message(
            draft_text=draft_raw, tagged_record_ids=tagged_record_ids, repository_records=repository_records,
        )
        last_error = None
        for attempt, delay in enumerate((0, 2, 4, 8)):
            if delay:
                time.sleep(delay)
            revised_outcome = stream_voice_turn(
                client, model_id, system_prompt=world.prompt_text, turn_directive=None,
                message=revision_message, history=None, timeout=90.0,
            )
            if revised_outcome.status == "ok":
                break
            last_error = revised_outcome
        else:
            revised_outcome = last_error
        if revised_outcome.status != "ok":
            raise RuntimeError(f"revision call {i} failed: {revised_outcome.status} {revised_outcome.value}")
        if revised_outcome.raw_usage is not None:
            usage_records.append(normalize_usage(revised_outcome.raw_usage))
        revised_raw = revised_outcome.value.text
        revised_tagged_text, _truncated2 = gn._drop_truncated_tail(revised_raw)
        revised_parsed = gn.parse_tagged(revised_tagged_text)
        revised_tagged_sentences = [{"sentence": s["text"], "tags": s["tags"]} for s in revised_parsed if s["tags"]]

        runs.append({
            "run": i,
            "tagged_record_ids": tagged_record_ids,
            "draft_raw_text": draft_raw,
            "draft_tagged_sentences": draft_tagged_sentences,
            "revised_raw_text": revised_raw,
            "revised_tagged_sentences": revised_tagged_sentences,
            "changed": draft_raw.strip() != revised_raw.strip(),
        })
        time.sleep(0.4)

    total_dollars = sum((estimate_cost(u, SONNET_4_5_PRICE_TABLE).dollars or 0.0) for u in usage_records)

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "model_id": model_id,
        "message": MESSAGE,
        "directive": PROPOSED_OTHER_TRADITION_DIRECTIVE,
        "revision_instruction_template": REVISION_INSTRUCTION,
        "n": n,
        "calls_made": len(usage_records),
        "total_dollars": round(total_dollars, 4),
        "runs": runs,
    }


def main():
    parser = argparse.ArgumentParser()
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    parser.add_argument("--n", type=int, default=20)
    args = parser.parse_args()

    print(
        f"About to make {args.n * 2} live Sonnet 4.5 calls "
        f"({args.n} drafts + {args.n} self-revision passes). Estimated cost: ~$2-4 - proceeding.",
        flush=True,
    )
    report = run(args.region, n=args.n)
    out_path = REPORTS_DIR / f"r38-self-revision-measure-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    changed_count = sum(1 for r in report["runs"] if r["changed"])
    print(f"Real cost: ${report['total_dollars']} ({report['calls_made']} calls)")
    print(f"Revision pass changed the text in {changed_count}/{report['n']} runs")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")
    print("Next: hand-read every draft/revised pair and record leak + over-trim verdicts.")


if __name__ == "__main__":
    main()
