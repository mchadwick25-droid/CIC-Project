"""Deterministic builders: records -> the compiled/ half of a World Package
(Artifact-2 SS1). Every function here is pure - same records in, same bytes
out, no wall clock, no randomness, no network. Content-only; the
`generated-by` header stamping (Artifact-2 SS3) happens once, centrally, in
compiler.py, so it doesn't have to be threaded through every function here.
"""
import hashlib
import re

from engine.m1 import canon
from engine.prose import DEMONSTRATION_TAG_FLOOR, content_words, quote_aware_sentences

from .canonical import canonical_json

CHUNK_DIR_BY_TYPE = {
    "term": "lexicon",
    "story": "story",
    "ambient": "ambient",
    "doctrinal_witness": "doctrinal_witness",
}


def _by_type(records: dict, record_type: str) -> list[dict]:
    return sorted((r for r in records.values() if r.get("record_type") == record_type), key=lambda r: r["id"])


def _one(records: dict, record_type: str) -> dict | None:
    hits = _by_type(records, record_type)
    return hits[0] if hits else None


# ---- compiled/prompt.txt ----------------------------------------------

# LIVE-GENERATION-DESIGN.md §5.2: the fleet's one register/pronoun/
# citation-contract/limit-discipline segment, compiled from the fleet's
# own fleet_voice record (records/_fleet/fleet_voice/) rather than
# hand-edited per world (principle 3: prompt content is records, never
# code) - first in the file, so it reads as the voice's own standing
# instruction, ahead of any one world's own identity.
def _fleet_voice_record(fleet: dict) -> dict | None:
    return _one(fleet, "fleet_voice")


# The citation contract's worked example ships PLACEHOLDER ids, and the fleet
# record says so itself: they exist "only so citation_contract is a complete,
# self-explanatory paragraph on its own - never the line a model is actually
# shown", with the per-world substitution named there as open M2 work. It was
# never implemented, so all seven packages shipped the literal token `world`
# into live model input - and a model reads that as the namespace, emitting
# world.story.pliny-interrogation, world.term.hesychia: right shape, no such
# record, sentence withheld. Filled from the world's own records, exactly as
# `{world}` in pronoun_rule already is.
def _fill_citation_example(contract: str, records: dict) -> str:
    for placeholder in ("world.term.example", "world.gravity.example"):
        if f"[[{placeholder}]]" not in contract:
            continue
        wanted = placeholder.split(".")[1]
        ids = sorted(r["id"] for r in records.values() if r.get("record_type") == wanted) or sorted(
            r["id"] for r in records.values() if r.get("record_type") != "demonstration"
        )
        real = next((i for i in ids if f"[[{i}]]" not in contract), None)
        # A placeholder with no substitute is dropped, never shipped: an absent
        # second tag still reads as a correct worked line; an unresolvable one
        # teaches a fabrication.
        contract = (contract.replace(f"[[{placeholder}]]", f"[[{real}]]") if real
                    else contract.replace(f" [[{placeholder}]]", "").replace(f"[[{placeholder}]]", ""))
    return contract


def build_fleet_preamble(fleet: dict, registry_entry: dict, records: dict | None = None) -> list[str]:
    """Returns the preamble's own emitted segments (already `## Header`-
    formatted, same shape build_prompt's other segments use) - a list, not
    bytes, so build_prompt can splice it in front of everything else with
    no format translation. Empty list (not an error) when the fleet record
    doesn't exist yet, or hasn't cleared its completion gate - a package
    can still compile without it, same as any other not-yet-required field.

    The pronoun rule's `{world}` placeholder is filled from this world's
    own registry `display_name` - real, already-existing registry data,
    never a fresh, hand-composed-per-world phrase (the fleet record's own
    trailing body names this exact substitution as the compiler's call to
    make; using the registry's own name field, rather than inventing a new
    poetic epithet per world, keeps the fill mechanical and DECIDABLE)."""
    record = _fleet_voice_record(fleet)
    if record is None:
        return []

    segments: list[str] = []

    def emit(header: str, body: str | None) -> None:
        if body and body.strip():
            segments.append(f"## {header}\n\n{body.strip()}\n")

    statements = sorted(record.get("register_statements") or [], key=lambda s: s["number"])
    if statements:
        body = "\n".join(f"{s['number']}. {s['statement']}" for s in statements)
        # register_hold: how the seven hold under load (Mark-approved
        # wording, 2026-08-28 register & reach pass) - emitted beneath the
        # numbered statements, never as an eighth statement.
        hold = (record.get("register_hold") or "").strip()
        if hold:
            body = f"{body}\n\n{hold}"
        emit("Register", body)

    world_name = registry_entry.get("display_name") or "this world"
    pronoun_rule = record.get("pronoun_rule")
    if pronoun_rule:
        emit("Pronoun rule", pronoun_rule.replace("{world}", world_name))

    emit("Citation contract", _fill_citation_example(record.get("citation_contract") or "", records or {}))
    emit("Limit discipline", record.get("limit_discipline"))
    return segments


# Demonstration citation tagging (LIVE-GENERATION-DESIGN.md §5.3): demos
# are rendered "with citation tags derived from the demonstration record's
# own sources field" per the design's own words - but a real-record check
# (M4 step 4) found `sources` points to bibliographic editions, never to
# the repository records (term/witness/gravity/quote) a demo actually
# draws on, so that field can't drive tagging as written. This is the
# direct alternative the design itself recommends elsewhere for exactly
# this shape of gap (§3.2: "score them directly off their compiled record
# JSON rather than adding a chunk directory") - applied here to demo
# sentences instead of live evidence candidates. Deterministic, no model
# call, same floor/splitter/overlap metric the live net polices turns
# with (engine.m1.gates_experimental), so a demo that would pass its own
# net if it were live output is exactly the demo that gets tagged here -
# and a sentence that can't clear the floor against anything in its own
# cell gets NO tag, same as a connective/interpretive sentence always
# would, never a forced or guessed one.
_DEMO_CANDIDATE_TYPES = {"doctrinal_witness", "term", "story", "quote", "honest_limit", "gravity", "force", "contested_claim"}


def _demonstration_candidates(records: dict, demo: dict) -> list[dict]:
    cells = set(demo.get("canon_cells") or [])
    if not cells:
        return []
    seen: dict[str, dict] = {}
    for record in records.values():
        if record.get("record_type") in _DEMO_CANDIDATE_TYPES and cells & set(record.get("canon_cells") or []):
            seen[record["id"]] = record
    return list(seen.values())


def _candidate_head_text(record: dict) -> str:
    """The same compiled-facing text this record contributes elsewhere in
    build_prompt/build_chunks - never the trailing analytical/provenance
    body. Scoring against the FULL record (engine.m1.gates_experimental's
    own all_text, what overlap_coefficient and the live net's own ratio
    check both use) is fine for ranking already-cell-scoped candidates
    (engine.m4.evidence's job - a slightly imprecise ranking there never
    asserts a false citation) but proved too permissive here on real data:
    a short demo sentence can share 2 merely-common words with a large
    record's own review/history prose and clear the floor by coincidence.
    Demo tags ARE asserted ground truth in the compiled prompt's own
    highest-leverage teaching surface, so scoring is scoped tighter here,
    on purpose, to exactly what a participant (or a live model reading its
    own prompt) would ever actually see this record say."""
    record_type = record.get("record_type")
    if record_type == "term":
        return " ".join(filter(None, [record.get("plain_meaning"), record.get("quick_meaning")]))
    if record_type == "story":
        return " ".join(filter(None, [record.get("tellable_as"), record.get("text")]))
    if record_type in ("quote", "doctrinal_witness"):
        return record.get("text") or ""
    if record_type == "honest_limit":
        return record.get("statement") or ""
    if record_type in ("gravity", "force"):
        return record.get("description") or ""
    if record_type == "contested_claim":
        return record.get("claim") or ""
    return ""


# A ratio floor alone can be cleared by a short sentence sharing just one
# or two very common words with a large candidate's own head text (found
# against real data: a 5-word martyrdom sentence scored 40% against an
# unrelated term purely on "name"/"cost" overlap in the term's own head
# text). Requiring at least this many REAL shared words too is a second,
# independent gate a coincidence can't clear by ratio alone - the same
# belt-and-suspenders discipline grounding_net's own quote-verbatim check
# uses (a ratio pass never overrides a structural check).
#
# MEASURED, and raised from 2 to 3 on that measurement. Over all 444
# representative sentences in the 50 demonstration records, at the
# shipping floor:
#
#     shared words   tags   on-provenance
#          2          24         67%
#          3          17         94%
#         4-5         41         90%
#         6-9         58         91%
#         10+         67         90%
#
# The two-word bucket is the only one that underperforms, and reading all
# 24 of its tags shows the 67% is generous: the ones the provenance proxy
# counts as correct are no better than the ones it counts as wrong, since
# any two-word sentence will coincidentally hit one of the handful of
# records a demonstration names. What is actually in that bucket is
# scaffolding, questions and list fragments being handed citations -
# "We do not resolve that for you now; our own record never did." tagged
# to a force record on {never, record}; "We are not going to pretend to
# you now that we did." tagged to a martyrdom story on {going, now}.
#
# These go into the PROMPT as worked examples of a correctly cited turn,
# so a wrong tag teaches the live model to attach citations to framing.
# The floor beside it cannot reach these at all, because a two-content-word
# sentence scores ratio 1.00 whenever both its words appear anywhere in a
# candidate - only a shared-word count can.
#
# At 3 the demonstration corpus keeps 190 tags of the 214 it carried at 2,
# and on-provenance rises from 88% to 91%. Every one of the 24 dropped
# tags rested on exactly two shared words.
_MIN_SHARED_WORDS = 3


def _tag_representative_text(text: str, candidates: list[dict]) -> str:
    candidate_words = [(record["id"], content_words(_candidate_head_text(record))) for record in candidates]
    tagged: list[str] = []
    for sentence in quote_aware_sentences(text):
        words = content_words(sentence)
        best_id, best_ratio, best_shared = None, 0.0, 0
        for record_id, record_words in candidate_words:
            if not words or not record_words:
                continue
            shared = words & record_words
            ratio = len(shared) / min(len(words), len(record_words))
            if ratio > best_ratio:
                best_ratio, best_id, best_shared = ratio, record_id, len(shared)
        if best_id and best_ratio >= DEMONSTRATION_TAG_FLOOR and best_shared >= _MIN_SHARED_WORDS:
            # BEFORE the terminal punctuation, per the citation contract's own
            # words: "so a sentence-boundary split can never break inside one."
            # engine.m4.grounding_net splits on (?<=[.!?])\s+, so a tag after
            # the stop is carried onto the NEXT sentence - grounding a claim it
            # never came from and leaving its own claim untagged and withheld.
            cut = max(sentence.rfind(m) for m in ".!?")
            tagged.append(
                f"{sentence} [[{best_id}]]" if cut < 0
                else f"{sentence[:cut]} [[{best_id}]]{sentence[cut:]}"
            )
        else:
            tagged.append(sentence)
    return " ".join(tagged)


def _quote_speaker(quote: dict) -> str:
    """speaker_or_author is sometimes a figure id and sometimes prose - the
    corpus holds both alx.figure.athanasius and "The Council of Chalcedon
    (451), Canon 28". Show the readable half of either."""
    raw = (quote.get("speaker_or_author") or "").strip()
    if not raw:
        return "unattributed"
    if re.fullmatch(r"[a-z0-9_]+\.[a-z0-9_]+\.[a-z0-9-]+", raw):
        return raw.rsplit(".", 1)[-1].replace("-", " ")
    return raw if len(raw) <= 70 else raw[:67].rstrip() + "..."


def _quote_opening(quote: dict, width: int = 60) -> str:
    text = " ".join((quote.get("text") or "").split())
    return f'"{text}"' if len(text) <= width else f'"{text[:width].rstrip()}..."'


# THE PROMPT HAS TWO HALVES, and until now only one of them was named.
#
# One half is records of the world, each section addressed by an id the
# voice copies when it draws on that section. The other is standing
# instruction - the fleet's own register/pronoun/citation/limit segment -
# which carries no ids, needs none, and has never had one invented for it:
# nobody has ever seen [[fleet.voice.register]] in a live turn.
#
# Both regions existed already. What did not exist was any statement of
# where one stopped and the other began: the boundary was wherever
# build_fleet_preamble's output happened to end, and nothing on the page
# said so. voice_craft - the voice's own identity, guard, concerns and
# flavor notes, which are instruction about how we speak, not evidence
# about the world - sat on the wrong side of that unnamed boundary, and was
# given an id so the model would stop inventing one.
#
# This constant is the boundary, written out. It replaces the id that
# voice_craft was carrying; see the fabrication history on emit() below for
# what that id cost and why it was reached for, and instruct() for why
# moving the content is a better answer than keeping the id.
#
# The wording is the lesson of the adjacency failure, run the other way.
# Printing an id beside a heading told a model the id existed without
# telling it what the id addressed, and the model kept inventing. Omitting
# an id tells a model nothing at all about why it is missing. So the
# absence is stated, and what to do instead is stated with it: a claim
# about the world that we happen to have met in our own instruction is
# carried by the record that holds it, from below the line or from the
# turn's ground - never by an address for the instruction.
_GROUND_LINE = """## Below this line is our world's own record

Everything above this line is our own standing instruction - our register, our
pronouns, who we are, what we hold ourselves to, what we keep returning to,
how we word things. It is how we speak, not something we know about the world.
It carries no record id because it is not a record of anything, and no id is
ever written for it: a sentence about ourselves carries no tag at all.

Everything below this line is our world's own record, and so is the ground
given with each turn. Each of those carries its own id - printed in the
section's heading, or beside each entry in a list - and a claim drawn from one
carries that id, copied exactly. Where something above the line is a claim
about the world - a person, a place, a date, how much of our own record
survives - the record that holds it is below the line or in this turn's
ground, and it is that id which is copied.
"""


def build_prompt(records: dict, fleet: dict, registry_entry: dict) -> bytes:
    # Two lists, spliced at the end with _GROUND_LINE between them, because
    # the halves are no longer interleaved: voice_craft's four sections used
    # to be emitted around world_core's four, and a reader (or a model) had
    # nothing to tell instruction from record but the prose itself.
    standing: list[str] = build_fleet_preamble(fleet, registry_entry, records)
    ground: list[str] = []

    # A STANDING-INSTRUCTION SECTION NEVER CARRIES AN ID. Same two-argument
    # shape build_fleet_preamble's own emit() has always had, and for the
    # same reason - there is no third argument to pass, because there is no
    # address for content that is not a record of the world.
    #
    # This is where voice_craft now compiles. Every voice_craft record in the
    # fleet carries `sources: []` on purpose (spec principle 14: a
    # Representative's name, role and manner of speaking are the build's one
    # sanctioned fabrication), so "(cite as [[<world>.voice.craft]])" was an
    # instruction to produce a citation that can never resolve to a source -
    # and a live M3 admission probe produced exactly that, [[desert.voice.craft]]
    # on f3-t-probe-01 ("Was your church 'Catholic'? Is there a church today I
    # could visit that's yours?" - a question about the voice itself, which is
    # the shape that reaches for this material).
    #
    # WHY THIS DOES NOT REOPEN THE FABRICATION THE ID WAS SUPPRESSING. The
    # measurement below reads as "sections without an id fabricate", but the
    # fleet preamble was in that same prompt, four sections deep, with no id
    # and plain-noun headings ("Register", "Limit discipline"), and it
    # contributed nothing to the table - build_fleet_preamble landed in
    # 4994ff0, before the run 4909dd1 measured. So id-presence was never the
    # discriminator. What fabricated was material the model read as ground it
    # owed an address for; what did not was material it read as instruction
    # about how to speak. voice_craft is the second kind and was filed with
    # the first.
    #
    # And the headings are phrased as clauses in the voice's own we-form, not
    # as the plain nouns "Identity", "Guard", "Characteristic concerns",
    # "Flavor notes". That is the adjacency finding's own diagnosis applied
    # directly - "a heading which is a plain noun still reads as a namespace
    # of its own", and "Identity" was in fact one of the three headings that
    # produced invented ids. "Who we are" cannot be read as an id segment;
    # id segments are single lowercase tokens.
    #
    # Nothing on the checking side changes. A sentence about ourselves that
    # names nobody and counts nothing already passes the live net as
    # interpretive framing; the two first-person lines that must be speakable
    # with no ground at all - the honesty scaffolding and "I am a
    # representative of ..." - are already exempt by literal marker, because
    # the fleet contract teaches those verbatim. A sentence that DOES carry a
    # claim marker is by definition naming a person, place, text or number,
    # which is a claim about the world, and the record that holds it is below
    # the line or in the turn's ground. There is no third category needing a
    # new exemption.
    def instruct(header: str, body: str | None) -> None:
        if body and body.strip():
            standing.append(f"## {header}\n\n{body.strip()}\n")

    # EVERY SECTION CARRIES THE ID OF THE RECORD IT CAME FROM, in the exact
    # [[id]] form the citation contract asks the voice to write. Measured on
    # a six-turn live conversation with desert: 14 of 47 tag uses pointed at
    # records that do not exist, and the split was almost perfectly along
    # this line -
    #
    #   type      real  invented   id was in its header?
    #   story       13         0   yes
    #   term        11         0   yes (world_word, id as fallback)
    #   demo         1         0   yes
    #   dw           1         6   no  - "Witness (F1-I)"
    #   gravity      5         3   no
    #   identity     0         2   no  - "Identity"
    #   thinness     0         2   no  - "Thinness"
    #   caution      0         1   no  - "Cautions"
    #
    # The invented ids were built out of the headers themselves: a section
    # headed "Thinness" produced [[desert.thinness.womens-first-person]], one
    # headed "Cautions" produced [[desert.caution.single-voice-concentration]],
    # and desert has neither record type. Six of the seven invented ids
    # pointed at prose that IS in this prompt - the voice was grounded and
    # could not name its ground, so it constructed an address from the only
    # label it had been given.
    #
    # engine.m4.evidence.render_evidence_block already does this for the
    # per-turn candidates ("- [[id]] type, ... - head") and its own docstring
    # says why: "this block and the model's own tags share one id vocabulary
    # by construction." The cached prefix did not, and the turn that got no
    # evidence block at all (44 input tokens, turn 1) fabricated the most.
    #
    # ADJACENCY WAS NOT ENOUGH, measured again on the same six-turn shape
    # 2026-08-27 against a package where every canon cell had a voice.
    # Fabrication fell from 14 uses in 47 to 2 in 27 - but both survivors
    # were [[desert.cautions]], emitted from the section headed "Cautions",
    # which by then DID carry [[desert.core.desert]] beside it. The earlier
    # invention had been a full three-segment address
    # ([[desert.caution.single-voice-concentration]]); what was left was the
    # bare namespace. So printing the id next to the heading tells a model
    # the id exists; it does not tell it that THIS heading is addressed by
    # THAT id, and a heading which is a plain noun still reads as a
    # namespace of its own. The four world_core sections make it worst:
    # four different headings, one repeated id, and nothing on the page
    # saying they are fields of one record.
    #
    # So the heading states the relation instead of implying it. "(cite as
    # [[id]])" is an instruction where " [[id]]" was an adjacency, and it
    # costs four words a section.
    #
    # This treatment is now scoped to what it was always FOR: sections that
    # are records of the world. It no longer reaches the voice's own craft
    # material, which goes through instruct() above.
    def emit(header: str, body: str | None, record_id: str | None = None) -> None:
        if body and body.strip():
            head = f"{header} (cite as [[{record_id}]])" if record_id else header
            ground.append(f"## {head}\n\n{body.strip()}\n")

    # The four voice_craft fields, together, above the line - not split around
    # world_core's four the way they used to be. Grouping them is half the
    # point: four contiguous sections in the voice's own we-form, in the same
    # run as the register and the pronoun rule, read as one block of standing
    # instruction. Interleaved with Horizon and Cautions they read as content.
    craft = _one(records, "voice_craft")
    if craft:
        instruct("Who we are", craft.get("identity"))
        instruct("What we hold ourselves to", craft.get("guard"))
        concerns = craft.get("characteristic_concerns") or []
        if concerns:
            instruct("What we keep returning to", "\n".join(f"- {c}" for c in concerns))
        notes = craft.get("flavor_notes") or []
        if notes:
            instruct(
                "How we word things",
                "\n".join(f"- [{n.get('segment')}] {n.get('note')}" for n in notes),
            )

    core = _one(records, "world_core")
    if core:
        # four sections, one record - they are all fields of world_core, and
        # saying so is what stops "Formation logic" becoming a namespace.
        emit("Horizon", core.get("horizon"), core["id"])
        emit("Formation logic", core.get("formation_logic"), core["id"])
        emit("Thinness", core.get("thinness"), core["id"])
        emit("Cautions", core.get("cautions"), core["id"])

    for term in _by_type(records, "term"):
        body = "\n\n".join(filter(None, [term.get("plain_meaning"), term.get("quick_meaning")]))
        emit(f"Term: {term.get('world_word', term['id'])}", body, term["id"])

    for witness in _by_type(records, "doctrinal_witness"):
        cells = ",".join(witness.get("canon_cells") or [])
        emit(f"Witness ({cells})", witness.get("text"), witness["id"])

    for limit in _by_type(records, "honest_limit"):
        cells = ",".join(limit.get("canon_cells") or [])
        emit(f"Honest limit ({cells})", limit.get("statement"), limit["id"])

    # Gravities carry their own id for the same measured reason every other
    # section now does. After the header change above, desert's fabrication
    # rate halved (30% -> 14%) and every remaining invented id was a gravity:
    # the model had the concept and the right type and was guessing the slug -
    # [[desert.gravity.evagrian-psychology]] for the record actually named
    # evagrian-systematization ("Evagrian systematized interior psychology"),
    # [[desert.gravity.disciple-elder-bond]] for elder-authority
    # ("Elder-mediated oral authority").
    #
    # A gravity reaches the voice two ways and neither named all of them: as
    # narrative prose folded into Horizon/Formation logic/Identity, which
    # carried no id at all, and as an evidence candidate, of which M4 offers
    # at most two per turn (engine.m4.evidence._PER_TYPE_CAP) out of desert's
    # ten. So the voice met eight unnamed gravities in the prefix and built
    # addresses for them out of their names.
    #
    # The name is emitted with the description because it carries the
    # classification the voice needs anyway - "[PRIMARY]", "[TENSIONAL]".
    # This does not change what a gravity IS for the admission gate: they stay
    # analytical, out of substantive_types(), exactly as _ANALYTICAL_TYPES
    # below sets out. Naming a record is not promoting it.
    gravities = _by_type(records, "gravity")
    if gravities:
        emit(
            "Gravities",
            "\n".join(f"- [[{g['id']}]] {g.get('name')}" for g in gravities),
        )

    # Quotes are indexed, not reproduced. Both fabrications in the last
    # 36-turn fleet run were quote ids the voice invented while reaching for
    # a real record - [[ijc.quote.leo-two-natures]] for the record actually
    # named leo-tome-each-form ("He who is true God is also true man"), which
    # IS Leo on the two natures. Right content, guessed slug, the same
    # failure the section-naming and gravity-index changes already measured
    # and closed for every other citable type. Quote was the last one left:
    # 16 named of 87 across the fleet.
    #
    # An id and a speaker are not enough to pick one. 13 of alx's 14 quotes
    # share a speaker with another, and 15 of hal's 19 - "jerome" names
    # sixteen different records. So each entry carries its opening words,
    # which is what makes the index usable and what costs it 1-4% of the
    # prefix; reproducing every quote in full costs 4-16% (ijc 15.8%) and
    # duplicates what the per-turn evidence block already delivers, with the
    # full text, for the quotes a turn actually needs.
    #
    # The opening words are labelled as an opening. A voice that quotes
    # beyond them is caught by the verbatim check the citation contract
    # already runs ("a quote with no tag, or words not found in the tagged
    # record, is not spoken") - so the cost of the excerpt is a withheld
    # sentence, never a misquotation reaching a participant.
    quotes = _by_type(records, "quote")
    if quotes:
        emit(
            "Quotes we hold (opening words only - the full text arrives with the turn's ground)",
            "\n".join(
                f"- [[{q['id']}]] {_quote_speaker(q)}: {_quote_opening(q)}" for q in quotes
            ),
        )

    for story in _by_type(records, "story"):
        body = "\n\n".join(filter(None, [story.get("tellable_as"), story.get("text")]))
        emit("Story", body, story["id"])

    for demo in _by_type(records, "demonstration"):
        exchange = demo.get("exchange") or []
        candidates = _demonstration_candidates(records, demo)
        lines = []
        for turn in exchange:
            text = turn["text"]
            if turn.get("speaker") == "representative" and candidates:
                text = _tag_representative_text(text, candidates)
            lines.append(f"{turn['speaker']}: {text}")
        emit("Demonstration", "\n".join(lines), demo["id"])

    # The line is a boundary, so it is only written where there are two sides
    # to divide. A prompt with no standing instruction at all (a bare-records
    # unit fixture, never a real compile - every world loads the fleet record)
    # would otherwise open with a paragraph about material above it that is
    # not there.
    segments = standing + ([_GROUND_LINE] + ground if standing and ground else ground)
    return ("\n".join(segments) + "\n").encode("utf-8")


# ---- compiled/capsule.md ------------------------------------------------


def build_capsule(records: dict, registry_entry: dict) -> bytes:
    core = _one(records, "world_core") or {}
    rep = registry_entry.get("representative") or {}
    window = registry_entry.get("time_window") or {}
    lines = [
        f"# {registry_entry.get('display_name', '')}",
        "",
        f"Representative: {rep.get('name', '')} ({rep.get('role_label', '')})",
        f"Time window: {window.get('start')}-{window.get('end')}",
        f"Place: {registry_entry.get('place', '')}",
        "",
        "## Thinness",
        registry_entry.get("thinness_statement", ""),
        "",
        "## Cautions",
        core.get("cautions", ""),
    ]
    return ("\n".join(lines) + "\n").encode("utf-8")


# ---- compiled/chunks/{lexicon,story,ambient,doctrinal_witness}/*.md ----
# Artifact-2 SS1 names chunks/{lexicon,story,ambient}/ explicitly; Artifact-1
# SS3 lists doctrinal_witness as a fourth chunk-feeding (retrieval-block)
# type. Adding a fourth directory that follows the same one-file-per-record
# pattern is the minimal, fully-determined resolution of that gap - DECIDABLE
# (Build-Blueprint.md SS4), not a spec contradiction needing Mark's input.


def _chunk_text(record: dict) -> str:
    record_type = record["record_type"]
    lines = [f"id: {record['id']}", f"canon_cells: {','.join(record.get('canon_cells') or [])}", ""]
    if record_type == "term":
        lines += [record.get("plain_meaning", ""), "", f"world_word: {record.get('world_word', '')}", "", record.get("quick_meaning", "")]
    elif record_type == "story":
        lines += [record.get("tellable_as", ""), "", record.get("text", "")]
    elif record_type == "ambient":
        lines += [record.get("detail", "")]
    elif record_type == "doctrinal_witness":
        lines += [record.get("text", "")]
    return "\n".join(lines) + "\n"


def build_chunks(records: dict) -> dict[str, bytes]:
    out = {}
    for record in records.values():
        record_type = record.get("record_type")
        chunk_dir = CHUNK_DIR_BY_TYPE.get(record_type)
        if chunk_dir is None:
            continue
        out[f"compiled/chunks/{chunk_dir}/{record['id']}.md"] = _chunk_text(record).encode("utf-8")
    return out


# ---- compiled/indexes/{lexicon,story}.faiss -----------------------------
# DECIDABLE placeholder (recorded in the stage-2 commit): a real semantic
# embedding requires a model/provider choice, which spec principle 11 rules
# lands last and alone - not smuggled into compiler infrastructure ahead of
# M4 (stage 5). This is a deterministic, hash-derived pseudo-vector purely so
# the .faiss file/hash pipeline is exercised end-to-end now; it carries no
# semantic meaning and says so in its own "format" field.


def _pseudo_vector(text: str, dim: int = 8) -> list[float]:
    digest = hashlib.sha256((text or "").encode("utf-8")).digest()
    return [digest[i % len(digest)] / 255 for i in range(dim)]


def _index_blob(entries: list[dict]) -> bytes:
    return canonical_json(
        {
            "format": "cic-m2-placeholder-index-v1",
            "dim": 8,
            "note": (
                "deterministic hash-derived placeholder, NOT a semantic embedding - "
                "real retrieval vectors are an M4/stage-5 decision (spec principle 11: "
                "model/provider switches land last and alone)"
            ),
            "entries": entries,
        }
    )


def build_indexes(records: dict) -> dict[str, bytes]:
    lexicon_entries = [
        {"id": r["id"], "vector": _pseudo_vector((r.get("plain_meaning") or "") + (r.get("quick_meaning") or ""))}
        for r in _by_type(records, "term")
    ]
    story_entries = [
        {"id": r["id"], "vector": _pseudo_vector(r.get("text") or "")} for r in _by_type(records, "story")
    ]
    return {
        "compiled/indexes/lexicon.faiss": _index_blob(lexicon_entries),
        "compiled/indexes/story.faiss": _index_blob(story_entries),
    }


# ---- compiled/quotes.json, figures.json, repository.json ----------------


def build_quotes_json(records: dict) -> bytes:
    quotes = [
        {
            "id": q["id"],
            "text": q.get("text"),
            "speaker_or_author": q.get("speaker_or_author"),
            "license": q.get("license"),
            "canon_cells": q.get("canon_cells") or [],
            "sources": q.get("sources") or [],
        }
        for q in _by_type(records, "quote")
    ]
    return canonical_json({"quotes": quotes})


def build_figures_json(records: dict) -> bytes:
    figures = [
        {
            "id": f["id"],
            "names": f.get("names") or [],
            "dates": f.get("dates") or {},
            "narratable": f.get("narratable"),
            "bridge_line": f.get("bridge_line"),
        }
        for f in _by_type(records, "figure")
    ]
    return canonical_json({"figures": figures})


def build_repository_json(records: dict) -> bytes:
    entries = [
        {k: v for k, v in record.items() if not k.startswith("_")}
        for record in sorted(records.values(), key=lambda r: r["id"])
    ]
    return canonical_json({"records": entries})


# ---- compiled/coverage.json ----------------------------------------------

# Analytical record types eligible for the per-cell "analytical" list below.
# Deliberately NOT passed through canon.classify_cell / substantive_types():
# that function is the single spec-mandated implementation of Artifact-1
# SS6's coverage rule ("every open world has >=1 doctrinal_witness/term/
# story/quote OR exactly one honest_limit per cell") - an admission-gate
# question. Whether a gravity/force/contested_claim record can retrieval-
# ground a turn is a different question (M4's evidence assembly, not M1
# admission), and folding these three types into substantive_types() would
# silently let a cell pass SS6 coverage on analytical material alone,
# changing what the gate means. So they get their own field, computed the
# same way (canon_cells membership) but never touching "status" or
# "substantive".
_ANALYTICAL_TYPES = {"gravity", "force", "contested_claim"}


def build_coverage_json(records: dict, fleet: dict) -> bytes:
    out = {}
    for cell in sorted(canon.valid_cells(fleet)):
        classification = canon.classify_cell(cell, records)
        substantive_ids = classification["substantive"]
        figures = sorted(
            {
                records[rid]["speaker_or_author"]
                for rid in substantive_ids
                if records[rid].get("record_type") == "quote" and records[rid].get("speaker_or_author")
            }
        )
        analytical_ids = sorted(
            rid
            for rid, r in records.items()
            if r.get("record_type") in _ANALYTICAL_TYPES and cell in (r.get("canon_cells") or [])
        )
        out[cell] = {
            "status": classification["status"],
            "terms": [rid for rid in substantive_ids if records[rid]["record_type"] == "term"],
            "stories": [rid for rid in substantive_ids if records[rid]["record_type"] == "story"],
            "quotes": [rid for rid in substantive_ids if records[rid]["record_type"] == "quote"],
            "doctrinal_witness": [rid for rid in substantive_ids if records[rid]["record_type"] == "doctrinal_witness"],
            "figures": figures,
            "honest_limit": classification["honest_limit"],
            "gravities": [rid for rid in analytical_ids if records[rid]["record_type"] == "gravity"],
            "forces": [rid for rid in analytical_ids if records[rid]["record_type"] == "force"],
            "contested_claims": [rid for rid in analytical_ids if records[rid]["record_type"] == "contested_claim"],
        }
    return canonical_json(out)


# ---- compiled/indexes/canon-map.json --------------------------------------
# LIVE-GENERATION-DESIGN.md §3.2, Stage A's own compile-time cache: a
# per-cell keyword corpus plus that cell's own canon_question texts,
# derived once via engine.m1.canon.cell_keywords - the identical
# derivation engine.m4.evidence.match_asks_to_cells scores a live turn's
# asks against. Not yet READ by the live turn loop (M4 still derives this
# live, correctly, straight from the fleet records) - this lands the
# artifact, hash-verified like everything else in the package, ahead of
# that read switching over; landing the cache before the read exists is
# the safer order (a bug in an unread file breaks nothing).


def build_canon_map_json(fleet: dict) -> bytes:
    cell_words = canon.cell_keywords(fleet)
    cell_questions: dict[str, list[str]] = {}
    for record in fleet.values():
        if record.get("record_type") != "canon_question" or not record.get("cell"):
            continue
        cell_questions.setdefault(record["cell"], []).append(record.get("text") or "")

    out = {
        cell: {
            "keywords": sorted(cell_words.get(cell, set())),
            "questions": sorted(cell_questions.get(cell, [])),
        }
        for cell in sorted(canon.valid_cells(fleet))
    }
    return canonical_json(out)


# ---- compiled/frame.json --------------------------------------------------
# O8: only the General/Seeker voice exists through pilot and Phase 1, so
# "frames" carries exactly one key on purpose - not an oversight.


def build_frame_json(records: dict, fleet: dict, registry_entry: dict) -> bytes:
    # `horizon` comes straight from this world's own world_core record - the
    # same field build_capsule already feeds the voice's own system prompt
    # under the "Horizon" heading (see _one(records, "world_core") above).
    # Reused verbatim for the doorway rather than re-authored: it is already
    # the world's approved, model-facing self-description, and Program-Spec
    # SS165 calls for exactly this kind of orienting scene-setting on the
    # doorway card, which the doorway never had a source for until now.
    core = _one(records, "world_core")
    horizon = core.get("horizon") if core else None

    starters = []
    for cell in sorted(canon.valid_cells(fleet)):
        classification = canon.classify_cell(cell, records)
        if classification["status"] != "substantive":
            continue
        question = next(
            (r for r in fleet.values() if r.get("record_type") == "canon_question" and r.get("cell") == cell),
            None,
        )
        if question:
            starters.append({"cell": cell, "text": question["text"]})

    payload = {
        "representative": registry_entry.get("representative"),
        "display_name": registry_entry.get("display_name"),
        "time_window": registry_entry.get("time_window"),
        "place": registry_entry.get("place"),
        "thinness_statement": registry_entry.get("thinness_statement"),
        "horizon": horizon,
        "living_tradition_flag": registry_entry.get("living_tradition_flag", False),
        "frames": {"general_seeker": {"starters": starters}},
    }
    return canonical_json(payload)


# ---- media/portrait.svg ----------------------------------------------------
# Deterministic placeholder graphic - no image-generation call, honest about
# what it is (a labeled silhouette), sized/shaped for the doorway card.


def build_media(registry_entry: dict) -> dict[str, bytes]:
    rep = registry_entry.get("representative") or {}
    name, role = rep.get("name", ""), rep.get("role_label", "")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">'
        '<rect width="240" height="240" fill="#e8e2d4"/>'
        '<circle cx="120" cy="95" r="45" fill="#b9ac8f"/>'
        '<rect x="55" y="150" width="130" height="70" rx="20" fill="#b9ac8f"/>'
        f'<text x="120" y="205" font-family="sans-serif" font-size="14" fill="#3a3226" '
        f'text-anchor="middle">{name} - {role}</text>'
        "</svg>\n"
    )
    return {"compiled/media/portrait.svg": svg.encode("utf-8")}
