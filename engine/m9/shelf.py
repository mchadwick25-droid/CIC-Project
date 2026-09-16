"""Builds the `Shelf` value for one world - a world's own computed
projection of the library (Library Access Gate D3 SS1.3). Pure: no
filesystem I/O, so a determinism check can call it twice on identical
input and diff the result, the same contract `engine/m2/compiler.py`'s own
`compile_world()` already holds. `engine/m9/loader.py` is the only thing
that reads `cic/corpus-map/` and `cic/texts/`; this module only shapes
what `loader.py` already read.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Shelf:
    world_key: str
    census_id: str
    # row_id -> {source_file, work, author, role, confidence, locus,
    # locus_ids|None, voice_of|None, documented_exchange|None}
    rows: dict[str, dict] = field(default_factory=dict)
    # source_file -> [row_id, ...] - every file this world's bucket claims
    # at least one row from, AT FILE GRAIN, independent of whether any of
    # those rows carry a real row_id (CM-1) yet. Deliberately not derived
    # from `rows` below: verbatim-in-shelf (Direction B) was measured real,
    # on real fleet data, months before CM-1 existed anywhere (Q7-B, 98.2%)
    # - gating file-grain membership on a row_id that today's real buckets
    # don't have would silently empty this for every world but the fixture
    # and fail every verbatim quote for a reason that has nothing to do
    # with its own bytes. A row with no row_id still contributes its file
    # here; its own row_id list entry is simply the empty placeholder
    # "(unaddressable)" rather than a real id, since shelf_row can never
    # point at it.
    files: dict[str, list[str]] = field(default_factory=dict)
    # source_file -> normalized full text, for every file this world's
    # checks need to read: every file in `files` (verbatim-in-shelf), plus
    # any additional off-shelf file a `kind: absence` source record names
    # (Q5's narrow build-time exception) - loader.py decides which files
    # to include; this module just stores what it's given. Never
    # serialized into compiled/shelf.json (D5 ruled sources stay out of
    # worlds; the package is a projection of records/, not a copy of the
    # library).
    units: dict[str, str] = field(default_factory=dict)
    # frozenset({a, b}) -> {relation, direction|None, confidence} - every
    # ruled tradition pair from cic/corpus-map/PAIRS.yaml, not scoped to
    # this world (the lookup itself scopes it).
    pairs: dict[frozenset, dict] = field(default_factory=dict)
    # slug -> {kind, evidence} - non-census parties from PAIRS.yaml.
    parties: dict[str, dict] = field(default_factory=dict)
    # Every real filename under cic/texts/ (any world's), for source-kind's
    # "does this edition path resolve to a real vendored file AT ALL" check
    # - a broader, weaker question than "is it on my shelf" (shelf-row's
    # job). Not part of D3 SS1.3's own Shelf listing, which enumerates
    # per-world fields only; added here because a pure confinement check
    # needs this without doing its own filesystem read, and it is
    # unambiguously "data about the library" like every other Shelf field.
    vendored_files: frozenset[str] = field(default_factory=frozenset)


def build_shelf(
    *,
    world_key: str,
    census_id: str,
    bucket_rows: list[dict],
    pairs_list: list[dict],
    parties: dict[str, dict],
    units_by_file: dict[str, str],
    vendored_files: frozenset[str],
) -> Shelf:
    """bucket_rows: the raw `works` list from cic/corpus-map/<census_id>.yaml
    (each entry already carries row_id - CM-1). pairs_list: the raw `pairs`
    list from PAIRS.yaml. units_by_file: source_file -> normalized text,
    already assembled by loader.py from corpus_index.passage_units()."""
    rows: dict[str, dict] = {}
    files: dict[str, list[str]] = {}
    for entry in bucket_rows:
        source_file = entry.get("source_file")
        row_id = entry.get("row_id")
        if source_file:
            # File-grain membership never depends on row_id (see the Shelf
            # dataclass's own comment on `files`); an id-less row still
            # marks its file as on-shelf.
            files.setdefault(source_file, []).append(row_id or "(unaddressable)")
        if not row_id:
            continue  # no CM-1 id yet on this row - `rows` (shelf_row's own target) stays row_id-only
        rows[row_id] = {
            "source_file": source_file,
            "work": entry.get("work"),
            "author": entry.get("author"),
            "role": entry.get("role"),
            "confidence": entry.get("confidence"),
            "locus": entry.get("locus"),
            "locus_ids": entry.get("locus_ids"),
            "voice_of": entry.get("voice_of"),
            "documented_exchange": entry.get("documented_exchange"),
        }

    pairs: dict[frozenset, dict] = {}
    for p in pairs_list:
        a, b = p.get("a"), p.get("b")
        if not a or not b:
            continue
        pairs[frozenset({a, b})] = {
            "relation": p.get("relation"),
            "direction": p.get("direction"),
            "confidence": p.get("confidence"),
        }

    return Shelf(
        world_key=world_key,
        census_id=census_id,
        rows=rows,
        files=files,
        units=dict(units_by_file),
        pairs=pairs,
        parties=dict(parties),
        vendored_files=frozenset(vendored_files),
    )
