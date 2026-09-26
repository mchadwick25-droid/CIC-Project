"""The 12-record authoring test (memo: Model-Assignment-2026-09-24.md in
this folder). Two authors re-wrote the same 12 renderings from one brief
(Authoring-Brief-12-Records.md, also in this folder). This script blinds
and scores their output; it never edits a record.

  assemble  parse both authors' raw output, put each record's two
            renderings under letters A and B in a random order per record,
            write the blind set (renderings only) and the key (which letter
            is which author, per record, plus each author's self-reported
            model id) to separate files, and print the key file's SHA-256
            so the sealed key can be committed to before it is opened.
  score     run the rendering grader (Haiku 4.5 and Sonnet 4.6, N runs
            each) and the sentence-completeness check on all 24 blind
            renderings; results are reported per letter, never per author.

Real, billed Bedrock calls in `score` - a by-hand, credentialed run.

Run (from the repository root):
  python3 Ministry/Operations/Audits/Tech-Readiness-2026-09/Model-Assignment/authoring_blind_set.py assemble --author-a-raw X --author-b-raw Y --blind OUT.md --key KEY.json
  python3 Ministry/Operations/Audits/Tech-Readiness-2026-09/Model-Assignment/authoring_blind_set.py score --blind OUT.md --region us-east-1
"""
import argparse
import hashlib
import json
import pathlib
import re
import secrets
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[5]))

from engine.m1.reports.rendering_grader_model_study import MODELS
from engine.m1.rendering_fidelity import grade_rendering
from engine.m8.cost import estimate_cost
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

BRIEF = Path(__file__).resolve().parent / "Authoring-Brief-12-Records.md"
SCORE_PATH = Path(__file__).resolve().parent / "Authoring-Test-Scores-2026-09-24.json"

_RECORD = re.compile(r"^### (\S+)\s*\nRENDERING:\s*(.+?)\s*\nNOTE:\s*(.+?)\s*$", re.M | re.S)
_MODEL = re.compile(r"^MODEL:\s*(.+?)\s*$", re.M)
_BLIND = re.compile(r"^### (\S+)\n\n\*\*A:\*\* (.+?)\n\n\*\*B:\*\* (.+?)\n", re.M | re.S)


def brief_records() -> dict[str, str]:
    """record id -> verbatim `text`, in brief order, read from the brief itself."""
    body = BRIEF.read_text(encoding="utf-8").split("## The 12 records", 1)[1]
    out = {}
    for block in re.split(r"^### ", body, flags=re.M)[1:]:
        rid = block.split("\n", 1)[0].strip()
        out[rid] = re.search(r"^> (.+)$", block, re.M).group(1).strip()
    return out


def parse_author(raw: str, expected: list[str]) -> tuple[dict, str | None]:
    found = {m.group(1): {"rendering": m.group(2), "note": m.group(3)} for m in _RECORD.finditer(raw)}
    missing = [r for r in expected if r not in found]
    if missing:
        raise ValueError(f"author output is missing records: {missing}")
    model = _MODEL.search(raw)
    return {r: found[r] for r in expected}, (model.group(1) if model else None)


def assemble(a_raw: Path, b_raw: Path, blind_out: Path, key_out: Path) -> str:
    records = brief_records()
    ids = list(records)
    authors = {}
    for label, path in (("author_1", a_raw), ("author_2", b_raw)):
        renderings, model = parse_author(path.read_text(encoding="utf-8"), ids)
        authors[label] = {"source_file": path.name, "self_reported_model": model, "renderings": renderings}

    key = {"generated": datetime.now(timezone.utc).isoformat(), "authors": {}, "letters": {}}
    for label, a in authors.items():
        key["authors"][label] = {"source_file": a["source_file"], "self_reported_model": a["self_reported_model"]}
    lines = [
        "# Authoring test: blind set",
        "",
        "Each record's two renderings are labelled A and B. The order is random per record; the key is sealed.",
        "",
    ]
    for rid in ids:
        order = ["author_1", "author_2"]
        if secrets.randbelow(2):
            order.reverse()
        key["letters"][rid] = {"A": order[0], "B": order[1]}
        a, b = (authors[o]["renderings"][rid] for o in order)
        lines += [
            f"### {rid}", "",
            f"**A:** {a['rendering']}", "",
            f"**B:** {b['rendering']}", "",
            f"Notes. A: {a['note']} B: {b['note']}", "",
            f"Original `text`: {records[rid]}", "",
        ]
    blind_out.write_text("\n".join(lines), encoding="utf-8")
    key_bytes = (json.dumps(key, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    key_out.write_bytes(key_bytes)
    return hashlib.sha256(key_bytes).hexdigest()


def parse_blind(path: Path) -> dict[str, dict[str, str]]:
    return {m.group(1): {"A": m.group(2).strip(), "B": m.group(3).strip()} for m in _BLIND.finditer(path.read_text(encoding="utf-8"))}


def score(blind: Path, region: str, runs: int, model_keys: list[str]) -> dict:
    from engine.m1.sentence_completeness import check_rendering, load_parsers

    records = brief_records()
    renderings = parse_blind(blind)
    if list(renderings) != list(records):
        raise ValueError("blind set does not hold exactly the brief's 12 records, in order")
    parsers = load_parsers()
    client = make_client(region)
    resolved = {k: resolve_model_id(MODELS[k][0], region) for k in model_keys}

    rows = []
    for rid, pair in renderings.items():
        for letter in ("A", "B"):
            row = {"record_id": rid, "letter": letter, "rendering": pair[letter],
                   "sentence_completeness": check_rendering(parsers, pair[letter]), "grader": {}}
            for key in model_keys:
                calls = []
                for _ in range(runs):
                    start = time.perf_counter()
                    outcome = grade_rendering(client, resolved[key], original=records[rid],
                                              modern_rendering=pair[letter], timeout=60.0)
                    call = {"status": outcome.status, "latency_seconds": round(time.perf_counter() - start, 3)}
                    if outcome.status == "ok":
                        usage = normalize_usage(outcome.raw_usage)
                        call.update(verdict=outcome.value["verdict"], reasoning=outcome.value["reasoning"],
                                    dollars=estimate_cost(usage, MODELS[key][1]).dollars)
                    else:
                        call["detail"] = outcome.value
                    calls.append(call)
                row["grader"][key] = calls
            print(f"{rid:55} {letter} fragments={len(row['sentence_completeness'])} "
                  + " ".join(f"{k}={[c.get('verdict', c['status']) for c in row['grader'][k]]}" for k in model_keys), flush=True)
            rows.append(row)

    summary = {}
    for letter in ("A", "B"):
        mine = [r for r in rows if r["letter"] == letter]
        s = {"renderings": len(mine),
             "renderings_with_a_flagged_sentence": sum(bool(r["sentence_completeness"]) for r in mine),
             "flagged_sentences": sum(len(r["sentence_completeness"]) for r in mine)}
        for key in model_keys:
            ok = [c for r in mine for c in r["grader"][key] if c["status"] == "ok"]
            s[key] = {
                "calls_translation": sum(c["verdict"] == "translation" for c in ok),
                "calls_ok": len(ok),
                "renderings_translation_by_majority": sum(
                    sum(c.get("verdict") == "translation" for c in r["grader"][key]) * 2 > runs for r in mine),
            }
        s["renderings_flagged_by_either_grader_majority"] = sum(
            any(sum(c.get("verdict") not in (None, "translation") for c in r["grader"][k]) * 2 > runs for k in model_keys)
            for r in mine)
        summary[letter] = s
    dollars = sum(c.get("dollars", 0) for r in rows for k in model_keys for c in r["grader"][k])
    return {"generated": datetime.now(timezone.utc).isoformat(), "region": region, "model_ids": resolved,
            "runs_per_rendering": runs, "dollars_total": round(dollars, 4), "summary_by_letter": summary, "renderings": rows}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("assemble")
    a.add_argument("--author-a-raw", type=Path, required=True)
    a.add_argument("--author-b-raw", type=Path, required=True)
    a.add_argument("--blind", type=Path, required=True)
    a.add_argument("--key", type=Path, required=True)
    s = sub.add_parser("score")
    s.add_argument("--blind", type=Path, required=True)
    s.add_argument("--region", required=True)
    s.add_argument("--runs", type=int, default=3)
    s.add_argument("--models", default="haiku,sonnet46")
    s.add_argument("--out", type=Path, default=SCORE_PATH)
    args = parser.parse_args(argv)

    if args.cmd == "assemble":
        print(f"key sha256: {assemble(args.author_a_raw, args.author_b_raw, args.blind, args.key)}")
        return 0
    report = score(args.blind, args.region, args.runs, args.models.split(","))
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["summary_by_letter"], indent=2), f"\n${report['dollars_total']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
