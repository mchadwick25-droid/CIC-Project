"""The fit step over a finished test-set run, with no model call. For every
quote or story an answer placed, it builds the fit judge's request
(engine.m4.fit_step), writes it out for whoever judges it, and reads the
replies back into a verdict and a keep-or-drop decision.

  python -m engine.m3.test100_fit export --set <set.yaml> --work <run dir>
  python -m engine.m3.test100_fit import --set <set.yaml> --work <run dir>

`export` writes `fit/prompts/<question>.<record>.md` and an empty `fit/replies`
directory. A judge writes `fit/replies/<question>.<record>.txt` holding the
reply. `import` writes `fit/fit.jsonl`, one row per placed record: the question,
the record, the length told, the judgement and the decision. The prompts carry
the question wording, so the run directory must lie outside the repository.
"""
import argparse
import json
from pathlib import Path

from engine.m3.test100 import _outside_repo, load_set, question_text
from engine.m4 import fit_step


def placed_items(questions: list[dict], answers_dir: Path, records: dict[str, dict], texts_root: Path = fit_step.REPO_ROOT) -> list[dict]:
    items = []
    for question in questions:
        path = answers_dir / f"{question['id']}.json"
        if not path.exists():
            continue
        answer = json.loads(path.read_text(encoding="utf-8"))
        shape = answer.get("reply_shape") or {}
        for record_id in shape.get("placed", []):
            record = records.get(record_id)
            if record is None or record.get("record_type") not in ("quote", "story"):
                continue
            length = (shape.get("story_lengths") or {}).get(record_id)
            items.append({
                "key": f"{question['id']}.{record_id}", "question_id": question["id"], "record_id": record_id, "length": length,
                "request": fit_step.fit_request(question_text(question), record, fit_step.context_blocks(record, texts_root), length, answer["text"]),
            })
    return items


def export(items: list[dict], work: Path) -> int:
    (work / "fit" / "prompts").mkdir(parents=True, exist_ok=True)
    (work / "fit" / "replies").mkdir(exist_ok=True)
    for item in items:
        request = item["request"]
        (work / "fit" / "prompts" / f"{item['key']}.md").write_text(f"SYSTEM\n{request['system']}\n\nUSER\n{request['user']}\n", encoding="utf-8")
    return len(items)


def import_replies(items: list[dict], work: Path) -> list[dict]:
    rows = []
    for item in items:
        path = work / "fit" / "replies" / f"{item['key']}.txt"
        if not path.exists():
            continue
        judgement = fit_step.parse_fit(path.read_text(encoding="utf-8"))
        rows.append({
            "question_id": item["question_id"], "record_id": item["record_id"], "length": item["length"],
            "judgement": judgement, "decision": fit_step.decide(judgement),
        })
    return rows


def main(argv: list[str] | None = None) -> int:
    from engine.m1.loader import load_world_records

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=("export", "import"))
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--world", default="lpc")
    args = parser.parse_args(argv)
    work = _outside_repo(args.work)
    items = placed_items(load_set(args.question_set), work / "answers", load_world_records(args.world))
    if args.command == "export":
        print(json.dumps({"prompts_written": export(items, work)}))
        return 0
    rows = import_replies(items, work)
    (work / "fit").mkdir(parents=True, exist_ok=True)
    (work / "fit" / "fit.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    print(json.dumps({"placed": len(items), "replies": len(rows), "unreadable": sum(r["judgement"] is None for r in rows), "dropped": sum(r["decision"] == "drop" for r in rows)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
