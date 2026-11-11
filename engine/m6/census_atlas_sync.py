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
    "placeLabel",
    "modernCountries",
    "placeQualifiers",
    "publicOpen",
    "continuesAs",
    "kind",
)

# A tradition's people, a person's home tradition and a person's card: the
# map's Who stacks and person cards draw them for every movement, built or not.
PEOPLE_FIELDS = (
    "people",
    "peopleNote",
    "toldWithin",
    "card",
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

# Census fields the Atlas never carries: the dated evidence behind the living
# mark stays in the census record only.
CENSUS_ONLY_FIELDS = ("livingEvidence",)


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
        fields = STRUCTURAL_FIELDS + PEOPLE_FIELDS + (BUILT_WORLD_FIELDS if cm.get("status") == LIVE_STATUS else NON_BUILT_WORLD_FIELDS)
        for field in fields:
            if field not in cm:
                continue
            new_val = cm[field]
            old_val = m.get(field)
            if old_val != new_val:
                changes.append({"id": mid, "field": field, "old": old_val, "new": new_val})
                m[field] = new_val

    return atlas_movements, changes


def atlas_row(census_movement: dict) -> dict:
    """The Atlas's copy of a census movement it does not yet hold: the census
    record whole, less the census-only fields and, for a built world, the
    prose the Atlas fetches from the world's own orientation JSON instead."""
    omit = set(CENSUS_ONLY_FIELDS)
    if census_movement.get("status") == LIVE_STATUS:
        omit |= set(NON_BUILT_WORLD_FIELDS) - set(BUILT_WORLD_FIELDS)
    return {k: copy.deepcopy(v) for k, v in census_movement.items() if k not in omit}


def sync_roster(census: dict, atlas_movements: list[dict]) -> tuple[list[dict], list[str], list[str]]:
    """Returns (new_atlas_movements, added_ids, removed_ids). The Atlas holds
    exactly the census's movements, in the census's order: a census movement
    it lacks is added as atlas_row() builds it, and a movement the census no
    longer holds is dropped. Rows the Atlas already holds are kept as they
    are; sync_atlas mirrors their fields."""
    held = {m.get("id"): m for m in atlas_movements}
    census_movements = [m for m in census.get("movements", []) if isinstance(m, dict) and "id" in m]
    census_ids = {m["id"] for m in census_movements}
    new_movements, added = [], []
    for cm in census_movements:
        if cm["id"] in held:
            new_movements.append(copy.deepcopy(held[cm["id"]]))
        else:
            new_movements.append(atlas_row(cm))
            added.append(cm["id"])
    removed = [m.get("id") for m in atlas_movements if m.get("id") not in census_ids]
    return new_movements, added, removed


def eras_out_of_sync(census: dict, atlas_eras: list[dict]) -> bool:
    """The Atlas's eras are a plain mirror of the census's, whole."""
    return census.get("eras", []) != atlas_eras


def edges_out_of_sync(census: dict, atlas_edges: list[dict]) -> bool:
    """The Atlas's edges are a plain mirror of the census's, whole."""
    return census.get("edges", []) != atlas_edges
