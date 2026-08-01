"""S6.2/PAHC S2.8-equivalent - render parity: staged views vs deployed
chunks, every difference CLASSIFIED or the run fails loud
(whitespace-normalized).

PAHC classification rules, explicit and narrow:
- `Tags` deployed-only -> intended-change (RETIRED, CO-P2-09).
- `Aliases` differing -> BOTH lines through the VG-1a parse; a
  deployed-only remainder that exactly matches the S2.2 RULE-A DROP
  TABLE (the declared classification authority: elder / church /
  assembly / communion / minister / the water / association) ->
  intended-change; identical parsed sets -> equivalent-restructure;
  anything else -> defect.
- `Related-Terms` differing -> membership via the term/alias
  resolver; generated-superset -> intended-change (record-graph
  enrichment); equal -> equivalent-restructure; deployed-superset ->
  defect.
- anything else -> UNCLASSIFIED (loud failure).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(BACKEND / "wrs" / "migrate"))
from s62_pahc_s22 import parse_aliases_vg1a, DROPS_RULEA  # noqa: E402

STAGING = HERE / "staging" / "pahc_world"
DEPLOYED = BACKEND / "data" / "pahc_world"


def parse_aliases(value):
    return parse_aliases_vg1a(value or "", "parity", [])


def _term_resolver():
    recs = []
    for tp in sorted((BACKEND / "wrs" / "records" / "pahc_world"
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
    extra = {"two ways": "pahclex007", "agape": "pahclex010", "agape-label": "pahclex010",
             "episkopos": "pahclex001", "presbyteros": "pahclex002",
             "ekklesia": "pahclex003", "eucharistia": "pahclex004",
             "diakonos": "pahclex005", "presbyterion": "pahclex006",
             "prophetes": "pahclex008", "baptisma": "pahclex011",
             "hetaeria": "pahclex012", "pertinacia": "pahclex013",
             "ministrae": "pahclex009"}

    def resolve(name):
        c = canon(name)
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
        mm = re.search(r"## Retrieval Front-Matter\s*\n+```\n(.*?)```",
                       txt, re.S)
        head = mm.group(1) if mm else ""
        rest = txt[mm.end():] if mm else txt
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
    for sm in re.finditer(r"^## (?!Retrieval Front-Matter)(.+?)$\n(.*?)(?=^## |\Z)",
                          rest, re.S | re.M):
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
        dset = set(a.lower() for a in parse_aliases(dep or ""))
        gset = set(a.lower() for a in parse_aliases(gen or ""))
        dropped = set(DROPS_RULEA.get(rid, {}))
        if dset - gset == (dset - gset) & dropped and gset <= dset:
            if dset - gset:
                out.append(("intended-change",
                            f"{rid}: Aliases Rule-A-dropped-at-birth per "
                            f"the S2.2 table ({sorted(dset - gset)})"))
            else:
                out.append(("equivalent-restructure",
                            f"{rid}: Aliases surface variant, identical "
                            f"key space"))
            return True
        out.append(("defect", f"{rid}: Aliases unexplained difference "
                              f"(dep-only {sorted(dset - gset - dropped)}, "
                              f"gen-only {sorted(gset - dset)})"))
        return True
    if key == "Related-Terms":
        dset = {i for x in (dep or "").split(",")
                if x.strip() and not x.strip().startswith("(")
                for i in RESOLVE(x)}
        gset = {i for x in (gen or "").split(",")
                if x.strip() and not x.strip().startswith("(")
                for i in RESOLVE(x)}
        missing = sorted(dset - gset)
        extra = sorted(gset - dset)
        if not missing and not extra:
            out.append(("equivalent-restructure",
                        f"{rid}: Related-Terms membership complete; "
                        f"surface variant"))
        elif not missing:
            out.append(("intended-change",
                        f"{rid}: Related-Terms enriched by the record "
                        f"graph (+{len(extra)})"))
        else:
            out.append(("defect",
                        f"{rid}: Related-Terms shortfall ({missing})"))
        return True
    return False


def compare(kind, dep_path, gen_path, out, unclassified):
    rid = dep_path.stem.split("_")[0]
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
    print(f"# S2.8-equivalent render parity (PAHC) - {n} files compared")
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
