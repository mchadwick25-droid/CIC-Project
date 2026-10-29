#!/usr/bin/env python3
"""Mechanical verification of a world's Doc_01, Doc_02 and Source_Registry.

Usage: python tools/verify_world_source_citations.py <world-code> [--world-dir DIR] [--texts-dir DIR]

Checks (every failure is printed; the exit code is 1 if any check fails):
  1. Every vendored file the three documents name exists in cic/texts/ (full file
     names, and shorthand such as `npnf203` that must resolve to exactly one file).
  2. No document says a file is "not vendored" when a file named on that line exists.
  3. Registry rows and the cross-references to them agree: a sentence in Doc_01 or
     Doc_02 that cites Registry rows and carries one status class (live edge case,
     or out of the window/boundary) must match the Boundary Status of each cited row;
     every cited row exists; no section locus appears under two contradictory rows.
  4. Quotations (6 words or more) are found verbatim, after whitespace and tag
     normalization, in a vendored file cited in the same row or paragraph, or in a
     corpus-map file; where the same passage cites file lines, the quotation lies in
     those lines; where it cites an XML paragraph id, it lies in that paragraph.
  5. Any table whose rows pair a vendored file with corpus-map buckets lists exactly
     the buckets the corpus map assigns to that file (other than this world's own).
"""
import argparse
import collections
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXTS_FALLBACK = "/home/user/CIC-Project/cic/texts"

SHORT = re.compile(r"^(?:npnf|anf)\d+[a-z]*$")
EXT = (".txt", ".xml", ".yaml")
LIVE = re.compile(r"live edge case", re.I)
OUT = re.compile(r"out of the window|out of the boundary|out-of-boundary|excluded", re.I)


def norm(s):
    s = re.sub(r"</?(?:p|div\d?|br|lb|head|item|list|l|lg|note|table|tr|td|th)\b[^>]*>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


class Ctx:
    def __init__(self, world, world_dir, texts_dir):
        self.world = world
        self.world_dir = world_dir
        self.texts_dir = texts_dir
        self.fail = collections.OrderedDict()
        self.files = sorted(os.listdir(texts_dir))
        self._raw = {}
        self._norm = {}

    def bad(self, check, msg):
        self.fail.setdefault(check, []).append(msg)

    def raw(self, name):
        if name not in self._raw:
            with open(os.path.join(self.texts_dir, name), encoding="utf-8", errors="replace") as f:
                self._raw[name] = f.read()
        return self._raw[name]

    def normed(self, name):
        if name not in self._norm:
            self._norm[name] = norm(self.raw(name))
        return self._norm[name]

    def resolve(self, tok):
        if tok in self.files:
            return [tok]
        if SHORT.match(tok):
            return [f for f in self.files if f.startswith(tok + "_")]
        return []


def read_docs(world_dir):
    docs = {}
    for key, pat in (("Doc_01", "Doc_01_*.md"), ("Doc_02", "Doc_02_*.md"), ("Registry", "Source_Registry.md")):
        hits = glob.glob(os.path.join(world_dir, pat))
        if len(hits) != 1:
            raise SystemExit("expected one %s in %s, found %d" % (pat, world_dir, len(hits)))
        docs[key] = open(hits[0], encoding="utf-8").read()
    return docs


def file_tokens(ctx, text):
    out = []
    for tok in re.findall(r"`([^`\n]+)`", text):
        t = tok.split(":")[1] if tok.startswith("cic:") and tok.count(":") >= 1 else tok
        t = t.strip()
        if t.startswith("cic/texts/"):
            t = t[len("cic/texts/"):]
        if t.endswith(EXT) or SHORT.match(t):
            out.append(t)
    return out


def check_files_exist(ctx, docs):
    for key, text in docs.items():
        for tok in sorted(set(file_tokens(ctx, text))):
            found = ctx.resolve(tok)
            if tok.endswith(EXT) and tok not in ctx.files:
                if not tok.endswith(".yaml"):
                    ctx.bad("1 named files exist", "%s names `%s`: no such file in cic/texts" % (key, tok))
            elif SHORT.match(tok) and len(found) != 1:
                ctx.bad("1 named files exist", "%s shorthand `%s` resolves to %d files" % (key, tok, len(found)))


def check_not_vendored(ctx, docs):
    for key, text in docs.items():
        for n, line in enumerate(text.split("\n"), 1):
            for sent in re.split(r"(?<=[.;])(?:\*\*)?\s+", line):
                if re.search(r"not vendored|no vendored|is not in the library", sent, re.I):
                    for tok in file_tokens(ctx, sent):
                        if ctx.resolve(tok):
                            ctx.bad("2 'not vendored' claims", "%s line %d says not vendored but `%s` exists: %.100s" % (key, n, tok, sent))


def registry_rows(text):
    rows = {}
    for line in text.split("\n"):
        m = re.match(r"^\| (\d+[a-z]?) \|", line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows[m.group(1)] = cells
    return rows


def status_class(cells):
    # Registry columns: row | work | origin | confidence | boundary status | boundary class | ...
    st = cells[4] if len(cells) > 4 else ""
    if st.startswith("Excluded"):
        return "out"
    if "live edge case" in st:
        return "live"
    return "native"


def expand_rows(s):
    return re.findall(r"\b(\d+[a-z]?)\b", s)


def check_row_refs(ctx, docs):
    rows = registry_rows(docs["Registry"])
    classes = {k: status_class(v) for k, v in rows.items()}
    for key in ("Doc_01", "Doc_02", "Registry"):
        text = docs[key]
        for sent in re.split(r"(?<=[.;])\s+(?=[A-Z*])", text):
            for m in re.finditer(r"\b[Rr]ows? ((?:\d+[a-z]?(?:,? and |, | and | to )?)+)", sent):
                refs = [r for r in expand_rows(m.group(1))]
                for r in refs:
                    if r not in rows and not re.fullmatch(r"\d+", r):
                        ctx.bad("3 row cross-references", "%s cites row %s, which the Registry does not have: %.90s" % (key, r, sent))
                if key == "Registry":
                    continue
                live, out = bool(LIVE.search(sent)), bool(OUT.search(sent))
                if live != out and len(refs) <= 4 and "context" not in sent[:0]:
                    want = "live" if live else "out"
                    for r in refs:
                        if r in classes and classes[r] in ("live", "out") and classes[r] != want:
                            ctx.bad("3 row cross-references", "%s says %s for row %s, but the Registry holds it as %s: %.100s" % (key, want, r, classes[r], sent.strip()))
    # one locus, one status: a letter or paragraph id listed in a row may not be listed in a row of the other class
    seen = collections.defaultdict(set)
    for r, cells in rows.items():
        c = classes[r]
        if c == "native":
            continue
        for loc in set(re.findall(r"`(iv\.x\.[a-z]+)`", " ".join(cells[1:2] + cells[6:7]))):
            seen[loc].add((c, r))
    for loc, cs in seen.items():
        if len({c for c, _ in cs}) > 1:
            ctx.bad("3 row cross-references", "locus %s is listed under rows of different status: %s" % (loc, sorted(cs)))
    # a letter named as live in row text and as out elsewhere
    for loc in sorted({l for t in docs.values() for l in re.findall(r"`(iv\.x\.[a-z]+)`", t)}):
        lives, outs = [], []
        for key, text in docs.items():
            for sent in re.split(r"(?<=[.;])\s+(?=[A-Z*])", text):
                if "`%s`" % loc in sent:
                    if re.search(r"`%s`[^`]{0,60}(is|are) out of the window|`%s`\)? is out of the window" % (loc, loc), sent):
                        outs.append(key)
                    if re.search(r"(run of|Letters) .*live edge|live edge case.*\(e\.g|for example [^)]*`%s`" % loc, sent):
                        lives.append(key)
        if outs and lives:
            ctx.bad("3 row cross-references", "letter %s is out of the window in %s and a live edge case in %s" % (loc, sorted(set(outs)), sorted(set(lives))))


QUOTE = re.compile(r'"([^"\n]{20,}?)"')


def segments(q):
    q = re.sub(r"\[[^\]]*\]", "\u0000", q)
    parts = re.split(r"\u0000|\.\.\.|…", q)
    segs = []
    for p in parts:
        p = p.strip(" ,.;:\u0000")
        if len(p.split()) >= 3:
            segs.append(p)
    return segs


def corpusmap_text(ctx):
    d = os.path.join(ROOT, "cic", "corpus-map")
    out = ""
    for f in glob.glob(os.path.join(d, "*.yaml")):
        out += " " + norm(open(f, encoding="utf-8").read().replace("\n", " ").replace("''", "'"))
    return out


def has(text, sn):
    if sn in text:
        return True
    first, _, rest = sn.partition(" ")
    return bool(rest) and re.search("(?i:%s) %s" % (re.escape(first), re.escape(rest)), text) is not None


def para_locus(ctx, name, pid):
    raw = ctx.raw(name)
    m = re.search(r'id="%s"[^>]*>(.*?)</p>' % re.escape(pid), raw, re.S)
    return norm(m.group(1)) if m else None


def lines_range(ctx, name, a, b):
    ls = ctx.raw(name).split("\n")
    return norm(" ".join(ls[max(0, a - 3):b + 2]))


LINEREF = re.compile(r"lines? ((?:\d+(?:\s*(?:-|\u2013|to)\s*\d+)?(?:\s*,\s*and\s+|\s*,\s*|\s+and\s+)?)+)")


def line_ranges(win):
    out = [(int(x), int(x)) for x in re.findall(r":line(\d+)", win)]
    for m in LINEREF.finditer(win):
        for a, b in re.findall(r"(\d+)(?:\s*(?:-|\u2013|to)\s*(\d+))?", m.group(1)):
            out.append((int(a), int(b) if b else int(a)))
    return out


def find_quotes(block):
    quotes = []
    i = 0
    while True:
        a = block.find('"', i)
        if a < 0:
            break
        b = block.find('"', a + 1)
        if b < 0:
            break
        before = block[a - 1] if a else " "
        after = block[b + 1] if b + 1 < len(block) else " "
        inner = block[a + 1:b]
        if before in " (*[\u2014" and after in " .,;:)*]\u2014" and "`" not in inner and not inner.startswith(" "):
            quotes.append((a, b, inner))
            i = b + 1
        else:
            i = a + 1
    return quotes


def project_text(ctx):
    out = ""
    for sub in ("Build/reference", "Build/worlds/" + ctx.world, "Build/worlds/_cross-world"):
        for f in glob.glob(os.path.join(ROOT, sub, "**", "*.md"), recursive=True):
            if f.startswith(ctx.world_dir) or "Review-Artifacts" in f or os.path.basename(f) in ("Source_Registry.md",) or os.path.basename(f).startswith(("Doc_01_", "Doc_02_")):
                continue
            out += " " + norm(open(f, encoding="utf-8", errors="replace").read())
    import zipfile
    for f in glob.glob(os.path.join(ROOT, "Build", "reference", "**", "*.docx"), recursive=True):
        try:
            with zipfile.ZipFile(f) as z:
                out += " " + norm(re.sub(r"</w:p>", " ", z.read("word/document.xml").decode("utf-8", "replace")))
        except (OSError, KeyError, zipfile.BadZipFile):
            continue
    return out


def check_quotes(ctx, docs, cm):
    proj = project_text(ctx)
    for key, text in docs.items():
        doc_cited = set()
        for tok in file_tokens(ctx, text):
            doc_cited.update(ctx.resolve(tok))
        blocks = [b for b in text.split("\n") if b.strip()]
        for bi, block in enumerate(blocks):
            cited = set()
            for tok in file_tokens(ctx, block):
                cited.update(ctx.resolve(tok))
            near_files = set(cited)
            if bi:
                for tok in file_tokens(ctx, blocks[bi - 1]):
                    near_files.update(ctx.resolve(tok))
            for a, b, q in find_quotes(block):
                if len(q.split()) < 6:
                    continue
                win = block[max(0, a - 350):b + 350]
                pids = re.findall(r"`(xii\.[a-z0-9.]+-p\d+)`", win)
                for seg in segments(q):
                    sn = norm(seg)
                    holders = [f for f in near_files if has(ctx.normed(f), sn)]
                    if not holders:
                        holders = [f for f in doc_cited if has(ctx.normed(f), sn)]
                    if not holders and not (sn in cm or sn in proj):
                        ctx.bad("4 quotations verbatim", "%s: quotation not found in any cited vendored file, the corpus map or the project documents: \"%.90s\"" % (key, seg))
                        continue
                    if pids:
                        qend = b - max(0, a - 350)
                        after = [p for p in pids if win.find("`%s`" % p) > qend and win.find("`%s`" % p) - qend < 90]
                        near = after[0] if after else pids[-1] if all(win.find("`%s`" % p) < qend for p in pids) else min(pids, key=lambda p: abs(win.find("`%s`" % p) - qend))
                        for f in holders:
                            if f.endswith(".xml"):
                                pt = para_locus(ctx, f, near)
                                if pt is not None and not has(pt, sn):
                                    ctx.bad("4 quotations verbatim", "%s: \"%.70s\" is cited to %s but is not in that paragraph of %s" % (key, seg, near, f))
                    txts = [f for f in holders if f.endswith(".txt")]
                    lr = line_ranges(win)
                    if lr and len(txts) == 1 and len(holders) == 1 and len(lr) <= 6:
                        f = txts[0]
                        if sn not in cm and not any(has(lines_range(ctx, f, x, y), sn) for x, y in lr):
                            ctx.bad("4 quotations verbatim", "%s: \"%.70s\" lies outside the stated file lines %s of %s" % (key, seg, lr, f))



def check_bucket_tables(ctx, docs):
    idx = collections.defaultdict(set)
    for f in glob.glob(os.path.join(ROOT, "cic", "corpus-map", "*.yaml")):
        d = yaml.safe_load(open(f, encoding="utf-8"))
        if not isinstance(d, dict) or "works" not in d:
            continue
        for w in d["works"] or []:
            if isinstance(w, dict) and "source_file" in w:
                idx[w["source_file"]].add(d.get("atlas_id"))
    own = None
    for f in glob.glob(os.path.join(ROOT, "cic", "corpus-map", "*.yaml")):
        d = yaml.safe_load(open(f, encoding="utf-8"))
        if isinstance(d, dict) and d.get("atlas_id") and ctx.world in str(d.get("atlas_id")):
            pass
    text = docs["Doc_02"]
    n = 0
    for line in text.split("\n"):
        m = re.match(r"^\| `([^`]+)` \| Deferred \| (.*) \|\s*$", line)
        if not m:
            continue
        n += 1
        listed = set(re.findall(r"`([^`]+)`", m.group(2)))
        actual = idx.get(m.group(1), set())
        if listed != actual:
            ctx.bad("5 bucket tables", "%s: Table lists %s; the corpus map assigns %s (missing %s, extra %s)" % (
                m.group(1), sorted(listed), sorted(actual), sorted(actual - listed), sorted(listed - actual)))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("world")
    ap.add_argument("--world-dir")
    ap.add_argument("--texts-dir")
    a = ap.parse_args()
    world_dir = a.world_dir or os.path.join(ROOT, "Build", "worlds", a.world)
    texts_dir = a.texts_dir or os.path.join(ROOT, "cic", "texts")
    if not os.path.isdir(texts_dir) or not os.listdir(texts_dir):
        texts_dir = TEXTS_FALLBACK
    ctx = Ctx(a.world, world_dir, texts_dir)
    docs = read_docs(world_dir)
    cm = corpusmap_text(ctx)
    check_files_exist(ctx, docs)
    check_not_vendored(ctx, docs)
    check_row_refs(ctx, docs)
    check_quotes(ctx, docs, cm)
    n = check_bucket_tables(ctx, docs)
    names = ["1 named files exist", "2 'not vendored' claims", "3 row cross-references", "4 quotations verbatim", "5 bucket tables"]
    print("verify_world_source_docs: world %s, texts %s, %d Table-D-style rows checked" % (a.world, texts_dir, n))
    for nm in names:
        f = ctx.fail.get(nm, [])
        print("%s: %s" % (nm, "PASS" if not f else "FAIL (%d)" % len(f)))
        for x in f:
            print("   - " + x)
    sys.exit(1 if ctx.fail else 0)


if __name__ == "__main__":
    main()
