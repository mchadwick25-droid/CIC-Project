"""Transparency reach: which hard words reach the reader with no bridge.

WHY THIS EXISTS. Mark's read of the live site, 2026-08-09: "it uses
complicated words but no three level transparency or simple ways to say
it." The specific catch was Chloe saying "catechumen" and "Didache" - two
words a tenth-grade reader stops on - while her glossary covers
episkopos, presbyteros, hetaeria and ten more Greek and Latin terms that
nobody would mistake for English. Her glossary bridges the words that
LOOK foreign. It does not bridge the words that look English and are not.

That gap is invisible to every instrument we have. The readability gate
measures syllables and sentence length. `_vocab_reach` (phase2_checkpoint)
measures the SHARE of out-of-list words and deliberately EXCLUDES world
terms, because a bridged world term is flavor, not a vocabulary failure.
Both are right, and between them they hide the case that matters: a word
that is out-of-list AND world-specific AND carries no gloss at all. That
word is not flavor. It is a wall.

So this reads the committed checkpoint artifacts and lists, per world, the
out-of-list words a Representative actually said which NO confirmed gloss
and NO lexicon term line covers. That list is authoring work - the supply
half of worklist item 7 - and it is the only output that matters here.

REPORT ONLY, per the Goodhart rule. No threshold, never a bar. A world is
not "failing" at some coverage rate, and driving a number up by glossing
everything would produce a Representative who lectures. The output is a
candidate list for human authoring judgement, nothing more.

Zero API cost: it reads artifacts that already exist.

Usage (from cic-poc/backend):
  python scripts/transparency_reach.py
  python scripts/transparency_reach.py --world pahc
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

BATTERIES = BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "batteries"
OUTDIR = BATTERIES

WORLDS = {"pahc": "post-apostolic-house-church",
          "ijc": "imperial-juridical-christianity",
          "alx": "alexandria-catechetical",
          "des": "desert-monasticism",
          "syr": "syriac-edessa-nisibis",
          "hal": "hieronymian-ascetic-literary"}

# Artifact prefix per world key - alx/des/syr/hal/ijc/pahc match the file
# names written by phase2_checkpoint.py.
ARTIFACT_GLOB = "{key}_phase2_checkpoint*_full_*.json"

# Words that are out-of-list but are ordinary modern English a B2 reader
# handles, or are function words the frequency table simply lacks. Kept
# short and explicit rather than heuristic - every entry is a judgement,
# and a judgement in a list can be argued with.
_NOT_A_WALL = {
    "didn", "doesn", "wasn", "weren", "hadn", "couldn", "wouldn", "shouldn",
    "isn", "aren", "haven", "hasn", "won", "don", "ll", "ve", "re", "st",
}


def _freq_table() -> set:
    from wrs.gates.core import _alias_freq_table
    return _alias_freq_table()


# Suffix pairs (strip, append) tried against the frequency table, longest
# first. The bundled top-5000 list carries BASE forms only, so a raw
# membership test reports "walked", "gathered", "feels" and "honestly" as
# out-of-list - which is nonsense, and which the first run of this script
# duly printed. A reader who knows "walk" is not stopped by "walked". This
# is deliberately crude morphology, not a stemmer: it only ever REMOVES a
# word from the wall list, so a miss costs a false positive a human will
# discard, never a false negative that hides a real wall.
_SUFFIXES = [
    ("'s", ""), ("s'", ""), ("iness", "y"), ("ingly", ""), ("edly", ""),
    ("ations", "ate"), ("ation", "ate"), ("ies", "y"), ("ied", "y"),
    ("iest", "y"), ("ier", "y"), ("ily", "y"), ("ing", ""), ("ing", "e"),
    ("ness", ""), ("less", ""), ("ment", ""), ("ers", ""), ("est", ""),
    ("ed", ""), ("ed", "e"), ("ly", ""), ("er", ""), ("er", "e"),
    ("es", ""), ("es", "e"), ("s", ""),
]


def _in_english(tok: str, table: set) -> bool:
    """True if the token, or a plausible base form of it, is ordinary
    English. Inflection is not a comprehension wall."""
    if tok in table:
        return True
    for strip, add in _SUFFIXES:
        if len(tok) > len(strip) + 2 and tok.endswith(strip):
            base = tok[:-len(strip)] + add
            if base in table:
                return True
            # doubled final consonant: "stopped" -> "stop"
            if (len(base) > 3 and not add and base[-1] == base[-2]
                    and base[:-1] in table):
                return True
    return False


def _covered_tokens(world_id: str, key: str) -> tuple[set, dict]:
    """Every token already bridged for this world: confirmed-gloss originals
    and glosses, plus each lexicon record's own `term` line and aliases. A
    token here is NOT a wall - the participant has a way through it."""
    covered: set = set()
    detail: dict = {"confirmed_gloss_terms": [], "lexicon_terms": []}
    try:
        from app.prompts.confirmed_glosses import CONFIRMED_GLOSSES
        for g in CONFIRMED_GLOSSES.get(world_id, []):
            detail["confirmed_gloss_terms"].append(g.original)
            covered.update(re.findall(r"[a-z']+", g.original.lower()))
            covered.update(re.findall(r"[a-z']+", g.gloss.lower()))
    except Exception:  # noqa: BLE001
        pass
    import yaml
    world_dir = {"pahc": "pahc_world", "ijc": "imperial_juridical_world",
                 "alx": "alexandria_world", "des": "desert_world",
                 "syr": "syriac_world", "hal": "hieronymian_world"}[key]
    tdir = BACKEND / "wrs" / "records" / world_dir / "term"
    for p in sorted(tdir.glob("*.md")) if tdir.is_dir() else []:
        try:
            fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
        except Exception:  # noqa: BLE001
            continue
        for field in ("term", "aliases"):
            val = fm.get(field)
            for s in ([val] if isinstance(val, str) else (val or [])):
                if isinstance(s, str):
                    detail["lexicon_terms"].append(s) if field == "term" else None
                    covered.update(re.findall(r"[a-z']+", s.lower()))
    return covered, detail


_WORLD_DIR = {"pahc": "pahc_world", "ijc": "imperial_juridical_world",
              "alx": "alexandria_world", "des": "desert_world",
              "syr": "syriac_world", "hal": "hieronymian_world"}


def _world_vocabularies() -> dict:
    """Token set per world, read from that world's own record files. Used as
    a cross-world rarity discriminator, and it is the discriminator that
    makes this report readable.

    The bundled top-5000 list is a WEB-frequency table (google-10000-english).
    It is missing a great deal of ordinary literary English - "cannot",
    "beside", "gathered", "sorrow" are all absent from it - so out-of-list
    alone reports far too much. But a word that is out-of-list AND appears in
    only one or two of the six worlds' records is world vocabulary, not
    ordinary English: no world's records are the place you would find
    "cannot" appearing in one world and nowhere else. Ordinary English is
    ubiquitous across all six corpora by construction; period vocabulary is
    not. That asymmetry is the whole trick."""
    vocab = {}
    for key, wdir in _WORLD_DIR.items():
        toks: set = set()
        root = BACKEND / "wrs" / "records" / wdir
        for p in root.rglob("*.md") if root.is_dir() else []:
            toks.update(re.findall(r"[a-z']{4,}",
                                   p.read_text(encoding="utf-8").lower()))
        vocab[key] = toks
    return vocab


def _rep_turns(art: dict, rep: str | None) -> list:
    out = []
    for section in ("probe", "sustained"):
        sec = art.get(section) or {}
        for m in sec.get("transcript", []) or []:
            if m.get("role") != "assistant":
                continue
            if rep and (m.get("name") or "").lower() != rep:
                continue
            out.append(m)
    return out


def analyze(key: str, artifact: Path, vocab: dict) -> dict:
    world_id = WORLDS[key]
    art = json.loads(artifact.read_text(encoding="utf-8"))
    from app.world_manifest import WORLD_MANIFEST
    entry = next((e for e in WORLD_MANIFEST if e.world_id == world_id), None)
    rep = entry.representative_message_name if entry else None

    table = _freq_table()
    covered, cov_detail = _covered_tokens(world_id, key)
    turns = _rep_turns(art, rep)

    glossed_turns = sum(1 for m in turns if m.get("glosses_used"))
    cited_turns = sum(1 for m in turns if m.get("citations"))
    fired = collections.Counter()
    for m in turns:
        for g in m.get("glosses_used") or []:
            fired[g.get("original") if isinstance(g, dict) else str(g)] += 1

    # The walls: out-of-list, not covered by any gloss or lexicon term, and
    # not a proper noun (a name is a different transparency need - it wants a
    # who-was-this, not a word gloss - so names are reported separately).
    walls, names = collections.Counter(), collections.Counter()
    for m in turns:
        text = m.get("content") or ""
        for raw in re.findall(r"[A-Za-z'’]+", text):
            tok = raw.lower().replace("’", "'")
            if len(tok) < 4 or tok in covered or tok in _NOT_A_WALL:
                continue
            if _in_english(tok, table):
                continue
            # an inflected form of a covered world term is still covered
            if any(tok.startswith(c) and len(c) >= 4 for c in covered):
                continue
            # cross-world rarity: ubiquitous across the six corpora means
            # ordinary English the frequency table simply lacks, not world
            # vocabulary. Only words local to one or two worlds survive.
            in_worlds = sum(1 for v in vocab.values() if tok in v)
            if in_worlds > 2:
                continue
            # capitalized and not sentence-initial -> treat as a name
            idx = text.find(raw)
            prev = text[:idx].rstrip()
            sentence_initial = (not prev) or prev[-1] in ".!?—-:\n"
            if raw[:1].isupper() and not sentence_initial:
                names[raw] += 1
            else:
                walls[tok] += 1

    return {
        "world_id": world_id,
        "artifact": artifact.name,
        "representative_turns": len(turns),
        "turns_with_a_gloss": glossed_turns,
        "turns_with_a_citation": cited_turns,
        "glosses_that_fired": dict(fired.most_common()),
        "confirmed_gloss_count": len(cov_detail["confirmed_gloss_terms"]),
        "lexicon_term_count": len(cov_detail["lexicon_terms"]),
        "unbridged_hard_words": dict(walls.most_common(40)),
        "discriminator": "out-of-list (top-5000, after morphology), not "
                         "covered by any confirmed gloss or lexicon term, "
                         "and present in at most 2 of the 6 worlds' record "
                         "corpora",
        "named_figures_unbridged": dict(names.most_common(25)),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", choices=sorted(WORLDS))
    ap.add_argument("--date", default="2026-08-09")
    args = ap.parse_args()

    keys = [args.world] if args.world else sorted(WORLDS)
    vocab = _world_vocabularies()
    results = {}
    for key in keys:
        cands = sorted(BATTERIES.glob(ARTIFACT_GLOB.format(key=key)))
        cands = [c for c in cands if "VOID" not in c.name]
        if not cands:
            print(f"[tr] {key}: no checkpoint artifact found - skipped")
            continue
        results[key] = analyze(key, cands[-1], vocab)

    print("\n[tr] ============ TRANSPARENCY REACH ============")
    for key, r in results.items():
        print(f"[tr] {key} ({r['artifact']})")
        print(f"[tr]   {r['representative_turns']} turns | "
              f"gloss fired on {r['turns_with_a_gloss']} | "
              f"citation on {r['turns_with_a_citation']}")
        print(f"[tr]   glossary size: {r['confirmed_gloss_count']} confirmed "
              f"glosses over {r['lexicon_term_count']} lexicon terms")
        print(f"[tr]   fired: {list(r['glosses_that_fired']) or 'NONE'}")
        walls = list(r["unbridged_hard_words"])[:12]
        print(f"[tr]   UNBRIDGED HARD WORDS: {', '.join(walls) or 'none'}")
        figs = list(r["named_figures_unbridged"])[:10]
        print(f"[tr]   unbridged names: {', '.join(figs) or 'none'}")

    out = {"scope": "committed checkpoint artifacts - zero API cost",
           "worlds": results,
           "note": "REPORT ONLY - no threshold, never a bar (Goodhart rule). "
                   "An unbridged hard word is a candidate for authoring "
                   "judgement, not a defect count. Driving coverage up by "
                   "glossing everything would produce a Representative who "
                   "lectures, which is the failure this report exists to "
                   "avoid, not to cause."}
    OUTDIR.mkdir(parents=True, exist_ok=True)
    path = OUTDIR / f"transparency_reach_{args.date}.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    print(f"[tr] written: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
