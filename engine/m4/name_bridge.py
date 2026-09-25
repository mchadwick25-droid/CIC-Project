"""The name/figure bridge (VR_1A_Transparency_Gap_2026-08-09.md SS1-SS3):
a detection pass over the voice's own finished turn text, finding which of
the world's figure records the turn actually named - Aphrahat, Gushtazad,
Jacob of Nisibis - so the UI can offer the in-world-name/scholarly-name
bridge every figure record already carries in its `names` field.

VR_1A's own measurement is why this exists: unfamiliar names, not hard
words, were the fleet's dominant unbridged-transparency gap (Papnoute
firing zero glosses across eight turns while carrying nine unbridged
names), and "the gloss system cannot help: it is keyed on
`confirmed_glosses`, which is a vocabulary table. Names were never in
scope for it." This is the missing scope, built the shape VR_1A proposed:
"A detection pass alongside find_glosses_used, matching figure-record
names[] against the emitted turn."

Never touches what the voice says. VR_1A SS3: "Never inline in the voice.
The Representative goes on saying 'Aphrahat' the way a person would. The
bridge is the UI's job, not a reason to make the voice lecture." This
module runs only on text already decided for the participant (same
discipline as engine.m4.grounding_net: string-only, no model call) and it
gates nothing - a figure going undetected here is simply not yet bridged,
never a withheld sentence.

Reads `world.figures["figures"]` (compiled/figures.json, built by
engine.m2.builders.build_figures_json from records/<world>/figure/*.md) -
already compiled, already loaded into every turn as LoadedWorld.figures,
previously read by nothing (engine.m4.grounding_net.build_figure_lexicon
reads figure names too, but only to feed the citation-verification net's
attribution heuristic - a different job, word-level and blind to which
specific figure matched). No new compiler builder, no records/ change.

A standing note for whoever writes a figure record's own `bridge_line`
(the text this module hands the frontend as the mark's short Level-2
line - FigureBridgeMark.tsx): more than a generic category label -
"the school's greatest and most contested teacher," not "a historical
figure." But not abstract personification either - a line implying the
figure is somehow still present ("his voice is still here, but he
isn't") doesn't make sense to a participant who already knows the
person is dead; it reads as false, not as warmth. Every bridge_line in
the fleet already reads the first way as of this note, checked across
every world's figure/*.md - this is guidance for what's written next,
not a correction of what's already there.
"""
import re


def _matchable_forms(figure: dict) -> list[str]:
    """Every name a figure record carries, reduced to the short spoken form
    a voice would actually say - the head of the string before any
    parenthetical scholarly aside. `names[]` stores two very different
    shapes under one field: a bare in-world epithet ("the Persian sage")
    and a scholarly citation-form ("Aphrahat (fl. 337-345; 'Mar Jacob, the
    Persian sage' in the 510 colophon; ...)"). Neither the parenthetical
    nor anything after it is a string a voice would ever say verbatim, but
    the HEAD of the scholarly form often is - VR_1A's own measured example:
    syr.figure.aphrahat's in-world tag is "the Persian sage", yet the real
    transcript that measurement read had the voice say "Aphrahat" (the
    scholarly form's head) once anyway. Checking only the in-world tag
    would have missed the exact case the report was written about.

    Both tags checked, not just in-world, per VR_1A SS3's own wording -
    "matching figure-record names[]", the whole field, not one entry of
    it. Order preserved (in-world first, as stored) so a caller that wants
    only the canonical epithet can still take element 0.

    The comma-role epithet is the same shape as the parenthetical aside
    and gets the same treatment: "Ignatius, bishop of Antioch" is a name
    whose HEAD ("Ignatius") is what a voice actually says, and the role
    after the comma is what it never says verbatim. Measured on a
    pilot transcript: both Chloe turns named Ignatius,
    and zero bridges fired, because neither recorded form's paren-head is
    the bare name. The comma head rides as an ADDITIONAL form after the
    full one, so a longer, earlier match still wins on position; checked
    against every world's compiled figures, every comma head is either a
    real spoken name (Ignatius, Pliny, Tacitus, Rabbula, Damasus I...)
    or a phrase too long to false-match.
    """
    forms = []
    for entry in figure.get("names") or []:
        if not isinstance(entry, dict):
            continue
        name = (entry.get("name") or "").split(" (", 1)[0].strip()
        if not name:
            continue
        forms.append(name)
        head = name.split(",", 1)[0].strip()
        if head and head != name:
            forms.append(head)
    return forms


def spoken_name(figure: dict) -> str | None:
    """The one short form of a figure's name a voice would say - the first
    of _matchable_forms (in-world first, as stored; the same element-0
    convention that function's own docstring promises callers). Public
    because the evidence layer needs a display name for a figure the
    session has already introduced (a pilot read found both
    Chloe turns opened "One of us, Ignatius" - the session tracked the
    introduction, but only to suppress the UI's second mark; the voice
    itself was never told), and resolving it here keeps one naming
    convention instead of two. The comma head of the first recorded name
    ("Ignatius", not "Ignatius, bishop of Antioch") - the shortest form
    a voice would actually say, same reasoning as _matchable_forms."""
    forms = _matchable_forms(figure)
    return forms[0].split(",", 1)[0].strip() if forms else None


def find_figures_used(text: str, figures: list[dict], *, already_bridged_ids: set[str] | None = None) -> list[dict]:
    """One entry per figure record any of whose names (in-world or the
    short form of the scholarly name - see _matchable_forms) appears in
    `text`, ordered by where that first appears (reading order, matching
    how citations already read) - skipping any id already in
    already_bridged_ids, so a name bridged earlier this session (the
    caller's own transcript-derived set, threaded the same way
    engine.m4.turn already threads already_told_ids for stories/quotes)
    does not fire twice. This module makes no store reads of its own.

    Word-boundary, not fuzzy: a figure only fires on one of its own
    recorded names, verbatim. Two figures whose names genuinely overlap
    (e.g. "Simeon" inside a longer "Simeon Stylites") can both fire on the
    same span with DIFFERENT matched_name strings - left as an honest
    ambiguity a human editor can see and fix by how the figure record's
    own name is written, not something this module should guess its way
    around.

    A stricter case IS resolved here, not left to the frontend's own
    overlap-drop to pick arbitrarily: two figures whose recorded name is
    IDENTICAL, not merely overlapping (hal.figure.paula and hal.figure.
    paula-younger both register the bare in-world name "Paula" - the text
    alone cannot say which one is meant). When two or more figures tie on
    the exact same (position, matched text), exactly one is kept -
    deterministically, by lowest id, so the same turn always resolves the
    same way - rather than firing both and consuming both records' one
    bridging chance this session for a match neither one specifically
    earned.
    """
    already = already_bridged_ids or set()
    by_span: dict[tuple[int, str], list[dict]] = {}
    for figure in figures:
        if figure.get("id") in already:
            continue
        best: tuple[int, str] | None = None
        for form in _matchable_forms(figure):
            # Case-insensitive: a name recorded lowercase-led ("the Elder",
            # a mid-sentence epithet) still has to match sentence-initial,
            # where ordinary capitalization makes the voice say "The
            # Elder" - a real miss caught in testing against fix.figure.
            # the-elder, not a hypothetical. match.group(0) (the text's
            # own capitalization), not `form` (the record's), is what's
            # returned below - the frontend locates this span with a
            # plain, case-sensitive indexOf, same as VoiceTurnBody already
            # does for citation sentences, so it has to be the substring
            # actually sitting in the text, not the canonical form.
            match = re.search(rf"\b{re.escape(form)}\b", text, re.IGNORECASE)
            if match and (best is None or match.start() < best[0]):
                best = (match.start(), match.group(0))
        if best is not None:
            by_span.setdefault(best, []).append(figure)

    hits = [(start, min(candidates, key=lambda f: f["id"]), matched_name) for (start, matched_name), candidates in by_span.items()]
    hits.sort(key=lambda h: h[0])
    return [
        {
            "id": figure["id"],
            "matched_name": matched_name,
            "text_start": pos,
            "names": figure.get("names") or [],
            "bridge_line": figure.get("bridge_line"),
            "dates": figure.get("dates") or {},
        }
        for pos, figure, matched_name in hits
    ]


def attach_cited_sources(figures_used: list[dict], citations_with_sources: list[dict]) -> list[dict]:
    """The real point of the bridge: not just who the figure is, but what is being said about or by
    them here, and where a participant can check it. Each figure entry
    gains `sourced_by` - the underlying primary sources (author, work,
    locus - citation_cards.resolve_source_card's own `sources[]`) of
    whichever cited sentence its own matched_name actually sits inside.

    Flattened past the cited RECORD (e.g. alx.term.allegoria) straight to
    that record's own sources: a participant asking "what backs this" is
    asking about Origen's Philocalia, not about the lexicon entry that
    happens to cite it - the record is this engine's own bookkeeping, not
    something to hand back as if it answered the question.

    Matched by substring against the citation's own sentence text, not by
    character offset: figures_used and citations are computed over the
    same finished answer_text by two independent passes (this module's
    own text search; engine.m4.grounding_net's sentence split), and
    neither carries a shared position system - but a figure's matched
    name, once found, can only sensibly belong to the one sentence whose
    own text contains it. A figure mentioned in a sentence the net
    withheld or that carries no citation gets an empty sourced_by, not a
    guess at one - an honest "nothing was cited here," never fabricated.
    """
    out = []
    for figure in figures_used:
        sentence = next((c for c in citations_with_sources if figure["matched_name"] in c["sentence"]), None)
        sourced_by = [source for card in (sentence["sources"] if sentence else []) for source in card["sources"]]
        out.append({**figure, "sourced_by": sourced_by})
    return out
