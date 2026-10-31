"""The answer check over a finished test-set run, with no model call
(engine.m4.answer_check). One read of each answer after the bound-drafting step;
one rewrite from what survives when something failed; the same read of the
rewrite; the fallback sentence when too little survives or the rewrite fails.

  python -m engine.m3.test100_check export         --set <set.yaml> --work <run dir> --world lpc
  python -m engine.m3.test100_check import         --set <set.yaml> --work <run dir> --world lpc
  python -m engine.m3.test100_check rewrite-import --set <set.yaml> --work <run dir> --world lpc [--connectives <file.yaml>]
  python -m engine.m3.test100_check final          --set <set.yaml> --work <run dir> --world lpc

Starts from `bound/items.jsonl` (engine.m3.test100_bound). Prompts go to
`check/<stage>/prompts/<question>.md` and replies are read from
`check/<stage>/replies/<question>.txt`; `import` also writes `check/fit.jsonl`, one row per placed passage (the score sheet's fit columns). Stages: `read` (every answer with a bound
sentence or a placed passage), `rewrite` (each answer where something failed and enough
survives), `reread` (each accepted rewrite). `final` writes `check/final/<question>.txt`
and `check/summary.json`. A missing or unreadable reply keeps what it was asked about and
is counted (`pending_*`, `unreadable`); a run is complete only when those are zero.
The prompts carry question wording, so the run directory must lie outside the repository.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import yaml

from engine.m3.test100 import _outside_repo, load_set, question_text
from engine.m4 import answer_check as ac
from engine.m4 import bound_draft, fit_step


def _write_prompt(work: Path, stage: str, key: str, request: dict) -> None:
    base = work / "check" / stage
    (base / "prompts").mkdir(parents=True, exist_ok=True)
    (base / "replies").mkdir(parents=True, exist_ok=True)
    (base / "prompts" / f"{key}.md").write_text(f"SYSTEM\n{request['system']}\n\nUSER\n{request['user']}\n", encoding="utf-8")


def _reply(work: Path, stage: str, key: str) -> str | None:
    path = work / "check" / stage / "replies" / f"{key}.txt"
    return path.read_text(encoding="utf-8") if path.exists() else None


def _save(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")


def _load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


def _answers(questions: list[dict], work: Path) -> list[tuple[dict, list[dict]]]:
    by_question: dict[str, list[dict]] = {}
    for row in _load(work / "bound" / "items.jsonl"):
        by_question.setdefault(row["question_id"], []).append(row)
    return [(q, ac.units(by_question[q["id"]])) for q in questions if q["id"] in by_question]


def _placed_packs(question: dict, units: list[dict], work: Path, records: dict) -> dict[str, str]:
    shape = (json.loads((work / "answers" / f"{question['id']}.json").read_text(encoding="utf-8")).get("reply_shape") or {})
    packs = {}
    for unit in units:
        rid = unit.get("placed_id")
        record = records.get(rid) if unit.get("placed") and rid else None
        if record is not None and record.get("record_type") in ("quote", "story") and rid not in packs:
            packs[rid] = fit_step.fit_pack(record, fit_step.context_blocks(record), (shape.get("story_lengths") or {}).get(rid))
    return packs


def _needs_read(units: list[dict]) -> bool:
    return any(u["records"] or u.get("placed") for u in units)


def export(rows: list, work: Path, records: dict) -> dict:
    written = 0
    for question, units in rows:
        if _needs_read(units):
            _write_prompt(work, "read", question["id"], ac.check_request(question_text(question), units, records, _placed_packs(question, units, work, records)))
            written += 1
    return {"prompts_written": written, "answers": len(rows)}


def import_read(rows: list, work: Path, records: dict) -> dict:
    out, fit_rows, counts = [], [], Counter()
    for question, units in rows:
        qid = question["id"]
        if not _needs_read(units):
            out.append({"question_id": qid, "status": "clean", "units": units, "unsupported": {}, "dropped": []})
            continue
        reply = _reply(work, "read", qid)
        if reply is None:
            counts["pending_read"] += 1
            continue
        parsed = ac.parse_check(reply, units, records)
        if parsed is None:
            counts["unreadable"] += 1
            out.append({"question_id": qid, "status": "clean", "units": units, "unsupported": {}, "dropped": [], "unreadable_reply": True})
            continue
        result = ac.outcome(units, parsed, records)
        counts["unreadable"] += result["unreadable"]
        for rid in dict.fromkeys(u["placed_id"] for u in units if u.get("placed") and u.get("placed_id")):
            if (records.get(rid) or {}).get("record_type") not in ("quote", "story"):
                continue
            judgement = parsed["placed"].get(rid)
            fit_rows.append({"question_id": qid, "record_id": rid, "judgement": judgement, "decision": fit_step.decide(judgement)})
        failed = bool(result["unsupported"] or result["dropped"])
        left = ac.survivors(units, result)
        status = "clean" if not failed else ("rewrite" if ac.words(left) >= ac.SURVIVE_MIN_WORDS else "too_little")
        out.append({"question_id": qid, "status": status, "units": units, "unsupported": {str(i): j for i, j in result["unsupported"].items()}, "dropped": result["dropped"]})
        if status == "rewrite":
            _write_prompt(work, "rewrite", qid, ac.rewrite_request(question_text(question), units, {"unsupported": result["unsupported"], "dropped": result["dropped"]}, records))
            counts["to_rewrite"] += 1
    _save(work / "check" / "read.jsonl", out)
    _save(work / "check" / "fit.jsonl", fit_rows)
    return {"answers": len(out), **counts, **dict(Counter(r["status"] for r in out))}


def import_rewrite(rows: list, work: Path, records: dict, connectives: frozenset[str]) -> dict:
    out, counts = [], Counter()
    for row in _load(work / "check" / "read.jsonl"):
        if row["status"] != "rewrite":
            continue
        qid = row["question_id"]
        reply = _reply(work, "rewrite", qid)
        if reply is None:
            counts["pending_rewrite"] += 1
            continue
        result = {"unsupported": {int(i): j for i, j in row["unsupported"].items()}, "dropped": row["dropped"]}
        kept = ac.survivors(row["units"], result)
        new = ac.parse_rewrite(reply, kept, records, connectives)
        out.append({**row, "rewrite": new})
        if new is None:
            counts["rewrite_refused"] += 1
            continue
        question = next(q for q, _u in rows if q["id"] == qid)
        _write_prompt(work, "reread", qid, ac.check_request(question_text(question), new, records, {}))
        counts["to_reread"] += 1
    _save(work / "check" / "rewrite.jsonl", out)
    return {"rewrites": len(out), **counts}


def final(rows: list, work: Path, records: dict) -> dict:
    read = {r["question_id"]: r for r in _load(work / "check" / "read.jsonl")}
    rewritten = {r["question_id"]: r for r in _load(work / "check" / "rewrite.jsonl")}
    counts: Counter = Counter()
    problems: Counter = Counter()
    out_dir = work / "check" / "final"
    out_dir.mkdir(parents=True, exist_ok=True)
    for question, units in rows:
        qid = question["id"]
        row = read.get(qid)
        if row is None:
            counts["pending_read"] += 1
            continue
        for judgement in row["unsupported"].values():
            problems[judgement.get("problem") or "other"] += 1
        counts["unsupported_sentences"] += len(row["unsupported"])
        counts["placements_dropped"] += len(row["dropped"])
        start = work / "bound" / "final" / f"{qid}.txt"
        if row["status"] == "clean":
            text = start.read_text(encoding="utf-8") if start.exists() else ac.assemble(units)
            counts["clean"] += 1
        elif row["status"] == "too_little":
            text = bound_draft.FALLBACK_ALONE
            counts["abstained_too_little"] += 1
        else:
            rewrite = rewritten.get(qid)
            if rewrite is None:
                counts["pending_rewrite"] += 1
                continue
            if rewrite["rewrite"] is None:
                text = bound_draft.FALLBACK_ALONE
                counts["abstained_rewrite_refused"] += 1
            else:
                reply = _reply(work, "reread", qid)
                if reply is None:
                    counts["pending_reread"] += 1
                    continue
                parsed = ac.parse_check(reply, rewrite["rewrite"], records)
                result = ac.outcome(rewrite["rewrite"], parsed, records) if parsed is not None else None
                if result is None or result["unsupported"] or result["unreadable"]:
                    text = bound_draft.FALLBACK_ALONE
                    counts["abstained_rewrite_failed_read"] += 1
                else:
                    text = ac.assemble(rewrite["rewrite"])
                    counts["rewritten"] += 1
        (out_dir / f"{qid}.txt").write_text(text, encoding="utf-8")
        counts["answers"] += 1
    summary = {**counts, "problems": dict(problems)}
    (work / "check" / "summary.json").write_text(json.dumps(summary, indent=1, sort_keys=True), encoding="utf-8")
    return summary


def main(argv: list[str] | None = None) -> int:
    from engine.m1.loader import load_world_records

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=("export", "import", "rewrite-import", "final"))
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--world", required=True)
    parser.add_argument("--connectives", type=Path)
    args = parser.parse_args(argv)
    work = _outside_repo(args.work)
    records = load_world_records(args.world)
    rows = _answers(load_set(args.question_set), work)
    connectives = bound_draft.connective_set(yaml.safe_load(args.connectives.read_text(encoding="utf-8")) if args.connectives else [])
    result = {
        "export": lambda: export(rows, work, records), "import": lambda: import_read(rows, work, records),
        "rewrite-import": lambda: import_rewrite(rows, work, records, connectives), "final": lambda: final(rows, work, records),
    }[args.command]()
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
