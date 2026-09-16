"""A real, billed live run against two real world packages (alx and ijc,
chosen for contrast in system-prompt size), priced against Anthropic's
published rate card. Like engine/provider/preflight.py and
engine/m4/live_turn_run.py, a by-hand, credentialed run - not a CI job.

Where those two scripts measure token counts or turn behavior but discard
the usage, this script is the missing third piece: it captures the real
UsageRecords engine.m4.turn.run_turn already produces, persists them
through engine.m8.log_store, summarizes them through engine.m8.summary,
and prices them through engine.m8.cost - the first time all three M8
pieces and a real price table are run together end to end.

PRICE SOURCE, stated plainly (spec principle 13's own requirement - a price
table must name where its numbers came from): Anthropic's own published API
rate card (platform.claude.com/docs/en/about-claude/pricing, fetched
2026-08-25) for Claude Sonnet 4.5 and Claude Haiku 4.5. AWS Bedrock's own
pricing page could not be fetched directly in this environment (network
egress to aws.amazon.com is blocked here) - Bedrock has historically
mirrored Anthropic's direct per-token rates for the same models, but that
has NOT been independently re-verified against Bedrock's own page for this
report. Treat these figures as published-rate, not invoice-reconciled -
the same distinction cost.py's own docstring draws.
"""
import argparse
import json
import sys
import tempfile
from pathlib import Path

from engine.m1.registry import load_registry
from engine.m4.turn import run_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import PriceTable, dollars_per_hour, estimate_cost
from engine.m8.log_store import UsageLogStore
from engine.m8.summary import summarize_session
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "live-cost-report.json"

PRICE_TABLE_SOURCE = (
    "Anthropic published API rate card (platform.claude.com/docs/en/about-claude/pricing, "
    "fetched 2026-08-25); Bedrock's own pricing page was not independently fetchable in this "
    "environment (egress to aws.amazon.com blocked) - Bedrock has historically mirrored "
    "Anthropic's direct per-token rates for the same models, not independently re-verified here"
)

SONNET_4_5_PRICE_TABLE = PriceTable(
    input_per_token=3.00 / 1_000_000,
    output_per_token=15.00 / 1_000_000,
    cache_write_per_token=3.75 / 1_000_000,  # 5-minute cache write (Bedrock's own default TTL)
    cache_read_per_token=0.30 / 1_000_000,
    source=PRICE_TABLE_SOURCE,
)
HAIKU_4_5_PRICE_TABLE = PriceTable(
    input_per_token=1.00 / 1_000_000,
    output_per_token=5.00 / 1_000_000,
    cache_write_per_token=1.25 / 1_000_000,
    cache_read_per_token=0.10 / 1_000_000,
    source=PRICE_TABLE_SOURCE,
)

WORLD_KEYS = ["alx", "ijc"]  # contrast in system-prompt size: alx is the largest world in the registry, ijc a mid-sized one

TURNS = [
    "Who was Jesus to your people?",
    "What does your community actually believe happens at the Eucharist?",
]


def _price_for_call_kind(call_kind: str) -> PriceTable:
    # voice_generation* is Sonnet-class; safety_call/reader_call are Haiku-class (spec, Artifact-4)
    return HAIKU_4_5_PRICE_TABLE if call_kind in ("safety_call", "reader_call") else SONNET_4_5_PRICE_TABLE


def run(region: str) -> dict:
    registry = load_registry()
    loader = LazyWorldLoader()
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    with tempfile.TemporaryDirectory() as tmp:
        store = UsageLogStore(Path(tmp) / "live-cost-run-usage.db")
        per_world = {}

        for world_key in WORLD_KEYS:
            entry = registry[world_key]
            world, _timing = loader.load(
                world_key, package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
            )
            session_id = f"cost-study-{world_key}"
            per_turn = []

            for i, message in enumerate(TURNS):
                result = run_turn(
                    session_id=session_id,
                    voice_client=client,
                    voice_model_id=voice_model_id,
                    safety_client=client,
                    safety_model_id=safety_model_id,
                    world=world,
                    participant_message=message,
                    pressed={},
                    anachronistic_term_ids=set(),
                )
                for rec in result.usage_records:
                    store.append(rec)
                turn_dollars = sum(
                    estimate_cost(rec.usage, _price_for_call_kind(rec.call_kind)).dollars for rec in result.usage_records
                )
                per_turn.append(
                    {
                        "turn_index": i,
                        "message": message,
                        "routing_action": result.routing_action,
                        "call_count": len(result.usage_records),
                        "by_call_kind": {rec.call_kind: rec.model_id for rec in result.usage_records},
                        "turn_dollars": turn_dollars,
                    }
                )

            records = store.read_for_session(session_id)
            summary = summarize_session(records)
            session_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in records)
            per_world[world_key] = {
                "session_id": session_id,
                "turns": per_turn,
                "session_summary": {
                    "call_count": summary.call_count,
                    "input_tokens": summary.input_tokens,
                    "output_tokens": summary.output_tokens,
                    "cache_creation_input_tokens": summary.cache_creation_input_tokens,
                    "cache_read_input_tokens": summary.cache_read_input_tokens,
                    "by_call_kind": summary.by_call_kind,
                },
                "session_dollars": session_dollars,
                "dollars_per_turn": session_dollars / len(TURNS),
                "dollars_per_participant_hour": dollars_per_hour(session_dollars / len(TURNS)),
            }

    all_turn_dollars = [t["turn_dollars"] for w in per_world.values() for t in w["turns"]]
    report = {
        "voice_model_id": voice_model_id,
        "safety_model_id": safety_model_id,
        "region": region,
        "price_table_source": PRICE_TABLE_SOURCE,
        "price_tables": {
            "sonnet_4_5": {k: v for k, v in vars(SONNET_4_5_PRICE_TABLE).items() if k != "source"},
            "haiku_4_5": {k: v for k, v in vars(HAIKU_4_5_PRICE_TABLE).items() if k != "source"},
        },
        "worlds": per_world,
        "overall_mean_dollars_per_turn": sum(all_turn_dollars) / len(all_turn_dollars),
        "overall_mean_dollars_per_participant_hour": dollars_per_hour(sum(all_turn_dollars) / len(all_turn_dollars)),
        "note": (
            "Priced against a published rate card, not a reconciled AWS invoice - spec principle 13's "
            "distinction. This is a small, real, billed run (2 worlds x 2 turns x voice+safety+reader "
            "calls) - not a statistically powered sample; treat as an order-of-magnitude first look, not "
            "a final production cost figure."
        ),
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", required=True)
    args = parser.parse_args()

    report = run(args.region)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
