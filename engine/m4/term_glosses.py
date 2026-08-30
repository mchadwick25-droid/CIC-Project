"""Term/concept glosses - the OTHER track VR_1A named, and the original
complaint that started this whole audit (Mark, live site, 2026-08-09: "it
uses complicated words ... catechumen and Didache"). `glosses` has been a
required key on every voice_turn event since the catalog was written
(engine/m4/events.py); this module populates it.

HISTORY OF THE FIRING RULE - two designs, and Mark's ruling between them.
The old system (cic-poc/backend's `confirmed_glosses.py`) word-matched a
hand-curated allowlist. The first record-native build here swung the
other way: citation-anchored - a gloss fired only when the voice CITED
the term record AND said the word in that cited sentence - to avoid the
Goodhart failure transparency_reach.py's docstring names ("driving
coverage up by glossing everything would produce a Representative who
lectures"). Measured on the live pilot (2026-08-30), that lock never
opened: when the voice says "Logos" it grounds the sentence in the
doctrinal witness where the claim lives, not in the lexicon entry, so
glosses fired zero times across every probe while the name bridge (a
plain text scan) lit every author. Mark's ruling: "the lexicon is not
working ... and it is the heart of the depth. so when Alexandria talks
about Logos (a core word for their world) that should be [marked] with
a hover and click access to the glossary that is built in the system."

So this is now the same design as engine.m4.name_bridge: a detection
pass over the finished turn text, string-only, no model call, gating
nothing. The lecturing fear is answered by the lexicon itself, not by
citation-anchoring: the world's term records ARE the curated allowlist
(Doc_03's own deliberately built, tiered, reviewed vocabulary), the
first-occurrence-per-session grammar keeps the thread calm (same
already_bridged_ids threading as the name bridge), and the mark is
UI-only - it never adds a word to what the voice says.
"""
import re


def _matchable_forms(term_record: dict) -> list[str]:
    """Every string a voice would actually say for this term's world_word.
    The corpus writes the field three ways, measured fleet-wide (35
    compound forms across the six worlds): a parenthetical aside that is
    never spoken verbatim ("anastasis (resurrection)" - the head is the
    word), comma pairs where both halves are real words ("baptism,
    photismos"), and slash lists of alternate forms ("geron / abba /
    amma"). The full pre-parenthetical form always rides first - a longer
    phrase like "Imperator intra Ecclesiam, non supra Ecclesiam" still
    matches whole - with the pieces after it. Fragments under three
    characters are dropped rather than word-matched."""
    word = (term_record.get("world_word") or "").split(" (", 1)[0].strip()
    if not word:
        return []
    forms = [word]
    for sep in (",", "/"):
        if sep in word:
            forms.extend(piece.strip() for piece in word.split(sep))
    seen: set[str] = set()
    out = []
    for form in forms:
        key = form.lower()
        if len(form) >= 3 and key not in seen:
            seen.add(key)
            out.append(form)
    return out


def find_glosses_used(text: str, citations: list[dict], repository_records: dict[str, dict], *, already_bridged_ids: set[str] | None = None) -> list[dict]:
    """One entry per term record whose world_word (any matchable form -
    see _matchable_forms) appears in `text`, ordered by where it first
    appears, skipping anything in already_bridged_ids - the identical
    contract, span discipline, and tie-break as
    engine.m4.name_bridge.find_figures_used:

    - Word-boundary, case-insensitive; matched_name is the text's own
      substring (the frontend locates it with a plain indexOf).
    - Two records tying on the exact same (position, matched text) - e.g.
      alx.term.baptism's "photismos" piece against alx.term.photismos
      itself - resolve deterministically to the lowest id, consuming one
      gloss chance, not both.

    `sourced_by` carries the flattened source cards of whichever citation
    sentence the matched word sits inside (citations here are
    resolve_citation_sources output) - and an empty list when the word's
    sentence carries no citation: an honest "nothing was cited here,"
    never a fabricated source. The term record's own meanings always ride
    regardless, straight from the compiled lexicon entry.
    """
    already = set(already_bridged_ids or ())
    by_span: dict[tuple[int, str], list[dict]] = {}
    for record in repository_records.values():
        if record.get("record_type") != "term" or record.get("id") in already:
            continue
        best: tuple[int, str] | None = None
        for form in _matchable_forms(record):
            match = re.search(rf"\b{re.escape(form)}\b", text, re.IGNORECASE)
            if match and (best is None or match.start() < best[0]):
                best = (match.start(), match.group(0))
        if best is not None:
            by_span.setdefault(best, []).append(record)

    hits = [(start, min(candidates, key=lambda r: r["id"]), matched_name) for (start, matched_name), candidates in by_span.items()]
    hits.sort(key=lambda h: h[0])

    out = []
    for _pos, record, matched_name in hits:
        sentence = next((c for c in citations if matched_name in c.get("sentence", "")), None)
        sourced_by = [source for card in (sentence.get("sources") or [] if sentence else []) for source in card["sources"]]
        out.append(
            {
                "id": record["id"],
                "matched_name": matched_name,
                "plain_meaning": record.get("plain_meaning"),
                "quick_meaning": record.get("quick_meaning"),
                "translational_sense": (record.get("senses") or {}).get("translational"),
                "false_friend": record.get("false_friend") or [],
                "sourced_by": sourced_by,
            }
        )
    return out
