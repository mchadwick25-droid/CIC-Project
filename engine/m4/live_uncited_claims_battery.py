"""R27 build item 4 (Decision-Log.md Entry 51, reviewer thread build order,
2026-09-22): a real, billed live run measuring the report-only uncited-
claims check's actual catch rate per world, before Mark sets an
enforcement threshold. Like engine/m4/live_table_battery.py and
engine/m8/live_cost_run.py, a by-hand, credentialed run - not a CI job.

Interview mode, two turns per admitted formation world:
  1. A generic in-scope conflict-history ask - the kind of substantive,
     citation-heavy answer the check exists to watch, with no built-in
     bias toward either offense class.
  2. A named-other-tradition ask (built per world from a real OTHER
     admitted formation world's own card_name) - the R26 shape this
     check's "neighbour_named" and "own_doctrine_in_other_tradition_turn"
     classes exist to catch.

Plus one small table session (3 worlds, 2 rounds) to prove the table
caller path (engine.api.table_wiring._advance_open_round's own
uncited_claims wiring, PR #415) produces the same events live, not only
against synthetic dicts in test_uncited_claims.py.

Every voice_event's own "uncited_claims" field (engine.m4.turn's report-
only, additive field - present whether or not this script's own refined
event fires) is read back directly rather than re-derived, then refined
through the same build_uncited_claims_event() both real callers already
use, so this report counts exactly what production would have logged.

Cost, M8-style (engine.m8.cost/summary, same published rate card
engine.m8.live_cost_run already cites) - reused, not re-priced from
scratch, so a second live run's price table can't quietly drift from the
first's.
"""
import argparse
import json
import sys
import tempfile
from pathlib import Path

from engine.api.table_wiring import continue_table_round, create_table_session, handle_table_message
from engine.m1.registry import load_registry
from engine.m4.projection import project_fresh
from engine.m4.store import Store
from engine.m4.turn import run_turn
from engine.m4.uncited_claims import build_uncited_claims_event
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE, PRICE_TABLE_SOURCE, SONNET_4_5_PRICE_TABLE
from engine.m8.log_store import UsageLogStore
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "live-uncited-claims-battery-report.json"

CONFLICT_TURN = (
    "Tell me about a real conflict or controversy inside your own community's own history - "
    "who was on each side, and how did it end?"
)


def _other_tradition_turn(world_key: str, registry: dict) -> str:
    # A real other admitted formation world's own card_name (not
    # known_tradition_names, which also mixes in representative names for
    # the classifier's own sentence-matching purpose - a tradition's own
    # name reads naturally in this sentence, a person's given name would
    # not). First alphabetically for a deterministic, reproducible report
    # across re-runs.
    card_names = sorted(
        entry["card_name"]
        for key, entry in registry.items()
        if key != world_key and entry.get("kind") == "formation" and entry.get("card_name")
    )
    return f"What did {card_names[0]} believe about this same kind of conflict?"


def _price_for_call_kind(call_kind: str):
    return HAIKU_4_5_PRICE_TABLE if call_kind in ("safety_call", "reader_call", "turn_selector") else SONNET_4_5_PRICE_TABLE


def _run_interview_turn(*, client, voice_model_id, safety_model_id, world, session_id, message, usage_store):
    result = run_turn(
        session_id=session_id,
        voice_client=client, voice_model_id=voice_model_id,
        safety_client=client, safety_model_id=safety_model_id,
        world=world, participant_message=message,
        pressed={}, anachronistic_term_ids=set(),
    )
    for rec in result.usage_records:
        usage_store.append(rec)
    out_of_scope_class = (result.gate.get("out_of_scope") or {}).get("class")
    return result, out_of_scope_class


def run(region: str, *, world_keys: list[str], table_world_keys: list[str]) -> dict:
    registry = load_registry()
    loader = LazyWorldLoader()
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    per_world = {}
    with tempfile.TemporaryDirectory() as tmp:
        usage_store = UsageLogStore(Path(tmp) / "live-uncited-claims-battery-usage.db")

        for world_key in world_keys:
            entry = registry[world_key]
            world, _timing = loader.load(
                world_key, package_dir=REPO_ROOT / entry["package"]["location"],
                expected_manifest_hash=entry["package"]["manifest_hash"],
            )
            session_id = f"uncited-claims-battery-{world_key}"
            turns_info = []
            offenses_by_class: dict[str, int] = {}
            turns_with_offense = 0

            for message in (CONFLICT_TURN, _other_tradition_turn(world_key, registry)):
                result, out_of_scope_class = _run_interview_turn(
                    client=client, voice_model_id=voice_model_id, safety_model_id=safety_model_id,
                    world=world, session_id=session_id, message=message, usage_store=usage_store,
                )
                voice_event = result.voice_event
                event = (
                    build_uncited_claims_event(
                        voice_event, registry=registry,
                        is_other_tradition_turn=(result.routing_action == "voice_with_directive" and out_of_scope_class == "other_tradition"),
                    )
                    if voice_event is not None else None
                )
                offenses = event["offenses"] if event else []
                if offenses:
                    turns_with_offense += 1
                for o in offenses:
                    offenses_by_class[o["class"]] = offenses_by_class.get(o["class"], 0) + 1
                turns_info.append(
                    {
                        "message": message,
                        "routing_action": result.routing_action,
                        "out_of_scope_class": out_of_scope_class,
                        "voice_present": voice_event is not None,
                        "offenses": offenses,
                    }
                )

            records = usage_store.read_for_session(session_id)
            session_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in records) if records else 0.0
            per_world[world_key] = {
                "card_name": entry.get("card_name"),
                "turns": turns_info,
                "turns_run": len(turns_info),
                "turns_with_uncited_offense": turns_with_offense,
                "uncited_turn_rate": turns_with_offense / len(turns_info),
                "offenses_by_class": offenses_by_class,
                "session_dollars": session_dollars,
            }

        # The table path (PR #415's own caller wiring) - one small session,
        # proving the same events fire live through _advance_open_round,
        # not only interview's handle_message.
        store = Store(Path(tmp) / "live-uncited-claims-battery-events.db")
        table_session_id, _code = create_table_session(store=store, world_loader=loader, registry=registry, world_keys=table_world_keys)
        call_kwargs = dict(
            store=store, usage_store=usage_store, world_loader=loader, registry=registry,
            voice_client=client, voice_model_id=voice_model_id,
            safety_client=client, safety_model_id=safety_model_id, session_id=table_session_id,
        )
        table_turns = []
        for message in (CONFLICT_TURN, f"{registry[table_world_keys[1]].get('representative', {}).get('name')}, what do you make of that?"):
            results = [handle_table_message(**call_kwargs, text=message)]
            while results[-1].round_open:
                results.append(continue_table_round(**{k: v for k, v in call_kwargs.items() if k != "text"}))
            table_turns.extend(results)

        table_state = project_fresh(table_session_id, store)
        table_uncited_events = [e.payload for e in table_state.raw_events if e.event_type == "uncited_claims"]
        table_records = usage_store.read_for_session(table_session_id)
        table_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in table_records) if table_records else 0.0

    total_turns = sum(w["turns_run"] for w in per_world.values())
    total_with_offense = sum(w["turns_with_uncited_offense"] for w in per_world.values())
    total_dollars = sum(w["session_dollars"] for w in per_world.values()) + table_dollars

    return {
        "region": region, "voice_model_id": voice_model_id, "safety_model_id": safety_model_id,
        "price_table_source": PRICE_TABLE_SOURCE,
        "interview": {
            "worlds": per_world,
            "overall_turns_run": total_turns,
            "overall_turns_with_uncited_offense": total_with_offense,
            "overall_uncited_turn_rate": total_with_offense / total_turns if total_turns else 0.0,
        },
        "table": {
            "world_keys": table_world_keys,
            "session_id": table_session_id,
            "voice_turns": sum(1 for r in table_turns if r.voice),
            "uncited_claims_events": table_uncited_events,
            "session_dollars": table_dollars,
        },
        "total_dollars": total_dollars,
        "note": (
            "Priced against a published rate card, not a reconciled AWS invoice (spec principle 13). "
            "2 turns per world x 11 worlds + one small table session - an order-of-magnitude first look "
            "at the real uncited-claim rate, not a statistically powered sample."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", required=True)
    parser.add_argument(
        "--worlds", default="alx,cappadocian,desert,don,gallic,hal,ijc,pahc,rzg,syr,witt",
        help="comma-separated formation world keys (interview mode)",
    )
    parser.add_argument("--table-worlds", default="alx,don,rzg", help="2-3 comma-separated world keys (table mode)")
    parser.add_argument("--out", default=str(REPORT_PATH))
    args = parser.parse_args()
    world_keys = [k.strip() for k in args.worlds.split(",") if k.strip()]
    table_world_keys = [k.strip() for k in args.table_worlds.split(",") if k.strip()]
    print(f"LIVE, BILLED battery: uncited-claims rate, {len(world_keys)} worlds x 2 interview turns + 1 table session, region {args.region}", flush=True)
    report = run(args.region, world_keys=world_keys, table_world_keys=table_world_keys)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"report written: {out}")
    print(
        f"overall interview uncited-turn rate: {report['interview']['overall_uncited_turn_rate']:.0%} "
        f"({report['interview']['overall_turns_with_uncited_offense']}/{report['interview']['overall_turns_run']}); "
        f"table uncited_claims events: {len(report['table']['uncited_claims_events'])}; "
        f"total cost: ${report['total_dollars']:.4f}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
