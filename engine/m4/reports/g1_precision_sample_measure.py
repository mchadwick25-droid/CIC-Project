"""Follow-up to G1's own null-result battery (Decision-Log.md Entry 60):
before the retrofit PR opens, Mark's own ask - the precision of the
detector that produced the 95.5% raw rate. `g1_citation_contract_
battery.py`'s own report only persisted aggregate counts, not the real
flagged-sentence text, so it cannot be sampled directly; this script
re-runs the same battery mechanism (`engine.m4.live_uncited_claims_
battery`'s own `_run_probe_turn`/`CONFLICT_TURN`/`_other_tradition_
turn`), CURRENT citation-contract wording only (the proposed wording
made no measurable difference to the raw rate, Entry 60, so which
condition the sample is drawn from does not bear on the detector's own
precision), 11 worlds x 2 probes = 22 fresh probes, and this time keeps
every raw `find_uncited_claims` offense's own sentence text, per world,
for sampling and hand-reading - an honest methodology note (a fresh
22-probe run, not literally the same 44-probe run, since that run's own
sentence text was never saved) stated plainly rather than glossed over.

Run: python3 -m engine.m4.reports.g1_precision_sample_measure --region us-east-1
"""
import argparse
import json
import pathlib
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1.registry import load_registry
from engine.m4.live_uncited_claims_battery import (
    CONFLICT_TURN,
    _other_tradition_turn,
    _price_for_call_kind,
    _run_probe_turn,
)
from engine.m4.reports.g1_citation_contract_battery import WORLDS, _compile_world
from engine.m8.cost import estimate_cost
from engine.m8.log_store import UsageLogStore
from engine.provider.bedrock import make_client, resolve_model_id

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORTS_DIR = pathlib.Path(__file__).resolve().parent


def run(region: str) -> dict:
    registry = load_registry()
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)
    world_keys = [k.strip() for k in WORLDS.split(",")]

    all_offenses = []  # [{"world_key", "probe_id", "sentence", "class"}]
    per_world_probes = 0

    with tempfile.TemporaryDirectory() as tmp:
        usage_store = UsageLogStore(Path(tmp) / "g1-precision-usage.db")

        for world_key in world_keys:
            world = _compile_world(world_key)
            probes = {"A-conflict": CONFLICT_TURN, "B-other-tradition": _other_tradition_turn(world_key, registry)}
            for probe_id, message in probes.items():
                session_id = f"g1-precision-{world_key}-{probe_id}"
                result = _run_probe_turn(
                    client=client, voice_model_id=voice_model_id, safety_model_id=safety_model_id,
                    world=world, world_key=world_key, registry=registry,
                    session_id=session_id, message=message, usage_store=usage_store,
                )
                per_world_probes += 1
                for o in result["raw_offenses"]:
                    all_offenses.append({"world_key": world_key, "probe_id": probe_id, **o})

        all_records = usage_store.read_all()
        total_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in all_records)

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "probes_run": per_world_probes,
        "total_dollars": round(total_dollars, 4),
        "all_offenses": all_offenses,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    args = parser.parse_args()

    print("LIVE, BILLED battery: G1 precision-sample run, current wording only, 11 worlds x 2 probes = 22 calls", flush=True)
    report = run(args.region)
    out_path = REPORTS_DIR / f"g1-precision-sample-measure-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    print(f"Real cost: ${report['total_dollars']} ({report['probes_run']} probes)")
    print(f"Raw offenses captured: {len(report['all_offenses'])}")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
