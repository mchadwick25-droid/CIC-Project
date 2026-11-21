"""The tree overlap check (tools/check_tree_overlap.py): a quote another story already uses is shared,
a brief's own census entry is not compared, and a name close to one on the tree is listed for a person to check."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from check_tree_overlap import check, main  # noqa: E402

CENSUS = {
    "movements": [
        {"id": "arius", "name": "Arius", "longDescription": 'Arius said, "There was a time when he was not." King Chlothar ruled.'},
        {"id": "nicaea", "name": "Council of Nicaea", "longDescription": 'The bishops wrote "of one being with the Father" into the creed.'},
        {"id": "jerome", "name": "Jerome", "longDescription": "",
         "card": {"quotationOriginals": [{"modern": "The whole world groaned and was amazed."}]}},
    ]
}


def test_a_quote_another_story_uses_is_shared():
    r = check({"nicaea": 'He taught, "There was a time when he was not."'}, CENSUS)
    assert r["nicaea"]["shared"] == [{"quote": "There was a time when he was not.", "in": ["arius"]}]


def test_a_card_quotation_counts_and_short_quotes_do_not():
    r = check({"new": 'Jerome wrote, "the whole world groaned and was amazed". They called him "the one".'}, CENSUS)
    assert [s["in"] for s in r["new"]["shared"]] == [["jerome"]]


def test_a_brief_is_not_compared_with_its_own_census_entry():
    r = check({"nicaea": 'The bishops wrote "of one being with the Father" into the creed.'}, CENSUS)
    assert r["nicaea"]["shared"] == []


def test_two_briefs_in_one_batch_are_compared():
    q = '"Love the work, and the work will keep you."'
    r = check({"a": "She wrote, " + q, "b": "Her abbess said, " + q}, CENSUS)
    assert r["a"]["shared"][0]["in"] == ["b"] and r["b"]["shared"][0]["in"] == ["a"]


def test_a_close_spelling_is_listed_and_a_known_name_is_not():
    r = check({"new": "Lothar married her. Arius had died. Chlothar's son ruled."}, CENSUS)
    assert r["new"]["spelling"] == [{"name": "Lothar", "tree": ["Chlothar"]}]


def test_main_exits_one_only_on_a_shared_quote(tmp_path):
    census = tmp_path / "census.json"
    census.write_text(json.dumps(CENSUS))
    shared = tmp_path / "x.brief.txt"
    shared.write_text('"There was a time when he was not."')
    spelled = tmp_path / "y.brief.txt"
    spelled.write_text("Lothar ruled.")
    assert main([str(shared), "--census", str(census)]) == 1
    assert main([str(spelled), "--census", str(census)]) == 0


def test_a_reuse_the_slate_allows_is_reported_and_does_not_fail(tmp_path):
    from check_tree_overlap import read_allow
    allow = tmp_path / "allow.txt"
    allow.write_text('nicaea: "There was a time when he was not."\n', encoding="utf-8")
    r = check({"nicaea": 'He taught, "There was a time when he was not."'}, CENSUS, read_allow(allow))
    assert r["nicaea"]["shared"] == []
    assert r["nicaea"]["reused"] == [{"quote": "There was a time when he was not.", "in": ["arius"]}]


def test_an_allowance_for_one_brief_does_not_cover_another(tmp_path):
    from check_tree_overlap import read_allow
    allow = tmp_path / "allow.txt"
    allow.write_text("other: There was a time when he was not.\n", encoding="utf-8")
    r = check({"nicaea": 'He taught, "There was a time when he was not."'}, CENSUS, read_allow(allow))
    assert len(r["nicaea"]["shared"]) == 1
