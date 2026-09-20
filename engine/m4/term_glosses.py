"""Term/concept glosses - the OTHER track VR_1A named, and the original
complaint that started this whole audit: the voice used complicated words
like "catechumen" and "Didache" with no way to look them up. `glosses`
has been a
required key on every voice_turn event since the catalog was written
(engine/m4/events.py); this module populates it.

HISTORY OF THE FIRING RULE - two designs.
The old system (cic-poc/backend's `confirmed_glosses.py`) word-matched a
hand-curated allowlist. The first record-native build here swung the
other way: citation-anchored - a gloss fired only when the voice CITED
the term record AND said the word in that cited sentence - to avoid the
Goodhart failure transparency_reach.py's docstring names ("driving
coverage up by glossing everything would produce a Representative who
lectures"). Measured on the live pilot, that lock never
opened: when the voice says "Logos" it grounds the sentence in the
doctrinal witness where the claim lives, not in the lexicon entry, so
glosses fired zero times across every probe while the name bridge (a
plain text scan) lit every author. The fix: the lexicon needs the same
plain-text-scan design as the name bridge, since it is the heart of the
depth - when a world talks about a core word like Logos, that should be
marked with a hover and click access to the built-in glossary.

So this is now the same design as engine.m4.name_bridge: a detection
pass over the finished turn text, string-only, no model call, gating
nothing. The lecturing fear is answered by the lexicon itself, not by
citation-anchoring: the world's term records ARE the curated allowlist
(Doc_03's own deliberately built, tiered, reviewed vocabulary), the
first-occurrence-per-session grammar keeps the thread calm (same
already_bridged_ids threading as the name bridge), and the mark is
UI-only - it never adds a word to what the voice says.

PER-FORM EXCEPTION (Build-Plan.md Stage 3d / Adjusted-Design.md item 8).
The bare-appearance rule above is right for a foreign/technical form -
"Logos" or "hesychia" appearing at all IS the signal, uncited or not.
It measurably misfires for an ordinary-English form some world_word
happens to carry: gallic.term.the-world-secular's "the world",
gallic.term.virtus's "power", gallic.term.elder-senior-abbot's "elder" -
common enough in unrelated prose that a bare appearance is not evidence
the concept is even in play. `engine.m1.schemas`'s new `gloss_forms`
field lets a term record mark specific forms "ordinary"; those alone
fall back to the OLD citation-anchored rule (fire only inside a sentence
the turn already cited to this same term record) - scoped per-form, not
reintroduced project-wide, so it never reopens the zero-fires failure
the 2026-08-30 ruling fixed. A form the field doesn't name, and every
term record fleet-wide that predates the field, defaults to "technical"
- today's exact behavior, unchanged.
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


def _form_pattern(form: str) -> tuple[str, int]:
    """(pattern, flags) for one form. Case-insensitive by default, same as
    the name bridge - but a form whose CAPITAL sits past the first
    character ("the Word", "the Son", "the Two Ways") is distinguished
    from ordinary prose BY that capital, and matching it case-blind is a
    measured false positive, not a hypothetical: "The word meant the
    whole church" (a sentence about the word 'catholic') lit the
    Christ-as-Word gloss on the first fleet-wide dry run. Such forms
    match case-sensitively, with only the first letter flexible (a
    sentence-initial "The Word" still matches)."""
    if any(c.isupper() for c in form[1:]):
        first, rest = form[0], re.escape(form[1:])
        if first.isalpha():
            return rf"\b[{first.upper()}{first.lower()}]{rest}\b", 0
        return rf"\b{re.escape(form)}\b", 0
    return rf"\b{re.escape(form)}\b", re.IGNORECASE


def _form_kind(term_record: dict, form: str) -> str:
    """"technical" (fire on sight - today's behavior) or "ordinary"
    (citation-gated) for one matchable form, from the term record's own
    optional `gloss_forms` (engine.m1.schemas, Build-Plan.md Stage 3d).
    Case-insensitive lookup, matching _form_pattern's own default. A form
    `gloss_forms` doesn't name - including every term record fleet-wide
    that predates the field - defaults to "technical"."""
    for entry in term_record.get("gloss_forms") or []:
        if (entry.get("form") or "").lower() == form.lower():
            return entry.get("kind") or "technical"
    return "technical"


def _ordinary_form_match(pattern: str, flags: int, text: str, own_cited_sentences: list[str]) -> tuple[int, str] | None:
    """The pre-2026-08-30 citation-anchored rule, scoped to one form: only
    a match sitting inside a sentence this turn already cited to the
    form's own term record counts. `own_cited_sentences` are that
    record's own citation sentences (already filtered by the caller);
    the match's position is resolved back into `text`'s own coordinates
    (matched_name's downstream contract - see find_glosses_used) via the
    cited sentence's own offset, since citations carry sentence text, not
    spans."""
    best: tuple[int, str] | None = None
    for sentence in own_cited_sentences:
        match = re.search(pattern, sentence, flags)
        if not match:
            continue
        offset = text.find(sentence)
        if offset < 0:
            continue
        candidate = (offset + match.start(), match.group(0))
        if best is None or candidate[0] < best[0]:
            best = candidate
    return best


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

    A form the record's own `gloss_forms` marks "ordinary" (module
    docstring) only counts inside a sentence this same turn already
    cited to this record - every other form keeps firing on sight,
    exactly as before.
    """
    already = set(already_bridged_ids or ())
    by_span: dict[tuple[int, str], list[dict]] = {}
    for record in repository_records.values():
        if record.get("record_type") != "term" or record.get("id") in already:
            continue
        own_cited_sentences = [
            c["sentence"] for c in citations if record["id"] in (c.get("record_ids") or []) and c.get("sentence")
        ]
        best: tuple[int, str] | None = None
        for form in _matchable_forms(record):
            pattern, flags = _form_pattern(form)
            if _form_kind(record, form) == "ordinary":
                candidate = _ordinary_form_match(pattern, flags, text, own_cited_sentences)
            else:
                match = re.search(pattern, text, flags)
                candidate = (match.start(), match.group(0)) if match else None
            if candidate and (best is None or candidate[0] < best[0]):
                best = candidate
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
