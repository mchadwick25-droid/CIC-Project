"""A free pre-screen of pool items for the rarer failure classes, so the
labelling stream can be enriched with likely candidates. A cue only decides
which natural items are labelled; it never labels anything, and it is
recorded beside each item so per-class figures can say how the items were
drawn.

  generalisation  a first-person-plural sentence bound only to quote records
                  (one author's words)
  negation_modal  a negation, modal or sweeping quantifier
  false_friend    the head word of one of the world's lexicon terms, in a
                  sentence bound to anything
  embedded_voice  bound to an etic quote record, or to a quote record whose
                  text reports someone else's speech ("they say", "you say")

  python -m goldset.cues --pool <pool.jsonl> --exclude-world lpc --out <cues.jsonl>
  python -m goldset.cues --pool <pool.jsonl> --exclude-world lpc --out <cues.jsonl> --select <draw.jsonl>

With --all-cued, also writes every item that has a cue as a draw, for a later
stream that takes what earlier streams left (goldset.stream --exclude-labelled).

With --select, also writes the draw for a labelling stream: every item with
a generalisation or embedded-voice cue, up to PER_WORLD items per world for
each of the false-friend and negation cues, and a plain random sample of
RANDOM items whatever their cues, so the natural rate of each class can still
be read off the random part. Each drawn item names what drew it.
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

from goldset.common import read_jsonl, records_at, stable_id, write_jsonl

TAKE_ALL = ("generalisation", "embedded_voice")
PER_WORLD = {"false_friend": 12, "negation_modal": 12}
RANDOM = 100
DRAW_SALT = "cue-draw-2026-10-29"

_WE = re.compile(r"\b(we|our|us|ours|ourselves)\b", re.IGNORECASE)
_NEG = re.compile(r"\b(not|never|no|nor|none|nothing|cannot|can't|n't|must|may|might|always|all|every|only|any)\b", re.IGNORECASE)
_REPORTED = re.compile(r"\b(they|you|some|others|he) (say|says|said|claim|claims|claimed|hold|held|think|thought|argue|argued|object|objected)\b", re.IGNORECASE)


def lexicon_words(records: dict) -> set[str]:
    words = set()
    for record in records.values():
        if record.get("record_type") != "term":
            continue
        head = re.split(r"[(/,;]", str(record.get("world_word") or ""))[0].strip().lower()
        if head and len(head) >= 4:
            words.add(head)
    return words


def cues_for(item: dict, records: dict, flagged: set[str]) -> list[str]:
    bound = [records.get(b["id"]) or {} for b in item["bindings"]]
    sentence = item["sentence"]
    found = []
    if _WE.search(sentence) and bound and all(r.get("record_type") == "quote" for r in bound):
        found.append("generalisation")
    if _NEG.search(sentence):
        found.append("negation_modal")
    lowered = sentence.lower()
    if any(re.search(rf"\b{re.escape(w)}\b", lowered) for w in flagged):
        found.append("false_friend")
    if any(r.get("record_type") == "quote" and (r.get("register") == "etic" or _REPORTED.search(" ".join(str(r.get("modern_rendering") or r.get("text") or "").split()))) for r in bound):
        found.append("embedded_voice")
    return found


def draw(rows: list[dict], pool_ids: list[str]) -> list[dict]:
    order = lambda item_id: stable_id("d", DRAW_SALT, item_id, length=16)
    drawn: dict[str, str] = {}
    for row in sorted(rows, key=lambda r: order(r["item_id"])):
        hit = next((c for c in TAKE_ALL if c in row["cues"]), None)
        if hit:
            drawn.setdefault(row["item_id"], f"cue:{hit}")
    for cue, cap in PER_WORLD.items():
        taken: Counter = Counter()
        for row in sorted(rows, key=lambda r: order(r["item_id"])):
            if cue in row["cues"] and row["item_id"] not in drawn and taken[row["world"]] < cap:
                drawn[row["item_id"]] = f"cue:{cue}"
                taken[row["world"]] += 1
    rest = [i for i in sorted(pool_ids, key=order) if i not in drawn]
    for item_id in rest[:RANDOM]:
        drawn[item_id] = "random"
    return [{"item_id": i, "drawn_by": why} for i, why in drawn.items()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--pool", type=Path, required=True)
    parser.add_argument("--exclude-world", action="append", default=[])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--select", type=Path)
    parser.add_argument("--all-cued", type=Path, help="also write every item with a cue as a draw, each drawn by its first cue")
    args = parser.parse_args(argv)
    rows, pool_ids = [], []
    for item in read_jsonl(args.pool):
        if item["world"] in args.exclude_world or item["gate"]["verdict"] == "unmatched":
            continue
        pool_ids.append(item["item_id"])
        records = records_at(item["records_commit"], item["world"])
        found = cues_for(item, records, lexicon_words(records))
        if found:
            rows.append({"item_id": item["item_id"], "world": item["world"], "cues": found})
    write_jsonl(args.out, rows)
    print(json.dumps({"items_with_a_cue": len(rows), "by_cue": Counter(c for r in rows for c in r["cues"])}, sort_keys=True))
    if args.all_cued:
        write_jsonl(args.all_cued, [{"item_id": r["item_id"], "drawn_by": f"cue:{r['cues'][0]}"} for r in rows])
    if args.select:
        drawn = draw(rows, pool_ids)
        write_jsonl(args.select, drawn)
        print(json.dumps({"drawn": len(drawn), "by_reason": Counter(d["drawn_by"] for d in drawn)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
