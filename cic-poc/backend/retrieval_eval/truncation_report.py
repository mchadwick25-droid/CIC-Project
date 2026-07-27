"""S3.1 - the real truncation distribution (Pass 1 R2's first step).

Pass 1 Appendix A carries a Medium-confidence "~85% of an Alexandria chunk
truncated" arithmetic; this converts it into measurement. For every chunk
file in every world (lexicon + story), tokenize with the embedding model's
own tokenizer (all-MiniLM-L6-v2, max_seq_length 256) and report:

- CURRENT embedded surface: what create_documents() actually embeds today
  (Term/Aliases/Related + full body; stories: title/tier/confidence + body)
- R1 retrieval surface: term + aliases + related + retrieve_when +
  quick_meaning (stories: title + retrieve_when)

Output: per-world distribution (n, median, p90, max, % over 256 = the
truncation rate) for both surfaces, JSON + printed table. Run:
  python retrieval_eval/truncation_report.py --out <path.json>
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))


def pct(sorted_vals, q):
    if not sorted_vals:
        return None
    i = min(len(sorted_vals) - 1, int(round(q * (len(sorted_vals) - 1))))
    return sorted_vals[i]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    from transformers import AutoTokenizer

    from app.rag.indexer import LexiconIndexer
    from app.rag.story_indexer import StoryIndexer
    from app.world_manifest import WORLD_MANIFEST
    from app.config import settings

    tok = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    MAX = 256

    def ntok(text: str) -> int:
        return len(tok.encode(text, add_special_tokens=True,
                              truncation=False, verbose=False))

    li, si = LexiconIndexer(), StoryIndexer()
    report = {"max_seq_length": MAX, "worlds": {}}
    total = {"current": [], "r1": []}
    n_files = 0

    for entry in WORLD_MANIFEST:
        wid = entry.world_id
        base = settings.data_base_path / entry.data_dir_name
        rows = {"lexicon": {"current": [], "r1": []},
                "story": {"current": [], "r1": []}}
        lex_dir = base / "lexicon_chunks"
        if lex_dir.is_dir():
            for f in sorted(lex_dir.glob("*.md")):
                e = li.parse_lexicon_file(f)
                current = (f"\nTerm: {e.term}\nAliases: {', '.join(e.aliases)}\n"
                           f"Related: {', '.join(e.related_terms)}\n\n{e.content}\n")
                qm = getattr(e, "quick_meaning", "") or ""
                r1 = (f"Term: {e.term}\nAliases: {', '.join(e.aliases)}\n"
                      f"Related: {', '.join(e.related_terms)}\n"
                      f"Retrieve when: {e.retrieve_when}\n"
                      f"Quick meaning: {qm}")
                rows["lexicon"]["current"].append(ntok(current))
                rows["lexicon"]["r1"].append(ntok(r1))
                n_files += 1
        story_dir = base / "story_chunks"
        if story_dir.is_dir():
            for f in sorted(story_dir.glob("*.md")):
                e = si.parse_story_file(f)
                current = (f"\nStory: {e.story_title}\nTier: {e.tier}\n"
                           f"Confidence: {e.confidence}\n\n{e.content}\n")
                r1 = (f"Story: {e.story_title}\n"
                      f"Retrieve when: {e.retrieve_when}")
                rows["story"]["current"].append(ntok(current))
                rows["story"]["r1"].append(ntok(r1))
                n_files += 1
        wrep = {}
        for kind in ("lexicon", "story"):
            for surface in ("current", "r1"):
                vals = sorted(rows[kind][surface])
                if not vals:
                    continue
                total[surface].extend(vals)
                wrep[f"{kind}.{surface}"] = {
                    "n": len(vals), "median": pct(vals, 0.5),
                    "p90": pct(vals, 0.9), "max": vals[-1],
                    "truncated_over_256": sum(1 for v in vals if v > MAX),
                    "truncation_rate": round(
                        sum(1 for v in vals if v > MAX) / len(vals), 3),
                }
        report["worlds"][wid] = wrep

    for surface in ("current", "r1"):
        vals = sorted(total[surface])
        report[f"total.{surface}"] = {
            "n": len(vals), "median": pct(vals, 0.5), "p90": pct(vals, 0.9),
            "max": vals[-1] if vals else None,
            "truncated_over_256": sum(1 for v in vals if v > MAX),
            "truncation_rate": round(
                sum(1 for v in vals if v > MAX) / len(vals), 3) if vals else None,
        }
    report["n_files"] = n_files

    print(f"{'world/kind.surface':52s} {'n':>4} {'med':>5} {'p90':>5} "
          f"{'max':>5} {'>256':>5} {'rate':>6}")
    for wid, wrep in report["worlds"].items():
        for key, s in wrep.items():
            print(f"{wid + '/' + key:52s} {s['n']:>4} {s['median']:>5} "
                  f"{s['p90']:>5} {s['max']:>5} {s['truncated_over_256']:>5} "
                  f"{s['truncation_rate']:>6}")
    for surface in ("current", "r1"):
        s = report[f"total.{surface}"]
        print(f"{'TOTAL.' + surface:52s} {s['n']:>4} {s['median']:>5} "
              f"{s['p90']:>5} {s['max']:>5} {s['truncated_over_256']:>5} "
              f"{s['truncation_rate']:>6}")

    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=2) + "\n",
                                  encoding="utf-8")
        print(f"written: {args.out}")


if __name__ == "__main__":
    main()
