"""The candidate pool: every draft sentence of a saved run that the voice bound
to a record, with the binding as drafted and the current gates' decision on it.

Reads the run's per-world reports (each probe's saved `raw_text`, shipped
`answer_text` and `citation_entries`) and the package manifest each world was
pinned to, so the records named are the records the voice was shown. No probe
wording is read or written: an item carries the probe id and cell only.

The gates' decision on each sentence comes from engine/m3/gate_replay.py,
which replays the saved draft through the run's own shaper at the run's own
commit and reproduces every shipped answer. Its rows are joined to the draft
sentences by the sentence as drafted, tags included:
  ok        kept, and its tags became citations
  withhold  kept without its citation, or removed (with the reason)
  unmatched no replay row carries this sentence as drafted (reported)

  python -m goldset.pool --reports <run reports dir> --gates <replay dir> --out <pool.jsonl>
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

from goldset.common import package_for_manifest_hash, read_jsonl, stable_id, write_jsonl
from engine.m4 import grounding_net

_MARKER = re.compile(r"\[\[\s*(quote|story)\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)
def _draft_key(text: str) -> str:
    """Placement drops the full stop after a marker, so the key ignores
    closing punctuation."""
    return " ".join(text.split()).rstrip(" .!?")


def load_gates(gates_dir: Path) -> dict[tuple[str, str, str], dict]:
    """The replay's rows by (world, probe_id, sentence as drafted)."""
    out = {}
    for path in sorted(Path(gates_dir).glob("*.jsonl")):
        for row in read_jsonl(path):
            out.setdefault((row["world"], row["probe_id"], _draft_key(row["draft"])), row)
    return out


def gate_decision(row: dict | None) -> dict:
    if row is None:
        return {"verdict": "unmatched", "why": None, "removed": None, "cited": None}
    return {k: row[k] for k in ("verdict", "why", "removed", "cited")}


def draft_sentences(raw_text: str) -> list[dict]:
    """The draft's sentences in order, as the gates split them."""
    text = grounding_net.strip_markdown(raw_text)
    return [s for paragraph in grounding_net.split_into_paragraphs(text) for s in grounding_net.parse_tagged(paragraph)]


def pool_from_report(report: dict, gates: dict) -> list[dict]:
    items = []
    settings = report["run_settings"]
    for world, block in report["worlds"].items():
        manifest = package_for_manifest_hash(world, settings["package_manifest_hash"][world])
        for probe in block["per_probe"]:
            transcript = probe.get("transcript") or {}
            raw = transcript.get("raw_text")
            if not raw:
                continue
            for index, sentence in enumerate(draft_sentences(raw)):
                markers = [(k.lower(), rid) for k, rid in _MARKER.findall(sentence["raw"])]
                bindings = [{"kind": "record", "id": t} for t in dict.fromkeys(sentence["tags"])]
                bindings += [{"kind": kind, "id": rid} for kind, rid in markers]
                if not bindings:
                    continue
                items.append({
                    "item_id": stable_id("gs", world, probe["probe_id"], str(index), sentence["raw"]),
                    "origin": "natural",
                    "world": world,
                    "probe_id": probe["probe_id"],
                    "cell": probe.get("cell"),
                    "sentence_index": index,
                    "sentence": _MARKER.sub("", sentence["text"]).strip(),
                    "draft": sentence["raw"].strip(),
                    "bindings": bindings,
                    "records_commit": manifest["records_commit"],
                    "package": manifest["_location"],
                    "gate": gate_decision(gates.get((world, probe["probe_id"], _draft_key(sentence["raw"])))),
                })
    return items


def build_pool(reports_dir: Path, gates_dir: Path) -> list[dict]:
    gates = load_gates(gates_dir)
    items = []
    for path in sorted(Path(reports_dir).glob("*.json")):
        report = json.loads(path.read_text(encoding="utf-8"))
        if "run_settings" in report and "worlds" in report:
            items.extend(pool_from_report(report, gates))
    return items


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--reports", type=Path, required=True)
    parser.add_argument("--gates", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    items = build_pool(args.reports, args.gates)
    write_jsonl(args.out, items)
    by_world = Counter(i["world"] for i in items)
    verdicts = Counter((i["gate"]["verdict"], i["gate"]["removed"]) for i in items)
    print(json.dumps({"items": len(items), "by_world": by_world, "gate": {f"{v}{'/removed' if r else ''}": n for (v, r), n in verdicts.items()}}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
