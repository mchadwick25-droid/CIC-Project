"""The question-ending gate: a spoken sentence never ends on a bare question
word."""
import pytest

from engine.m1 import gates
from engine.m1.loader import load_world_records
from engine.m1.question_endings import bare_question_hits, ends_on_bare_question_word, sentences

BARE = [
    "We cannot tell you we had settled how.",
    "We will not tell you why.",
    "So we cannot tell you why.",
    "Our record gives no answer to why.",
    "We just never wrote down when.",
    "We do not explain how.",
    "It does not preserve anyone explaining why.",
    "It recurs across named elders, but it is not settled why.",
    "Christ is truly present in the bread and wine, and we did not explain how.",
    "Eusebius, his own court panegyrist, is our only source for why.",
    "We asked no deeper questions about how.",
    "We never said where.",
    "Nobody told us who.",
    "We were not told which.",
    "Our sources do not say what.",
    "We cannot tell you why!",
    "We do not explain how.”",
    "the presence at the table, held without asking how",
]

NAMED = [
    "We cannot tell you we had settled how he could be God when the Father is God, and God is one.",
    "We did not explain how bread and wine become his body.",
    "Substance here is what a thing is; Person is who.",
    "X is who, not what.",
    "We never settled which is which.",
    "We kept no list of who reads what.",
    "No one wrote down who did what.",
    "The question is how much of the confession may be said aloud, to whom and when.",
    "It also meant knowing how much truth to say out loud, and when.",
    "Scholars dispute who wrote them, and when.",
    "What we left is where our teachers ranked marriage, and why.",
    "It may have been her own prudence, or our age's constraint - we cannot now tell you which.",
    "We cared less for the what than for the how.",
    "They passed on their know-how.",
    "Why?",
    "Where was God when it happened?",
    "We will not tell you why God allows such suffering.",
    "We do not know why he waited, and we say so.",
]


@pytest.mark.parametrize("sentence", BARE)
def test_a_sentence_ending_on_a_bare_question_word_is_flagged(sentence):
    assert ends_on_bare_question_word(sentence)


@pytest.mark.parametrize("sentence", NAMED)
def test_a_sentence_that_names_its_question_is_not_flagged(sentence):
    assert not ends_on_bare_question_word(sentence)


def test_sentences_split_on_end_marks_and_keep_a_final_unpunctuated_one():
    assert sentences("We do not explain how. We take him at his word! Is that enough? and the rest") == [
        "We do not explain how.", "We take him at his word!", "Is that enough?", "and the rest",
    ]


def _record(rid, record_type, **fields):
    return {"id": rid, "record_type": record_type, **fields}


def test_hits_cover_spoken_fields_and_the_use_note_meaning():
    records = {
        r["id"]: r
        for r in [
            _record("zzz.term.a", "term", plain_meaning="Christ is present. We do not explain how.",
                    use_note={"means": "Christ present, taken at his word without explaining how."}),
            _record("zzz.limit.a", "honest_limit", statement="We cannot tell you why the brothers died."),
        ]
    }
    hits = bare_question_hits(records)
    assert ("zzz.term.a", "plain_meaning", "We do not explain how.") in hits
    assert ("zzz.term.a", "use_note.means", "Christ present, taken at his word without explaining how.") in hits
    assert not [h for h in hits if h[0] == "zzz.limit.a"]


def test_source_wording_participant_turns_and_analytic_records_are_not_read():
    records = {
        r["id"]: r
        for r in [
            _record("zzz.quote.a", "quote", text="He would not say why."),
            _record("zzz.demo.a", "demonstration", exchange=[
                {"speaker": "participant", "text": "Can you tell me why."},
                {"speaker": "representative", "text": "We cannot tell you why God allows it."},
            ]),
            _record("zzz.term.b", "term", voice="analytic", plain_meaning="We do not explain how."),
        ]
    }
    assert bare_question_hits(records) == []


def test_the_gate_is_registered_and_reports_each_sentence():
    assert gates.GATES["question-ending"] is gates.gate_question_ending
    records = {"zzz.term.a": _record("zzz.term.a", "term", plain_meaning="We do not explain how.")}
    findings = gates.gate_question_ending(records, {}, {})
    assert len(findings) == 1
    assert findings[0].startswith("zzz.term.a.plain_meaning: ends on a bare question word")


@pytest.mark.parametrize("code", ["alx", "cappadocian", "desert", "don", "fix", "gallic", "hal", "ijc", "pahc", "rzg", "syr", "witt"])
def test_no_built_world_ends_a_spoken_sentence_on_a_bare_question_word(code):
    assert bare_question_hits(load_world_records(code)) == []
