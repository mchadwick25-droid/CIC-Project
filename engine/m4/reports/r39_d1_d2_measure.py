"""R39, the reviewer's own follow-up (relayed 2026-09-23) after the first
generation-side measurement (r39_generation_side_measure.py) showed the
proposed directive alone is a partial fix, not a real one (3 of 20 leaks
under the current directive, 2 of 20 under the proposed one - the exact
traditor detail recurred twice under the "fixed" directive). The
reviewer's own diagnosis, read directly off that measurement's own JSON:
`evidence_offers_church_failure` is False and
`prompt_contains_church_failure_text` is True. The voice tagged a record
that was never in the turn's own assembled ground at all - it reached
into the compiled world prompt (the full system context, always present)
and filled the missing detail from memory rather than from anything this
turn actually offered it.

Two more conditions, same worked example (Theon, "What was your
relationship with the Donatists?"), same world (alx), same model, same
20-per-condition count, hand-read the same way as the first measurement:

  D1. The proposed directive (r39_generation_side_measure's own
      PROPOSED_OTHER_TRADITION_DIRECTIVE, imported unchanged) PLUS
      alx.dw.church-failure actually offered in this turn's own evidence
      block - not just its usual one-sentence head (render_evidence_block's
      own first-sentence truncation), but its real, full `text` field
      verbatim. The retrieval fix under test: if the record the question
      most needs is genuinely in front of the voice, does it paraphrase
      from that text instead of reaching into memory for a detail this
      turn never actually offered it?

  D2. D1 plus one added directive line, stated plainly rather than
      implied: "Tag only records offered in this turn's own evidence
      block above; a record you remember from elsewhere, even if it is
      real and even if it is in your own world's compiled prompt, is not
      ground for THIS turn." Ground and prompt are not the same channel
      (render_evidence_block's own docstring already makes exactly this
      distinction for a different confusion - AVAILABLE is not the same
      as ALREADY SAID; this is the same shape of confusion, AVAILABLE
      ANYWHERE in the prompt is not the same as OFFERED THIS TURN).

Run: python3 -m engine.m4.reports.r39_d1_d2_measure --region us-east-1
"""
import argparse
import json
import pathlib
import sys
from datetime import date, datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1.registry import load_registry
from engine.m4 import evidence as ev
from engine.m4.reports.net_remainder_measure import latest_complete_package
from engine.m4.reports.r39_generation_side_measure import (
    MESSAGE,
    PROPOSED_OTHER_TRADITION_DIRECTIVE,
    build_evidence_and_message,
    run_batch,
)
from engine.m4.world_loader import LazyWorldLoader
from engine.provider import guard
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import SONNET_4_5_PRICE_TABLE

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORTS_DIR = pathlib.Path(__file__).resolve().parent

D2_ADDED_LINE = (
    " Tag only records offered in this turn's own evidence block above; a record you remember from "
    "elsewhere, even if it is real and even if it is in your own world's compiled prompt, is not ground "
    "for THIS turn."
)
D2_DIRECTIVE = PROPOSED_OTHER_TRADITION_DIRECTIVE + D2_ADDED_LINE


def build_evidence_with_church_failure_offered(world_key: str, record_id: str = "alx.dw.church-failure") -> tuple[str, dict]:
    """Same evidence assembly r39_generation_side_measure.build_evidence_and_message
    already does for this exact message (confirmed there: the real cell-match
    pipeline does not select this record for this message) - plus one line
    appended after the normal block, carrying `record_id`'s own real, full
    `text` field verbatim rather than render_evidence_block's usual
    first-sentence truncation. The retrieval fix under test, simulated
    directly rather than by changing the retrieval pipeline itself (report-
    only measurement, same discipline as r39_generation_side_measure)."""
    registry = load_registry()
    C = latest_complete_package(world_key)
    manifest_hash = registry[world_key]["package"]["manifest_hash"]
    loader = LazyWorldLoader()
    world, _timing = loader.load(world_key, package_dir=C, expected_manifest_hash=manifest_hash)
    repository_records = ev.repository_records_by_id(world.repository)

    base_message, base_ctx = build_evidence_and_message(world_key)
    record = repository_records[record_id]
    full_text = (record.get("text") or "").strip()
    offered_line = f"- [[{record_id}]] doctrinal_witness (offered in full, not head-truncated) — {full_text}\n"
    # base_message is "<evidence_block>\n<MESSAGE>" (build_evidence_and_message's
    # own shape) - insert the new line at the end of the evidence block,
    # immediately before the message line, rather than appending after it.
    evidence_block, _, message_line = base_message.rpartition("\n")
    augmented_message = f"{evidence_block}\n{offered_line}{message_line}"

    return augmented_message, {
        **base_ctx,
        "evidence_offers_church_failure_full_text": True,
        "offered_line": offered_line,
    }


def run(region: str, n_per_condition: int = 20) -> dict:
    model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    client = make_client(region)
    user_message, ctx = build_evidence_with_church_failure_offered("alx")

    usage_records: list = []
    d1_results = run_batch(
        client, model_id, world=ctx["world"], user_message=user_message,
        directive_text=PROPOSED_OTHER_TRADITION_DIRECTIVE, n=n_per_condition, usage_records=usage_records,
    )
    d2_results = run_batch(
        client, model_id, world=ctx["world"], user_message=user_message,
        directive_text=D2_DIRECTIVE, n=n_per_condition, usage_records=usage_records,
    )

    total_dollars = sum((estimate_cost(u, SONNET_4_5_PRICE_TABLE).dollars or 0.0) for u in usage_records)

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "model_id": model_id,
        "message": MESSAGE,
        "offered_line": ctx["offered_line"],
        "user_message": user_message,
        "d1_directive": PROPOSED_OTHER_TRADITION_DIRECTIVE,
        "d2_directive": D2_DIRECTIVE,
        "n_per_condition": n_per_condition,
        "calls_made": len(usage_records),
        "total_dollars": round(total_dollars, 4),
        "d1_runs": d1_results,
        "d2_runs": d2_results,
    }


def main():
    parser = argparse.ArgumentParser()
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    parser.add_argument("--n", type=int, default=20)
    args = parser.parse_args()

    print(
        f"About to make {args.n * 2} live Sonnet 4.5 voice-generation calls "
        f"({args.n} D1 + {args.n} D2). Estimated cost: ~$2-4 - proceeding.",
        flush=True,
    )
    report = run(args.region, n_per_condition=args.n)
    out_path = REPORTS_DIR / f"r39-d1-d2-measure-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    print(f"Real cost: ${report['total_dollars']} ({report['calls_made']} calls)")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")
    print("Next: hand-read every tagged sentence in d1_runs/d2_runs and record verdicts.")


if __name__ == "__main__":
    main()
