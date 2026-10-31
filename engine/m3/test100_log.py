"""One log record per answer of a finished test-set run, with no model call:
the question, the sub-question the reader named, what was offered, each
sentence's binding, label and decision (engine.m3.test100_bound), the answer
check's judgements, the placement verdicts, how the answer ended, and its final text.

  python -m engine.m3.test100_log --set <set.yaml> --work <run dir>

Reads `answers/`, `bound/items.jsonl`, `check/read.jsonl`, `check/rewrite.jsonl`,
`check/fit.jsonl` and `check/final/`. Writes `log/<question>.json` and
`log/summary.json`. The records carry question wording, so the run directory must
lie outside the repository.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from engine.m3.test100 import _outside_repo, load_set, question_text


def _load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


def _by_question(rows: list[dict]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for row in rows:
        out.setdefault(row["question_id"], []).append(row)
    return out


def ending(read: dict | None, rewrite: dict | None, final: str | None) -> str:
    if read is None or final is None:
        return "incomplete"
    if read["status"] == "clean":
        return "clean"
    if read["status"] == "too_little":
        return "abstained_too_little"
    if rewrite is None:
        return "incomplete"
    if rewrite["rewrite"] is None:
        return "abstained_rewrite_refused"
    return "rewritten" if final and not final.startswith("We do not have that here.") else "abstained_rewrite_failed_read"


def run(questions: list[dict], work: Path) -> dict:
    bound, fit = _by_question(_load(work / "bound" / "items.jsonl")), _by_question(_load(work / "check" / "fit.jsonl"))
    read = {r["question_id"]: r for r in _load(work / "check" / "read.jsonl")}
    rewrite = {r["question_id"]: r for r in _load(work / "check" / "rewrite.jsonl")}
    out_dir = work / "log"
    out_dir.mkdir(parents=True, exist_ok=True)
    counts: Counter = Counter()
    for question in questions:
        path = work / "answers" / f"{question['id']}.json"
        if not path.exists():
            continue
        answer = json.loads(path.read_text(encoding="utf-8"))
        final_path = work / "check" / "final" / f"{question['id']}.txt"
        final = final_path.read_text(encoding="utf-8") if final_path.exists() else None
        how = ending(read.get(question["id"]), rewrite.get(question["id"]), final)
        record = {
            "question_id": question["id"], "group": question["group"], "question": question_text(question),
            "sub_question": answer.get("sub_question"), "offered": answer.get("offered", []),
            "draft": answer.get("raw_text", ""), "shipped_by_net": answer.get("text", ""),
            "sentences": [{k: r[k] for k in ("n", "sentence", "tags", "label", "decision", "reason", "placed", "placed_id")} for r in bound.get(question["id"], [])],
            "read": None if question["id"] not in read else {k: read[question["id"]][k] for k in ("status", "unsupported", "dropped")},
            "placements": [{k: r[k] for k in ("record_id", "judgement", "decision")} for r in fit.get(question["id"], [])],
            "rewrite": (rewrite.get(question["id"]) or {}).get("rewrite"), "ending": how, "final": final,
        }
        (out_dir / f"{question['id']}.json").write_text(json.dumps(record, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        counts["answers"] += 1
        counts[how] += 1
        counts["named_a_sub_question"] += bool(answer.get("sub_question"))
    (out_dir / "summary.json").write_text(json.dumps(dict(counts), indent=1, sort_keys=True), encoding="utf-8")
    return dict(counts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    args = parser.parse_args(argv)
    print(json.dumps(run(load_set(args.question_set), _outside_repo(args.work))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
