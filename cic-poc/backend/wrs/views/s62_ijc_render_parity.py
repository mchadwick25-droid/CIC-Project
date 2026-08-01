"""S6.2/IJC S2.8-equivalent - render parity: staged views vs deployed
chunks, every difference CLASSIFIED or the run fails loud
(whitespace-normalized).

IJC classification rules, explicit and narrow:
- `Tags` deployed-only -> intended-change (RETIRED, CO-P2-09).
- `Aliases` differing -> the S2.2 AUTHORING TABLES are the
  classification authority (ALIAS_AUTHORED + DROPS_RULEA from
  s62_ijc_s22): a difference on a table-authored chunk whose staged
  line equals the authored list -> intended-change (the FLAG-035
  fixes and the Rule-A drop landing at swap); identical parsed sets
  -> equivalent-restructure; anything else -> defect.
- anything else -> UNCLASSIFIED (loud failure).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(BACKEND / "wrs" / "migrate"))
from s62_ijc_s22 import ALIAS_AUTHORED, DROPS_RULEA  # noqa: E402
from s62_pahc_s22 import parse_aliases_vg1a  # noqa: E402

STAGING = HERE / "staging" / "imperial_juridical_world"
DEPLOYED = BACKEND / "data" / "imperial_juridical_world"


def parse_chunk(path: Path):
    txt = path.read_text(encoding="utf-8")
    fm = {}
    fence = re.search(r"```\n(.*?)```", txt, re.S)
    key = None
    for line in (fence.group(1) if fence else "").splitlines():
        km = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            fm[key] = km.group(2).strip()
        elif key and line.strip():
            fm[key] += " " + line.strip()
    rest = txt[fence.end():] if fence else txt
    secs = {}
    for sm in re.finditer(r"^## (.+?)$\n(.*?)(?=^## |\Z)",
                          rest, re.S | re.M):
        body = re.sub(r"^-{3,}\s*$", "", sm.group(2), flags=re.M).strip()
        secs[sm.group(1).strip()] = body
    return fm, secs


def norm(s):
    return " ".join((s or "").split())


def classify(rid, key, dep, gen, out):
    if key == "Tags" and dep and not gen:
        out.append(("intended-change",
                    f"{rid}: Tags line (RETIRED, CO-P2-09)"))
        return True
    if key == "Aliases":
        gen_list = parse_aliases_vg1a(gen or "", rid, [])
        if rid in ALIAS_AUTHORED:
            authored = ALIAS_AUTHORED[rid][0]
            if gen_list == authored:
                why = ALIAS_AUTHORED[rid][1]
                out.append(("intended-change",
                            f"{rid}: Aliases AUTHORED per the S2.2 table "
                            f"({why[:90]})"))
                return True
        dep_list = parse_aliases_vg1a(dep or "", rid, [])
        if dep_list == gen_list:
            out.append(("equivalent-restructure",
                        f"{rid}: Aliases surface variant"))
            return True
        out.append(("defect", f"{rid}: Aliases unexplained difference "
                              f"(dep {dep_list} vs gen {gen_list})"))
        return True
    return False


def main() -> int:
    out, unclassified = [], []
    n = 0
    for sub in ("lexicon_chunks", "story_chunks"):
        for dep_path in sorted((DEPLOYED / sub).glob("*.md")):
            gen_path = STAGING / sub / dep_path.name
            if not gen_path.exists():
                unclassified.append(f"{dep_path.name}: no staged view")
                continue
            rid = dep_path.stem.split("_")[0]
            dfm, dsecs = parse_chunk(dep_path)
            gfm, gsecs = parse_chunk(gen_path)
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
            n += 1
    from collections import Counter
    counts = Counter(c for c, _d in out)
    print(f"# S2.8-equivalent render parity (IJC) - {n} files compared")
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
