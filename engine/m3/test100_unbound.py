"""The unbound-sentence step over a finished test-set run, with no model call.
Each sentence an answer ships that the net withheld is taken out; every other
sentence the voice wrote is classified by a reader; an unbound claim about the
world is taken out, and so is a sentence that says something is missing unless a
record it is bound to states that limit (engine.m4.unbound_step).

  python -m engine.m3.test100_unbound classify-export --set <set.yaml> --work <run dir> --world lpc
  python -m engine.m3.test100_unbound classify-import --set <set.yaml> --work <run dir> --world lpc
  python -m engine.m3.test100_unbound final           --set <set.yaml> --work <run dir> --world lpc

Prompts go to `unbound/classify/prompts/<question>.<n>.md` (n is the sentence's
position in the answer's net output; a rewrite the verify step used is `<n>r`),
replies are read from `unbound/classify/replies/<question>.<n>.txt`. `final`
starts from `verify/final/<question>.txt` when the verify step has run, else from
the answer text, and writes `unbound/final/<question>.txt` and
`unbound/summary.json`. Only sentences that stand in the starting text are
read: one the verify step replaced or removed is not. When withheld limits leave
an answer with no statement of limits, the fallback sentence stands where the
first one stood (not added while any reply for that answer is missing or unreadable). A missing or
unreadable reply keeps its sentence and is counted (`pending_classify`,
`unreadable`); a run is complete only when those are zero. The prompts carry the
question wording, so the run directory must lie outside the repository.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from engine.m3.test100 import _outside_repo, load_set, question_text
from engine.m4 import unbound_step as us
from engine.m4 import verify_step as vs
from engine.m4.verify_step import splice


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


def _rewritten(work: Path, records: dict) -> dict[str, list[dict]]:
    """The sentences the verify step rewrote and used, by question: they ship in
    place of the originals and are classified like any bound sentence of the voice."""
    used: dict[str, list[dict]] = {}
    for row in _load(work / "verify" / "rewrite.jsonl"):
        path = work / "verify" / "reread" / "replies" / f"{row['key']}.txt"
        if row.get("rewrite") and path.exists() and (vs.read_reply(path.read_text(encoding="utf-8"), row["rewrite"], row["bound"], records) or {}).get("supported"):
            used.setdefault(row["question_id"], []).append({"n": f"{row['n']}r", "sentence": row["rewrite"], "bound": True, "records": row["bound"], "withheld": False, "why": None})
    return used


def _answers(questions: list[dict], work: Path, records: dict) -> list[tuple[dict, dict, list[dict]]]:
    out = []
    rewritten = _rewritten(work, records)
    for question in questions:
        path = work / "answers" / f"{question['id']}.json"
        if path.exists():
            answer = json.loads(path.read_text(encoding="utf-8"))
            if answer.get("text"):
                out.append((question, answer, us.shipped_items(answer, records) + rewritten.get(question["id"], [])))
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


def classify_import(rows: list, work: Path, records: dict) -> dict:
    out, pending, unreadable = [], 0, 0
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
            out.append({**item, "key": key, "question_id": question["id"], "judgement": judgement,
                        "decision": us.decide_classified(judgement, item, records)})
    _save(work / "unbound" / "classify.jsonl", out)
    return {"rows": len(out), "missing_replies": pending, "unreadable": unreadable,
            "world_claim": sum(r["decision"] == "withhold" for r in out),
            "limit_not_stated_by_a_record": sum(r["decision"] == "withhold_limit" for r in out),
            "withheld_by_the_net": sum(r["decision"] == "withhold_net" for r in out)}


def final(rows: list, work: Path) -> dict:
    classified = {r["key"]: r for r in _load(work / "unbound" / "classify.jsonl")}
    counts: Counter = Counter()
    out_dir = work / "unbound" / "final"
    out_dir.mkdir(parents=True, exist_ok=True)
    for question, answer, items in rows:
        start = work / "verify" / "final" / f"{question['id']}.txt"
        text = start.read_text(encoding="utf-8") if start.exists() else answer["text"]
        shipped = [i for i in items if splice(text, i["sentence"], None)[1]]
        complete = True
        kept_limits, withheld_limits = 0, []
        for item in shipped:
            key = f"{question['id']}.{item['n']}"
            row = classified.get(key)
            if row is None:
                counts["pending_classify"] += 1
                complete = False
                continue
            decision = row["decision"]
            if row["judgement"] is None and decision == "keep":
                counts["unreadable"] += 1
                complete = False
            counts[decision] += 1
            kept_limits += decision == "keep" and (row["judgement"] or {}).get("kind") == "limit"
            if decision == "withhold_limit":
                withheld_limits.append(item["sentence"])
            elif decision in ("withhold", "withhold_net"):
                text, _found = splice(text, item["sentence"], None)
        if withheld_limits:
            first = min(withheld_limits, key=text.find)
            for sentence in withheld_limits:
                if sentence != first:
                    text, _found = splice(text, sentence, None)
            add_fallback = complete and not kept_limits
            if add_fallback:
                counts["fallback_added"] += 1
            text, _found = splice(text, first, us.LIMIT_FALLBACK if add_fallback else None)
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
    records = load_world_records(args.world)
    rows = _answers(load_set(args.question_set), work, records)
    result = {
        "classify-export": lambda: classify_export(rows, work),
        "classify-import": lambda: classify_import(rows, work, records),
        "final": lambda: final(rows, work),
    }[args.command]()
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
