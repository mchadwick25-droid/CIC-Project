"""The bound-drafting step over a finished test-set run, with no model call.
Each sentence the net let through is decided from the draft itself
(engine.m4.bound_draft): kept, or withheld for an inference label, no valid
binding, or talk of confidence tags. When what is left is under
FALLBACK_BELOW_WORDS words and something was withheld, the world's fallback
sentence stands where the first withheld sentence stood: the long form when a bound or
placed sentence comes after it for it to introduce, the short form when nothing after it is bound or placed.

  python -m engine.m3.test100_bound --set <set.yaml> --work <run dir> --world lpc [--connectives <file.yaml>]

The connectives file is a YAML list of the world's reviewed joining sentences;
without it only questions to the visitor stand unbound. Writes `bound/items.jsonl`
(one row per sentence, with its decision), `bound/final/<question>.txt` and
`bound/summary.json`. The run directory carries question wording and must lie
outside the repository.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import yaml

from engine.m3.test100 import _outside_repo, load_set
from engine.m4 import bound_draft
from engine.m4.verify_step import splice

_MARK = "\x00first\x00"


def _position(text: str, sentence: str) -> int:
    marked, found = splice(text, sentence, _MARK)
    return marked.find(_MARK) if found else len(text) + 1


def final_text(text: str, rows: list[dict]) -> tuple[str, bool]:
    """The answer with its withheld sentences out, and whether the fallback stands.
    The fallback stands only if the place of the first withheld sentence was found."""
    withheld = [r["sentence"] for r in rows if r["decision"].startswith("withhold")]
    if not withheld:
        return text, False
    first = min(withheld, key=lambda sentence: _position(text, sentence))
    text, marked = splice(text, first, _MARK)
    rest = list(withheld)
    if marked:
        rest.remove(first)
    for sentence in rest:
        text, _found = splice(text, sentence, None)
    before, _mark, after = text.partition(_MARK)
    if marked and len((before + " " + after).split()) < bound_draft.FALLBACK_BELOW_WORDS:
        tells = any(r["decision"] == "keep" and (r.get("placed") or r.get("records")) and r["sentence"] in after for r in rows)
        return splice(text, _MARK, bound_draft.FALLBACK if tells else bound_draft.FALLBACK_ALONE)[0], True
    return splice(text, _MARK, None)[0], False


def run(questions: list[dict], work: Path, records: dict, connectives: frozenset[str]) -> dict:
    out_dir = work / "bound" / "final"
    out_dir.mkdir(parents=True, exist_ok=True)
    counts: Counter = Counter()
    all_rows = []
    for question in questions:
        path = work / "answers" / f"{question['id']}.json"
        if not path.exists():
            continue
        answer = json.loads(path.read_text(encoding="utf-8"))
        if not answer.get("text"):
            continue
        if answer.get("voice_set_aside"):
            counts["voice_set_aside"] += 1
            continue
        rows = [{**row, "question_id": question["id"]} for row in bound_draft.items(answer, records, connectives)]
        text, fallback = final_text(answer["text"], rows)
        (out_dir / f"{question['id']}.txt").write_text(text, encoding="utf-8")
        all_rows += rows
        counts["answers"] += 1
        counts["fallback_stands"] += fallback
        for row in rows:
            counts[row["decision"]] += 1
            counts[f"label_{row['label'] or 'none'}"] += not row["placed"] and row["decision"] != "withhold_net"
    (work / "bound" / "items.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in all_rows), encoding="utf-8")
    (work / "bound" / "summary.json").write_text(json.dumps(dict(counts), indent=1, sort_keys=True), encoding="utf-8")
    return dict(counts)


def main(argv: list[str] | None = None) -> int:
    from engine.m1.loader import load_world_records

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--world", required=True)
    parser.add_argument("--connectives", type=Path)
    args = parser.parse_args(argv)
    connectives = bound_draft.connective_set(yaml.safe_load(args.connectives.read_text(encoding="utf-8")) if args.connectives else [])
    print(json.dumps(run(load_set(args.question_set), _outside_repo(args.work), load_world_records(args.world), connectives)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
