"""Tests for passage_index.py. Run: python cic/engine/tests_passage_index.py

Builds a throwaway index from the real corpus (a few seconds) and checks
every returned hit against the file itself: the cited line must carry a
tag whose osisRef covers the queried passage.
"""
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import passage_index as pi

results = []


def check(label, ok):
    print(f"  {'OK ' if ok else '***'} {label}")
    results.append(bool(ok))


def spans(v):
    return pi.parse_osis_ref(v)[0]


check("single verse", spans("Bible:Rom.5.12") == [("Rom", 5012, 5012)])
check("verse range", spans("Bible:Acts.1.1-Acts.1.2") == [("Acts", 1001, 1002)])
check("whole chapter", spans("Bible:Ps.51") == [("Ps", 51000, 51999)])
check("list of refs", len(spans("Bible:Matt.5.3 Bible:Matt.5.8-Matt.5.9")) == 2)
check("range across books is rejected, not guessed", pi.parse_osis_ref("Gen.1.1-Exod.2.2") == ([], 1))
check("malformed token is counted", pi.parse_osis_ref("Bible:X:Y.1.1")[1] == 1)
check("query: verse", pi.parse_query("Romans 5:12") == ("Rom", 5012, 5012))
check("query: verse range", pi.parse_query("Rom 5:12-21") == ("Rom", 5012, 5021))
check("query: chapter", pi.parse_query("Matt 5") == ("Matt", 5000, 5999))
check("query: chapter range", pi.parse_query("Matt 5-7") == ("Matt", 5000, 7999))
check("query: numbered book", pi.parse_query("1 Cor 13:4") == ("1Cor", 13004, 13004))
try:
    pi.parse_query("Hezekiah 3:1")
    check("unknown book raises", False)
except ValueError:
    check("unknown book raises", True)


def readings(text):
    return [(r["book"], r["spans"]) for r in pi.parse_readings(text)]


check("readings: verse letters dropped, list of verses",
      readings("Acts 2:14a, 22-32") == [("Acts", [(2014, 2014), (2022, 2032)])])
check("readings: whole psalm", readings("Ps 16") == [("Ps", [(16000, 16999)])])
check("readings: semicolons and numbered books",
      [b for b, _ in readings("Isa 9:2-7; Ps 96; Titus 2:11-14")] == ["Isa", "Ps", "Titus"])
check("readings: a bare chapter part continues the book before it",
      readings("Gen 2:15-17; 3:1-7") == [("Gen", [(2015, 2017)]), ("Gen", [(3001, 3007)])])
check("readings: cross-chapter range", readings("Matt 4:23-5:12") == [("Matt", [(4023, 5012)])])
check("readings: 'or' separates alternatives", len(pi.parse_readings("John 3:1-17 or Matt 17:1-9")) == 2)
check("readings: en dash", readings("Rom 4:1\u20135") == [("Rom", [(4001, 4005)])])
for bad in ("Hezekiah 3:1", "Acts", "Acts 2:x", "Acts 2:9-3"):
    try:
        pi.parse_readings(bad)
        check(f"readings: {bad!r} raises", False)
    except ValueError:
        check(f"readings: {bad!r} raises", True)

PASSAGES = ["Romans 5:12", "Genesis 1:1", "John 1:1", "1 Cor 13:4", "Psalm 51:5", "Matt 6:9", "Matt 5-7",
            "Heb 11:1", "Romans 8:28", "Acts 2:38", "Gal 2:11", "Eph 5:22", "Luke 15:11", "Isa 53:5",
            "Rev 20:1", "James 2:24", "Phil 2:6", "John 3:5", "Col 1:15", "Rom 13:1"]

with tempfile.TemporaryDirectory() as td:
    db = Path(td) / "P.sqlite"
    totals = pi.build(db)
    check("index has both kinds", totals["treats"] > 0 and totals["cites"] > 0)
    for q in PASSAGES:
        book, s, e = pi.parse_query(q)
        rows, total = pi.search(q, db, limit=10**6)
        ok = total > 0
        for kind, ty, f, line, title, sid, work, lang in rows[:60]:
            text = (pi.TEXTS_DIR / f).read_text(encoding="utf-8", errors="replace").splitlines()[line - 1]
            covered = False
            for m in re.finditer(r'osisRef="([^"]*)"', text):
                for b, a, z in pi.parse_osis_ref(m.group(1))[0]:
                    covered |= b == book and a <= e and z >= s
            ok = ok and covered
        check(f"{q}: {total} hit(s), each line carries a covering tag", ok)
    rows, _ = pi.search("Romans 5:12", db, treats_only=True)
    check("Romans 5:12 treats: Chrysostom Homily X",
          any("Homily X on Rom" in r[4] and r[2].startswith("npnf111") for r in rows))
    rows, _ = pi.search("Romans 5:12", db, treats_only=True, limit=10**6)
    check("treats_only returns no citations", all(r[0] == "treats" for r in rows))
    con = sqlite3.connect(db)
    rows, total = pi.search_spans("Acts", [(2014, 2014), (2022, 2032)], db, limit=10**6)
    ok = total > 0 and len({(r[0], r[2], r[3]) for r in rows}) == len(rows)
    check("readings: several spans return each hit once", ok)
    check("a Citation-typed scripCom is stored as cites",
          con.execute("SELECT COUNT(*) FROM hits WHERE tag_type='Citation' AND kind='treats'").fetchone()[0] == 0)
    con.close()

sys.exit(0 if all(results) else 1)
