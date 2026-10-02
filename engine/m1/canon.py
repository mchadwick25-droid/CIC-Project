"""The set of valid canon cells is derived from the fleet's own
canon_question records - never hardcoded (law 4: one registry; everything
derived). At stage 0.6 this is the 8-cell fixture-scope subset; stage 3
grows it to the full 28 without any code here changing.

classify_cell() is the single implementation of the coverage rule (Artifact-1
SS6: "for every canon cell, every open world has >=1 doctrinal_witness/term/
story/quote OR exactly one honest_limit - never neither, never blank"). Both
the M1 canon-coverage gate and the M2 coverage.json builder call this one
function rather than each re-deriving the rule (a landmine this project has
already named: "duplicated logic fixed in one copy").

cell_keywords() is the same discipline applied to the M4 Live-Generation
Design's Stage A (LIVE-GENERATION-DESIGN.md §3.2): engine.m4.evidence
scores a live turn's asks against it at turn time, and engine.m2.builders'
compiled/indexes/canon-map.json caches its output at compile time - one
derivation, owned once, so a live Stage A match and the compiled cache can
never silently diverge.

retrieval_hint_keywords() is the second half of that same corpus, and the
reason it is a SEPARATE function rather than more words inside
cell_keywords: the canon vocabulary is fleet-owned and world-independent
(which is exactly what canon-map.json can cache once for every world),
while retrieval hints belong to one world's own records. Unioning them
inside cell_keywords would make the compiled fleet cache wrong for every
world; keeping them apart lets Stage A union the two at turn time and
leaves the cache meaning precisely what it says.

entity_cells() is the third corpus, added after a measured
failure: every router above compares CONTENT WORDS, and a proper noun
carries no more weight than any other word, so a participant naming a
figure gets nothing from the name. Measured on desert - "Is there
anything Pachomius himself actually put in writing that I could read?"
reached F4-T and F2-I at 0.29 each on the strength of "writing" and
"read", returned six records of scriptural-engagement material, and none
of the Pachomian Rule, which sits in F3-I. The name did no work at all.
"""
import re

from engine.prose import all_text, content_words


def valid_cells(fleet_records: dict[str, dict]) -> set[str]:
    return {
        r["cell"]
        for r in fleet_records.values()
        if r.get("record_type") == "canon_question" and r.get("cell")
    }


def cell_keywords(fleet_records: dict[str, dict]) -> dict[str, set[str]]:
    """Per-cell content-word corpus, built from every canon_question
    record's own `text` field - the small per-cell keyword list §3.2
    names as what Stage A scores an ask against."""
    words: dict[str, set[str]] = {}
    for record in fleet_records.values():
        if record.get("record_type") != "canon_question" or not record.get("cell"):
            continue
        words.setdefault(record["cell"], set()).update(content_words(record.get("text") or ""))
    return words


def retrieval_hint_keywords(records: dict[str, dict]) -> dict[str, set[str]]:
    """Per-cell content-word corpus contributed by one world's own records:
    each record's `retrieval.retrieve_when` text, credited to every cell in
    that record's `canon_cells`. A record that says it should be retrieved
    on "sickness, death, plague, care for the dying" is, in saying so,
    naming the words that ought to reach its cell - the field was already
    written by the world builder, gated by M1 and compiled into the
    package, and until now nothing read it at retrieval time (only
    retrieval.tier was ever read), so a question could miss ground whose
    own record named the missing word.

    Hints are sparse by design - most records carry none - so this widens
    Stage A where a builder took the trouble and changes nothing where
    they did not.
    """
    words: dict[str, set[str]] = {}
    for record in records.values():
        hints = (record.get("retrieval") or {}).get("retrieve_when") or []
        if not hints:
            continue
        hint_words = content_words(" ".join(hints))
        if not hint_words:
            continue
        for cell in record.get("canon_cells") or []:
            words.setdefault(cell, set()).update(hint_words)
    return words


def substantive_types() -> set[str]:
    return {"doctrinal_witness", "term", "story", "quote"}


# voice_scaffold_types() was removed: the fleet-parity admission battery
# measured it unreachable. Its root cause (voice_craft compiling as a
# headed record section carrying "(cite as [[id]])") is fixed in the
# compiler (builders.py: a standing-instruction section never carries an
# id), confirmed by zero voice-scaffold citations across the six-world
# battery's probes. A category whose root cause is already fixed should
# not be kept looking live beside the one below, which IS real and
# live-load-bearing.


def evidence_status_types() -> set[str]:
    """Record types whose content IS a record of the evidence situation -
    what was searched for, through what channel, and whether it was found -
    never themselves a claim resting on a source. A distinct citation
    category, found the way the (since-deleted) voice-scaffold one was: a
    live admission run (hal) answered an
    evidence-pressure probe honestly - "the richness is in the letters, not
    in the stones" - and cited the search_record that establishes exactly
    that absence (hal.search.latin-critical-texts, result: not_found). The
    citation is the answer naming its actual ground: the search that was
    run. A `result: not_found` search record is definitionally sourceless -
    73 of the fleet's 74 search records carry `sources: []` by design,
    because the record documents the looking, and what was found (if
    anything) gets its own source record instead. Requiring such a record
    to trace to a source would demand the absence of evidence come with
    evidence attached.

    Consumer rule: anything checking whether a citation is fabricated
    (M3's source_boundedness_check, chiefly) needs BOTH this and
    source-resolution to call something fabricated - never a locally
    re-derived guess at what belongs here."""
    return {"search_record"}


def classify_cell(cell: str, records: dict[str, dict]) -> dict:
    """Returns {"status": ..., "substantive": [ids], "honest_limit": [ids]}.
    status is one of: "substantive", "honest_limit", "multiple_honest_limit"
    (a gate defect - more than one honest_limit claims the same cell), or
    "empty" (a gate defect - neither route covers the cell)."""
    substantive = sorted(
        rid
        for rid, r in records.items()
        if r.get("record_type") in substantive_types() and cell in (r.get("canon_cells") or [])
    )
    honest_limit = sorted(
        rid
        for rid, r in records.items()
        if r.get("record_type") == "honest_limit" and cell in (r.get("canon_cells") or [])
    )
    if substantive:
        status = "substantive"
    elif len(honest_limit) == 1:
        status = "honest_limit"
    elif len(honest_limit) > 1:
        status = "multiple_honest_limit"
    else:
        status = "empty"
    return {"status": status, "substantive": substantive, "honest_limit": honest_limit}


# A figure's in-world name is a PHRASE, not a token list: pahc's church of
# Rome is named "the church of God sojourning at Rome". Splitting on
# whitespace - which is what engine.m4.grounding_net.build_figure_lexicon
# does, correctly, for its own job - yields {church, god, sojourning,
# rome}, and routing on "church" in a world that says church 51 times
# sends every question everywhere. That lexicon is a POSITIVE check on
# text the model already produced, where over-inclusion is harmless;
# routing is the opposite risk, so this extractor is separate and
# stricter rather than shared.
#
# Document frequency was tried first and is the WRONG discriminator,
# measured: a world's central figures are its most frequent words, so a
# df cap drops pachomius (24 mentions), antony (46) and ephrem (49) while
# keeping sojourning (7) and themselves (21). Capitalisation is what
# actually separates a name from a common noun in these fields.
_LEADING_ARTICLES = {"the", "a", "an"}


def _proper_tokens(name: str) -> set[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z'-]*", name or "")
    out: set[str] = set()
    for position, token in enumerate(tokens):
        if position == 0 and token.lower() in _LEADING_ARTICLES:
            continue
        if not token[0].isupper() or len(token) < 3:
            continue
        out.add(token.lower())
    return out


def entity_names(records: dict[str, dict]) -> set[str]:
    """Lowercased proper-noun tokens from this world's figure records'
    IN-WORLD names only. Scholarly forms are skipped for the same reason
    build_figure_lexicon skips them - "Clement of Alexandria (Titus
    Flavius Clemens...)" drags common place and epithet words in."""
    names: set[str] = set()
    for record in records.values():
        if record.get("record_type") != "figure":
            continue
        for entry in record.get("names") or []:
            if isinstance(entry, dict) and entry.get("tag") == "in-world":
                names |= _proper_tokens(entry.get("name") or "")
    return names


def entity_cells(records: dict[str, dict], *, canon_vocabulary: set[str] | None = None, min_share: float = 0.2) -> dict[str, list[str]]:
    """entity token -> the cells that token's own world actually discusses
    it in, most-discussed first.

    Mention-based rather than curated from the figure record's relations,
    deliberately: a record added tomorrow routes on the day it lands, with
    no edge to remember to declare. Measured on desert, both derivations
    return the same three cells for "pachomius" ({F3-I, F4-I, F6-I}), and
    only this one carries the WEIGHT that lets F6-I's single mention be
    dropped while F3-I's thirteen are kept.

    canon_vocabulary drops tokens the fleet's own canon questions already
    contain - ijc's "constantine" is one - because such a token already
    routes through cell_keywords and giving it a second path would only
    let entity routing displace the honest match it duplicates.

    min_share is the floor a cell must hold of one entity's mentions to
    count as a cell that entity is ABOUT rather than one it is mentioned
    in passing."""
    names = entity_names(records)
    if canon_vocabulary:
        names = {n for n in names if n not in canon_vocabulary}
    if not names:
        return {}

    counts: dict[str, dict[str, int]] = {n: {} for n in names}
    for record in records.values():
        words = content_words(all_text(record))
        cells = record.get("canon_cells") or []
        if not cells:
            continue
        for name in names & words:
            for cell in cells:
                counts[name][cell] = counts[name].get(cell, 0) + 1

    out: dict[str, list[str]] = {}
    for name, cell_counts in counts.items():
        total = sum(cell_counts.values())
        if not total:
            continue
        ranked = sorted(cell_counts.items(), key=lambda kv: (-kv[1], kv[0]))
        kept = [cell for cell, n in ranked if n / total >= min_share]
        if kept:
            out[name] = kept
    return out
