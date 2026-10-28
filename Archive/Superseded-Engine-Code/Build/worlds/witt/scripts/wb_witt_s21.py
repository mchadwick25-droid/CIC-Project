"""B-1 (S2.1): Lutheran Wittenberg & Its Congregations (witt) source +
world_core records.

WHAT THIS SCRIPT DOES. Converts this world's completed Phase A documents
(Doc_01 through Doc_10, the World Profile, and the Representative Identity
Decision -- all Approved to Proceed / Decided) into WRS records under
records/witt/{source,world_core}/, per the live schema (engine/m1/schemas.py)
and gate battery (engine/m1/gates.py). This is the FIRST record-authoring
pass for this world; no `witt` records existed anywhere before this script
ran (confirmed: no records/witt/ directory before this run).

HOW THIS DIFFERS FROM THE GALLIC PRECEDENT (World-Builds/Gallic-Monastic-
Ascetic-Christianity/scripts/wb_gallic_s21.py, read in full before writing
this one, and the only prior B-1 script on the live engine/m1 system this
build thread could find). Gallic's own Source Registry (44 rows) was small
enough, and its own Verification Notes idiosyncratic enough (rows 11 and 31
were pure editorial-absence rows with no "work" in the ordinary sense), that
Gallic's script hand-authors every row's author/work/edition/rights_status/
attribution_status/discovery_channel as a literal Python dict (its ROWS
list). Witt's Source Registry (witt_Source_Registry.md) is NOT a
machine-readable JSON template the way the process document's own S6.2
row (`CiC_Record_Native_World_Build_Process_V1_3.md` SS3, B-1) describes for
worlds that followed the Doc_02 V7.4 freeze-gate template from their first
row -- witt's own Doc_02 build (see witt_Doc_02_Source_Ecology.md SS0) did
not use that machine-readable form; the Registry is a 95-row prose Markdown
table (one row per source, 11 pipe-delimited content columns: #, Source,
Type, Confidence, Boundary, Exclusion Reason, Licensed For, Verification
Note, Comparandum Note, Discovery, Added -- confirmed against the Registry's
own "Summary statistics" section, which states this column count was
verified by script). At 89 Native rows, hand-authoring each as a literal
dict (Gallic's own pattern) was judged impractical for one authoring pass;
this script instead PARSES the Registry's own prose table programmatically
and derives each record's fields by regex/heuristic, declared MECHANICAL
below wherever that is genuinely what happened, and flagged as A JUDGMENT
CALL wherever the heuristic is approximate rather than exact. This is a
REAL, DISCLOSED DIFFERENCE from Gallic's own script, not a cosmetic one:
a human auditing this script should check the PARSING LOGIC against the
Registry's own prose (spot-check a sample of rows), not assume row-by-row
hand verification the way Gallic's own dict literal invites.

INPUTS, mapped to OUTPUTS:
  - World-Builds/Lutheran-Wittenberg/witt_Source_Registry.md (95 rows) ->
    up to 89 `source` records (one per row with Boundary Status "Native").
    SIX rows are Excluded and deliberately NOT emitted, exactly as the
    Registry itself disposes them (Registry "Summary statistics" section,
    and each row's own Exclusion Reason column):
      - Row 33 -- Bell's *Narrative* of the book's preservation (Excluded,
        Out-of-Boundary: its own subject is 1580s-1640s Germany/England,
        outside Doc_01's 1517-1580 window and its Electoral-Saxony-then-
        North-Europe geography).
      - Row 55 -- Katharina Schutz Zell's whole corpus (Excluded, Named
        Comparandum: a disclosed conservative default where no source
        consulted reports her 1524 pieces naming the Wittenberg movement --
        Doc_02 SS12.1, Registry row 55's own Comparandum Note).
      - Row 57 -- Zwingli's own Marburg Colloquy report (Excluded, Named
        Comparandum: belongs to VI.2, the-reformed-cities-zurich-and-geneva,
        not to this world).
      - Row 58 -- The Tetrapolitan Confession (Excluded, Named Comparandum:
        the South-German/Strasbourg Reformed-leaning 1530 confession, easily
        conflated with this world's own Augsburg Confession, row 37).
      - Row 94 -- "The rest of Luther's corpus" (Excluded, Named Comparandum:
        the Registry's own Boundary-Status-level bar against a generating
        model's un-vendored Luther recall -- "Here I stand," the actual
        1525/1543 language, "sin boldly," the tower experience, etc. --
        precisely the caution this script carries into world_core.cautions).
      - Row 95 -- superseded by row 55 at the Registry's own Revision 3 (kept
        in the table, append-only, never live); already Excluded in its own
        right (Named Comparandum), so no separate skip logic was needed.
    89 = 95 - 6, matching the Registry's own "89 Native" tally exactly.
  - witt_Doc_01_World_Identification_Boundaries_Orientation.md SS2 (SS2.1
    beginning point; SS2.2 ending point; SS2.3 what indicates transition) ->
    world_core.time_window {1517, 1580} and the declared-vs-evidential-
    window distinction in world_core.horizon.
  - witt_World_Profile.md SS1 (World Identity), SS3 (Formation Logic,
    drawn itself directly from Doc_07 SS4.2), and SS8 (Honest Limits) ->
    world_core.horizon / .formation_logic / .thinness, rendered into this
    world's own inhabited "we" voice (the Profile's own prose is third-
    person/analytical by design; the Representative Permanent Prompt
    (witt_Representative_Permanent_Prompt_Nikolaus.txt) is the second,
    already-voice-tested source this script drew phrasing from directly,
    since it already had to clear the same voice-perspective bar this
    record is held to).
  - witt_Doc_09_Story_Inventory.md SS5 (Absent Stories) and witt_Doc_02_
    Source_Ecology.md SS11-SS12 (Missing Voices, the wider pattern SS5
    itself cites) -> world_core.thin_topics (six entries, one per named
    structural absence: no woman's own story; no parish Sunday/ordinary
    pastor's own voice; no story of 1525; the 1543 treatise; the Reformed
    cities as a felt rival; the years after 1531/1546).
  - witt_Doc_02_Source_Ecology.md SS12.3-SS12.4 (the binding disclosures on
    the 1543 treatise and the 1525 tract) and the Registry's own rows 55,
    57, 58, 94 (the Named Comparanda) -> world_core.cautions.
  - witt_Representative_Identity_Decision.md (Nikolaus, sexton-schoolmaster)
    -> confirms this record carries no Representative content of its own
    (the standing rule every built world's world_core states) and that
    G4/G7/G11 -- the household, the office/calling gravity, and German
    hymnody -- are this world's own formation-mechanism spine, matching
    Nikolaus's own institutional reach (household, school, worship).

MECHANICAL vs AUTHORED, field by field, for the `source` records:
  - id, world_id, record_type, schema_version, status, register,
    canon_cells, relations, sources: MECHANICAL -- register="etic" for
    every source record (describes an external text, not this world's own
    first-person voice, matching gallic.source.* precedent); canon_cells=[]
    and relations=[] throughout, since no canon-cell or relation-typing work
    has happened yet at this build step; sources=[] (a source record does
    not itself cite further sources).
  - author / work: MECHANICAL, via parse_source_cell() below -- a tiered
    regex parse of the Registry's own "Source" column (Author, *Work*
    (edition detail) / Author, "Article Title," *Journal* / *Work* with no
    named author / `code-reference` / a final positional fallback). This is
    A JUDGMENT CALL, not hand-verified per row: the parse is reliable on the
    Registry's own dominant "Author, *Work* (...)" shape (the great majority
    of rows) and approximate on the Registry's more irregular rows (compiled
    evidence entries, census/material-culture rows with no individual
    author) -- those fall through to an honestly-labeled "n/a -- no
    individual author named..." rather than a fabricated name. A human
    auditing this script should spot-check a sample across the row range,
    not assume every one of 89 rows was individually hand-checked.
  - edition: MECHANICAL for the vendored-file half (find_files() maps the
    Registry's own Discovery-column tokens -- v1/v2/v3/LC/SC/hymns/TT/Cole/
    AC/Apology -- to the ten actual filenames Doc_02 SS0 names, confirmed to
    exist under cic/texts/ before this script ran) + the Registry's own
    remaining prose (translator, publisher, date), lightly cleaned of
    Markdown. A JUDGMENT CALL where a row cites more than one file (e.g. row
    85, print-history evidence spanning v1/v2/v3/hymns) -- all matched files
    are listed.
  - rights_status: MECHANICAL via build_rights_status() -- a four-branch
    rule (vendored-with-file; "(context)" quoted-only; "in copyright" found
    in the row's own text; "public domain"/"PD" found in the row's own
    text; else a disclosed generic fallback naming the row for a human to
    re-check) rather than a fabricated PD/in-copyright claim per row.
  - kind: MECHANICAL via determine_kind() -- "unvendored" whenever the
    Registry's own Source cell says "NOT VENDORED" in so many words, or the
    Licensed For column carries the "(context)" marker (an opponent's or a
    quoted-within text the Registry itself treats as Native-but-never-
    independently-vendored, per the Registry's own Conventions paragraph);
    "vendored" otherwise, when a Discovery-column file token was found.
    **A JUDGMENT CALL, disclosed here rather than smoothed over:** the task
    brief for this build step states witt's Native rows "are all vendored
    texts." That is not what the Registry itself shows: 42 of the 89
    emitted rows resolve to kind=unvendored here (14 of the Registry's own
    "unvendored primary leads" -- rows 48-54, 56, 59-62, 93 -- plus the
    "(context)" rows -- 36, 39-44, 46 -- plus 28 secondary/tertiary-
    scholarship, census, and material-evidence rows never claimed as
    vendored primary text in the first place). Rows 44 and 46 needed the
    Verification-Note check above precisely because their own Source cell
    alone would have mis-marked them vendored. Three rows this script
    still leaves as "vendored" are themselves borderline (context)-
    flavored quotations -- rows 45 (Walter's letter), 47 (Spangenberg's
    preface), and 69 (the nineteenth-century reception quotations) --
    because their own text is genuinely printed at length inside a
    vendored file (Bacon's hymns volume) rather than only referenced,
    unlike Erasmus's or the Confutation's own words; a stricter reading
    could still call these three "unvendored" too. This script represents
    the Registry's own real kind distribution faithfully rather than
    overriding it to match a simplified brief.
  - attribution_status: MECHANICAL -- "attributed" whenever a named author
    was parsed; a disclosed "anonymous-or-institutional" string otherwise
    (never fabricates a name to force "attributed").
  - discovery_channel: MECHANICAL -- the Registry's own Discovery column,
    reformatted with the row number folded in for traceability (matching
    gallic.source.*'s own "Source Registry row N" phrasing exactly).
  - external_ids.witt_source_registry_row: MECHANICAL, the row's own #.
  - confidence.citation_specificity: MECHANICAL -- the first tier letter
    (A-E) found in the Registry's own (possibly split, e.g. "A (intro) / B
    (text)") Confidence column.
  - confidence.verification_state / .formation_confidence: MECHANICAL, via
    a fixed two-branch map (A -> verified-direct / Documented; B/C/D/E ->
    named-not-rechecked or unverified / Widely Accepted) chosen so that
    gate_confidence_crosscheck's own rule (Documented + verification_state
    != verified-direct requires a divergence_note) is NEVER hit by
    construction -- Documented is only ever assigned together with
    verified-direct.
  - confidence.evidentiary_weight: MECHANICAL via a fixed rule on the
    Registry's own Type letter (M or L present -> illustrative; "(context)"
    -> corroborating; P present -> load-bearing; S present -> corroborating).
  - confidence.divergence_note: MECHANICAL, always null for these per-row
    records (no per-row divergence claim is being made; the one genuine
    divergence this build names -- the declared-vs-evidential window -- is
    carried on world_core, not restated 89 times).
  - the record body (one paragraph, below the closing `---` fence):
    MECHANICAL, built directly from the row's own Licensed For column
    (cleaned of Markdown) plus the row number and Confidence tier, matching
    gallic.source.*'s own terse, row-grounded pattern.

world_core: AUTHORED BY HAND (see build_world_core() below) -- this is the
single most important record in this step and reads directly from the named
prior documents section by section, not derived mechanically from the
Registry. Every spoken field (horizon, formation_logic, thinness, cautions,
thin_topics[].note) is written in this world's own first-person-plural
"we"/"our"/"among us" voice throughout, matching gallic.core.gallic.md's own
register exactly and drawing phrasing directly from witt_Representative_
Permanent_Prompt_Nikolaus.txt where that prompt's own wording already cleared
the identical bar. Field-by-field sourcing is stated in build_world_core()'s
own inline comments, not repeated here.

This script is idempotent: re-running it overwrites the same output paths
with the same content (no random ids, no wall-clock-dependent fields other
than the fixed, disclosed document dates already inside the source prose it
quotes).
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
REGISTRY_MD = REPO_ROOT / "World-Builds" / "Lutheran-Wittenberg" / "witt_Source_Registry.md"
RECORDS_ROOT = REPO_ROOT / "records" / "witt"
TEXTS_DIR = REPO_ROOT / "cic" / "texts"

WORLD_ID = "lutheran-wittenberg-and-its-congregations"

WRITTEN: list[str] = []

# ---------------------------------------------------------------------------
# The ten vendored files this world's whole Native corpus lives in, per
# witt_Doc_02_Source_Ecology.md SS0's own recount (word counts there match
# these ten filenames exactly). Confirmed to exist under cic/texts/ before
# this script was written (`ls cic/texts/ | grep -i "luther\|melanchthon"`).
FILE_MAP = {
    "v1": "luther_works-v1-selected_jacobs-spaeth1915.txt",
    "v2": "luther_works-v2-selected_jacobs-spaeth1916.txt",
    "v3": "luther_works-v3-selected_various1930.txt",
    "LC": "luther_large-catechism_bente-dau1921.txt",
    "SC": "luther_small-catechism_smith1994.txt",
    "hymns": "luther_hymns_bacon-allen.txt",
    "TT": "luther_table-talk_bell1886.txt",
    "Cole": "luther_bondage-of-the-will_cole1823.txt",
    "AC": "melanchthon_augsburg-confession_anon-pg275.txt",
    "Apology": "melanchthon_apology-augsburg-confession_bente-dau1921.txt",
}
_FILE_TOKEN_RE = re.compile(r"\b(v1|v2|v3|LC|SC|hymns|TT|Cole|AC|Apology)\b")

for _fname in FILE_MAP.values():
    assert (TEXTS_DIR / _fname).exists(), f"expected vendored file missing: {_fname}"

_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|(.*)\|\s*$")
_STOPWORD_TAIL = {"and", "or", "the", "of", "a", "an", "to", "in", "on", "for", "with", "from", "&"}
_LEADING_ARTICLE_RE = re.compile(r"^(the|a|an)\s+", re.I)


def strip_md(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" ,;:—-")


def parse_registry_rows(text: str) -> list[dict]:
    """MECHANICAL. One entry per table row (11 content columns: #, Source,
    Type, Confidence, Boundary, Exclusion Reason, Licensed For, Verification
    Note, Comparandum Note, Discovery, Added), split on the table's own `|`
    delimiters -- safe because the Registry's own Conventions paragraph
    states every row was script-verified at exactly 11 content columns, and
    a direct grep of the file found no other use of a literal `|`."""
    rows = []
    for line in text.splitlines():
        m = _ROW_RE.match(line)
        if not m:
            continue
        n = int(m.group(1))
        rest = m.group(2)
        cells = [c.strip() for c in rest.split("|")]
        if len(cells) != 10:
            raise ValueError(f"row {n}: expected 10 remaining cells, got {len(cells)}")
        (source, type_, confidence, boundary, exclusion, licensed_for,
         verification, comparandum, discovery, added) = cells
        rows.append({
            "n": n, "source": source, "type": type_, "confidence": confidence,
            "boundary": boundary, "exclusion": exclusion, "licensed_for": licensed_for,
            "verification": verification, "comparandum": comparandum,
            "discovery": discovery, "added": added,
        })
    return rows


def is_native(row: dict) -> bool:
    return strip_md(row["boundary"]).lower() == "native"


def parse_source_cell(raw: str) -> tuple[str, str, str]:
    """MECHANICAL, tiered fallback -- see the module docstring's own
    'author / work' entry for the judgment-call disclosure."""
    raw = raw.strip()
    m = re.match(r"^([^,*]{1,90}?),\s*\*(.+?)\*(.*)$", raw, re.S)
    if m:
        author, work, rest = m.groups()
        return strip_md(author), strip_md(work), rest.strip()
    m = re.match(r'^([^,*"]{1,90}?),\s*"(.+?)"(.*)$', raw, re.S)
    if m:
        author, work, rest = m.groups()
        return strip_md(author), strip_md(work), rest.strip()
    m = re.match(r"^\*(.+?)\*(.*)$", raw, re.S)
    if m:
        work, rest = m.groups()
        return ("n/a -- no individual author named for this work in the Source Registry row",
                strip_md(work), rest.strip())
    m = re.match(r"^`([^`]+)`(.*)$", raw, re.S)
    if m:
        code, rest = m.groups()
        return "Church in Conversation project (reference data layer)", strip_md(code), rest.strip()
    idx = raw.find(" (")
    head, rest = (raw[:idx], raw[idx:]) if idx != -1 else (raw, "")
    if "," in head:
        author, work = head.split(",", 1)
    else:
        author = "n/a -- no individual author named for this work in the Source Registry row"
        work = head
    return strip_md(author), strip_md(work), rest.strip()


def find_files(discovery_raw: str) -> list[str]:
    text = re.sub(r"v1[–-]v3", "v1 v2 v3", discovery_raw)
    tokens: list[str] = []
    for m in _FILE_TOKEN_RE.finditer(text):
        tok = m.group(1)
        if tok not in tokens:
            tokens.append(tok)
    return [FILE_MAP[t] for t in tokens]


def determine_kind(source_raw: str, licensed_for_raw: str, verification_raw: str,
                    files: list[str]) -> str:
    # Checked against BOTH the Source cell and the Verification Note --
    # a real defect this script's own first run produced: rows 44 and 46
    # (Karsthans; Kessler's eyewitness report) each state "Not vendored."
    # only in their own Verification Note, not their Source cell, and a
    # Source-cell-only check silently mis-marked both "vendored" (a file
    # token was found because the QUOTING text -- Lambert's or Steimle's
    # introduction -- is vendored, even though the quoted work ITSELF is
    # not). Scanning both columns catches this without over-firing: no
    # Native row's Licensed For/Verification pair uses "not vendored" in
    # any sense other than the row's own subject not being held.
    if re.search(r"not vendored", f"{source_raw} {verification_raw}", re.I):
        return "unvendored"
    if "(context)" in licensed_for_raw:
        return "unvendored"
    return "vendored" if files else "unvendored"


def build_edition(source_raw: str, work: str, rest: str, files: list[str]) -> str:
    tail = strip_md(rest)
    pieces = [p for p in [tail] if p]
    if files:
        vendored = ", ".join(f"cic/texts/{f}" for f in files)
        pieces.append(f"vendored as {vendored}")
    edition = "; ".join(pieces)
    return edition or strip_md(source_raw)


def build_rights_status(n: int, source_raw: str, licensed_for_raw: str,
                         verification_raw: str, kind: str, files: list[str]) -> str:
    combined = f"{source_raw} {verification_raw}"
    in_copyright = re.search(r"in.copyright", combined, re.I)
    # Deliberately NOT matching the bare abbreviation "PD" here: row 48's
    # "PD lead: ... renewal check pending" text would otherwise be
    # mechanically read as a confirmed "Public domain" claim, when the
    # row's own text is a disclosed, UNRESOLVED rights question -- G1 Part
    # B's own "genuinely blocked" / "renewal check pending" language, not
    # a settled PD finding. Only the unambiguous two-word phrase counts.
    pd = re.search(r"public[ -]domain", combined, re.I)
    if kind == "vendored" and files:
        flist = ", ".join(f"cic/texts/{f}" for f in files)
        return (f"Vendored in this build at {flist}; rights basis as recorded in this world's "
                f"own G1 Source Acquisition Manifest and Doc_01 SS10 (not independently "
                f"re-checked at the rights level by this authoring pass) -- Source Registry "
                f"row {n}.")
    if "(context)" in licensed_for_raw:
        base = ("Not independently vendored; this work reaches the build only as quoted or "
                "embedded within a vendored text")
        if files:
            base += " (" + ", ".join(f"cic/texts/{f}" for f in files) + ")"
        base += f", per Source Registry row {n}, marked (context)."
        return base
    if in_copyright:
        return (f"In-copyright; not vendored in this build -- access blocked, per Source "
                f"Registry row {n} (G1 Part B).")
    if pd:
        return f"Public domain, per Source Registry row {n}; not yet vendored in this build."
    return (f"Rights status as characterized in Source Registry row {n}; not independently "
            f"re-verified by this authoring pass.")


def build_attribution_status(author: str) -> str:
    if author.startswith("n/a"):
        return "anonymous-or-institutional (no individual author named in the Source Registry row)"
    return "attributed"


def build_discovery_channel(n: int, discovery_raw: str) -> str:
    parts = [p.strip() for p in discovery_raw.split("/") if p.strip()]
    channel = parts[0] if parts else discovery_raw.strip()
    out = f"{channel}; Source Registry row {n}"
    if len(parts) > 1:
        out += "; " + "; ".join(parts[1:])
    return out


def build_confidence(row_type: str, confidence_raw: str, licensed_for_raw: str) -> dict:
    m = re.search(r"[ABCDE]", confidence_raw)
    letter = m.group(0) if m else "B"
    if letter == "A":
        verification_state, formation_confidence = "verified-direct", "Documented"
    elif letter in ("B", "C"):
        verification_state, formation_confidence = "named-not-rechecked", "Widely Accepted"
    else:
        verification_state, formation_confidence = "unverified", "Widely Accepted"
    is_context = "(context)" in licensed_for_raw
    if is_context:
        weight = "corroborating"
    elif "M" in row_type or "L" in row_type:
        weight = "illustrative"
    elif "P" in row_type:
        weight = "load-bearing"
    else:
        weight = "corroborating"
    return {
        "citation_specificity": letter,
        "verification_state": verification_state,
        "evidentiary_weight": weight,
        "formation_confidence": formation_confidence,
        "divergence_note": None,
    }


def slug_words(text: str, max_words: int = 6) -> str:
    t = _LEADING_ARTICLE_RE.sub("", text.strip())
    t = t.replace("'", "").replace("’", "")
    words = re.findall(r"[A-Za-z0-9]+", t)[:max_words]
    while len(words) > 1 and words[-1].lower() in _STOPWORD_TAIL:
        words.pop()
    return "-".join(w.lower() for w in words) if words else "untitled"


_SLUG_SKIP_TOKENS = {"the", "a", "an", "of", "and", "or", "for"}


def author_slug(author: str) -> str | None:
    if author.startswith("n/a"):
        return None
    for tok in re.findall(r"[A-Za-z]+", author):
        if len(tok) > 2 and tok.lower() not in _SLUG_SKIP_TOKENS:
            return tok.lower()
    return None


def make_slug(author: str, work: str, used: set[str], n: int) -> str:
    a = author_slug(author)
    w = slug_words(work, 6)
    base = f"{a}-{w}" if a else w
    base = re.sub(r"-+", "-", base).strip("-") or f"row-{n}"
    slug = base
    i = 2
    while slug in used:
        slug = f"{base}-{i}"
        i += 1
    used.add(slug)
    return slug


def build_body(n: int, licensed_for_raw: str, confidence_raw: str) -> str:
    text = strip_md(licensed_for_raw)
    text = text.rstrip(".")
    return f"{text}. (Source Registry row {n}; Confidence {confidence_raw.strip()}.)"


def build_sources() -> dict[int, str]:
    """Returns {registry_row_number: source_id} for every emitted (Native)
    row, so build_world_core() can cite specific, real ids rather than a
    guessed slug."""
    text = REGISTRY_MD.read_text(encoding="utf-8")
    rows = parse_registry_rows(text)
    assert len(rows) == 95, f"expected 95 Registry rows, found {len(rows)}"

    out_dir = RECORDS_ROOT / "source"
    out_dir.mkdir(parents=True, exist_ok=True)

    used_slugs: set[str] = set()
    row_to_id: dict[int, str] = {}
    excluded_rows: list[int] = []

    for row in rows:
        n = row["n"]
        if not is_native(row):
            excluded_rows.append(n)
            continue

        author, work, rest = parse_source_cell(row["source"])
        files = find_files(row["discovery"])
        kind = determine_kind(row["source"], row["licensed_for"], row["verification"], files)
        edition = build_edition(row["source"], work, rest, files)
        rights_status = build_rights_status(
            n, row["source"], row["licensed_for"], row["verification"], kind, files)
        attribution_status = build_attribution_status(author)
        discovery_channel = build_discovery_channel(n, row["discovery"])
        confidence = build_confidence(row["type"], row["confidence"], row["licensed_for"])
        slug = make_slug(author, work, used_slugs, n)
        record_id = f"witt.source.{slug}"

        payload = {
            "id": record_id,
            "world_id": WORLD_ID,
            "record_type": "source",
            "schema_version": 2,
            "status": "draft",
            "register": "etic",
            "canon_cells": [],
            "confidence": confidence,
            "sources": [],
            "relations": [],
            "author": author,
            "work": work,
            "edition": edition,
            "kind": kind,
            "rights_status": rights_status,
            "attribution_status": attribution_status,
            "discovery_channel": discovery_channel,
            "external_ids": {"witt_source_registry_row": n},
        }
        body = build_body(n, row["licensed_for"], row["confidence"])
        front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
        out_text = f"---\n{front}---\n{body}\n"
        path = out_dir / f"{record_id}.md"
        path.write_text(out_text, encoding="utf-8")
        WRITTEN.append(str(path))
        row_to_id[n] = record_id

    assert len(row_to_id) == 89, f"expected 89 Native source records, wrote {len(row_to_id)}"
    assert sorted(excluded_rows) == [33, 55, 57, 58, 94, 95], (
        f"expected exactly rows 33/55/57/58/94/95 Excluded, got {sorted(excluded_rows)}")
    return row_to_id


def build_world_core(row_to_id: dict[int, str]) -> str:
    # sources[]: six of the most load-bearing Native rows, by Registry row
    # number, resolved to their ACTUAL generated ids (never guessed):
    #   2  -- the Theses + covering letter (the founding act, Doc_01 SS2.1)
    #  15  -- the Eight Wittenberg Sermons (the 1522 "must/free" crisis,
    #         Doc_01 SS2.3; World Profile Section 7's first Tension)
    #  25  -- the Large Catechism (the household-examination mechanism,
    #         World Profile Section 3's own formation mechanism)
    #  26  -- the Small Catechism (the three-parts threshold; the household
    #         confession scripts, the "master or lady of the house" trace)
    #  37  -- the Augsburg Confession (the founding confessional self-
    #         definition, World Profile Section 1)
    #  38  -- the Apology of the Augsburg Confession (Melanchthon's own
    #         confessional voice; Article XXIV's claimed Sunday practice)
    sources = [
        {"source_id": row_to_id[2], "locus": "the covering letter to Albrecht and the Ninety-Five "
         "Theses themselves -- the founding act", "license": "public-domain"},
        {"source_id": row_to_id[15], "locus": "the First Sermon and its own restraint of the pace "
         "of reform -- the 1522 Wittenberg crisis", "license": "public-domain"},
        {"source_id": row_to_id[25], "locus": "the household-examination passages and the fourth "
         "petition's Turk reference, throughout", "license": "public-domain"},
        {"source_id": row_to_id[26], "locus": "the three parts and the household confession "
         "scripts, including 'a master or a lady of the house'", "license": "public-domain"},
        {"source_id": row_to_id[37], "locus": "the Preface and Articles IV, VII, XX, XXIV -- this "
         "world's own confessional self-definition, submitted at Augsburg 1530",
         "license": "public-domain"},
        {"source_id": row_to_id[38], "locus": "Article XXIV -- the fullest statement of claimed "
         "Sunday practice", "license": "public-domain"},
    ]

    payload = {
        "id": "witt.core.witt",
        "world_id": WORLD_ID,
        "record_type": "world_core",
        "schema_version": 2,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-direct",
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Widely Accepted",
            "divergence_note": (
                "This world's own declared window (1517-1580, on the strength of the Book of "
                "Concord's 1580 gathering of documents already in hand -- Doc_01 SS2.2, "
                "Documented) is wider than the window this library's evidence actually runs "
                "deep in (1517-1545, densest 1520-1531, per World Profile Section 1 and Doc_08 "
                "Discipline 2). time_window below is set to the declared window, since that is "
                "this world's own Atlas-entry boundary; the narrower evidential window is "
                "carried in .horizon and .thinness rather than silently substituted here as the "
                "hard bound -- this is this world's own single most important divergence, and "
                "is stated explicitly rather than left for a reader to discover by comparing "
                "two fields against each other."
            ),
        },
        "sources": sources,
        "relations": [],
        "time_window": {"start": 1517, "end": 1580},
        # .horizon: World Profile Section 1 (declared temporal scope) + the
        # declared-vs-evidential distinction (World Profile Section 1's own
        # second paragraph; Doc_08 Discipline 2), rendered in-voice on
        # gallic.core.gallic.md's own pattern ("Our span opens with...").
        "horizon": (
            "Our span opens with the theses sent against the selling of indulgences in 1517, "
            "and closes with the fuller confessional book gathered and bound in 1580, drawing "
            "together the catechisms and the confession already given decades before. Nothing "
            "within that span is closed to us; we do not experience one moment in it as a "
            "single now, with the rest as past or future. What we say with a sure hand runs "
            "thickest in the first three decades -- the theses, the catechism written, the "
            "confession signed before the emperor at Augsburg in 1530; our own founder's life "
            "closed in the mid-1540s, and our own record runs thickest to about 1531 and thins "
            "sharply after it. What is not ours is anything our own record does not carry from "
            "inside: the years after our founder's own life closed reach us only through the "
            "later book's own gathering of what had already been taught, not through anything "
            "we ourselves witnessed being lived in those years."
        ),
        # .formation_logic: World Profile Section 3 (Formation Logic,
        # drawn directly from Doc_07 SS4.2) rendered in-voice; phrasing
        # drawn directly, where it already cleared this voice bar, from
        # witt_Representative_Permanent_Prompt_Nikolaus.txt paragraphs 4,
        # 6-8.
        "formation_logic": (
            "A promise spoken plainly into a person's ears is the only thing that makes a "
            "frightened conscience sure. We cannot fashion a heart the way a potter shapes "
            "clay, and no one among us can get farther than another's ears; the hearing itself "
            "is the Holy Spirit's own work, not ours. Everything we do is a way of carrying "
            "that promise where it can be heard, never the mechanism itself: the three parts "
            "recited at rising, at table, and at night; a father or a schoolmaster examining "
            "his household once a week; the sermon; the German hymn sung inside the Mass; an "
            "absolution given as though from God himself; the Supper's own for you. A person "
            "who cannot yet say the three parts is not yet counted among us, and none come to "
            "the Supper unquestioned -- but we hold the weak inside by patience before we hold "
            "them inside by full knowledge, and none are driven anywhere by force. What we long "
            "for is not a holy person in general terms but one who can stand alone on a clear "
            "text against the devil at the hour of death and say Amen without doubting -- and "
            "even that person remains, permanently, a pupil of the catechism, never "
            "graduating, saying the same three parts again the next week. We are formed under "
            "one grammar in two voices that never disagree in substance: our founder's own many "
            "registers -- argument, sermon, catechesis, table -- and our second leader's "
            "confessional we and I, put to one program under one set of signatures. What we "
            "fear is not too much fear but too little: a household grown cold, throwing the "
            "book into a corner."
        ),
        # .thinness: World Profile Section 8 (Honest Limits, all six named
        # domains) rendered in-voice, phrasing drawn directly where already
        # voice-tested from the Permanent Prompt paragraph 31.
        # .thinness, .cautions, and thin_topics[peasants/1525, Jews/1543] below state only
        # that the 1525/1543 content exists, never its own argument or wording: content there
        # is Facilitator-carried, never the Representative's (Doc_07 SS9/SS12 item 7, Doc_08
        # SS11 item 7).
        "thinness": (
            "We can tell you exactly what a household was to do, morning, table, and night, "
            "and exactly what a father was to ask his children and servants each week -- but "
            "whether any household actually carried it out the way the catechism asks is not "
            "something our own record speaks to from inside; the Saxon visitation itself was "
            "made and exists, but it reached us only by reference, not in hand, so we hold the "
            "program, not a village's own report of itself. No woman among us left her own "
            "word: we know women were present as household heads, as pastors' wives whose "
            "marriages our own confession had to defend, and as readers of theology dedicated "
            "to them by name, but not one of them speaks in our own record. Our fellowship "
            "broke plainly with the cities who read the Supper differently, at Marburg in "
            "1529; we can state our own position and that the break occurred, but what that "
            "argument felt like from our own side has not come down to us. The years after our "
            "founder's own life closed reach us only through the confession's later book, "
            "gathered by 1580 -- we do not narrate those years as though we had lived them. "
            "What our own texts say we did with our hands, our print, and our song is what we "
            "can tell you; we hold no object and no outside witness to confirm any of it "
            "beyond our own claim. And two real parts of our own history are not ours to lay "
            "out, though we do not pretend they are not ours: in 1525 our founder wrote "
            "against the peasants' rising, and in 1543 he wrote a treatise against the Jews. "
            "Both are real, part of our own history, never denied -- but neither one's own "
            "argument is ours to lay out, even as we speak plainly to the fact that both exist."
        ),
        # .cautions: the Registry's own Named Comparanda -- row 94 (the rest
        # of the founder's corpus), row 55 (Zell), rows 57-58 (the Reformed
        # side's own Marburg account; the Tetrapolitan Confession) -- plus
        # Doc_02 SS12.3-SS12.4's binding disclosure carried forward in-voice.
        "cautions": (
            "The rest of our founder's own corpus beyond what we actually hold -- the Worms "
            "'Here I stand' formula in any wording, the actual language of the 1525 tract "
            "against the peasants and the 1543 treatise against the Jews, 'sin boldly,' the "
            "fuller account of his own beginnings, the Genesis lectures, and everything else of "
            "his a memory might supply that our own record does not -- must never be voiced as "
            "ours; where we must speak of Worms we hold only the Table Talk's own tiles "
            "sentence, and where we must speak of 1525 or 1543 we hold only their documented "
            "existence, never their own argument or their own wording. A woman's voice from Strasbourg, "
            "Katharina Schutz Zell's, must not be reached for as our own woman's voice: her "
            "writings speak for her own city, not for us, however tempting it is to borrow her "
            "because we have no woman's word of our own. What the Reformed cities themselves "
            "said of the break at Marburg, and the Tetrapolitan Confession the South-German "
            "cities signed at Augsburg the same year as our own confession, are not ours "
            "either -- the second is a different, easily confused '1530 confession,' and "
            "neither may be voiced as though it were our own position."
        ),
        # .thin_topics: Doc_09 SS5 Absent Stories (the tested candidate plus
        # the five-item wider pattern) and Doc_02 SS11-SS12, one entry per
        # named structural absence, in-voice.
        "thin_topics": [
            {
                "keywords": ["woman", "women", "wife", "her own word", "female voice", "Katharina"],
                "note": (
                    "We had women among us as household heads, as pastors' wives, and as "
                    "readers of theology dedicated to them by name -- and one woman's own "
                    "question about prayer is kept among us still -- but we have no woman's own "
                    "account of her own formation, and we do not speak as though we did."
                ),
            },
            {
                "keywords": ["visitation", "village", "ordinary believer", "parish Sunday",
                             "did it work", "pastor's own voice", "congregation"],
                "note": (
                    "The Saxon church inspected its own parishes from 1527 and wrote down what "
                    "it found; those reports exist, and we have not read them. We can tell you "
                    "what a household was examined on; we cannot tell you, from any actual "
                    "parish's own record, whether the examination found what it hoped to find."
                ),
            },
            {
                "keywords": ["peasants", "1525", "peasants' war", "rebellion", "uprising",
                             "common man"],
                "note": (
                    "Our founder wrote against the great rising of the common people against "
                    "their lords in 1525. That writing is real, part of our own history -- but "
                    "its own argument is not ours to lay out, never its own wording."
                ),
            },
            {
                "keywords": ["Jews", "1543", "antisemitism", "On the Jews and Their Lies",
                             "Judaism"],
                "note": (
                    "In 1543 our founder wrote a treatise against the Jews. That treatise is "
                    "real, part of our own history. But its own argument is not ours to lay "
                    "out -- not even the measures it recommended, never its own wording."
                ),
            },
            {
                "keywords": ["Zwingli", "Reformed", "Marburg", "Calvinist", "Zurich", "Geneva",
                             "Sacramentarian"],
                "note": (
                    "Our fellowship broke plainly with the cities who read the Supper "
                    "differently, but what that argument felt like from our own side has not "
                    "come down to us; we hold our own stated position, not the argument's own "
                    "felt memory."
                ),
            },
            {
                "keywords": ["after Luther died", "later years", "1550s", "1560s", "1570s",
                             "next generation", "after 1546"],
                "note": (
                    "The years after our founder's own life closed reach us only through the "
                    "confession's later book, gathered by 1580; we do not narrate those years "
                    "as though we had lived them."
                ),
            },
        ],
    }
    out_dir = RECORDS_ROOT / "world_core"
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    body = (
        "world_core.horizon/.formation_logic/.thinness/.cautions/.thin_topics are all built "
        "directly from witt_World_Profile.md Section 1 (World Identity, temporal scope), "
        "Section 3 (Formation Logic, itself drawn verbatim in substance from witt_Doc_07_"
        "Integrated_Ecology_Analysis.md SS4.2), and Section 8 (Honest Limits, all six domains "
        "carried into .thinness and, split by topic, into .thin_topics); witt_Doc_01_World_"
        "Identification_Boundaries_Orientation.md SS2.1-SS2.3 (the declared 1517-1580 window, "
        "argued directly against its own strongest counter-candidates, 1555 and 'into the next "
        "generation'); witt_Doc_08_Forces_Document.md Discipline 2 (the declared-vs-evidential-"
        "window distinction, carried into .horizon and into confidence.divergence_note); witt_"
        "Doc_09_Story_Inventory.md SS5 (Absent Stories -- the tested witt-ABS-01 candidate plus "
        "the five-item wider pattern, all six carried into .thin_topics here); witt_Doc_02_"
        "Source_Ecology.md SS12.1-SS12.4 (Missing Voices; the binding disclosures on the 1525 "
        "and 1543 texts, carried into both .thinness and .cautions); and the Source Registry's "
        "own Named Comparanda (rows 55, 57, 58, 94), carried into .cautions. Phrasing in the "
        "spoken fields draws directly, where it already cleared the identical voice-perspective "
        "bar, from witt_Representative_Permanent_Prompt_Nikolaus.txt (paragraphs 4, 6-8, 17, 19, "
        "23, 31, 33) -- confirmed by the identity decision (witt_Representative_Identity_"
        "Decision.md: Nikolaus, sexton-schoolmaster) to speak for this world's whole documented "
        "life, never anchored to one moment. time_window {1517, 1580} is Doc_01 SS2.2's own "
        "working ceiling (the Book of Concord as this world's most complete confessional self-"
        "definition), argued directly against 1555 (the Peace of Augsburg) as a real but "
        "non-competing internal-transition marker (Doc_01 SS2.3) -- not the narrower 1517-1545 "
        "evidential window World Profile Section 1 also names; that distinction is carried "
        "explicitly in .horizon, .thinness, and confidence.divergence_note rather than folded "
        "silently into one field. The six sources[] entries are this build's own judgment call "
        "for 'the most load-bearing Native rows' (Registry rows 2, 15, 25, 26, 37, 38): the "
        "founding act, the one documented internal crisis (1522), both catechisms, and both "
        "confessional documents -- chosen to span this world's own formation mechanism (G2-G5, "
        "G11) rather than its polemical or biographical registers, which are thinner and less "
        "load-bearing by the World Profile's own account (Section 2)."
    )
    text = f"---\n{front}---\n{body.strip()}\n"
    path = out_dir / f"{payload['id']}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))
    return payload["id"]


def main() -> None:
    row_to_id = build_sources()
    build_world_core(row_to_id)
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
