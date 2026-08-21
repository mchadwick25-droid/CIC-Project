"""Live evidence for stage-6's remaining gate items, run against the real
Bedrock account and the real fixture world package: per-session usage
attribution end to end through the actual M4 turn loop (not a synthetic
call), and "zero unattributed calls" checked over a real logged batch, not
merely asserted about the type. Every real call this script triggers is
also parity-checked inline (engine.m4.turn's own wiring, not a separate
step) - a divergence would have raised before this script could finish.

Real, billed Bedrock calls - by-hand, credentialed, not a CI job.
"""
import argparse
import json
import sys
import tempfile
from pathlib import Path

import yaml

from engine.m4.turn import run_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.log_store import UsageLogStore
from engine.m8.summary import summarize_session
from engine.m8.usage import zero_unattributed
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
WORLDS_YAML = REPO_ROOT / "records" / "worlds.yaml"
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "live-attribution-report.json"
SESSION_ID = "evidence-session-stage6"


def run(region: str) -> dict:
    registry = yaml.safe_load(WORLDS_YAML.read_text(encoding="utf-8"))
    entry = registry["worlds"]["fix"]
    loader = LazyWorldLoader()
    world, _timing = loader.load(
        "fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )

    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    with tempfile.NamedTemporaryFile(suffix=".sqlite3") as tmp:
        store = UsageLogStore(Path(tmp.name))

        result = run_turn(
            session_id=SESSION_ID,
            voice_client=client,
            voice_model_id=voice_model_id,
            safety_client=client,
            safety_model_id=safety_model_id,
            world=world,
            participant_message="Who was Jesus to your people?",
            pressed={},
            anachronistic_term_ids=set(),
        )
        for record in result.usage_records:
            store.append(record)

        session_records = store.read_for_session(SESSION_ID)
        summary = summarize_session(session_records)

    report = {
        "session_id": SESSION_ID,
        "voice_model_id": voice_model_id,
        "safety_model_id": safety_model_id,
        "region": region,
        "routing_action": result.routing_action,
        "call_count": summary.call_count,
        "by_call_kind": summary.by_call_kind,
        "token_totals": {
            "input_tokens": summary.input_tokens,
            "output_tokens": summary.output_tokens,
            "cache_creation_input_tokens": summary.cache_creation_input_tokens,
            "cache_read_input_tokens": summary.cache_read_input_tokens,
        },
        "zero_unattributed_calls": zero_unattributed(session_records),
        "parity_checked_inline": True,
        "cache_write_engaged_this_run": summary.cache_creation_input_tokens > 0,
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
    return 0 if report["zero_unattributed_calls"] else 1


if __name__ == "__main__":
    sys.exit(main())
