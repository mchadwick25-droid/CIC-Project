"""Turns a finished test-set run into the two inputs the gold-set pool reads, so
the judge steps can run over the run's own answers: a run report (each
question's raw draft, shipped answer and citation entries, with the package
manifest hash it was pinned to) and the current gates' verdict on every draft
sentence, taken from the net's own output in the run's answers.

  python -m engine.m3.test100_export --set <lpc_106_questions.yaml> --work <run dir> --out <export dir>

Writes `<out>/reports/report.json` and `<out>/gates/gates.jsonl`. Then, from
Sandbox/Answering-From-Sources:

  python -m goldset.pool --reports <out>/reports --gates <out>/gates --out <pool.jsonl>

The gate rows have the shape engine.m3.gate_replay wrote: world, probe_id, the
sentence as drafted, the sentence as shown, verdict, reason, removed, cited.
"""
import argparse
import json
from pathlib import Path

from engine.m3.test100 import load_set


def gate_rows(world: str, question_id: str, answer: dict) -> list[dict]:
    rows = []
    for entry in answer.get("net_sentences", []):
        rows.append({
            "world": world, "probe_id": question_id, "draft": entry.get("draft") or entry["sentence"], "shown": entry["sentence"],
            "verdict": entry["verdict"], "why": entry.get("why"), "removed": False,
            "cited": entry["verdict"] == "ok" and bool(entry.get("tags")),
        })
    for gone in (answer.get("reply_shape") or {}).get("removed", []):
        rows.append({
            "world": world, "probe_id": question_id, "draft": gone.get("draft") or gone["sentence"], "shown": None,
            "verdict": "withhold", "why": gone["why"], "removed": True, "cited": False,
        })
    return rows


def report_probe(question: dict, answer: dict) -> dict:
    return {
        "probe_id": question["id"], "cell": question.get("cell") or question["group"],
        "transcript": {
            "raw_text": answer.get("raw_text", ""), "answer_text": answer["text"],
            "citation_entries": [dict(e) for e in answer.get("citation_entries") or []],
        },
    }


def build_export(questions: list[dict], answers_dir: Path, world: str, manifest_hash: str) -> tuple[dict, list[dict], list[str]]:
    probes, rows, missing = [], [], []
    for question in questions:
        path = answers_dir / f"{question['id']}.json"
        if not path.exists():
            missing.append(question["id"])
            continue
        answer = json.loads(path.read_text(encoding="utf-8"))
        probes.append(report_probe(question, answer))
        rows.extend(gate_rows(world, question["id"], answer))
    report = {"run_settings": {"package_manifest_hash": {world: manifest_hash}}, "worlds": {world: {"per_probe": probes}}}
    return report, rows, missing


def main(argv: list[str] | None = None) -> int:
    from engine.m1.registry import load_registry

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--world", default="lpc")
    args = parser.parse_args(argv)
    manifest_hash = load_registry()[args.world]["package"]["manifest_hash"]
    report, rows, missing = build_export(load_set(args.question_set), args.work / "answers", args.world, manifest_hash)
    (args.out / "reports").mkdir(parents=True, exist_ok=True)
    (args.out / "gates").mkdir(parents=True, exist_ok=True)
    (args.out / "reports" / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    (args.out / "gates" / "gates.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    print(json.dumps({"questions": len(report["worlds"][args.world]["per_probe"]), "gate_rows": len(rows), "unanswered": len(missing)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
