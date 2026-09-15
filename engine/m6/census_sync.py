"""Syncs the Atlas census's registry-derivable fields from records/worlds.yaml
into cic-website/data/world-census.json (spec Build-Blueprint.md row 8 /
CiC-Program-Spec.md line 162: "the Atlas consumes a generated open-worlds
view... never a hand-synced list").

Deliberately narrow. The census carries 292 historical "movement" entries;
only the ones whose id matches a registry world's census_id are touched at
all, and only a specific field set on those - the ones with no editorial
judgment involved. Everything else (region, lane, sourcing, dates prose,
voices, legacy, sources[], the `living` flag - which is a genuine editorial
override, not a copy of living_tradition_flag, see README below) stays
exactly as hand-authored. Widening this field set is a real decision, not a
refactor - see engine/m6/README.md before adding one.

Pure function, no filesystem I/O, mirrors engine/m2/compiler.py's own
compile_world() - testable in-memory, and it's what lets the determinism
check call it twice with identical input and diff the result.

`name` (census) / `display_name` (registry) is deliberately NOT synced,
despite looking like an obvious direct-copy candidate. Running this
against the real files during development surfaced why: engine/m1/
cross_world.py already carries a documented, ACCEPTED_OPEN finding,
`census-display-name/alx` ("F-09 - alx alone sets display_name to the
Atlas's friendly short name; the other five carry the census's formal
name") - alx's own registry display_name is the known-wrong field here,
not the census. Syncing `name` would silently propagate that registry
bug into the census instead of leaving it for whoever fixes F-09 at its
actual source.
"""
import copy

LIVE_STATUS = "Built & Live"
LIVE_STATES = {"admitted", "open"}

_TIME_WINDOW_FIELDS = (
    ("start", "start"),
    ("end", "end"),
)
# census statusMeta key -> census field, applied only once status == LIVE_STATUS
_STATUS_META_FIELDS = (
    ("chip", "chip"),
    ("glyph", "glyph"),
    ("shortWord", "statusWord"),
    ("description", "statusDescription"),
)
# census entry.* field -> registry field, applied only once status == LIVE_STATUS
_ENTRY_FIELDS = (
    ("representativeName", ("representative", "name")),
    ("representativeTitle", ("representative", "role_label")),
    ("worldName", ("card_name",)),
)


def _get_path(entry: dict, path: tuple[str, ...]):
    value = entry
    for key in path:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def sync_census(registry: dict, census: dict) -> tuple[dict, list[dict]]:
    """Returns (new_census, changes). changes is a list of
    {world, census_id, field, old, new} records - empty means the census
    already agrees with the registry everywhere this function looks."""
    census = copy.deepcopy(census)
    changes: list[dict] = []
    movements = census.get("movements", [])
    by_id = {m["id"]: m for m in movements if isinstance(m, dict) and "id" in m}
    status_meta = census.get("statusMeta", {})

    for world_key in sorted(registry):
        entry = registry[world_key]
        census_id = entry.get("census_id")
        if not census_id or census_id not in by_id:
            continue
        m = by_id[census_id]

        def record(field: str, old, new) -> None:
            changes.append({"world": world_key, "census_id": census_id, "field": field, "old": old, "new": new})

        # status: only ever advances toward Built & Live, never demotes or
        # invents a not-yet-built category the registry has no concept of.
        if entry.get("state") in LIVE_STATES and m.get("status") != LIVE_STATUS:
            record("status", m.get("status"), LIVE_STATUS)
            m["status"] = LIVE_STATUS

        window = entry.get("time_window") or {}
        for census_field, registry_field in _TIME_WINDOW_FIELDS:
            new_val = window.get(registry_field)
            if new_val is not None and m.get(census_field) != new_val:
                record(census_field, m.get(census_field), new_val)
                m[census_field] = new_val

        if m.get("status") == LIVE_STATUS:
            meta_for_status = status_meta.get(LIVE_STATUS, {})
            for meta_key, census_field in _STATUS_META_FIELDS:
                if meta_key not in meta_for_status:
                    continue
                new_val = meta_for_status[meta_key]
                if m.get(census_field) != new_val:
                    record(census_field, m.get(census_field), new_val)
                    m[census_field] = new_val

            if m.get("entry") is None:
                m["entry"] = {}
            sub = m["entry"]
            for census_field, registry_path in _ENTRY_FIELDS:
                new_val = _get_path(entry, registry_path)
                if new_val is not None and sub.get(census_field) != new_val:
                    record(f"entry.{census_field}", sub.get(census_field), new_val)
                    sub[census_field] = new_val

    _resync_meta_counts(census, movements, changes)
    return census, changes


def _resync_meta_counts(census: dict, movements: list[dict], changes: list[dict]) -> None:
    status_counts: dict[str, int] = {}
    for m in movements:
        status = m.get("status")
        status_counts[status] = status_counts.get(status, 0) + 1
    live_count = status_counts.get(LIVE_STATUS, 0)

    meta = census.setdefault("meta", {})
    if meta.get("totalEntries") != len(movements):
        changes.append({"world": None, "census_id": None, "field": "meta.totalEntries", "old": meta.get("totalEntries"), "new": len(movements)})
        meta["totalEntries"] = len(movements)
    if meta.get("liveCount") != live_count:
        changes.append({"world": None, "census_id": None, "field": "meta.liveCount", "old": meta.get("liveCount"), "new": live_count})
        meta["liveCount"] = live_count
    if meta.get("statusCounts") != status_counts:
        changes.append({"world": None, "census_id": None, "field": "meta.statusCounts", "old": meta.get("statusCounts"), "new": status_counts})
        meta["statusCounts"] = status_counts
