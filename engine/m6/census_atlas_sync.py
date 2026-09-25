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
