"""Totals and a before-and-after sample from the bench's results.json.

Usage: python summarize.py <results.json> <out.md>
"""
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

STEPS = (0, 1, 2, 3)
NAMES = {0: "V0 today", 1: "V1 marker repair", 2: "V2 + typed quote selected", 3: "V3 + cited quote selected"}


def main(results_path: Path, out_path: Path) -> None:
    rows = json.loads(results_path.read_text(encoding="utf-8"))
    out = [f"{len(rows)} saved drafts; apply_net reproduced the shipped answer on {sum(r['reproduces_shipped'] for r in rows)}.\n"]

    out.append("| Step | Cuts | Probes with a placed quote | Placed quotes the net verified | Orphan flags | Repairs made |")
    out.append("|---|---|---|---|---|---|")
    for step in STEPS:
        v = [r["variants"][str(step)] for r in rows]
        out.append(
            f"| {NAMES[step]} | {sum(len(x['removed']) for x in v)} | {sum(1 for x in v if x['placed'])} | "
            f"{sum(x['placed_ok'] for x in v)} | {sum(x['orphans'] for x in v)} | {sum(len(x['repairs']) for x in v)} |"
        )

    out.append("\nCuts by reason:\n")
    reasons = sorted({c["why"] for r in rows for s in STEPS for c in r["variants"][str(s)]["removed"]})
    out.append("| Reason | " + " | ".join(NAMES[s] for s in STEPS) + " |")
    out.append("|---|" + "---|" * len(STEPS))
    for why in reasons:
        counts = [sum(1 for r in rows for c in r["variants"][str(s)]["removed"] if c["why"] == why) for s in STEPS]
        out.append(f"| {why} | " + " | ".join(map(str, counts)) + " |")

    out.append("\nBy world (V3 against V0):\n")
    out.append("| World | Drafts | Cuts V0 | Cuts V3 | Placed V0 | Placed V3 | Orphans V0 | Orphans V3 |")
    out.append("|---|---|---|---|---|---|---|---|")
    by_world = defaultdict(list)
    for r in rows:
        by_world[r["world"]].append(r)
    for world, items in sorted(by_world.items()):
        def total(step, key):
            return sum(len(i["variants"][str(step)][key]) if key in ("removed", "placed") else i["variants"][str(step)][key] for i in items)
        out.append(
            f"| {world} | {len(items)} | {total(0, 'removed')} | {total(3, 'removed')} | {total(0, 'placed')} | "
            f"{total(3, 'placed')} | {total(0, 'orphans')} | {total(3, 'orphans')} |"
        )

    gained = [r for r in rows if r["variants"]["3"]["repairs"]]
    out.append(f"\nDrafts changed by any repair: {len(gained)}. By first repair step: " + str(dict(Counter(r['variants']['3']['repairs'][0]['step'] for r in gained))) + ".")
    unplaced = [r for r in gained if not r["variants"]["3"]["placed"]]
    out.append(f"Drafts where a repair was made but no quote ended up placed: {len(unplaced)}.")
    worse = [r for r in rows if len(r["variants"]["3"]["removed"]) > len(r["variants"]["0"]["removed"])]
    out.append(f"Drafts with more cuts after repair than before: {len(worse)}.")

    before = sum(len(r["shipped"].split()) for r in gained)
    after = sum(len(r["variants"]["3"]["text"].split()) for r in gained)
    out.append(
        f"Words per changed draft: {before / len(gained):.0f} shipped today, {after / len(gained):.0f} after repair "
        f"(mean change {(after - before) / len(gained):+.0f}). All drafts: "
        f"{sum(len(r['shipped'].split()) for r in rows) / len(rows):.0f} today, "
        f"{sum(len(r['variants']['3']['text'].split()) for r in rows) / len(rows):.0f} after repair."
    )
    random.seed(1029)
    sample = random.sample(gained, min(30, len(gained)))
    out.append("\n## Sample of 30 changed drafts, before and after (for a human read)\n")
    for r in sample:
        v = r["variants"]["3"]
        out.append(f"### {r['world']} {r['probe']} ({r['cell']}); repairs: " + ", ".join(f"V{x['step']} -> {x['record']}" for x in v["repairs"]))
        out.append("\nBefore (shipped today):\n\n> " + r["shipped"].replace("\n", "\n> ") + "\n")
        out.append("After:\n\n> " + v["text"].replace("\n", "\n> ") + "\n")
    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out[:40]))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
