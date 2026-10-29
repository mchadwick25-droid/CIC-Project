import pytest

from answering_library.union import WORLD_KEYS, build_union


@pytest.fixture(scope="module")
def entries():
    return build_union()


def test_union_covers_the_twelve_worlds_once_per_file(entries):
    names = [e.filename for e in entries]
    assert len(names) == len(set(names)) == 338
    assert sum(1 for e in entries if e.suffix == ".txt") == 305
    assert sum(1 for e in entries if e.suffix == ".xml") == 33
    assert [e.size for e in entries] == sorted((e.size for e in entries), reverse=True)


def test_every_entry_lists_its_worlds_and_rows(entries):
    assert set(WORLD_KEYS) == {w for e in entries for w in e.worlds}
    assert all(e.worlds and e.row_ids for e in entries)
    assert any(len(e.worlds) > 1 for e in entries)
