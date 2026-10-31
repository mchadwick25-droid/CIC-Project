"""Calibration of the fit step on planted pairs. Each pair is a visitor
question and a quote or story record of the lpc world. A planted pair shares
words or a topic with the record, but the record in its own context does not
answer the question (expected `off_point`); a control pair is one the record
answers (expected `fits`). The fit step must drop at least 19 of 20 planted
pairs before its verdicts count, and the controls show what it wrongly drops.

  python -m goldset.fit export --pairs <pairs.yaml> --dir <work>
  python -m goldset.fit import --pairs <pairs.yaml> --dir <work> --model <name> --out <fit.jsonl>
  python -m goldset.fit score  --pairs <pairs.yaml> --verdicts <fit.jsonl> [--out <score.json>]

`export` writes `<dir>/prompts/<pair>.md` and an empty `<dir>/replies`; a judge
writes `<dir>/replies/<pair>.txt`. The decision for each pair is the fit step's
own (engine.m4.fit_step.decide): off-point is dropped, partly is dropped unless
the answer states the limit (a pair has no answer text), fits is kept. An
unreadable reply counts as not judged, in neither count.
"""
import argparse
import json
import time
from pathlib import Path

import yaml

from goldset.common import REPO_ROOT  # noqa: F401  (puts the repository root on the import path)
from engine.m1.loader import load_world_records
from engine.m4 import fit_step

BAR = 19


def load_pairs(path: Path) -> list[dict]:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))["pairs"]


def pair_request(pair: dict, records: dict[str, dict]) -> dict:
    record = records[pair["record_id"]]
    return fit_step.fit_request(pair["question"], record, fit_step.context_blocks(record), pair.get("length"))


def export_prompts(pairs: list[dict], records: dict[str, dict], work: Path) -> int:
    (work / "prompts").mkdir(parents=True, exist_ok=True)
    (work / "replies").mkdir(exist_ok=True)
    for pair in pairs:
        request = pair_request(pair, records)
        (work / "prompts" / f"{pair['pair_id']}.md").write_text(f"SYSTEM\n{request['system']}\n\nUSER\n{request['user']}\n", encoding="utf-8")
    return len(pairs)


def import_replies(pairs: list[dict], model: str, work: Path) -> list[dict]:
    rows = []
    for pair in pairs:
        path = work / "replies" / f"{pair['pair_id']}.txt"
        if not path.exists():
            continue
        judgement = fit_step.parse_fit(path.read_text(encoding="utf-8"))
        rows.append({
            "pair_id": pair["pair_id"], "model_id": model, "judgement": judgement, "decision": fit_step.decide(judgement) if judgement else None,
            "route": "in plan (Claude Code subagent), no metered call", "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        })
    return rows


def score(pairs: list[dict], rows: list[dict]) -> dict:
    by_id = {r["pair_id"]: r for r in rows}
    out: dict = {"bar": f"{BAR} of 20 planted pairs dropped"}
    for kind, wanted in (("planted", "drop"), ("control", "keep")):
        group = [p for p in pairs if p["kind"] == kind]
        judged = [p for p in group if by_id.get(p["pair_id"], {}).get("decision")]
        right = [p for p in judged if by_id[p["pair_id"]]["decision"] == wanted]
        out[kind] = {
            "pairs": len(group), "judged": len(judged), "unreadable_or_missing": len(group) - len(judged),
            "right": len(right), "wrong": [p["pair_id"] for p in judged if p not in right],
            "verdicts": {v: sum(by_id[p["pair_id"]]["judgement"]["fit"] == v for p in judged) for v in fit_step.VERDICTS},
        }
    planted = out["planted"]
    out["planted_dropped"] = planted["right"]
    out["meets_bar"] = planted["unreadable_or_missing"] == 0 and planted["right"] >= BAR
    out["controls_wrongly_dropped"] = len(out["control"]["wrong"])
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("export", "import", "score"):
        p = sub.add_parser(name)
        p.add_argument("--pairs", type=Path, required=True)
        if name != "score":
            p.add_argument("--dir", type=Path, required=True)
        if name == "import":
            p.add_argument("--model", required=True)
        if name in ("import", "score"):
            p.add_argument("--out", type=Path, required=name == "import")
        if name == "score":
            p.add_argument("--verdicts", type=Path, required=True)
    args = parser.parse_args(argv)
    pairs = load_pairs(args.pairs)
    if args.command == "export":
        print(json.dumps({"prompts_written": export_prompts(pairs, load_world_records("lpc"), args.dir)}))
        return 0
    if args.command == "import":
        rows = import_replies(pairs, args.model, args.dir)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
        print(json.dumps({"pairs": len(pairs), "replies": len(rows), "unreadable": sum(r["judgement"] is None for r in rows)}))
        return 0
    rows = [json.loads(line) for line in args.verdicts.read_text(encoding="utf-8").splitlines() if line.strip()]
    result = score(pairs, rows)
    text = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
