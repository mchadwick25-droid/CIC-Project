#!/usr/bin/env python3
"""Check that every row of Wanted_Sources.md traces to a row of an audit or to an Open-Gaps entry.

Run from the repository root:  python3 Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/trace_check.py
Exit 1 if any row fails.
"""
import re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
AUD = ROOT / "Build/Ministry/Operations/Audits"
MD = Path(__file__).with_name("Wanted_Sources.md")
OG = (ROOT / "Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md").read_text()


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def tokens(name):
    name = re.sub(r"\(.*?\)", " ", name)
    return [t for t in norm(name).split() if len(t) >= 4 and t not in {"saint", "bishop", "king", "pope", "patriarch", "metropolitan", "archbishop", "catholicos", "abba", "pair", "paired"}]


section = ""
checked = failed = 0
fails = []
cache = {}
for raw in MD.read_text().split("\n"):
    if raw.startswith("## "):
        section = raw[3:]
    if not raw.startswith("|") or raw.startswith("|---") or raw.startswith("| #"):
        continue
    c = [x.strip() for x in raw.strip().strip("|").split("|")]
    ok = False
    if section.startswith("Person sources") or re.match(r"Era \d+", ""):
        pass
    if section.startswith("Person sources"):
        person, refs = c[1], re.findall(r"`([^`]+?):(\d+)`", c[-1])
        toks = tokens(person) or [x for x in norm(re.sub(r"\(.*?\)", " ", person)).split() if len(x) >= 2]
        ok = bool(refs)
        for f, ln in refs:
            p = AUD / f
            if not p.exists():
                ok = False
                break
            lines = cache.setdefault(f, p.read_text().split("\n"))
            line = norm(lines[int(ln) - 1])
            if not lines[int(ln) - 1].startswith("|") or "wanted" not in line or not any(t in line for t in toks):
                ok = False
                break
    elif section.startswith("Outside-witness"):
        ok = norm(c[1].split(",")[0].split("(")[0]) in norm(OG) or norm(c[1].split(",")[0].split("(")[0]).split()[-1] in norm(OG)
    elif section.startswith("Council records"):
        f, ln = re.findall(r"`([^`]+?):(\d+)`", c[-1])[0]
        lines = cache.setdefault(f, (AUD / f).read_text().split("\n"))
        line = norm(lines[int(ln) - 1])
        ok = norm(c[1])[:14] in line and "wanted" in line
    elif section.startswith("Library-label"):
        key = {"Zclin", "French spellings", "19644", "Heykamp"}
        ok = any(k in OG for k in re.findall(r"[A-Z][\w'.-]{4,}", c[1])[:3]) and f"{c[2]}." in OG.replace("\n", " ") or f"\n{c[2]}. " in OG
    else:
        continue
    checked += 1
    if not ok:
        failed += 1
        fails.append((section[:20], c[1][:60]))
print(f"rows checked: {checked}; failed: {failed}")
for f in fails:
    print("FAIL", f)
sys.exit(1 if failed else 0)
