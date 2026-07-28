"""S6.2 S2.8-equivalent render-parity (P): classified comparison of staged
Alexandria chunk views vs. deployed files.

Blueprint standard (Desert render_parity.py carried): byte-parity is NOT
expected; every difference must be classified `equivalent-restructure` /
`intended-change` (citing its warrant) / `defect` (citing its flag/CO
route). ZERO unclassified - any unmatched difference fails the run loudly.

Comparison model: both files are parsed into (front-matter dict, ordered
{section-heading: text}) and compared per key / per section,
whitespace-normalized. Classification rules, explicit and narrow:

- `Tags` key deployed-only                  -> intended-change (RETIRED per
  CO-P2-09 - dead metadata, parsed into the index and read by nothing;
  the S2.2 split logged the drop).
- `Related-Terms` differing                 -> defect (view renders
  record-backed relations only; the deployed extras are the 37 untyped
  mutual pairs + not-yet-built partners = the DECLARED render-shortfall
  class, routed to the S2.9-equivalent CO at the S2.3 close-out).
- `Do-Not-Retrieve-When` deployed carries a retired cross-world clause or
  the em-dash sentinel beyond the generated list -> intended-change
  (Pass 1 SS3.2 retires the class; the S2.2 split logged each drop).
- story `Confidence` key deployed-only      -> defect (schema gap - no
  record home; S2.9 CO candidate "story confidence line").
- anything else differing after whitespace normalization -> UNCLASSIFIED
  (loud failure).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]

STAGING = HERE / "staging" / "alexandria_world"
DEPLOYED = BACKEND / "data" / "alexandria_world"

RETIRED_DNRW = re.compile(r"cross-world|another world['’]s voice", re.I)


def _term_resolver():
    """name -> record id, same resolution order as s62_alx_s29_co13
    (full term names win; slash-segments; aliases last)."""
    import yaml
    recs = []
    for tp in sorted((BACKEND / "wrs" / "records" / "alexandria_world" / "term").glob("*.md")):
        txt = tp.read_text(encoding="utf-8")
        front, _, _b = txt[4:].partition("\n---\n")
        recs.append(yaml.safe_load(front))
    canon = lambda s: re.sub(r"\s*/\s*", "/", s.strip()).casefold()
    m = {}
    for r in recs:
        m[canon(r["term"])] = r["id"]
    for r in recs:
        for seg in r["term"].split("/"):
            m.setdefault(canon(seg), r["id"])
    for r in recs:
        for a in r.get("aliases") or []:
            m.setdefault(canon(a), r["id"])
    short = {"image": "alexlex009", "likeness": "alexlex012"}

    def resolve(name):
        """-> tuple of ids (compound shorthand like 'Image/Likeness'
        expands to both; unresolvable names stay literal)."""
        c = canon(name)
        if c in m:
            return (m[c],)
        seg = [m.get(canon(s)) or short.get(canon(s)) for s in name.split("/")]
        if len(seg) > 1 and all(seg):
            return tuple(sorted(set(seg)))
        return (c,)
    return resolve


RESOLVE = _term_resolver()


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
    """Return True if classified; append (class, detail) to out."""
    if key == "Tags" and dep and not gen:
        out.append(("intended-change", f"{rid}: Tags line (RETIRED, CO-P2-09)"))
        return True
    if key == "Related-Terms" and norm(dep) != norm(gen):
        # CO-P2-13 (Mark, 2026-07-28): mutual pairs now carry typed
        # associated-with edges, so membership is the standard - the
        # record's edge-order vs the chunk's list-order is presentational.
        dset = {i for x in (dep or "").split(",") if x.strip() for i in RESOLVE(x)}
        gset = {i for x in (gen or "").split(",") if x.strip() for i in RESOLVE(x)}
        missing = sorted(dset - gset)
        extra = sorted(gset - dset)
        if not missing and not extra:
            out.append(("equivalent-restructure",
                        f"{rid}: Related-Terms membership complete "
                        f"(CO-P2-13); edge-order vs chunk list-order"))
        elif not missing:
            # the record graph exceeds the chunk's own list: S2.3's typed
            # edges (EF-derived, cross-batch mirrors) + CO-P2-13 pairs
            out.append(("intended-change",
                        f"{rid}: Related-Terms enriched by the record graph "
                        f"(+{len(extra)}: S2.3 typed edges beyond the chunk "
                        f"list; CO-P2-13 render)"))
        else:
            out.append(("defect", f"{rid}: Related-Terms shortfall "
                                  f"({', '.join(missing)}) - "
                                  f"one-directional/not-yet-built class -> "
                                  f"S2.9 completion-items decision"))
        return True
    if key == "Do-Not-Retrieve-When" and norm(dep) != norm(gen):
        dep_clauses = [norm(c) for c in (dep or "").split(";") if c.strip()]
        gen_clauses = [norm(c) for c in (gen or "").split(";") if c.strip()]
        extra = [c for c in dep_clauses if c not in gen_clauses]
        missing_in_dep = [c for c in gen_clauses if c not in dep_clauses]
        if not missing_in_dep and all(
                RETIRED_DNRW.search(c) or c in ("—", "-") for c in extra):
            out.append(("intended-change",
                        f"{rid}: DNRW retired-class/sentinel drop (Pass 1 SS3.2)"))
            return True
        return False
    if kind == "story" and key == "Confidence" and dep and not gen:
        out.append(("defect", f"{rid}: story Confidence line - no record home "
                              f"(schema gap; S2.9 CO candidate)"))
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
    print(f"# S2.8-equivalent render parity - {n} chunk files compared")
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
