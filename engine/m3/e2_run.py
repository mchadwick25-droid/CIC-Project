"""E2: uncited claims on the real turn path, three arms from one draft.

Each sealed probe goes through production's own gate (run_gate, Haiku
4.5) and voice turn (_run_ordinary_voice_turn, Sonnet 4.5), with the
production settings: self-revision off, sentence enforcement off. That
first draft is arm "off", today's behaviour. The other two arms start
from the same draft, so the only difference between arms is the
regeneration:

- "paragraph": the uncited-claims enforcement as production has it -
  regenerate once when a paragraph carries no citation at all or a
  sentence names a neighbouring tradition uncited; a second failure
  hands the turn to the Facilitator (empty voice text). Mirrors
  turn.py's uncited-claims enforcement block step for step, with the
  same correction text passed through the `correction` parameter.
- "sentence": regenerate once when any declarative claim sentence
  carries no citation (find_uncited_claims), naming every such
  sentence; the retry stands whatever it contains. Not production
  behaviour.

- "records_only" (--mode records-only): a separate first draft whose
  turn directive carries RECORDS_ONLY below; no regeneration. Compared
  against the "off" draft of the same probes.

Paid run: every setting is printed before the first billed call, and
spend is checked against --max-usd after every probe.
"""
import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from engine.m1.registry import load_registry
from engine.m3 import protocol, sealed_probes
from engine.m4 import evidence
from engine.m4.grounding_net import check_turn_with_paragraph_coverage
from engine.m4.turn import _append_r27_correction, _run_ordinary_voice_turn, run_gate
from engine.m4.uncited_claims import classify_neighbour_named, find_uncited_claims, find_uncited_paragraphs, known_tradition_names
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.price_tables import price_for_call
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = Path(__file__).resolve().parent / "reports" / "e2"
ARMS = ("off", "paragraph", "sentence")
RECORDS_ONLY = (
    "\n## Staying inside your records\n"
    "Say only what your own records hold. Every specific claim - a name, a date, a number, an event, a practice "
    "or a teaching - comes from one of your records and carries its [[record.id]] tag. Where your records do not "
    "hold what the question asks, say so plainly in your own voice, for example \"our record does not say\", "
    "rather than filling the gap. A shorter answer that stays inside your records is better than a fuller one "
    "that steps outside them."
)


def _usd(records) -> float:
    total = 0.0
    for rec in records:
        table = price_for_call(rec.call_kind, rec.model_id)
        if table is None:
            raise RuntimeError(f"no price for {rec.call_kind} on {rec.model_id}")
        total += estimate_cost(rec.usage, table).dollars
    return total


def _offenses(net_result: dict, names: list[str]) -> tuple[list[dict], list[dict]]:
    """(hard offenses as production enforces them, every uncited claim sentence)."""
    uncited = [classify_neighbour_named(o, names) for o in find_uncited_claims(net_result["sentences"])]
    hard = [o for o in find_uncited_paragraphs(net_result) if o["class"] == "wholly_uncited_paragraph"]
    hard += [o for o in uncited if o["class"] == "neighbour_named"]
    return hard, uncited


def _transcript(event: dict, *, facilitator: bool = False) -> dict:
    net = event["grounding"]
    return {
        "answer_text": "" if facilitator else event["text"],
        "citation_entries": [] if facilitator else event["citations"],
        "handed_to_facilitator": facilitator,
        "uncited_claim_sentences": [] if facilitator else [o["sentence"] for o in find_uncited_claims(net["sentences"])],
    }


def run_world(world_key: str, *, registry: dict, loader: LazyWorldLoader, client, voice_model_id: str,
              safety_model_id: str, spent_before: float, max_usd: float, limit: int | None,
              mode: str = "arms") -> tuple[list[dict], float, str | None]:
    entry = registry[world_key]
    world, _ = loader.load(world_key, package_dir=REPO_ROOT / entry["package"]["location"],
                           expected_manifest_hash=entry["package"]["manifest_hash"])
    records = evidence.repository_records_by_id(world.repository)
    names = known_tradition_names(registry, exclude_world_key=world_key)
    spent = spent_before
    out = []
    for seal in protocol.battery()[:limit]:
        if spent >= max_usd:
            return out, spent, f"stopped before {world_key}:{seal['probe_id']}: spent {spent:.4f} >= cap {max_usd}"
        message = sealed_probes.read_probe(seal["probe_id"])["text"]
        session_id = f"e2-{world_key}-{seal['probe_id']}"
        t0 = time.monotonic()
        gate = run_gate(session_id=session_id, safety_client=client, safety_model_id=safety_model_id,
                        participant_message=message, pressed={}, anachronistic_term_ids=set())
        usage = list(gate.usage_records)
        action = gate.gate_result.routing.action
        row = {"probe_id": seal["probe_id"], "cell": seal["cell"], "routing_action": action, "arms": {}}
        if action not in ("voice_with_directive", "voice_pass_through"):
            spent += _usd(usage)
            row["usd"] = round(_usd(usage), 6)
            out.append(row)
            continue
        oos = gate.gate_result.routing.out_of_scope_class if action == "voice_with_directive" else None
        common = dict(voice_client=client, voice_model_id=voice_model_id, world=world, participant_message=message,
                      directive=gate.gate_result.routing.directive, session_id=session_id, usage_world_key=world_key,
                      is_other_tradition_first_ask=oos == "other_tradition", self_revision_enabled=False)

        if mode == "records-only":
            draft, rec = _run_ordinary_voice_turn(**common, correction=RECORDS_ONLY)
            usage += rec
            row["arms"]["records_only"] = _transcript(draft)
            cost = _usd(usage)
            spent += cost
            row.update(usd=round(cost, 6), seconds=round(time.monotonic() - t0, 2), out_of_scope_class=oos)
            out.append(row)
            print(json.dumps({"world": world_key, "probe": seal["probe_id"], "usd": round(cost, 4), "spent": round(spent, 4),
                              "records_only": len(row["arms"]["records_only"]["uncited_claim_sentences"])}), flush=True)
            continue

        draft, rec = _run_ordinary_voice_turn(**common)
        usage += rec
        row["arms"]["off"] = _transcript(draft)
        hard, uncited = _offenses(draft["grounding"], names)

        # paragraph arm: production enforcement, Facilitator on a second failure
        if hard:
            retry, rec = _run_ordinary_voice_turn(**common, correction=_append_r27_correction(None, hard))
            usage += rec
            retry_hard, _ = _offenses(retry["grounding"], names)
            row["arms"]["paragraph"] = {**_transcript(retry, facilitator=bool(retry_hard)), "regenerated": True}
        else:
            row["arms"]["paragraph"] = {**row["arms"]["off"], "regenerated": False}

        # sentence arm: every uncited claim sentence named, retry stands
        named = list(uncited) + [o for o in hard if o["sentence"] not in {u["sentence"] for u in uncited}]
        if named:
            retry, rec = _run_ordinary_voice_turn(**common, correction=_append_r27_correction(None, named))
            usage += rec
            row["arms"]["sentence"] = {**_transcript(retry), "regenerated": True}
        else:
            row["arms"]["sentence"] = {**row["arms"]["off"], "regenerated": False}

        cost = _usd(usage)
        spent += cost
        row.update(usd=round(cost, 6), seconds=round(time.monotonic() - t0, 2), out_of_scope_class=oos)
        out.append(row)
        print(json.dumps({"world": world_key, "probe": seal["probe_id"], "usd": round(cost, 4), "spent": round(spent, 4),
                          **{a: len(row["arms"][a]["uncited_claim_sentences"]) for a in ARMS}}), flush=True)
    return out, spent, None


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--region", required=True)
    p.add_argument("--worlds", required=True)
    p.add_argument("--max-usd", type=float, required=True)
    p.add_argument("--authorized-by", required=True)
    p.add_argument("--limit", type=int, default=None, help="first N probes per world (default all)")
    p.add_argument("--mode", choices=("arms", "records-only"), default="arms")
    p.add_argument("--settings-only", action="store_true")
    p.add_argument("--out", default=None)
    args = p.parse_args(argv)

    registry = load_registry()
    worlds = args.worlds.split(",")
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", args.region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", args.region)
    settings = {
        "worlds": worlds, "probes_per_world": args.limit or len(protocol.battery()),
        "voice_model_id": voice_model_id, "safety_model_id": safety_model_id, "region": args.region,
        "mode": args.mode, "arms": ["records_only"] if args.mode == "records-only" else list(ARMS),
        "records_only_directive": RECORDS_ONLY if args.mode == "records-only" else None, "self_revision": "off (production)", "sentence_enforce": "off (production)",
        "max_usd": args.max_usd, "authorized_by": args.authorized_by,
        "package_manifest_hash": {w: registry[w]["package"]["manifest_hash"] for w in worlds},
    }
    print(json.dumps({"run_settings": settings}, indent=2), flush=True)
    if args.settings_only:
        return 0

    loader = LazyWorldLoader()
    client = make_client(args.region)
    report = {"run_settings": settings, "started": datetime.now(timezone.utc).isoformat(timespec="seconds"), "worlds": {}}
    spent, aborted = 0.0, None
    for w in worlds:
        rows, spent, aborted = run_world(w, registry=registry, loader=loader, client=client, voice_model_id=voice_model_id,
                                         safety_model_id=safety_model_id, spent_before=spent, max_usd=args.max_usd, limit=args.limit,
                                         mode=args.mode)
        report["worlds"][w] = rows
        if aborted:
            break
    report.update(actual_usd_spent=round(spent, 6), aborted_reason=aborted)
    out = Path(args.out) if args.out else REPORT_DIR / f"e2-{datetime.now(timezone.utc):%Y-%m-%dT%H-%M-%SZ}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {out}; spent {spent:.4f}; aborted={aborted}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
