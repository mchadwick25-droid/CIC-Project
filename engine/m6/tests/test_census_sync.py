import copy
import json

from engine.m1.registry import load_registry
from engine.m6.census_sync import LIVE_STATUS, sync_census

STATUS_META = {
    "Built & Live": {"chip": "live", "glyph": None, "shortWord": "Open for conversation", "description": "You can sit down with this tradition now."},
}


def _registry():
    return {
        "abc": {
            "state": "admitted",
            "display_name": "The Formal Scholarly Name",
            "card_name": "The Friendly Name",
            "census_id": "abc-census-id",
            "time_window": {"start": 100, "end": 200},
            "living_tradition_flag": True,
            "representative": {"name": "Rep", "role_label": "Role Label"},
        },
        "notyet": {
            "state": "built",
            "display_name": "Not Yet Admitted",
            "card_name": "Not Yet Friendly",
            "census_id": "notyet-census-id",
            "time_window": {"start": 300, "end": 400},
            "living_tradition_flag": False,
            "representative": {"name": "Rep2", "role_label": "Role2"},
        },
        "noncensus": {
            "state": "admitted",
            "display_name": "No Census Link",
            "card_name": "No Census Link Friendly",
            "census_id": None,
            "time_window": {"start": 1, "end": 2},
            "living_tradition_flag": False,
            "representative": {"name": "Rep3", "role_label": "Role3"},
        },
    }


def _census():
    return {
        "meta": {"totalEntries": 3, "liveCount": 0, "statusCounts": {"Selected - Not Yet Built": 3}},
        "statusMeta": copy.deepcopy(STATUS_META),
        "movements": [
            {
                "id": "abc-census-id", "status": "Selected - Not Yet Built", "start": 1, "end": 2,
                "name": "A Different Editorial Name Entirely", "entry": None, "living": False,
                "chip": "sel", "glyph": "sel", "statusWord": "Not yet built", "statusDescription": "placeholder",
            },
            {
                "id": "notyet-census-id", "status": "Selected - Not Yet Built", "start": 300, "end": 400,
                "entry": None, "living": False,
                "chip": "sel", "glyph": "sel", "statusWord": "Not yet built", "statusDescription": "placeholder",
            },
            {
                "id": "unrelated-historical-entry", "status": "Pre-Survey Candidate", "start": 500, "end": 600,
                "sourcing": "Real historical research prose, never touched.", "entry": None,
                "chip": None, "glyph": None, "statusWord": None, "statusDescription": None,
            },
        ],
    }


def _by_id(census, cid):
    return next(m for m in census["movements"] if m["id"] == cid)


def test_determinism_twice_identical():
    registry, census = _registry(), _census()
    first, _ = sync_census(registry, census)
    second, _ = sync_census(registry, census)
    assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)


def test_admitted_world_advances_to_live_and_populates_derived_fields():
    registry, census = _registry(), _census()
    new_census, changes = sync_census(registry, census)
    entry = _by_id(new_census, "abc-census-id")
    assert entry["status"] == LIVE_STATUS
    assert entry["chip"] == "live"
    assert entry["glyph"] is None
    assert entry["statusWord"] == "Open for conversation"
    assert entry["statusDescription"] == "You can sit down with this tradition now."
    assert entry["start"] == 100
    assert entry["end"] == 200
    assert entry["entry"] == {
        "representativeName": "Rep",
        "representativeTitle": "Role Label",
        "worldName": "The Friendly Name",
    }
    assert {c["field"] for c in changes if c["world"] == "abc"} == {
        "status", "chip", "glyph", "statusWord", "statusDescription", "start", "end",
        "entry.representativeName", "entry.representativeTitle", "entry.worldName",
    }


def test_built_not_admitted_world_is_left_untouched():
    """state: built (not yet admitted) must never be advanced to Built & Live
    or gain populated entry.* fields - the registry has no concept of the
    census's own finer-grained not-yet-built categories, so this module
    never guesses at one. Matches the real, live Donatism case (state:
    built, census still correctly shows Selected - Not Yet Built)."""
    registry, census = _registry(), _census()
    before = copy.deepcopy(_by_id(census, "notyet-census-id"))
    new_census, changes = sync_census(registry, census)
    after = _by_id(new_census, "notyet-census-id")
    assert after == before
    assert not any(c["world"] == "notyet" for c in changes)


def test_unrelated_historical_entry_is_byte_identical():
    registry, census = _registry(), _census()
    before = copy.deepcopy(_by_id(census, "unrelated-historical-entry"))
    new_census, _ = sync_census(registry, census)
    after = _by_id(new_census, "unrelated-historical-entry")
    assert after == before


def test_name_field_is_never_synced():
    """Deliberately not a direct-copy field - see census_sync.py's own
    module docstring: engine/m1/cross_world.py's ACCEPTED_OPEN finding
    census-display-name/alx (F-09) establishes that a census `name`/
    registry `display_name` mismatch is sometimes the REGISTRY's own bug,
    not census staleness. Syncing this field would propagate that class of
    bug instead of leaving it for whoever fixes it at its actual source."""
    registry, census = _registry(), _census()
    new_census, changes = sync_census(registry, census)
    entry = _by_id(new_census, "abc-census-id")
    assert entry["name"] == "A Different Editorial Name Entirely"
    assert not any(c["field"] == "name" for c in changes)


def test_living_field_is_never_synced():
    """living is a real editorial override in at least one live case (ijc,
    held false pending a separate Article 29 confirmation gate) - see
    census_sync.py's module docstring. Never touched, regardless of
    living_tradition_flag."""
    registry, census = _registry(), _census()
    new_census, changes = sync_census(registry, census)
    entry = _by_id(new_census, "abc-census-id")
    assert entry["living"] is False  # registry living_tradition_flag is True for "abc"
    assert not any(c["field"] == "living" for c in changes)


def test_no_census_id_world_is_ignored():
    registry, census = _registry(), _census()
    new_census, changes = sync_census(registry, census)
    assert not any(c["world"] == "noncensus" for c in changes)


def test_meta_counts_recomputed():
    registry, census = _registry(), _census()
    new_census, changes = sync_census(registry, census)
    assert new_census["meta"]["liveCount"] == 1
    assert new_census["meta"]["totalEntries"] == 3
    assert new_census["meta"]["statusCounts"] == {LIVE_STATUS: 1, "Selected - Not Yet Built": 1, "Pre-Survey Candidate": 1}
    assert any(c["field"] == "meta.liveCount" for c in changes)


def test_idempotent_second_pass_produces_no_further_changes():
    registry, census = _registry(), _census()
    once, _ = sync_census(registry, census)
    twice, changes = sync_census(registry, once)
    assert changes == []
    assert json.dumps(once, sort_keys=True) == json.dumps(twice, sort_keys=True)


def test_input_dicts_are_not_mutated():
    registry, census = _registry(), _census()
    registry_before, census_before = copy.deepcopy(registry), copy.deepcopy(census)
    sync_census(registry, census)
    assert registry == registry_before
    assert census == census_before


def test_real_repo_data_is_currently_in_sync():
    """Regression lock: the committed cic-website/data/world-census.json
    must stay in sync with records/worlds.yaml going forward. This is the
    same computation engine.m6.cli's `check` subcommand runs in CI - a
    failure here means someone edited the registry or hand-edited the
    census without running `python -m engine.m6.cli sync`."""
    from engine.m6.cli import CENSUS_PATH

    registry = load_registry()
    census = json.loads(CENSUS_PATH.read_text(encoding="utf-8"))
    _new_census, changes = sync_census(registry, census)
    assert changes == [], changes
