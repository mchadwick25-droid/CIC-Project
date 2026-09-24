"""Hermetic tests for engine.m1.sentence_completeness: the main-clause
rules against hand-built parse trees (no spaCy model in CI - see the
module docstring), the sentence splitter, the readings a sentence is
tried under, the any-reading-whole rule across parsers, and sweep_world's
aggregation over quote records. The real parser is exercised by the
module's own calibration step against KNOWN_CASES on every CLI run."""
from engine.m1.sentence_completeness import (
    NO_FINITE_VERB,
    NO_SUBJECT,
    classify_root,
    classify_sentence,
    readings,
    split_sentences,
    sweep_world,
)


class Tok:
    def __init__(self, text, tag, dep, children=()):
        self.text = text
        self.lower_ = text.lower()
        self.tag_ = tag
        self.dep_ = dep
        self.children = list(children)


def root(text, tag, *children):
    return Tok(text, tag, "ROOT", children)


def test_whole_sentence_with_subject_and_finite_verb():
    assert classify_root(root("showed", "VBD", Tok("He", "PRP", "nsubj"))) is None


def test_finite_auxiliary_makes_a_participle_root_finite():
    r = root("gone", "VBN", Tok("He", "PRP", "nsubj"), Tok("has", "VBZ", "aux"))
    assert classify_root(r) is None


def test_non_verb_root_is_no_finite_verb():
    # "Of his Deity, by his miracles ..." - the parse root is the preposition.
    assert classify_root(root("Of", "IN")) == NO_FINITE_VERB


def test_participle_without_finite_auxiliary_is_no_finite_verb():
    assert classify_root(root("made", "VBN", Tok("vessels", "NNS", "nsubjpass"))) == NO_FINITE_VERB


def test_infinitive_root_is_no_finite_verb_not_imperative():
    assert classify_root(root("learn", "VB", Tok("to", "TO", "aux"))) == NO_FINITE_VERB


def test_modal_mislabelled_as_subject_counts_as_finite_not_as_subject():
    # The real misparse of "... which might, as she saw, be made to my statements."
    r = root("made", "VBN", Tok("might", "MD", "nsubjpass"), Tok("be", "VB", "auxpass"))
    assert classify_root(r) == NO_SUBJECT


def test_imperative_is_whole():
    assert classify_root(root("Love", "VB", Tok("enemies", "NNS", "dobj"))) is None


def test_negative_imperative_with_do_support_is_whole():
    r = root("reason", "VB", Tok("Do", "VBP", "aux"), Tok("not", "RB", "neg"))
    assert classify_root(r) is None


def test_subjunctive_is_whole():
    # "To you be the glory forever."
    assert classify_root(root("be", "VB", Tok("glory", "NN", "nsubj"))) is None


def test_finite_verb_without_subject_is_no_subject():
    assert classify_root(root("held", "VBD", Tok("back", "RP", "prt"))) == NO_SUBJECT


def test_expletive_counts_as_subject():
    assert classify_root(root("is", "VBZ", Tok("There", "EX", "expl"))) is None


def test_split_sentences_keeps_ellipsis_and_closing_quotes():
    text = "At one point I said, 'with the Son.' At another, 'through the Son.' Some attacked me... Then they left."
    assert split_sentences(text) == [
        "At one point I said, 'with the Son.'",
        "At another, 'through the Son.'",
        "Some attacked me...",
        "Then they left.",
    ]


def test_split_sentences_does_not_break_before_lowercase():
    assert split_sentences("He came, i.e. he returned. It ended.") == ["He came, i.e. he returned.", "It ended."]


def test_readings_strip_label_and_leading_connective():
    assert readings("Question: And is it so?") == ["Question: And is it so?", "And is it so?", "is it so?"]
    assert readings("For the heart is a deep gulf.") == ["For the heart is a deep gulf.", "the heart is a deep gulf."]
    assert readings("He came.") == ["He came."]


class FakeDoc(list):
    pass


def fake_parser(whole_readings):
    """Parses a reading as whole iff it is in whole_readings; otherwise as
    a verbless fragment."""

    def parse(text):
        if text in whole_readings:
            return FakeDoc([root("is", "VBZ", Tok("it", "PRP", "nsubj"))])
        return FakeDoc([root("Of", "IN")])

    return parse


def test_sentence_is_whole_if_any_parser_finds_it_whole():
    s = "Silver couches."
    assert classify_sentence([fake_parser(set()), fake_parser({s})], s) is None


def test_sentence_is_whole_if_any_reading_is_whole():
    s = "For the heart is a deep gulf."
    assert classify_sentence([fake_parser({"the heart is a deep gulf."})], s) is None


def test_sentence_flagged_only_when_every_parser_and_reading_flags_it():
    assert classify_sentence([fake_parser(set()), fake_parser(set())], "Silver couches.") == NO_FINITE_VERB


def test_doc_with_no_root_is_no_finite_verb():
    assert classify_sentence([lambda text: FakeDoc([])], "...") == NO_FINITE_VERB


def test_sweep_world_counts_only_quote_renderings_and_quotes_flagged_sentences():
    records = {
        "w.quote.a": {"record_type": "quote", "modern_rendering": "It is whole. Silver couches."},
        "w.quote.b": {"record_type": "quote", "modern_rendering": "It is whole."},
        "w.quote.c": {"record_type": "quote", "text": "no rendering"},
        "w.term.d": {"record_type": "term", "modern_rendering": "Silver couches."},
    }
    parsers = [fake_parser({"It is whole."})]
    result = sweep_world("w", parsers, load=lambda _world: records)
    assert result["total_quotes"] == 3
    assert result["renderings_checked"] == 2
    assert result["sentences_checked"] == 3
    assert result["renderings_flagged"] == 1
    assert result["category_counts"] == {NO_FINITE_VERB: 1, NO_SUBJECT: 0}
    assert result["findings"] == [
        {"id": "w.quote.a", "flagged_sentences": [{"sentence": "Silver couches.", "category": NO_FINITE_VERB}]}
    ]
