"""The optional reading card on quote and story records: every line names its
source, complicated_by ids resolve, the card stays at or under 120 words, and
the confidence comes from the five-level vocabulary. The gate is run by
engine/m9/enforce.py, not registered in GATES (that list is baked into every
package manifest)."""
import copy

from engine.m1 import gates
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import load_registry

QUOTE_ID = "alx.quote.a-doctrine-they-would-not-have-taught"
STORY_ID = "alx.story.arsinoite-conference"


def _world():
    return copy.deepcopy(load_world_records("alx"))


def _card():
    return {
        "setting": "Origen answers the pagan critic Celsus in a long written reply.",
        "source_says": "The disciples risked their lives to teach the resurrection, so they did not invent it.",
        "historians_conclude": {
            "text": "Scholars read this as an argument from sincerity, not as eyewitness testimony.",
            "confidence": "Documented",
        },
        "contributes": "It shows how this world defended its central claim in public argument.",
        "whose_view": "Origen's own argument. A leading teacher's reasoning is not the whole community's view.",
        "open": "The argument shows the disciples believed it, not that it happened.",
        "reads_differently_today": "Today it reads as an argument about sincerity, not about evidence.",
        "complicated_by": ["alx.quote.athanasius-death-trampled-down"],
        "sources": {
            "setting": "alx.source.origen-contra-celsum, Contra Celsum II.56",
            "source_says": "alx.source.origen-contra-celsum, Contra Celsum II.56",
            "historians_conclude": "Doc_05, section 3",
            "contributes": "alx.dw.resurrection",
            "whose_view": "Doc_05, section 3",
            "open": "alx.quote.a-doctrine-they-would-not-have-taught confidence.divergence_note",
            "reads_differently_today": "alx.quote.a-doctrine-they-would-not-have-taught modern_lens_note",
        },
    }


def _with_card(record_id=QUOTE_ID, card=None):
    records = _world()
    records[record_id]["reading_card"] = card if card is not None else _card()
    return records


def _card_findings(records):
    return gates.gate_reading_card(records, load_fleet_records(), load_registry())


def _schema_findings(records, record_id):
    return gates.gate_schema_validation({record_id: records[record_id]}, load_fleet_records(), load_registry())


def test_a_full_card_validates_on_a_quote_and_on_a_story():
    for record_id in (QUOTE_ID, STORY_ID):
        records = _with_card(record_id)
        assert _schema_findings(records, record_id) == []
        assert _card_findings(records) == []


def test_records_without_a_card_are_unchanged():
    records = _world()
    assert _card_findings(records) == []
    assert _schema_findings(records, QUOTE_ID) == []


def test_a_line_without_its_source_fails_the_gate():
    card = _card()
    del card["sources"]["whose_view"]
    found = _card_findings(_with_card(card=card))
    assert len(found) == 1
    assert found[0].startswith(f"{QUOTE_ID}.reading_card.whose_view: ")
    assert "names no source" in found[0]


def test_a_card_over_120_words_fails_the_gate():
    card = _card()
    card["source_says"] = " ".join(["The disciples taught it at the risk of their lives."] * 12)
    found = _card_findings(_with_card(card=card))
    assert len(found) == 1
    assert "words, over the 120-word ceiling" in found[0]


def test_a_card_at_120_words_passes():
    card = _card()
    other = sum(len(gates._WORD.findall(text)) for text in gates.reading_card_texts(card)) - len(gates._WORD.findall(card["source_says"]))
    card["source_says"] = " ".join(["word"] * (gates.READING_CARD_MAX_WORDS - other))
    assert _card_findings(_with_card(card=card)) == []


def test_a_complicated_by_id_that_does_not_exist_fails_the_gate():
    card = _card()
    card["complicated_by"] = ["alx.quote.no-such-record"]
    found = _card_findings(_with_card(card=card))
    assert found == [f"{QUOTE_ID}.reading_card.complicated_by: 'alx.quote.no-such-record' does not resolve to any record"]


def test_a_confidence_outside_the_vocabulary_fails_gate_and_schema():
    card = _card()
    card["historians_conclude"]["confidence"] = "Not Attested"
    records = _with_card(card=card)
    assert any("historians_conclude.confidence" in f for f in _card_findings(records))
    assert any("reading_card" in f for f in _schema_findings(records, QUOTE_ID))


def test_the_schema_rejects_an_unknown_line_and_a_source_for_an_unknown_line():
    card = _card()
    card["rank"] = "majority view"
    assert any("reading_card" in f for f in _schema_findings(_with_card(card=card), QUOTE_ID))
    card = _card()
    card["sources"]["rank"] = "Doc_05"
    assert any("reading_card" in f for f in _schema_findings(_with_card(card=card), QUOTE_ID))


def test_the_card_is_only_allowed_on_quote_and_story_records():
    records = _world()
    gravity_id = next(rid for rid, r in records.items() if r.get("record_type") == "gravity")
    records[gravity_id]["reading_card"] = _card()
    assert any("reading_card" in f for f in _schema_findings(records, gravity_id))


def test_the_gate_stays_out_of_gates():
    assert "reading-card" not in gates.GATES
