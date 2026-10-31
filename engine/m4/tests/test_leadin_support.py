"""A quote's lead-in may state a detail only a source document supports: the
quote's record, its speaker's figure record, a source record, or the edition
text around its cited lines. Anything else is replaced by code's plain lead-in.
The three examples are the project lead's, settled against the real sources."""
import json
from pathlib import Path

import pytest

from engine.m4.leadin_support import REPO_ROOT, check_leadin, extract_details
from engine.m4.quote_placement import PlacementContext, REPAIR_LEAD_IN_UNSUPPORTED, place_quotes

RENDERING = "No repentance is too late while a man still lives."
RECORDS = {
    "fix.figure.cyprian": {
        "id": "fix.figure.cyprian", "record_type": "figure",
        "names": [{"name": "Cyprian", "tag": "in-world"}], "display": "Cyprian, our bishop at Carthage",
    },
    "fix.source.address": {"id": "fix.source.address", "record_type": "source", "author": "Cyprian", "work": "An Address to Demetrianus"},
    "fix.quote.late": {
        "id": "fix.quote.late", "record_type": "quote", "speaker_or_author": "fix.figure.cyprian",
        "modern_rendering": RENDERING, "use_note": {"means": "No one is too late to turn."},
        "sources": [{"source_id": "fix.source.address", "locus": "To Demetrianus, section 25"}],
    },
}
OFFERED = PlacementContext(offered=frozenset({"fix.quote.late"}))


def _place(text, records=RECORDS, context=OFFERED):
    return place_quotes(text, repository_records=records, context=context)


def _words(name="cyprian"):
    return frozenset({name})


def test_a_detail_the_quote_record_states_is_supported_and_its_span_is_kept():
    checked = check_leadin("Cyprian wrote to Demetrianus", RECORDS["fix.quote.late"], RECORDS, speaker_words=_words())
    assert checked["unresolved"] == []
    assert {d["detail"] for d in checked["supported"]} >= {"Demetrianus"}
    assert next(d for d in checked["supported"] if d["detail"] == "Demetrianus")["span"] == "record fix.quote.late"


def test_a_detail_only_another_record_states_is_supported_by_that_record():
    checked = check_leadin("Cyprian, as bishop at Carthage, said", RECORDS["fix.quote.late"], RECORDS, speaker_words=_words())
    assert checked["unresolved"] == []
    assert {d["span"] for d in checked["supported"]} == {"record fix.figure.cyprian"}


def test_a_detail_only_the_edition_states_is_supported_by_the_edition(tmp_path):
    (tmp_path / "cic" / "texts").mkdir(parents=True)
    lines = ["<DC.Title>Homilies on the Gospel of John</DC.Title>"] + ["filler"] * 50 + [
        '<div2 type="Tractate" title="Chapter VII." n="XXXIII">', "You remember, my beloved, what we said to you."]
    (tmp_path / "cic" / "texts" / "ed.xml").write_text("\n".join(lines), encoding="utf-8")
    record = {"id": "fix.quote.w", "record_type": "quote", "speaker_or_author": "fix.figure.cyprian",
              "sources": [{"locus": "Tractate 33, cic/texts/ed.xml, lines 52-53"}]}
    checked = check_leadin("Cyprian preached on this", record, {**RECORDS, "fix.quote.w": record}, speaker_words=_words(), texts_root=tmp_path)
    assert checked["unresolved"] == []
    assert checked["supported"][0]["span"].startswith("cic/texts/ed.xml")


def test_a_detail_no_source_states_is_unresolved():
    checked = check_leadin("Cyprian wrote to Fortunatus in Rome", RECORDS["fix.quote.late"], RECORDS, speaker_words=_words())
    assert {d["detail"] for d in checked["unresolved"]} == {"Fortunatus", "Rome"}


def test_what_a_record_says_the_speaker_must_not_claim_supports_nothing():
    record = {**RECORDS["fix.quote.late"], "not_for": ["a claim that Cyprian was a bishop of Rome"]}
    checked = check_leadin("Cyprian, as presbyter, said", record, {**RECORDS, "fix.quote.late": record}, speaker_words=_words())
    assert [d["detail"] for d in checked["unresolved"]] == ["presbyter"]
    checked = check_leadin("Cyprian, as bishop of Rome, said", record, {**RECORDS, "fix.quote.late": record}, speaker_words=_words())
    assert {d["detail"] for d in checked["unresolved"]} == {"Rome"}


def test_a_time_relation_no_source_states_is_unresolved():
    checked = check_leadin("Cyprian, a century and a half earlier, said", RECORDS["fix.quote.late"], RECORDS, speaker_words=_words())
    assert [d["kind"] for d in checked["unresolved"]] == ["time"]


def test_a_lead_in_with_no_added_detail_needs_no_support():
    assert extract_details("Cyprian said", _words()) == []
    assert extract_details("In today's English, Cyprian says", _words()) == []


def test_placement_keeps_a_supported_lead_in_and_records_its_support():
    shaped = _place("Cyprian wrote to Demetrianus [[quote:fix.quote.late]].")
    assert shaped["text"].startswith("Cyprian wrote to Demetrianus: “")
    assert shaped["repaired"] == []
    assert any(d["detail"] == "Demetrianus" for d in shaped["leadin_support"]["fix.quote.late"])


def test_placement_replaces_an_unsupported_lead_in_with_codes_and_still_places_the_quote():
    shaped = _place("Cyprian wrote to Fortunatus [[quote:fix.quote.late]].")
    assert shaped["placed"] == ["fix.quote.late"]
    assert shaped["text"].startswith("In today's English, Cyprian says: “")
    assert shaped["repaired"][0]["why"] == REPAIR_LEAD_IN_UNSUPPORTED
    assert [d["detail"] for d in shaped["repaired"][0]["unresolved"]] == ["Fortunatus"]
    assert shaped["leadin_support"] == {}


# The three examples, against the real records and vendored editions.

@pytest.fixture(scope="module")
def lpc():
    from engine.m1.loader import load_world_records

    return load_world_records("lpc")


@pytest.mark.parametrize("quote_id, lead, speaker", [
    ("lpc.quote.let-it-be-the-office-of-love-to-feed-the-flock", "Here is how Augustine, as bishop at Hippo, spoke of the duty of those who feed Christ's flock", "augustine"),
    ("lpc.quote.no-repentance-is-too-late", "Cyprian wrote to Demetrianus", "cyprian"),
    ("lpc.quote.the-wretched-woman-and-mercy", "Augustine preached on the Gospel of the woman and her accusers", "augustine"),
])
def test_the_three_examples_are_supported_by_the_sources(lpc, quote_id, lead, speaker):
    checked = check_leadin(lead, lpc[quote_id], lpc, speaker_words=frozenset({speaker}), texts_root=REPO_ROOT)
    assert checked["unresolved"] == [], checked
    assert checked["supported"]


def test_the_supporting_span_reaches_the_transparency_element_of_the_quote():
    from engine.m4.transparency_plan import build_transparency_plan
    from engine.m4.turn import apply_net

    text, citations, net_result = apply_net(
        "Cyprian wrote to Demetrianus [[quote:fix.quote.late]].",
        repository_records=RECORDS, thin_topics=None, placement=OFFERED, quotable_texts=None,
    )
    plan = build_transparency_plan(citations=citations, net_result=net_result, repository_records=RECORDS, world_key="fix", text=text)
    quote = next(e for e in plan["elements"] if e["kind"] == "quote")
    assert any(d["detail"] == "Demetrianus" and d["span"] == "record fix.quote.late" for d in quote["leadin_support"])
    text, citations, net_result = apply_net(
        "Cyprian wrote to Fortunatus [[quote:fix.quote.late]].",
        repository_records=RECORDS, thin_topics=None, placement=OFFERED, quotable_texts=None,
    )
    plan = build_transparency_plan(citations=citations, net_result=net_result, repository_records=RECORDS, world_key="fix", text=text)
    assert "leadin_support" not in next(e for e in plan["elements"] if e["kind"] == "quote")
