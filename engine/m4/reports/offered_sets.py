"""Which records every world offers for three sets of questions, offline, no
model call, so a change to evidence selection can be shown to add and never
remove.

  python engine/m4/reports/offered_sets.py run out.json
      the sample questions (sample_questions.json), the 98 canon questions and
      the recorded messages of 13 and 14 October, each against every package's
      newest compiled build: the cells reached and the record ids offered.
      The recorded messages also run as follow-ups (the conversation's earlier
      participant messages as history) and with the previous message as the
      secondary context a Table turn carries, so the paths that cap the cells
      are covered too.
  python engine/m4/reports/offered_sets.py compare base.json head.json
      for each set, how many question-world pairs changed, every pair where a
      record offered on the base is no longer offered on the head (the add-only
      proof: none), and every pair that gained records.

Run `run` on the base and on the branch, then `compare`. Needs the compiled
packages (`python -m engine.m2.cli restore`).
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from engine.m1 import loader
from engine.m4 import evidence as ev
from engine.m4.tests import live11_replay

SAMPLE = pathlib.Path(__file__).resolve().parent / "sample_questions.json"


def _packages():
    for package_dir in sorted(pathlib.Path("packages").iterdir()):
        builds = sorted(package_dir.iterdir()) if package_dir.is_dir() else []
        compiled = builds[-1] / "compiled" if builds else None
        if compiled and (compiled / "repository.json").exists():
            records = ev.repository_records_by_id(json.loads((compiled / "repository.json").read_text()))
            yield package_dir.name, records, json.loads((compiled / "coverage.json").read_text()), ev.thin_topics_for(records)


def _offered(canon, records, coverage, thin, message, *, history=None, secondary_context=None):
    found = ev.assemble_evidence(
        message=message, asks=[{"order": 1, "text": message}], canon_questions=canon,
        coverage=coverage, repository_records=records, thin_topics=thin, kind="what_did",
        history=history, secondary_context=secondary_context,
    )
    return {"cells": [c["cell"] for c in found["cells"]], "offered": [c["id"] for c in found["candidates"]]}


def run(path: str) -> None:
    fleet = loader.load_fleet_records()
    canon = {rid: r for rid, r in fleet.items() if r.get("record_type") == "canon_question"}
    recorded = [(turn["world"], turn["message"], turn["asked"][:-1]) for r in live11_replay.RUNS for turn in live11_replay.turns(r)]
    sets = {"sample": {}, "canon": {}, "recorded": {}, "recorded-follow-up": {}, "recorded-context": {}}
    for world, records, coverage, thin in _packages():
        for question in json.loads(SAMPLE.read_text()):
            sets["sample"][f"{world}|{question}"] = _offered(canon, records, coverage, thin, question)
        for record in canon.values():
            if record.get("cell"):
                sets["canon"][f"{world}|{record['id']}"] = _offered(canon, records, coverage, thin, record["text"])
    packaged = {world: (records, coverage, thin) for world, records, coverage, thin in _packages()}
    for index, (world, message, earlier) in enumerate(recorded):
        if world in packaged:
            records, coverage, thin = packaged[world]
            key = f"{index}|{world}|{message}"
            sets["recorded"][key] = _offered(canon, records, coverage, thin, message)
            if earlier:
                history = [{"role": "user", "content": text} for text in earlier]
                sets["recorded-follow-up"][key] = _offered(canon, records, coverage, thin, message, history=history)
                sets["recorded-context"][key] = _offered(canon, records, coverage, thin, message, secondary_context=earlier[-1])
    pathlib.Path(path).write_text(json.dumps(sets, indent=1))
    print({name: len(pairs) for name, pairs in sets.items()})


def compare(base_path: str, head_path: str) -> int:
    base, head = json.loads(pathlib.Path(base_path).read_text()), json.loads(pathlib.Path(head_path).read_text())
    removed_total = 0
    for name in base:
        changed = removed = 0
        for key, before in base[name].items():
            after = head[name][key]
            lost, gained = set(before["offered"]) - set(after["offered"]), set(after["offered"]) - set(before["offered"])
            changed += bool(lost or gained or before["cells"] != after["cells"])
            if lost:
                removed += len(lost)
                print(f"REMOVED [{name}] {key[:90]!r}: {sorted(lost)}")
            if gained or before["cells"] != after["cells"]:
                print(f"  [{name}] {key[:90]!r}: cells {before['cells']} -> {after['cells']}, +{len(gained)} records")
        print(f"== {name}: {len(base[name])} pairs, {changed} changed, {removed} records removed")
        removed_total += removed
    return removed_total


if __name__ == "__main__":
    command, *arguments = sys.argv[1:]
    sys.exit(1 if {"run": run, "compare": compare}[command](*arguments) else 0)
