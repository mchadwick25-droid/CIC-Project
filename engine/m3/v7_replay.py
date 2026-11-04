"""The cut-step replay for the V7 controlled test: apply_net run again on each
saved voice draft, so the sentences the cut step removes can be counted the
same way for both arms. No client is built and no model is called.

For each saved record the turn evidence is rebuilt with the arm's own
answering core (engine.m3.v7_run.V7Answerer.prepare): arm a as the admission
run rendered it, arm b with world.frame["reading_context"] set and the reading
cards and lens notes read from --reading-records-dir. apply_net then runs on
the saved raw_text with the arguments V7Answerer.answer gives it, and each
sentence in net_result["reply_shape"]["removed"] is one cut.

Each --saved file is either an admission report (--format admission: the
worlds.<world>.per_probe entries of a graded run's <world>.json, whose
transcripts hold raw_text and answer_text) or a v7_run record file (--format
v7: one JSON line per probe). Each world's package is the one under
--packages-root whose manifest hash equals the hash the saved records name;
when none does the command is refused, unless --allow-package-differ, which
replays on the registered package and marks the world as not matching.

--out receives one JSON line per removed sentence: world, arm, run, probe_id,
cell, reason, removed_sentence, draft, next_shipped and located_in_draft.
next_shipped is the first sentence of the replayed answer that follows the cut
in the draft, or None when the cut is the last or cannot be found in the
draft. <out>.summary.json holds the settings and, per world and in all: the
probes replayed, the probes whose replayed text equals the saved answer_text
byte for byte, the probes whose citation set equals the saved one, the cuts,
the cuts per answer and the cuts by reason. A v7 record also carries the
offered record ids, and the summary counts the probes whose rebuilt evidence
offers the same ids in the same order.

No sealed probe wording is written. A text field that shares a run of
PROBE_RUN_WORDS words with its probe is replaced by WITHHELD, and the summary
counts how many were. --out must lie outside the repository and outside the
main checkout.

Exit codes: 0 done, 2 refused.
"""
import argparse
import dataclasses
import json
import re
import sys
from collections import Counter
from pathlib import Path

from engine.m1.loader import load_fleet_records
from engine.m1.registry import load_registry
from engine.m2.manifest import manifest_hash
from engine.m3 import sealed_probes
from engine.m3.v7_run import (
    ARMS,
    EXIT_REFUSED,
    READING_CONTEXT,
    REPO_ROOT,
    V7Answerer,
    _git,
    _inside_protected,
    reading_refusal,
    seal_hash,
)
from engine.m4 import evidence as m4_evidence
from engine.m4 import grounding_net
from engine.m4.quote_placement import PlacementContext
from engine.m4.reading_cards import load_reading_context
from engine.m4.turn import apply_net
from engine.m4.world_loader import LazyWorldLoader
from engine.shape import shape_hash, shape_text

EXIT_DONE = 0
FORMATS = ("admission", "v7")
PROBE_RUN_WORDS = 6
WITHHELD = "[withheld: shares words with the sealed probe]"
_WORD = re.compile(r"[a-z0-9']+")


class Refused(Exception):
    """The replay cannot run on these inputs; the message says why."""


def saved_records(path: Path, fmt: str) -> list[dict]:
    """The saved drafts as {world, probe_id, cell, raw_text, answer_text, citations,
    offered_record_ids, package_manifest_hash}; a record with no draft or no
    shipped answer is left out."""
    if fmt == "admission":
        report = json.loads(path.read_text(encoding="utf-8"))
        hashes = report["run_settings"]["package_manifest_hash"]
        rows = [
            {"world": world, "probe_id": probe["probe_id"], "cell": probe.get("cell"),
             "raw_text": probe["transcript"].get("raw_text"), "answer_text": probe["transcript"].get("answer_text"),
             "citations": probe["transcript"].get("citations"), "offered_record_ids": None,
             "package_manifest_hash": hashes[world]}
            for world, result in report["worlds"].items() for probe in result["per_probe"]
        ]
    else:
        rows = [
            {"world": r["world"], "probe_id": r["probe_id"], "cell": r.get("cell"), "raw_text": r.get("raw_text"),
             "answer_text": r.get("answer_text"), "citations": r.get("citations"), "offered_record_ids": r.get("offered_record_ids"),
             "package_manifest_hash": r["package_manifest_hash"]}
            for r in (json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
        ]
    return [r for r in rows if r["raw_text"] is not None and r["answer_text"] is not None]


def find_package(packages_root: Path, world: str, wanted_hash: str) -> Path | None:
    """The package directory under packages_root/<world>/ whose manifest hashes to wanted_hash."""
    for manifest_path in sorted((packages_root / world).glob("*/manifest.json")):
        if manifest_hash(json.loads(manifest_path.read_text(encoding="utf-8"))) == wanted_hash:
            return manifest_path.parent
    return None


def _words(text: str) -> list[str]:
    return _WORD.findall(text.lower())


def probe_runs(probe_texts: list[str], run: int = PROBE_RUN_WORDS) -> set[tuple[str, ...]]:
    """Every run of `run` consecutive words in the probe texts."""
    runs = set()
    for probe_text in probe_texts:
        words = _words(probe_text)
        runs.update(tuple(words[i:i + run]) for i in range(len(words) - run + 1))
    return runs


def shares_probe_run(text: str | None, runs: set[tuple[str, ...]], run: int = PROBE_RUN_WORDS) -> bool:
    """Whether text holds one of the probe word runs."""
    if not text:
        return False
    words = _words(text)
    return any(tuple(words[i:i + run]) in runs for i in range(len(words) - run + 1))


def replay_net(answerer: V7Answerer, raw_text: str, probe_text: str, turn_evidence: dict) -> tuple[str, list[dict], dict]:
    """apply_net on raw_text with the arguments V7Answerer.answer passes it."""
    return apply_net(
        raw_text, repository_records=answerer.repository_records, thin_topics=answerer.thin_topics,
        quotable_texts=[probe_text], window_end=(answerer.world.frame.get("time_window") or {}).get("end"),
        placement=PlacementContext.for_evidence(
            turn_evidence["candidates"],
            offered_stories=frozenset(c["id"] for c in turn_evidence["candidates"] if c.get("placeable")),
        ),
    )


def cuts_with_next(raw_text: str, net_result: dict) -> tuple[list[dict], int]:
    """Each removed sentence with the first shipped sentence after it in the
    draft, and the number of shipped sentences not found in the draft. A
    sentence is found by its draft, tags included, in the markdown-scrubbed
    raw text with whitespace collapsed."""
    draft = grounding_net.placed_key(grounding_net.strip_markdown(raw_text))
    shipped, cursor, unlocated = [], 0, 0
    for entry in net_result["sentences"]:
        needle = grounding_net.placed_key(entry.get("draft") or entry["sentence"])
        at = draft.find(needle, cursor) if needle else -1
        if at < 0:
            unlocated += 1
            continue
        cursor = at + len(needle)
        shipped.append((at, entry["sentence"]))
    cuts = []
    for removed in net_result["reply_shape"]["removed"]:
        needle = grounding_net.placed_key(removed.get("draft") or removed["sentence"])
        at = draft.find(needle) if needle else -1
        following = next((sentence for start, sentence in shipped if start > at), None) if at >= 0 else None
        cuts.append({
            "reason": removed["why"], "removed_sentence": removed["sentence"], "draft": removed.get("draft"),
            "next_shipped": following, "located_in_draft": at >= 0,
        })
    return cuts, unlocated


def load_arm_world(world_key: str, wanted_hash: str, *, packages_root: Path, allow_package_differ: bool):
    """The loaded world and its package facts: the package matching wanted_hash, or with
    allow_package_differ the registered one."""
    package_dir = find_package(packages_root, world_key, wanted_hash)
    matches = package_dir is not None
    if not matches:
        if not allow_package_differ:
            raise Refused(f"no package under {packages_root / world_key} has manifest hash {wanted_hash}, the hash the saved "
                          f"{world_key} records name. Refused; --allow-package-differ replays on the registered package.")
        entry = load_registry()[world_key]["package"]
        package_dir = REPO_ROOT / entry["location"]
        wanted_hash = entry["manifest_hash"]
    world, _timing = LazyWorldLoader().load(world_key, package_dir=package_dir, expected_manifest_hash=wanted_hash)
    return world, {"package_dir": str(package_dir.resolve()), "package_manifest_hash": wanted_hash, "package_matches_saved": matches}


def arm_answerer(world, *, arm: str, canon_questions: dict, reading_records_dir: Path | None) -> V7Answerer:
    """V7Answerer as v7_run.main builds it for the arm, with no client."""
    if arm == "a":
        return V7Answerer(world=world, canon_questions=canon_questions, client=None, model_id=None, max_tokens=0,
                          reading_context=False)
    reading = load_reading_context(reading_records_dir, world.world_key)
    if refusal := reading_refusal(reading, m4_evidence.repository_records_by_id(world.repository), str(reading_records_dir)):
        raise Refused(refusal)
    world = dataclasses.replace(world, frame={**world.frame, READING_CONTEXT: True})
    return V7Answerer(world=world, canon_questions=canon_questions, client=None, model_id=None, max_tokens=0,
                      reading_context=True, reading=reading)


def _tally(probes: list[dict]) -> dict:
    cuts = [c for p in probes for c in p["cuts"]]
    offered = [p["offered_ids_equal"] for p in probes if p["offered_ids_equal"] is not None]
    return {
        "probes": len(probes),
        "answer_text_equal": sum(p["text_equal"] for p in probes),
        "citations_equal": sum(p["citations_equal"] for p in probes),
        "offered_ids_compared": len(offered),
        "offered_ids_equal": sum(offered),
        "probes_with_a_cut": sum(1 for p in probes if p["cuts"]),
        "cuts": len(cuts),
        "cuts_per_answer": round(len(cuts) / len(probes), 3) if probes else None,
        "cuts_located_in_draft": sum(c["located_in_draft"] for c in cuts),
        "shipped_sentences_not_located": sum(p["shipped_unlocated"] for p in probes),
        "cuts_by_reason": dict(Counter(c["reason"] for c in cuts).most_common()),
        "text_differs": [p["probe_id"] for p in probes if not p["text_equal"]],
    }


def replay(rows: list[dict], *, arm: str, run: str, packages_root: Path, reading_records_dir: Path | None,
           allow_package_differ: bool) -> tuple[list[dict], dict]:
    """The cut lines and the per-world summary for the saved rows of one arm."""
    canon_questions = load_fleet_records()
    runs = probe_runs([sealed_probes.read_probe(probe_id)["text"] for probe_id in sorted({r["probe_id"] for r in rows})])
    lines, per_world, packages, every_probe, withheld = [], {}, {}, [], 0
    for world_key in sorted({r["world"] for r in rows}):
        world_rows = [r for r in rows if r["world"] == world_key]
        wanted = {r["package_manifest_hash"] for r in world_rows}
        if len(wanted) != 1:
            raise Refused(f"the saved {world_key} records name {len(wanted)} package hashes; replay one package at a time")
        world, packages[world_key] = load_arm_world(world_key, wanted.pop(), packages_root=packages_root,
                                                    allow_package_differ=allow_package_differ)
        answerer = arm_answerer(world, arm=arm, canon_questions=canon_questions, reading_records_dir=reading_records_dir)
        probes = []
        for row in world_rows:
            probe_text = sealed_probes.read_probe(row["probe_id"])["text"]
            turn_evidence = answerer.prepare(probe_text)["turn_evidence"]
            text, citation_entries, net_result = replay_net(answerer, row["raw_text"], probe_text, turn_evidence)
            cuts, shipped_unlocated = cuts_with_next(row["raw_text"], net_result)
            offered = [c["id"] for c in turn_evidence["candidates"]]
            probes.append({
                "probe_id": row["probe_id"], "cuts": cuts, "shipped_unlocated": shipped_unlocated,
                "text_equal": text == row["answer_text"],
                "citations_equal": sorted({rid for e in citation_entries for rid in e["record_ids"]}) == sorted(row["citations"] or []),
                "offered_ids_equal": offered == row["offered_record_ids"] if row["offered_record_ids"] is not None else None,
            })
            for index, cut in enumerate(cuts):
                line = {"world": world_key, "arm": arm, "run": run, "probe_id": row["probe_id"], "cell": row["cell"],
                        "cut_index": index, **cut}
                for field in ("removed_sentence", "draft", "next_shipped"):
                    if shares_probe_run(line[field], runs):
                        line[field] = WITHHELD
                        withheld += 1
                lines.append(line)
        per_world[world_key] = _tally(probes)
        every_probe += probes
    summary = {"packages": packages, "worlds": per_world, "all": _tally(every_probe), "fields_withheld": withheld}
    return lines, summary


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--arm", choices=ARMS, required=True)
    parser.add_argument("--run", required=True, help="a label for the saved run, written on every line")
    parser.add_argument("--saved", required=True, action="append",
                        help="the saved records: an admission report or a v7_run record file; may be given more than once")
    parser.add_argument("--format", choices=FORMATS, required=True)
    parser.add_argument("--out", required=True, help="JSON-lines cut file; <out>.summary.json is written beside it")
    parser.add_argument("--packages-root", default=str(REPO_ROOT / "packages"),
                        help="a packages directory holding <world>/<pin>/manifest.json and compiled/")
    parser.add_argument("--reading-records-dir", help="arm b: the records directory the reading cards and lens notes are read from")
    parser.add_argument("--allow-package-differ", action="store_true",
                        help="replay on the registered package when none matches the saved records' hash")
    parser.add_argument("--overwrite", action="store_true", help="replace an existing cut file and summary")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(sys.argv[1:] if argv is None else argv)
    out = Path(args.out)
    summary_path = Path(f"{out}.summary.json")
    refusal = None
    if _inside_protected(out):
        refusal = f"{out} is inside the repository or its main checkout; the replay writes outside them. Refused."
    elif args.arm == "b" and args.reading_records_dir is None:
        refusal = "--arm b needs --reading-records-dir, the records directory its reading cards and lens notes come from. Refused."
    elif args.arm == "a" and args.reading_records_dir is not None:
        refusal = "--reading-records-dir is for --arm b only. Refused."
    elif not args.overwrite and (existing := [str(p) for p in (out, summary_path) if p.exists()]):
        refusal = f"{', '.join(existing)} exists; pass --overwrite to replace it. Refused."
    if refusal:
        print(refusal, file=sys.stderr, flush=True)
        return EXIT_REFUSED
    rows = [row for saved in args.saved for row in saved_records(Path(saved), args.format)]
    reading_dir = Path(args.reading_records_dir) if args.reading_records_dir else None
    try:
        lines, summary = replay(rows, arm=args.arm, run=args.run, packages_root=Path(args.packages_root),
                                reading_records_dir=reading_dir, allow_package_differ=args.allow_package_differ)
    except Refused as error:
        print(str(error), file=sys.stderr, flush=True)
        return EXIT_REFUSED
    summary = {
        "settings": {
            "arm": args.arm, "run": args.run, "saved": [str(Path(saved).resolve()) for saved in args.saved], "format": args.format,
            "packages_root": str(Path(args.packages_root).resolve()),
            "reading_records_dir": str(reading_dir.resolve()) if reading_dir else None,
            "repo_commit": _git("rev-parse", "HEAD"), "shape_hash": shape_hash(shape_text()), "seal_hash": seal_hash(),
            "model_calls": 0,
        },
        **summary,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(line, ensure_ascii=False) + "\n" for line in lines), encoding="utf-8")
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"worlds": {w: {k: v for k, v in s.items() if k != "text_differs"} for w, s in summary["worlds"].items()},
                      "all": {k: v for k, v in summary["all"].items() if k != "text_differs"}}, indent=2), flush=True)
    return EXIT_DONE


if __name__ == "__main__":
    sys.exit(main())
