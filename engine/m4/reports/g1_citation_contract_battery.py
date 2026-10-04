"""R39-audit G1/G2 (the reviewer's own retrofit brief, 2026-09-23): the
fleet-wide `citation_contract` (engine/shape/records/fleet_voice/
_fleet.voice.fleet.md) has no paragraph-level anchoring language (a
paragraph's own interpretive/connective sentences ride on the same
ground the paragraph opened with, but nothing says that explicitly -
this is what engine.m4.grounding_net.check_turn_with_paragraph_coverage
and find_uncited_paragraphs check for at RUNTIME, with nothing on the
generation side asking for it), and no tag-is-a-promise content rule
(R39's own gap, Decision-Log.md Entry 59: the contract's own verbatim-
fidelity promise is scoped to quoted spans only - an ordinary tagged
sentence's non-quoted content is never told it must stay inside what
the record supports).

Reuses engine.m4.live_uncited_claims_battery's own real machinery
(_run_probe_turn, CONFLICT_TURN, _other_tradition_turn, the paragraph-
offense classes) rather than reimplementing the probe/regeneration
logic - the INTERVIEW half only (the reviewer's own "22-probe battery"
- 11 admitted formation worlds x 2 fresh probes each), no table
session, to keep this report-only measurement's own real cost scoped to
what G1 actually asks (a paragraph-anchoring/tag-is-a-promise wording
before/after comparison, not a re-run of the table half F3/item 4/item
5 already measured elsewhere).

The "proposed" condition never edits records/ or any compiled package -
each loaded world's own frozen `LoadedWorld.prompt_text` is swapped for
a copy (dataclasses.replace) with the two additions appended
immediately after the citation contract's own last sentence ("...only
the sentence is."), a stable anchor present verbatim in every world's
compiled prompt regardless of that world's own per-world example ids
inside the contract's own worked example - the actual contract wording
is fleet-wide (engine/shape/records/fleet_voice/_fleet.voice.fleet.md's own
`citation_contract` field), and only its two bracketed example ids get
per-world substituted at compile time, so appending after this stable
tail sentence is safe across every world without needing to match the
example ids themselves.

Run: python3 -m engine.m4.reports.g1_citation_contract_battery --region us-east-1
"""
import argparse
import dataclasses
import json
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from engine.m1.registry import load_registry
from engine.m2.compiler import compile_and_hash
from engine.m4.live_uncited_claims_battery import (
    _PARAGRAPH_OFFENSE_CLASSES,
    CONFLICT_TURN,
    _other_tradition_turn,
    _run_probe_turn,
    _price_for_call_kind,
)
from engine.m4.world_loader import LoadedWorld
from engine.m8.cost import estimate_cost
from engine.m8.log_store import UsageLogStore
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[3]
REPORTS_DIR = Path(__file__).resolve().parent

CITATION_CONTRACT_TAIL_ANCHOR = "The tags themselves are never shown to the participant; only the sentence is."

PARAGRAPH_ANCHORING_ADDITION = (
    " Ground travels by paragraph, not only by sentence: an interpretive or connective sentence - one that "
    "carries no tag of its own because it names no person, place, text, number, or quote - stays attached to "
    "the claim it interprets, and that claim's own ground is what it rides on. It never drifts past a "
    "paragraph break to ride on a different paragraph's ground instead; a new paragraph that opens with its "
    "own claim starts its own ground fresh, and everything within that paragraph, tagged or not, answers to "
    "it."
)

TAG_IS_A_PROMISE_ADDITION = (
    " A tag is a promise about more than address: every specific detail in a tagged sentence - not only a "
    "quoted span - must be that record's own content, stated or a fair paraphrase of it, never a detail "
    "added because it sounds plausible, fits the period, or belongs to a related matter this voice happens "
    "to know about from outside the record. Where a sentence would need one more specific detail than its "
    "tagged record actually gives, it stops at what the record gives; anything further is named, if at all, "
    "as our own honest limit, never folded into the tagged sentence itself."
)

PROPOSED_ADDITION = PARAGRAPH_ANCHORING_ADDITION + TAG_IS_A_PROMISE_ADDITION

WORLDS = "alx,cappadocian,desert,don,gallic,hal,ijc,pahc,rzg,syr,witt"


def _compile_world(world_key: str) -> LoadedWorld:
    """Compiles fresh from records/, in memory, rather than reading a
    package_dir off disk - the same discipline test_citation_cards.py's
    own _real_repository already uses. packages/ is gitignored build
    output (records/ is the source of truth); this local checkout's own
    packages/ directory has at least one world (alx) whose registry-
    current package timestamp points at an empty directory (a build
    artifact from elsewhere in this session's own heavy local test
    running, never actually populated here) - compiling fresh sidesteps
    that entirely rather than depending on this environment's own
    possibly-stale packages/ state."""
    package, manifest_hash = compile_and_hash(world_key=world_key, package_id="G1", records_commit="G1", compiler_version="G1")
    return LoadedWorld(
        world_key=world_key,
        manifest_hash=manifest_hash,
        prompt_text=package["compiled/prompt.txt"].decode("utf-8"),
        capsule_text=package["compiled/capsule.md"].decode("utf-8"),
        repository=json.loads(package["compiled/repository.json"]),
        quotes=json.loads(package["compiled/quotes.json"]),
        figures=json.loads(package["compiled/figures.json"]),
        coverage=json.loads(package["compiled/coverage.json"]),
        frame=json.loads(package["compiled/frame.json"]),
    )


def _proposed_world(world):
    if CITATION_CONTRACT_TAIL_ANCHOR not in world.prompt_text:
        raise RuntimeError(f"{world.world_key}: citation-contract tail anchor not found in compiled prompt_text")
    new_prompt = world.prompt_text.replace(CITATION_CONTRACT_TAIL_ANCHOR, CITATION_CONTRACT_TAIL_ANCHOR + PROPOSED_ADDITION, 1)
    return dataclasses.replace(world, prompt_text=new_prompt)


def run_condition(region: str, *, world_keys: list[str], proposed: bool) -> dict:
    registry = load_registry()
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    per_world = {}
    with tempfile.TemporaryDirectory() as tmp:
        usage_store = UsageLogStore(Path(tmp) / "g1-battery-usage.db")

        for world_key in world_keys:
            world = _compile_world(world_key)
            if proposed:
                world = _proposed_world(world)

            probes = {"A-conflict": CONFLICT_TURN, "B-other-tradition": _other_tradition_turn(world_key, registry)}
            probes_run = 0
            raw_with_offense = 0
            raw_offense_total = 0
            raw_paragraph_turns_by_class = {c: 0 for c in _PARAGRAPH_OFFENSE_CLASSES}
            raw_paragraph_offense_total_by_class = {c: 0 for c in _PARAGRAPH_OFFENSE_CLASSES}

            for probe_id, message in probes.items():
                session_id = f"g1-battery-{'proposed' if proposed else 'current'}-{world_key}-{probe_id}"
                result = _run_probe_turn(
                    client=client, voice_model_id=voice_model_id, safety_model_id=safety_model_id,
                    world=world, world_key=world_key, registry=registry,
                    session_id=session_id, message=message, usage_store=usage_store,
                )
                probes_run += 1
                raw_offenses = result["raw_offenses"]
                if raw_offenses:
                    raw_with_offense += 1
                    raw_offense_total += len(raw_offenses)
                raw_classes_here = {o["class"] for o in result["raw_paragraph_offenses"]}
                for cls in raw_classes_here:
                    raw_paragraph_turns_by_class[cls] += 1
                for o in result["raw_paragraph_offenses"]:
                    raw_paragraph_offense_total_by_class[o["class"]] += 1

            records = []
            for probe_id in probes:
                records += usage_store.read_for_session(f"g1-battery-{'proposed' if proposed else 'current'}-{world_key}-{probe_id}")
            session_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in records) if records else 0.0

            per_world[world_key] = {
                "probes_run": probes_run,
                "raw_turns_with_offense": raw_with_offense,
                "raw_offense_total": raw_offense_total,
                "raw_turn_rate": raw_with_offense / probes_run if probes_run else 0.0,
                "raw_paragraph_turn_rate_by_class": {c: raw_paragraph_turns_by_class[c] / probes_run if probes_run else 0.0 for c in _PARAGRAPH_OFFENSE_CLASSES},
                "raw_paragraph_offense_total_by_class": raw_paragraph_offense_total_by_class,
                "session_dollars": session_dollars,
            }

    total_probes = sum(w["probes_run"] for w in per_world.values())
    total_raw_with_offense = sum(w["raw_turns_with_offense"] for w in per_world.values())
    total_dollars = sum(w["session_dollars"] for w in per_world.values())
    overall_raw_paragraph_turns_by_class = {
        c: sum(round(w["raw_paragraph_turn_rate_by_class"][c] * w["probes_run"]) for w in per_world.values()) for c in _PARAGRAPH_OFFENSE_CLASSES
    }

    return {
        "proposed": proposed,
        "worlds": per_world,
        "overall_probes_run": total_probes,
        "overall_raw_turns_with_offense": total_raw_with_offense,
        "overall_raw_turn_rate": total_raw_with_offense / total_probes if total_probes else 0.0,
        "overall_raw_paragraph_turns_by_class": overall_raw_paragraph_turns_by_class,
        "overall_raw_paragraph_turn_rate_by_class": {c: overall_raw_paragraph_turns_by_class[c] / total_probes if total_probes else 0.0 for c in _PARAGRAPH_OFFENSE_CLASSES},
        "total_dollars": total_dollars,
    }


def run(region: str) -> dict:
    world_keys = [k.strip() for k in WORLDS.split(",")]
    current = run_condition(region, world_keys=world_keys, proposed=False)
    proposed = run_condition(region, world_keys=world_keys, proposed=True)
    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "proposed_addition": PROPOSED_ADDITION,
        "current": current,
        "proposed": proposed,
        "total_dollars": round(current["total_dollars"] + proposed["total_dollars"], 4),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    args = parser.parse_args()

    print(
        "LIVE, BILLED battery: G1 citation-contract wording, interview only "
        f"(11 worlds x 2 probes x 2 conditions = 44 probes), region {args.region}", flush=True,
    )
    report = run(args.region)
    out_path = REPORTS_DIR / f"g1-citation-contract-battery-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    c, p = report["current"], report["proposed"]
    print(f"Real cost: ${report['total_dollars']} ({c['overall_probes_run'] + p['overall_probes_run']} calls)")
    print(f"current  - raw turn rate: {c['overall_raw_turn_rate']:.0%} ({c['overall_raw_turns_with_offense']}/{c['overall_probes_run']}); "
          f"wholly_uncited_paragraph: {c['overall_raw_paragraph_turn_rate_by_class']['wholly_uncited_paragraph']:.0%}")
    print(f"proposed - raw turn rate: {p['overall_raw_turn_rate']:.0%} ({p['overall_raw_turns_with_offense']}/{p['overall_probes_run']}); "
          f"wholly_uncited_paragraph: {p['overall_raw_paragraph_turn_rate_by_class']['wholly_uncited_paragraph']:.0%}")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
