"""Table parity for other-tradition handling (reviewer thread, 2026-09-23,
item 5): "re-run the Table battery's other-tradition probes (or add them
if the Table battery has none) and report step-ins, self-revision counts,
and one full transcript in the PR body." engine.m4.live_table_battery has
no other_tradition probe at all - this is a small, focused, standalone
live battery (real, billed Bedrock calls) rather than folding a new probe
shape into that file's own large multi-session L1-L6 orchestration.

Two probes, each its own fresh 2-seat table session, a directly-addressed
seat asked about a real, named, unseated tradition (the same
"What was your relationship with X?" shape
engine.m4.live_uncited_claims_battery._other_tradition_turn already
proved reliably classifies other_tradition with the real reader):

  OT1 (alx, no evidence) - alx's own records never mention Donatism
    (Decision-Log.md Entry 66/#436's worked example) - the honest-limit
    branch.
  OT2 (ijc, has evidence) - ijc's own real records (ijc.quote.compelled-
    to-come-in, ijc.story.emperor-builds-another-basilica) genuinely name
    Donatism (#440's own fix) - the records branch.

Both probes are also is_other_tradition_first_ask turns whose draft
carries a tag (grounded_sentence-shaped output is not scripted here -
the voice call is real and live), so R38 self-revision fires on both by
the same rule engine/m4/tests/test_turn.py and engine/api/tests/
test_table_api.py already pin at the deterministic level. This live run
is what proves the WIRING (engine.api.table_wiring._advance_open_round)
actually reaches production, not the mechanism itself (already measured
in PR #436/#445).

Run: python3 -m engine.m4.reports.table_other_tradition_battery --region us-east-1
"""
import argparse
import json
import pathlib
import sys
import tempfile
import time
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.api.table_wiring import create_table_session, handle_table_message, continue_table_round
from engine.api.wiring import _load_world
from engine.m1.registry import load_registry
from engine.m4 import evidence as ev
from engine.m4.store import Store
from engine.m4.turn import R26_HONEST_LIMIT_SENTENCE
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE, SONNET_4_5_PRICE_TABLE
from engine.m8.log_store import UsageLogStore
from engine.provider.bedrock import make_client, resolve_model_id

REPORT_PATH = pathlib.Path(__file__).resolve().parent / "table-other-tradition-battery-2026-09-23.json"


def _price_for_call_kind(call_kind: str):
    return HAIKU_4_5_PRICE_TABLE if call_kind in ("safety_call", "reader_call", "turn_selector") else SONNET_4_5_PRICE_TABLE


def _drive_round(call_kwargs, text):
    results = [handle_table_message(**call_kwargs, text=text)]
    while results[-1].round_open:
        results.append(continue_table_round(**{k: v for k, v in call_kwargs.items() if k != "text"}))
    return results


def _run_probe(*, probe_id, world_key, other_seat_key, card_name, client, voice_model_id, safety_model_id, registry, loader):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix=f"cic-table-ot-battery-{probe_id}-"))
    store, usage_store = Store(tmp / "events.db"), UsageLogStore(tmp / "usage.db")
    world = _load_world(loader, registry, world_key)
    name = world.frame["representative"]["name"]
    session_id, _code = create_table_session(store=store, world_loader=loader, registry=registry, world_keys=[world_key, other_seat_key])
    call_kwargs = dict(
        store=store, usage_store=usage_store, world_loader=loader, registry=registry,
        voice_client=client, voice_model_id=voice_model_id,
        safety_client=client, safety_model_id=safety_model_id, session_id=session_id,
    )
    message = f"{name}, what was your relationship with {card_name}?"
    results = _drive_round(call_kwargs, message)
    r0 = results[0]
    voice = r0.voice
    self_revision_meta = (voice or {}).get("attempts_meta", {}).get("self_revision", {})
    text = (voice or {}).get("text") or ""
    stepped_in = (
        R26_HONEST_LIMIT_SENTENCE.lower() in text.lower()
        or bool((voice or {}).get("citations"))
    )
    records = usage_store.read_for_session(session_id)
    dollars = sum((estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars or 0.0) for r in records)
    return {
        "probe_id": probe_id,
        "world_key": world_key,
        "routing_action": r0.routing_action,
        "out_of_scope_class": None,  # not surfaced on TableMessageResult; routing_reason carries it in text form
        "routing_reason": r0.routing_reason,
        "voice_speaker": (voice or {}).get("speaker"),
        "voice_text": text,
        "citations": (voice or {}).get("citations", []),
        "stepped_in": stepped_in,
        "self_revision": self_revision_meta,
        "calls_made": len(records),
        "dollars": round(dollars, 4),
        "message": message,
    }


def run(region: str) -> dict:
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)
    registry = load_registry()
    loader = LazyWorldLoader()

    don_card_name = registry["don"]["card_name"]

    probes = []
    for probe_id, world_key, other_seat in [("OT1-no-evidence", "alx", "desert"), ("OT2-has-evidence", "ijc", "desert")]:
        print(f"Running {probe_id} ({world_key})...", flush=True)
        probe = _run_probe(
            probe_id=probe_id, world_key=world_key, other_seat_key=other_seat, card_name=don_card_name,
            client=client, voice_model_id=voice_model_id, safety_model_id=safety_model_id, registry=registry, loader=loader,
        )
        probes.append(probe)
        print(f"  {probe_id}: stepped_in={probe['stepped_in']} self_revision.ran={probe['self_revision'].get('ran')} "
              f"self_revision.changed={probe['self_revision'].get('changed')} ${probe['dollars']}", flush=True)

    total_dollars = round(sum(p["dollars"] for p in probes), 4)
    total_calls = sum(p["calls_made"] for p in probes)
    step_in_count = sum(1 for p in probes if p["stepped_in"])
    self_revision_ran_count = sum(1 for p in probes if p["self_revision"].get("ran"))
    self_revision_changed_count = sum(1 for p in probes if p["self_revision"].get("changed"))

    return {
        "asof": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "total_dollars": total_dollars,
        "total_calls": total_calls,
        "step_ins": f"{step_in_count}/{len(probes)}",
        "self_revision_ran": f"{self_revision_ran_count}/{len(probes)}",
        "self_revision_changed": f"{self_revision_changed_count}/{len(probes)}",
        "probes": probes,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", default="us-east-1")
    args = parser.parse_args()
    start = time.monotonic()
    report = run(args.region)
    elapsed = time.monotonic() - start
    REPORT_PATH.write_text(json.dumps(report, indent=2))
    print(f"\nReal cost: ${report['total_dollars']} ({report['total_calls']} calls), {elapsed:.1f}s")
    print(f"Step-ins: {report['step_ins']}  Self-revision ran: {report['self_revision_ran']}  changed: {report['self_revision_changed']}")
    print(f"Report: {REPORT_PATH}")
