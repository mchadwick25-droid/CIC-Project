#!/usr/bin/env python3
"""The corpus's author index - who is actually IN the vendored volumes.

WHY THIS EXISTS. The vendored files are volumes, and a volume is the wrong
unit for almost every question worth asking of this corpus - the sources
often carry multiple authors in a single volume, so indexing has to work
by person, not by book. A first attempt at
assignment was keyed by file and therefore wrong: one `out-of-region` ruling
on `anf02` would have declined Clement of Alexandria - the single most
important author for the alx world - along with Tatian, who belongs to syr's
ecology instead. The corpus map (`cic/corpus-map/`) is keyed per work for
exactly this reason. The reverse mistake is just as easy: Origen sits in two
files, Jerome in two, Gregory the Great in two, Chrysostom in six, Augustine
in eight, so a file-keyed review makes a world rule on Augustine eight
separate times and on Origen twice.

DERIVED, NOT ASSERTED - which is the whole point. Every name here is read out
of the file's own CCEL markup, never supplied by a session's own knowledge of
patristics:

  * `<DC.Creator>` slugs are CCEL's own normalised author ids (`clement_alex`,
    `gregory_naz`, `vincent_lerins`). Authoritative where present.
  * `<div1 title="...">` sections carry per-author divisions in the ANF
    volumes, which is where DC.Creator is thinnest - anf01 lists only
    `irenaeus` in its metadata while its div1s name Clement of Rome,
    Mathetes, Polycarp, Ignatius, Barnabas and Justin.

Neither alone is complete, so the index is their union, and the gap between
them is reported rather than papered over: a volume whose two signals
disagree is exactly where a human should look.

MODERN EDITORS ARE NOT AUTHORS. Schaff, Coxe, Menzies, McGiffert, Wace and
Freemantle appear in DC.Creator because they edited or translated the
volume. They are not figures any world can source, and including them would
put "did alx consider Philip Schaff?" on six worlds' review lists.

    python cic/engine/corpus_authors.py             # report
    python cic/engine/corpus_authors.py --write     # regenerate cic/texts/AUTHORS.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXTS_DIR = HERE.parent / "texts"

# NPNF/ANF series editors and translators, in DC.Creator because they made the
# volume, never because they wrote anything in it.
EDITORS = {"schaff", "coxe", "menzies", "mcgiffert", "wace", "freemantlewh", "roberts", "donaldson"}

# div1 titles that are apparatus, not a work: front matter, indexes, editorial
# scaffolding. Matched at the start of the title, case-insensitively.
_APPARATUS = re.compile(
    r"^(title page|second title|series title|table of contents|contents|indexes?|"
    r"index of|subject index|prolegomena|editor|editorial|translator|preface|"
    r"introductory (note|essay)|credits|dedication|genealogical|chronological|"
    r"appended note|excursus|general (introduction|index)|comparative table|"
    r"bibliograph|elucidat|chief events|appendix)",
    re.I,
)

_DC_CREATOR = re.compile(r"<DC\.Creator[^>]*>(.*?)</DC\.Creator>", re.S)
_DIV1_TITLE = re.compile(r'<div1[^>]*\btitle="([^"]{3,90})"')


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:40]


def scan_file(path: Path) -> dict:
    """One volume's two independent author signals, kept apart on purpose so
    the report can show where they disagree."""
    text = path.read_text(encoding="utf-8", errors="replace")
    creators = [c.strip() for c in _DC_CREATOR.findall(text)]
    slugs = [c for c in creators if re.fullmatch(r"[a-z][a-z0-9_]{2,}", c) and c not in EDITORS]
    divisions = [t.strip() for t in _DIV1_TITLE.findall(text) if not _APPARATUS.match(t.strip())]
    return {"dc_creator": slugs, "divisions": divisions}


def _names_author(slug: str, title: str) -> bool:
    """Does this div1 title plainly carry this DC.Creator slug's name?

    Two failure modes matter here:

    SUBSTRING. A bare `in` test matches `leo` inside `leonides` - the same trap
    this project already fixed once in the cross-world checker, where `"Basil"`
    matched `"Basilidean"` and `"Leo"` matched Origen's father. So the primary
    test is a word-boundary match on the slugified title.

    SEPARATORS. A handful of CCEL slugs are written without them -
    `juliusafricanus`, `sulpiciusseverus`, `athenagoras` - while the titles
    slugify to `julius-africanus`. The boundary test cannot see through that,
    so `Julius Africanus` was reported unattributed in a volume whose own
    header names him. The fallback strips separators from both sides, guarded
    on length so a short slug cannot match inside a longer word.

    What this still does NOT fix, deliberately: CCEL spells the slug
    `sulpiciusseverus` and its own div1 title `Sulpitius Severus`. Matching
    across that would need fuzzy comparison, which buys one attribution at the
    cost of false ones. It stays reported.
    """
    stem = slug.split("_")[0]
    slugged = slugify(title)
    # A Latin nominal ending on the title is the same name: CCEL's slug is
    # `commodian` and its own div1 title is "Commodianus.". Kept narrow - `leo`
    # plus an ending is still `leo`, `leous`, `leoi`, none of which reach
    # `leonides`.
    if re.search(rf"(^|-){re.escape(stem)}(us|um|i|o)?($|-)", slugged):
        return True
    return len(stem) >= 10 and stem in slugged.replace("-", "")


def build_index() -> tuple[dict, dict]:
    """Returns (author_slug -> {"files": [...], "titles": [...]}, per_file)."""
    per_file: dict[str, dict] = {}
    authors: dict[str, dict] = defaultdict(lambda: {"files": [], "titles": []})
    for path in sorted(TEXTS_DIR.iterdir()):
        if path.suffix not in (".xml", ".txt"):
            continue
        info = scan_file(path) if path.suffix == ".xml" else {"dc_creator": [], "divisions": []}
        # A plain-text file is a single work, vendored under a name that already
        # says whose it is - there is no markup to read, so the filename's own
        # leading token is the honest answer rather than a guess at its contents.
        if path.suffix == ".txt":
            info["dc_creator"] = [re.split(r"[_.]", path.name)[0]]
        per_file[path.name] = info
        for slug in info["dc_creator"]:
            entry = authors[slug]
            entry["files"].append(path.name)
        # div1 titles are WORKS (and sometimes author sections). They are not
        # minted as authors: an earlier pass did that and produced 183
        # "authors" including `introductory-notice` and `the-gospel-of-peter`.
        # A work is attributed to a DC.Creator slug only when the title plainly
        # carries that author's name; otherwise it is left unattributed and
        # REPORTED, because an unattributed work in a multi-author volume is
        # precisely where CCEL's metadata is thin and a human is needed.
        # A volume with exactly ONE non-editor author is unambiguous: every
        # work in it is his, whether or not the section title says his name.
        # That clears Augustine's eight volumes and Chrysostom's six without
        # anyone asserting anything - "City of God" is Augustine's because
        # npnf102 has no other author in it, not because a session knows so.
        # ...but ONLY for NPNF. The two series divide differently, and it is
        # visible in the data: NPNF `div1`s are WORKS of one author ("City of
        # God", "The Confessions"), while ANF `div1`s are AUTHOR sections
        # ("CLEMENT OF ROME", "POLYCARP", "TATIAN"). Applying the rule to ANF
        # attributed Clement of Rome, Mathetes, Polycarp, Ignatius, Barnabas,
        # Papias and Justin Martyr to IRENAEUS, because anf01 happens to list
        # only `irenaeus` in its metadata. Caught before shipping; the guard is
        # the series, read off the filename, not a judgement about contents.
        is_npnf = path.name.startswith("npnf")
        sole = info["dc_creator"][0] if is_npnf and len(set(info["dc_creator"])) == 1 else None
        for title in info["divisions"]:
            slug = next((s for s in info["dc_creator"] if _names_author(s, title)), None) or sole
            if slug:
                authors[slug]["titles"].append(f"{path.name}: {title}")
            else:
                per_file[path.name].setdefault("unattributed", []).append(title)
    return dict(authors), per_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python cic/engine/corpus_authors.py")
    parser.add_argument("--write", action="store_true", help="regenerate cic/texts/AUTHORS.md")
    parser.add_argument("--json", action="store_true", help="emit the index as JSON")
    args = parser.parse_args(argv)

    authors, per_file = build_index()
    if args.json:
        print(json.dumps({k: v["files"] for k, v in sorted(authors.items())}, indent=2))
        return 0

    multi = {s: v for s, v in authors.items() if len(set(v["files"])) > 1}
    orphaned = {n: i["unattributed"] for n, i in per_file.items() if i.get("unattributed")}
    lines = ["# Corpus author index\n"]
    lines.append(
        "Generated by `cic/engine/corpus_authors.py` from each file's own CCEL markup — "
        "`<DC.Creator>` slugs and `<div1>` section titles. Nothing here is supplied from "
        "outside the files.\n"
    )
    lines.append(
        f"**{len(authors)} authors across {len(per_file)} volumes.** "
        f"{len(multi)} of them span more than one volume, which is why the review unit is the "
        "person and not the book: a file-keyed ruling makes a world decide about Augustine "
        "eight separate times and about Origen twice.\n"
    )
    lines.append("\n## Authors spanning more than one volume\n")
    lines.append("| author | volumes |")
    lines.append("|---|---|")
    for slug, v in sorted(multi.items(), key=lambda kv: -len(set(kv[1]["files"]))):
        lines.append(f"| `{slug}` | " + ", ".join(f"`{f.split('_')[0]}`" for f in sorted(set(v["files"]))) + " |")

    lines.append(
        f"\n## Where CCEL's metadata is thin — {sum(len(v) for v in orphaned.values())} "
        f"work(s) in {len(orphaned)} volume(s) with no author attribution\n"
    )
    lines.append(
        "These `div1` sections could not be attributed to any `DC.Creator` slug in their own "
        "volume. Some are genuinely anonymous (the Didache, the apocrypha, conciliar acts); "
        "some are authors CCEL simply did not list in the metadata — `anf01` names only "
        "`irenaeus` while its sections carry Clement of Rome, Polycarp, Ignatius, Barnabas "
        "and Justin. **This script does not guess which is which.** Attributing them is a "
        "trusted-source question, not one a text scan can answer.\n"
    )
    for name in sorted(orphaned):
        lines.append(f"- **`{name.split('_')[0]}`** ({len(orphaned[name])}): "
                     + ", ".join(t[:38] for t in orphaned[name][:8])
                     + ("…" if len(orphaned[name]) > 8 else ""))

    lines.append("\n## Every author, by volume\n")
    for name in sorted(per_file):
        info = per_file[name]
        found = sorted({s for s in info["dc_creator"]})
        divs = info["divisions"]
        lines.append(f"\n**`{name}`**  ")
        lines.append(f"DC.Creator: {', '.join(f'`{s}`' for s in found) if found else '— none —'}  ")
        if divs:
            lines.append(f"div1 works ({len(divs)}): " + ", ".join(d[:40] for d in divs[:10]) + ("…" if len(divs) > 10 else ""))
        if found and not divs:
            lines.append("div1 works: — none (single-work volume, or no per-work divisions) —")
        if divs and not found:
            lines.append("*(no DC.Creator metadata — div1 titles are the only signal here)*")

    out = "\n".join(lines) + "\n"
    if args.write:
        (TEXTS_DIR / "AUTHORS.md").write_text(out)
        print(f"wrote {TEXTS_DIR / 'AUTHORS.md'} — {len(authors)} authors, {len(multi)} spanning volumes")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
