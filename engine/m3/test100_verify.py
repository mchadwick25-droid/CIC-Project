"""The verify and rewrite step over a finished test-set run, with no model call.
Each cited sentence of an answer is read against the records it is bound to
(engine.m4.verify_step); one found unsupported is rewritten once; the rewrite is
read again; a rewrite still unsupported, or refused, is taken out.

  python -m engine.m3.test100_verify export         --set <set.yaml> --work <run dir>
  python -m engine.m3.test100_verify import         --set <set.yaml> --work <run dir>
  python -m engine.m3.test100_verify rewrite-import --set <set.yaml> --work <run dir>
  python -m engine.m3.test100_verify final          --set <set.yaml> --work <run dir>

Each stage writes prompts under `verify/<stage>/prompts/<question>.<n>.md` (n is
the sentence's position in the answer's net output) and reads a judge's replies
from `verify/<stage>/replies/<question>.<n>.txt`. Stages: `read` (every cited
sentence), `rewrite` (each sentence found unsupported), `reread` (each accepted
rewrite). `final` writes `verify/final/<question>.txt` and `verify/summary.json`.
The prompts carry the question wording, so the run directory must lie outside the
repository.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from engine.m3.test100 import _outside_repo, load_set, question_text
from engine.m4 import verify_step as vs


def _dir(work: Path, stage: str, kind: str) -> Path:
    path = work / "verify" / stage / kind
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write_prompt(work: Path, stage: str, key: str, request: dict) -> None:
    (_dir(work, stage, "prompts") / f"{key}.md").write_text(f"SYSTEM\n{request['system']}\n\nUSER\n{request['user']}\n", encoding="utf-8")
    _dir(work, stage, "replies")


def _reply(work: Path, stage: str, key: str) -> str | None:
    path = work / "verify" / stage / "replies" / f"{key}.txt"
    return path.read_text(encoding="utf-8") if path.exists() else None


def _answers(questions: list[dict], work: Path, records: dict) -> list[tuple[dict, dict, list[dict]]]:
    out = []
    for question in questions:
        path = work / "answers" / f"{question['id']}.json"
        if path.exists():
            answer = json.loads(path.read_text(encoding="utf-8"))
            out.append((question, answer, vs.sentence_items(answer, records)))
    return out


def export(rows: list, work: Path, records: dict) -> dict:
    written = held = 0
    for question, _answer, items in rows:
        for item in items:
            if item["held_out"]:
                held += 1
                continue
            _write_prompt(work, "read", f"{question['id']}.{item['n']}", vs.verify_request(item["sentence"], item["bound"], records))
            written += 1
    return {"prompts_written": written, "held_out_no_valid_binding": held}


def import_read(rows: list, work: Path, records: dict) -> dict:
    out, unread, wrote = [], 0, 0
    for question, _answer, items in rows:
        for item in items:
            key = f"{question['id']}.{item['n']}"
            reply = None if item["held_out"] else _reply(work, "read", key)
            if reply is None and not item["held_out"]:
                continue
            judgement = None if item["held_out"] else vs.parse_verify(reply)
            decision = "held_out" if item["held_out"] else vs.decide(judgement)
            unread += judgement is None and not item["held_out"]
            out.append({"key": key, "question_id": question["id"], "n": item["n"], "sentence": item["sentence"], "bound": item["bound"],
                        "judgement": judgement, "decision": decision})
            if decision == "rewrite":
                _write_prompt(work, "rewrite", key, vs.rewrite_request(question_text(question), item["sentence"], judgement, item["bound"], records))
                wrote += 1
    _save(work / "verify" / "read.jsonl", out)
    return {"rows": len(out), "unreadable": unread, "to_rewrite": wrote, "held_out": sum(r["decision"] == "held_out" for r in out)}


def import_rewrite(work: Path, records: dict) -> dict:
    out, wrote = [], 0
    for row in _load(work / "verify" / "read.jsonl"):
        if row["decision"] != "rewrite":
            continue
        reply = _reply(work, "rewrite", row["key"])
        if reply is None:
            continue
        new = vs.parse_rewrite(reply)
        out.append({**row, "rewrite": new})
        if new:
            _write_prompt(work, "reread", row["key"], vs.verify_request(new, row["bound"], records))
            wrote += 1
    _save(work / "verify" / "rewrite.jsonl", out)
    return {"rewrites": len(out), "refused_or_dropped": sum(r["rewrite"] is None for r in out), "to_reread": wrote}


def final(rows: list, work: Path) -> dict:
    read = {r["key"]: r for r in _load(work / "verify" / "read.jsonl")}
    rewritten = {r["key"]: r for r in _load(work / "verify" / "rewrite.jsonl")}
    counts: Counter = Counter()
    problems: Counter = Counter()
    out_dir = work / "verify" / "final"
    out_dir.mkdir(parents=True, exist_ok=True)
    for question, answer, items in rows:
        text = answer["text"]
        for item in items:
            key = f"{question['id']}.{item['n']}"
            row = read.get(key)
            if row is None:
                continue
            counts["checked"] += row["decision"] != "held_out"
            counts["held_out"] += row["decision"] == "held_out"
            if row["decision"] == "keep":
                counts["kept"] += 1
                continue
            if row["decision"] == "held_out":
                text = vs.splice(text, item["sentence"], None)
                continue
            problems[(row["judgement"] or {}).get("problem") or "other"] += 1
            counts["unsupported"] += 1
            new = (rewritten.get(key) or {}).get("rewrite")
            again = vs.parse_verify(_reply(work, "reread", key) or "") if new else None
            if new and (again is None or again["supported"]):
                counts["rewritten_kept"] += 1
                text = vs.splice(text, item["sentence"], new)
            else:
                counts["taken_out"] += 1
                text = vs.splice(text, item["sentence"], None)
        (out_dir / f"{question['id']}.txt").write_text(text, encoding="utf-8")
    summary = {"answers": len(rows), **counts, "problems": dict(problems)}
    (work / "verify" / "summary.json").write_text(json.dumps(summary, indent=1, sort_keys=True), encoding="utf-8")
    return summary


def _save(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")


def _load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


def main(argv: list[str] | None = None) -> int:
    from engine.m1.loader import load_world_records

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=("export", "import", "rewrite-import", "final"))
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--world", default="lpc")
    args = parser.parse_args(argv)
    work = _outside_repo(args.work)
    records = load_world_records(args.world)
    rows = _answers(load_set(args.question_set), work, records)
    result = {
        "export": lambda: export(rows, work, records), "import": lambda: import_read(rows, work, records),
        "rewrite-import": lambda: import_rewrite(work, records), "final": lambda: final(rows, work),
    }[args.command]()
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
