"""Cut the source lines a Church Family Tree story cites into one file.

Reads the story folder's Source_Sheet.md (and Outline.md, if present). The
sheet names each file once under a short name, as "- **ANF** = `file.xml`",
and cites lines as "ANF 4704-4705" or "ANF 4704–4705, 4710". Every cited
range is cut from its file in cic/texts/ (or the repository root), with a
margin of context on each side, overlapping ranges merged, and written to
Excerpts.md in the folder. A range wider than --max-span lines (a whole
letter or book cited as one span) is not cut: it is listed, to be opened at
need. Reviewers read Excerpts.md and open a file itself only at a line
range, never whole.

Usage: python tools/cut_source_excerpts.py <story folder> [--margin N] [--max-span N]
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXTS = ROOT / "cic" / "texts"
SHORT = re.compile(r"\*\*([A-Za-z][\w.-]*)\*\*\s*=\s*`([^`]+)`")
NUM = r"\d{1,6}"
RANGE = rf"{NUM}(?:\s*[-–]\s*{NUM})?"
DASH = re.compile(r"\s*[-–]\s*")


def find_file(name):
    for base in (TEXTS, ROOT):
        p = base / name
        if p.is_file():
            return p
    hits = list(TEXTS.rglob(Path(name).name))
    return hits[0] if len(hits) == 1 else None


def citations(text, names):
    """Map each short name to the (start, end) ranges the text cites."""
    out = {n: [] for n in names}
    alt = "|".join(sorted((re.escape(n) for n in names), key=len, reverse=True))
    pat = re.compile(rf"(?<![\w-])({alt})(?![\w-])\s+({RANGE}(?:\s*,\s*{RANGE})*)")
    for m in pat.finditer(text):
        for part in m.group(2).split(","):
            bits = DASH.split(part.strip())
            a = int(bits[0])
            b = int(bits[1]) if len(bits) > 1 else a
            if b < a:  # short form such as 4704-05
                b = int(str(a)[: len(str(a)) - len(bits[1])] + bits[1])
            if b >= a:
                out[m.group(1)].append((a, b))
    return out


def merge(ranges, margin, last):
    spans = sorted((max(1, a - margin), min(last, b + margin)) for a, b in ranges)
    merged = []
    for a, b in spans:
        if merged and a <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    return merged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--margin", type=int, default=4)
    ap.add_argument("--max-span", type=int, default=40)
    args = ap.parse_args()
    folder = Path(args.folder)
    sheet = folder / "Source_Sheet.md"
    if not sheet.is_file():
        sys.exit(f"no Source_Sheet.md in {folder}")
    text = sheet.read_text(encoding="utf-8")
    outline = folder / "Outline.md"
    if outline.is_file():
        text += "\n" + outline.read_text(encoding="utf-8")
    names = dict(SHORT.findall(sheet.read_text(encoding="utf-8")))
    if not names:
        sys.exit("the sheet names no files as - **NAME** = `file`")
    cited = citations(text, names)
    lines_out = [f"# Source excerpts: {folder.name}", "",
                 f"Cut by `tools/cut_source_excerpts.py` from the lines `Source_Sheet.md` and `Outline.md` cite, "
                 f"{args.margin} lines of context on each side. Each line keeps its file's own number. "
                 "Open a file itself only at a line range.", ""]
    report, missing, wide = [], [], []
    for name, file in names.items():
        if not cited[name]:
            continue
        path = find_file(file)
        if path is None:
            missing.append(f"{name} = {file}")
            continue
        src = path.read_text(encoding="utf-8", errors="replace").splitlines()
        narrow = [(a, b) for a, b in cited[name] if b - a + 1 <= args.max_span]
        wide += [f"{name} {a}-{b} (`{file}`)" for a, b in sorted(set(cited[name])) if b - a + 1 > args.max_span]
        if not narrow:
            continue
        spans = merge(narrow, args.margin, len(src))
        lines_out += [f"## {name} = `{file}`", ""]
        for a, b in spans:
            lines_out.append(f"### {name} {a}-{b}")
            lines_out.append("```")
            lines_out += [f"{i}: {src[i - 1]}" for i in range(a, b + 1)]
            lines_out += ["```", ""]
        report.append(f"{name}: {len(narrow)} citations, {sum(b - a + 1 for a, b in spans)} lines")
    if wide:
        lines_out += [f"## Wide ranges, not cut (over {args.max_span} lines; open at the lines needed)", ""] + [f"- {w}" for w in wide] + [""]
    if missing:
        lines_out += ["## Files not found", ""] + [f"- {m}" for m in missing] + [""]
    out = folder / "Excerpts.md"
    out.write_text("\n".join(lines_out), encoding="utf-8")
    print(f"wrote {out}")
    for r in report:
        print("  " + r)
    print(f"  wide ranges listed, not cut: {len(wide)}")
    for m in missing:
        print("  NOT FOUND: " + m)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
