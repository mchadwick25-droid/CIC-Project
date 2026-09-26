#!/usr/bin/env python3
"""Generate lpc_Story_Index.md from Doc_09 and the Story-Chunks/ files.

Built on what eight review rounds of `gen_force_index.py` cost to learn:

  * DERIVE, never type. Every count, tier tally and table row below is read
    from the chunks. A number typed here is a number that goes stale.
  * Correction notices are NOT derivation input. Both tag and separator are
    open patterns, and the coverage assertion is deliberately BROADER than
    the stripper -- a guard built from the same string as the thing it guards
    can only detect what it already strips.
  * Every relation has exactly one derivation, and where a second statement
    of the same relation exists (Doc_09 §3's hand-written table), it is
    CROSS-CHECKED rather than trusted.
  * FAIL LOUDLY. A short or inconsistent index is worse than none.
"""
import re, sys, pathlib

BASE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
DOC = BASE / "Doc_09_Story_Inventory.md"
ART = BASE / "Review-Artifacts"
CHUNKS = BASE / "Story-Chunks"
REG = BASE / "Source_Registry.md"
OUT = BASE / "lpc_Story_Index.md"

TAGS = r"CORRECTED|ADDED|MOVED HERE|MOVED|REVISED|CORRECTION|SUPERSEDED"
# One negation vocabulary, shared by every polarity-aware derivation in this
# script, so that fixing it in one place fixes it everywhere.
NEG_CLAUSE = re.compile(
    r"\bnot been read\b|\bhas not\b|\bnot used\b|\bunread\b|\bnot vendored\b"
    r"|\bExcluded\b|\bnot built\b|\bneither\b|\bnor\b|\bdoes not\b|\bdo not\b"
    r"|\bnot connected\b|\bbears on neither\b", re.I)
# Round 5's MEDIUM-4: NEG_CLAUSE catches "has not been read" and misses the
# other way a row gets named without being used -- stated availability.
# lpcstory003 names rows 191/194 as a "Latin second witness" and Doc_09 §8
# item 6 records that check as PENDING; the index credited both rows as
# sources the story "actually draws on". Same class as M4(c), fourth
# recurrence. A row named because it EXISTS is not a row DRAWN ON.
AVAIL_CLAUSE = re.compile(
    r"\bsecond witness\b|\bpending\b|\bavailable\b|\bLatin only\b"
    r"|\bwhere no English\b|\bnot yet\b|\bwould let\b|\byet to be\b", re.I)
# A clause that both claims USE and carries a negation is ambiguous, and
# Round 5 showed the silent guess runs the wrong way: "row 28 supplies the
# formula, which the Registry does not otherwise license" demoted a row that
# IS used. The script no longer guesses -- it halts and asks for two
# sentences. Polarity is a fact about the chunk, not about this regex.
USE_VERB = re.compile(r"\b(?:supplies|supply|provides|provide|gives|give|"
                      r"carries|carry|is drawn on|are drawn on|draws on)\b", re.I)
# CF V7.4 ties a confidence band to each tier; a mismatch is a classification
# error. Round 5's COSMETIC-5: this was declared `global` INSIDE the chunk
# loop and rebuilt every iteration, leaving it undefined if the loop body
# never ran while it is read again further down.
BANDS = {"1": {"Documented", "Widely Accepted"},
         "2": {"Widely Accepted", "Dominant Modern Reconstruction"},
         "3": {"Contested", "Inferential/Thin"},
         "4": {"Inferential/Thin"}}

# 2026-09-15 — the notice system was removed from the deliverables.
#
# Build-process notices used to live inline in Doc_09, the chunks and this
# index — 76 spans, ~3,100 words, up to 23% of a chunk. That created a
# MENTION-versus-USE problem (a corrected phrase survives inside the notice
# recording it), which needed a stripper to resolve, which then had to be
# right. `scripts/notice_strip.py` produced a HIGH finding in two rounds
# (5 and 7), each inside the fix for the previous round's finding. Two
# strippers also had to be kept in step with each other. Round 8 then found
# the module CORRECT under 200,000 fuzzed inputs — so this removal is about
# where change history belongs, not about a broken tool.
#
# The correction history now lives in
# `Review-Artifacts/Doc09_Correction_History.md`, per CLAUDE.md's rule that
# change history belongs in the audit trail and never inline in a canonical
# surface. So there is nothing to strip, no mention/use question, and no
# second implementation to keep in step.
#
# What remains is ONE guard, pointing the other way: a notice anywhere in a
# deliverable is FATAL. It replaces three weaker guards (swallowed openers,
# openers surviving the stripper, notices inside Story Text) and cannot be
# defeated by an unrecognised tag, because it matches the SHAPE rather than
# a vocabulary.
NOTICE_SHAPE = re.compile(
    r"\[(?:[A-Z][A-Za-z]{1,24})(?:\s+[A-Za-z][A-Za-z]{0,24}){0,3}"
    r"(?:\s*[,:;(]|\s*[—–]|\s+-\s|\s+\d)")


def assert_no_notices(t, label):
    """A build-process notice in a deliverable is corruption, not content."""
    hits = NOTICE_SHAPE.findall(t)
    if hits:
        sys.exit(f"FATAL: {label} contains {len(hits)} build-process notice(s) "
                 f"({hits[:3]}). Correction history belongs in "
                 "Review-Artifacts/Doc09_Correction_History.md, never inline "
                 "in a deliverable. Refusing to emit.")


# ------------------------------------------------------------------ chunks
def field(block, name):
    # \Z matters: the LAST field in the block has no following field and no
    # closing fence inside the captured group, so without it every chunk's
    # Do-Not-Retrieve-When read as missing and the guard fired on good files.
    m = re.search(rf"^{name}:\s*(.+?)(?=\n[A-Z][A-Za-z-]*:|\n```|\Z)", block, re.S | re.M)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

stories = []
# Round 5's LOW-15: two files carrying the same story id produced "Eight
# stories -- Tier 1 (7)" with two identical rows and no halt.
_seen_ids = {}
for p in sorted(CHUNKS.glob("lpcstory*.md")):
    raw = p.read_text(encoding="utf-8")
    assert_no_notices(raw, p.name)
    t = raw
    fm = re.search(r"```(.*?)```", t, re.S)
    if not fm:
        sys.exit(f"FATAL: {p.name} has no retrieval front-matter block. Refusing to emit.")
    b = fm.group(1)
    sid = p.name.split("_")[0]
    if sid in _seen_ids:
        sys.exit(f"FATAL: story id '{sid}' is claimed by two chunk files, "
                 f"{_seen_ids[sid]} and {p.name}. Refusing to emit.")
    _seen_ids[sid] = p.name
    s = dict(id=sid, file=p.name, title=field(b, "Story-Title"), tier=field(b, "Tier"),
             conf=field(b, "Confidence"), src=field(b, "Source"),
             rw=field(b, "Retrieve-When"), dnr=field(b, "Do-Not-Retrieve-When"), body=t)
    for k in ("title", "tier", "conf", "src", "rw", "dnr"):
        if not s[k]:
            sys.exit(f"FATAL: {p.name} is missing front-matter field '{k}'. Refusing to emit.")
    if s["tier"] not in {"1", "2", "3", "4"}:
        sys.exit(f"FATAL: {p.name} declares Tier '{s['tier']}'. The four-tier rule permits 1-4 and "
                 "CF V7.4 states there is NO Tier 5. Refusing to emit.")
    for sec in ("## Story Text", "## Formation Ecology Connection", "## Tier Justification", "## Usage Guidance"):
        if sec not in t:
            sys.exit(f"FATAL: {p.name} is missing the required section '{sec}'. Refusing to emit.")
    if s["tier"] == "4" and "## Source Identification" not in t:
        sys.exit(f"FATAL: {p.name} is Tier 4 and has no Source Identification section, which the "
                 "L4 template requires for Tier 4 only. Refusing to emit.")
    # CF V7.4 ties a confidence band to each tier; a mismatch is a classification error.
    # Round 5's LOW-9: `b in s["conf"]` is a SUBSTRING test, so a Tier 1
    # chunk declaring "Not Documented" passed and the No-Tier-5 audit printed
    # "Yes -- Not Documented". Bands are compared as whole tokens now.
    _decl = {b for b in BANDS[s["tier"]]
             if re.search(r"(?<!\bnot )(?<!\bNot )\b" + re.escape(b) + r"\b", s["conf"])}
    if not _decl:
        sys.exit(f"FATAL: {p.name} is Tier {s['tier']} with Confidence '{s['conf']}', outside the band "
                 f"CF V7.4 assigns that tier ({sorted(BANDS[s['tier']])}). Refusing to emit.")
    # Round 1's M4(c): this scanned the Source field for row numbers WITHOUT
    # REGARD TO POLARITY, so a row cited in order to say it was NOT used was
    # credited as though it were. lpcstory006 names row 41 (the Acta) in the
    # clause "has not been read in this build", and the index then asserted
    # "Every cited row is Native" over it. A row mentioned inside a negating
    # clause is excluded, and what was excluded is reported rather than
    # silently dropped -- a silent exclusion is the same defect inverted.
    # Round 5's MEDIUM-5: this findall carried no IGNORECASE, so a Source
    # sentence BEGINNING with a row citation -- "Row 28 supplies ..." -- was
    # invisible to every derivation including the Excluded-row boundary
    # guard. A breach was one capital letter away.
    ROW_RE = re.compile(r"row(?:s)?\s+((?:\d+)(?:\s*[/,]\s*\d+)*)", re.I)
    used, excluded = [], []
    for clause in re.split(r"(?<=[.;])\s+", s["src"]):
        found = ROW_RE.findall(clause)
        if not found:
            continue
        neg = NEG_CLAUSE.search(clause) or AVAIL_CLAUSE.search(clause)
        if neg and USE_VERB.search(clause):
            sys.exit(
                f"FATAL: {p.name}'s Source field claims both use and non-use of "
                f"row(s) {found} in one clause:\n    {clause.strip()}\n"
                "Polarity cannot be derived from it. Split it into two "
                "sentences, one stating what the story draws on and one "
                "stating what is named but not drawn on. Refusing to emit.")
        (excluded if neg else used).extend(found)
    s["rows"] = sorted(set(used), key=str)
    s["rows_excluded"] = sorted(set(excluded), key=str)
    # Round 2: this was polarity-blind -- the SAME defect Round 1's M4(c) had
    # just fixed for Registry rows, eleven lines above, in this same script.
    # "bears on neither G5 nor G7" printed G5 and G7 as connected gravities.
    # Fixing one instance of a defect class and not looking for its siblings
    # is the shape this build keeps repeating; both derivations now share
    # NEG_CLAUSE so they cannot drift apart again.
    grav = set()
    # Round 3: the splitter could not break at ".**", so a chunk's own
    # "**Gravities: G2 …, G1 ….**" line joined the sentence after it -- and
    # where that sentence said "does not persist", the negation filter threw
    # the declaration away with it. Both entries were right only because
    # Retrieve-When happens to repeat the codes. Split on a bold-run boundary
    # as well as on sentence punctuation.
    for clause in re.split(r"(?<=[.;])\s+|(?<=\.\*\*)\s*|\n", t):
        if NEG_CLAUSE.search(clause):
            continue
        grav |= set(re.findall(r"\b(G[1-8])\b", clause))
    s["gravities"] = sorted(grav)
    stories.append(s)

if not stories:
    sys.exit("FATAL: no story chunks found. Refusing to emit.")

def parent_disposition(t, label):
    """An index cannot state its own disposition: it inherits its parent's.

    Hard-coding it is how a Status line and a Disposition section drift apart,
    so both are read from the parent here and a disagreement halts the run.
    """
    m = re.search(r"^\*\*Status:\s*\*{0,2}(.*)$", t, re.M)
    if not m:
        sys.exit(f"FATAL: {label} carries no '**Status:' line, so this index "
                 "cannot derive its own disposition. Refusing to emit.")
    d = re.search(r"^#{2,3}\s*(?:\d+\.\s*)?Disposition\s*$", t, re.M)
    if not d:
        sys.exit(f"FATAL: {label} carries no Disposition section, so this index "
                 "cannot derive its own disposition. Refusing to emit.")
    tail = t[d.end():]
    nxt = re.search(r"^#{2,3}\s", tail, re.M)
    section = tail[:nxt.start()] if nxt else tail
    APP = re.compile(r"approved to proceed", re.I)
    s_ok, d_ok = bool(APP.search(m.group(1))), bool(APP.search(section))
    if s_ok != d_ok:
        sys.exit(f"FATAL: {label}'s Status line says "
                 f"{'Approved to proceed' if s_ok else 'NOT approved'} while its "
                 f"Disposition section says "
                 f"{'Approved to proceed' if d_ok else 'NOT approved'}. A "
                 "disposition stated in two places has gone stale in one. "
                 "Refusing to emit.")
    return s_ok


doc = DOC.read_text(encoding="utf-8")
DISPOSED = parent_disposition(doc, "Doc_09_Story_Inventory.md")
assert_no_notices(doc, DOC.name)
doc_live = doc

# --- cross-check Doc_09 §3's hand-written table against the chunks themselves
sec3 = doc_live.split("## Section 3 — Story Index")[1].split("### 3.1")[0]
# Round 1's M4(b): only the TIER column was compared, though the masthead
# claimed the whole table -- and a live divergence already existed in the
# Confidence column at lpcstory006. Tier AND confidence are compared now.
claimed = {m.group(1): tuple(x.strip() for x in m.groups()[1:])
           for m in re.finditer(
               r"\|\s*`(lpcstory\d+)`\s*\|\s*([^|]*?)\s*\|\s*(\d)\s*\|\s*([^|]+?)\s*\|"
               r"\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|", sec3)}
problems = []
for s in stories:
    if s["id"] not in claimed:
        problems.append(f"{s['id']} exists as a chunk but is absent from Doc_09 §3's table")
        continue
    ctitle, ctier, cconf, csrccell, cgravcell = claimed[s["id"]]
    # Round 2: §3 could retitle a story "Cyprian of Antioch" with no halt.
    # A first fix compared "significant words" and let that exact scenario
    # through, because "Cyprian" appears in both -- a fuzzy test that fails
    # open is worse than none. The index is generated, so exact agreement is
    # a real invariant: titles must match on case- and punctuation-normalised
    # text, and a reword in either place halts until both are changed.
    def _norm(x):
        return re.sub(r"[^a-z0-9 ]", "", x.lower()).strip()
    if _norm(ctitle) != _norm(s["title"]):
        problems.append(f"{s['id']}: Doc_09 §3 titles it '{ctitle}', the chunk titles it '{s['title']}'")
    if ctier != s["tier"]:
        problems.append(f"{s['id']}: Doc_09 §3 says Tier {ctier}, the chunk says Tier {s['tier']}")
    # the chunk may state a fuller band than the table; the table must not
    # state one the chunk does not carry.
    if cconf.split(";")[0].strip().lower() not in s["conf"].lower():
        problems.append(f"{s['id']}: Doc_09 §3 says Confidence '{cconf}', the chunk says '{s['conf']}'")
    # Round 1's M4(b) asked for Gravities and Source too; Round 2 added Title
    # and Confidence and the masthead kept claiming the whole table. Both
    # remaining columns are compared now, so the claim is true.
    cgrav = set(re.findall(r"G[1-8]", cgravcell))
    # Round 5's MEDIUM-5: `if cgrav and ...` skipped the comparison entirely
    # when §3's Gravities cell carried no G-code, so the masthead's claim of
    # full-table agreement was untrue. This is the surviving half of Round
    # 4's M4 -- the source half was fixed and this one was not.
    if not cgrav:
        problems.append(f"{s['id']}: Doc_09 §3 states no gravities (cell: {cgravcell.strip()!r})")
    elif cgrav != set(s["gravities"]):
        problems.append(f"{s['id']}: Doc_09 §3 lists gravities {sorted(cgrav)}, the chunk yields {s['gravities']}")
    csrc_rows = {r for grp in re.findall(r"row(?:s)?\s+((?:\d+)(?:\s*[/,]\s*\d+)*)",
                                        csrccell, re.I)
                 for r in re.split(r"[/,]\s*", grp)}
    # Round 5's LOW-20: the comparison ran one way only, so §3 could name
    # FEWER rows than the chunk with no halt -- which is how MEDIUM-4's
    # divergence (§3: row 1; index: rows 1, 191, 194) reached committed
    # output uncaught. Both directions are compared now.
    # Round 6's LOW-4: s["rows"] holds raw capture groups such as "191/194"
    # while csrc_rows is already split, so a correct chunk halted. Fails
    # closed, but a guard that cannot be satisfied by correct input is a
    # defect. Both sides are split now, as the neighbouring comparisons are.
    _srows = {r for grp in s["rows"] for r in re.split(r"[/,]\s*", grp)}
    _missing = _srows - csrc_rows
    if _missing:
        problems.append(f"{s['id']}: the chunk draws on row(s) {sorted(_missing)} "
                        f"that Doc_09 §3's Source column does not name")
    # Requiring only an INTERSECTION failed open, exactly as the first title
    # check did: §3 could cite a nonexistent row beside a real one and pass.
    # Every row §3 names must be one the chunk actually draws on.
    # Round 4's M4: subtracting rows_excluded meant Doc_09 §3 could cite as a
    # story's SOURCE precisely the row the chunk says it never opened, with no
    # halt -- Round 1's M4(c) polarity blindness reappearing inside the fix
    # written for it. §3's Source column states what a story draws on, so an
    # excluded row appearing there is a defect, not an exemption.
    _used = {r for grp in s["rows"] for r in re.split(r"[/,]\s*", grp)}
    _excl = {r for grp in s.get("rows_excluded", []) for r in re.split(r"[/,]\s*", grp)}
    for _r in sorted(csrc_rows & _excl):
        problems.append(f"{s['id']}: Doc_09 §3 cites row {_r} as a source, but the chunk says it does not draw on it")
    _stray = sorted(csrc_rows - _used - _excl)
    if _stray:
        problems.append(f"{s['id']}: Doc_09 §3 cites row(s) {_stray} the chunk does not draw on")
for cid in claimed:
    if cid not in {s["id"] for s in stories}:
        problems.append(f"{cid} is listed in Doc_09 §3 but no chunk file exists")
if problems:
    sys.exit("FATAL: Doc_09 §3 disagrees with the chunks:\n  - " + "\n  - ".join(problems) + "\nRefusing to emit.")

phase_of = {m.group(1): m.group(2).strip()
            for m in re.finditer(r"\|\s*`(lpcstory\d+)`\s*\|(?:[^|]*\|){5}\s*([^|]+?)\s*\|", sec3)}
# Round 5's LOW-10: an all-whitespace Phase cell yielded "" and passed, so
# the Master Table printed a blank Phase under a comment claiming "a missing
# value is reported rather than inferred". Emptiness is now the test.
missing_phase = [s["id"] for s in stories
                 if not phase_of.get(s["id"], "").strip()]
if missing_phase:
    sys.exit(f"FATAL: Doc_09 §3 states no transmission phase for {missing_phase}. Refusing to emit.")

# --- Absent Stories must be substantive, not a placeholder
absent = doc_live.split("## Section 7 — Absent Stories")[1].split("## Section 8")[0]
# Round 1's M4(e): the guard counted with one pattern and §5 rendered with a
# different one over the same text, so a legal Markdown variant passed the
# guard and emitted garbage rows under an unchanged "Not a placeholder."
# ONE pattern now, used for both.
# Both legal Markdown forms: "**1. Heading**" and "**1.** Heading". Making the
# guard and renderer share one pattern was necessary and NOT sufficient --
# the shared pattern still could not read the second form, and §5 emitted
# rows opening with a stray "**" under an unchanged "Not a placeholder."
ABSENT_ITEM = re.compile(r"^\*\*(\d)\.(?:\*\*)?\s*(.+?)(?:\*\*|(?<=\.)(?=\s)|$)", re.M)
absent_items = ABSENT_ITEM.findall(absent)
if len(absent_items) < 2 or len(absent.split()) < 250:
    sys.exit(f"FATAL: Doc_09 §7 (Absent Stories) has {len(absent_items)} enumerated item(s) and "
             f"{len(absent.split())} words. CF V7.4 requires the question answered substantively. Refusing to emit.")

# --- source cross-reference against the Registry
reg = REG.read_text(encoding="utf-8")
def boundary(row):
    m = re.search(rf"^\|\s*{row}\s*\|(.*)$", reg, re.M)
    if not m: return "ROW NOT FOUND"
    cells = [c.strip() for c in m.group(1).split("|")]
    for c in cells:
        cc = re.sub(r"\*+", "", c)
        if cc in ("Native", "Excluded"): return cc
    return "not found in Source_Registry.md"

# Round 6's MEDIUM-4: this was built from s["rows"] only, so any row routed
# into rows_excluded -- by a negation OR by the AVAIL_CLAUSE vocabulary added
# at Round 5 -- was never boundary-checked at all. One ordinary word
# ("available", "pending") took an Excluded row out of the guard whose output
# prints "The check is mechanical". Round 5 fixed an instance and enlarged the
# class; this checks BOTH sets, which closes it without a vocabulary.
# A row this world may not use is a breach whether or not a chunk claims it
# used it, so polarity is irrelevant to the boundary question.
allrows = sorted({r for s in stories for key in ("rows", "rows_excluded")
                  for grp in s[key] for r in re.split(r"[/,]\s*", grp)}, key=int)
bmap = {r: boundary(r) for r in allrows}
bad = [r for r, v in bmap.items() if v != "Native"]
if bad:
    sys.exit(f"FATAL: row(s) {bad} named in a story's Source field are not Native in "
             f"Source_Registry.md "
             f"({ {r: bmap[r] for r in bad} }). Since Round 6 this checks disclaimed rows "
             "too, so the breach is naming a non-Native row at all, whichever "
             "polarity the chunk claims. Refusing to emit.")

# ------------------------------------------------------------------ render
O = []; w = O.append
tiers = {t: [s for s in stories if s["tier"] == t] for t in "1234"}
NW = {0:"No",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}

w("# Story Index — Latin Pastoral-Congregational Christianity")
w("")
# Round 2: this said "DRAFT -- not reviewed" in the pass that RESPONDED to
# Round 1, because it was a literal. Counted from the artifacts on disk now,
# the same remedy gen_force_index.py needed after going stale twice.
_rounds = sorted(int(m.group(1)) for f in ART.glob("Doc09_Round*_Review.md")
                 for m in [re.search(r"Doc09_Round(\d+)_Review", f.name)] if m)
NR = len(_rounds); LATEST = _rounds[-1] if _rounds else 0
# Round 5's LOW-8: this claimed "this file is the Round N fix pass" purely
# because Doc09_RoundN_Review.md existed -- so a one-word review artifact
# landing on disk made the index assert a fix pass that had not happened,
# and it fired the moment Round 5's own review file was written. The review
# count comes from the artifacts; the FIX-PASS claim comes from Doc_09's own
# Document Log, which the fix pass has to write.
_fixed = sorted(int(m) for m in re.findall(r"\|\s*Round (\d+) fix pass", doc))
FIXED = _fixed[-1] if _fixed else 0
# Round 7's COSMETIC-2: this map stopped at six, so the seventh round would
# have printed a digit mid-sentence. Extended by hand to twelve, which is a
# typed literal and will go stale again if this ever reaches thirteen rounds.
_NW = {0: "No", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
       7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve"}
w(f"**Status:** " + ("**Approved to proceed**, inherited from `Doc_09_Story_Inventory.md`'s own "
   f"Disposition, which governs this line; the Round {FIXED} fix pass is itself unreviewed."
   if DISPOSED and FIXED else
   "**Approved to proceed**, inherited from `Doc_09_Story_Inventory.md`'s own Disposition, which governs this line."
   if DISPOSED else
   f"**REVISED after Round {FIXED} — the revision is unreviewed, and not self-disposed.**"
   if NR and FIXED else "**DRAFT — not reviewed, not self-disposed.**") +
  " Co-output of Construction Step 9 with `Doc_09_Story_Inventory.md` and `Story-Chunks/`; reviewed and disposed of together.")
w(f"**Review history, counted from `Review-Artifacts/` rather than typed:** "
  + (f"{_NW.get(NR, NR)} round(s) — " + ", ".join(f"Round {r}" for r in _rounds) if NR else "none run")
  + ".")
w("**World file-code:** `lpc` · **Drafted:** 2026-09-15 · **Generated by** `scripts/gen_story_index.py`, committed beside this file.")
w("")
w("**To regenerate:** `python3 scripts/gen_story_index.py` from any working directory — the script resolves its own base path.")
w("")
w("**What re-running the generator re-verifies, stated exactly.** **Derived, and re-checked on every run:** every table below, every count, the tier tallies, the confidence-band check, the source cross-reference against `Source_Registry.md`, and the agreement between each chunk and Doc_09 §3's own table. **Hard-coded prose, re-verified by nothing:** the explanatory paragraphs, including this one.")
w("")
# The count is read off this file rather than typed. It has been misstated in
# three consecutive rounds across two generators, always by being copied
# forward into the Decision Log and then into the next round's brief.
# Round 3: counting the string "sys.exit(" in this file counts THIS LINE's
# own literal too, so the self-derived figure was 14 where 13 sites exist
# -- and it was wrong in the same sentence as a notice saying thirteen.
# A count derived from a script's own source text is a literal in
# disguise. Parsed from the syntax tree instead, which cannot see itself.
_NHALT = sum(1 for _n in __import__("ast").walk(
    __import__("ast").parse(pathlib.Path(__file__).read_text(encoding="utf-8")))
    if isinstance(_n, __import__("ast").Call)
    and getattr(getattr(_n, "func", None), "attr", None) == "exit")
# Round 5's LOW-12: the masthead enumerated EIGHT conditions under a derived
# count of thirteen, for a third round. The enumeration is a list now, and
# the script halts if it ever stops matching the count it is printed beside
# -- prose that can drift from a derived number is a literal in disguise too.
GUARD_LABELS = (
    "no story chunks found at all",
    "a story whose Doc_09 §3 row, tier, confidence or gravities disagree with its chunk",
    "a story with no transmission phase in Doc_09 §3",
    "an Absent-Stories section short enough to be a placeholder",
    "a story sourced to a row that is not **Native** in the Registry",
    "a chunk with no retrieval front-matter fence",
    "two chunk files claiming the same story id",
    "**a chunk declaring a Tier 5**",
    "a Tier 4 chunk with no Source Identification section",
    "a tier/confidence pair outside the band CF V7.4 assigns that tier",
    "a chunk missing a front-matter field",
    "a chunk missing a required section",
    "a Source clause that claims both use and non-use of the same row",
    "a build-process notice anywhere in a deliverable",
    "a parent document with no Status line to inherit a disposition from",
    "a parent document with no Disposition section to inherit one from",
    "a parent whose Status line and Disposition section state different dispositions",
    "this list itself falling out of step with the script's halting-site count",
)
if len(GUARD_LABELS) != _NHALT:
    sys.exit(f"FATAL: this script has {_NHALT} halting sites but GUARD_LABELS "
             f"names {len(GUARD_LABELS)}. The index masthead would misdescribe "
             "its own guards. Refusing to emit.")
_GUARD_PROSE = "; ".join(GUARD_LABELS[:-1]) + "; and " + GUARD_LABELS[-1] + "."
w(f"**Guards that halt the run rather than emitting a wrong index — {_NHALT} of them, counted off this script rather than typed.** {_GUARD_PROSE}")
w("")
w("")
w("")
w("")
w("---")
w("")
w("## 1. Master Story Table")
w("")
w("| ID | Story | Tier | Confidence | Gravities | Transmission phase | Chunk |")
w("|---|---|---|---|---|---|---|")
for s in stories:
    # Round 1's M4(d): phase was guessed from author keywords in the Source
    # field, so adding "Augustine" to a phase-one source flipped it. It is
    # read from Doc_09 §3's own Phase column, which a human sets, and a
    # missing value is reported rather than inferred.
    ph = phase_of.get(s["id"], "**NOT STATED**")
    # Round 5's COSMETIC-1, fourth round: a two-clause confidence band made
    # the master table unscannable at the one row a reader most wants to
    # scan. The leading band goes in the table; the full declaration is
    # printed under it, so nothing is lost by shortening the cell.
    _short = s["conf"].split(";")[0].strip()
    _cell = _short + (" …" if _short != s["conf"].strip() else "")
    w(f"| **{s['id']}** | {s['title']} | {s['tier']} | {_cell} | {', '.join(s['gravities']) or '—'} | {ph} | `{s['file']}` |")
w("")
_trunc = [s for s in stories if s["conf"].split(";")[0].strip() != s["conf"].strip()]
if _trunc:
    w("Confidence cells above carry the leading band only where a chunk declares "
      "more than one. In full: " + "; ".join(
          f"**{s['id']}** — {s['conf']}" for s in _trunc) + ".")
    w("")
w(f"**{NW.get(len(stories), len(stories))} stories** — " +
  ", ".join(f"Tier {t} ({len(tiers[t])})" for t in "1234") + ".")
w("")
w("---")
w("")
w("## 2. By Tier")
w("")
for t in "1234":
    lst = ", ".join("`"+s["id"]+"`" for s in tiers[t]) or "*none*"
    w(f"**Tier {t}** — {len(tiers[t])}: {lst}")
w("")
w("**Tier 4 carries the most inferential weight and is the tier a reviewer should be able to find without reading the repository — which is why it has its own line above even at zero.** CF V7.4 assigns Tier 4 **Inferential/Thin confidence regardless of how well-sourced the individual elements are**, and places Tier 4 narration in ecological-reconstruction sections. This world's Tier 4 material is in `Doc_05_Ecological_Reconstruction.md`, marked as reconstruction there; Doc_09 §3.1 records that as a placement decision rather than an absence.")
w("")
w("**Tier 2 is zero and the reason is evidentiary, not editorial.** Tier 2 requires a collection with an identifiable collection history, and this world transmitted itself by correspondence rather than by remembered story. **What Doc_08 §2B-5 establishes is that Cyprian forwarded a thirteen-letter dossier of his own; whether the corpus as a whole was assembled in his lifetime is not something this build has established.** The Tier 2 finding does not depend on the answer — Tier 2 requires a *community's* remembered collection, and this world has none either way. See Doc_09 §3.1.")
w("")
w("---")
w("")
w("## 3. No-Tier-5 Audit")
w("")
w("**The rule, from CF V7.4:** *\"Generated or illustrative narrative … is not permitted within this framework. If the evidence does not support a story, the story does not exist for this world. Silence in thin areas is the right response.\"*")
w("")
w("| Story | Tier declared | Within the four permitted tiers? | Confidence within CF's band for that tier? |")
w("|---|---|---|---|")
for s in stories:
    # Round 1's M4(a): these two answer columns were the string literals
    # "**Yes**" and "**Yes**", printed regardless of what the chunk said --
    # an output with no live computation, in the audit table whose whole
    # purpose is to be computed, and against this script's own "DERIVE,
    # never type". They are now the evaluated predicates. (Both conditions
    # also halt the run above, so a "No" is unreachable in a file that
    # emits; it is printed derived so that the table cannot go stale if a
    # guard is ever relaxed, and the redundancy is the point.)
    in_tiers = s["tier"] in {"1", "2", "3", "4"}
    # Round 6's LOW-3: Round 5's L9 rewrote the GUARD to compare whole tokens
    # with a not-lookbehind and left this renderer on the old substring test,
    # so "Not Documented" printed as "**Yes** -- Not Documented". This line is
    # the backstop the comment below calls the point of the duplication; a
    # backstop weaker than the guard it backs is not redundancy.
    in_band = bool({b for b in BANDS[s["tier"]]
                    if re.search(r"(?<!\bnot )(?<!\bNot )\b" + re.escape(b) + r"\b",
                                 s["conf"])})
    w(f"| `{s['id']}` | {s['tier']} | {'**Yes**' if in_tiers else '**NO**'} | "
      f"{('**Yes** — ' + s['conf']) if in_band else '**NO** — ' + s['conf']} |")
w("")
w(f"**{len(stories)} of {len(stories)} stories classified within the four permitted tiers, each with a confidence band CF V7.4 assigns that tier. Zero unclassified, zero ambiguous, zero Tier 5.**")
w("")
w("**This table is a structural check and not a substitute for reading the stories.** It proves each chunk *declares* a permitted tier and a consistent band. **Whether a story is genuinely sourced rather than composited is a reviewer's judgement no script makes** — Doc_09 §4 is where that judgement is recorded, story by story, and §6 records **five** candidates considered and not built.")
w("")
w("---")
w("")
w("## 4. Source Cross-Reference")
w("")
w("| Story | Registry row(s) cited | Boundary Status (read from `Source_Registry.md`) |")
w("|---|---|---|")
for s in stories:
    rs = sorted({r for grp in s["rows"] for r in re.split(r"[/,]\s*", grp)}, key=int)
    ex = sorted({r for grp in s.get("rows_excluded", []) for r in re.split(r"[/,]\s*", grp)}, key=int)
    # "explicitly not used" was accurate for a negated clause and wrong for
    # an availability clause (lpcstory003's "Latin second witness"), which
    # Round 5's MEDIUM-4 added. One label covers both.
    extra = (" · *named, not drawn on: " + ", ".join(ex) + "*") if ex else ""
    w(f"| `{s['id']}` | {', '.join(rs) or '—'}{extra} | " + ", ".join(f"row {r}: **{bmap[r]}**" for r in rs) + " |")
w("")
w(f"**Every row a story actually draws on is Native. No story draws on an Excluded row, and none draws on a neighbouring world's evidence base.** The check is mechanical: the row number is read from each chunk's own Source field and its Boundary Status read from the Registry table. **A story sourced to an Excluded row halts the generator** — the nearest live case is row 28, *The Passion of the Scillitan Martyrs*, marked **Excluded, Named Comparandum**, which Doc_09 §6 records as considered and not built.")
w("")
w("**Rows a chunk names in order to say it did *not* use them are listed separately and excluded from the check.** The derivation was **polarity-blind**: `lpcstory006` names rows 41 and 194 inside the clause *\"has not been read in this build\"*, and the index credited it with them and then asserted they were Native — **vouching for a source the chunk says it never opened.** They are shown rather than silently dropped, because a silent exclusion is the same defect inverted.")
w("")
w("---")
w("")
w("## 5. Absent Stories Check")
w("")
items = absent_items
w(f"**Doc_09 §7 answers the required question with {NW.get(len(items), len(items)).lower()} enumerated absences, in {len(absent.split())} words.** Not a placeholder.")
w("")
w("| # | Absence named |")
w("|---|---|")
for n, txt in items:
    _t = re.sub(r"\s+", " ", txt).strip()
    w(f"| {n} | {_t} |")
w("")
w("**The generator checks that this section is substantive — enumerated and above a word floor — and nothing more.** Whether the absences named are the *right* ones is a reviewer's question. Doc_09 §7 item 1 is the one to test hardest: this world's 133-year documentary silence is the absence that distinguishes it from every other world in the portfolio, and a repository that did not name it would be concealing its central evidentiary fact.")
w("")
w("---")
w("")
w("## 6. Retrieval Matrix")
w("")
w("| Story | Retrieve-When (summary) | Do-Not-Retrieve-When (summary) |")
w("|---|---|---|")
for s in stories:
    rw = s["rw"].split(";")[0].strip().rstrip(".")
    dnr = s["dnr"].split(".")[0].strip()
    w(f"| `{s['id']}` | {rw}… | {dnr}. |")
w("")
w("---")
w("")
w("## Disposition")
w("")
w(("**Approved to proceed, 2026-09-15**, together with `Doc_09_Story_Inventory.md` and the chunks in `Story-Chunks/`, which are reviewed and disposed of with it. "
   if DISPOSED else
   "**Not disposed.** Reviewed and disposed of together with `Doc_09_Story_Inventory.md` and the chunks in `Story-Chunks/`. ")
  + (f"**{_NW.get(NR, NR)} independent review round(s) have been run**, the most recent `Review-Artifacts/Doc09_Round{LATEST}_Review.md`; this file is regenerated from the Round {FIXED} fix pass and is **unreviewed**."
     if FIXED >= LATEST else
     f"**{_NW.get(NR, NR)} independent review round(s) have been run**, the most recent `Review-Artifacts/Doc09_Round{LATEST}_Review.md`; **no fix pass has been recorded against it in Doc_09's Document Log**, so this file still reflects the Round {FIXED} pass."
     if NR else "**No review round has been run against any of the three.**")
  + " Not self-certified. Not Frozen.")
w("")

OUT.write_text("\n".join(O), encoding="utf-8")
print(f"wrote {OUT}  ({len(stories)} stories; tiers " +
      ", ".join(f"{t}:{len(tiers[t])}" for t in "1234") + ")")
