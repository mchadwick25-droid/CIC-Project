"""Live evidence for the Table (Artifact-7 SS8 item 4): a real multi-voice
round end to end against real, committed formation-world packages - real
gate calls, real turn-selector calls, real voice generations, the
grounding net over real model output, per-world usage attribution read
back from the usage store. Real, billed Bedrock calls - like
engine/provider/preflight.py and engine/m4/live_turn_run.py, a by-hand,
credentialed run under explicit per-run authorization, never a CI
job.

Deliberately drives engine.api.table_wiring itself (create_table_session /
handle_table_message / continue_table_round) against a throwaway store,
not a re-implementation - the smoke run and a participant's real table
session execute the same code path, so they cannot disagree. The stores
live in a temp directory and are discarded; the checked-in artifact is the
report JSON alone.

Reports token counts and latency, never $ figures (spec principle 13: no
price is quoted until measured against a reconciled AWS invoice).
"""
import argparse
import json
import sys
import tempfile
import time
from collections import defaultdict
from pathlib import Path

from engine.api.table_wiring import (
    continue_table_round,
    create_table_session,
    handle_table_message,
)
from engine.m1.registry import load_registry
from engine.m4.output_check import find_shipped_defects
from engine.m4.projection import project_fresh
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.log_store import UsageLogStore
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "live-table-report.json"

# The two default messages: one genuinely open to every seated world (the
# "what do each of you think" shape the Table Process doc's breadth-of-voice
# guidance exists for), then a follow-up that only works if cross-voice
# memory works - it asks the voices about what was just said at THIS table.
DEFAULT_MESSAGES = [
    "How should I pray when God feels silent?",
    "You have each just spoken of prayer in your own way - what would each of you most want me to carry with me from what the other said?",
]


def _turn_summary(result) -> dict:
    voice = result.voice
    summary = {
        "round_no": result.round_no,
        "position": result.position,
        "round_open": result.round_open,
        "routing_action": result.routing_action,
        "turn_selected": result.turn_selected,
        "facilitator_kinds": [f["kind"] for f in result.facilitator],
    }
    if voice:
        sentences = voice["grounding"]["sentences"] if voice.get("grounding") else []
        summary["voice"] = {
            "speaker": voice["speaker"],
            "chars": len(voice["text"]),
            "words": len(voice["text"].split()),
            "citations": len(voice["citations"]),
            "cited_record_ids": sorted({rid for c in voice["citations"] for rid in c["record_ids"]}),
            "sentences_checked": len(sentences),
            "sentences_withheld": sum(1 for s in sentences if s["verdict"] == "withhold"),
            "withhold_reasons": [s["why"] for s in sentences if s["verdict"] == "withhold"],
            "degraded_by_net": voice.get("degraded_by_net", False),
            "output_defects": voice.get("output_defects", []),
            "text": voice["text"],
            # The transparency apparatus, whole (the first three reports
            # turned out to have summarized it away, when it needs to be
            # visible): per-sentence citations with their
            # resolved sources, lexicon glosses, figure bridges, quote
            # offers. This is participant-facing data the engine produces
            # on every turn - a run report that drops it hides the
            # system's own best evidence.
            "citations_full": voice["citations"],
            "glosses": voice.get("glosses", []),
            "figures_used": voice.get("figures_used", []),
            "quote_offers": voice.get("quote_offers", []),
        }
    return summary


def run(region: str, *, world_keys: list[str], messages: list[str]) -> dict:
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)  # voice stays Sonnet-class (spec)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)  # gate + selector stay Haiku-class (Artifact-4 / Artifact-7 SS5)
    client = make_client(region)
    registry = load_registry()

    tmp = Path(tempfile.mkdtemp(prefix="cic-live-table-"))
    store = Store(tmp / "events.db")
    usage_store = UsageLogStore(tmp / "usage.db")
    loader = LazyWorldLoader()

    session_id, _code = create_table_session(store=store, world_loader=loader, registry=registry, world_keys=world_keys)

    call_kwargs = dict(
        store=store, usage_store=usage_store, world_loader=loader, registry=registry,
        voice_client=client, voice_model_id=voice_model_id,
        safety_client=client, safety_model_id=safety_model_id, session_id=session_id,
    )

    rounds = []
    for message in messages:
        turns = []
        start = time.monotonic()
        result = handle_table_message(**call_kwargs, text=message)
        turns.append({**_turn_summary(result), "latency_s": round(time.monotonic() - start, 1)})
        print(f"  round {result.round_no} pos {result.position}: {result.turn_selected and result.turn_selected['world_key']}"
              f" ({turns[-1]['latency_s']}s)", flush=True)
        while result.round_open:
            start = time.monotonic()
            result = continue_table_round(**call_kwargs)
            turns.append({**_turn_summary(result), "latency_s": round(time.monotonic() - start, 1)})
            label = result.turn_selected["world_key"] if result.turn_selected else "(closed)"
            print(f"  round {result.round_no} pos {result.position}: {label} ({turns[-1]['latency_s']}s)", flush=True)
        rounds.append({"message": message, "turns": turns, "committed_turn_no": result.turn_no})

    # Dominance across the whole conversation (Table Process V1.0 SS3's
    # cumulative word-share; 65% is the single-Representative threshold).
    state = project_fresh(session_id, store)
    words_by_speaker = defaultdict(int)
    for t in state.transcript:
        if t.get("speaker") not in ("participant", "facilitator", None):
            words_by_speaker[t["speaker"]] += len((t.get("text") or "").split())
    total_words = sum(words_by_speaker.values()) or 1
    dominance = {k: round(v / total_words, 2) for k, v in sorted(words_by_speaker.items())}

    # Usage, read back from the store the run attributed into - token
    # counts only, aggregated per (call_kind, world_key).
    usage = defaultdict(lambda: {"calls": 0, "input_tokens": 0, "output_tokens": 0, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0})
    for rec in usage_store.read_for_session(session_id):
        bucket = usage[f"{rec.call_kind}:{rec.world_key or '-'}"]
        bucket["calls"] += 1
        for field in ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"):
            bucket[field] += getattr(rec.usage, field, 0) or 0

    # The isolation sweep, run live exactly as the CI suite runs it hermetic:
    # every surviving citation of every voice turn resolves in the speaker's
    # own repository.
    from engine.api.wiring import _load_world
    from engine.m4 import evidence

    repos = {k: set(evidence.repository_records_by_id(_load_world(loader, registry, k).repository)) for k in world_keys}
    isolation_violations = []
    for t in state.transcript:
        speaker = t.get("speaker")
        if speaker in repos:
            cited = {rid for c in (t.get("citations") or []) for rid in c.get("record_ids", [])}
            outside = cited - repos[speaker]
            if outside:
                isolation_violations.append({"speaker": speaker, "outside_ids": sorted(outside)})

    return {
        "region": region,
        "voice_model_id": voice_model_id,
        "safety_model_id": safety_model_id,
        "world_keys": world_keys,
        "rounds": rounds,
        "dominance_word_share": dominance,
        "usage_token_counts": dict(sorted(usage.items())),
        "isolation_violations": isolation_violations,
        "note": "token counts only - no $ figure until reconciled against an AWS invoice (spec principle 13)",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", required=True)
    parser.add_argument("--worlds", default="alx,desert", help="2-3 comma-separated world keys (default alx,desert)")
    parser.add_argument("--message", action="append", help="participant message (repeatable); defaults to the two-message script")
    parser.add_argument("--out", default=str(REPORT_PATH))
    args = parser.parse_args()

    world_keys = [k.strip() for k in args.worlds.split(",") if k.strip()]
    messages = args.message or DEFAULT_MESSAGES
    print(f"LIVE, BILLED run: table {world_keys}, {len(messages)} message(s), region {args.region}", flush=True)
    report = run(args.region, world_keys=world_keys, messages=messages)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"report written: {out}")
    print(f"isolation violations: {len(report['isolation_violations'])}")

    # H-3 (witt go-live adversarial review, 2026-09-19) - see
    # engine.m4.output_check.find_shipped_defects for why this is checked
    # here rather than left to a reviewer reading the raw JSON.
    shipped_defects = find_shipped_defects(report)
    if shipped_defects:
        print(f"SHIPPED OUTPUT DEFECT(S): {len(shipped_defects)} - see output_defects in the report above", flush=True)
        for d in shipped_defects:
            print(f"  [round {d.get('round_no')} pos {d.get('position')}] {d.get('family')}: {d.get('finding')}", flush=True)

    return 0 if not report["isolation_violations"] and not shipped_defects else 1


if __name__ == "__main__":
    sys.exit(main())
