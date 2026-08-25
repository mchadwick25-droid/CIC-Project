"""Resolves a cited record_id into a real, checkable source reference -
author, work, locus, rights status - instead of the bare record id a
citation used to be (Mark, reviewing the first name/figure bridge build:
"the point is not just who Origen is, but the reference of what he is
saying [so] the participant can actually look at the source document").

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
"""

_LABEL_FIELDS = {
    "term": lambda r: r.get("world_word") or r.get("term"),
    "story": lambda r: r.get("tellable_as"),
    "quote": lambda r: r.get("speaker_or_author"),
    "figure": lambda r: next(
        (n.get("name") for n in (r.get("names") or []) if isinstance(n, dict) and n.get("tag") == "in-world"), None
    ),
}


def _label(record: dict) -> str:
    getter = _LABEL_FIELDS.get(record.get("record_type"))
    label = getter(record) if getter else None
    return label or record.get("id", "")


def resolve_source_card(record_id: str, repository_records: dict[str, dict]) -> dict | None:
    """None only when record_id isn't in this world's repository at all -
    every real citation's record_id already resolves, since citations are
    only ever emitted against ids the grounding net verified exist there."""
    record = repository_records.get(record_id)
    if record is None:
        return None
    sources = []
    for entry in record.get("sources") or []:
        source_id = entry.get("source_id")
        source_record = repository_records.get(source_id) or {}
        sources.append(
            {
                "source_id": source_id,
                "author": source_record.get("author"),
                "work": source_record.get("work"),
                "locus": entry.get("locus"),
                "rights_status": source_record.get("rights_status"),
            }
        )
    return {
        "record_id": record_id,
        "record_type": record.get("record_type"),
        "label": _label(record),
        "sources": sources,
    }


def resolve_citation_sources(citations: list[dict], repository_records: dict[str, dict]) -> list[dict]:
    """citations, unchanged, with one new key per entry: `sources`, the
    resolved cards for every record_id that sentence cited. Never mutates
    the sentence/record_ids the citation-verification net already
    produced - additive only, same principle _apply_net itself follows
    ("the checks gate decoration, never the text")."""
    out = []
    for citation in citations:
        cards = [resolve_source_card(rid, repository_records) for rid in citation.get("record_ids") or []]
        out.append({**citation, "sources": [c for c in cards if c is not None]})
    return out
