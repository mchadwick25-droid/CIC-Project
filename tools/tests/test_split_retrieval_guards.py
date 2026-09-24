"""Stage 4a (parts 2-3), R11: pins split_retrieval_guards.split_frontmatter's
raw-text splice against constructed examples first (exact line shape, not
just parsed content), then checks the real fleet-wide migration's counts
match the 5 guard records Stage 1's own D1 measurement already named, and
that all 11 built worlds are genuinely done."""
from pathlib import Path

import yaml

from tools.split_retrieval_guards import _FRONTMATTER, is_guard, migrate_world, split_frontmatter

REPO_ROOT = Path(__file__).resolve().parents[2]

_PLAIN_RECORD = """id: x.term.example
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks about X"
  do_not_retrieve_when:
  - "participant asks about Y - retrieve x.term.y"
text: >-
  some prose
"""

_GUARD_RECORD = """id: x.story.example
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks about X"
  do_not_retrieve_when:
  - "participant asks who succeeded them - our vendored evidence does not say, and the Representative must not supply it"
  - "participant asks about Z - retrieve x.term.z"
relations:
- type: associated-with
  target: x.figure.someone
"""

_WRAPPED_ITEM_RECORD = """id: x.figure.example
retrieval:
  tier: 1
  do_not_retrieve_when:
  - participant wants a personal biography beyond the nine linked stories -
    this library does not attest one and must not invent detail
text: >-
  some prose
"""


def test_is_guard_matches_the_stage_1_marker_set():
    assert is_guard("our vendored evidence does not say")
    assert is_guard("the Representative must not supply it")
    assert not is_guard("participant asks about Y - retrieve x.term.y")


def test_plain_record_becomes_prefer_instead_in_place_no_claim_guards():
    new_fm, change = split_frontmatter(_PLAIN_RECORD)
    assert change == {"prefer_instead": 1, "claim_guards": 0}
    assert "do_not_retrieve_when" not in new_fm
    assert "claim_guards" not in new_fm
    assert '  prefer_instead:\n  - "participant asks about Y - retrieve x.term.y"\n' in new_fm
    # everything else survives byte-for-byte
    assert 'text: >-\n  some prose\n' in new_fm


def test_guard_record_splits_into_both_fields_correctly_placed():
    new_fm, change = split_frontmatter(_GUARD_RECORD)
    assert change == {"prefer_instead": 1, "claim_guards": 1}
    lines = new_fm.splitlines()
    # prefer_instead stays nested at 2-indent, in retrieval's own position
    assert '  prefer_instead:' in lines
    assert '  - "participant asks about Z - retrieve x.term.z"' in lines
    # claim_guards is a new top-level (0-indent) key, dedented from its
    # old 2-indent do_not_retrieve_when position
    assert 'claim_guards:' in lines
    guard_idx = lines.index('claim_guards:')
    assert lines[guard_idx + 1] == '- "participant asks who succeeded them - our vendored evidence does not say, and the Representative must not supply it"'
    # claim_guards lands right after the retrieval: block, before relations:
    assert lines[guard_idx + 2] == 'relations:'


def test_wrapped_multiline_item_classifies_and_dedents_as_one_unit():
    new_fm, change = split_frontmatter(_WRAPPED_ITEM_RECORD)
    assert change == {"prefer_instead": 0, "claim_guards": 1}
    lines = new_fm.splitlines()
    guard_idx = lines.index('claim_guards:')
    assert lines[guard_idx + 1].startswith('- participant wants a personal biography')
    # the continuation line dedents with the item, keeping its own relative indent
    assert lines[guard_idx + 2].startswith('  this library does not attest')


def test_record_with_no_do_not_retrieve_when_is_left_alone():
    fm = 'id: x.term.plain\nretrieval:\n  tier: 1\ntext: >-\n  prose\n'
    assert split_frontmatter(fm) is None


def test_inline_empty_list_is_dropped_with_nothing_injected():
    """The dominant real shape fleet-wide (525 records) - a field present
    but never populated. Nothing to redirect, nothing to guard."""
    fm = 'id: x.term.example\nretrieval:\n  tier: 3\n  retrieve_when: []\n  do_not_retrieve_when: []\nrelations: []\n'
    new_fm, change = split_frontmatter(fm)
    assert change == {"prefer_instead": 0, "claim_guards": 0}
    assert "do_not_retrieve_when" not in new_fm
    assert "prefer_instead" not in new_fm
    assert "claim_guards" not in new_fm
    assert new_fm == 'id: x.term.example\nretrieval:\n  tier: 3\n  retrieve_when: []\nrelations: []\n'


def test_gallic_is_already_migrated_with_exactly_the_five_known_guard_records():
    """gallic was the pilot world (Build-Plan.md's own "gallic first"
    ordering) and is already migrated for real on disk - this pins that
    outcome as a regression check rather than re-running the (now
    inapplicable, since do_not_retrieve_when no longer exists here)
    dry run."""
    world_dir = REPO_ROOT / "records" / "gallic"
    guard_hits = {}
    for path in sorted(world_dir.glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        assert "do_not_retrieve_when:" not in text, path
        doc = yaml.safe_load(_FRONTMATTER.match(text).group(1))
        guards = doc.get("claim_guards")
        if guards:
            assert isinstance(doc.get("retrieval"), dict)
            guard_hits[doc["id"]] = (len(doc["retrieval"].get("prefer_instead") or []), len(guards))
    assert guard_hits == {
        "gallic.story.brictio-in-the-courtyard": (2, 1),
        "gallic.story.germanus-scruple-at-morning-service": (3, 1),
        "gallic.story.honoratus-and-the-island": (2, 1),
        "gallic.story.the-angel-and-the-twelve-psalms": (2, 1),
        "gallic.term.mortification": (3, 1),
    }


def test_migrate_world_finds_nothing_left_to_do_on_the_already_migrated_gallic():
    assert migrate_world("gallic", dry_run=True) == []


def test_every_rewritten_fix_frontmatter_still_parses_as_valid_yaml():
    """fix (the fixture world used by the M1 gate battery selftest) is
    deliberately out of scope for the real fleet migration - it is not one
    of the 11 built worlds Build-Plan.md and Decision-Log.md's own "714
    lines fleet-wide" count ever refers to - so it stays real,
    do_not_retrieve_when-bearing, and permanently unmigrated. A durable
    dry-run target for this shape check, unlike a real fleet world (all 11
    are migrated for real as of this stage)."""
    touched = 0
    for path in sorted((REPO_ROOT / "records" / "fix").glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        m = _FRONTMATTER.match(text)
        if not m or "do_not_retrieve_when:" not in m.group(1):
            continue
        result = split_frontmatter(m.group(1))
        assert result is not None, path
        touched += 1
        new_fm, _ = result
        doc = yaml.safe_load(new_fm)
        assert isinstance(doc, dict)
        assert "do_not_retrieve_when" not in (doc.get("retrieval") or {})
    assert touched > 0  # fix genuinely has do_not_retrieve_when records to check against


_FLEET_WORLDS = ("alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "pahc", "rzg", "syr", "witt")


def test_the_whole_fleet_is_migrated_with_nothing_left_to_do():
    for world in _FLEET_WORLDS:
        assert migrate_world(world, dry_run=True) == [], world
        for path in sorted((REPO_ROOT / "records" / world).glob("*/*.md")):
            assert "do_not_retrieve_when:" not in path.read_text(encoding="utf-8"), path
