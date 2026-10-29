"""Check and sample a hand curation.

  python -m answering_library.curate check <file-stem> [--curation-dir DIR]
  python -m answering_library.curate sample <file-stem> [--n 12] [--context 4] [--out FILE]

check segments the file under curation/<file-stem>.yaml and prints the class
before (heuristic markers) and after, the number of divisions, address
uniqueness, coverage, oversize divisions, the divisions evenly spaced through
the file for human sampling, and the completeness checks. It exits 1 when any
check fails, 2 when the curation file cannot be loaded or applied.

A file is class 'curated' when all of these hold:
  - every division address (division_locus) is unique;
  - divisions and declared apparatus ranges cover at least 95% of the text
    that is neither library header nor declared furniture;
  - no body division is over 5,000 words, unless its rule or entry carries an
    allow_oversize justification (apparatus divisions are exempt);
  - every rule matched, every fix landed on a match, and every evidence quote
    appears on the line it cites;
  - passage words plus declared furniture words equal the words of the file;
  - every passage byte range, re-read from the vendored file, reproduces the
    passage text, less only words on declared furniture lines.

The file is read from cic/texts without the union of shelves (reading the union
takes about 40 seconds); only a curation that lists speakers loads the union, to
check each named voice against the file's authors.

sample writes a review packet for the second reader to <out>/review/<stem>.md
(the out directory is gitignored): scheme, evidence, the sampled divisions with
the lines around them, the extremes in size, the apparatus ranges and the check.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

from . import curation as cu
from . import segment
from .run import DEFAULT_OUT
from .textio import Source
from .union import TEXTS_DIR, build_union

SAMPLE_WORDS = 25
DEFAULT_SAMPLE = 12


@dataclass
class Result:
    ok: bool
    lines: list[str]
    sampled: list
    resolved: cu.Resolved
    curation: cu.Curation
    entry: object
    work: str


def entry_for(filename: str, union: bool = False):
    """The union entry for a file. Reading the union takes tens of seconds, so by default
    the file gets a bare entry: segmentation, class and every check are the same, and only
    the speaker voices a curation may name need the real authors."""
    if union:
        for e in build_union():
            if e.filename == filename:
                return e
        raise cu.CurationError(f"{filename} is not in the union of shelves")
    path = TEXTS_DIR / filename
    if not path.exists():
        raise cu.CurationError(f"{filename} is not in cic/texts")
    return SimpleNamespace(filename=filename, path=path, suffix=path.suffix, authors=[], row_ids=[], worlds=[],
                           size=path.stat().st_size)


def sample_indices(count: int, n: int) -> list[int]:
    if count <= n:
        return list(range(count))
    if n == 1:
        return [0]
    return sorted({round(k * (count - 1) / (n - 1)) for k in range(n)})


def _words(text: str, start: int, end: int, limit: int) -> str:
    return " ".join(text[start:end].split()[:limit])


def run_check(cur: cu.Curation, entry, n: int = DEFAULT_SAMPLE) -> Result:
    src = Source.read(entry.path)
    before = segment.plan(entry, src, curation=None)
    records, summary = segment.segment(entry, None, src, curation=cur)
    p = segment.plan(entry, src, curation=cur)
    res, m, work = p.curated.resolved, p.curated.measure, p.curated.work
    ev = summary["evidence"]
    verify = ev["completeness"]
    out: list[str] = []
    ok = True

    def line(label, passed, detail):
        nonlocal ok
        ok = ok and passed
        out.append(f"{'PASS' if passed else 'FAIL'}  {label}: {detail}")

    out.append(f"file: {cur.file}")
    out.append(f"curation: {cur.path.name} sha256 {cur.sha256[:12]} status {cur.status} curator {cur.curator}")
    out.append(f"scheme: {cur.scheme}")
    out.append(f"class before: {before.cls} ({'; '.join(before.evidence.get('not_clean_because', [])) or 'none'})")
    out.append(f"class after:  {summary['class']}")
    out.append(f"divisions: {m['divisions']} ({m['marker_divisions']} body, {m['apparatus_divisions']} apparatus); "
               f"rule hits {res.rule_hits}; repeats skipped {res.skipped_repeats or 'none'}")
    line("address uniqueness", not m["repeated_loci"],
         "all unique" if not m["repeated_loci"] else f"{len(m['repeated_loci'])} repeated, e.g. {m['repeated_loci'][:5]}")
    line("coverage", m["covered_word_share"] >= cu.CURATED_MIN_COVER,
         f"{m['covered_word_share']:.1%} of {m['body_words']} body words (needs >= {cu.CURATED_MIN_COVER:.0%})")
    line("oversize", not m["oversize_divisions"],
         f"{len(m['oversize_divisions'])} over {cu.CURATED_MAX_DIVISION_WORDS} words"
         + (f" {m['oversize_divisions'][:5]}" if m["oversize_divisions"] else "")
         + (f"; justified {m['justified_oversize']}" if m["justified_oversize"] else ""))
    line("rules and evidence", not m["problems"], "all rules matched, all quotes found, all fixes landed"
         if not m["problems"] else "; ".join(m["problems"][:6]))
    line("word completeness", verify["passage_words"] + verify["furniture_words"] == verify["file_words"]
         and verify["passage_words"] == verify["passage_words_resplit"],
         f"passage words {verify['passage_words']} + furniture {verify['furniture_words']} "
         f"= {verify['passage_words'] + verify['furniture_words']}; file words {verify['file_words']}")
    line("verbatim byte ranges", verify["verbatim_mismatch"] == 0,
         f"{verify['verbatim_exact']} exact, {verify['verbatim_with_declared_furniture']} less declared furniture, "
         f"{verify['verbatim_mismatch']} mismatch of {verify['passages']}")
    for rid, note in cu.sequence_notes(res).items():
        out.append(f"info  numbers read by rule '{rid}': {note['readings']} readings, first {note['first']}, "
                   f"last {note['last']}, repeated {len(note['repeated'])}, backward {len(note['backward'])}, "
                   f"gaps {len(note['gaps'])}, unreadable {len(note['unread'])}")
        for label in ("repeated", "backward", "gaps"):
            if note[label]:
                out.append(f"      {label}: {note[label][:8]}")
        if note["unread"]:
            out.append(f"      unreadable at lines: {note['unread'][:8]}")

    body = [d for d in res.divisions if d.origin != "header" and d.words > 0 and not d.apparatus]
    sampled = [body[i] for i in sample_indices(len(body), n)]
    out.append(f"sample: {len(sampled)} divisions evenly spaced through {len(body)} body divisions")
    for d in sampled:
        out.append(f"  line {d.start + 1} | {d.locus} | {d.title or '-'} | "
                   f"{_words(work, res.line_offsets[d.start], res.line_offsets[d.end], SAMPLE_WORDS)}")
    out.append("RESULT: " + ("PASS" if ok and summary["class"] == "curated" else "FAIL"))
    return Result(ok and summary["class"] == "curated", out, sampled, res, cur, entry, work)


def packet(result: Result, lines: list[str], context: int) -> str:
    cur, res = result.curation, result.resolved
    raw = lines
    md = [f"# Review packet: {cur.file}", "",
          f"Curation `{cur.path.name}`, sha256 `{cur.sha256}`, status `{cur.status}`, curator `{cur.curator}`.", "",
          "## Scheme", "", cur.scheme, "", "## Evidence the scheme is the edition's own", ""]
    for e in cur.evidence:
        md.append(f"- line {e['line']}: `{e['quote']}`")
    md += ["", "## Checker", "", "```", *result.lines, "```", "", "## Sampled divisions", ""]

    def block(first, last):
        return ["```"] + [f"{i + 1:>7}  {raw[i][:160]}" for i in range(max(0, first), min(len(raw), last))] + ["```"]

    for k, d in enumerate(result.sampled, 1):
        md += [f"### {k}. line {d.start + 1}, `{d.locus}`, title `{d.title or '-'}`", "",
               f"{d.words} words; division ends before line {d.end + 1}. Lines before the start, the start, and the end:", ""]
        md += block(d.start - context, d.start + context + 4)
        md += [""] + block(d.end - context, d.end + 1) + [""]
    body = [d for d in res.divisions if d.origin != "header" and d.words > 0 and not d.apparatus]
    md += ["## Smallest and largest body divisions", ""]
    for d in sorted(body, key=lambda x: (x.words, x.start))[:3] + sorted(body, key=lambda x: (-x.words, x.start))[:3]:
        md += [f"- line {d.start + 1}, `{d.locus}`, {d.words} words"]
    md += ["", "## Apparatus ranges", ""]
    for d in (x for x in res.divisions if x.apparatus and x.origin != "header"):
        md += [f"- lines {d.start + 1}-{d.end}, `{d.locus}`, {d.words} words"]
    md += ["", "## Questions for the reader", "",
           "1. Does each sampled locus restate what the printed heading says, with no number the edition does not print?",
           "2. Does each sampled division begin at its heading and end where the next begins, with no text of another division inside it?",
           "3. Is anything in the apparatus ranges actually body text, or any body division actually apparatus?",
           "4. Do the evidence quotes show the scheme is the edition's own?",
           "5. Set status to `sampled-ok` or `needs-redo` in the curation file and say why in the commit.", ""]
    return "\n".join(md)


def _load(stem: str, directory: Path | None):
    path = Path(directory or cu.CURATION_DIR) / f"{stem}.yaml"
    if not path.exists():
        raise cu.CurationError(f"no curation file {path}")
    cur = cu.load(path)
    return cur, entry_for(cur.file, union=bool(cur.speakers))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    for name in ("check", "sample"):
        sp = sub.add_parser(name)
        sp.add_argument("stem")
        sp.add_argument("--curation-dir", type=Path)
        sp.add_argument("--n", type=int, default=DEFAULT_SAMPLE)
    sub.choices["sample"].add_argument("--context", type=int, default=4)
    sub.choices["sample"].add_argument("--out", type=Path)
    args = ap.parse_args(argv)
    try:
        cur, entry = _load(args.stem, args.curation_dir)
        result = run_check(cur, entry, args.n)
    except cu.CurationError as exc:
        print(f"curation error: {exc}")
        return 2
    if args.command == "check":
        print("\n".join(result.lines))
        return 0 if result.ok else 1
    out = args.out or (DEFAULT_OUT / "review" / f"{args.stem}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(packet(result, Source.read(entry.path).text.split("\n"), args.context), encoding="utf-8")
    print(f"wrote {out}")
    print("\n".join(result.lines[-3:]))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
