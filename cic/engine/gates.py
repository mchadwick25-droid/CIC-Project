"""S1.3 machine gates (Pass 1 SS4.2), run against record sets.

Requirements source (S6.1, adopted 2026-07-27): the governing standard
is the World Build Completion Standard (archived old tree; see git history).

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
            # Four-register firewall (redesign step 5, 2026-08-14): a record
            # that feeds retrievable chunks may never stand on an Excluded
            # source - the Comparandum firewall held structurally only by
            # omission before this check existed.
            elif sid and r.get("record_type") in ("term", "story", "ambient") \
                    and records[sid].get("boundary_status") == "Excluded":
                out.append(f"{rid}: sources[] -> {sid} is boundary_status="
                           f"Excluded - chunk-feeding records may not cite "
                           f"an Excluded source")
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
        # "sources" added 2026-08-05 (full-system review, Rigor P0-3): the
        # completion profile didn't require it, so the one world that
        # omitted sources[] on every force record (Imperial-Juridical,
        # 0/10) passed anyway. A force record with a genuinely empty
        # sources[] (evidence living in a different world's registry, for
        # example) still SHOULD show up here - that's the honest result,
        # not a bug to work around.
        "force": ["six_cell_position", "layer_historical_event",
                   "layer_worlds_own_experience", "layer_formation_impact",
                   "layer4", "sources"],
        "figure": ["names", "narratable"],
        # Redesign step 5 (2026-08-14): Native-Ambient's own bar - texture
        # without a source is invented texture, and unmarked texture can be
        # mistaken for a named voice's own claim.
        "ambient": ["title", "text", "ambient_domain", "period_note",
                     "sources", "retrieval", "source_register"],
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
            # A not-advanced gravity documents a candidate Doc_04 did NOT
            # advance (the schema keeps them as required records); the
            # six-test battery is what advancing would have been, so its
            # absence is the record's meaning, not a gap.
            if f == "six_tests" and rt == "gravity" \
                    and r.get("classification") == "not-advanced":
                continue
            if not _present(r, f):
                out.append(f"{rid} ({rt}, {profile}): required field missing/empty: {f}")
        if rt == "gravity" and _present(r, "six_tests") and len(r["six_tests"]) < 6:
            out.append(f"{rid}: six_tests carries {len(r['six_tests'])}/6 verdicts")
        # Redesign step 5 (2026-08-14): the register marking must be RIGHT,
        # not merely present - an ambient record claiming any other register
        # would smuggle texture past the four-register rules.
        if rt == "ambient" and r.get("source_register") not in (None, "native-ambient"):
            out.append(f"{rid}: ambient record carries source_register="
                       f"{r.get('source_register')!r} - must be native-ambient")
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
    Values from the reading-floor parameters (RCF V3.2 Part Five).

    Deliberately hard-fails, not silently, if textstat isn't installed -
    a readability GATE that can't actually check readability must not
    report a false pass. The guard here only turns an opaque
    ModuleNotFoundError into an actionable one; textstat is a dev/gate-time
    dependency (pyproject.toml's [dev] extra, requirements.txt), never
    imported by the running app (2026-08-05 full-system review,
    Accessibility P1-8)."""
    try:
        import textstat
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "readability_check requires the 'textstat' package, which isn't "
            "installed in this environment. Install it with `pip install "
            "textstat` or `pip install -e '.[dev]'` (see pyproject.toml)."
        ) from exc
    # textstat >= 0.7.7 counts syllables through nltk's cmudict, which
    # `pip install textstat` does NOT bring with it - the corpus is a
    # separate download. Untranslated, that surfaces as a forty-line nltk
    # LookupError from three frames inside textstat, which is how this
    # module's first two-move calibration run died. Same discipline as the
    # missing-textstat guard above: an unrunnable readability gate must say
    # so in one actionable line.
    try:
        fk = textstat.flesch_kincaid_grade(text)
    except LookupError as exc:
        raise LookupError(
            "readability_check needs nltk's 'cmudict' corpus, which textstat "
            "uses to count syllables and which pip does not install. Run "
            "`python -c \"import nltk; nltk.download('cmudict')\"`."
        ) from exc
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


# ------------------------------------------------- readability, by the move
#
# A Representative's turn is not one register and must not be scored as one
# (Mark, 2026-08-17: "split the readability check into the two moves").
# readability_check above averages a whole turn into a single grade, so the
# plain answer and the sourced claim behind it cancel each other out: hitting
# one band across both flattens the depth, and the average hides a first
# sentence nobody can skim behind a simple second half. The two moves are
# scored separately, against different rules, because they are doing
# different jobs:
#
#   move one - the plain answer, front-loaded. This is the part that must
#     survive skimming, so the reading ceiling is non-negotiable here.
#   move two - the world's own angle: the sourcing, the hedge, the thing
#     that stands on one leg. Allowed to be denser. Judged on grounding
#     elsewhere; here it only has to stay this side of impenetrable.
#
# Where the boundary falls. The corpus has no paragraph breaks to split on
# and no author-marked boundary, so the split is the reader's, not the
# writer's: move one is the leading WHOLE sentences up to a 30-word skim
# window. Whole sentences because FK divides words by sentences - a fragment
# scored as a sentence corrupts the number being read. 30 words because it is
# roughly what a reader takes in before deciding whether to keep going, and
# because measured against the 127 Representative turns in the corpus it
# leaves 107 of them with a move two long enough to score (a 50-word window
# leaves only 83).
SKIM_WINDOW_WORDS = 30

# Below this, FK is noise, not a measurement: the first calibration run
# returned FK -0.7 on a 12-word residual. Short segments are reported as
# unscored rather than given a number that looks like a finding.
_MIN_SCOREABLE_WORDS = 15

# Move one carries a CEILING ONLY, and the absence of a floor here is a
# decision, not an oversight.
#
# A syllables-per-word floor stood here briefly (2026-08-17) as an attempt at
# the both-directions guard, and was withdrawn the same day. It contradicted
# this project's own governing parameter, which had already settled the
# question and which I had not read before writing it -
# parameters.yaml reading_floor says the band is "independent of vocabulary"
# and "Sentence structure only, never vocabulary". Syllables-per-word is a
# vocabulary measure. It also failed on its merits: it flagged nine move-ones
# for using short words, which is not a defect, and Mark's objection was the
# correct one - syllable count is not an indicator of quality.
#
# Nor can the floor be FK. FK = 0.39*(words/sentence) + 11.8*(syllables/word)
# - 15.59, and measured across the corpus 67% of the gap between the
# sub-floor move-ones and the in-band ones is the sentence-length term. An FK
# floor would mostly push six worlds toward LONGER SENTENCES - against both
# the desert short-sentence rule added after a measured breach, and the
# exemplars this system is aiming at, which are plainer than the band, not
# denser (BBC's measured grade sits near 6).
#
# The real conclusion is that the too-simple direction is not a readability
# failure at all. "Oversimplified" means the answer left out the major
# truths - a claim about CONTENT, which no readability formula can see. A
# turn that omits everything that matters, said in short clean sentences,
# scores beautifully here and always will. That direction is guarded by the
# answer-completeness check, not by this one, and pretending a formula covers
# it is how the floor stayed decorative for so long.
MOVE_ONE_BAND = {"fk_max": 10.0, "fre_min": 60.0}

# Move two is allowed to be hard; it is not allowed to be unreadable. These
# flag 5 of 83 - the syriac and hieronymian turns whose second move runs to
# FK 20+, which is not density, it is a sentence that got away.
MOVE_TWO_BAND = {"fk_max": 14.0, "fre_min": 40.0}

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
# Demonstration dialogue is a script: "{{random_user}}: ..." alternating with
# "Theon: ...". Only the Representative's turns are answers to a participant,
# so only they have two moves - scoring the participant's scripted questions
# for readability, as the whole-field check did, measures our own test prose.
_SPEAKER_LINE = re.compile(r"^\s*(\{\{random_user\}\}|[A-Z][\w'’\- ]{0,40}):\s*(.*)$")
_PARTICIPANT_LABEL = "{{random_user}}"


def split_moves(text: str, window: int = SKIM_WINDOW_WORDS) -> tuple:
    """Split one Representative turn into (move one, move two).

    Move one is the leading whole sentences up to `window` words; move two is
    everything after. A turn shorter than the window is all move one and
    returns "" for move two - which is a real answer, not a defect: a short
    plain reply has no second move to score.

    The sentence that CROSSES the window is kept in move one, not pushed into
    move two. A reader skimming 30 words has already started it, so it is part
    of what has to survive skimming; the consequence is that one runaway
    sentence early in a turn lands as a move-one finding rather than a
    move-two one, which is the correct report and not a misfile.
    """
    sentences = [s for s in _SENTENCE_SPLIT.split((text or "").strip()) if s.strip()]
    first, words = [], 0
    for sentence in sentences:
        first.append(sentence)
        words += len(sentence.split())
        if words >= window:
            break
    return " ".join(first), " ".join(sentences[len(first):])


def representative_turns(dialogue: str,
                         participant: str = _PARTICIPANT_LABEL) -> list:
    """The Representative's turns out of a demonstration dialogue, in order.

    A dialogue carrying no speaker labels at all is one turn - the fixture
    prose is written that way, and so is any record that predates the
    convention.
    """
    turns, current, speaker = [], [], None
    for line in (dialogue or "").splitlines():
        match = _SPEAKER_LINE.match(line)
        if match:
            if speaker is not None and speaker != participant and current:
                turns.append(" ".join(current).strip())
            speaker, current = match.group(1), [match.group(2)]
        elif line.strip():
            current.append(line.strip())
    if speaker is not None and speaker != participant and current:
        turns.append(" ".join(current).strip())
    if speaker is None:
        turns = [" ".join((dialogue or "").split())]
    return [t for t in turns if t.strip()]


def _measure(segment: str) -> dict:
    """Sentence structure and word choice for one segment, or None if it is
    too short for those numbers to mean anything.

    THREE numbers, not two. FK and FRE are sentence-architecture measures -
    FK's vocabulary term is a syllable count, which is not a measure of
    whether a reader knows the word. Dale-Chall is the industry-standard
    word-CHOICE instrument: the share of words falling outside a 2,941-word
    familiar list. That is the difference between "hard to say" and "unknown",
    and under the current design (plain modern word first, lexicon word
    introduced after) word choice is squarely in scope.

    parameters.yaml still says the reading floor is "independent of
    vocabulary". That parameter describes the SUPERSEDED design, where the
    world's own word led and the explanation followed; see its own dated note.
    Do not read it as excluding this.
    """
    if len(segment.split()) < _MIN_SCOREABLE_WORDS:
        return None
    import textstat  # guarded by readability_check's own import error above
    return {
        "words": len(segment.split()),
        "fk_grade": round(textstat.flesch_kincaid_grade(segment), 2),
        "fre": round(textstat.flesch_reading_ease(segment), 2),
        "dale_chall": round(textstat.dale_chall_readability_score(segment), 2),
    }


# ------------------------------------------------------ the lexicon's order
#
# Mark, 2026-08-17, correcting the design this module had been reading out of
# a stale parameter: "the independence of vocabulary was under an old design
# where we were using the world words and then explaining them, but we have
# switched the order and are now limiting words to modern easy read and then
# introducing the lexicon word. we taught about two ways to see the world (the
# two ways) before we came to baptism (the water)."
#
# So the rule is positional and it needs no threshold: the plain modern form
# leads, the world's word is introduced against it. Both halves are already in
# the term records, and those records are still written in the OLD order -
#
#     term: 'Anachoresis (Withdrawal)'      world word first, plain in parens
#     term: 'Knowledge / Gnosis'
#
# - which is itself worth seeing.
#
# What counts as "the lexicon word" is decided by the same familiar-word list
# Dale-Chall uses, not by a guess. Alexandria's lexicon carries Teacher, Soul,
# Love and Prayer as terms; those are already modern easy-read words and
# flagging them would make this gate noise. A term form is a lexicon word only
# if some part of it falls outside the familiar list.
def _familiar_words():
    from textstat.backend.utils._get_lang_easy_words import get_lang_easy_words
    return get_lang_easy_words("en")


def _fold(text: str) -> str:
    """Strip diacritics so raza / razā / rāzā are one form."""
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", text or "")
                   if not unicodedata.combining(c)).lower()


_TERM_TOKEN = re.compile(r"[a-z' -]{4,}")


def lexicon_index(records: dict) -> tuple:
    """(lexicon forms, plain forms) for a world, from its own term records.

    A form whose every word is on the familiar list is a PLAIN form - it is
    what should lead. Anything else is a lexicon word needing introduction.
    """
    easy = _familiar_words()
    lexicon, plain = {}, set()

    def parts(raw):
        for chunk in re.split(r"[/,]", re.sub(r"\([^)]*\)", " ", raw or "")):
            chunk = _fold(chunk.strip().strip('"'))
            if _TERM_TOKEN.fullmatch(chunk):
                yield chunk

    for rid, r in sorted(records.items()):
        if r.get("record_type") != "term":
            continue
        sources = [r.get("term", "")]
        sources += [a for a in (r.get("aliases") or []) if isinstance(a, str)]
        # the parenthetical inside a term head is the world's own gloss -
        # "Anachoresis (Withdrawal)" hands us the plain form directly
        for gloss in re.findall(r"\(([^)]*)\)", r.get("term", "") or ""):
            for form in parts(gloss):
                plain.add(form)
        for src in sources:
            for form in parts(src):
                if all(w.strip("'-") in easy for w in form.split()):
                    plain.add(form)
                else:
                    lexicon.setdefault(form, rid)
    # A form reachable both ways is plain. Flagging an ordinary English word
    # as the lexicon word is the failure that makes a check like this useless.
    for form in plain:
        lexicon.pop(form, None)
    return lexicon, plain


def lexicon_order_findings(turn: str, lexicon: dict, plain: set) -> list:
    """Did a lexicon word arrive before any plain form that could carry it?"""
    if not lexicon:
        return []
    folded = _fold(turn)
    pattern = re.compile(r"\b(" + "|".join(sorted(map(re.escape, lexicon),
                                                  key=len, reverse=True)) + r")\b")
    hit = pattern.search(folded)
    if not hit:
        return []
    word, at = hit.group(1), hit.start()
    if plain:
        lead = re.compile(r"\b(" + "|".join(sorted(map(re.escape, plain),
                                                   key=len, reverse=True)) + r")\b")
        if lead.search(folded[:at]):
            return []
    where = "move one" if _fold(split_moves(turn)[0]).find(word) != -1 else "move two"
    return [f"lexicon word '{word}' ({lexicon[word]}) arrives in {where} with no "
            f"plain form ahead of it - the modern word leads, the world's word "
            f"is introduced against it"]


def two_move_readability(turn: str) -> dict:
    """Score one Representative turn as its two moves rather than as an
    average. Returns {"move_one": ..., "move_two": ..., "violations": [...]},
    where each move is a _measure() dict, None if too short to score.

    Both directions are guarded on move one; move two carries a ceiling only.
    """
    # readability_check's textstat import error is the actionable one; call it
    # on a trivial string first so a missing dependency fails here the same
    # way rather than surfacing as an opaque ImportError inside _measure.
    readability_check("A sentence.")
    one, two = split_moves(turn)
    m1, m2 = _measure(one), _measure(two)
    violations = []

    if m1 is None:
        violations.append(
            f"move one is {len(one.split())} words - too short to score "
            f"(under {_MIN_SCOREABLE_WORDS}); a turn this short cannot be "
            "read as an answer plus its grounding")
    else:
        if m1["fk_grade"] > MOVE_ONE_BAND["fk_max"]:
            violations.append(
                f"move one FK grade {m1['fk_grade']:.1f} > "
                f"{MOVE_ONE_BAND['fk_max']} - the opening does not survive "
                "skimming")
        if m1["fre"] < MOVE_ONE_BAND["fre_min"]:
            violations.append(
                f"move one FRE {m1['fre']:.1f} < {MOVE_ONE_BAND['fre_min']} - "
                "the opening does not survive skimming")

    if m2 is not None:
        if m2["fk_grade"] > MOVE_TWO_BAND["fk_max"]:
            violations.append(
                f"move two FK grade {m2['fk_grade']:.1f} > "
                f"{MOVE_TWO_BAND['fk_max']} - past dense into impenetrable")
        if m2["fre"] < MOVE_TWO_BAND["fre_min"]:
            violations.append(
                f"move two FRE {m2['fre']:.1f} < {MOVE_TWO_BAND['fre_min']} - "
                "past dense into impenetrable")

    return {"move_one": m1, "move_two": m2, "violations": violations}


# gate_readability (above) has existed since the clean-room rebuild but was
# never called by anything - no entry in run_gates.py's GATES dict, no CI
# coverage. voice_profile even carries a schema field for this
# (reading_level_check, "$comment": "inherits the reading floor from the
# engine parameters - a pointer, not a restatement") that nothing has ever
# verified; it is builder-written prose today, not a computed result. This
# gate closes that gap for the record types whose fields are actual spoken
# material a Representative would say to a participant.
#
# demonstration is deliberately NOT in this map any more (2026-08-17). Its
# dialogue field is the only one here that holds Representative turns - the
# thing the two-move split is about - so it routes through
# two_move_readability instead. The rest stay on the whole-text check because
# they are not turns: a quote translation, a story, an ambient passage and a
# voice_profile rubric have no plain-answer-then-grounding shape to split, and
# a skim window over a quote would be measuring a boundary that isn't there.
_READABILITY_FIELDS = {
    "quote": ("text_translation",),
    "story": ("text",),
    "ambient": ("text",),
    "voice_profile": ("speaking_model", "trait_rubric"),
}
# contested_claim dropped from v1 (2026-08-16, Mark's call): its fields mix
# etic framing into emic-register records in ways not yet sorted out field
# by field. guided_starters deferred to v2 for a different reason - its
# content is body-verbatim (the schema is almost empty by design), and
# run_gates.py's load_records() keeps front matter only, discarding the
# body every other gate here reads from. Adding it would need a second,
# parallel loader that nothing else in this file needs.


def gate_voice_readability(records: dict) -> list:
    """Does this world's participant-facing prose actually clear the
    reading-floor thresholds (readability_check/RCF V3.2 Part Five), not
    just carry an unverified claim that it does?

    Scoped to register: emic records only - the world's own spoken voice,
    not etic/builder scaffolding, mirroring how every quote/story record
    authored this session has carried register: emic already.

    Two paths, because two kinds of prose (2026-08-17):
      - demonstration.dialogue holds Representative TURNS, so each turn is
        split at the skim window and its two moves scored against their own
        rules (two_move_readability). The participant's scripted lines are
        dropped - they are our test prose, not the world's voice, and the
        whole-field check was scoring them.
      - everything else in _READABILITY_FIELDS is checked whole, as before.

    ADVISORY (2026-08-16 decision, mirroring mechanism_coverage's
    2026-08-15 one): a first run against six worlds' pre-existing emic
    content will surface real debt that predates this gate, not a defect
    introduced by anything landing today. Every finding is reported in
    full behind _NOTE_PREFIX rather than counted as a violation - visible,
    not blocking, and unable to fail CI by construction (gate_counts()
    already excludes _NOTE_PREFIX lines from its ratchet unit, the same
    mechanism that keeps mechanism_coverage advisory in practice and not
    just in name).
    """
    out = []
    lexicon, plain = None, set()
    for rid, r in sorted(records.items()):
        if r.get("register") != "emic":
            continue

        if r.get("record_type") == "demonstration":
            dialogue = r.get("dialogue")
            if not isinstance(dialogue, str) or not dialogue.strip():
                continue
            if lexicon is None:  # built once per world, not once per record
                lexicon, plain = lexicon_index(records)
            for i, turn in enumerate(representative_turns(dialogue), start=1):
                findings = (two_move_readability(turn)["violations"]
                            + lexicon_order_findings(turn, lexicon, plain))
                for finding in findings:
                    out.append(f"{_NOTE_PREFIX} {rid}.dialogue turn {i}: {finding}")
            continue

        fields = _READABILITY_FIELDS.get(r.get("record_type"))
        if not fields:
            continue
        texts = {}
        for field in fields:
            v = r.get(field)
            if isinstance(v, str) and v.strip():
                texts[f"{rid}.{field}"] = v
        for finding in gate_readability(texts):
            out.append(f"{_NOTE_PREFIX} {finding}")
    return out


# --------------------------------------------------------- discovery channel

# discovery_channel is the one field whose whole purpose is to tell a
# reviewer where to concentrate scrutiny (doc 14: "that column IS the
# fabricated-precision risk map"). Added 2026-08-05 (full-system review,
# Rigor P0-1) after a migration-time bug stamped 50 rows across three
# worlds "field-bibliography" by a type heuristic, not evidence - the
# worlds' own search records confirm no field bibliography was ever
# consulted. This gate can't detect THAT specific failure (it has no way
# to check a claim against a search record), but it catches the general
# shape of it going forward: a channel that claims a real search
# instrument was used, with no instrument actually named.
_INSTRUMENT_REQUIRED_CHANNELS = {
    "field-bibliography", "database-search", "library-catalogue",
}


def gate_discovery_instrument(records: dict) -> list:
    """Every source row whose discovery_channel claims a searched
    instrument (field-bibliography / database-search / library-catalogue)
    must name discovery_instrument. A row that names none of those three
    channels is unaffected - builder-prior-knowledge, snowball, and the
    other channels don't imply a search instrument exists to name."""
    out = []
    for rid, r in records.items():
        if r.get("record_type") != "source":
            continue
        channel = r.get("discovery_channel")
        if channel in _INSTRUMENT_REQUIRED_CHANNELS and not _present(r, "discovery_instrument"):
            out.append(
                f"{rid}: discovery_channel={channel} requires a "
                f"discovery_instrument naming what was actually searched"
            )
    return out


# ----------------------------------------------------- priority-review trigger

def gate_priority_review_trigger(records: dict) -> list:
    """Priority-review trigger, re-keyed (2026-08-05 full-system review,
    Rigor P1-2). The prior rule (L3B-World-Build-Methodology's Source
    Registry Template / Doc_02B, step 4) flagged 'anything at Confidence C
    or below supporting a vivid, specific claim.' That threshold was set
    when the Confidence letter's B meant 'specific work/locus named.' After
    IJC's Round-1 recalibration, B means recall: 'drawn from this build's
    own historical knowledge; not independently re-collated this session' -
    the legacy letter no longer marks the risk boundary doc 14's own
    evidence says the risk actually lives at.

    Re-keyed onto the SS3.0 axes that now exist, joined the way the data
    actually is: a source row's own discovery_channel records HOW it was
    found; a source row never itself carries a populated confidence block
    (verification_state/evidentiary_weight) in the current record store -
    those live on the CITING record's confidence block (a term, quote, or
    any other record type that links back to the source via sources[]).
    So the flag is:

        source.discovery_channel == "builder-prior-knowledge"
        AND some citing record C with {source.id} in C.sources[]
            has C.confidence.evidentiary_weight == "load-bearing"
        AND that same C.confidence.verification_state != "verified-direct"

    i.e. a recall-sourced row that licenses a load-bearing claim which has
    never itself been directly re-verified this session - the fabricated-
    precision failure mode the rule exists to catch.

    Only term and quote records carry a populated confidence block in the
    record store today (2026-08-05 audit); a source cited only by
    gravity/force/story/contested_claim/world_core rows - none of which
    carry confidence yet - cannot be flagged by this rule until those
    record types are backfilled. That is a real, separate data gap (the
    same one P1-1 diagnosed for verification_state), not a defect in this
    gate; it means the count this gate reports on the live fleet is a
    floor, not a ceiling."""
    out = []
    citing = {}
    for rid, r in records.items():
        for link in r.get("sources") or []:
            sid = link.get("source_id")
            if sid:
                citing.setdefault(sid, []).append(r)
    for rid, r in records.items():
        if r.get("record_type") != "source":
            continue
        if r.get("discovery_channel") != "builder-prior-knowledge":
            continue
        for citer in citing.get(rid, []):
            conf = citer.get("confidence") or {}
            if (conf.get("evidentiary_weight") == "load-bearing"
                    and conf.get("verification_state") != "verified-direct"):
                out.append(
                    f"{rid}: discovery_channel=builder-prior-knowledge licenses "
                    f"{citer.get('id')}'s load-bearing claim "
                    f"(verification_state={conf.get('verification_state')}) - "
                    f"priority review"
                )
    return out


# --------------------------------------------------------- distribution health

# 2026-08-05 (full-system review, Rigor P1-1): 118/118 term records read
# `verification_state: verified-via-authority` - never the other three
# values of that four-value axis. A field whose distribution is a constant
# carries zero information, and no existing gate could see it: schema
# validation only checks that a value is A member of the enum, never that
# the enum as actually used carries more than one member fleet-wide.
# General on purpose (doc 14's own complaint - "judgments stored in free
# text where the next builder has to rediscover it by reading" - applies
# to any enum field, not only this one): a small, versioned, configurable
# list of (record_type, dotted_field_path) pairs, checked the same way.
# Adding a pair here rides the gate-integrity rule like SYMMETRIC/INVERSE
# above; it is not auto-derived from the schema, so a genuinely-legitimate
# constant (a field that just happens to have one valid value across a
# small fleet) needs a human decision to add, not a silent trip.
DISTRIBUTION_HEALTH_CHECKS = [
    ("term", "confidence.verification_state"),
    ("source", "boundary_status"),
]


def _get_dotted(record: dict, dotted_field: str):
    v = record
    for part in dotted_field.split("."):
        if not isinstance(v, dict):
            return None
        v = v.get(part)
    return v


def gate_distribution_health(records: dict, checks=None) -> list:
    """Fails when a checked enum field's value distribution, across every
    record of a given record_type, is a single constant value (100% one
    value, 2+ records carrying it). Checks a small configurable list of
    (record_type, dotted_field_path) pairs (DISTRIBUTION_HEALTH_CHECKS by
    default) rather than hardcoding the verification_state case alone -
    this is a general distribution-health check, not a one-off patch.
    Records where the field is absent/empty are excluded from the sample
    (silent - a missing field is gate_field_completion's job, not this
    one's); fewer than 2 present values can't demonstrate a distribution
    either way and are skipped."""
    checks = DISTRIBUTION_HEALTH_CHECKS if checks is None else checks
    out = []
    for record_type, field in checks:
        values = []
        for r in records.values():
            if r.get("record_type") != record_type:
                continue
            v = _get_dotted(r, field)
            if v is None or (isinstance(v, (list, dict, str)) and not v):
                continue
            values.append(v)
        if len(values) >= 2 and len(set(values)) == 1:
            out.append(
                f"{record_type}.{field}: all {len(values)} record(s) carry "
                f"the single value {values[0]!r} - a field whose "
                f"distribution is a constant carries zero information"
            )
    return out


# ------------------------------------------- confidence/source cross-check

def gate_confidence_source_crosscheck(records: dict) -> list:
    """2026-08-05 (full-system review, Rigor P1-8): the record-level
    analogue of Syriac Doc_04's own Confidence/Gravity Cross-Check
    (Doc_04_Gravity_Discovery.md - each candidate's own paragraph:
    'Evidential confidence is Documented ... No divergence to flag', or,
    where it does diverge, 'This is the clearest case of intentional
    divergence ... named explicitly, not resolved by upgrading'). Doc_04
    runs that check in prose, once per gravity candidate, one document at
    a time; there is no analogue one level down, at the individual record
    - so the divergence it exists to catch is invisible and ungated there.

    A record whose own confidence.formation_confidence == 'Documented' is
    claiming the Constitution's own top evidentiary tier ('multiple
    independent sources with no serious scholarly dispute'). Per P1-8,
    that is a claim about the STATE OF THE EVIDENCE, not the builder's
    own diligence this session - so it is not itself a defect for every
    linked source to fall short of verified-direct. What IS a defect is
    for that gap to go unnamed: if NONE of the record's own sources[]
    carry confidence.verification_state == 'verified-direct', the record
    must carry its own confidence.divergence_note, on Doc_04's own
    pattern, or this gate flags it.

    A record with an empty (or absent) sources[] is skipped - that is
    gate_field_completion's finding (a term/story/etc. missing sources
    entirely) or referential_integrity's (a dangling source_id), not a
    divergence to name here. A single verified-direct source is enough
    to clear the check for the whole record (Doc_04's own worked cases
    clear on a single strong stream, not unanimity)."""
    out = []
    for rid, r in records.items():
        conf = r.get("confidence") or {}
        if conf.get("formation_confidence") != "Documented":
            continue
        source_ids = [link.get("source_id") for link in r.get("sources") or []
                      if link.get("source_id")]
        if not source_ids:
            continue
        states = {sid: _get_dotted(records.get(sid) or {}, "confidence.verification_state")
                  for sid in source_ids}
        if any(state == "verified-direct" for state in states.values()):
            continue  # at least one linked source is verified-direct - no divergence to flag
        if not conf.get("divergence_note"):
            out.append(
                f"{rid}: confidence.formation_confidence=Documented but none of its "
                f"{len(source_ids)} linked source(s) carry verification_state="
                f"verified-direct ({states}) and no confidence.divergence_note is "
                f"recorded - the Doc_04 Confidence/Gravity Cross-Check's own "
                f"record-level analogue"
            )
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


# ------------------------------------------------------- mechanism coverage


def gate_mechanism_coverage(records: dict) -> list:
    """Tier 3, T3-B: does this world carry what its runtime mechanisms read?

    Every other gate here validates the records that EXIST. None of them
    asks whether the records a runtime mechanism depends on exist at all,
    and that gap is measurable: across the six built worlds, five of twelve
    (world x Tier-2 check) cells have a check running with nothing to check
    against, pahc has both inert, and every gate reported green throughout.
    Correctly - a world with no quote records has no quote record to fail.
    This gate closes that specific hole and nothing else.

    Reads its dependency list from mechanism_dependencies.py (T3-A), which
    is deliberately NOT part of this package: declaring a new mechanism is
    an ordinary change, while changing this gate's behaviour is bound by
    the gate-integrity rule at the top of this file.

    ADVISORY, by Mark's decision 2026-08-15: every finding here is emitted
    behind _NOTE_PREFIX, so it prints in full but never enters the
    runner's violation TOTAL. That decision is encoded here rather than
    left to the runner's current always-exit-0 behaviour on purpose - the
    moment anything gives the runner teeth, a finding sitting in the
    ordinary violation count would become blocking by default and silently
    reverse the decision. Promoting coverage to blocking is therefore a
    one-line change AT THIS GATE, made deliberately, when a floor exists to
    promote it against.

    REPORTS ZERO-COVERAGE ONLY. A dependency satisfied by even one record
    passes here, even at 1-of-12: no floor has been set, and inventing one
    inside a gate would be exactly the "assume the threshold" move the
    completion standard's own SS D refuses ("thresholds set only once real
    baselines exist"). Floors are a separate, later decision made from this
    gate's own numbers - see coverage_report.py for the fleet view those
    numbers come from.

    Distinguishes the two zero cases, because they call for different work:
    no records of the type at all (author some) versus records that exist
    but none carrying the needed content (fill a field in).

    Fails CLOSED on its own import error, unlike the gloss loader's fail-
    open above. A coverage gate that reports green when it could not run is
    the precise defect it exists to catch.
    """
    try:
        from mechanism_dependencies import coverage
    except Exception as exc:  # noqa: BLE001
        # NOT advisory - this one is a real violation. The gate being unable
        # to run is a defect in the gate, not a coverage shortfall in a
        # world, and it must not be filed under the same "known, accepted"
        # heading as the findings it exists to report.
        return [f"mechanism_dependencies.py could not be loaded ({exc!r}) - "
                f"coverage is UNKNOWN, not green"]

    out = []
    for dep, n_satisfying, n_of_type in coverage(records):
        if n_satisfying:
            continue
        if n_of_type == 0:
            shortfall = (f"no {dep.record_type} records exist for this world "
                         f"at all")
        else:
            shortfall = (f"0 of {n_of_type} {dep.record_type} record(s) carry "
                         f"{dep.requirement}")
        out.append(
            f"{_NOTE_PREFIX} {dep.label}: {shortfall} - the mechanism runs "
            f"and cannot function. Inert-{dep.inert_mode}: "
            f"{dep.inert_consequence} [reads {dep.record_type}.{dep.field}]"
        )
    return out


# ---------------------------------------------------------- texts registry


def gate_texts_registry(records: dict) -> list:  # noqa: ARG001 - see below
    """Does cic/texts/ (the vendored public-domain reference corpus) match
    what texts_registry.py's ENTRIES declares it should?

    IGNORES `records` ENTIRELY, unlike every other gate here - a deliberate
    choice, not an oversight, and the one thing about this gate worth
    reading before touching it. This is a hygiene check on a directory of
    vendored TEXT FILES and a Python-level manifest (texts_registry.ENTRIES),
    neither of which any single world's own record set determines. The
    per-world `records` argument the runner always passes exists to keep
    this gate's call signature uniform with the other eleven, nothing more.

    ONE CONSEQUENCE OF IGNORING records worth naming explicitly, so a future
    reader of gate_baseline.json is not confused by it: because this check
    is fleet-wide and does not vary by world, it returns the SAME violation
    count for every world in a single --check run. That is correct, not a
    bug - a torn rights line or an unregistered file is equally true
    regardless which world's report you happen to be reading, and the
    redundancy means a regression here trips every world's ratchet at once
    rather than hiding in whichever world nobody happened to check.

    THREE checks, not four - see texts_registry.registry_problems' own
    docstring for the reasoning. In short: a declared-but-missing file, an
    undeclared-but-present file, and an unverifiable rights line are real
    mistakes with a knowable right answer. Whether a vendored volume has
    been cited by anything YET is not a mistake, and is deliberately kept
    out of this gate for the same reason mechanism_coverage refuses to
    invent a coverage floor - it stays in texts_registry.py's own report()
    as information, never a violation here.

    REGULAR, not advisory - the one deliberate difference from
    mechanism_coverage worth naming, not an inconsistency. mechanism_coverage
    is advisory because it describes PRE-EXISTING gaps this session found
    already sitting in the six worlds' own records - debt to surface, not
    something to block on immediately. This gate describes something with a
    genuinely clean baseline as of the day it was written: zero problems,
    verified. There is no legacy debt to grandfather here, so a violation
    is new, current-moment state (someone vendored a file and forgot to
    register it, or a header's rights line doesn't say what was claimed) -
    exactly the shape of thing this package's other gates already block on
    without ceremony.

    Fails CLOSED on its own error, matching mechanism_coverage's own
    precedent: a hygiene check that cannot run is a defect in the check,
    not a clean pass.
    """
    try:
        from texts_registry import registry_problems_live
        return registry_problems_live()
    except Exception as exc:  # noqa: BLE001
        return [f"texts_registry.py could not be loaded/run ({exc!r}) - "
                f"cic/texts/ state is UNKNOWN, not clean"]
