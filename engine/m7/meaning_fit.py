"""Meaning fit: does a sentence that leans on a record use it within what the
record means? Each load-bearing use (a sentence tagged with a citable record)
is read against the record's text and its use note, and graded accepted,
defensible or misread. The bar is scholarly acceptance on meaningful content.

Grading is done offline by an Opus grader, never on the live turn. This
module builds the grader's packet and scores the verdicts. Uses from every
run being compared go into one packet under shuffled ids, so the grader
cannot tell which run a sentence came from; the key that maps ids back to runs
stays beside the packet.

    python -m engine.m7.meaning_fit packet --world rzg --run before=<report> --run after=<report> --out <dir>
    python -m engine.m7.meaning_fit score --dir <dir>

The grader writes <dir>/verdicts.json: {use_id: {"verdict": "accepted" |
"defensible" | "misread", "reason": str}}.
"""
import argparse
import json
import random
import sys
from pathlib import Path

from engine.m1.gates import USE_NOTE_TYPES
from engine.m1.loader import load_world_records, voiced_records
from engine.m4.grounding_net import parse_tagged, split_into_paragraphs

VERDICTS = ("accepted", "defensible", "misread")

_VOICED_TEXT = {
    "quote": ("modern_rendering", "text"),
    "doctrinal_witness": ("text",),
    "term": ("plain_meaning", "quick_meaning"),
    "story": ("tellable_as",),
    "honest_limit": ("statement",),
    "contested_claim": ("claim",),
    "gravity": ("description",),
}


def record_text(record: dict) -> str:
    fields = _VOICED_TEXT.get(record.get("record_type"), ())
    return next((str(record[f]).strip() for f in fields if record.get(f)), "")


def uses_from_report(report: dict, world: str, records: dict[str, dict]) -> list[dict]:
    """Every sentence in the run's answers that carries a tag of a citable
    record, with the paragraph it sits in."""
    citable = {rid: r for rid, r in voiced_records(records).items() if r.get("record_type") in USE_NOTE_TYPES}
    uses = []
    for probe in report["worlds"][world]["per_probe"]:
        raw = (probe.get("transcript") or {}).get("raw_text") or ""
        for paragraph in split_into_paragraphs(raw):
            sentences = parse_tagged(paragraph)
            context = " ".join(s["text"] for s in sentences)
            for sentence in sentences:
                for rid in dict.fromkeys(sentence["tags"]):
                    if rid in citable:
                        uses.append({"probe_id": probe["probe_id"], "sentence": sentence["text"], "paragraph": context,
                                     "record_id": rid, "record_type": citable[rid]["record_type"],
                                     "record_text": record_text(citable[rid]), "use_note": citable[rid].get("use_note")})
    return uses


def build_packet(world: str, runs: dict[str, dict], out_dir: Path, *, seed: int = 0) -> int:
    records = load_world_records(world)
    labelled = [(label, use) for label, report in runs.items() for use in uses_from_report(report, world, records)]
    random.Random(seed).shuffle(labelled)
    packet, key = [], {}
    for i, (label, use) in enumerate(labelled, 1):
        use_id = f"u{i:04d}"
        key[use_id] = label
        packet.append({"use_id": use_id, **{k: v for k, v in use.items() if k != "probe_id"}})
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "packet.json").write_text(json.dumps({"world": world, "uses": packet}, indent=2, ensure_ascii=False) + "\n")
    (out_dir / "key.json").write_text(json.dumps(key, indent=2, sort_keys=True) + "\n")
    return len(packet)


def score(out_dir: Path) -> dict[str, dict]:
    """Per run: how many uses, how many of each verdict, and the misread rate.
    A use with no verdict is counted as ungraded, never as accepted."""
    key = json.loads((out_dir / "key.json").read_text())
    verdicts = json.loads((out_dir / "verdicts.json").read_text())
    runs: dict[str, dict] = {}
    for use_id, label in key.items():
        tally = runs.setdefault(label, {"uses": 0, "ungraded": 0, **{v: 0 for v in VERDICTS}})
        tally["uses"] += 1
        verdict = (verdicts.get(use_id) or {}).get("verdict")
        tally[verdict if verdict in VERDICTS else "ungraded"] += 1
    for tally in runs.values():
        graded = tally["uses"] - tally["ungraded"]
        tally["misread_rate"] = round(tally["misread"] / graded, 4) if graded else None
    return runs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m7.meaning_fit")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("packet")
    p.add_argument("--world", required=True)
    p.add_argument("--run", action="append", required=True, help="label=path to a live admission report with transcripts")
    p.add_argument("--out", required=True)
    p.add_argument("--seed", type=int, default=0)
    s = sub.add_parser("score")
    s.add_argument("--dir", required=True)
    args = parser.parse_args(argv)
    if args.command == "packet":
        runs = {}
        for item in args.run:
            label, _, path = item.partition("=")
            runs[label] = json.loads(Path(path).read_text())
        print(f"{build_packet(args.world, runs, Path(args.out), seed=args.seed)} uses written to {args.out}/packet.json")
        return 0
    print(json.dumps(score(Path(args.dir)), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
