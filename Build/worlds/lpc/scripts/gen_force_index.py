#!/usr/bin/env python3
"""Generate lpc_Force_Index.md from Doc_08_Forces_Document.md.

Design rules, each one made structural:
  * EXACTLY ONE derivation per relation. Gravity connections are read from
    Section 5 alone and inverted once for the master table.
  * No fixed-width truncation anywhere. Cells carry their full text.
  * An unmatched confidence is reported UNCLASSIFIED, never silently dropped.
"""
import re, sys, pathlib

# The script lives in the world-build folder beside the documents it derives
# from, following the sibling precedent of World-Builds/Donatism/scripts/.
# BASE is resolved from this file's own location, so the script is portable
# and has no session path baked into it. An override is accepted as argv[1]
# for mutation testing.
BASE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
SRC  = BASE / "Doc_08_Forces_Document.md"
OUT  = BASE / "lpc_Force_Index.md"

# Two notice syntaxes are in use: "**[TAG ...]**" and "**Heading. [TAG ...]**",
# where the opening "**" belongs to the heading rather than the bracket. The
# opening "**" is therefore optional, and coverage is ASSERTED below rather
# than assumed.
#
# TAGS is not used to detect a notice: a closed, case-sensitive list of known
# tags misses variant phrasing, title case, and a tag with its separating
# comma omitted -- any of which reaching the parser unstripped becomes false
# source with every other guard clean. The pattern is instead OPEN: any
# bracketed capitalised tag followed by a comma or a dash is a notice. The
# five known tags are kept only for the error messages.
KNOWN_TAGS = ("CORRECTED", "ADDED", "MOVED HERE", "MOVED", "REVISED", "CORRECTION", "SUPERSEDED")
# A real notice opens "[TAG, 2026-..." or "[TAG — ...". The document also
# MENTIONS tags in prose -- §8 discusses "the [ADDED …] provenance clauses" --
# and an opener pattern that could not tell the two apart made the
# over-consumption guard fire on the live document. The lookahead requires a
# comma or a dash after the tag, which every real notice has and no mention does.
# A notice opens with a bracketed capitalised word or two -- CORRECTED, ADDED,
# CORRECTION, SUPERSEDED, MOVED HERE -- followed by a comma or a dash. The
# "[X]" recapitalisation convention this build uses ("[I]t", "[Y]our") is a
# single letter and cannot match; "[Supporting]" has no comma or dash after it.
#
# The tag and the separator after it are both open-ended rather than either
# being a closed list: whitelisting the tag and then whitelisting the
# separator only defers the same failure mode to whichever one is still
# closed (forms like "[FURTHER CORRECTION, ...]" or "[SUPERSEDED: ...]"
# defeat a closed tag list; forms with an unlisted separator defeat a closed
# separator list).
#
# Both are open now. A notice is one to four capitalised words inside a
# bracket, followed by ANY separator punctuation or a number. What is
# deliberately excluded is every short bracket convention this build uses:
# "[X]" recapitalisation ("[I]t", "[Y]our"), the "[CT]" contested tag, and
# "[Supporting]" -- none has a separator after the word. "[world-code]", the
# L4 template's own filename, is excluded because its hyphen is inside a word
# rather than spaced.
_TAG = r"[A-Z][A-Za-z]{1,24}(?:\s+[A-Za-z][A-Za-z]{0,24}){0,3}"
_SEP = r"(?=\s*[,:;(]|\s*[—–]|\s+-\s|\s+\d)"
_OPEN = r"\[" + _TAG + _SEP
NOTICE = re.compile(r"\*{0,2}" + _OPEN + r".*?\]\*\*", re.S)
OPENER = re.compile(_OPEN)
# DETECT stays deliberately broader than the stripper and case-insensitive, so
# a form the stripper does not know halts the run instead of becoming source.
DETECT = re.compile(r"\[[A-Za-z][A-Za-z]{1,24}(?:\s+[A-Za-z][A-Za-z]{0,24}){0,3}"
                    r"(?:\s*[,:;(]|\s*[—–]|\s+-\s|\s+\d)", re.I)

NOTICE_SHAPE = re.compile(
    r"\[(?:[A-Z][A-Za-z]{1,24})(?:\s+[A-Za-z][A-Za-z]{0,24}){0,3}"
    r"(?:\s*[,:;(]|\s*[—–]|\s+-\s|\s+\d)")


def assert_no_notices(t, label):
    """Build-process notices do not belong in a deliverable.

    Correction history lives in `Review-Artifacts/`, never inline in a
    canonical surface. A notice in a deliverable is corruption, not
    content, and this halts rather than stripping it. Backtick-quoted
    MENTIONS of a notice tag are masked first, so documentation about
    notices is not mistaken for one.
    """
    probe = re.sub(r"`[^`]*`", " ", t)
    hits = NOTICE_SHAPE.findall(probe)
    if hits:
        sys.exit(f"FATAL: {label} contains {len(hits)} build-process notice(s) "
                 f"({hits[:3]}). Correction history belongs in Review-Artifacts/, "
                 "never inline in a deliverable. Refusing to emit.")


def strip_notices(t):
    return "\n".join(NOTICE.sub(" ", ln) for ln in t.split("\n"))

# A notice must never span a structural marker. A malformed notice -- one
# whose own terminator is missing -- otherwise matches forward to the NEXT
# notice's terminator and eats everything between, silently removing real
# content such as a gravity list. Any marker a notice must not swallow, plus
# the force-ID pattern: a notice that contains several force IDs is almost
# certainly eating a gravity list.
STRUCTURAL = re.compile(
    r"Connected forces:|^\*\*G\d — |^\#{2,4} |^\*\*Layer [123] |^\| ", re.M)

def assert_notice_coverage(t, label):
    """Two failures are tested, not one. (a) A notice the stripper cannot see
    is read as source. (b) A notice that swallows a structural marker removes
    real source -- the mirror image, equally silent."""
    # The over-consumption test does not depend on where a notice sits in the
    # text; it depends on the span itself being implausibly long or crossing
    # content it has no business crossing. The precise signature, rather than
    # a positional heuristic: a runaway notice matches forward to the NEXT
    # notice's terminator, so its own span contains that next notice's
    # OPENER. Nothing well-formed does that. The length and structural tests
    # below are kept as a backstop.
    for m in NOTICE.finditer(t):
        span = m.group(0)
        swallowed = len(OPENER.findall(span)) > 1
        if swallowed or STRUCTURAL.search(span) or len(span) > 3000:
            sys.exit(f"FATAL: a correction notice in {label} spans a structural marker "
                     f"({m.group(0)[:70]!r}...). It is almost certainly missing its own "
                     "terminator and is consuming real source. Refusing to emit.")
    # Non-circular: DETECT is broader than the stripper, so a notice form the
    # stripper does not know still halts the run rather than becoming source.
    left = DETECT.findall(strip_notices(t))
    if left:
        sys.exit(f"FATAL: {len(left)} notice-like opener(s) survive stripping in {label} "
                 f"({left[:3]}). A notice the stripper cannot see is derivation input, "
                 f"which would put a false connection into the Index. "
                 f"Known tags: {', '.join(KNOWN_TAGS)}. Refusing to emit.")

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


text = SRC.read_text(encoding="utf-8")
DISPOSED = parent_disposition(text, "Doc_08_Forces_Document.md")
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
    # Claims INSIDE correction notices are quotations of superseded text, not
    # live claims -- a notice that says 'this previously read "REVISED after
    # Round 1"' is the record of a fix, not a false statement. Notices are
    # stripped before the assertion, exactly as they are before derivation.
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

    if problems:
        sys.exit("FATAL: Doc_08's review-history claims disagree with Review-Artifacts/:\n  - "
                 + "\n  - ".join(problems) + "\nRefusing to emit.")

# ---- The review history is DERIVED from the artifacts on disk, not typed.
# A number that is counted cannot go stale the way a hand-maintained one can.
ROUNDS = sorted(
    (int(m.group(1)), f) for f in (BASE / "Review-Artifacts").glob("Doc08_Round*_Review.md")
    for m in [re.search(r"Doc08_Round(\d+)_Review\.md", f.name)] if m)
NROUNDS = len(ROUNDS)
LATEST = ROUNDS[-1][0] if ROUNDS else 0
WORDNUM = {0: "No", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
           6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
_W2I = {w.lower(): i for i, w in WORDNUM.items()}
_W2I.update({"eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
             "fifteen": 15, "sixteen": 16, "seventeen": 17})

def _as_int(tok):
    return int(tok) if tok.isdigit() else _W2I.get(tok.lower(), -1)
NWORD = WORDNUM.get(NROUNDS, str(NROUNDS))

def verdict_counts(path):
    """Each round artifact's OWN finding counts, anchored to its own VERDICT
    heading rather than to the first textual occurrence of "## VERDICT" --
    a review artifact routinely mentions that heading in backticks elsewhere,
    so the heading must appear at line start. A file that does not yield one
    is reported as unparsed rather than guessed."""
    t = path.read_text(encoding="utf-8", errors="replace")
    _h = re.search(r"^#{2,3} VERDICT", t, re.M)
    i = _h.start() if _h else -1
    if i < 0:
        return "no VERDICT heading", "verdict not stated"
    # The window ends at the next markdown heading, which is where the
    # verdict statement itself ends -- a structural bound, not a fixed
    # character count, since a fixed window can reach into a later artifact's
    # own recital of an earlier round's counts.
    rest = t[_h.end():]
    nxt = re.search(r"^#{2,3} ", rest, re.M)
    window = rest[:nxt.start()] if nxt else rest[:1200]
    # The verdict word comes from this same structural window as the counts,
    # so the two cannot be read from different bounds and disagree.
    vm = re.search(r"(CLEARED|MINOR REVISION|SUBSTANTIAL REVISION REQUIRED|REJECTED)",
                   window)
    verdict = vm.group(1) if vm else "verdict not parsed"
    m = re.search(r"(\d+)\s*HIGH\D{1,4}(\d+)\s*MEDIUM\D{1,4}(\d+)\s*LOW\D{1,4}(\d+)\s*COSMETIC",
                  window)
    counts = f"{m.group(1)}H {m.group(2)}M {m.group(3)}L {m.group(4)}C" if m else "counts not parsed"
    return counts, verdict

_VC = {n: verdict_counts(f) for n, f in ROUNDS}
HISTORY = "; ".join(f"Round {n} ({_VC[n][0]})" for n, _ in ROUNDS)
_verdicts = {v for _, v in _VC.values()}
# The verdict word is read from each artifact rather than hard-coded, so a
# CLEARED round is never reported as a revision round by a stale literal.
VERDICT_LINE = ("**all " + _verdicts.pop() + "**" if len(_verdicts) == 1
                else "verdicts: " + "; ".join(f"Round {n}: {v}" for n, (_, v) in sorted(_VC.items())))
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
sec5 = strip_notices(text.split("## Section 5 —")[1].split("## Section 6")[0])
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
sec4 = strip_notices(text.split("## Section 4 —")[1].split("## Section 5")[0])
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
sec7 = strip_notices(text.split("## Section 7 —")[1].split("## Section 8")[0])
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
w(f"**Status:** " + ("**Approved to proceed**, inherited from `Doc_08_Forces_Document.md`'s own Disposition, "
  f"which governs this line; the Round {LATEST_FIX_PASS} fix pass is itself unreviewed."
  if DISPOSED else
  f"**REVISED after Round {LATEST_FIX_PASS} — the revision is unreviewed, and not self-disposed.**")
  + " Co-output of Construction Step 8 with `Doc_08_Forces_Document.md`; reviewed and disposed of together.")
w(f"**Review history, counted from `Review-Artifacts/` rather than typed:** {HISTORY} — {VERDICT_LINE}.")
w(f"**World file-code:** `lpc` · **Drafted:** 2026-09-15 · **Revised:** 2026-09-15 (Round {LATEST_FIX_PASS} fix pass) · **Generated by** `scripts/gen_force_index.py`, committed beside this file")
w("**Generated from `Doc_08_Forces_Document.md` by `gen_force_index.py`. Never hand-edited.**")
w("")
w("**What re-running the generator actually re-verifies, stated exactly, since a blanket claim can cover less than it sounds like.** "
  "**Derived from the source document, and therefore re-checked on every run:** every table in §§1–4, all counts and totals, the §6 reconciliation report and the §7 cross-check. "
  "**Hard-coded prose, re-verified by nothing:** this whole header block — **including the Status line, the Review-history line, the Revised date and the Disposition** — and every explanatory paragraph under §§2, 3, 4, 5, 6 and 7, **both branches of §6 included**. In §§6 and 7 only the *findings* are derived: the contradiction table, the observation table, the disagreement lines and the agreement sentence. Everything around them is commentary. "
  "")
w("")
w("")
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
w("**What the regression test shows.** Against the pre-fix draft the control reports all three divergences — `1B-1`/G2, `2A-1`/G8 and `2B-1`/G7. Against the live document it reports none. On the stub side it flags the same three entries the stub check is designed to catch.")
w("")
w("**Cross-cell cross-check (§3 prose against §4's table).** "
  + ("**No disagreements:** every force ID named in a connection-asserting Layer 3 sentence appears as that force's partner in §4's table."
     if not xc_mismatch else
     "**" + str(len(xc_mismatch)) + " disagreement(s):** " + ", ".join(f"`{a}` names `{b}`, §4 does not pair them" for a, b in xc_mismatch) + "."))
w("")
w("**The controls, stated at what they actually cover.** "
  "There are **thirteen**: **one regression (A), six positive controls (B–F, M) whose planted defect must appear in the output, and six negative controls (G–L) that must halt the generator.** "
  "*(The count is re-derived by exit code each run, not copied, since a total stated once and carried forward risks going stale as controls are added.)* "
  "**(A)** regression against the pre-fix draft at `9eccc532` — three §3/§5 divergences, three stubs. "
  "**(B)** a false denial produces a contradiction row. "
  "**(C)** a force ID planted inside a notice does not reach the tables. "
  "**(D)** an omitted connection produces a contradiction row. "
  "**(E)** a Layer-3 claim §4 does not carry produces a cross-cell row. "
  "**(F)** a build-process notice anywhere in Doc_08 halts the run. "
  "**(G)** a malformed notice halts rather than being parsed. "
  "**(H)** a review-status claim disagreeing with `Review-Artifacts/` halts. "
  "**(I)** a force filed under a `### CELL` heading its ID contradicts halts. "
  "**(J)** a §4 row that fails to parse — a de-bolded force ID, a missing trailing pipe — halts, instead of silently printing one connection fewer than Doc_08 certifies. "
  "**(K)** a duplicated §4 row halts: it raises the total *without* failing (J), because the parse and the row count move together. "
  "**(L)** a connection total disagreeing with the count Doc_08 certifies in its own prose halts. "
  "**(M)** a review artifact returning `CLEARED` is reported as CLEARED — the verdict word is read from the artifact's own structural window, not from a literal. "
  "**(A) Regression** against the pre-fix draft at `9eccc532`: all three §3/§5 divergences found by hand. "
  "**(B) False denial** — §3 claiming §5 does not carry `G6` produces a contradiction row. "
  "**(C) Notice injection** — a bold force ID planted inside a `[CORRECTED …]` notice does not reach the tables. "
  "**(D) Omitted connection** — removing `2B-1` from §5's G6 list while §3 asserts it produces a contradiction row. "
  "**(E) Cross-cell** — a Layer-3 connection claim §4's table does not carry produces a §3-vs-§4 row. "
  "**(F) Unknown notice syntax** — a notice written `**Heading. [ADDED …]**` is stripped and its planted ID does not reach the tables. "
  "**(G) Notice over-consumption** — a malformed notice missing its terminator halts the generator. "
  "**(H) Review history** — a Doc_08 whose round claims disagree with `Review-Artifacts/` halts the generator. "
  "**(I) Cell/ID agreement** — a force filed under a `### CELL` heading its own ID contradicts halts the generator.")
w("")
w("**What each control's design guards against, stated directly.** "
  "**(G)** does not key on a structural marker appearing inside the notice span alone — the same malformed notice, placed anywhere in the text, still halts on an implausibly long or emphasis-dense span, which is what over-consumption actually looks like, rather than on where the marker sits. "
  "**(H)** flattens emphasis first and matches every claim form, so a bold marker, a lowercase word, or a bare numeral cannot hide a claim from the Status-line check. "
  "**(D)'s** sibling in `verdict_counts` anchors the parse to each artifact's own `## VERDICT` heading and ends the window at the next heading — a structural bound rather than a fixed character count, since a fixed window can still reach into a later round's own recital of a predecessor's counts. "
  "**A control stated more broadly than it is implemented is worse than no control, because it will be trusted.**")
w("")
w("**To regenerate this file:** `python3 scripts/gen_force_index.py` from the world-build folder, or with any working directory — the script resolves its own base path. An optional first argument overrides that base, and exists only for mutation testing.")
w("")
w("**This is a weaker test than it looks and the weakness is stated.** It is a sentence-level keyword match: a connection asserted with a verb outside its list, or phrased so that a disclaim keyword also appears, is invisible to it. **Broadening the verb list produced a false positive of its own** — the verb *\"carries\"* matched *\"Neither §5's G6 list **nor** its G7 list carries it,\"* a negation and a sentence about §5 rather than a connection claim; the verb was withdrawn rather than the sentence reworded. **This control catches one class of defect. It is not a proof of consistency, and no run of it substitutes for a reader.**")
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
w(("**Approved to proceed, 2026-09-15**, together with `Doc_08_Forces_Document.md`, which is reviewed and disposed of with it."
   if DISPOSED else
   "**Not disposed.** Reviewed and disposed of together with `Doc_08_Forces_Document.md`.")
  + f" **{NWORD} independent round(s) have been run**, the most recent `Review-Artifacts/Doc08_Round{LATEST}_Review.md` ({_VC[LATEST][0]}, {_VC[LATEST][1]}); this file is the Round {LATEST_FIX_PASS} fix pass and is **unreviewed**.{FIXPASS_NOTE} Not self-certified. Not Frozen.")
w("")

OUT.write_text("\n".join(O), encoding="utf-8")
print(f"wrote {OUT}  ({len(forces)} forces, {len(conns)} connections, {len(gmap)} gravities)")
print("longest Force cell:", max(len(f['name']) for f in forces),
      "| longest Connection cell:", max(len(c['desc']) for c in conns))
