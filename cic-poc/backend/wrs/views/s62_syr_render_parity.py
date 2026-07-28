"""S6.2/SYR S2.8-equivalent - render parity: staged views vs deployed
chunks, every difference CLASSIFIED or the run fails loud (the ALX
instrument ported; whitespace-normalized).

Syriac classification rules, explicit and narrow:
- `Tags` key deployed-only            -> intended-change (RETIRED,
  CO-P2-09; the S2.2 split logged each drop).
- `Related-Terms` differing           -> membership compared through the
  term/alias resolver: equal membership = equivalent-restructure
  (surface names/order); generated-superset = intended-change (the
  record graph's typed edges exceed the chunk list); deployed-superset
  = defect. BOTH-NONE variants ('(none — see note)' vs '(none —
  flag-only entry, standalone by design)') = equivalent-restructure
  (wording of an empty list).
- `Key Sources` section differing ONLY by the FLAG-025 pointer
  ('#26, cross-checked' -> '#56') -> intended-change (the flag's own
  routed correction, applied to the records at this step).
- anything else                       -> UNCLASSIFIED (loud failure).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]

STAGING = HERE / "staging" / "syriac_world"
DEPLOYED = BACKEND / "data" / "syriac_world"

FLAG025_OLD = "(Source Registry #26, cross-checked)"
FLAG025_NEW = "(Source Registry #56)"


def _term_resolver():
    recs = []
    for tp in sorted((BACKEND / "wrs" / "records" / "syriac_world" / "term").glob("*.md")):
        txt = tp.read_text(encoding="utf-8")
        front, _, _b = txt[4:].partition("\n---\n")
        recs.append(yaml.safe_load(front))
    canon = lambda s: re.sub(r"\s*/\s*", "/", re.sub(r"\([^)]*\)", "", s).strip()).casefold()
    m = {}
    for r in recs:
        m[canon(r["term"])] = r["id"]
    for r in recs:
        for seg in re.sub(r"\([^)]*\)", "", r["term"]).split("/"):
            if seg.strip():
                m.setdefault(canon(seg), r["id"])
    for r in recs:
        for a in r.get("aliases") or []:
            m.setdefault(canon(a), r["id"])
    # deployed shorthand spellings (diacritic-free etc.)
    extra = {"ihidaya": "syrlex007", "tahwyata (tahwiya)": "syrlex003",
             "tahwyata": "syrlex003", "raza (shrara)": "syrlex001",
             "raza": "syrlex001", "shrara": "syrlex001",
             "madrasha": "syrlex004", "memra": "syrlex005",
             "ewangeliyon da-mhallete": "syrlex006", "qyama": "syrlex002",
             "mar": "syrlex008"}

    def resolve(name):
        c = canon(name)
        if c in m:
            return (m[c],)
        if c in extra:
            return (extra[c],)
        return (c,)
    return resolve


RESOLVE = _term_resolver()

NONEISH = re.compile(r"^\(none\b", re.I)


def parse_chunk(path: Path):
    txt = path.read_text(encoding="utf-8")
    fm = {}
    m = re.search(r"```\n(.*?)```", txt, re.S)
    if m:
        key = None
        for line in m.group(1).splitlines():
            km = re.match(r"([A-Za-z-]+):\s*(.*)", line)
            if km:
                key = km.group(1)
                fm[key] = km.group(2).strip()
            elif key and line.strip():
                fm[key] += " " + line.strip()
    secs = {}
    for sm in re.finditer(r"^## (?!Retrieval Front-Matter)(.+?)$\n(.*?)(?=^## |\Z)",
                          txt, re.S | re.M):
        secs[sm.group(1).strip()] = sm.group(2).replace("\n---\n", "\n").strip()
    return fm, secs


def norm(s):
    return " ".join((s or "").split())


def classify(kind, rid, key, dep, gen, out):
    if key == "Tags" and dep and not gen:
        out.append(("intended-change", f"{rid}: Tags line (RETIRED, CO-P2-09)"))
        return True
    if key == "Related-Terms" and norm(dep) != norm(gen):
        if NONEISH.match(norm(dep)) and NONEISH.match(norm(gen)):
            out.append(("equivalent-restructure",
                        f"{rid}: Related-Terms empty-list wording variant"))
            return True
        dset = {i for x in (dep or "").split(",") if x.strip() for i in RESOLVE(x)}
        gset = {i for x in (gen or "").split(",") if x.strip() for i in RESOLVE(x)}
        missing = sorted(dset - gset)
        extra = sorted(gset - dset)
        if not missing and not extra:
            out.append(("equivalent-restructure",
                        f"{rid}: Related-Terms membership complete; "
                        f"surface-name/order variant"))
        elif not missing:
            out.append(("intended-change",
                        f"{rid}: Related-Terms enriched by the record graph "
                        f"(+{len(extra)}: typed S2.3 edges beyond the chunk "
                        f"list)"))
        else:
            out.append(("defect", f"{rid}: Related-Terms shortfall "
                                  f"({', '.join(missing)})"))
        return True
    return False


def classify_section(kind, rid, sec, dep, gen, out):
    if sec == "Key Sources" and dep and gen:
        if norm(dep.replace(FLAG025_OLD, FLAG025_NEW)) == norm(gen):
            out.append(("intended-change",
                        f"{rid}: Key Sources FLAG-025 pointer correction "
                        f"(#26 -> #56, the flag's routed fix)"))
            return True
    return False


def compare(kind, dep_path: Path, gen_path: Path, out, unclassified):
    rid = dep_path.stem.split("_")[0]
    dfm, dsecs = parse_chunk(dep_path)
    gfm, gsecs = parse_chunk(gen_path)
    for key in sorted(set(dfm) | set(gfm)):
        dep, gen = dfm.get(key), gfm.get(key)
        if norm(dep or "") == norm(gen or ""):
            continue
        if not classify(kind, rid, key, dep, gen, out):
            unclassified.append(f"{rid}: front-matter '{key}':\n  deployed: "
                                f"{norm(dep or '(absent)')[:160]}\n  generated: "
                                f"{norm(gen or '(absent)')[:160]}")
    for sec in sorted(set(dsecs) | set(gsecs)):
        dep, gen = dsecs.get(sec), gsecs.get(sec)
        if norm(dep or "") == norm(gen or ""):
            continue
        if not classify_section(kind, rid, sec, dep, gen, out):
            unclassified.append(f"{rid}: section '{sec}':\n  deployed: "
                                f"{norm(dep or '(absent)')[:200]}\n  generated: "
                                f"{norm(gen or '(absent)')[:200]}")


def main() -> int:
    out, unclassified = [], []
    n = 0
    for sub, kind in (("lexicon_chunks", "lexicon"), ("story_chunks", "story")):
        for dep_path in sorted((DEPLOYED / sub).glob("*.md")):
            gen_path = STAGING / sub / dep_path.name
            if not gen_path.exists():
                unclassified.append(f"{dep_path.name}: no staged view")
                continue
            compare(kind, dep_path, gen_path, out, unclassified)
            n += 1
    from collections import Counter
    counts = Counter(c for c, _d in out)
    print(f"# S2.8-equivalent render parity (Syriac) - {n} chunk files compared")
    print(f"classified: {dict(counts)} ({len(out)} total)")
    for c, d in out:
        print(f"  [{c}] {d}")
    if unclassified:
        print(f"\nUNCLASSIFIED ({len(unclassified)}) - FAIL:")
        for u in unclassified:
            print("  " + u)
        return 1
    print("\n0 unclassified - PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
