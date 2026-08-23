"""Deterministic builders: records -> the compiled/ half of a World Package
(Artifact-2 SS1). Every function here is pure - same records in, same bytes
out, no wall clock, no randomness, no network. Content-only; the
`generated-by` header stamping (Artifact-2 SS3) happens once, centrally, in
compiler.py, so it doesn't have to be threaded through every function here.
"""
import hashlib

from engine.m1 import canon
from engine.m1.gates_experimental import _GROUNDING_FLOOR, _content_words, _quote_aware_sentences
# The compiler tags demonstrations against the LIVE net's own quote rule,
# imported rather than reimplemented. engine.m4.grounding_net depends only on
# `re` and engine.m1.gates_experimental (no m2, no m4 siblings), so this is a
# leaf import, not a compiler->runtime cycle. Copying the check here instead
# would defeat the point: the two must agree BY CONSTRUCTION, because a demo
# tagged one way and checked another is exactly the defect it exists to stop.
from engine.m4.grounding_net import _quoted_spans, _span_in_records

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


# The citation contract's worked example ships two PLACEHOLDER ids -
# `world.term.example` / `world.gravity.example` - and the fleet record's own
# trailing body says so plainly: they exist "only so `citation_contract` is a
# complete, self-explanatory paragraph on its own - never the line a model is
# actually shown", with the per-world substitution named there as still-open
# M2 compiler work. It was never implemented, so all seven packages shipped
# the literal token `world` into live model input. A model reads that as the
# namespace and emits `world.story.pliny-interrogation`,
# `world.term.hesychia` - correct shape, no such record - and every sentence
# so tagged is withheld as an unresolvable id. Measured live 2026-08-23: 46%
# of all emitted tags were this one substitution, and one desert turn on
# prayer was annihilated whole, the participant told the world had no
# grounded material on prayer.
#
# Filled from the world's own records, exactly as `{world}` in pronoun_rule
# is already filled from the world's own registry entry - mechanical,
# deterministic (lowest sorted id of the matching type), never a hand-written
# per-world phrase. Principle 3 holds: this substitutes real ids into record-
# authored prose, it does not let the compiler author prompt content.
_EXAMPLE_PLACEHOLDERS = ("world.term.example", "world.gravity.example")


def _example_record_id(records: dict, preferred_type: str) -> str | None:
    """Lowest sorted id of `preferred_type`; failing that, of any citable
    record. A demonstration is never citable ground, so it is excluded."""
    for wanted in (preferred_type, None):
        ids = sorted(
            record["id"]
            for record in records.values()
            if record.get("record_type") != "demonstration"
            and (wanted is None or record.get("record_type") == wanted)
        )
        if ids:
            return ids[0]
    return None


def _fill_citation_example(contract: str, records: dict) -> str:
    """Substitutes each placeholder id for a real one from this world's own
    corpus. A placeholder with no substitute available is dropped from the
    example rather than shipped: an absent second tag still reads as a
    correct worked line, an unresolvable one teaches a fabrication."""
    for placeholder in _EXAMPLE_PLACEHOLDERS:
        if f"[[{placeholder}]]" not in contract:
            continue
        real = _example_record_id(records, placeholder.split(".")[1])
        if real and f"[[{real}]]" not in contract:
            contract = contract.replace(f"[[{placeholder}]]", f"[[{real}]]")
        else:
            contract = contract.replace(f" [[{placeholder}]]", "").replace(f"[[{placeholder}]]", "")
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
        emit("Register", "\n".join(f"{s['number']}. {s['statement']}" for s in statements))

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
    own _all_text, what _overlap_coefficient and the live net's own ratio
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
_MIN_SHARED_WORDS = 2


# The citation contract's own words: tags go "before the terminal
# punctuation... so a sentence-boundary split can never break inside one."
# That is not a stylistic preference - engine.m4.grounding_net.parse_tagged
# splits on _SENTENCE_SPLIT (?<=[.!?])\s+, so a tag emitted AFTER the final
# stop is carried into the NEXT sentence and grounds the wrong claim, while
# the sentence it was meant for is left untagged and withheld outright. The
# first substantive claim of every turn is the one that loses its tag that
# way, and the two memorable lines of an answer are usually quotes, so the
# quotes are what a participant stops seeing. Found live, 2026-08-23, at 36%
# of generated sentences withheld; and the compiled demonstrations are also
# what teaches a live model where to put its own tags, so this one character
# of placement propagates straight into generation.
_TERMINAL_PUNCTUATION = ".!?"


def _insert_tag(sentence: str, tag: str) -> str:
    """Place `tag` immediately before the sentence's final terminal
    punctuation mark - the placement the contract specifies and the live
    splitter requires. A sentence with no terminal punctuation at all (a
    trailing fragment) gets the tag appended; there is no split for it to
    fall across."""
    cut = max((sentence.rfind(mark) for mark in _TERMINAL_PUNCTUATION), default=-1)
    if cut < 0:
        return f"{sentence} {tag}"
    return f"{sentence[:cut]} {tag}{sentence[cut:]}"


def _quote_holder(sentence: str, records: dict | None) -> str | None:
    """A sentence carrying a quoted span is judged by the live net on ONE
    structural rule, not on ratio: the quoted words must appear verbatim in
    a tagged record (grounding_net.check_turn's quoted-span branch). Lexical
    overlap is the wrong instrument for that - a record that PARAPHRASES a
    quote routinely out-scores the record that actually holds it, so the
    ranked-best tag names a record the net will then reject, and the quote
    is withheld. Found in the compiled demos: hal's Ciceronian-dream quote
    tagged to a paraphrasing doctrinal_witness while
    hal.quote.dream-follower-of-cicero, holding it verbatim, sat unused in
    the same package.

    Searched over the whole package rather than the demo's own canon cells:
    a quote record is where it is, and the net does not scope its verbatim
    check by cell either. Deterministic - lowest record id wins a tie.
    Demonstration records are excluded: a demo can never be another demo's
    ground (its own text would match itself trivially)."""
    if not records:
        return None
    spans = _quoted_spans(sentence)
    if not spans:
        return None
    for record_id in sorted(records):
        record = records[record_id]
        if record.get("record_type") == "demonstration":
            continue
        if all(_span_in_records(span, [record]) for span in spans):
            return record_id
    return None


def _tag_representative_text(text: str, candidates: list[dict], records: dict | None = None) -> str:
    candidate_words = [(record["id"], _content_words(_candidate_head_text(record))) for record in candidates]
    tagged: list[str] = []
    for sentence in _quote_aware_sentences(text):
        # The quote rule first: it is the net's own hard structural check,
        # and a ratio win can never satisfy it.
        holder = _quote_holder(sentence, records)
        if holder:
            tagged.append(_insert_tag(sentence, f"[[{holder}]]"))
            continue
        words = _content_words(sentence)
        best_id, best_ratio, best_shared = None, 0.0, 0
        for record_id, record_words in candidate_words:
            if not words or not record_words:
                continue
            shared = words & record_words
            ratio = len(shared) / min(len(words), len(record_words))
            if ratio > best_ratio:
                best_ratio, best_id, best_shared = ratio, record_id, len(shared)
        if best_id and best_ratio >= _GROUNDING_FLOOR and best_shared >= _MIN_SHARED_WORDS:
            tagged.append(_insert_tag(sentence, f"[[{best_id}]]"))
        else:
            tagged.append(sentence)
    return " ".join(tagged)


def build_prompt(records: dict, fleet: dict, registry_entry: dict) -> bytes:
    segments: list[str] = build_fleet_preamble(fleet, registry_entry, records)

    def emit(header: str, body: str | None) -> None:
        if body and body.strip():
            segments.append(f"## {header}\n\n{body.strip()}\n")

    craft = _one(records, "voice_craft")
    if craft:
        emit("Identity", craft.get("identity"))

    core = _one(records, "world_core")
    if core:
        emit("Horizon", core.get("horizon"))
        emit("Formation logic", core.get("formation_logic"))
        emit("Thinness", core.get("thinness"))
        emit("Cautions", core.get("cautions"))

    if craft:
        emit("Guard", craft.get("guard"))
        concerns = craft.get("characteristic_concerns") or []
        if concerns:
            emit("Characteristic concerns", "\n".join(f"- {c}" for c in concerns))
        notes = craft.get("flavor_notes") or []
        if notes:
            emit(
                "Flavor notes",
                "\n".join(f"- [{n.get('segment')}] {n.get('note')}" for n in notes),
            )

    for term in _by_type(records, "term"):
        body = "\n\n".join(filter(None, [term.get("plain_meaning"), term.get("quick_meaning")]))
        emit(f"Term: {term.get('world_word', term['id'])}", body)

    for witness in _by_type(records, "doctrinal_witness"):
        cells = ",".join(witness.get("canon_cells") or [])
        emit(f"Witness ({cells})", witness.get("text"))

    for limit in _by_type(records, "honest_limit"):
        cells = ",".join(limit.get("canon_cells") or [])
        emit(f"Honest limit ({cells})", limit.get("statement"))

    for story in _by_type(records, "story"):
        body = "\n\n".join(filter(None, [story.get("tellable_as"), story.get("text")]))
        emit(f"Story: {story['id']}", body)

    for demo in _by_type(records, "demonstration"):
        exchange = demo.get("exchange") or []
        candidates = _demonstration_candidates(records, demo)
        lines = []
        for turn in exchange:
            text = turn["text"]
            if turn.get("speaker") == "representative" and candidates:
                text = _tag_representative_text(text, candidates, records)
            lines.append(f"{turn['speaker']}: {text}")
        emit(f"Demonstration: {demo['id']}", "\n".join(lines))

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
