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
CHUNKS = BASE / "Story-Chunks"
REG = BASE / "Source_Registry.md"
OUT = BASE / "lpc_Story_Index.md"

TAGS = r"CORRECTED|ADDED|MOVED HERE|MOVED|REVISED|CORRECTION|SUPERSEDED"
_TAG = r"[A-Z][A-Za-z]{1,24}(?:\s+[A-Za-z][A-Za-z]{0,24}){0,3}"
_SEP = r"(?=\s*[,:;(]|\s*[—–]|\s+-\s|\s+\d)"
NOTICE = re.compile(r"\*{0,2}\[" + _TAG + _SEP + r".*?\]\*\*", re.S)
OPENER = re.compile(r"\[" + _TAG + _SEP)
DETECT = re.compile(r"\[[A-Za-z][A-Za-z]{1,24}(?:\s+[A-Za-z][A-Za-z]{0,24}){0,3}"
                    r"(?:\s*[,:;(]|\s*[—–]|\s+-\s|\s+\d)", re.I)

def strip_notices(t):
    return "\n".join(NOTICE.sub(" ", ln) for ln in t.split("\n"))

def assert_coverage(t, label):
    for m in NOTICE.finditer(t):
        if len(OPENER.findall(m.group(0))) > 1:
            sys.exit(f"FATAL: a notice in {label} swallows another notice's opener "
                     f"({m.group(0)[:70]!r}...). Refusing to emit.")
    left = DETECT.findall(strip_notices(t))
    if left:
        sys.exit(f"FATAL: {len(left)} notice-like opener(s) survive stripping in {label} "
                 f"({left[:3]}). A notice the stripper cannot see is derivation input. Refusing to emit.")

# ------------------------------------------------------------------ chunks
def field(block, name):
    # \Z matters: the LAST field in the block has no following field and no
    # closing fence inside the captured group, so without it every chunk's
    # Do-Not-Retrieve-When read as missing and the guard fired on good files.
    m = re.search(rf"^{name}:\s*(.+?)(?=\n[A-Z][A-Za-z-]*:|\n```|\Z)", block, re.S | re.M)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

stories = []
for p in sorted(CHUNKS.glob("lpcstory*.md")):
    raw = p.read_text(encoding="utf-8")
    assert_coverage(raw, p.name)
    t = strip_notices(raw)
    fm = re.search(r"```(.*?)```", t, re.S)
    if not fm:
        sys.exit(f"FATAL: {p.name} has no retrieval front-matter block. Refusing to emit.")
    b = fm.group(1)
    sid = p.name.split("_")[0]
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
    global BANDS
    BANDS = {"1": {"Documented", "Widely Accepted"},
             "2": {"Widely Accepted", "Dominant Modern Reconstruction"},
             "3": {"Contested", "Inferential/Thin"},
             "4": {"Inferential/Thin"}}
    if not any(b in s["conf"] for b in BANDS[s["tier"]]):
        sys.exit(f"FATAL: {p.name} is Tier {s['tier']} with Confidence '{s['conf']}', outside the band "
                 f"CF V7.4 assigns that tier ({sorted(BANDS[s['tier']])}). Refusing to emit.")
    # Round 1's M4(c): this scanned the Source field for row numbers WITHOUT
    # REGARD TO POLARITY, so a row cited in order to say it was NOT used was
    # credited as though it were. lpcstory006 names row 41 (the Acta) in the
    # clause "has not been read in this build", and the index then asserted
    # "Every cited row is Native" over it. A row mentioned inside a negating
    # clause is excluded, and what was excluded is reported rather than
    # silently dropped -- a silent exclusion is the same defect inverted.
    NEG = re.compile(r"\bnot been read\b|\bhas not\b|\bnot used\b|\bunread\b"
                     r"|\bnot vendored\b|\bExcluded\b|\bnot built\b", re.I)
    used, excluded = [], []
    for clause in re.split(r"(?<=[.;])\s+", s["src"]):
        found = re.findall(r"row(?:s)?\s+((?:\d+)(?:\s*[/,]\s*\d+)*)", clause)
        (excluded if NEG.search(clause) else used).extend(found)
    s["rows"] = sorted(set(used), key=str)
    s["rows_excluded"] = sorted(set(excluded), key=str)
    s["gravities"] = sorted(set(re.findall(r"\b(G[1-8])\b", t)))
    stories.append(s)

if not stories:
    sys.exit("FATAL: no story chunks found. Refusing to emit.")

doc = DOC.read_text(encoding="utf-8")
assert_coverage(doc, DOC.name)
doc_live = strip_notices(doc)

# --- cross-check Doc_09 §3's hand-written table against the chunks themselves
sec3 = doc_live.split("## Section 3 — Story Index")[1].split("### 3.1")[0]
# Round 1's M4(b): only the TIER column was compared, though the masthead
# claimed the whole table -- and a live divergence already existed in the
# Confidence column at lpcstory006. Tier AND confidence are compared now.
claimed = {m.group(1): (m.group(2).strip(), m.group(3).strip())
           for m in re.finditer(r"\|\s*`(lpcstory\d+)`\s*\|[^|]*\|\s*(\d)\s*\|\s*([^|]+?)\s*\|", sec3)}
problems = []
for s in stories:
    if s["id"] not in claimed:
        problems.append(f"{s['id']} exists as a chunk but is absent from Doc_09 §3's table")
        continue
    ctier, cconf = claimed[s["id"]]
    if ctier != s["tier"]:
        problems.append(f"{s['id']}: Doc_09 §3 says Tier {ctier}, the chunk says Tier {s['tier']}")
    # the chunk may state a fuller band than the table; the table must not
    # state one the chunk does not carry.
    if cconf.split(";")[0].strip().lower() not in s["conf"].lower():
        problems.append(f"{s['id']}: Doc_09 §3 says Confidence '{cconf}', the chunk says '{s['conf']}'")
for cid in claimed:
    if cid not in {s["id"] for s in stories}:
        problems.append(f"{cid} is listed in Doc_09 §3 but no chunk file exists")
if problems:
    sys.exit("FATAL: Doc_09 §3 disagrees with the chunks:\n  - " + "\n  - ".join(problems) + "\nRefusing to emit.")

phase_of = {m.group(1): m.group(2).strip()
            for m in re.finditer(r"\|\s*`(lpcstory\d+)`\s*\|(?:[^|]*\|){5}\s*([^|]+?)\s*\|", sec3)}
missing_phase = [s["id"] for s in stories if s["id"] not in phase_of]
if missing_phase:
    sys.exit(f"FATAL: Doc_09 §3 states no transmission phase for {missing_phase}. Refusing to emit.")

# --- Absent Stories must be substantive, not a placeholder
absent = doc_live.split("## Section 7 — Absent Stories")[1].split("## Section 8")[0]
absent_items = re.findall(r"^\*\*\d\.", absent, re.M)
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
    return "status not parsed"

allrows = sorted({r for s in stories for grp in s["rows"] for r in re.split(r"[/,]\s*", grp)}, key=int)
bmap = {r: boundary(r) for r in allrows}
bad = [r for r, v in bmap.items() if v != "Native"]
if bad:
    sys.exit(f"FATAL: story source row(s) {bad} are not Native in Source_Registry.md "
             f"({ {r: bmap[r] for r in bad} }). A story sourced to an Excluded row is a boundary breach. Refusing to emit.")

# ------------------------------------------------------------------ render
O = []; w = O.append
tiers = {t: [s for s in stories if s["tier"] == t] for t in "1234"}
NW = {0:"No",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}

w("# Story Index — Latin Pastoral-Congregational Christianity")
w("")
w("**Status:** **DRAFT — not reviewed, not self-disposed.** Co-output of Construction Step 9 with `Doc_09_Story_Inventory.md` and `Story-Chunks/`; reviewed and disposed of together.")
w("**World file-code:** `lpc` · **Drafted:** 2026-09-15 · **Generated by** `scripts/gen_story_index.py`, committed beside this file.")
w("")
w("**To regenerate:** `python3 scripts/gen_story_index.py` from any working directory — the script resolves its own base path.")
w("")
w("**What re-running the generator re-verifies, stated exactly.** **Derived, and re-checked on every run:** every table below, every count, the tier tallies, the confidence-band check, the source cross-reference against `Source_Registry.md`, and the agreement between each chunk and Doc_09 §3's own table. **Hard-coded prose, re-verified by nothing:** the explanatory paragraphs, including this one.")
w("")
w("**Guards that halt the run rather than emitting a wrong index.** A chunk missing a front-matter field or a required section; **a chunk declaring a Tier 5**; a tier/confidence pair outside the band CF V7.4 assigns that tier; a Tier 4 chunk with no Source Identification section; a story whose Doc_09 §3 tier disagrees with its own chunk; a story sourced to a row that is not **Native** in the Registry; an Absent-Stories section short enough to be a placeholder; and a correction notice that swallows another's opener. **[CORRECTED, 2026-09-15 — Round 1's brief-correction 1:** this said *nine* guards and called them *the eight lessons*; **the script has thirteen halting sites and Round 1 forced all of them.** The miscount went from this prose into the Decision Log and then into Round 1's own brief without being re-derived — the same shape `gen_force_index.py` produced three rounds running. Counted here with a grep over the script rather than from memory.**]**")
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
    w(f"| **{s['id']}** | {s['title']} | {s['tier']} | {s['conf']} | {', '.join(s['gravities']) or '—'} | {ph} | `{s['file']}` |")
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
w("**Tier 2 is zero and the reason is evidentiary, not editorial.** Tier 2 requires a collection with an identifiable collection history. This world transmitted itself by correspondence, and a dossier assembled by its own author in his own lifetime is not a community's remembered collection. See Doc_09 §3.1.")
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
    in_band = any(b in s["conf"] for b in BANDS[s["tier"]])
    w(f"| `{s['id']}` | {s['tier']} | {'**Yes**' if in_tiers else '**NO**'} | "
      f"{('**Yes** — ' + s['conf']) if in_band else '**NO** — ' + s['conf']} |")
w("")
w(f"**{len(stories)} of {len(stories)} stories classified within the four permitted tiers, each with a confidence band CF V7.4 assigns that tier. Zero unclassified, zero ambiguous, zero Tier 5.**")
w("")
w("**This table is a structural check and not a substitute for reading the stories.** It proves each chunk *declares* a permitted tier and a consistent band. **Whether a story is genuinely sourced rather than composited is a reviewer's judgement no script makes** — Doc_09 §4 is where that judgement is recorded, story by story, and §6 records two candidates declined on exactly that ground.")
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
    extra = (" · *named but explicitly not used: " + ", ".join(ex) + "*") if ex else ""
    w(f"| `{s['id']}` | {', '.join(rs) or '—'}{extra} | " + ", ".join(f"row {r}: **{bmap[r]}**" for r in rs) + " |")
w("")
w(f"**Every row a story actually draws on is Native. No story draws on an Excluded row, and none draws on a neighbouring world's evidence base.** The check is mechanical: the row number is read from each chunk's own Source field and its Boundary Status read from the Registry table. **A story sourced to an Excluded row halts the generator** — the nearest live case is row 28, *The Passion of the Scillitan Martyrs*, marked **Excluded, Named Comparandum**, which Doc_09 §6 records as considered and not built.")
w("")
w("**Rows a chunk names in order to say it did *not* use them are listed separately and excluded from the check. [CORRECTED, 2026-09-15 — Round 1's M4(c).]** The derivation was **polarity-blind**: `lpcstory006` names rows 41 and 194 inside the clause *\"has not been read in this build\"*, and the index credited it with them and then asserted they were Native — **vouching for a source the chunk says it never opened.** They are shown rather than silently dropped, because a silent exclusion is the same defect inverted.")
w("")
w("---")
w("")
w("## 5. Absent Stories Check")
w("")
items = re.findall(r"^\*\*(\d)\.\s*(.+?)\*\*", absent, re.M)
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
w("**Not disposed.** Reviewed and disposed of together with `Doc_09_Story_Inventory.md` and the chunks in `Story-Chunks/`. **No review round has been run against any of the three.** Not self-certified. Not Frozen.")
w("")

OUT.write_text("\n".join(O), encoding="utf-8")
print(f"wrote {OUT}  ({len(stories)} stories; tiers " +
      ", ".join(f"{t}:{len(tiers[t])}" for t in "1234") + ")")
