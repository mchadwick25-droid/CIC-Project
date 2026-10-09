"""Syncs atlas-v3.html's embedded movement records from world-census.json
(spec Build-Blueprint.md row 8 / CiC-Program-Spec.md line 162: "the Atlas
consumes a generated open-worlds view... never a hand-synced list" - the
same principle census_sync.py already applies one layer up, registry into
census; this is the next layer, census into the Atlas).

world-census.json is authoritative. Every field named in STRUCTURAL_FIELDS,
NON_BUILT_WORLD_FIELDS, or BUILT_WORLD_FIELDS is a plain mirror: whatever
census.json says, the Atlas gets. There is no merge logic here and there
must not be one - if the two files disagree on one of these fields, that
disagreement is a content decision for a human or an editorial pass to make
in census.json, never something this module guesses at.

STRUCTURAL_FIELDS (status, chip, glyph, living, entry, start/end/dates,
lane placement, ...) sync unconditionally for every movement, built or not -
a movement's own identity and routing, not prose content.

Built worlds (status == LIVE_STATUS) are the one further exception, for
prose content only: their Atlas entries deliberately omit most of the
NON_BUILT_WORLD_FIELDS in favor of content fetched at runtime from the
separately compiled per-world orientation JSON (cic-website/data/worlds/
<id>.json, built by engine/m2/site_compiler.py's compile_world_front, run
via `python -m engine.m2.site_cli build`, from a world's own world_front
record) - BUILT_WORLD_FIELDS is the subset of that prose the Atlas still
carries directly for them.

Deliberately excluded from every list above: `legacySources`,
`storySources`, and `verifiedSources` - checked directly, world-census.json
carries none of the three on any of its 292 movements, so there is nothing
for this module to mirror from. Where a built world's Atlas entry carries
real values for them (post-apostolic-house-church does), that content
comes from a different pipeline entirely; syncing these fields from
census.json would overwrite real Atlas content with an absent value on
every movement that has any, which is the merge-logic/content-guess this
module's own first paragraph rules out.

Edges are compared, not written: compare_edges reports every way the Atlas's
embedded edges differ from census.json's (an edge present on one side only,
or a differing confidence or note), keyed by from, to and type. The check is
the CI gate; a reported difference is fixed in census.json, the authoritative
side, and in the Atlas's embedded copy to match it.
"""
import copy

LIVE_STATUS = "Built & Live"

# Identity/routing fields every movement carries regardless of built status -
# not content, so not subject to the built-world "fetched at runtime from the
# compiled orientation JSON instead" exception below. A drift here breaks the
# Atlas's own status chip, glyph, living-tradition flag, or lane placement for
# that movement, not just its prose.
STRUCTURAL_FIELDS = (
    "status",
    "chip",
    "glyph",
    "statusWord",
    "statusDescription",
    "living",
    "entry",
    "start",
    "end",
    "dates",
    "lane",
    "laneLabel",
    "laneOrder",
    "name",
    "shortName",
    "era",
    "region",
    "continuesAs",
)

NON_BUILT_WORLD_FIELDS = (
    "why",
    "relationsSummary",
    "sourcing",
    "floorNote",
    "legacy",
    "longDescription",
    "voices",
    "sources",
    "experienceToday",
    "documentedStories",
    "teaser",
)

BUILT_WORLD_FIELDS = ("sources",)


def sync_atlas(census: dict, atlas_movements: list[dict]) -> tuple[list[dict], list[dict]]:
    """Returns (new_atlas_movements, changes). changes is a list of
    {id, field, old, new} records - empty means the Atlas already agrees
    with census.json everywhere this function looks."""
    atlas_movements = copy.deepcopy(atlas_movements)
    changes: list[dict] = []
    census_by_id = {m["id"]: m for m in census.get("movements", []) if isinstance(m, dict) and "id" in m}

    for m in atlas_movements:
        mid = m.get("id")
        cm = census_by_id.get(mid)
        if cm is None:
            continue
        fields = STRUCTURAL_FIELDS + (BUILT_WORLD_FIELDS if cm.get("status") == LIVE_STATUS else NON_BUILT_WORLD_FIELDS)
        for field in fields:
            if field not in cm:
                continue
            new_val = cm[field]
            old_val = m.get(field)
            if old_val != new_val:
                changes.append({"id": mid, "field": field, "old": old_val, "new": new_val})
                m[field] = new_val

    return atlas_movements, changes


def _edge_key(edge: dict) -> tuple:
    return (edge.get("from"), edge.get("to"), edge.get("type"))


def _edge_label(key: tuple) -> str:
    return f"{key[0]} > {key[1]} ({key[2]})"


def compare_edges(census: dict, atlas_edges: list[dict]) -> list[dict]:
    """Returns changes as {id, field, old, new} records, the same shape
    sync_atlas returns: old is the Atlas's value, new is census.json's. An
    edge only in census.json reports field "edge" with old None; an edge
    only in the Atlas reports field "edge" with new None. Empty means the
    Atlas's edges agree with census.json everywhere this function looks."""
    changes: list[dict] = []
    census_edges = {_edge_key(e): e for e in census.get("edges", []) if isinstance(e, dict)}
    atlas_by_key = {_edge_key(e): e for e in atlas_edges if isinstance(e, dict)}

    for key, ce in census_edges.items():
        ae = atlas_by_key.get(key)
        if ae is None:
            changes.append({"id": _edge_label(key), "field": "edge", "old": None, "new": ce})
            continue
        for field in sorted((set(ce) | set(ae)) - {"from", "to", "type"}):
            if ae.get(field) != ce.get(field):
                changes.append({"id": _edge_label(key), "field": field, "old": ae.get(field), "new": ce.get(field)})

    for key, ae in atlas_by_key.items():
        if key not in census_edges:
            changes.append({"id": _edge_label(key), "field": "edge", "old": ae, "new": None})

    return changes
