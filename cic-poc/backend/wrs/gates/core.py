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
