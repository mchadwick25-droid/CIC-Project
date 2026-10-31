"""The unbound-sentence step over a finished test-set run, with no model call.
Each sentence an answer ships that the net withheld is taken out; every other
sentence the voice wrote is classified by a reader (an unbound claim about the
world is taken out), and a denial of what the world's sources hold, bound or
not, is checked against the shelf by a second reader
(engine.m4.unbound_step).

  python -m engine.m3.test100_unbound classify-export --set <set.yaml> --work <run dir> --world lpc
  python -m engine.m3.test100_unbound classify-import --set <set.yaml> --work <run dir> --world lpc
  python -m engine.m3.test100_unbound final           --set <set.yaml> --work <run dir> --world lpc

Prompts go to `unbound/<stage>/prompts/<question>.<n>.md` (n is the sentence's
position in the answer's net output), replies are read from
`unbound/<stage>/replies/<question>.<n>.txt`. Stages: `classify` (every sentence
the voice wrote that the net did not withhold), `shelf` (each sentence found to be a denial,
with the shelf passages found). `final` starts from `verify/final/<question>.txt`
when the verify step has run, else from the answer text, and writes
`unbound/final/<question>.txt` and `unbound/summary.json`. A missing or unreadable
reply keeps its sentence and is counted (`pending_classify`, `pending_shelf`,
`unreadable`); a run is complete only when those are zero. The prompts carry the
question wording, so the run directory must lie outside the repository.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from engine.m3.test100 import _outside_repo, load_set, question_text
from engine.m4 import unbound_step as us
from engine.m4.leadin_support import shelf_files
from engine.m4.verify_step import splice

TEXTS_ROOT = Path(__file__).resolve().parents[2] / "cic" / "texts"


def _write_prompt(work: Path, stage: str, key: str, request: dict) -> None:
    base = work / "unbound" / stage
    (base / "prompts").mkdir(parents=True, exist_ok=True)
    (base / "replies").mkdir(parents=True, exist_ok=True)
    (base / "prompts" / f"{key}.md").write_text(f"SYSTEM\n{request['system']}\n\nUSER\n{request['user']}\n", encoding="utf-8")


def _reply(work: Path, stage: str, key: str) -> str | None:
    path = work / "unbound" / stage / "replies" / f"{key}.txt"
    return path.read_text(encoding="utf-8") if path.exists() else None


def _save(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")


def _load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


def _answers(questions: list[dict], work: Path, records: dict) -> list[tuple[dict, dict, list[dict]]]:
    out = []
    for question in questions:
        path = work / "answers" / f"{question['id']}.json"
        if path.exists():
            answer = json.loads(path.read_text(encoding="utf-8"))
            if answer.get("text"):
                out.append((question, answer, us.shipped_items(answer, records)))
    return out


def classify_export(rows: list, work: Path) -> dict:
    written = withheld = 0
    for question, _answer, items in rows:
        for item in items:
            if item["withheld"]:
                withheld += 1
                continue
            _write_prompt(work, "classify", f"{question['id']}.{item['n']}", us.classify_request(question_text(question), item["sentence"]))
            written += 1
    return {"prompts_written": written, "withheld_by_the_net": withheld}


def classify_import(rows: list, work: Path, shelf_root: Path = TEXTS_ROOT, world: str = "lpc") -> dict:
    out, pending, unreadable, queries = [], 0, 0, []
    for question, _answer, items in rows:
        for item in items:
            key = f"{question['id']}.{item['n']}"
            if item["withheld"]:
                out.append({**item, "key": key, "question_id": question["id"], "judgement": None, "decision": "withhold_net"})
                continue
            reply = _reply(work, "classify", key)
            if reply is None:
                pending += 1
                continue
            judgement = us.parse_classify(reply)
            unreadable += judgement is None
            decision = us.decide_classified(judgement, item["bound"])
            row = {**item, "key": key, "question_id": question["id"], "judgement": judgement, "decision": decision}
            out.append(row)
            if decision == "shelf_check":
                queries.append((row, question_text(question), us.query_terms(question_text(question), item["sentence"], judgement["denies"])))
    if queries:
        index = us.ShelfIndex(shelf_root, sorted(shelf_files(world)), {t for _r, _q, terms in queries for t in terms})
        for row, question, terms in queries:
            passages = index.search(terms)
            row["passages"] = [{k: p[k] for k in ("file", "lines")} for p in passages]
            _write_prompt(work, "shelf", row["key"], us.shelf_request(question, row["sentence"], row["judgement"]["denies"], passages))
    _save(work / "unbound" / "classify.jsonl", out)
    return {"rows": len(out), "missing_replies": pending, "unreadable": unreadable, "world_claim": sum(r["decision"] == "withhold" for r in out),
            "to_shelf_check": len(queries), "withheld_by_the_net": sum(r["decision"] == "withhold_net" for r in out)}


def final(rows: list, work: Path) -> dict:
    classified = {r["key"]: r for r in _load(work / "unbound" / "classify.jsonl")}
    counts: Counter = Counter()
    out_dir = work / "unbound" / "final"
    out_dir.mkdir(parents=True, exist_ok=True)
    for question, answer, items in rows:
        start = work / "verify" / "final" / f"{question['id']}.txt"
        text = start.read_text(encoding="utf-8") if start.exists() else answer["text"]
        for item in items:
            key = f"{question['id']}.{item['n']}"
            row = classified.get(key)
            if row is None:
                counts["pending_classify"] += 1
                continue
            decision = row["decision"]
            if decision == "shelf_check":
                reply = _reply(work, "shelf", key)
                if reply is None:
                    counts["pending_shelf"] += 1
                    continue
                judgement = us.parse_shelf(reply)
                counts["unreadable"] += judgement is None
                decision = "withhold_shelf" if us.decide_shelf(judgement) == "withhold" else "keep_denial"
            elif row["judgement"] is None and decision == "keep":
                counts["unreadable"] += 1
            counts[decision] += 1
            if decision in ("withhold", "withhold_net", "withhold_shelf"):
                text, found = splice(text, item["sentence"], None)
                counts["not_found_in_text"] += not found
        (out_dir / f"{question['id']}.txt").write_text(text, encoding="utf-8")
    summary = {"answers": len(rows), **counts}
    (work / "unbound" / "summary.json").write_text(json.dumps(summary, indent=1, sort_keys=True), encoding="utf-8")
    return summary


def main(argv: list[str] | None = None) -> int:
    from engine.m1.loader import load_world_records

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=("classify-export", "classify-import", "final"))
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--world", required=True)
    args = parser.parse_args(argv)
    work = _outside_repo(args.work)
    rows = _answers(load_set(args.question_set), work, load_world_records(args.world))
    result = {
        "classify-export": lambda: classify_export(rows, work),
        "classify-import": lambda: classify_import(rows, work, world=args.world),
        "final": lambda: final(rows, work),
    }[args.command]()
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
