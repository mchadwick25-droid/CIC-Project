"""Which records each world offers for distress, suicide, self-harm, abuse and
grief questions, offline, no model call.

  python engine/m4/reports/safety_offered.py run out.json
      every question in safety_questions.json against every world's newest
      package: the cells reached and the record ids offered.
  python engine/m4/reports/safety_offered.py compare base.json head.json
      the doctrinal witnesses, honest limits and contested claims offered on
      the base and no longer on the head (and the reverse), and how many
      questions changed any offered record.

Run `run` on the base and on the branch, then `compare`. Needs the compiled
packages (`python -m engine.m2.cli restore`).
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from engine.m1 import loader
from engine.m4 import evidence as ev

QUESTIONS = pathlib.Path(__file__).resolve().parent / "safety_questions.json"
KINDS = ("witness", "limit", "contested")


def run(path: str) -> None:
    fleet = loader.load_fleet_records()
    canon = {rid: r for rid, r in fleet.items() if r.get("record_type") == "canon_question"}
    result = {}
    for package_dir in sorted(pathlib.Path("packages").iterdir()):
        compiled = (sorted(package_dir.iterdir()) or [None])[-1]
        if compiled is None or not (compiled / "compiled" / "repository.json").exists():
            continue
        records = ev.repository_records_by_id(json.loads((compiled / "compiled" / "repository.json").read_text()))
        coverage = json.loads((compiled / "compiled" / "coverage.json").read_text())
        thin = ev.thin_topics_for(records)
        for question in json.loads(QUESTIONS.read_text()):
            found = ev.assemble_evidence(
                message=question, asks=[{"order": 1, "text": question}], canon_questions=canon,
                coverage=coverage, repository_records=records, thin_topics=thin, kind="what_did",
            )
            result[f"{package_dir.name}|{question}"] = {
                "cells": [[c["cell"], c["score"]] for c in found["cells"]],
                "offered": [c["id"] for c in found["candidates"]],
            }
    pathlib.Path(path).write_text(json.dumps(result, indent=1))
    print(f"{len(result)} world-question pairs")


def _guarded(ids) -> set[str]:
    return {i for i in ids if any(kind in i.split(".")[1] for kind in KINDS)}


def compare(base_path: str, head_path: str) -> None:
    base, head = json.loads(pathlib.Path(base_path).read_text()), json.loads(pathlib.Path(head_path).read_text())
    changed = 0
    for key in base:
        changed += set(base[key]["offered"]) != set(head[key]["offered"])
        lost = _guarded(base[key]["offered"]) - _guarded(head[key]["offered"])
        gained = _guarded(head[key]["offered"]) - _guarded(base[key]["offered"])
        if lost or gained:
            world, question = key.split("|", 1)
            print(f"{world:11s} {question[:70]!r}\n    cells {base[key]['cells']} -> {head[key]['cells']}\n    no longer offered {sorted(lost)}\n    newly offered {sorted(gained)}")
    print(f"questions with any offered record changed: {changed} of {len(base)}")


if __name__ == "__main__":
    {"run": run, "compare": compare}[sys.argv[1]](*sys.argv[2:])
