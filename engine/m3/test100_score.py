"""The scoring sheet for a finished lpc test-set run: one row per question,
the machine-measured columns filled from the run's answers, and the columns
for human or judge readers left empty.

  python -m engine.m3.test100_score --set <lpc_106_questions.yaml> --work <run dir> --out <sheet.csv>

Measured here: route, words, reading scores (the engine's own turn scorer),
sentences shipped, cuts and their reasons, orphan flags (the S1-L2 bench's
rule, loaded from the bench itself), quotes placed by code, lead-ins repaired,
stories placed, answer records placed, citations. Empty for readers: fit to
the question, answers the question asked, the five quality marks, pass or fail,
still-works, and the judge columns. The fit judge's verdict per placed record and the count of
placements it would drop are filled when `fit/fit.jsonl` exists (engine.m3.test100_fit).

The totals printed at the end split the 28 sealed probes from the rest, so they
stay comparable with the Stage 3 baseline, and report the fit traps (group K)
as their own line.
"""
import argparse
import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from engine.m3.test100 import load_set
from engine.m7.turn_readability import score_turn

REPO_ROOT = Path(__file__).resolve().parents[2]
BENCH = REPO_ROOT / "Build" / "Ministry" / "Features" / "Answering-From-Sources" / "S1-L2" / "bench.py"
READER_COLUMNS = [
    "fit_to_question", "answers_question_asked", "rigor", "accessibility", "craft", "focus", "fabrication",
    "pass_fail", "still_works", "judge_citation_recall", "judge_verifier", "adjudicated_label",
]
MEASURED_COLUMNS = [
    "id", "group", "cluster", "route", "words", "fk", "fre", "sentences_shipped", "cuts", "cut_reasons",
    "orphan_flags", "quotes_placed", "leadins_repaired", "stories_placed", "answer_records_placed", "citations",
    "fit_judge", "fit_drops", "voice_set_aside",
]


def _load_orphans():
    spec = importlib.util.spec_from_file_location("s1_l2_bench", BENCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.orphans


def measure(question: dict, answer: dict, orphans, fit_rows: list[dict] | None = None) -> dict:
    shape = answer.get("reply_shape") or {}
    removed = shape.get("removed", [])
    sentences = answer.get("net_sentences", [])
    score = score_turn(answer["text"])
    return {
        "id": question["id"], "group": question["group"], "cluster": question.get("cluster", ""),
        "route": answer["routing_action"], "words": score.words,
        "fk": None if score.fk is None else round(score.fk, 1), "fre": None if score.fre is None else round(score.fre, 1),
        "sentences_shipped": len(sentences), "cuts": len(removed),
        "cut_reasons": "; ".join(f"{why} x{n}" for why, n in sorted(Counter(e["why"] for e in removed).items())),
        "orphan_flags": orphans(answer.get("raw_text", ""), answer["text"]) if answer.get("raw_text") else 0,
        "quotes_placed": sum(1 for s in sentences if s.get("placed_quote")),
        "leadins_repaired": len(shape.get("repaired", [])),
        "stories_placed": sum(1 for s in sentences if s.get("placed_story")),
        "answer_records_placed": sum(1 for s in sentences if s.get("placed_answer")),
        "citations": len(answer.get("citations", [])),
        "fit_judge": "; ".join(f"{r['record_id']}: {(r['judgement'] or {}).get('fit', 'unreadable')}" for r in fit_rows or []),
        "fit_drops": sum(r["decision"] == "drop" for r in fit_rows or []),
        "voice_set_aside": bool(answer.get("voice_set_aside")),
    }


def _totals(rows: list[dict]) -> dict:
    graded = [r for r in rows if r["fk"] is not None]
    return {
        "answers": len(rows), "voice_set_aside": sum(r["voice_set_aside"] for r in rows), "cuts": sum(r["cuts"] for r in rows), "orphan_flags": sum(r["orphan_flags"] for r in rows),
        "quotes_placed": sum(r["quotes_placed"] for r in rows),
        "answers_with_a_quote_placed": sum(1 for r in rows if r["quotes_placed"]),
        "leadins_repaired": sum(r["leadins_repaired"] for r in rows),
        "stories_placed": sum(r["stories_placed"] for r in rows),
        "mean_words": round(sum(r["words"] for r in rows) / len(rows), 1) if rows else None,
        "mean_fk": round(sum(r["fk"] for r in graded) / len(graded), 1) if graded else None,
        "mean_fre": round(sum(r["fre"] for r in graded) / len(graded), 1) if graded else None,
    }


def build_sheet(questions: list[dict], answers_dir: Path, fit_path: Path | None = None) -> tuple[list[dict], list[str]]:
    orphans = _load_orphans()
    fit_by_question: dict[str, list[dict]] = {}
    for line in (fit_path.read_text(encoding="utf-8").splitlines() if fit_path and fit_path.exists() else []):
        row = json.loads(line)
        fit_by_question.setdefault(row["question_id"], []).append(row)
    rows, missing = [], []
    for question in questions:
        path = answers_dir / f"{question['id']}.json"
        if not path.exists():
            missing.append(question["id"])
            continue
        rows.append(measure(question, json.loads(path.read_text(encoding="utf-8")), orphans, fit_by_question.get(question["id"])))
    return rows, missing


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    rows, missing = build_sheet(load_set(args.question_set), args.work / "answers", args.work / "fit" / "fit.jsonl")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MEASURED_COLUMNS + READER_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({
        "unanswered": len(missing), "unanswered_ids": missing if len(missing) <= 10 else missing[:10] + ["..."],
        "sealed_probes_28": _totals([r for r in rows if r["group"] == "A"]),
        "all_other_questions": _totals([r for r in rows if r["group"] not in ("A", "K")]),
        "fit_traps": _totals([r for r in rows if r["group"] == "K"]),
    }, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
