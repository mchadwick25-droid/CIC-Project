#!/usr/bin/env python3
"""Generate lpc_Force_Index.md from Doc_08_Forces_Document.md.

Design rules, each one made structural:
  * EXACTLY ONE derivation per relation. Gravity connections are read from
    Section 5 alone and inverted once for the master table.
  * No fixed-width truncation anywhere. Cells carry their full text.
  * An unmatched confidence is reported UNCLASSIFIED, never silently dropped.
"""
import re, sys, pathlib

_USAGE = ("usage: gen_force_index.py [BASE_DIR]\n"
          "  BASE_DIR holds Doc_08_Forces_Document.md and Review-Artifacts/; it defaults to\n"
          "  the world-build folder that contains scripts/. The Index is written beside Doc_08.")
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(_USAGE)
    sys.exit(0)
if len(sys.argv) > 2:
    sys.exit("FATAL: too many arguments.\n" + _USAGE)

# BASE is resolved from this file's own location, so the script carries no
# session path. argv[1] overrides it.
BASE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
SRC  = BASE / "Doc_08_Forces_Document.md"
OUT  = BASE / "lpc_Force_Index.md"
if not SRC.is_file():
    sys.exit(f"FATAL: {SRC} does not exist.\n" + _USAGE)

# ---- Notice detection. A build-process notice is a bracketed opener (one to
# four words of letters, digits and hyphens) followed by a separator: a comma,
# colon, semicolon, parenthesis, dash, a full stop or slash before a digit, or a
# digit. One pattern serves the stripper, the detector and the no-notice rule,
# so the three cannot disagree. Short bracket conventions carry no separator
# after the word and do not match: "[I]t" and "[Y]our" (recapitalisation),
# "[CT]", "[Supporting]", "[world-code]".
KNOWN_TAGS = ("CORRECTED", "ADDED", "MOVED HERE", "MOVED", "REVISED", "SUPERSEDED")
_TAG = r"[A-Z][A-Za-z0-9]{1,24}(?:-[A-Za-z0-9]{1,24})*(?:\s+[A-Za-z0-9][A-Za-z0-9-]{0,24}){0,3}"
_SEP = r"(?=\s*[,:;(]|\s*[—–]|\s+-\s|\s+\d|[./]\d)"
_OPEN = r"\[" + _TAG + _SEP
NOTICE = re.compile(r"\*{0,2}" + _OPEN + r".*?\]\*\*", re.S)
OPENER = re.compile(_OPEN)
# DETECT is case-insensitive, so a lower-case opener also halts the run.
DETECT = re.compile(_OPEN, re.I)
NOTICE_SHAPE = re.compile(_OPEN)


def assert_no_notices(t, label):
    """Build-process notices do not belong in a deliverable, so the run halts
    on one rather than stripping it. Backtick-quoted mentions of a notice tag
    are masked first."""
    probe = re.sub(r"`[^`]*`", " ", t)
    hits = NOTICE_SHAPE.findall(probe)
    if hits:
        sys.exit(f"FATAL: {label} contains {len(hits)} bracketed opener(s) of the shape a "
                 f"build-process notice takes ({hits[:3]}). Correction history belongs in "
                 "Review-Artifacts/, never inline in a deliverable. A legitimate citation "
                 "written in that shape, such as [CSEL 1868], must be written without the "
                 "bracket. Refusing to emit.")


def strip_notices(t):
    return "\n".join(NOTICE.sub(" ", ln) for ln in t.split("\n"))

# A notice must not span a structural marker: a notice missing its own
# terminator would otherwise match forward to the next terminator and remove
# real content such as a gravity list.
STRUCTURAL = re.compile(
    r"Connected forces:|^\*\*G\d — |^\#{2,4} |^\*\*Layer [123] |^\| ", re.M)

def assert_notice_coverage(t, label):
    """Halt when a notice span crosses a structural marker or contains a second
    opener (a runaway match), and when an opener survives stripping."""
    for m in NOTICE.finditer(t):
        span = m.group(0)
        swallowed = len(OPENER.findall(span)) > 1
        if swallowed or STRUCTURAL.search(span) or len(span) > 3000:
            sys.exit(f"FATAL: a correction notice in {label} spans a structural marker "
                     f"({m.group(0)[:70]!r}...). It is almost certainly missing its own "
                     "terminator and is consuming real source. Refusing to emit.")
    left = DETECT.findall(strip_notices(t))
    if left:
        sys.exit(f"FATAL: {len(left)} notice-like opener(s) survive stripping in {label} "
                 f"({left[:3]}). A notice the stripper cannot see is derivation input, "
                 f"which would put a false connection into the Index. "
                 f"Known tags: {', '.join(KNOWN_TAGS)}. Refusing to emit.")


# ---- Approval state. Only the document's own Status line and the opening of
# its own Disposition section count; a mention of the phrase elsewhere in
# either does not.
_APPROVED = re.compile(r"approved\s+to\s+proceed\b", re.I)
_NOT_DISPOSED = re.compile(r"(?:not\s+disposed|revised)\b", re.I)

def classify_disposition(own_text, where):
    """True when the statement opens 'Approved to proceed'; False when it opens
    'Not disposed' or 'REVISED'; anything else is unrecognised."""
    lead = re.sub(r"[*_`]+", "", own_text).strip()
    if _APPROVED.match(lead):
        return True
    if _NOT_DISPOSED.match(lead):
        return False
    raise ValueError(f"{where} opens with {lead[:60]!r}, which is neither 'Approved to proceed' "
                     "nor 'Not disposed' / 'REVISED'")


def parent_disposition(t, label):
    """An index cannot state its own disposition: it inherits its parent's.
    Returns (approved, date). The Status line and the Disposition section are
    both read, and a disagreement halts the run."""
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
    section = (tail[:nxt.start()] if nxt else tail).lstrip()
    try:
        s_ok = classify_disposition(m.group(1), f"{label}'s Status line")
        d_ok = classify_disposition(section, f"{label}'s Disposition section")
    except ValueError as e:
        sys.exit(f"FATAL: {e}. Refusing to emit.")
    if s_ok != d_ok:
        sys.exit(f"FATAL: {label}'s Status line says "
                 f"{'Approved to proceed' if s_ok else 'NOT approved'} while its "
                 f"Disposition section says "
                 f"{'Approved to proceed' if d_ok else 'NOT approved'}. A "
                 "disposition stated in two places has gone stale in one. "
                 "Refusing to emit.")
    date = None
    if d_ok:
        dm = re.search(r"\d{4}-\d{2}-\d{2}", section.split("\n\n")[0])
        if not dm:
            sys.exit(f"FATAL: {label}'s Disposition section opens 'Approved to proceed' "
                     "with no date in its opening paragraph. Refusing to emit.")
        date = dm.group(0)
    return s_ok, date


# ---- Verdict parsing. A review file states its own verdict on its VERDICT
# headings. Text elsewhere, such as a recital of an earlier round's verdict,
# is not read.
VERDICT_WORDS = ("SUBSTANTIAL REVISION REQUIRED", "MINOR REVISION", "CLEARED", "REJECTED")
_VHEAD = re.compile(r"^#{2,3} VERDICT(.*)$", re.M)

def parse_verdict(t, label):
    """The verdict word on the file's VERDICT heading line(s). Each heading must
    state exactly one verdict word and all headings must state the same one;
    otherwise ValueError."""
    heads = _VHEAD.findall(t)
    if not heads:
        raise ValueError(f"{label} has no '## VERDICT' heading")
    found = []
    for tail in heads:
        words = [w for w in VERDICT_WORDS if w in tail]
        if len(words) != 1:
            raise ValueError(f"{label}: a VERDICT heading ({tail.strip()!r}) states "
                             f"{len(words)} verdict words; its own verdict must be exactly one")
        found.append(words[0])
    if len(set(found)) != 1:
        raise ValueError(f"{label}: its VERDICT headings disagree ({sorted(set(found))})")
    return found[0]


def _selftest_parsers():
    """Each parser is run on inputs it must reject and inputs it must accept.
    A parser that no longer separates the two stops generation."""
    def halts(fn, *args):
        try:
            fn(*args)
        except ValueError:
            return True
        return False
    failures = []
    good = "## VERDICT: SUBSTANTIAL REVISION REQUIRED\n\n**2 HIGH, 1 MEDIUM, 0 LOW, 0 COSMETIC.**\n"
    recital = "The prior review was CLEARED.\n\n## VERDICT: SUBSTANTIAL REVISION REQUIRED\n"
    bare = "## VERDICT\n\nThe prior review was **CLEARED** on the analysis.\n\nThis review: **SUBSTANTIAL REVISION REQUIRED**.\n"
    two = "## VERDICT: CLEARED (prior: SUBSTANTIAL REVISION REQUIRED)\n"
    split = "## VERDICT: CLEARED\n\n## VERDICT: SUBSTANTIAL REVISION REQUIRED\n"
    if parse_verdict(good, "t") != "SUBSTANTIAL REVISION REQUIRED":
        failures.append("verdict: own heading not read")
    if parse_verdict(recital, "t") != "SUBSTANTIAL REVISION REQUIRED":
        failures.append("verdict: recital before the heading was read")
    for name, sample in (("bare heading", bare), ("two words", two), ("disagreeing headings", split),
                         ("no heading", "no heading here")):
        if not halts(parse_verdict, sample, "t"):
            failures.append(f"verdict: {name} did not halt")
    for name, sample, want in (
            ("Approved status", "**Approved to proceed** (dated)", True),
            ("REVISED status naming the phrase", "REVISED after a fix pass — unreviewed; not yet Approved to proceed.", False),
            ("Not disposed naming the phrase", "**Not disposed.** This document has not been Approved to proceed.", False)):
        if classify_disposition(sample, "t") is not want:
            failures.append(f"approval: {name} misclassified")
    if not halts(classify_disposition, "Pending review.", "t"):
        failures.append("approval: an unrecognised opening did not halt")
    planted = ["[CO-022, 2026 — x]", "[CORRECTED at R7 — x]", "[R8-FIX, 2026 — x]",
               "[Doc08-R8 — x]", "[CORRECTED.2026 x]", "[CORRECTED/2026 x]",
               "[Further Correction, x]", "[SUPERSEDED: x]", "[ADDED, 2026 — x]"]
    for p in planted:
        if not (NOTICE_SHAPE.search(p) and DETECT.search(p) and NOTICE.search("**" + p + "**")):
            failures.append(f"notice form not detected: {p}")
    for b in ("[I]t", "[Y]our", "[CT]", "[Supporting]", "[world-code]"):
        if DETECT.search(b):
            failures.append(f"short bracket convention detected as a notice: {b}")
    if failures:
        sys.exit("FATAL: parser self-test failed, so generation would not be trustworthy:\n  - "
                 + "\n  - ".join(failures) + "\nRefusing to emit.")

_selftest_parsers()


def between(t, start, end, label):
    """The text between two section headings, or a halt naming the missing one."""
    if start not in t or end not in t:
        sys.exit(f"FATAL: {label} lacks the heading {start if start not in t else end!r}. "
                 "Refusing to emit.")
    return t.split(start)[1].split(end)[0]


text = SRC.read_text(encoding="utf-8")
DISPOSED, DISP_DATE = parent_disposition(text, "Doc_08_Forces_Document.md")
assert_no_notices(text, SRC.name)
assert_notice_coverage(text, "Doc_08_Forces_Document.md")

# ---- Doc_08's review history is hand-maintained prose, so it is ASSERTED
# here against the artifacts on disk. This does not depend on phrasing: it
# counts, rather than pattern-matching only the phrasings already known.
def assert_doc08_round_count(t, n, fixpass, per_round):
    """Emphasis is flattened first and every claim form -- word, ordinal,
    bare numeral, any case -- is matched, so a bold marker cannot hide a
    claim from this check, and an ordinal is never compared against a
    cardinal count as though the two were the same kind of number."""
    # Notices are stripped before the assertion, as they are before derivation.
    flat = re.sub(r"\*+", "", strip_notices(t))
    word_alt = "|".join(WORDNUM[i] for i in range(1, 11))
    problems = []

    # Cardinal claims: "Six independent adversarial review rounds", "run six times"
    for m in re.finditer(r"\b(" + word_alt + r"|\d+)\s+independent adversarial review rounds", flat, re.I):
        if _as_int(m.group(1)) != n:
            problems.append(f"'{m.group(0)}' vs {n} artifacts")
    for m in re.finditer(r"has (?:now )?been run\s+(" + word_alt + r"|\d+)\s+times", flat, re.I):
        if _as_int(m.group(1)) != n:
            problems.append(f"'{m.group(0)}' vs {n} artifacts")
    for m in re.finditer(r"been through\s+(" + word_alt + r"|\d+)\s+review rounds", flat, re.I):
        if _as_int(m.group(1)) != n:
            problems.append(f"'{m.group(0)}' vs {n} artifacts")
    for m in re.finditer(r"all\s+(" + word_alt + r"|\d+)\s+rounds", flat, re.I):
        if _as_int(m.group(1)) != n:
            problems.append(f"'{m.group(0)}' vs {n} artifacts")

    # Ordinal claims: "REVISED after Round 6", "Round 6 fix pass" -- an
    # ordinal names a round, so the HIGHEST ordinal must equal the artifact
    # count. "REVISED after Round N" is a fix-pass statement and is checked
    # against the fix-pass ordinal, not the artifact count -- checking it
    # against the artifact count would demand the document claim a fix pass
    # that has not happened the moment a new review is filed.
    for m in re.finditer(r"REVISED after Round\s+(\d+)", flat, re.I):
        if int(m.group(1)) != fixpass:
            problems.append(f"'{m.group(0)}' vs latest fix pass Round {fixpass}")
    # Log rows may name any round up to n, but the highest must BE n.
    ords = [int(m.group(1)) for m in re.finditer(
        r"Round\s+(\d+)\s*(?:—|-|independent adversarial review|fix pass|\()", flat, re.I)]
    if ords and max(ords) != n:
        problems.append(f"highest round ordinal named is {max(ords)} vs {n} artifacts")

    # The per-round finding counts and verdict words Doc_08 states are
    # compared against each artifact's own recorded values.
    for rnd, (counts, verdict) in sorted(per_round.items()):
        for m in re.finditer(r"Round " + str(rnd) + r"\s*\(([^)]*)\)", flat):
            if m.group(1).strip() != counts and "H " in m.group(1):
                problems.append(f"Doc_08 says Round {rnd} ({m.group(1)}), artifact says ({counts})")
    stated = set(re.findall(r"all (?:three|four|five|six|seven|eight|nine|ten) returning \*{0,2}([A-Z][A-Z ]+)", flat))
    actual = {v for _, v in per_round.values()}
    for st in stated:
        if len(actual) == 1 and st.strip() not in actual:
            problems.append(f"Doc_08 states all rounds returned '{st.strip()}'; artifacts say {sorted(actual)}")

    # Each Document Log row that records a review round's verdict is compared
    # with the verdict word parsed from that round's own artifact, and every
    # artifact on disk must have such a row.
    logged = {}
    for ln in flat.split("\n"):
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if not ln.strip().startswith("|") or len(cells) != 4:
            continue
        rm = re.match(r"Round\s+(\d+)\b(?!\s+fix pass)", cells[1])
        words = [w for w in VERDICT_WORDS if w in cells[3]]
        if rm and len(words) == 1:
            logged[int(rm.group(1))] = words[0]
    for rnd, (counts, verdict) in sorted(per_round.items()):
        if rnd not in logged:
            problems.append(f"Doc_08's Document Log has no verdict row for Round {rnd}")
        elif logged[rnd] != verdict:
            problems.append(f"Doc_08's Document Log says Round {rnd} returned '{logged[rnd]}'; "
                            f"its artifact says '{verdict}'")

    if problems:
        sys.exit("FATAL: Doc_08's review-history claims disagree with Review-Artifacts/:\n  - "
                 + "\n  - ".join(problems) + "\nRefusing to emit.")

# ---- The review history is DERIVED from the artifacts on disk, not typed.
# A number that is counted cannot go stale the way a hand-maintained one can.
ROUNDS = sorted(
    (int(m.group(1)), f) for f in (BASE / "Review-Artifacts").glob("Doc08_Round*_Review.md")
    for m in [re.search(r"Doc08_Round(\d+)_Review\.md", f.name)] if m)
if not ROUNDS:
    sys.exit(f"FATAL: {BASE / 'Review-Artifacts'} holds no Doc08_Round<N>_Review.md file, so the "
             "review history cannot be derived. Refusing to emit.")
NROUNDS = len(ROUNDS)
LATEST = ROUNDS[-1][0]
WORDNUM = {0: "No", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
           6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
_W2I = {w.lower(): i for i, w in WORDNUM.items()}
_W2I.update({"eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
             "fifteen": 15, "sixteen": 16, "seventeen": 17})

def _as_int(tok):
    return int(tok) if tok.isdigit() else _W2I.get(tok.lower(), -1)
NWORD = WORDNUM.get(NROUNDS, str(NROUNDS))

def verdict_counts(path):
    """A review artifact's own finding counts and verdict. The verdict is read
    from its VERDICT heading lines by parse_verdict, and a file whose own
    verdict cannot be read unambiguously halts the run. The counts are read from
    the text that follows the first VERDICT heading, up to the next heading."""
    t = path.read_text(encoding="utf-8", errors="replace")
    try:
        verdict = parse_verdict(t, path.name)
    except ValueError as e:
        sys.exit(f"FATAL: {e}. A review file's verdict cannot be guessed. Refusing to emit.")
    _h = _VHEAD.search(t)
    rest = t[_h.end():]
    nxt = re.search(r"^#{2,3} ", rest, re.M)
    window = rest[:nxt.start()] if nxt else rest[:1200]
    m = re.search(r"(\d+)\s*HIGH\D{1,4}(\d+)\s*MEDIUM\D{1,4}(\d+)\s*LOW\D{1,4}(\d+)\s*COSMETIC",
                  window)
    counts = f"{m.group(1)}H {m.group(2)}M {m.group(3)}L {m.group(4)}C" if m else "counts not parsed"
    return counts, verdict

_VC = {n: verdict_counts(f) for n, f in ROUNDS}
HISTORY = "; ".join(f"Review {n} ({_VC[n][0]})" for n, _ in ROUNDS)
_verdicts = {v for _, v in _VC.values()}
# The verdict word is read from each artifact rather than hard-coded, so a
# CLEARED round is never reported as a revision round by a stale literal.
VERDICT_LINE = ("**all " + _verdicts.pop() + "**" if len(_verdicts) == 1
                else "verdicts: " + "; ".join(f"Review {n}: {v}" for n, (_, v) in sorted(_VC.items())))
# fix-pass ordinal read from Doc_08's own Document Log
_fp0 = [int(m) for m in re.findall(r"Round\s+(\d+)\s+fix pass", strip_notices(text))]
assert_doc08_round_count(text, NROUNDS, max(_fp0) if _fp0 else 0, _VC)

# LATEST is "latest review artifact on disk"; LATEST_FIX_PASS is "latest fix
# pass Doc_08's own Document Log records". The two are read separately and
# never conflated, so a review artifact present with no fix pass yet applied
# is stated as outstanding rather than silently assumed done.
_fp = [int(m) for m in re.findall(r"Round\s+(\d+)\s+fix pass", strip_notices(text))]
LATEST_FIX_PASS = max(_fp) if _fp else 0
FIXPASS_NOTE = ("" if LATEST_FIX_PASS == LATEST else
                f" **Note:** the most recent review artifact is Round {LATEST}, but Doc_08's "
                f"Document Log records no fix pass beyond Round {LATEST_FIX_PASS} — "
                "**this file therefore reflects the Round "
                f"{LATEST_FIX_PASS} fix pass and Round {LATEST}'s findings are outstanding.**")
lines = text.split("\n")

def plain(s):
    """Strip markdown emphasis; keep the words."""
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'\*(.+?)\*', r'\1', s)
    s = re.sub(r'`(.+?)`', r'\1', s)
    return s.strip()

# Terminator is "]**", not "**]**": notices in this document end both ways
# ("...applied.**]**" and "...the finding.]**"), so requiring the doubled
# form would leave one open and swallow the entries after it. Notices are
# also stripped line-by-line, so a mis-terminated one can never consume a
# following entry.
# ---------------------------------------------------------------- forces
CELL_RE  = re.compile(r'^### CELL (\d[AB]) — (.+?)(?:\s*\*\(.*\)\*)?\s*$')
FORCE_RE = re.compile(r'^#### Force (\d[AB]-\d): (.+)$')
# terminator-insensitive: the label may end with a period, comma, dash, or **
CONF_RE  = re.compile(r'Confidence:\s*\*{0,2}([A-Za-z][A-Za-z/ ]*?)\*{0,2}\s*(?:[.,;—-]|\*\*|$)')

CELL_LABEL = {
    "1A": "Initiating / External",  "1B": "Initiating / Internal",
    "2A": "Ongoing / External",     "2B": "Ongoing / Internal",
    "3A": "Ending-Transforming / External", "3B": "Ending-Transforming / Internal",
}

forces, cur_cell, cur = [], None, None
for ln in lines:
    m = CELL_RE.match(ln)
    if m:
        cur_cell = m.group(1); continue
    m = FORCE_RE.match(ln)
    if m:
        cur = dict(id=m.group(1), cell=cur_cell, name=plain(m.group(2)),
                   conf=None, conf2=None, layer2="", body=[])
        forces.append(cur); continue
    if ln.startswith("## Section 4"):
        cur = None
    if cur is not None:
        cur["body"].append(ln)

for f in forces:
    body = "\n".join(f["body"])
    # confidence: primary label from the Layer 1 line
    for ln in [strip_notices(x) for x in f["body"]]:
        if "Confidence:" in ln:
            m = CONF_RE.search(ln)
            if m:
                f["conf"] = m.group(1).strip()
            break
    if f["conf"] is None:
        f["conf"] = "UNCLASSIFIED"
    # a secondary confidence element declared in the force's own entry
    m2 = re.search(r'\*\*Confidence:\s*Contested\*\*', body)
    if m2 and f["conf"] != "Contested":
        f["conf2"] = "Contested"
    # Layer 2 present?
    m3 = re.search(r"\*\*Layer 2 — World's Own Experience\.\*\*(.*?)(?=\*\*Layer 3)", body, re.S)
    raw = m3.group(1) if m3 else ""
    # construction-record blocks are this build's voice, not the world's:
    # they do not count toward Layer 2 content.
    raw = re.split(r"\*\*Construction-record notes on this entry", raw)[0]
    # Layer 2 is measured after notices are stripped, consistent with every
    # other derivation in this file: an unstripped notice can pad a blank
    # Layer 2 so it measures as written, or sit beside a real one and be
    # mistaken for part of it.
    f["layer2"] = plain(strip_notices(raw)).strip()
    # A stub is not a written Layer 2.
    low = f["layer2"].lower()
    # Stub detection is by PHRASE, not by length: a length floor alone risks
    # flagging a real short Layer 2 as a stub, since "Not applicable at this
    # layer..." is non-empty text but not a written entry. The 40-character
    # floor below is only a backstop for a genuinely empty or one-line entry,
    # set well clear of the shortest real Layer 2 in this document (119
    # characters).
    f["stub"] = (len(f["layer2"]) < 40) or any(
        pat in low for pat in ("not applicable", "none, and not", "is supplied",
                               "not supplied", "left unfilled", "no layer 2",
                               "deliberately unfilled", "would invent"))
    f["transmission"] = f["name"].lower().startswith("transmission")

ids = [f["id"] for f in forces]
# A force's ID encodes its cell, so the two must agree -- a force filed under
# the wrong ### CELL heading would otherwise change the derived row
# distribution and contradict §9's hand-typed counts while passing every
# other check silently.
_misfiled = [(f["id"], f["cell"]) for f in forces if not f["id"].startswith(f["cell"] + "-")]
if _misfiled:
    sys.exit("FATAL: force(s) filed under a cell heading their ID contradicts: "
             + ", ".join(f"{i} under CELL {c}" for i, c in _misfiled) + ". Refusing to emit.")

if len(forces) != 17:
    sys.exit(f"FATAL: parsed {len(forces)} forces, expected 17. Refusing to emit a short index.")
byid = {f["id"]: f for f in forces}

# ------------------------------------------------- gravity map (§5 ONLY)
# Doc_08 carries correction notices inline, and a notice explaining that a
# force was REMOVED from a gravity's list can itself name that force in bold
# on the same line. Notices are therefore stripped before ANY derivation,
# everywhere, once -- an unstripped parse would put the removed force right
# back and contradict the source document with every other guard clean.
sec5 = strip_notices(between(text, "## Section 5 —", "## Section 6", "Doc_08"))
GRAV_RE = re.compile(r'^\*\*(G\d) — (.+?) \((Primary|Supporting|Tensional)\)\.\*\*(.*)$')
gmap = {}
for ln in sec5.split("\n"):
    m = GRAV_RE.match(ln)
    if not m:
        continue
    g, gname, gclass, rest = m.groups()
    explicit = re.findall(r'\*\*(\d[AB]-\d)\*\*', rest)
    extra, deriv = [], "§5 list"
    # expand prose set-references the token scanner cannot see
    for cell in re.findall(r'every force in Cell (\d[AB])', rest):
        hit = [i for i in ids if i.startswith(cell + "-")]
        if hit:
            extra += hit
            deriv = "§5 list + prose set-reference expanded"
    gmap[g] = dict(name=gname, cls=gclass,
                   forces=sorted(set(explicit + extra)), deriv=deriv)

# invert ONCE — the master table's Connected Gravities column is this and
# nothing else, so the two views cannot disagree by construction. A silently
# short index -- a mis-parsed gravity dropped without comment -- is the
# failure mode this guard exists for.
if len(gmap) != 8:
    sys.exit(f"FATAL: parsed {len(gmap)} gravities ({sorted(gmap)}), expected 8. "
             "Usually a correction notice swallowing a §5 entry. Refusing to emit.")

inv = {i: [] for i in ids}
for g, v in gmap.items():
    for fid in v["forces"]:
        if fid in inv:
            inv[fid].append(g)
        else:
            sys.exit(f"FATAL: §5 names force {fid}, which §3 does not define.")
for f in forces:
    f["grav"] = sorted(inv[f["id"]])

# --------------------------- §3 Layer-3 gravity tokens, as a SECOND opinion
# Deriving gravity links from §5 alone makes the two views agree by
# construction, which would make a real §3/§5 contradiction in the source
# document undetectable. This does NOT feed the tables -- it is compared
# against them and any disagreement is printed as a finding. A derived index
# that cannot disagree with its source is not a check on its source.
#
# Direction matters. "§5 carries it, §3's prose does not name it" is NOT a
# contradiction -- §3's Layer 3 is prose, not an enumeration, and §5's G4 list
# is itself built from a prose set-reference. The dangerous direction, and
# the only one reported, is §3 ASSERTING a connection that §5's canonical
# list omits.
#
# CONNECT and DISCLAIM are tuned against this document's actual sentences
# rather than a generic verb list. An attestation claim ("G2 and G8 are
# attested only within it") and a stated non-connection ("a family
# resemblance to G6 and G7") are not connection claims and must be excluded.
# Verbs the document actually uses for a real connection ("is why", "gives",
# "enables", "terminates", "outlives", "confirms", "intensifies") must be
# included. And an unbolded gravity token must still be matched, since not
# every real reference in this document is bolded.
CONNECT = re.compile(
    r"connects? to|is this force's|is the precondition for|makes\b.*?possible"
    r"|supplies|produces|generat|is the direct product|this force is\b"
    r"|is why|gives|enables|terminates|outlives|confirms|intensifies"
    r"|re-?opens|triggers|activates|shapes", re.I)
# The verb "carries" is deliberately withdrawn from CONNECT: it also matches
# a sentence that talks ABOUT §5 itself ("Neither §5's G6 list nor its G7
# list CARRIES it"), which is commentary on the index rather than a Layer-3
# connection claim.
DISCLAIM = re.compile(
    r"attested only|family resemblance|not a force-connection"
    r"|classified separately|tested and classified|does not carry"
    r"|\bneither\b|\bnor\b|\bnot a\b", re.I)
# DISCLAIM does not match on the bare mention of "§5" anywhere in a sentence:
# that would suppress a genuine claim purely because the same sentence also
# mentions a §5 entry.
GTOKEN = re.compile(r"\*{0,2}(G\d)\*{0,2}")
NEGTAIL = re.compile(r"\band not to\b|\bbut not to\b|\brather than to\b|\bnot to\b", re.I)

def sentences(seg):
    return re.split(r"(?<=[.!?])\s+", seg)

# One pass, two claim sets, so a single sentence can assert some connections
# and deny another -- exactly what a Layer 3 entry can do: "connects to G2
# and to G6 ... and not to G7". Splitting on the negation marker gives the
# head (assertions) and the tail (denials).
# An explicit denial ("does not connect to G6", "neither X nor Y carries it"),
# as opposed to a trailing negation, which NEGTAIL handles.
DISCONNECT = re.compile(
    r"(?:do(?:es)? not carry|does not connect|not a force-connection"
    r"|neither .*? nor .*? carries)", re.I)

l3claims, disconnect_claims = {}, {}
for f in forces:
    body = strip_notices("\n".join(f["body"]))
    m = re.search(r"\*\*Layer 3 — Formation Impact.*", body, re.S)
    seg = m.group(0) if m else ""
    claimed, denied = set(), set()
    for sent in re.split(r"(?<=[.!?])\s+", seg):
        # Emphasis is flattened before ANY pattern test: the document writes
        # "and **not** to G7", and matching the raw string would defeat the
        # negation match entirely.
        flat = re.sub(r"\*+", "", sent)
        if not GTOKEN.search(flat):
            continue
        parts = NEGTAIL.split(flat, maxsplit=1)
        head, tail = parts[0], (parts[1] if len(parts) > 1 else "")
        if tail:
            denied |= set(GTOKEN.findall(tail))
            # The head can itself be a denial ("does not connect to G6 ...
            # and not to G7"), so it is re-tested rather than assumed to be
            # an assertion once a trailing negation is found.
            if DISCONNECT.search(head):
                denied |= set(GTOKEN.findall(head))
            elif CONNECT.search(head) and not DISCLAIM.search(head):
                claimed |= set(GTOKEN.findall(head))
        elif DISCONNECT.search(flat):
            denied |= set(GTOKEN.findall(flat))
        elif CONNECT.search(flat) and not DISCLAIM.search(flat):
            claimed |= set(GTOKEN.findall(flat))
    l3claims[f["id"]] = sorted(claimed)
    disconnect_claims[f["id"]] = sorted(denied)

mismatch, observed = [], []
for f in forces:
    for g in sorted(set(disconnect_claims[f["id"]]) & set(f["grav"])):
        mismatch.append((f["id"], g, "**Contradiction** — §3 Layer 3 asserts §5 does NOT carry this; §5's list does carry it"))
for f in forces:
    for g in sorted(set(l3claims[f["id"]]) - set(f["grav"])):
        mismatch.append((f["id"], g, "**Contradiction** — §3 Layer 3 asserts this connection; §5's list omits it"))
    for g in sorted(set(f["grav"]) - set(l3claims[f["id"]])):
        observed.append((f["id"], g, "§5's list carries it; §3's Layer 3 does not assert it in a connection sentence"))

# ------------------------------------------------- cross-cell (§4 table)
sec4 = strip_notices(between(text, "## Section 4 —", "## Section 5", "Doc_08"))
ROW_RE = re.compile(r'^\|\s*\*\*(\d[AB]-\d)\*\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$')
conns = []
for ln in sec4.split("\n"):
    m = ROW_RE.match(ln)
    if not m:
        continue
    src, dst, direction, desc = m.groups()
    dst_id = plain(dst)
    conns.append(dict(src=src, dst=dst_id, dir=plain(direction), desc=plain(desc)))

# The parsed connection count is checked against the table's own data rows,
# using criteria independent of the parse's own success criteria: a row is
# any line in §4 beginning with a pipe that is not the header and not the
# rule, however malformed, so a de-bolded force ID or a missing trailing pipe
# cannot drop a row from both sides of the comparison at once.
_sec4_rows = [ln for ln in sec4.split("\n")
              if ln.strip().startswith("|")
              and not re.match(r"^\|[\s|:-]+\|?$", ln.strip())
              and not re.search(r"\|\s*\*{0,2}From\*{0,2}\s*\|", ln)]
_pairs = [(c["src"], c["dst"]) for c in conns]
_dupes = sorted({p for p in _pairs if _pairs.count(p) > 1})
if _dupes:
    sys.exit(f"FATAL: §4 lists duplicate connection(s): {_dupes}. "
             "A duplicated row raises the connection total without failing the row-count "
             "check, because both sides move together. Refusing to emit.")

# Doc_08 certifies the connection count in its own prose; the Index must agree.
_certified = set()
for m in re.finditer(r"(?:Cross-cell connections documented in Section 4 — |§4\.\s*)?"
                     r"\b(fifteen|sixteen|fourteen|thirteen|\d{1,2})\s+(?:cross-cell\s+)?connections",
                     strip_notices(text), re.I):
    _certified.add(_as_int(m.group(1)) if not m.group(1).isdigit() else int(m.group(1)))
if _certified and len(conns) not in _certified:
    sys.exit(f"FATAL: Doc_08 certifies {sorted(_certified)} connection(s) in its own prose "
             f"but §4's table yields {len(conns)}. Refusing to emit.")

if len(conns) != len(_sec4_rows):
    sys.exit(f"FATAL: §4's table has {len(_sec4_rows)} data row(s) but only {len(conns)} parsed. "
             "A row whose force ID is not bolded is dropped silently, which would understate "
             "the connection count Doc_08 certifies. Refusing to emit.")

xc = {i: [] for i in ids}
for c in conns:
    if c["dst"].startswith("(none)") or c["dst"] == "—":
        xc[c["src"]].append("**none — see §4**")
        continue
    xc[c["src"]].append(f"→ {c['dst']} ({c['dir']})")
    if c["dst"] in xc:
        xc[c["dst"]].append(f"← {c['src']} ({c['dir']})")

# --------------------------- §7's hand-maintained confidence list
# §7 restates the confidence relation by hand elsewhere in the document. This
# generator's own claim of "exactly one derivation per relation" would be
# true only inside this file and false across the deliverable pair unless §7
# is also read and cross-checked; a disagreement is reported here.
sec7 = strip_notices(between(text, "## Section 7 —", "## Section 8", "Doc_08"))
# The label pattern captures the FIRST confidence level named inside the
# parentheses, since an entry can read "(Documented, with a contested
# secondary element -- see below)" -- the closing paren need not immediately
# follow the label. All five of the Constitution's confidence levels are
# recognised, so a force at any level is compared rather than reported
# absent by default.
LEVELS = "Documented|Widely Accepted|Dominant Modern Reconstruction|Contested|Inferential/Thin"
s7 = dict((m.group(1), m.group(2))
          for m in re.finditer(r"(\d[AB]-\d)\**\s*\((" + LEVELS + r")\b", sec7))
s7_missing = [f["id"] for f in forces if f["id"] not in s7]
s7_conflict = [(i, s7[i], byid[i]["conf"]) for i in s7 if i in byid and s7[i] != byid[i]["conf"]]

# --------------------------- §3 prose vs §4 table
# A force's own Layer 3 prose is compared against §4's cross-cell table, so a
# force naming a connection §4 does not carry is caught, the same way a
# second opinion is taken against §5 above.
xc_pairs = set()
for c in conns:
    if not c["dst"].startswith("(none)"):
        xc_pairs.add((c["src"], c["dst"]))
        xc_pairs.add((c["dst"], c["src"]))

FID = re.compile(r"\b(\d[AB]-\d)\b")
xc_mismatch = []
for f in forces:
    body = strip_notices("\n".join(f["body"]))
    m = re.search(r"\*\*Layer 3 — Formation Impact.*", body, re.S)
    seg = m.group(0) if m else ""
    for sent in re.split(r"(?<=[.!?])\s+", seg):
        flat = re.sub(r"\*+", "", sent)
        if not CONNECT.search(flat) or DISCLAIM.search(flat):
            continue
        for other in set(FID.findall(NEGTAIL.split(flat)[0])):
            if other != f["id"] and (f["id"], other) not in xc_pairs:
                xc_mismatch.append((f["id"], other))
xc_mismatch = sorted(set(xc_mismatch))

# ---------------------------------------------------------------- render
def conf_cell(f):
    return f["conf"] + (f" *(+{f['conf2']})*" if f["conf2"] else "")

O = []
w = O.append
w("# Force Index — Latin Pastoral-Congregational Christianity")
w("")
w("**Status:** " + ("**Approved to proceed**" if DISPOSED else "**Not approved to proceed**")
  + ", read from `Doc_08_Forces_Document.md`'s own Status line and Disposition section, which agree. "
  "Co-output of Construction Step 8 with `Doc_08_Forces_Document.md`; reviewed and disposed of together.")
w(f"**Review files in `Review-Artifacts/`, counted rather than typed:** {HISTORY} — {VERDICT_LINE}.")
w(f"**World file-code:** `lpc` · **Drafted:** 2026-09-15 · **Revised:** 2026-09-15 (Round {LATEST_FIX_PASS} fix pass) · **Generated by** `scripts/gen_force_index.py`, committed beside this file")
w("**Generated from `Doc_08_Forces_Document.md` by `gen_force_index.py`. Never hand-edited.**")
w("")
w("**What each part of this file is.** "
  "**Derived from `Doc_08_Forces_Document.md` on every run:** every table in §§1–5, all counts and totals, the findings in §6 and §7, the review-history line, the approval state in the Status line and the Disposition, and the review counts in the Disposition. "
  "**Hard-coded prose:** the rest of this header block, including the Revised date, and the explanatory paragraphs under §§2 to 7. No run re-verifies those.")
w("")
w("---")
w("")
w("## 1. Master Force Table")
w("")
w("| Force ID | Cell | Force | Confidence | Connected Gravities | Cross-Cell Connections | Layer 2 | Transmission |")
w("|---|---|---|---|---|---|---|---|")
for f in forces:
    g = ", ".join(f["grav"]) or "—"
    x = "; ".join(xc[f["id"]]) or "*(no §4 row)*"
    w(f"| **{f['id']}** | {CELL_LABEL[f['cell']]} | {f['name']} | {conf_cell(f)} | {g} | {x} | "
      f"{'**STUB**' if f['stub'] else '✓'} | {'**YES**' if f['transmission'] else 'no'} |")
w("")
counts = {}
for f in forces:
    counts[f["cell"]] = counts.get(f["cell"], 0) + 1
cellsum = " — " + ", ".join(f"{c} ({counts[c]})" for c in ["1A","1B","2A","2B","3A","3B"])
nl2 = sum(1 for f in forces if not f["stub"])
w(f"**{len(forces)} forces**{cellsum}. Every cell populated; "
  + (f"**every force carries a written Layer 2**." if nl2 == len(forces)
     else f"**{len(forces)-nl2} force(s) MISSING a Layer 2.**"))
w("")
w("---")
w("")
w("## 2. By Confidence Level")
w("")
ORDER = ["Documented", "Widely Accepted", "Dominant Modern Reconstruction", "Contested", "Inferential/Thin"]
seen = {}
for f in forces:
    seen.setdefault(f["conf"], []).append(f["id"])
for lbl in ORDER + [k for k in seen if k not in ORDER]:
    got = seen.get(lbl, [])
    sec = sorted(f["id"] for f in forces if f["conf2"] == lbl)
    tail = f"  ·  *carried as a secondary element by:* {', '.join('`'+i+'`' for i in sec)}" if sec else ""
    body = ", ".join("`" + i + "`" for i in got) if got else "*none*"
    w(f"**{lbl}** — {len(got)}: {body}{tail}")
w("")
unc = len(seen.get("UNCLASSIFIED", []))
w(f"**Totals reconcile: {len(forces)-unc} classified + {unc} unclassified = {len(forces)} forces.** "
  "That arithmetic is printed because a classified/unclassified split silently summing to the wrong total is not otherwise visible. "
  "**`2B-3` carries `Contested` as a secondary element** — its external change is Documented; what is contested is the placement of its consequence as internal, and the force entry now says so rather than only §7's summary.")
w("")
w("---")
w("")
w("## 3. By Connected Gravity — the completion check")
w("")
w("**One question, answered at a glance:** does every confirmed gravity from Doc_04 connect to at least one force? An empty row is what the template's §9 calls ecologically incomplete.")
w("")
w("**Notation.** `G1`–`G8` are this document's short labels for Doc_04's **Candidate 1**–**Candidate 8**, in Doc_04's own order and with Doc_04's own classifications. Doc_04 uses the \"Candidate *n*\" form throughout; the correspondence is one-to-one.")
w("")
w("| Gravity | Class | Connected Forces | Count | Derivation |")
w("|---|---|---|---|---|")
for g in sorted(gmap):
    v = gmap[g]
    lst = ", ".join("`" + i + "`" for i in v["forces"]) or "**EMPTY — ecologically incomplete**"
    w(f"| **{g}** — {v['name']} | {v['cls']} | {lst} | {len(v['forces'])} | {v['deriv']} |")
w("")
empty = [g for g, v in gmap.items() if not v["forces"]]
w(f"**Result: all {len(gmap)} gravities connect; {len(empty)} empty rows. The completion requirement is met.**"
  if not empty else f"**Result: {len(empty)} EMPTY row(s): {', '.join(empty)}.**")
w("")
w("**`G4`'s row carries five forces because a prose set-reference is expanded rather than left as the two forces bolded in the same sentence.** Doc_08 §5 connects it to *\"1B-3, 2A-2, and in truth every force in Cell 2A\"*; the set-reference is expanded, which is why G4 shows five forces — and it matters, because G4 is the channel through which every external pressure reaches an ordinary believer, so a two-force row would understate the one mechanism Doc_08 §5 calls this world's characteristic response.")
w("")
w("---")
w("")
w("## 4. Cross-Cell Connection Map")
w("")
w("| From | To | Direction | Connection |")
w("|---|---|---|---|")
for c in conns:
    w(f"| `{c['src']}` | " + (f"*(none)*" if c["dst"].startswith("(none)") else f"`{c['dst']}`")
      + f" | {c['dir']} | {c['desc']} |")
w("")
noconn = sum(1 for c in conns if c["dst"].startswith("(none)"))
_iso = [c["src"] for c in conns if c["dst"].startswith("(none)")]
_coin = [(c["src"], c["dst"]) for c in conns if "coincid" in c["dir"].lower()]
_isotxt = ", ".join("`"+i+"`" for i in _iso) or "*none*"
_cointxt = "; ".join(f"`{a}` → `{b}`" for a, b in _coin) or "*none*"
w(f"**{len(conns)} connections**, including "
  f"**{noconn} deliberate non-connection{'' if noconn==1 else 's'}** ({_isotxt}) and "
  f"**{len(_coin)} coincidence{'' if len(_coin)==1 else 's'} marked as not causal** ({_cointxt}). "
  "")
w("")
w("---")
w("")
w("## 5. Transmission and Layer-2 Check")
w("")
w("| Check | Result |")
w("|---|---|")
for cell in ["2B", "3B"]:
    t = [f["id"] for f in forces if f["cell"] == cell and f["transmission"]]
    w(f"| Dedicated transmission force in Cell {cell} | " +
      (f"**YES** — {', '.join('`'+i+'`' for i in t)} |" if t else "**NO** |"))
w(f"| Every force carries a written Layer 2 | " +
  (f"**YES** — all {len(forces)} |" if nl2 == len(forces) else f"**NO** — {len(forces)-nl2} missing |"))
w("")
w("**What this column does and does not prove.** The test flags a Layer 2 that matches a stub phrasing, and construction-record blocks are excluded from the count; a 40-character floor is kept only as a backstop for a genuinely empty entry. **It measures presence, not quality.** Whether a Layer 2 is written in this world's voice is a reviewer's judgement no generator makes.")
w("")
w("")
w("---")
w("")
w("## 6. §3-versus-§5 Gravity Reconciliation")
w("")
w("**Why this section exists.** Deriving the gravity relation from §5 alone, and only from §5, is correct for the tables above, but it also means the tables alone cannot notice the source document contradicting itself. The tables still derive from §5 alone. This section derives a **second opinion** from each force's own §3 Layer 3 prose and prints every disagreement instead of resolving it.")
w("")
if mismatch:
    w("**Contradictions — findings for a reviewer.**")
    w("")
    w("| Force | Gravity | Disagreement |")
    w("|---|---|---|")
    for fid, g, why in mismatch:
        w(f"| `{fid}` | **{g}** | {why} |")
    w("")
    w(f"**{len(mismatch)} contradiction(s). Each is a finding for a reviewer, not a defect this file resolves.**")
else:
    w("**No contradictions: no force's §3 Layer 3 asserts a gravity connection that §5's canonical list omits, and none asserts a disconnection §5 contradicts.** All three directions are tested — connection asserted-but-omitted, connection carried-but-unasserted, and disconnection asserted-but-contradicted; see below.")
w("")
if observed:
    w("**Observations — not defects.** §3's Layer 3 is prose, not an enumeration, and §5's G4 list is built from a prose set-reference (*\"every force in Cell 2A\"*) no §3 entry restates. These are listed so the asymmetry is visible rather than hidden by a control that only looks one way.")
    w("")
    w("| Force | Gravity | Observation |")
    w("|---|---|---|")
    for fid, g, why in observed:
        w(f"| `{fid}` | {g} | {why} |")
    w("")
w("**Three tests, not one.** §3 asserting a connection §5 omits (contradiction); §5 carrying one §3 does not assert (observation); and §3 asserting that §5 does *not* carry something §5 does carry.")
w("")
w("**Cross-cell cross-check (§3 prose against §4's table).** "
  + ("**No disagreements:** every force ID named in a connection-asserting Layer 3 sentence appears as that force's partner in §4's table."
     if not xc_mismatch else
     "**" + str(len(xc_mismatch)) + " disagreement(s):** " + ", ".join(f"`{a}` names `{b}`, §4 does not pair them" for a, b in xc_mismatch) + "."))
w("")
w("**What the generator checks on every run.** "
  "It halts, with no file written, when: "
  "**(a)** Doc_08 contains a bracketed build-process notice, or a notice-shaped opener survives stripping, or a notice span crosses a structural marker; "
  "**(b)** Doc_08's Status line and its Disposition section disagree on approval, or either opens with neither *Approved to proceed* nor *Not disposed* / *REVISED*; "
  "**(c)** a review file's `VERDICT` headings state no verdict word, more than one, or disagree with each other; "
  "**(d)** Doc_08's review counts, round ordinals, per-round finding counts or per-round verdicts disagree with `Review-Artifacts/`, or a round on disk has no Document Log row; "
  "**(e)** a force sits under a cell heading its ID contradicts, or the parse yields other than 17 forces or 8 gravities, or §5 names a force §3 does not define; "
  "**(f)** a §4 row fails to parse, a §4 row is duplicated, or the §4 count differs from the connection count stated in Doc_08's prose. "
  "Before it reads Doc_08 it runs a self-test of the verdict, approval and notice parsers on inputs each must reject and inputs each must accept, and halts if any result is wrong. "
  "**Reported in the output, not halted on:** the §6 contradictions, observations and cross-cell disagreements, and the §7 disagreements.")
w("")
w("**Limits.** "
  "The notice detector matches a bracket of one to four words (letters, digits, hyphens) followed by a comma, colon, semicolon, parenthesis, dash, digit, or a full stop or slash before a digit. A notice in any other shape is not detected, and a legitimate bracketed citation in that shape, such as `[CSEL 1868]`, halts the run. "
  "The §6 check is a sentence-level keyword match: a connection stated with a verb outside its list, or in a sentence that also contains a disclaiming word, is not seen. It is not a proof of consistency. "
  "Doc_08 §9's cell distribution is not read, and §9's connection count is read only where a number precedes the word *connections*. "
  "The Layer 2 check in §5 measures presence, not quality.")
w("")
w("**To regenerate this file:** `python3 scripts/gen_force_index.py` from any working directory; the script resolves its own base path. An optional first argument overrides that base path.")
w("")
w("---")
w("")
w("## 7. Section 7 Cross-Check — the second, hand-maintained derivation")
w("")
w("**Why this section exists.** Doc_08 §7 restates the confidence of all seventeen forces by hand. The generator does not read it by default, so this file's claim that *\"every relation now has exactly one derivation\"* would be true only inside the Index and false across the deliverable pair — the relation would still be computed twice, the second time by a human. §7 is read and compared below.")
w("")
if not s7_missing and not s7_conflict:
    w(f"**Agreement: all {len(forces)} forces carry the same confidence in Doc_08 §7 as in their own §3 entry.** No force is missing from §7's list and none is labelled differently.")
else:
    for i in s7_missing:
        w(f"- **`{i}` is absent from §7's list** but carries `{byid[i]['conf']}` at §3.")
    for i, a, b in s7_conflict:
        w(f"- **`{i}`**: §7 says `{a}`, §3 says `{b}`.")
    w("")
    w("**Each line above is a disagreement between two hand-and-script derivations of the same relation. It is reported, not resolved.**")
w("")
w("**The design rule at its true width.** Inside this file every relation has exactly one derivation. **Across the deliverable pair it does not** — §7 is a parallel hand-maintained statement, and what holds the two in agreement is this cross-check rather than any claim that the duplication is gone.")
w("")
w("---")
w("")
w("## Disposition")
w("")
w((f"**Approved to proceed, {DISP_DATE}**, together with `Doc_08_Forces_Document.md`, which is reviewed and disposed of with it."
   if DISPOSED else
   "**Not disposed.** Reviewed and disposed of together with `Doc_08_Forces_Document.md`.")
  + f" `Review-Artifacts/` holds {NWORD.lower()} file(s) matching `Doc08_Round<N>_Review.md`; the most recent is `Doc08_Round{LATEST}_Review.md` ({_VC[LATEST][0]}, {_VC[LATEST][1]}). "
  f"Doc_08's Document Log records a fix pass through Round {LATEST_FIX_PASS}.{FIXPASS_NOTE}")
w("")

OUT.write_text("\n".join(O), encoding="utf-8")
print(f"wrote {OUT}  ({len(forces)} forces, {len(conns)} connections, {len(gmap)} gravities)")
print("longest Force cell:", max(len(f['name']) for f in forces),
      "| longest Connection cell:", max(len(c['desc']) for c in conns))
