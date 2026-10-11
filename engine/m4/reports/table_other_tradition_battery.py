"""Table parity for other-tradition handling (reviewer thread, 2026-09-23,
item 5, plus round-1 review fixes): "re-run the Table battery's other-
tradition probes (or add them if the Table battery has none) and report
step-ins, self-revision counts, and one full transcript in the PR body."
engine.m4.live_table_battery has no other_tradition probe at all - this
is a small, focused, standalone live battery (real, billed Bedrock
calls) rather than folding a new probe shape into that file's own large
multi-session L1-L6 orchestration.

Three probes, each its own fresh 2-seat table session, a directly-
addressed seat asked about a real, named tradition (the same "What was
your relationship with X?" shape engine.m4.live_uncited_claims_battery.
_other_tradition_turn already proved reliably classifies other_
tradition with the real reader):

  OT1 (alx, unseated, no evidence) - alx's own records never mention
    Donatism (Decision-Log.md Entry 66/#436's worked example) - the
    honest-limit branch.
  OT2 (ijc, unseated, has evidence) - ijc's own real records (ijc.
    quote.compelled-to-come-in, ijc.story.emperor-builds-another-
    basilica) genuinely name Donatism (#440's own fix) - the records
    branch.
  OT3 (alx, SEATED, no evidence) - the round-1 review's own FIX 2:
    don is seated at this same table, so the fixed honest-limit
    sentence would be false (that tradition's own Representative sits
    right there) - the directive is suppressed entirely; the Table's
    own seat-to-seat clause governs instead.

All three are also is_other_tradition_first_ask turns whose draft
carries a tag (grounded_sentence-shaped output is not scripted here -
the voice call is real and live), so R38 self-revision fires on all
three by the same rule engine/m4/tests/test_turn.py and engine/api/
tests/test_table_api.py already pin at the deterministic level. This
live run is what proves the WIRING (engine.api.table_wiring._advance_
open_round) actually reaches production, not the mechanism itself
(already measured in PR #436/#445).

NAMING, corrected per round-1 review: "step-in" in this program means a
Facilitator takeover (the voice never speaks; a Facilitator turn
substitutes). What this battery measures is whether the other-
tradition DIRECTIVE fired for a seat's own turn - a different thing,
now named directive_fired throughout. facilitator_step_in is reported
separately and correctly: True only when the round's own routing never
reached a voice turn at all (etic_turn, a governed round, or similar).

MEASUREMENT, fixed in the same round-1 pass: directive_fired used to be
read back off the model's own prose ("does the answer contain the fixed
sentence, or does it have any citations at all?"). That is not ground
truth - an ordinary in-world answer always cites its own records for
reasons that have nothing to do with the other-tradition directive, so
the citations half of that check was a standing false positive on
exactly the turn OT3 exists to prove (the seated case, where the
directive is supposed to be suppressed). _run_probe now wraps engine.
m4.turn._other_tradition_directive itself (call-through, no behavior
change) and reads its real return value for the round's opening turn -
the one function whose return value the seated/repeat-turn/evidence/
default branches actually decide. directive_fired is that value's
presence, not an inference from what the voice went on to say.

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
from engine.m4 import turn as turn_module
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE, SONNET_4_5_PRICE_TABLE
from engine.m8.log_store import UsageLogStore
from engine.provider import guard
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

    # directive_fired ground truth: whether the other-tradition directive
    # text actually got built is a call-time fact of _other_tradition_
    # directive itself (engine/m4/turn.py), not something reliably read
    # back off the model's own prose. A surface-text heuristic ("does the
    # answer merely contain citations?") false-positives on any ordinary
    # cited answer, including OT3's own seated turn where the directive is
    # correctly suppressed - an ordinary in-world answer still cites its
    # own records for unrelated reasons. Wrap the real function (call-
    # through, no behavior change) to capture its actual return value per
    # call, in order; the first call belongs to this round's opening turn
    # (handle_table_message, i.e. r0) - the only turn this probe measures.
    captured_directives = []
    original_other_tradition_directive = turn_module._other_tradition_directive

    def _capturing_other_tradition_directive(*args, **kwargs):
        result = original_other_tradition_directive(*args, **kwargs)
        captured_directives.append(result)
        return result

    turn_module._other_tradition_directive = _capturing_other_tradition_directive
    try:
        results = _drive_round(call_kwargs, message)
    finally:
        turn_module._other_tradition_directive = original_other_tradition_directive

    r0 = results[0]
    voice = r0.voice
    self_revision_meta = (voice or {}).get("attempts_meta", {}).get("self_revision", {})
    text = (voice or {}).get("text") or ""
    opening_turn_directive_text = captured_directives[0] if captured_directives else None
    # directive_fired: did the opening turn (r0) actually carry other-
    # tradition directive text? Never "step-in" - that word means a
    # Facilitator takeover in this program, a different, separately-
    # reported thing (facilitator_step_in, below).
    directive_fired = opening_turn_directive_text is not None
    # A real Facilitator step-in: the round's own routing never reached
    # a voice turn at all (r0.voice is None whenever the opening routing
    # was governed/etic - engine.api.table_wiring._handle_table_message_
    # unlocked returns before _advance_open_round in that case).
    facilitator_step_in = voice is None
    records = usage_store.read_for_session(session_id)
    dollars = sum((estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars or 0.0) for r in records)
    return {
        "probe_id": probe_id,
        "world_key": world_key,
        "other_seat_key": other_seat_key,
        "routing_action": r0.routing_action,
        "routing_reason": r0.routing_reason,
        "voice_speaker": (voice or {}).get("speaker"),
        "voice_text": text,
        "citations": (voice or {}).get("citations", []),
        "directive_fired": directive_fired,
        "opening_turn_directive_text": opening_turn_directive_text,
        "facilitator_step_in": facilitator_step_in,
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

    # OT1/OT2: don unseated (the other seat is desert, which never
    # mentions Donatism either, so it can't accidentally supply
    # evidence). OT3 (FIX 2): don itself is the OTHER seat - seated.
    probe_specs = [
        ("OT1-unseated-no-evidence", "alx", "desert"),
        ("OT2-unseated-has-evidence", "ijc", "desert"),
        ("OT3-seated-no-evidence", "alx", "don"),
    ]

    probes = []
    for probe_id, world_key, other_seat in probe_specs:
        print(f"Running {probe_id} ({world_key}, other seat {other_seat})...", flush=True)
        probe = _run_probe(
            probe_id=probe_id, world_key=world_key, other_seat_key=other_seat, card_name=don_card_name,
            client=client, voice_model_id=voice_model_id, safety_model_id=safety_model_id, registry=registry, loader=loader,
        )
        probes.append(probe)
        print(f"  {probe_id}: directive_fired={probe['directive_fired']} facilitator_step_in={probe['facilitator_step_in']} "
              f"self_revision.ran={probe['self_revision'].get('ran')} self_revision.changed={probe['self_revision'].get('changed')} "
              f"${probe['dollars']}", flush=True)

    total_dollars = round(sum(p["dollars"] for p in probes), 4)
    total_calls = sum(p["calls_made"] for p in probes)
    directive_fired_count = sum(1 for p in probes if p["directive_fired"])
    facilitator_step_in_count = sum(1 for p in probes if p["facilitator_step_in"])
    self_revision_ran_count = sum(1 for p in probes if p["self_revision"].get("ran"))
    self_revision_changed_count = sum(1 for p in probes if p["self_revision"].get("changed"))

    return {
        "asof": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "total_dollars": total_dollars,
        "total_calls": total_calls,
        "directive_fired": f"{directive_fired_count}/{len(probes)}",
        "facilitator_step_in": f"{facilitator_step_in_count}/{len(probes)}",
        "self_revision_ran": f"{self_revision_ran_count}/{len(probes)}",
        "self_revision_changed": f"{self_revision_changed_count}/{len(probes)}",
        "probes": probes,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    guard.add_arguments(parser)
    parser.add_argument("--region", default="us-east-1")
    args = parser.parse_args()
    start = time.monotonic()
    report = run(args.region)
    elapsed = time.monotonic() - start
    REPORT_PATH.write_text(json.dumps(report, indent=2))
    print(f"\nReal cost: ${report['total_dollars']} ({report['total_calls']} calls), {elapsed:.1f}s")
    print(f"Directive fired: {report['directive_fired']}  Facilitator step-ins: {report['facilitator_step_in']}  "
          f"Self-revision ran: {report['self_revision_ran']}  changed: {report['self_revision_changed']}")
    print(f"Report: {REPORT_PATH}")
