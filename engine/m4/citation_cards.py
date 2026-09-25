"""Resolves a cited record_id into a real, checkable source reference -
author, work, locus, rights status - instead of the bare record id a
citation used to be. The point is not just who Origen is, but the
reference for what he is saying, so the participant can actually look at
the source document.

Every record's own `sources[]` (envelope field, Artifact-1 SS3) already
names a `source_id` + `locus`; every `source` record already names its
`author`/`work`/`edition`/`rights_status`, including which vendored file
under cic/texts/ it was read from. Nothing here reads a new field or adds
one - this is read-only resolution over what world.repository already
carries (compiled/repository.json's own blanket passthrough of every
record), the same data evidence.py and grounding_net.py already read for
other jobs.

Report only, same discipline as everything else in this package: a
record with no sources[] resolves to an empty list, never a fabricated
one.

Label resolution (cross-world transparency audit, 2026-08-26): every
citable record_type gets a real, participant-readable label - before
this, five record_types (gravity, force, contested_claim,
doctrinal_witness, honest_limit) had no entry at all here and fell
through to the bare record id, in every world, for every General
Reference of those types. And `quote`'s own label printed
speaker_or_author raw, which the corpus stores two ways (a figure
record id, or already-readable prose) - a participant saw a real name
on a world whose quotes happened to be authored as prose, and a
database key on a world whose quotes happened to be authored as figure
ids, for a difference in authoring convention that has nothing to do
with either world's actual content richness. engine.m2.builders.py's
own _quote_speaker carries the identical note for the compiled
prompt's own compact citation index; this module has full repository
access (unlike that terser context) so it resolves a figure id through
the SAME figure-label lookup a figure's own card uses, rather than a
cruder id-to-slug fallback.
"""
import re

from engine.prose import short_head

_NAME_TAXONOMY_SUFFIX = re.compile(r"\s*\[[^\]]*\]\s*$")


def _short_name(record: dict) -> str | None:
    """gravity/force records carry a `name` ending in a bracketed build
    taxonomy tag (e.g. "Divine Pedagogy [SUPPORTING - explanatory
    framework]") - real and useful to a reviewer, never meant for a
    participant. Strip it; the plain name underneath is already a good
    label."""
    name = (record.get("name") or "").strip()
    if not name:
        return None
    return _NAME_TAXONOMY_SUFFIX.sub("", name).strip() or None


def _first_sentence(text: str, max_len: int = 90) -> str:
    """doctrinal_witness and honest_limit have no title-length field of
    their own, only a full paragraph (`text`/`statement`) - the same
    first-sentence-as-head technique engine.m4.evidence.render_evidence_
    block already uses to turn a full field into a short ground-line,
    reused here for the identical reason."""
    first = (text or "").strip().split(". ")[0].rstrip(".")
    return first if len(first) <= max_len else first[: max_len - 1].rstrip() + "…"


def _figure_label(record: dict) -> str | None:
    """Prefer the in-world name a participant would actually hear the
    voice use; fall back to the scholarly name rather than a bare record
    id - a figure record always names itself somehow, in one tag or the
    other (pahc.figure.ministrae is the one figure in the fleet with no
    in-world tag at all - "no in-world name or self-designation
    survives" - not a data gap to fix, just this fallback's own reason
    for existing)."""
    names = record.get("names") or []
    in_world = next((n.get("name") for n in names if isinstance(n, dict) and n.get("tag") == "in-world"), None)
    if in_world:
        return in_world
    return next((n.get("name") for n in names if isinstance(n, dict) and n.get("tag") == "scholarly"), None)


def _quote_speaker_label(record: dict, repository_records: dict) -> str | None:
    raw = (record.get("speaker_or_author") or "").strip()
    if not raw:
        return None
    figure = repository_records.get(raw)
    if figure is not None and figure.get("record_type") == "figure":
        return _figure_label(figure) or raw
    return raw


def _quote_label(record: dict, repository_records: dict) -> str | None:
    """Source first, person as attribution: the quote card's
    headline used to be the speaker, with the work below it in small text,
    and the links pointed to the person rather than the source - the
    same correction already made once for the figure bridge: the
    point is not just who is speaking, but the reference for what they are
    saying. A quote with no sources[] still labels by its speaker -
    honest attribution beats a blank. The full work/locus strings stay in
    the card's sources[] untouched (engine.prose.short_head only builds
    this headline)."""
    speaker = _quote_speaker_label(record, repository_records)
    entry = next(iter(record.get("sources") or []), {})
    source_record = repository_records.get(entry.get("source_id")) or {}
    work = short_head(source_record.get("work") or "")
    locus = short_head(entry.get("locus") or "")
    head = ", ".join(part for part in (work, locus) if part)
    if head and speaker:
        return f"{head} — {speaker}"
    return head or speaker


_LABEL_FIELDS = {
    "term": lambda r, _repo: r.get("world_word") or r.get("term"),
    "story": lambda r, _repo: r.get("tellable_as"),
    "quote": _quote_label,
    "figure": lambda r, _repo: _figure_label(r),
    "gravity": lambda r, _repo: _short_name(r) or r.get("description"),
    "force": lambda r, _repo: _short_name(r) or r.get("description"),
    "contested_claim": lambda r, _repo: r.get("claim"),
    "doctrinal_witness": lambda r, _repo: _first_sentence(r.get("text") or ""),
    "honest_limit": lambda r, _repo: _first_sentence(r.get("statement") or ""),
    "modern_term": lambda r, _repo: ", ".join(r.get("display_terms") or []),
}


def _label(record: dict, repository_records: dict) -> str:
    getter = _LABEL_FIELDS.get(record.get("record_type"))
    label = getter(record, repository_records) if getter else None
    return label or record.get("id", "")


def _printable(value) -> bool:
    return bool(value and str(value).strip())


def resolve_source_card(record_id: str, repository_records: dict[str, dict]) -> dict | None:
    """None only when record_id isn't in this world's repository at all -
    every real citation's record_id already resolves, since citations are
    only ever emitted against ids the grounding net verified exist there.

    A real source_id, even a dangling one that fails to resolve in this
    repository, still leaves the renderer the id itself to print (its own
    primary field is `work ?? source_id`) - not an empty bullet, just an
    incompletely-resolved one. What genuinely leaves nothing to print is a
    `sources[]` entry with no source_id at all - missing or blanked
    upstream of this function, in the citing record's own sources[] list,
    a shape the grounding net's own checks don't cover since they verify
    the citing record's id, not the shape of its own sources[] entries -
    and no locus of its own either, so author/work/locus/rights_status
    are all None too (Mark's own staging report, 2026-09-23: "General
    references (1)" followed by five empty bullet items - "* " with
    nothing after). Dropped here, once, for both callers
    (resolve_citation_sources and transparency_plan.build_transparency_plan)
    rather than filtered a second time in the frontend - an entry with
    nothing to print is not a source, so it never leaves this function."""
    record = repository_records.get(record_id)
    if record is None:
        return None
    sources = []
    for entry in record.get("sources") or []:
        source_id = entry.get("source_id")
        source_record = repository_records.get(source_id) or {}
        candidate = {
            "source_id": source_id,
            "author": source_record.get("author"),
            "work": source_record.get("work"),
            "locus": entry.get("locus"),
            "rights_status": source_record.get("rights_status"),
        }
        if any(_printable(v) for v in candidate.values()):
            sources.append(candidate)
    card = {
        "record_id": record_id,
        "record_type": record.get("record_type"),
        "label": _label(record, repository_records),
        "sources": sources,
    }
    if record.get("record_type") == "quote" and record.get("modern_rendering"):
        # A quote spoken in its build-authored
        # modern rendering carries its original wording on the click page.
        card["original_wording"] = record.get("text")
        card["spoken_rendering"] = record.get("modern_rendering")
    if record.get("record_type") == "modern_term":
        # OG-13 (worlds/pahc/Open_Gaps_Tracking.md): modern_sense was read
        # only by facilitator_turns.bridge_turn, to compose its own spoken
        # sentence - never attached anywhere a participant could see it as
        # its own sourced card. Carried here the same way a quote's own
        # modern_rendering is: verbatim, additive, never composed by this
        # function.
        card["modern_sense"] = record.get("modern_sense")
        card["distinguishing_claim"] = record.get("distinguishing_claim")
    return card


def resolve_citation_sources(citations: list[dict], repository_records: dict[str, dict]) -> list[dict]:
    """citations, unchanged, with one new key per entry: `sources`, the
    resolved cards for every record_id that sentence cited. Never mutates
    the sentence/record_ids the citation-verification net already
    produced - additive only, same principle apply_net itself follows
    ("the checks gate decoration, never the text")."""
    out = []
    for citation in citations:
        cards = [resolve_source_card(rid, repository_records) for rid in citation.get("record_ids") or []]
        out.append({**citation, "sources": [c for c in cards if c is not None]})
    return out
