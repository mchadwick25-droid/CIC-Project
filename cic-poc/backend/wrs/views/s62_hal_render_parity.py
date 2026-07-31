"""S6.2/HAL S2.8-equivalent - render parity: staged views vs deployed
chunks, every difference CLASSIFIED or the run fails loud (the SYR
instrument ported; whitespace-normalized).

HAL classification rules, explicit and narrow:
- `Tags` key deployed-only            -> intended-change (RETIRED,
  CO-P2-09; the S2.2 split logged each drop).
- `Aliases` differing                 -> BOTH lines run through the
  runtime VG-1a parse (app.rag.indexer.parse_aliases): identical
  parsed key sets = equivalent-restructure (the surface differs only
  by VG-1a-dropped qualified segments / quote marks - the records
  were born from this very parse at S2.2); any parsed difference =
  defect.
- `Related-Terms` differing           -> membership compared through
  the term/alias resolver: equal membership =
  equivalent-restructure; deployed-only names resolving to the three
  NEVER-BUILT terms (Xenodochium, Praeceptor, Monasterium duplex) =
  intended-change (the S2.3 declared not-yet-built-partner class);
  generated-superset = intended-change (record-graph enrichment);
  any other deployed-superset = defect.
- `Force-LLM-Vote` key                -> none exist in this corpus
  (S2.2 grep-verified); any appearance = UNCLASSIFIED (loud).
- anything else                       -> UNCLASSIFIED (loud failure).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

# the runtime VG-1a parse semantics: app.rag.indexer's parse_aliases is
# a closure inside the indexer method (not importable); the S2.2
# splitter's port of the same semantics is the shared instrument
sys.path.insert(0, str(BACKEND / "wrs" / "migrate"))
from s62_hal_chunk_split import parse_aliases_vg1a


def parse_aliases(value):
    return parse_aliases_vg1a(value or "", "parity", [])

STAGING = HERE / "staging" / "hieronymian_world"
DEPLOYED = BACKEND / "data" / "hieronymian_world"

NEVER_BUILT = {"xenodochium", "praeceptor", "monasterium duplex"}


def _term_resolver():
    recs = []
    for tp in sorted((BACKEND / "wrs" / "records" / "hieronymian_world"
                      / "term").glob("*.md")):
        txt = tp.read_text(encoding="utf-8")
        front, _, _b = txt[4:].partition("\n---\n")
        recs.append(yaml.safe_load(front))
    canon = lambda s: re.sub(r"\s*/\s*", "/",
                             re.sub(r"\([^)]*\)", "", s).strip()).casefold()
    m = {}
    for r in recs:
        m[canon(r["term"])] = r["id"]
    for r in recs:
        for a in r.get("aliases") or []:
            m.setdefault(canon(a), r["id"])
    # deployed shorthand spellings in Related-Terms lines
    extra = {"exegesis-as-practiced-authority": "hallex11",
             "vulgata": "hallex02", "origenism": "hallex08",
             "pelagianism": "hallex09", "vidua": "hallex05",
             "epistula": "hallex07", "praefatio": "hallex13",
             "nosocomium": "hallex14", "grammaticus": "hallex12"}

    def resolve(name):
        c = canon(name)
        if c in NEVER_BUILT:
            return ("NEVER-BUILT:" + c,)
        if c in m:
            return (m[c],)
        if c in extra:
            return (extra[c],)
        return (c,)
    return resolve


RESOLVE = _term_resolver()


def parse_chunk(path: Path, kind: str):
    txt = path.read_text(encoding="utf-8")
    fm = {}
    if kind == "lexicon":
        m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
        head = m.group(1) if m else ""
        rest = txt[m.end():] if m else txt
    else:
        head, sep, rest = txt.partition("\n---\n")
        assert sep, path
    key = None
    for line in head.splitlines():
        km = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            fm[key] = km.group(2).strip()
        elif key and line.strip():
            fm[key] += " " + line.strip()
    secs = {}
    for sm in re.finditer(r"^## (.+?)$\n(.*?)(?=^## |\Z)", rest, re.S | re.M):
        body = re.sub(r"^-{3,}\s*$", "", sm.group(2), flags=re.M).strip()
        secs[sm.group(1).strip()] = body
    return fm, secs


def norm(s):
    return " ".join((s or "").split())


def classify(rid, key, dep, gen, out):
    if key == "Tags" and dep and not gen:
        out.append(("intended-change", f"{rid}: Tags line (RETIRED, CO-P2-09)"))
        return True
    if key == "Aliases":
        dset = set(parse_aliases(dep or ""))
        gset = set(parse_aliases(gen or ""))
        if (rid == "hallex02" and dset == set() and gset == {"The Vulgate"}
                and "The Vulgate (" in (dep or "")):
            out.append(("intended-change",
                        f"{rid}: Aliases re-authored unqualified 'The "
                        f"Vulgate' (the FLAG-028 correction, applied at "
                        f"S2.8 after retrieval parity measured the "
                        f"regression; the deployed line's qualified form "
                        f"parses to nothing)"))
            return True
        if dset == gset:
            out.append(("equivalent-restructure",
                        f"{rid}: Aliases surface differs only through the "
                        f"runtime VG-1a parse (identical key space)"))
        else:
            out.append(("defect", f"{rid}: Aliases parsed difference "
                                  f"(dep-only {sorted(dset - gset)}, "
                                  f"gen-only {sorted(gset - dset)})"))
        return True
    if key == "Related-Terms":
        dep_n, gen_n = norm(dep), norm(gen)
        if dep_n.startswith("(none") and gen_n.startswith("(none"):
            out.append(("equivalent-restructure",
                        f"{rid}: Related-Terms empty-list wording variant"))
            return True
        dset = {i for x in (dep or "").split(",")
                if x.strip() and not x.strip().startswith("(")
                for i in RESOLVE(x)}
        gset = {i for x in (gen or "").split(",")
                if x.strip() and not x.strip().startswith("(")
                for i in RESOLVE(x)}
        never = {i for i in dset - gset if i.startswith("NEVER-BUILT:")}
        missing = sorted(dset - gset - never)
        extra = sorted(gset - dset)
        msgs = []
        if never:
            msgs.append(("intended-change",
                         f"{rid}: Related-Terms deployed-only never-built "
                         f"partner(s) {sorted(n[12:] for n in never)} (the "
                         f"S2.3 declared class)"))
        if not missing and not extra and not never:
            msgs.append(("equivalent-restructure",
                         f"{rid}: Related-Terms membership complete; "
                         f"surface-name/order variant"))
        elif not missing and extra:
            msgs.append(("intended-change",
                         f"{rid}: Related-Terms enriched by the record "
                         f"graph (+{len(extra)}: typed S2.3 edges beyond "
                         f"the chunk list)"))
        elif not missing and never and not extra:
            msgs.append(("equivalent-restructure",
                         f"{rid}: Related-Terms remaining membership "
                         f"complete"))
        if missing:
            msgs.append(("defect", f"{rid}: Related-Terms shortfall "
                                   f"({', '.join(missing)})"))
        out.extend(msgs)
        return True
    return False


def compare(kind, dep_path: Path, gen_path: Path, out, unclassified):
    rid = "hal" + dep_path.stem.split("_")[1]
    dfm, dsecs = parse_chunk(dep_path, kind)
    gfm, gsecs = parse_chunk(gen_path, kind)
    for key in sorted(set(dfm) | set(gfm)):
        dep, gen = dfm.get(key), gfm.get(key)
        if norm(dep or "") == norm(gen or ""):
            continue
        if not classify(rid, key, dep, gen, out):
            unclassified.append(
                f"{rid}: front-matter '{key}':\n  deployed: "
                f"{norm(dep or '(absent)')[:160]}\n  generated: "
                f"{norm(gen or '(absent)')[:160]}")
    for sec in sorted(set(dsecs) | set(gsecs)):
        dep, gen = dsecs.get(sec), gsecs.get(sec)
        if norm(dep or "") == norm(gen or ""):
            continue
        unclassified.append(
            f"{rid}: section '{sec}':\n  deployed: "
            f"{norm(dep or '(absent)')[:200]}\n  generated: "
            f"{norm(gen or '(absent)')[:200]}")


def main() -> int:
    out, unclassified = [], []
    n = 0
    for sub, kind in (("lexicon_chunks", "lexicon"),
                      ("story_chunks", "story")):
        for dep_path in sorted((DEPLOYED / sub).glob("*.md")):
            gen_path = STAGING / sub / dep_path.name
            if not gen_path.exists():
                unclassified.append(f"{dep_path.name}: no staged view")
                continue
            compare(kind, dep_path, gen_path, out, unclassified)
            n += 1
    from collections import Counter
    counts = Counter(c for c, _d in out)
    print(f"# S2.8-equivalent render parity (HAL) - {n} chunk files compared")
    print(f"classified: {dict(counts)} ({len(out)} total)")
    for c, d in out:
        print(f"  [{c}] {d}")
    defects = [d for c, d in out if c == "defect"]
    if unclassified or defects:
        print(f"\nUNCLASSIFIED ({len(unclassified)}) + defects "
              f"({len(defects)}) - FAIL:")
        for u in unclassified:
            print("  " + u)
        return 1
    print("\n0 unclassified, 0 defects - PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
