"""A sentence naming something after the world's window closes is removed by
apply_net unless a record the sentence cites names it too. Fixture records
only; no model call."""
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import apply_net

RECORDS = {
    "fix.witness.later": {
        "id": "fix.witness.later", "record_type": "doctrinal_witness",
        "text": "Later people said he founded the choirs himself, but that tradition appears only around 500.",
    },
    "fix.witness.core": {
        "id": "fix.witness.core", "record_type": "doctrinal_witness",
        "text": "We kept the fast on the fourth day and on the Sabbath eve.",
    },
}
COUNCIL = "That council met in 451, and our last bishop died in 430."


def _net(raw, window_end):
    return apply_net(raw, repository_records=RECORDS, thin_topics=None, placement=PlacementContext(), window_end=window_end)


def test_a_sentence_naming_a_year_after_the_window_is_removed():
    raw = f"We were not at that council. {COUNCIL} What happened after our years is not ours to tell."
    text, _c, net_result = _net(raw, 430)
    assert text == "We were not at that council. What happened after our years is not ours to tell."
    [removed] = net_result["reply_shape"]["removed"]
    assert removed["sentence"] == COUNCIL and "after the world's window" in removed["why"]


def test_a_cited_record_that_names_the_later_year_keeps_the_sentence():
    raw = "Later people said he founded the choirs himself, but that tradition appears only around 500 [[fix.witness.later]]."
    text, citations, net_result = _net(raw, 410)
    assert "around 500" in text and citations and net_result["reply_shape"]["removed"] == []


def test_a_cited_record_that_does_not_name_it_does_not_keep_the_sentence():
    raw = f"We kept the fast. {COUNCIL.rstrip('.')} [[fix.witness.core]]."
    text, _c, net_result = _net(raw, 430)
    assert "451" not in text and len(net_result["reply_shape"]["removed"]) == 1


def test_no_window_removes_nothing():
    raw = f"We kept the fast [[fix.witness.core]]. {COUNCIL}"
    text, _c, net_result = _net(raw, None)
    assert "451" in text and net_result["reply_shape"]["removed"] == []


def test_a_year_inside_the_window_stays():
    raw = "Cyprian died in 258, and we kept the fast [[fix.witness.core]]."
    text, _c, net_result = _net(raw, 430)
    assert "258" in text and net_result["reply_shape"]["removed"] == []


def test_the_syr_choirs_sentence_that_names_the_later_tradition_survives_in_its_world():
    from engine.m1.loader import load_world_records

    records = load_world_records("syr")
    raw = (
        "Later people said he founded and led the women's choirs himself, but that tradition appears only around 500 - "
        "generations after he died [[syr.story.choirs-tradition]]."
    )
    text, citations, net_result = apply_net(raw, repository_records=records, thin_topics=None, placement=PlacementContext(), window_end=410)
    assert "around 500" in text and citations and net_result["reply_shape"]["removed"] == []


def test_the_lpc_chalcedon_year_is_removed_though_it_cites_the_world_core():
    from engine.m1.loader import load_world_records

    records = load_world_records("lpc")
    core = "lpc.core.latin-pastoral-congregational-christianity"
    raw = f"We were not at Chalcedon. That council met in 451, and our last bishop died in 430, while the Vandals stood outside his own city's walls [[{core}]]. What happened after our years is not ours to tell."
    text, _c, net_result = apply_net(raw, repository_records=records, thin_topics=None, placement=PlacementContext(), window_end=430)
    assert "451" not in text and "not ours to tell" in text
    assert [r["why"] for r in net_result["reply_shape"]["removed"]] == ["names something after the world's window closes that its own cited records do not"]
