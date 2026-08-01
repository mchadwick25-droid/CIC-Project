"""S1.3 machine gates (Pass 1 SS4.2), run against record sets.

Requirements source (S6.1, adopted 2026-07-27): the governing standard
is Ministry/Technology/CiC_World_Build_Completion_Standard_V1.0.md.

Each gate takes a record set (dict id -> record) plus gate-specific inputs
and returns a list of violation strings - empty list = green. The runner
(run_gates.py) executes them and writes the committed report; its
--selftest mode runs every gate against the committed clean and
seeded-defect fixtures (fixtures.py) and is the S1.3 checkpoint.

Gate-integrity rule (blueprint SS0 rule 4) is IN FORCE from this commit
forward: changes to this package are their own steps with their own review;
a session that needs a gate changed to pass files a flag and stops.
"""
import re

# ---------------------------------------------------------------- relations

RELATION_FIELDS = ("relations", "field_relations", "interaction", "connections")

# SS3.0: every relation is directional and reciprocity-checked. Encoding
# (documented, refinable only via Change Order):
#   - INVERSE pairs must be mirrored with the paired type.
#   - SYMMETRIC types must be mirrored with the same type.
#   - All other types require a back-edge of any type (linkage reciprocity) -
#     Pass 1 names no inverse vocabulary for them, and inventing one would
#     be silent redesign (see S1.5 review, same rule for force connections).
INVERSE = {"presupposes": "presupposed-by", "presupposed-by": "presupposes"}
SYMMETRIC = {"tension-with", "reinforcing", "competing",
             "associated-with"}  # associated-with: CO-P2-13 (same
             # symmetric-mirror code path the tension-with seed exercises)


def _edges(record):
    for field in RELATION_FIELDS:
        for edge in record.get(field) or []:
            yield field, edge


def gate_referential_integrity(records: dict) -> list:
    """Every id-reference resolves to a record in the set."""
    out = []
    ref_fields = {
        "owner_figure_id": None, "speaker_or_author": None, "translation_used": None,
        "snowball_parent": None, "story_ids": list, "gravities": list,
        "contested_claim_ids": list,
    }
    for rid, r in records.items():
        for field, kind in ref_fields.items():
            v = r.get(field)
            if v is None:
                continue
            targets = v if kind is list else [v]
            for t in targets:
                if t not in records:
                    out.append(f"{rid}: {field} -> {t} does not resolve")
        for field, edge in _edges(r):
            t = edge.get("target_id")
            if t and t not in records:
                out.append(f"{rid}: {field} -> {t} does not resolve")
        for link in r.get("sources") or []:
            sid = link.get("source_id")
            if sid and sid not in records:
                out.append(f"{rid}: sources[] -> {sid} does not resolve")
        # CO-P2-04: story-to-gravity links (gate STRENGTHENED - a new
        # reference class checked; no existing check weakened)
        for link in r.get("gravity_links") or []:
            gid = link.get("gravity_id")
            if gid and gid not in records:
                out.append(f"{rid}: gravity_links[] -> {gid} does not resolve")
    return out


def gate_reciprocity(records: dict) -> list:
    """Every directional edge has its reciprocal (typed where a pair or
    symmetric type is defined; linkage-level otherwise)."""
    out = []
    for rid, r in records.items():
        for field, edge in _edges(r):
            t, typ = edge.get("target_id"), edge.get("type")
            target = records.get(t)
            if target is None:
                continue  # referential gate's finding, not this one's
            back = [e for _f, e in _edges(target) if e.get("target_id") == rid]
            if typ in INVERSE:
                if not any(e.get("type") == INVERSE[typ] for e in back):
                    out.append(f"{rid} -[{typ}]-> {t}: no {INVERSE[typ]} edge back")
            elif typ in SYMMETRIC:
                if not any(e.get("type") == typ for e in back):
                    out.append(f"{rid} -[{typ}]-> {t}: symmetric type not mirrored")
            else:
                if not back:
                    out.append(f"{rid} -[{typ}]-> {t}: no back-edge (linkage reciprocity)")
    return out


# ---------------------------------------------------------- field completion

# SS11-A requiredness, encoded per record type. 'backfill' profile per the
# SS3.1 backfill rule (existing rows: only the four backfillable fields
# required; discovery_instrument/date never required - inventing them is the
# fabricated-precision failure). Term requiredness varies by retrieval.tier.
PROFILES = {
    "default": {
        "world_core": ["time_window", "horizon", "formation_logic", "gravities"],
        "source": ["attribution_status", "level_of_description", "language",
                    "discovery_channel", "boundary_status", "licensed_for"],
        "term@tier12": ["period_sense", "prior_sense", "modern_sense",
                         "conceptual_distance_note", "quick_meaning", "voice_surface",
                         "semantic_domain", "field_relations", "retrieval", "sources"],
        "term@tier3plus": ["quick_meaning", "sources"],
        "story": ["narrative_tier", "owner_figure_id", "attested_occasion",
                   "tellable_as", "sources"],
        "quote": ["locus", "translation_used", "license"],
        "gravity": ["six_tests", "classification"],
        "force": ["six_cell_position", "layer_historical_event",
                   "layer_worlds_own_experience", "layer_formation_impact", "layer4"],
        "figure": ["names", "narratable"],
        "contested_claim": ["claim", "held_against", "concedes",
                             "pressure_response", "divergence_partners"],
        "voice_profile": ["speaking_model", "trait_rubric",
                           "register_determination", "native_measure"],
        "demonstration": ["dialogue", "trait_scores", "situation_tag"],
        "modern_term": ["term", "display_terms", "origin_year", "modern_sense",
                         "underlying_subject", "distinguishing_claim"],
        "search_record": ["sampling_strategy", "types_sought", "years_searched",
                           "languages_searched", "inclusion_exclusions",
                           "terms_tried", "instruments"],
    },
    "backfill": {
        # SS3.1 backfill rule verbatim: schema_version 1 rows require only
        # these; never discovery_instrument / discovery_date.
        "source": ["attribution_status", "level_of_description", "language",
                    "discovery_channel"],
    },
}


def _present(record, field):
    v = record.get(field)
    if v is None:
        return False
    if isinstance(v, (list, dict, str)) and not v:
        return False
    return True


def gate_field_completion(records: dict, profile: str = "default") -> list:
    out = []
    prof = PROFILES[profile]
    for rid, r in records.items():
        rt = r.get("record_type")
        key = rt
        if rt == "term" and profile == "default":
            tier = (r.get("retrieval") or {}).get("tier", 1)
            key = "term@tier12" if tier in (1, 2) else "term@tier3plus"
        required = prof.get(key)
        if required is None:
            continue  # profile doesn't constrain this type (e.g. backfill)
        for f in required:
            if not _present(r, f):
                out.append(f"{rid} ({rt}, {profile}): required field missing/empty: {f}")
        if rt == "gravity" and _present(r, "six_tests") and len(r["six_tests"]) < 6:
            out.append(f"{rid}: six_tests carries {len(r['six_tests'])}/6 verdicts")
    return out


# ------------------------------------------------------------- narratability

def gate_figure_narratability(records: dict, voice_material: str) -> list:
    """Figures referenced in voice materials where narratable=false and no
    allusion-licensed story exists (the grief-list defect, as a query)."""
    out = []
    vm = voice_material.lower()
    for rid, r in records.items():
        if r.get("record_type") != "figure" or r.get("narratable") is not False:
            continue
        # CO-P2-07 (Mark, 2026-07-27): a figure carrying an
        # accepted_refusal_note is a DOCUMENTED decision that refusal is
        # the design (the live-tested guard) - quiet by decision recorded
        # on the record itself, not by suppression
        if r.get("accepted_refusal_note"):
            continue
        names = [n.get("name", "") for n in r.get("names") or []]
        mentioned = [n for n in names if n and n.lower() in vm]
        if not mentioned:
            continue
        has_allusion = any(
            records.get(s, {}).get("tellable_as") == "allusion-only"
            for s in r.get("story_ids") or []
        )
        if not has_allusion:
            out.append(
                f"{rid}: '{mentioned[0]}' appears in voice material, narratable=false, "
                f"and no allusion-licensed story exists"
            )
    return out


# ---------------------------------------------------------------- readability

def readability_check(text: str, fk_max: float = 10.0, fre_min: float = 60.0) -> dict:
    """The SS5.6 machine check: FK grade <= 10 and FRE >= 60 (band floor 8 is
    reported, not failed - too-simple is not the risk the floor guards).
    Values from wrs/parameters.yaml reading_floor (RCF V3.2 Part Five)."""
    import textstat
    fk = textstat.flesch_kincaid_grade(text)
    fre = textstat.flesch_reading_ease(text)
    violations = []
    if fk > fk_max:
        violations.append(f"FK grade {fk:.1f} > {fk_max}")
    if fre < fre_min:
        violations.append(f"FRE {fre:.1f} < {fre_min}")
    return {"fk_grade": round(fk, 2), "fre": round(fre, 2), "violations": violations}


def gate_readability(texts: dict, fk_max: float = 10.0, fre_min: float = 60.0) -> list:
    out = []
    for name, text in texts.items():
        res = readability_check(text, fk_max, fre_min)
        for v in res["violations"]:
            out.append(f"{name}: {v}")
    return out


# ------------------------------------------------------- quote recording

def gate_quote_fidelity_recording(records: dict) -> list:
    """The gate verifies a verification was RECORDED with its edition - the
    verification itself is human work the gate demands, not performs
    (blueprint S1.3)."""
    out = []
    for rid, r in records.items():
        if r.get("record_type") != "quote":
            continue
        conf = r.get("confidence") or {}
        state = conf.get("verification_state")
        if state not in ("verified-direct", "verified-via-authority"):
            out.append(f"{rid}: quote verification not recorded (verification_state={state})")
        elif not conf.get("verification_date"):
            out.append(f"{rid}: quote verified but verification_date missing")
        if not r.get("translation_used"):
            out.append(f"{rid}: quote lacks translation_used (the edition the verification ran against)")
    return out


# ------------------------------------------------------------ sentinel guard

def gate_no_sentinel_conditions(records: dict) -> list:
    """The em-dash historical defect, as a gate over record sets (the
    validator also rejects it per-file; the gate makes it a batch report)."""
    out = []
    sent = {"—", "–", "-"}
    for rid, r in records.items():
        ret = r.get("retrieval") or {}
        for c in ret.get("retrieve_when") or []:
            if c.strip() in sent:
                out.append(f"{rid}: retrieve_when carries an em-dash sentinel")
        for c in ret.get("do_not_retrieve_when") or []:
            text = c.get("text", "") if isinstance(c, dict) else str(c)
            if text.strip() in sent:
                out.append(f"{rid}: do_not_retrieve_when carries an em-dash sentinel")
    return out


# ------------------------------------------------------- alias safety (VG-1b)

# Rule A blocklist: small, curated, VERSIONED (changes ride the
# gate-integrity rule, like SYMMETRIC/INVERSE above). High-frequency
# general-register English words that are unsafe as bare aliases even
# when the bundled frequency table misses them (period-adjacent religious
# register the general-English table under-ranks).
ALIAS_GENERIC_BLOCKLIST_V1 = {
    "word", "son", "father", "spirit", "light", "life", "love", "truth",
    "way", "world", "death", "prayer", "teacher", "reading", "letter",
    "church", "faith", "grace", "glory", "peace", "hope", "fear", "heart",
    "soul", "mind", "body", "name", "bread", "water", "wine", "city",
    "king", "lord", "god", "christ", "cross", "law", "sin", "gift",
    "covenant", "vow", "communion", "gospel", "desert", "cell", "elder",
}

_ALIAS_FREQ_PATH = None  # resolved lazily so the module imports without I/O
_ALIAS_FREQ_TABLE = None
_DETERMINER_RE = re.compile(r"^(?:the|a|an)\s+", re.I)
_NOTE_PREFIX = "note:"


def _alias_freq_table() -> set:
    """The bundled offline top-N general-English frequency table
    (english_top5000_v1.txt beside this module) - flat file, no network,
    no model, the parroting.py/content_coverage.py offline discipline."""
    global _ALIAS_FREQ_TABLE
    if _ALIAS_FREQ_TABLE is None:
        from pathlib import Path
        path = Path(__file__).with_name("english_top5000_v1.txt")
        _ALIAS_FREQ_TABLE = {
            line.strip().lower() for line in
            path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")}
    return _ALIAS_FREQ_TABLE


def _postparse_alias_keys(record) -> list:
    """The post-parse alias key space for one term record - the SAME
    semantics app/rag/indexer.py's parse_aliases() (as fixed at VG-1a)
    applies to the deployed chunk this record generates: a
    parenthetically-qualified alias contributes NO key (dropped whole,
    never reduced to its bare head); surrounding quotes are shed;
    keys are lowercased. Render parity keeps record aliases textually
    equal to the chunk front matter, so this reproduces the runtime
    key space from record data without importing the indexer."""
    keys = []
    for a in record.get("aliases") or []:
        # quoted glosses first (the runtime extracts them BEFORE the
        # parenthetical check, so a quoted gloss inside a qualified item
        # still contributes its key)
        for phrase in re.findall(r'"([^"]*)"', a):
            cleaned = phrase.strip(" ,")
            if len(cleaned) > 1:
                keys.append(cleaned.lower())
        remainder = re.sub(r'"[^"]*"', "", a)
        for chunk in re.split(r"[;,/]", remainder):
            if "(" in chunk or ")" in chunk:
                continue
            cleaned = chunk.strip(" /").strip()
            if len(cleaned) > 1:
                keys.append(cleaned.lower())
    return keys


def _term_name_key(record) -> str:
    """The frontend's own term-name normalization (LexiconHighlight.tsx):
    strip parentheticals, take the pre-'/' segment, lowercase."""
    name = record.get("term") or ""
    name = re.sub(r"\([^)]*\)", "", name).split("/")[0].strip()
    return name.lower()


def gate_alias_safety(records: dict, voice_material: str = "") -> list:
    """VG-1b (Voice-Governance Addendum SS5.3-5.4, SS5.6, SS5.8).

    Rule A (generic alias): an alias whose determiner-stripped form is a
    single token on the curated blocklist or inside the bundled top-5000
    general-English frequency table is unsafe as a bare highlight key.
    Rule B (collision): within ONE world (the scope useLexicon.ts's
    termMapsByWorld actually renders from), {term-name key} ∪ post-parse
    alias keys must be unique across term records - two of the nine real
    collisions were a term's own canonical name vs another term's alias,
    so aliases-only checking misses the bug class.
    Rule C (gloss/alias cross-namespace) is DEFERRED to VG-1c - it needs
    the confirmed-gloss term_id field that does not exist yet.

    Override (SS5.6, the CO-P2-06/07 documented-exception precedent):
    a term-level `alias_generic_override_note` naming the deliberately
    generic alias(es) suppresses Rule A for that term's aliases and is
    REPORTED as a non-counting 'note:' line, never silently absorbed;
    an override on a term with no Rule-A hit is itself a violation
    (stale overrides don't get to accumulate).

    Operates on the post-parse key space (never the raw authored string):
    a raw-string gate would have reported zero violations on the exact
    record that caused the production bug.
    """
    out = []
    freq = _alias_freq_table()
    by_world = {}
    for rid, r in records.items():
        if r.get("record_type") == "term":
            by_world.setdefault(r.get("world_id", "?"), []).append(r)

    for world, terms in sorted(by_world.items()):
        # ---- Rule A
        for r in sorted(terms, key=lambda x: x["id"]):
            hits = []
            for key in _postparse_alias_keys(r):
                stripped = _DETERMINER_RE.sub("", key).strip()
                if " " in stripped:
                    continue  # multi-token after determiner-strip: Rule
                              # B's territory, not a generic-word case
                if stripped in ALIAS_GENERIC_BLOCKLIST_V1 or stripped in freq:
                    hits.append(key)
            note = r.get("alias_generic_override_note")
            if hits and note:
                out.append(f"{_NOTE_PREFIX} {r['id']}: generic alias(es) "
                           f"{hits} covered by alias_generic_override_note "
                           f"({note[:80]!r}) - documented exception, "
                           f"reported not suppressed")
            elif hits:
                out.append(f"{r['id']}: Rule A - generic alias(es) {hits} "
                           f"(determiner-stripped form on the blocklist/"
                           f"top-5000 table) and no "
                           f"alias_generic_override_note")
            elif note:
                out.append(f"{r['id']}: STALE alias_generic_override_note "
                           f"(no alias currently trips Rule A) - remove or "
                           f"re-justify")
        # ---- Rule B
        claims = {}
        for r in terms:
            keys = set(_postparse_alias_keys(r))
            tkey = _term_name_key(r)
            if tkey:
                keys.add(tkey)
            for k in keys:
                claims.setdefault(k, []).append(r["id"])
        for k in sorted(claims):
            owners = sorted(set(claims[k]))
            if len(owners) > 1:
                out.append(f"{world}: Rule B - key {k!r} claimed by "
                           f"{', '.join(owners)} (one world map, one "
                           f"winner: whichever indexes last silently "
                           f"steals the key)")
        # ---- Rule C (VG-1c / Voice-Governance Addendum SS5.5, landed at
        # the S6.2 tail 2026-08-01, after the SS4.3 data move): the
        # gloss/alias cross-namespace check. For each confirmed-gloss
        # entry in this world CARRYING term_id, the gloss's own
        # original-term key must not collide with a DIFFERENT term's
        # key space (term-name or post-parse alias): a participant
        # saying the glossed word would be alias-matched to the wrong
        # term. Entries without term_id are SKIPPED and counted as a
        # note (pending the term_id backfill) - never silent, never a
        # violation, per the S3.1 backfill rule.
        glosses = _confirmed_glosses_for(world)
        pending = 0
        for ge in glosses:
            tid = ge.get("term_id")
            if not tid:
                pending += 1
                continue
            gkey = _DETERMINER_RE.sub("", ge["original"].lower()).strip()
            for k, owners in claims.items():
                if k == gkey and any(o != tid for o in owners):
                    others = sorted(o for o in set(owners) if o != tid)
                    out.append(
                        f"{world}: Rule C - gloss original "
                        f"{ge['original']!r} (term_id {tid}) collides "
                        f"with {', '.join(others)}'s own key space")
        if pending:
            out.append(f"{_NOTE_PREFIX} {world}: Rule C - {pending} "
                       f"gloss entr{'y' if pending == 1 else 'ies'} "
                       f"without term_id skipped (the no-term-home "
                       f"circumlocution class, or pending backfill; "
                       f"reported not suppressed)")
    return out


def _confirmed_glosses_for(world_id: str) -> list:
    """The SS4.3 keyed list, world-filtered - loaded lazily and cached;
    fail-open to [] so a missing file never breaks the alias gate's
    A/B rules (Rule C simply has nothing to check)."""
    global _GLOSS_CACHE
    if _GLOSS_CACHE is None:
        try:
            import yaml
            from pathlib import Path
            path = (Path(__file__).resolve().parents[1] / "glosses"
                    / "confirmed_glosses.yaml")
            _GLOSS_CACHE = yaml.safe_load(
                path.read_text(encoding="utf-8"))["glosses"]
        except Exception:
            _GLOSS_CACHE = []
    return [g for g in _GLOSS_CACHE if g.get("world_id") == world_id]


_GLOSS_CACHE = None


def split_alias_reports(entries: list) -> tuple:
    """(violations, notes) - 'note:'-prefixed entries are documented-
    exception reports (SS5.6), printed but never counted as violations."""
    notes = [e for e in entries if e.startswith(_NOTE_PREFIX)]
    return [e for e in entries if not e.startswith(_NOTE_PREFIX)], notes
