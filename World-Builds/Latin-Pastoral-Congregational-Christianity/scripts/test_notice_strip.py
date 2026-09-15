#!/usr/bin/env python3
"""Tests for notice_strip. Run: python3 scripts/test_notice_strip.py

Written because Round 5's HIGH-2 shipped a stripper that deleted 48% of
Doc_09 §7 and this file did not exist to catch it. Every case below is
either a defect a review actually found or a live-file invariant.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from notice_strip import (classify, live, mentions_only, notice_spans,
                          trailing_spans, unterminated)  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
FAIL = []


def check(name, cond, detail=""):
    if cond:
        print(f"  ok   {name}")
    else:
        print(f"  FAIL {name}  {detail}")
        FAIL.append(name)


print("Form A — narration inside the brackets is removed exactly")
a = ('Alpha asserts something live. **[CORRECTED, 2026-09-15 — Round 1\'s M1:** '
     'an earlier version said *"unread at source"*.**]** Beta asserts something '
     'live and uncorrected.')
check("A1 notice text gone", "unread at source" not in live(a))
check("A2 prose BEFORE the notice kept", "Alpha asserts something live." in live(a))
check("A3 prose AFTER the notice kept  <- Round 5 HIGH-2",
      "Beta asserts something live and uncorrected." in live(a), repr(live(a)))

print("\nForm B — a bare stamp never eats what follows it")
b = ("**All four are visible; none is audible. [EXTENDED, 2026-09-15 — Round 1's "
     "L12.]** The second phase does not break the pattern.")
check("B1 live trailing prose kept  <- Round 5 HIGH-2",
      "The second phase does not break the pattern." in live(b), repr(live(b)))
check("B2 trailing span is reported as undecidable", len(trailing_spans(b)) == 1)
check("B3 a phrase only in that span classifies ambiguous, not live",
      classify(b, "does not break the pattern") == "ambiguous",
      classify(b, "does not break the pattern"))
check("B4 mentions_only is False on ambiguous (re-check by hand)",
      mentions_only(b, "does not break the pattern") is False)

print("\nLOW-17 — under-strip cases that left correction prose standing")
c = ('**First, the *ANF* reading. [CORRECTED, 2026-09-15 — Round 2:** the old '
     'text read *"to be killed by death"*.**]** Live tail.')
check("C1 italics in the prefix do not defeat the match",
      "to be killed by death" not in live(c), repr(live(c)))
check("C2 live tail survives that case", "Live tail." in live(c))

d = ('**[CORRECTED, 2026-09-15 — Round 3:** the draft read *"heap [sic]"* and a '
     '[link](x) sat in the prose.**]** Live tail.')
check("D1 a ']' inside the notice body does not defeat the match",
      "heap [sic]" not in live(d), repr(live(d)))
check("D2 live tail survives that case", "Live tail." in live(d))

e = ("**" + "x" * 300 + " [CORRECTED, 2026-09-15 — Round 2:** old.**]** Live tail.")
check("E1 a prefix longer than 120 chars does not defeat the match",
      "old." not in live(e).replace("Live tail.", ""), repr(live(e)[-60:]))

print("\nLive-file invariants — the deliverables themselves")
doc = (HERE / "Doc_09_Story_Inventory.md").read_text(encoding="utf-8")
lines = doc.split("\n")


def section(start, end):
    a_ = next(i for i, ln in enumerate(lines) if ln.startswith(start))
    b_ = next(i for i, ln in enumerate(lines) if i > a_ and ln.startswith(end))
    return "\n".join(lines[a_:b_])


s7 = section("## Section 7", "## Section 8")
s2 = section("## Section 2", "## Section 3")


def independent_live_words(txt):
    """Second, independent implementation of the contract: walk the text and
    skip from each `[TAG` to its `]**` terminator. Shares no regex with the
    module under test (CLAUDE.md: truncation checks use two methods)."""
    tags = ("CORRECTED", "ADDED", "MOVED HERE", "MOVED", "REVISED", "RE-FILED",
            "WITHDRAWN", "AMENDED", "EXTENDED", "SUPERSEDED", "CORRECTION")
    out, i, n = [], 0, len(txt)
    while i < n:
        if txt[i] == "[" and any(txt.startswith("[" + g, i) for g in tags):
            while out and out[-1] == "*":      # the span owns its bold
                out.pop()
            j = txt.find("]**", i)
            i = n if j == -1 else j + 3
            out.append(" ")
        else:
            out.append(txt[i])
            i += 1
    return len("".join(out).split())


for nm, sec_ in (("\u00a77", s7), ("\u00a72", s2)):
    got, want = len(live(sec_).split()), independent_live_words(sec_)
    check(f"F1 {nm} live word count matches an independent scan "
          f"({got} vs {want})", got == want, "regexes disagree with the walker")

for nm, sec_ in (("\u00a77", s7), ("\u00a72", s2)):
    removed = [w for w in sec_.split() if w not in live(sec_).split()]
    inside = all(any(a <= sec_.find(w) < b for a, b in notice_spans(sec_))
                 for w in removed if sec_.count(w) == 1)
    check(f"F2 {nm} every uniquely-removed word lay inside a notice span", inside)

r7 = len(live(s7).split()) / len(s7.split())
r2 = len(live(s2).split()) / len(s2.split())
print(f"     (retention: \u00a77 {r7:.0%}, \u00a72 {r2:.0%}; was 52% and 38%)")
check("F4 §2's escalation paragraph is not erased", len(live(s2).split()) > 300)

print("\nRound 6 — regressions the suite did not catch")
h = ("**[MOVED, 2026-09-15 - Round 6:** moved from Story Text.]\n\n"
     "Numeria and Candida are discussed, weighed, and dispatched to peace.\n\n"
     "**[ADDED - Round 5:** narration.**]**")
check("H1 a mistyped terminator does not swallow later paragraphs  <- M5",
      "Numeria and Candida are discussed" in live(h), repr(live(h)))
check("H2 the malformed opener is reported, not acted on  <- M5",
      len(unterminated(h)) == 1, unterminated(h))
check("H3 well-formed notices report no unterminated openers",
      unterminated(a) == [] and unterminated(b) == [])

n = ('Live intro. **[CORRECTED, 2026-09-15 - Round 6:** the earlier note read '
     '*"**[ADDED, 2026-09-15 - Round 1\'s L8.**]**"* and asserted that the library '
     'largely survived.**]** Live tail.')
check("H4 a notice quoting a notice does not truncate its container  <- L8",
      classify(n, "the library largely survived") == "notice-only",
      classify(n, "the library largely survived"))
check("H5 live prose after the nested case survives", "Live tail." in live(n))

for _f in sorted((HERE / "Story-Chunks").glob("*.md")) + [HERE / "Doc_09_Story_Inventory.md"]:
    _t = _f.read_text(encoding="utf-8")
    check(f"H6 no malformed notice markup in {_f.name[:34]}",
          unterminated(_t) == [], unterminated(_t))

print("\nLOW-18 — the two strippers must agree on real input")
_src = (HERE / "scripts" / "gen_story_index.py").read_text(encoding="utf-8")
_ns = {"re": __import__("re")}
for _b in ("_TAG", "_SEP", "NOTICE"):
    _m = __import__("re").search(rf"^{_b} = .*?(?=\n[A-Za-z_#])", _src,
                                 __import__("re").S | __import__("re").M)
    if _m:
        exec(_m.group(0), _ns)
_m = __import__("re").search(r"^def strip_notices.*?(?=\n[a-zA-Z_@#])", _src,
                             __import__("re").S | __import__("re").M)
exec(_m.group(0), _ns)
for nm, sec_ in (("\u00a77", s7), ("\u00a72", s2)):
    g, l = len(_ns["strip_notices"](sec_).split()), len(live(sec_).split())
    check(f"G1 {nm} generator and notice_strip agree ({g} vs {l})", g == l,
          "the two strippers have drifted apart")

print("\n" + ("FAILED: " + ", ".join(FAIL) if FAIL else "All checks passed."))
sys.exit(1 if FAIL else 0)
