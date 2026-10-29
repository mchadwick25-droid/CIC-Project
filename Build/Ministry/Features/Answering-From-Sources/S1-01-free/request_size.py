"""S1-01 free measures: what the live path sends the voice for each sealed probe,
per world, with the reader stubbed (no model call).

The stub reader returns the probe as its one ask and kind "other"; the real reader
would restate the ask and name a kind, so offered records can differ on the live
path. Sizes are characters; tokens are estimated as characters / 4.

Usage: python request_size.py <out.json>
"""
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))

from engine.m1.registry import formation_world_keys, load_registry  # noqa: E402
from engine.m3 import protocol, sealed_probes  # noqa: E402
from engine.m4.turn_prep import prepare_voice_turn_inputs  # noqa: E402
from engine.m4.world_loader import LazyWorldLoader  # noqa: E402
from engine.m4.rhythm import tally_from_transcript  # noqa: E402
from engine.m5.routing import Directive  # noqa: E402
from engine.shape import shape_text  # noqa: E402


def main(out: Path) -> None:
    registry = load_registry()
    loader = LazyWorldLoader()
    shape = len(shape_text())
    rows = {}
    for world_key in sorted(formation_world_keys(registry)):
        entry = registry[world_key]
        world, _ = loader.load(world_key, package_dir=ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
        sizes, offered, no_ground, directive_chars, quotes = [], [], 0, [], []
        for seal in protocol.battery():
            text = sealed_probes.read_probe(seal["probe_id"])["text"]
            ask = Directive(asks=[{"order": 1, "text": text}], kind="other")
            prepared = prepare_voice_turn_inputs(
                world=world, participant_message=text, directive=ask, already_told_ids=set(),
                already_bridged_figure_ids=set(), history=[], previous_kind=None, rhythm=tally_from_transcript([]),
            )
            sizes.append(len(prepared.user_message))
            directive_chars.append(len(prepared.turn_directive or ""))
            ids = prepared.offered_ids
            offered.append(sum(len(v) for v in ids.values()))
            quotes.append(len(ids.get("quote", [])))
            no_ground += prepared.user_message == text
        rows[world_key] = {
            "cached_system_chars": shape + len(world.prompt_text),
            "world_prompt_chars": len(world.prompt_text),
            "user_message_chars_mean": round(statistics.fmean(sizes)),
            "user_message_chars_max": max(sizes),
            "directive_chars_mean": round(statistics.fmean(directive_chars)),
            "offered_records_mean": round(statistics.fmean(offered), 1),
            "offered_quotes_mean": round(statistics.fmean(quotes), 1),
            "probes_with_no_ground": no_ground,
            "probes": len(sizes),
        }
        print(world_key, rows[world_key])
    out.write_text(json.dumps(rows, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
