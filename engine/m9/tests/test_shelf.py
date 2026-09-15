from engine.m9.shelf import build_shelf


def _bucket_rows():
    return [
        {
            "row_id": "w--a", "work": "Work A", "author": "Author A",
            "source_file": "a.txt", "locus": "whole document", "locus_ids": ["whole-file"],
            "role": "tradition", "confidence": "assigned",
        },
        {
            "row_id": "w--b", "work": "Work B", "author": "Author B",
            "source_file": "b.txt", "locus": "whole document", "locus_ids": ["whole-file"],
            "role": "context", "confidence": "assigned",
            "voice_of": "neighbour", "documented_exchange": "confirmed",
        },
        {"row_id": None, "work": "No id yet", "source_file": "c.txt", "role": "context", "confidence": "provisional"},
    ]


def test_rows_without_row_id_are_skipped_but_still_mark_their_file():
    """rows (shelf_row's own target) requires a real CM-1 id; files
    (verbatim-in-shelf's target) does not - Direction B was measured real
    on real fleet data months before CM-1 existed anywhere (Q7-B)."""
    shelf = build_shelf(
        world_key="w", census_id="w", bucket_rows=_bucket_rows(),
        pairs_list=[], parties={}, units_by_file={}, vendored_files=frozenset(),
    )
    assert set(shelf.rows) == {"w--a", "w--b"}
    assert "c.txt" in shelf.files
    assert shelf.files["c.txt"] == ["(unaddressable)"]


def test_files_derived_at_file_grain():
    shelf = build_shelf(
        world_key="w", census_id="w", bucket_rows=_bucket_rows(),
        pairs_list=[], parties={}, units_by_file={}, vendored_files=frozenset(),
    )
    assert shelf.files == {"a.txt": ["w--a"], "b.txt": ["w--b"], "c.txt": ["(unaddressable)"]}


def test_row_carries_voice_of_and_documented_exchange():
    shelf = build_shelf(
        world_key="w", census_id="w", bucket_rows=_bucket_rows(),
        pairs_list=[], parties={}, units_by_file={}, vendored_files=frozenset(),
    )
    assert shelf.rows["w--b"]["voice_of"] == "neighbour"
    assert shelf.rows["w--b"]["documented_exchange"] == "confirmed"
    assert shelf.rows["w--a"]["voice_of"] is None


def test_pairs_keyed_by_frozenset_both_directions():
    pairs_list = [{"a": "w", "b": "neighbour", "relation": "mutual-awareness", "confidence": "assigned"}]
    shelf = build_shelf(
        world_key="w", census_id="w", bucket_rows=[],
        pairs_list=pairs_list, parties={}, units_by_file={}, vendored_files=frozenset(),
    )
    assert shelf.pairs[frozenset({"w", "neighbour"})]["relation"] == "mutual-awareness"
    assert shelf.pairs[frozenset({"neighbour", "w"})] is shelf.pairs[frozenset({"w", "neighbour"})]


def test_pair_missing_a_or_b_is_skipped():
    pairs_list = [{"a": "w", "relation": "mutual-awareness"}]
    shelf = build_shelf(
        world_key="w", census_id="w", bucket_rows=[],
        pairs_list=pairs_list, parties={}, units_by_file={}, vendored_files=frozenset(),
    )
    assert shelf.pairs == {}


def test_units_and_vendored_files_passed_through():
    shelf = build_shelf(
        world_key="w", census_id="w", bucket_rows=[], pairs_list=[], parties={},
        units_by_file={"a.txt": "some text"}, vendored_files=frozenset({"a.txt", "z.txt"}),
    )
    assert shelf.units == {"a.txt": "some text"}
    assert shelf.vendored_files == frozenset({"a.txt", "z.txt"})
