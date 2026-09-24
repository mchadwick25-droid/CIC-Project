"""R37 live battery (Rulings-Pending.md R37, R37-A, R37-B; Decision-Log.md
Entry 72): real, billed Bedrock calls through the production wiring -
engine.api.wiring.handle_message for interview, engine.api.table_wiring
for the Table - with production defaults (self-revision on, R27
enforcement off). engine/m4/reports/r37_build_battery.py already proves
which directive branch each turn takes; this measures what the voice
actually does with it.

Four probes, each its own fresh session:

  L1-condition-a (interview, alx on the Donatists): alx (150-400) could
    have known of the Donatists (from 311), and its own records never
    mention them - the R26 sentence, then a pivot licensed under (a).
  L2-later-tradition (interview, alx on the Reformed Cities): arose
    1100 years after alx's window closed - the pivot must come from the
    question's own words alone.
  L3-condition-b (interview, alx, two turns): turn 1 reveals one fact
    about the Donatists in the participant's own words; turn 2 asks about
    them. The revealed sentence must reach the directive, and the voice
    may use only that.
  T1-r37-b (Table, ijc and alx): ijc is asked about the Donatists first
    (its own records name them); alx is drawn in second, and whatever
    ijc said naming them is what alx may use (R37-B).

Ground truth for what the voice was TOLD is the real return value of
engine.m4.turn._other_tradition_directive, captured by a call-through
wrapper (no behaviour change), in call order.

Outside-content markers: a small fixed list of names and facts about
each named tradition that only outside knowledge would supply. A marker
counts as a leak only when it appears in the answer AND nowhere in what
the conversation said before the answer AND nowhere in the speaking
world's own record prose (alx's records genuinely name Carthage, for
instance, through Cyprian). This is a coarse screen, not a verdict -
every answer is also in the report in full for a hand read.

Run: python -m engine.m4.reports.r37_live_battery --region us-east-1
"""
import argparse
import json
import pathlib
import sys
import tempfile
import time
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.api import wiring
from engine.api.table_wiring import continue_table_round, create_table_session, handle_table_message
from engine.m1.registry import load_registry
from engine.m4 import evidence as ev
from engine.m4 import turn as turn_module
from engine.m4.store import Store
from engine.m4.uncited_claims import _prose_text_for_evidence_scan
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE, SONNET_4_5_PRICE_TABLE
from engine.m8.log_store import UsageLogStore
from engine.provider.bedrock import make_client, resolve_model_id

REPORT_PATH = pathlib.Path(__file__).resolve().parent / "r37-live-battery-2026-09-24.json"

DONATIST_MARKERS = [
    "traditor", "Caecilian", "Donatus", "Majorinus", "Numidia", "Circumcellion",
    "rebapti", "Optatus", "Augustine", "Carthage", "Diocletian", "handed over",
]
REFORMED_MARKERS = [
    "Zwingli", "Calvin", "Bullinger", "Zurich", "Geneva", "predestination", "Reformation",
    "Protestant", "Consistory", "sixteenth", "Luther", "Marburg",
]

L3_REVEAL = (
    "My teacher told me the Donatists would not accept bishops who had handed over the scriptures. "
    "How did Alexandria choose its own bishops?"
)


def _price_for_call_kind(call_kind: str):
    return HAIKU_4_5_PRICE_TABLE if call_kind in ("safety_call", "reader_call", "turn_selector") else SONNET_4_5_PRICE_TABLE


class _DirectiveCapture:
    """Call-through wrapper on _other_tradition_directive: records what
    the directive actually returned, and the R37 inputs it was given."""

    def __init__(self):
        self.calls = []
        self._original = turn_module._other_tradition_directive

    def __enter__(self):
        def wrapper(*args, **kwargs):
            result = self._original(*args, **kwargs)
            self.calls.append({
                "known_in_window": kwargs.get("known_in_window"),
                "revealed_excerpts": [list(e) for e in (kwargs.get("revealed_excerpts") or [])],
                "evidence_record_ids": list(args[0]) if args and args[0] else [],
                "directive_text": result,
            })
            return result
        turn_module._other_tradition_directive = wrapper
        return self

    def __exit__(self, *exc):
        turn_module._other_tradition_directive = self._original


def _world_prose(loader, registry, world_key) -> str:
    world = wiring._load_world(loader, registry, world_key)
    return " ".join(_prose_text_for_evidence_scan(r) for r in ev.repository_records_by_id(world.repository).values()).lower()


def _leaks(answer: str, markers: list[str], *, said_before: str, world_prose: str) -> list[str]:
    a, before = answer.lower(), said_before.lower()
    return [m for m in markers if m.lower() in a and m.lower() not in before and m.lower() not in world_prose]


def _dollars(usage_store, session_id) -> tuple[float, int]:
    records = usage_store.read_for_session(session_id)
    return round(sum((estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars or 0.0) for r in records), 4), len(records)


def _uncited_claims_events(store, session_id) -> list[dict]:
    """R27's own report-only audit events for the session - what the
    detector flagged, whatever the voice was told."""
    return [e.payload for e in store.read_events(session_id) if e.event_type == "uncited_claims"]


def _fresh_stores(probe_id):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix=f"cic-r37-live-{probe_id}-"))
    return Store(tmp / "events.db"), UsageLogStore(tmp / "usage.db")


def _interview(*, probe_id, world_key, messages, markers, ctx) -> dict:
    store, usage_store = _fresh_stores(probe_id)
    session_id, _code = wiring.create_session(store=store, world_loader=ctx["loader"], registry=ctx["registry"], world_key=world_key)
    turns, said_before = [], " ".join(e.payload.get("text", "") for e in store.read_events(session_id) if e.event_type == "facilitator_turn")
    with _DirectiveCapture() as cap:
        for i, message in enumerate(messages, start=1):
            before_calls = len(cap.calls)
            result = wiring.handle_message(
                store=store, usage_store=usage_store, world_loader=ctx["loader"], registry=ctx["registry"],
                voice_client=ctx["client"], voice_model_id=ctx["voice_model_id"],
                safety_client=ctx["client"], safety_model_id=ctx["safety_model_id"],
                session_id=session_id, text=message, client_msg_id=f"{probe_id}-{i}",
            )
            said_before += " " + message
            answer = (result.voice or {}).get("text") or ""
            directive = cap.calls[before_calls] if len(cap.calls) > before_calls else None
            turns.append({
                "turn": i,
                "message": message,
                "routing_action": result.routing_action,
                "routing_reason": result.routing_reason,
                "facilitator_text": (result.facilitator or {}).get("text"),
                "directive": directive,
                "voice_text": answer,
                "said_r26_sentence": turn_module.R26_HONEST_LIMIT_SENTENCE.lower() in answer.lower(),
                "citations": (result.voice or {}).get("citations", []),
                "self_revision": ((result.voice or {}).get("attempts_meta") or {}).get("self_revision"),
                "leak_markers": _leaks(answer, markers, said_before=said_before, world_prose=ctx["prose"][world_key]),
            })
            said_before += " " + answer
    dollars, calls = _dollars(usage_store, session_id)
    return {
        "probe_id": probe_id, "mode": "interview", "world_key": world_key, "turns": turns,
        "uncited_claims_events": _uncited_claims_events(store, session_id), "dollars": dollars, "calls_made": calls,
    }


def _table(*, probe_id, first_key, second_key, markers, ctx) -> dict:
    store, usage_store = _fresh_stores(probe_id)
    registry, loader = ctx["registry"], ctx["loader"]
    session_id, _code = create_table_session(store=store, world_loader=loader, registry=registry, world_keys=[first_key, second_key])
    call_kwargs = dict(
        store=store, usage_store=usage_store, world_loader=loader, registry=registry,
        voice_client=ctx["client"], voice_model_id=ctx["voice_model_id"],
        safety_client=ctx["client"], safety_model_id=ctx["safety_model_id"], session_id=session_id,
    )
    first_name = wiring._load_world(loader, registry, first_key).frame["representative"]["name"]
    message = f"{first_name}, what was your relationship with the Donatists?"
    with _DirectiveCapture() as cap:
        results = [handle_table_message(**call_kwargs, text=message)]
        while results[-1].round_open:
            results.append(continue_table_round(**call_kwargs))
    said_before = " ".join(e.payload.get("text", "") for e in store.read_events(session_id) if e.event_type == "facilitator_turn")
    said_before += " " + message
    turns, directive_iter = [], iter(cap.calls)
    for r in results:
        voice = r.voice or {}
        answer = voice.get("text") or ""
        speaker = voice.get("speaker")
        turns.append({
            "speaker": speaker,
            "routing_action": r.routing_action,
            "directive": next(directive_iter, None) if voice else None,
            "voice_text": answer,
            "said_r26_sentence": turn_module.R26_HONEST_LIMIT_SENTENCE.lower() in answer.lower(),
            "citations": voice.get("citations", []),
            "self_revision": (voice.get("attempts_meta") or {}).get("self_revision"),
            "leak_markers": _leaks(answer, markers, said_before=said_before, world_prose=ctx["prose"].get(speaker, "")) if speaker else [],
        })
        said_before += " " + answer
    dollars, calls = _dollars(usage_store, session_id)
    return {
        "probe_id": probe_id, "mode": "table", "seats": [first_key, second_key], "message": message, "turns": turns,
        "uncited_claims_events": _uncited_claims_events(store, session_id), "dollars": dollars, "calls_made": calls,
    }


def run(region: str) -> dict:
    registry = load_registry()
    loader = LazyWorldLoader()
    ctx = {
        "registry": registry,
        "loader": loader,
        "client": make_client(region),
        "voice_model_id": resolve_model_id("us.anthropic.claude-sonnet-4-5", region),
        "safety_model_id": resolve_model_id("us.anthropic.claude-haiku-4-5", region),
        "prose": {k: _world_prose(loader, registry, k) for k in ("alx", "ijc")},
    }
    reformed = registry["rzg"]["card_name"]
    probes = []
    for spec in (
        dict(kind="interview", probe_id="L1-condition-a", world_key="alx",
             messages=["What was your relationship with the Donatists?"], markers=DONATIST_MARKERS),
        dict(kind="interview", probe_id="L2-later-tradition", world_key="alx",
             messages=[f"What was your relationship with {reformed}?"], markers=REFORMED_MARKERS),
        dict(kind="interview", probe_id="L3-condition-b", world_key="alx",
             messages=[L3_REVEAL, "What was your relationship with the Donatists?"], markers=DONATIST_MARKERS),
        dict(kind="table", probe_id="T1-r37-b", first_key="ijc", second_key="alx", markers=DONATIST_MARKERS),
    ):
        print(f"Running {spec['probe_id']}...", flush=True)
        kind = spec.pop("kind")
        probe = _interview(**spec, ctx=ctx) if kind == "interview" else _table(**spec, ctx=ctx)
        probes.append(probe)
        for t in probe["turns"]:
            d = t["directive"] or {}
            print(f"  {t.get('speaker') or 'turn ' + str(t.get('turn'))}: route={t['routing_action']} "
                  f"known_in_window={d.get('known_in_window')} excerpts={len(d.get('revealed_excerpts') or [])} "
                  f"r26={t['said_r26_sentence']} leaks={t['leak_markers']}", flush=True)
        print(f"  ${probe['dollars']} ({probe['calls_made']} calls)", flush=True)
    return {
        "asof": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "settings": {"r27_enforce": False, "self_revision_enabled": True, "note": "production defaults"},
        "total_dollars": round(sum(p["dollars"] for p in probes), 4),
        "total_calls": sum(p["calls_made"] for p in probes),
        "probes": probes,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", default="us-east-1")
    args = parser.parse_args()
    start = time.monotonic()
    report = run(args.region)
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"\nReal cost: ${report['total_dollars']} ({report['total_calls']} calls), {time.monotonic() - start:.1f}s")
    print(f"Report: {REPORT_PATH}")
