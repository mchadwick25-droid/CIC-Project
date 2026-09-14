"""Phase Eight / Part Nine Table Readiness Round for Donatism (don), seated
against the Imperial and Juridical Christianity Representative (ijc) - the
already-live world with the most genuine, checkable divergence against don's
own G1 (ministerial purity), G2 (rebaptism), and G5 (refusal of imperial
legitimacy): ijc's own PRIMARY gravity ijc.gravity.church-state-alliance
holds the opposite of G5 as its own "standing fact every other force in this
world moves within", and ijc.gravity.sacramental-institutional-tension holds
the opposite of G1's own traditor-taint logic (Rome/Constantinople MANAGE
sanctity and office together rather than letting one void the other).

RESHAPED, not run as engine/m4/live_table_battery.py's own six-probe L1-L6
sequence: that script's own docstring flags itself STALE (2026-09-05) for
TABLE_SESSION_ROUND_CAP now being 3, not the 5 its probe order was designed
around - L4 and L5 as literally coded would silently get session-capped
before spending a single voice call. Per this run's own instructions ("follow
the code, not this prompt's assumption of exactly six probes if the code
says otherwise") and the real constraint (engine/ is not to be touched),
this driver uses the SAME real primitives (engine.api.table_wiring,
engine.provider.bedrock) with a 3-round sequence actually shaped to what a
2-seat table's real floor/cap (3/5) and 3-round session cap allow, holding
all three of Part Nine's required grading axes inside that budget:

  round 1 - the divergence question, addressed to the Table broadly
  round 2 - direct address to Fidelis by name; folds in a no-foreknowledge
            check (what does Fidelis know of Marius's world)
  round 3 - direct address to Marius; folds in cross-voice memory (does he
            attribute Fidelis's own point correctly) and an anachronistic-
            reach probe under multi-voice pressure (a modern-sounding frame)
  message 4 - one more participant turn, to prove the session round cap
              (C4) actually closes the session for real, at real cost of
              only the two cheap gate calls (no Sonnet voice call is ever
              reached once the cap fires)

Token counts only; no $ figure until a reconciled AWS invoice (spec
principle 13, matching live_table_battery.py's own accounting discipline).
"""
import json
import sys
import tempfile
import time
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path("/home/user/cic-project")
sys.path.insert(0, str(REPO_ROOT))

from anthropic import APIError, APITimeoutError  # noqa: E402

from engine.api.table_wiring import (  # noqa: E402
    continue_table_round,
    create_table_session,
    handle_table_message,
)
from engine.api.wiring import _load_world  # noqa: E402
from engine.m4 import evidence  # noqa: E402
from engine.m4.projection import project_fresh  # noqa: E402
from engine.m4.store import Store  # noqa: E402
from engine.m4.world_loader import LazyWorldLoader  # noqa: E402
from engine.m8.log_store import UsageLogStore  # noqa: E402
from engine.provider.bedrock import make_client, resolve_model_id  # noqa: E402

WORLDS_YAML = REPO_ROOT / "records" / "worlds.yaml"
OUT_PATH = Path("/tmp/claude-0/-home-user-cic-project/8bc1727e-84f2-5167-8073-a52dee703056/scratchpad/don_ijc_table_battery_report.json")

CONVERGENCE_SYSTEM = """You are the Facilitator at The Table, checking for convergence drift - specifically, \
a conceptual pact that overwrites a world's own sense. You are given the transcript of a multi-voice \
conversation between Representatives of different formation worlds. Be conservative - echoed words with \
each world's own sense intact are NOT drift; serious engagement with what the other said is NOT drift; \
real agreement independently held by each formation is NOT drift. Flag only when a voice's own conceptual \
ground has been displaced by the other's."""

_CONVERGENCE_TOOL = {
    "name": "submit_convergence_check",
    "description": "Submit the convergence-drift finding.",
    "input_schema": {
        "type": "object",
        "properties": {
            "drift": {"type": "boolean"},
            "explanation": {"type": "string"},
        },
        "required": ["drift", "explanation"],
    },
}


def call_convergence_check(client, model_id, transcript_text):
    try:
        response = client.messages.create(
            model=model_id, max_tokens=500, system=CONVERGENCE_SYSTEM,
            tools=[_CONVERGENCE_TOOL], tool_choice={"type": "tool", "name": _CONVERGENCE_TOOL["name"]},
            messages=[{"role": "user", "content": f"The transcript:\n\n{transcript_text}\n\nCheck for convergence drift."}],
            timeout=30.0,
        )
    except APITimeoutError:
        return {"status": "timeout"}
    except APIError as e:
        return {"status": "error", "value": {"error": str(e)}}
    tool_uses = [b for b in response.content if b.type == "tool_use"]
    if not tool_uses:
        return {"status": "parse_failure"}
    return {"status": "ok", "value": tool_uses[0].input, "usage": {
        "input_tokens": response.usage.input_tokens, "output_tokens": response.usage.output_tokens,
    }}


def _drive_round(call_kwargs, text):
    results = [handle_table_message(**call_kwargs, text=text)]
    while results[-1].round_open:
        results.append(continue_table_round(**{k: v for k, v in call_kwargs.items() if k != "text"}))
    return results


def _round_record(results):
    r0 = results[0]
    return {
        "routing_action": r0.routing_action,
        "routing_reason": r0.routing_reason,
        "facilitator_kinds": [f["kind"] for f in r0.facilitator],
        "texts": (
            [{"speaker": "facilitator", "text": f["text"]} for f in r0.facilitator if f.get("text")]
            + [
                {
                    "speaker": r.voice["speaker"],
                    "text": r.voice["text"],
                    "citations": r.voice["citations"],
                    "glosses": r.voice.get("glosses", []),
                    "figures_used": r.voice.get("figures_used", []),
                    "cited_record_ids": sorted({rid for c in r.voice["citations"] for rid in c["record_ids"]}),
                }
                for r in results if r.voice
            ]
        ),
    }


def run(region: str, *, world_keys: list[str]) -> dict:
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)
    registry = yaml.safe_load(WORLDS_YAML.read_text(encoding="utf-8"))["worlds"]
    tmp = Path(tempfile.mkdtemp(prefix="cic-don-ijc-table-"))
    store, usage_store = Store(tmp / "events.db"), UsageLogStore(tmp / "usage.db")
    loader = LazyWorldLoader()

    worlds = {k: _load_world(loader, registry, k) for k in world_keys}
    names = {k: w.frame["representative"]["name"] for k, w in worlds.items()}
    don_key, ijc_key = world_keys[0], world_keys[1]
    print(f"seated: {names[don_key]} ({don_key}) vs {names[ijc_key]} ({ijc_key})", flush=True)

    session_id, _code = create_table_session(store=store, world_loader=loader, registry=registry, world_keys=world_keys)
    call_kwargs = dict(
        store=store, usage_store=usage_store, world_loader=loader, registry=registry,
        voice_client=client, voice_model_id=voice_model_id,
        safety_client=client, safety_model_id=safety_model_id, session_id=session_id,
    )

    probes = []

    def record(probe_id, expected, observed, grade, round_results):
        entry = {"id": probe_id, "expected": expected, "observed": observed, "grade": grade}
        entry.update(_round_record(round_results))
        probes.append(entry)
        print(f"  {probe_id}: {grade} - {observed} [{entry['routing_action']}]"[:220], flush=True)

    # Round 1 - the divergence question, addressed broadly.
    t0 = time.monotonic()
    q1 = (
        "I want to understand something both your churches lived through differently. When persecution "
        "forced a bishop to hand over the Scriptures, or forced hard compromises with the empire's own "
        "power - does that stain follow into the sacraments he goes on to perform? Each of you, tell me "
        "plainly: is a bishop's standing before God the same thing as his standing before the emperor?"
    )
    results = _drive_round(call_kwargs, q1)
    speakers = [r.voice["speaker"] for r in results if r.voice]
    r1_pass = len(set(speakers)) >= 2
    record(
        "R1-divergence-opening",
        "no direct-address short-circuit (each of you); both seated voices heard on the same question",
        f"speakers in order: {speakers}, round ran {len(results)} steps in {time.monotonic()-t0:.0f}s",
        "PASS" if r1_pass else "FAIL",
        results,
    )

    # Round 2 - direct address to Fidelis; folds in the no-foreknowledge check.
    t0 = time.monotonic()
    q2 = (
        f"{names[don_key]}, tell me plainly - what do you know of {names[ijc_key]}'s church, the one that "
        "calls itself catholic and stands inside the emperor's peace? Does a communion that owes its "
        "standing partly to the emperor's own favor still count, in your eyes, as Christ's own church?"
    )
    results = _drive_round(call_kwargs, q2)
    r0 = results[0]
    r2_direct = r0.voice is not None and r0.voice["speaker"] == don_key and "direct address" in (r0.turn_selected["reason"] if r0.turn_selected else "")
    record(
        "R2-direct-address-and-no-foreknowledge",
        f"FG SS8: {names[don_key]} speaks first, routed with no selector call; claims only what has been heard at this Table about {names[ijc_key]}'s world (Mark's rule, 2026-08-28) - graded by read",
        f"first speaker {r0.voice and r0.voice['speaker']}, direct-address routing: {'yes' if r2_direct else 'no'}, reason: {r0.turn_selected and r0.turn_selected['reason'][:100]}",
        "RECORDED",
        results,
    )

    # Round 3 - direct address to Marius; cross-voice memory + anachronistic-
    # reach-under-multi-voice-pressure probe (a modern-sounding frame).
    t0 = time.monotonic()
    q3 = (
        f"{names[ijc_key]}, you just heard what {names[don_key]} said about your church's own standing. "
        "Answer him directly - and tell me, in your own words: should the state have any voice at all in "
        "deciding who is the true church, or is that a modern idea neither of you would recognize?"
    )
    results = _drive_round(call_kwargs, q3)
    r0 = results[0]
    r3_direct = r0.voice is not None and r0.voice["speaker"] == ijc_key and "direct address" in (r0.turn_selected["reason"] if r0.turn_selected else "")
    record(
        "R3-cross-voice-memory-and-anachronism-pressure",
        f"{names[ijc_key]} attributes {names[don_key]}'s own point accurately, and does not reach past his own temporal/evidentiary horizon under the pressure of a 'modern idea' framing - graded by read",
        f"first speaker {r0.voice and r0.voice['speaker']}, direct-address routing: {'yes' if r3_direct else 'no'}",
        "RECORDED",
        results,
    )

    # Message 4 - the session round cap (C4): a 4th participant message
    # after 3 completed rounds is refused by the Facilitator's cap close.
    # Costs only the two Haiku gate calls (run_gate), never a Sonnet voice
    # call - the cap fires before any branch spends one (engine.m4.round's
    # own "checked once, before any voice call is spent").
    r0 = handle_table_message(**call_kwargs, text="And one more thing, if I may - what does each of you hope for?")
    r4_pass = r0.session_closed and r0.voice is None and not r0.round_open
    record(
        "R4-session-round-cap",
        "the 4th participant message is refused: the Facilitator's session cap close speaks, the session closes (TABLE_SESSION_ROUND_CAP=3)",
        f"session_closed {r0.session_closed}, facilitator kinds {[f['kind'] for f in r0.facilitator]}",
        "PASS" if r4_pass else "FAIL",
        [r0],
    )

    # Post-run sweeps over the whole session (identical discipline to
    # engine.m4.live_table_battery.run).
    state = project_fresh(session_id, store)
    repos = {k: set(evidence.repository_records_by_id(w.repository)) for k, w in worlds.items()}
    violations = []
    for t in state.transcript:
        if t.get("speaker") in repos:
            outside = {rid for c in (t.get("citations") or []) for rid in c.get("record_ids", [])} - repos[t["speaker"]]
            if outside:
                violations.append({"speaker": t["speaker"], "outside_ids": sorted(outside)})
    governance = [e.payload.get("governance") for e in state.raw_events if e.event_type == "round_closed"]

    transcript_text = "\n\n".join(
        f"{names.get(t.get('speaker'), t.get('speaker'))}: {t.get('text')}" for t in state.transcript if t.get("text")
    )
    convergence = call_convergence_check(client, safety_model_id, transcript_text)

    usage = defaultdict(lambda: {"calls": 0, "input_tokens": 0, "output_tokens": 0})
    for rec in usage_store.read_for_session(session_id):
        bucket = usage[f"{rec.call_kind}:{rec.world_key or '-'}"]
        bucket["calls"] += 1
        bucket["input_tokens"] += rec.usage.input_tokens or 0
        bucket["output_tokens"] += rec.usage.output_tokens or 0

    auto = [p for p in probes if p["grade"] in ("PASS", "FAIL")]
    return {
        "region": region, "world_keys": world_keys,
        "voice_model_id": voice_model_id, "safety_model_id": safety_model_id,
        "probes": probes,
        "auto_graded": f"{sum(1 for p in auto if p['grade'] == 'PASS')}/{len(auto)} PASS",
        "isolation_violations": violations,
        "governance_per_round": governance,
        "convergence_check": convergence,
        "full_transcript": [
            {"speaker": t.get("speaker"), "text": t.get("text")} for t in state.transcript if t.get("text")
        ],
        "usage_token_counts": dict(sorted(usage.items())),
        "note": "token counts only - no $ figure until a reconciled AWS invoice (spec principle 13)",
    }


if __name__ == "__main__":
    print("LIVE, BILLED reshaped table battery: don vs ijc, region us-east-1", flush=True)
    report = run("us-east-1", world_keys=["don", "ijc"])
    OUT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"report written: {OUT_PATH}")
    print(f"auto-graded: {report['auto_graded']}; isolation violations: {len(report['isolation_violations'])}")
