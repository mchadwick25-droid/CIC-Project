"""S1.3 gate fixtures: per gate, one clean set that must PASS and at least
two seeded-defect sets that must FAIL - including reconstructions of the
historical defects Pass 1 names (a non-reciprocal edge reported as mutual;
a figure referenced with narratable=false; an em-dash condition).

A gate that never fails checks nothing (Pass 1 SS10's health rule, applied
to the checkpoint layer before anything depends on it - SS1 mechanism 5).
"""


def _fig(rid, name, narratable, story_ids=()):
    return {"id": rid, "world_id": "fixture-world", "record_type": "figure",
            "schema_version": 1, "names": [{"name": name, "name_kind": "in-world"}],
            "narratable": narratable, "story_ids": list(story_ids)}


def _story(rid, owner, tellable="scene"):
    return {"id": rid, "world_id": "fixture-world", "record_type": "story",
            "schema_version": 1, "title": f"story {rid}",
            "narrative_tier": {"tier": 2, "justification": "fixture"},
            "text": "The story text.", "owner_figure_id": owner,
            "attested_occasion": "the attested occasion", "tellable_as": tellable,
            "sources": [{"source_id": "fixsrc001"}]}


def _term(rid, tier=1, **over):
    base = {"id": rid, "world_id": "fixture-world", "record_type": "term",
            "schema_version": 1, "term": rid,
            "period_sense": "p", "prior_sense": "none-attested", "modern_sense": "m",
            "conceptual_distance_note": "c", "quick_meaning": "q", "voice_surface": "v",
            "semantic_domain": "d",
            "field_relations": [],
            "retrieval": {"tier": tier, "retrieve_when": ["asked about it"],
                           "do_not_retrieve_when": [], "force_llm_vote": False},
            "sources": [{"source_id": "fixsrc001"}]}
    base.update(over)
    return base


def _src(rid="fixsrc001"):
    return {"id": rid, "world_id": "fixture-world", "record_type": "source",
            "schema_version": 1, "attribution_status": "genuine",
            "level_of_description": "work", "language": "syc",
            "discovery_channel": "field-bibliography",
            "discovery_instrument": "fixture reference-work sweep",
            "boundary_status": "Native", "licensed_for": "voice"}


def _quote(rid, state="verified-direct", date="2026-07-26", translation="fixsrc001"):
    q = {"id": rid, "world_id": "fixture-world", "record_type": "quote",
         "schema_version": 1, "locus": "Dem 6.1", "license": "verbatim",
         "confidence": {"verification_state": state}}
    if date:
        q["confidence"]["verification_date"] = date
    if translation:
        q["translation_used"] = translation
    return q


def clean_set():
    a = _term("fixlexA", field_relations=[{"type": "presupposes", "target_id": "fixlexB"}])
    b = _term("fixlexB", field_relations=[{"type": "presupposed-by", "target_id": "fixlexA"}])
    g1 = {"id": "fixgravA", "world_id": "fixture-world", "record_type": "gravity",
          "schema_version": 1,
          "six_tests": {n: {"verdict": "pass"} for n in ("repetition", "dependency", "formation", "explanatory", "persistence", "interaction")},
          "classification": "Primary",
          "interaction": [{"type": "reinforcing", "target_id": "fixgravB"}]}
    g2 = {**g1, "id": "fixgravB",
          "interaction": [{"type": "reinforcing", "target_id": "fixgravA"}]}
    fig_ok = _fig("fixfigA", "Abba Fixture", True, ["fixstoryA"])
    fig_guarded = _fig("fixfigB", "Mar Silent", False, ["fixstoryB"])
    story = _story("fixstoryA", "fixfigA")
    allusion = _story("fixstoryB", "fixfigB", tellable="allusion-only")
    return {r["id"]: r for r in
            [a, b, g1, g2, fig_ok, fig_guarded, story, allusion, _src(),
             _quote("fixqA")]}


CLEAN_VOICE_MATERIAL = (
    "You may speak of Abba Fixture and his teaching. Mar Silent is named in "
    "grief only; his one story is licensed for allusion, never narration."
)

READABLE_TEXT = (
    "The meal is the center of what we do. We gather in a house at evening. "
    "Someone reads a letter aloud. We share bread and give thanks. The "
    "youngest asks a question and an elder answers it. No one leaves hungry. "
    "When a traveler comes with news, we hear it after the prayers."
)

# Marius-reconstruction: one ~75-word sentence, average far past grade 10
# (the Imperial-Juridical Step10 boundary-testing FAIL, per F5).
UNREADABLE_LONG = (
    "The determination of orthodoxy, being inseparable from the "
    "adjudicative structures through which conciliar authority was "
    "promulgated and enforced across provincial jurisdictions whose "
    "episcopal incumbents maintained divergent interpretations of the "
    "relationship between imperial sponsorship and ecclesial autonomy, "
    "necessitated a jurisprudential apparatus whose complexity, "
    "notwithstanding the ostensible simplicity of the creedal formulations "
    "themselves, rendered the participation of the unlettered faithful in "
    "doctrinal deliberation a practical impossibility rather than a "
    "juridical prohibition."
)

UNREADABLE_JARGON = (
    "Ecclesiological legitimation presupposes institutional "
    "differentiation. Sacramental efficacy necessitates ministerial "
    "authorization. Doctrinal promulgation requires conciliar "
    "ratification. Jurisdictional demarcation follows metropolitan "
    "organization."
)

CHUNK_BODY = (
    "The covenant is a lifelong vow. Its members remain in the town among "
    "their kin. The vow is entered by men and women alike. The fast and the "
    "vigil mark its discipline."
)

COVERAGE_CLEAN = {
    "chunk": CHUNK_BODY,
    "fields": {
        "period_sense": "The covenant is a lifelong vow. Its members remain in the town among their kin.",
        "world_meaning": "The vow is entered by men and women alike. The fast and the vigil mark its discipline.",
    },
    "drops": [],
}
COVERAGE_LOST = {
    "chunk": CHUNK_BODY,
    "fields": {
        "period_sense": "The covenant is a lifelong vow. Its members remain in the town among their kin.",
        "world_meaning": "The fast and the vigil mark its discipline.",
    },
    "drops": [],  # 'entered by men and women alike' silently lost
}
COVERAGE_DUP = {
    "chunk": CHUNK_BODY,
    "fields": {
        "period_sense": "The covenant is a lifelong vow. Its members remain in the town among their kin. The vow is entered by men and women alike.",
        "world_meaning": "The vow is entered by men and women alike. The fast and the vigil mark its discipline.",
    },
    "drops": [],  # one sentence lands in two fields
}

PARROT_SOURCE = READABLE_TEXT
PARROT_RECITED = ("The meal is the center of what we do. We gather in a house "
                  "at evening. Someone reads a letter aloud.")
PARROT_PARAPHRASE = ("Our common supper anchors the whole gathering: letters "
                     "are read to everyone, bread is broken with thanksgiving, "
                     "and questions pass from young to old.")


def seeded_sets():
    """Per gate: named seeded-defect record sets (each must FAIL its gate)."""
    s = {}

    # referential integrity
    r1 = clean_set(); r1["fixstoryA"] = dict(r1["fixstoryA"], owner_figure_id="fixfig-GONE")
    r2 = clean_set(); r2["fixlexA"] = dict(r2["fixlexA"],
        field_relations=[{"type": "presupposes", "target_id": "fixlex-GONE"}])
    s["referential"] = [("dangling owner_figure_id", r1), ("dangling relation target", r2)]

    # reciprocity - incl. the historical 'reported as mutual' shape
    q1 = clean_set(); q1["fixlexB"] = dict(q1["fixlexB"], field_relations=[])
    q2 = clean_set(); q2["fixgravB"] = dict(q2["fixgravB"], interaction=[])
    s["reciprocity"] = [("presupposes edge with no presupposed-by back (reported as mutual)", q1),
                        ("symmetric reinforcing not mirrored", q2)]

    # field completion
    c1 = clean_set(); c1["fixlexA"] = dict(c1["fixlexA"]); c1["fixlexA"].pop("voice_surface")
    c2 = clean_set(); c2["fixstoryA"] = dict(c2["fixstoryA"]); c2["fixstoryA"].pop("attested_occasion")
    s["completion"] = [("tier-1 term missing voice_surface", c1),
                       ("story missing attested_occasion (Amma-Sarah class)", c2)]

    # narratability - the grief-list reconstruction
    n1 = clean_set(); n1["fixfigB"] = dict(n1["fixfigB"], story_ids=[])
    n2 = clean_set(); n2["fixstoryB"] = dict(n2["fixstoryB"], tellable_as="scene")
    s["narratability"] = [("narratable=false figure in voice text, no story at all", n1),
                          ("narratable=false figure whose only story is scene-licensed, not allusion", n2)]

    # quote recording
    k1 = clean_set(); k1["fixqA"] = _quote("fixqA", state="unverified")
    k2 = clean_set(); k2["fixqA"] = _quote("fixqA", date=None)
    k3 = clean_set(); k3["fixqA"] = _quote("fixqA", translation=None)
    s["quote_recording"] = [("verification never recorded", k1),
                            ("verified but no verification_date", k2),
                            ("no translation_used edition", k3)]

    # sentinel - the em-dash historical defect
    e1 = clean_set(); e1["fixlexA"] = dict(e1["fixlexA"], retrieval={
        "tier": 1, "retrieve_when": ["asked"],
        "do_not_retrieve_when": [{"condition_type": "sense-disambiguation", "text": "—"}],
        "force_llm_vote": False})
    e2 = clean_set(); e2["fixlexB"] = dict(e2["fixlexB"], retrieval={
        "tier": 1, "retrieve_when": ["-"], "do_not_retrieve_when": [],
        "force_llm_vote": False})
    s["sentinel"] = [("em-dash in do_not_retrieve_when (the historical defect)", e1),
                     ("dash sentinel in retrieve_when", e2)]

    # discovery instrument (2026-08-05, Rigor P0-1) - the historical defect:
    # a channel that claims a real search was performed with no instrument
    # named to say what was actually searched
    d1 = clean_set(); d1["fixsrc001"] = dict(d1["fixsrc001"]); d1["fixsrc001"].pop("discovery_instrument")
    s["discovery_instrument"] = [
        ("field-bibliography channel with no discovery_instrument named", d1),
    ]

    # priority-review trigger (2026-08-05, Rigor P1-2) - the re-keyed rule:
    # a builder-prior-knowledge source that licenses a load-bearing claim
    # never itself verified-direct. fixlexA already cites fixsrc001 by
    # default (_term's base sources[]); pushing fixsrc001's discovery
    # channel to builder-prior-knowledge and giving fixlexA a load-bearing,
    # not-verified-direct confidence block reproduces the risk shape.
    p1 = clean_set()
    p1["fixsrc001"] = dict(p1["fixsrc001"], discovery_channel="builder-prior-knowledge")
    p1["fixlexA"] = dict(p1["fixlexA"], confidence={
        "evidentiary_weight": "load-bearing", "verification_state": "verified-via-authority"})
    p2 = clean_set()
    p2["fixsrc001"] = dict(p2["fixsrc001"], discovery_channel="builder-prior-knowledge")
    p2["fixlexA"] = dict(p2["fixlexA"], confidence={
        "evidentiary_weight": "load-bearing", "verification_state": "unverified"})
    s["priority_review"] = [
        ("recall-sourced row licensing a load-bearing, verified-via-authority-only claim", p1),
        ("recall-sourced row licensing a load-bearing, unverified claim", p2),
    ]

    # confidence/source cross-check (2026-08-05, Rigor P1-8) - the record-
    # level Confidence/Gravity Cross-Check analogue: a Documented claim
    # whose linked source(s) carry no verified-direct state, and no
    # divergence_note names the gap (the IJC shape: 8/12 term records
    # Documented, 0/41 IJC source rows verified-direct).
    x1 = clean_set()
    x1["fixlexA"] = dict(x1["fixlexA"], confidence={"formation_confidence": "Documented"})
    # fixlexA already cites fixsrc001 (base sources[]); fixsrc001 carries no
    # confidence block at all here, so its verification_state is None -
    # None != "verified-direct", same as an unpopulated real source row.
    x2 = clean_set()
    x2["fixsrc001"] = dict(x2["fixsrc001"], confidence={"verification_state": "named-not-rechecked"})
    x2["fixlexA"] = dict(x2["fixlexA"], confidence={"formation_confidence": "Documented"})
    s["confidence_source_crosscheck"] = [
        ("Documented term, sole source carries no confidence block at all, no divergence_note", x1),
        ("Documented term, sole source named-not-rechecked (never verified-direct), no divergence_note", x2),
    ]

    # alias safety (VG-1b) - defined below, resolved at call time
    s["alias_safety"] = _alias_seeded_sets()

    # distribution health (2026-08-05, Rigor P1-1) - the historical defect:
    # every term record's confidence.verification_state landing on the same
    # value fleet-wide, reconstructed as a query. A second seed on a
    # different (record_type, field) pair proves the gate is the general
    # check the task asked for, not a verification_state special-case.
    u1 = clean_set()
    u1["fixlexA"] = dict(u1["fixlexA"], confidence={"verification_state": "verified-via-authority"})
    u1["fixlexB"] = dict(u1["fixlexB"], confidence={"verification_state": "verified-via-authority"})
    u2 = clean_set()
    u2["fixsrc002"] = _src("fixsrc002")  # boundary_status defaults to "Native", same as fixsrc001
    s["distribution_health"] = [
        ("all term records carry the same confidence.verification_state (the P1-1 shape)", u1),
        ("all source records carry the same boundary_status", u2),
    ]

    # mechanism coverage (T3-D/T3-G, 2026-08-15). One seed per declared
    # dependency in mechanism_dependencies.py, reconstructing the real
    # fleet defects the gate was built from: desert carries 13 figures and
    # not one attested date, pahc has no quote records at all. Uses its own
    # clean set (mechanism_coverage_clean) rather than clean_set(), whose
    # fixture figures and quotes predate all three dependencies - the same
    # per-gate clean-fixture pattern confidence_crosscheck_clean_pair and
    # rule_c_clean already follow.
    m1 = mechanism_coverage_clean()
    m1["fixfigA"] = {k: v for k, v in m1["fixfigA"].items() if k != "dates"}
    m2 = mechanism_coverage_clean()
    del m2["fixqA"]
    m3 = mechanism_coverage_clean()
    m3["fixfigA"] = {k: v for k, v in m3["fixfigA"].items() if k != "bridge_line"}
    s["mechanism_coverage"] = [
        ("figures exist but none carry a date (the desert 0/13 shape)", m1),
        ("no quote records at all (the pahc shape)", m2),
        ("figures exist but none carry a bridge_line", m3),
    ]

    # voice readability (T3 follow-on, 2026-08-16). Uses its own clean set
    # (readability_clean) for the same reason mechanism_coverage_clean and
    # confidence_crosscheck_clean_pair do - clean_set()'s fixture records
    # carry no `register` field at all, so testing against it would prove
    # nothing about whether the gate can actually see unreadable content.
    # selftest() counts an advisory (note:-prefixed) finding as a pass for
    # this loop's purposes - see its own comment on DETECTION vs blocking.
    w1 = readability_clean()
    w1["fixreadQ"] = dict(w1["fixreadQ"], text_translation=UNREADABLE_LONG)
    w2 = readability_clean()
    w2["fixreadV"] = dict(w2["fixreadV"], speaking_model=UNREADABLE_JARGON)
    s["readability"] = [
        ("emic quote text_translation past the FK/FRE reading floor "
         "(the Marius-reconstruction shape)", w1),
        ("emic voice_profile speaking_model in dense jargon prose", w2),
    ]
    return s


def mechanism_coverage_clean():
    """Every dependency in mechanism_dependencies.py satisfied, minimally.

    Deliberately NOT built on clean_set(): its `_fig` predates bridge_line
    and `dates`, and its `_quote` carries no text_translation, so the shared
    clean set fails all three coverage dependencies. Extending _fig/_quote
    instead would push new fields into every other gate's seeded sets -
    distribution_health in particular fails on a field whose values are
    uniform across records, so silently adding one to the shared fixture is
    how a fixture file starts breaking gates it was meant to prove.
    """
    fig = _fig("fixfigA", "Abba Fixture", True, [])
    fig["bridge_line"] = "A fixture figure, named so the bridge has something to render."
    fig["dates"] = {"kind": "life", "display": "d. 399"}
    quote = _quote("fixqA")
    quote["text_translation"] = "A licensed saying, recorded for the fixture."
    return {r["id"]: r for r in [fig, quote]}


# ------------------------------------------------------ voice readability

def readability_clean():
    """register: emic content across all five v1 record types
    (_READABILITY_FIELDS in gates.py), using the RCF-band READABLE_TEXT
    fixture prose - proves the gate passes genuinely readable content,
    not merely that it found nothing to check. Also carries one
    register: etic record with UNREADABLE_LONG text, proving the register
    filter actually excludes builder/scaffolding prose rather than
    happening to pass it."""
    quote = {"id": "fixreadQ", "world_id": "fixture-world", "record_type": "quote",
             "schema_version": 1, "register": "emic", "locus": "fixture",
             "license": "verbatim", "text_translation": READABLE_TEXT,
             "confidence": {"verification_state": "verified-direct"}}
    story = {"id": "fixreadS", "world_id": "fixture-world", "record_type": "story",
             "schema_version": 1, "register": "emic", "title": "fixture story",
             "narrative_tier": {"tier": 2, "justification": "fixture"},
             "text": READABLE_TEXT, "owner_figure_id": "fixfigA",
             "attested_occasion": "the attested occasion", "tellable_as": "scene"}
    ambient = {"id": "fixreadA", "world_id": "fixture-world", "record_type": "ambient",
               "schema_version": 1, "register": "emic", "title": "fixture ambient",
               "text": READABLE_TEXT}
    demo = {"id": "fixreadD", "world_id": "fixture-world", "record_type": "demonstration",
            "schema_version": 1, "register": "emic", "dialogue": READABLE_TEXT,
            "situation_tag": "fixture"}
    voice = {"id": "fixreadV", "world_id": "fixture-world", "record_type": "voice_profile",
              "schema_version": 1, "register": "emic",
              "speaking_model": READABLE_TEXT, "trait_rubric": READABLE_TEXT}
    etic_scaffolding = {"id": "fixreadE", "world_id": "fixture-world",
                        "record_type": "story", "schema_version": 1,
                        "register": "etic", "title": "fixture etic note",
                        "narrative_tier": {"tier": 2, "justification": "fixture"},
                        "text": UNREADABLE_LONG, "owner_figure_id": "fixfigA",
                        "attested_occasion": "the attested occasion",
                        "tellable_as": "scene"}
    return {r["id"]: r for r in
            [quote, story, ambient, demo, voice, etic_scaffolding]}


# -------------------------------------------------- alias safety (VG-1b)

def alias_override_set():
    """SS5.6 override fixture: a term whose bare generic alias is covered
    by a term-level alias_generic_override_note - the gate must REPORT it
    (one 'note:' line), neither silently pass nor hard-fail."""
    rs = clean_set()
    rs["fixlexC"] = _term(
        "fixlexC",
        term="Thanatos Fixture",
        aliases=["death"],
        alias_generic_override_note=(
            "'death' is deliberately generic: the world's own record has "
            "no distinct period form (the bare Death/Christ/Prayer class)."),
        field_relations=[])
    return rs


def _alias_seeded_sets():
    s = []
    # Rule A: a bare generic single-word alias, no override
    a1 = clean_set()
    a1["fixlexC"] = _term("fixlexC", term="Zoe Fixture",
                          aliases=["life"], field_relations=[])
    s.append(("bare generic single-word alias ('life'), no override", a1))
    # Rule A determiner shape: the 'the word'/'the son' reconstruction
    a2 = clean_set()
    a2["fixlexC"] = _term("fixlexC", term="Logos Fixture",
                          aliases=["the word", "ho logos fixture"],
                          field_relations=[])
    s.append(("determiner-led generic ('the word' -> 'word')", a2))
    # Rule B: the photismos shape - one term's alias colliding with
    # another term's alias, same world, post-parse key space (the
    # parenthetically-qualified variant contributes no key, exactly as
    # the VG-1a parser behaves - so the collision here is the REAL
    # unqualified overlap, the still-live class)
    b1 = clean_set()
    b1["fixlexC"] = _term("fixlexC", term="Baptism Fixture",
                          aliases=["photismos-fixture",
                                   "illumination-fixture (baptismal)"],
                          field_relations=[])
    b1["fixlexD"] = _term("fixlexD", term="Illumination Fixture",
                          aliases=["photismos-fixture"],
                          field_relations=[])
    s.append(("Rule B collision: two terms share an unqualified alias "
              "key (the photismos shape)", b1))
    # Rule B: term-name-vs-alias - the illumination shape (a canonical
    # name colliding with another term's alias; aliases-only checking
    # misses this class)
    b2 = clean_set()
    b2["fixlexC"] = _term("fixlexC", term="Restoration Fixture",
                          aliases=["apokatastasis-fixture"],
                          field_relations=[])
    b2["fixlexD"] = _term("fixlexD", term="Apokatastasis-Fixture",
                          aliases=[], field_relations=[])
    s.append(("Rule B collision: a term's own canonical name vs another "
              "term's alias (the apokatastasis shape)", b2))
    # stale override: note present, nothing trips Rule A
    o1 = clean_set()
    o1["fixlexC"] = _term("fixlexC", term="Qyama Fixture",
                          aliases=["bar qyama fixture"],
                          alias_generic_override_note="stale note",
                          field_relations=[])
    s.append(("stale alias_generic_override_note (nothing trips Rule A)", o1))
    return s


# ------------------------------- confidence/source cross-check (P1-8)

def confidence_crosscheck_clean_pair():
    """The two legitimate ways a Documented claim clears the cross-check
    (P1-8's own gate docstring) - a verified-direct linked source, or an
    explicit divergence_note where no linked source is verified-direct.
    Neither should trip the gate."""
    rs_verified = clean_set()
    rs_verified["fixsrc001"] = dict(rs_verified["fixsrc001"],
        confidence={"verification_state": "verified-direct"})
    rs_verified["fixlexA"] = dict(rs_verified["fixlexA"],
        confidence={"formation_confidence": "Documented"})

    rs_noted = clean_set()
    rs_noted["fixlexA"] = dict(rs_noted["fixlexA"], confidence={
        "formation_confidence": "Documented",
        "divergence_note": ("Evidential confidence is Documented for the underlying "
                             "fact; the sole linked source is named-not-rechecked, not "
                             "verified-direct this session - divergence named, not "
                             "resolved by upgrading (fixture, Doc_04's own pattern).")})
    return rs_verified, rs_noted


# ------------------------------------------------ Rule C (VG-1c SS5.5)

def rule_c_seeded():
    """A confirmed-gloss entry WITH term_id whose original collides with
    a DIFFERENT term's alias key in the same world - the cross-namespace
    defect Rule C exists to catch. Returns (records, gloss_entries) -
    the selftest injects gloss_entries via core._GLOSS_CACHE."""
    rs = clean_set()
    rs["fixlexC"] = _term("fixlexC", term="Lumen Fixture",
                          aliases=["fixture-light"], field_relations=[])
    rs["fixlexD"] = _term("fixlexD", term="Candela Fixture",
                          aliases=["lumen-fixture"], field_relations=[])
    glosses = [{"world_id": "fixture-world", "term_id": "fixlexC",
                "category": "A", "original": "lumen-fixture",
                "gloss": "the fixture light",
                "exact_wording_required": True}]
    return rs, glosses


def rule_c_clean():
    """The same shape with NO collision (the gloss original is its own
    term's key only) plus one entry WITHOUT term_id - Rule C must pass
    the first and report the second as a pending note, never a
    violation."""
    rs = clean_set()
    rs["fixlexC"] = _term("fixlexC", term="Lumen Fixture",
                          aliases=["lumen-fixture"], field_relations=[])
    glosses = [{"world_id": "fixture-world", "term_id": "fixlexC",
                "category": "A", "original": "lumen-fixture",
                "gloss": "the fixture light",
                "exact_wording_required": True},
               {"world_id": "fixture-world",
                "category": "A", "original": "candela-fixture",
                "gloss": "the other light",
                "exact_wording_required": True}]
    return rs, glosses
