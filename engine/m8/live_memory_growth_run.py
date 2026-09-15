"""Follow-up to live_cost_run.py: does conversation memory (Program-Spec
M4's "full-session memory", engine.api.wiring.history_from_transcript) grow
cost as a session gets longer? engine.m4.generation.stream_voice_turn's own
docstring says history rides in `messages`, after the one cache breakpoint
on the static system prompt - meaning it is NOT itself cached, and
history_from_transcript replays the FULL transcript every turn, unlike the
old system's bounded window. This script measures that directly across a
real 6-turn session rather than estimating it from the code alone.

Same discipline as live_cost_run.py: real, billed calls; priced against
Anthropic's published rate card (same PRICE_TABLE_SOURCE), not a
reconciled AWS invoice.
"""
import argparse
import json
import sys
from pathlib import Path

from engine.m1.registry import load_registry
from engine.m4.turn import run_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE, PRICE_TABLE_SOURCE, SONNET_4_5_PRICE_TABLE, _price_for_call_kind
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "live-memory-growth-report.json"

WORLD_KEY = "alx"  # the largest world in the registry - the world where this effect would show most clearly

MESSAGES = [
    "Who was Jesus to your people?",
    "What does your community actually believe happens at the Eucharist?",
    "You mentioned the Eucharist - how does that connect to what you said about Jesus earlier?",
    "What would you say to someone who thinks all of this is just myth?",
    "How does someone actually join your community?",
    "What does your community believe happens to the soul after death?",
    "Who has the authority to teach in your community, and why?",
    "What's the hardest thing about holding to your faith in this time and place?",
    "How do you read scripture - is there more than one way to understand it?",
    "Looking back on everything we've talked about, what's the one thing you most want me to understand?",
]


def run(region: str) -> dict:
    registry = load_registry()
    entry = registry[WORLD_KEY]
    loader = LazyWorldLoader()
    world, _timing = loader.load(
        WORLD_KEY, package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )

    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    session_id = f"memory-growth-{WORLD_KEY}"
    history: list[dict] = []
    turns = []

    for i, message in enumerate(MESSAGES):
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
            history=history,
        )
        turn_dollars = sum(estimate_cost(rec.usage, _price_for_call_kind(rec.call_kind)).dollars for rec in result.usage_records)
        voice_records = [r for r in result.usage_records if r.call_kind == "voice_generation"]
        voice_usage = voice_records[0].usage if voice_records else None
        turns.append(
            {
                "turn_index": i,
                "message": message,
                "history_messages_sent": len(history),
                "voice_call_input_tokens": voice_usage.input_tokens if voice_usage else None,
                "voice_call_cache_read_tokens": voice_usage.cache_read_input_tokens if voice_usage else None,
                "voice_call_cache_write_tokens": voice_usage.cache_creation_input_tokens if voice_usage else None,
                "voice_call_output_tokens": voice_usage.output_tokens if voice_usage else None,
                "turn_dollars": turn_dollars,
            }
        )
        voice_text = (result.voice_event or {}).get("text") or ""
        history = [*history, {"role": "user", "content": message}, {"role": "assistant", "content": voice_text}]

    report = {
        "voice_model_id": voice_model_id,
        "safety_model_id": safety_model_id,
        "region": region,
        "world_key": WORLD_KEY,
        "price_table_source": PRICE_TABLE_SOURCE,
        "turns": turns,
        "note": (
            "One continuous 6-turn session, real history accumulated turn over turn exactly as "
            "engine.api.wiring.history_from_transcript would build it. voice_call_input_tokens is the "
            "uncached messages-array size (history + this turn's message) - if it grows turn over turn, "
            "that is conversation memory's own uncached cost growth, distinct from the cached system "
            "prompt (which stays flat and is reported separately as cache_write/cache_read tokens)."
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
