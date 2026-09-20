"""What the shared prose primitives actually do.

engine/prose.py is 300-odd lines under five production modules - the cell
keyword corpus (whether a question reaches any ground), compile-time
demonstration tagging, Stage A/B retrieval scoring, and every per-sentence
grounding verdict. Until this file it had no test of its own: it was
exercised only sideways, through engine/m4/tests/test_grounding_net.py,
which tests the net's policy rather than the measurement underneath it.

These are characterization tests. They assert what the code does today,
including several behaviours that are surprising and load-bearing - a
number is not a word, a two-letter word is not a word, a sentence of pure
stopwords is perfectly grounded. Each one is named for its consequence
downstream, not for the function it calls, because the reason to pin it is
that changing it silently changes what a Representative may say.
"""
import pytest

from engine import prose


# ---------------------------------------------------------------- all_text

def test_all_text_walks_nested_records():
    rec = {"text": "kept", "nested": {"inner": "also kept"}}
    assert prose.all_text(rec) == "kept also kept"


def test_all_text_drops_the_build_notes_body():
    """engine/m1/loader.py: "The body is provenance/build notes only - never
    read by any builder." _body is in NON_PROSE_KEYS, so no amount of
    build-note prose can leak into a keyword corpus or a citation."""
    rec = {"text": "real prose", "_body": "how this record was built"}
    assert prose.all_text(rec) == "real prose"


def test_all_text_drops_identifiers_so_slugs_never_become_keywords():
    rec = {"id": "alx.doctrinal_witness.clement", "text": "real prose"}
    assert prose.all_text(rec) == "real prose"


def test_a_list_inherits_the_key_it_hangs_under():
    """Filtering is by key name at any depth, and a list's items are walked
    under the parent's key - so a list of ids is dropped whole, not
    item-by-item."""
    assert prose.all_text({"id": ["a.b.c", "d.e.f"], "tags": ["kept"]}) == "kept"


def test_non_string_values_are_not_text():
    """Ints and bools are dropped rather than stringified, so a year stored
    as a number contributes nothing to any lexical score."""
    assert prose.all_text({"year": 340, "sealed": True, "text": "prose"}) == "prose"


# ----------------------------------------------------------- content_words

def test_digits_are_not_content_words():
    """_WORD is [a-zA-Z']+. A question about a figure can never match a
    record on the figure itself - only on the words around it. This is the
    single most consequential rule in the file: combined with the cell
    matcher's two-word floor, "how many monks in 340?" carries exactly one
    matchable word."""
    assert prose.content_words("300 monks lived by the Nile in 340") == {
        "monks", "lived", "nile",
    }


def test_words_of_three_letters_or_fewer_are_dropped():
    """len(w) > 2 after stopword removal, so "war", "law" and "God" survive
    at three letters but "ox" does not."""
    words = prose.content_words("we go by law and by war and by an ox")
    assert words == {"law", "war"}


def test_a_hyphenated_word_is_two_words():
    assert prose.content_words("a well-known God-bearer") == {
        "well", "known", "god", "bearer",
    }


def test_an_apostrophe_stays_inside_the_word():
    """"god's" is one token, not "god" - so a record saying "God's word"
    does not lexically match a query saying "God"."""
    assert prose.content_words("God's own word") == {"god's", "word"}


# --------------------------------------------------------------- sentences

def test_a_sentence_break_needs_whitespace_after_the_stop():
    assert prose.sentences("One.Two. Three.") == ["One.Two.", "Three."]


def test_no_text_is_no_sentences():
    assert prose.sentences("") == []
    assert prose.sentences(None) == []


def test_an_abbreviation_splits_a_sentence():
    """Known and deliberately unfixed. "c." (circa) is the common case, and
    it appears 400+ times in records/ - but every one of those sits in a
    _body provenance block or a citation string, which all_text drops. The
    corpus invariant below is what keeps that true; this test just records
    that the splitter itself has no abbreviation table."""
    assert prose.sentences("Antony withdrew c. 285 to the desert.") == [
        "Antony withdrew c.", "285 to the desert.",
    ]


def test_no_demonstration_sentence_splits_on_an_abbreviation():
    """The invariant that makes the test above harmless.

    Only one production path sentence-splits record text: the compiler
    tagging a demonstration's representative turns
    (engine.m2.builders._tag_representative_text). Every other record is
    read word-wise - content_words(all_text(record)) for the keyword
    corpus and for both ratio scores - where sentence boundaries do not
    exist. So this is scoped to what actually gets split, not to all
    record prose.

    Measured across all six worlds: 444 demonstration sentences, 0 split
    at an abbreviation. Figure and contested records DO carry "c. 251-356"
    and would split - 457 such sentences exist in the corpus - but nothing
    splits them, which is why this test does not look there.

    Not covered here: the live net splits MODEL OUTPUT, and a
    Representative writing "c. 285" would split the same way. No record
    test can hold that; it would need a live-turn measurement.
    """
    import re

    from engine.m1 import loader, registry

    abbrevs = {"c", "ca", "cf", "e", "g", "i", "st", "ss", "vs", "al",
               "ad", "bc", "ce", "bce", "fl"}
    tail = re.compile(r"\b([A-Za-z]{1,4})\.$")
    checked = 0
    offenders = []
    for key in registry.formation_world_keys():
        for record_id, record in loader.load_world_records(key).items():
            if record.get("record_type") != "demonstration":
                continue
            for turn in record.get("exchange") or []:
                if turn.get("speaker") != "representative":
                    continue
                for sentence in prose.quote_aware_sentences(turn["text"]):
                    checked += 1
                    match = tail.search(sentence.strip())
                    if match and match.group(1).lower() in abbrevs:
                        offenders.append((record_id, sentence.strip()[-60:]))
    assert checked > 400, f"expected the full demonstration corpus, split only {checked}"
    assert offenders == []


# --------------------------------------------------- quote_aware_sentences

def test_a_stop_inside_a_quotation_does_not_end_the_sentence():
    text = 'Clement wrote: "Behold the might of the new song! It has made men out of stones."'
    assert prose.quote_aware_sentences(text) == [text]


def test_single_and_double_quotes_both_hold_a_sentence_together():
    single = "He said: 'Go out. Sit in your cell.'"
    assert prose.quote_aware_sentences(single) == [single]


def test_an_apostrophe_inside_a_word_opens_nothing():
    """Otherwise "God's" would leave the splitter permanently mid-quotation
    and merge the rest of the turn into one sentence."""
    text = "God's word is first. The rest follows."
    assert prose.quote_aware_sentences(text) == [
        "God's word is first.", "The rest follows.",
    ]


def test_a_lone_closing_mark_cannot_force_a_merge():
    """A plural possessive ("the teachers' rule") reads as a closer with no
    opener. Merging only triggers while openers outnumber closers, so a
    negative balance is inert."""
    text = "The teachers' rule was plain. It held for years."
    assert prose.quote_aware_sentences(text) == [
        "The teachers' rule was plain.", "It held for years.",
    ]


# ----------------------------------------------------- overlap_coefficient

def test_overlap_is_over_the_smaller_side():
    """Denominator is min(query, record), so a two-word query fully
    contained in a long record scores 1.0 - a short ask is not penalized
    for being short."""
    record = {"text": "the desert fathers withdrew from the city to pray alone"}
    assert prose.overlap_coefficient({"desert", "fathers"}, record) == 1.0


def test_an_empty_side_scores_zero_rather_than_dividing_by_zero():
    assert prose.overlap_coefficient(set(), {"text": "anything"}) == 0.0
    assert prose.overlap_coefficient({"desert"}, {"id": "x.y.z"}) == 0.0


# ------------------------------------------------------------ claim_markers

def test_scaffolding_makes_no_claim_and_is_skipped_outright():
    """An empty marker list is how the net knows a sentence is interpretive
    framing rather than a checkable assertion. These never need a citation."""
    for sentence in ["We cannot.",
                     "We will not invent what we do not have.",
                     "It is not our place to say."]:
        assert prose.claim_markers(sentence) == []


def test_a_name_mid_sentence_is_a_checkable_claim():
    assert prose.claim_markers("He was taught by Clement in Alexandria.") == [
        "proper-noun:['alexandria', 'clement']",
    ]


def test_a_name_that_opens_the_sentence_is_not_detected():
    """Capitalization at a clause start carries no information, so the
    first word is always skipped - "Clement" here is invisible to the
    proper-noun rule and the sentence rests on its other names."""
    assert prose.claim_markers("Clement taught here.") == []


def test_doctrinal_vocabulary_is_not_a_name():
    """"God", "Christ", "Scripture" are capitalized by convention, not
    because they name a checkable entity - flagging them would flag nearly
    every sentence a formation voice speaks. Plurals count too: the net
    once struck a sentence for saying "Scriptures"."""
    assert prose.claim_markers("We read the Scriptures and trust the Spirit.") == []


def test_the_word_I_and_its_contractions_are_not_names():
    assert prose.claim_markers("To be honest: I'd rather not say.") == []


def test_a_digit_is_always_a_figure():
    assert "number" in prose.claim_markers("Some 300 monks settled there.")


def test_a_spelled_number_about_the_world_is_a_figure():
    assert "number" in prose.claim_markers("He would read a passage three ways.")


def test_the_voice_counting_its_own_readings_is_not_a_figure():
    """Narrowed after 17 measured live turns: striking this shape
    decapitated the answer, handing the participant a list starting at
    item two. Gated on the sentence being about the ask, so a doctrine
    counted three ways still counts."""
    assert prose.claim_markers("Your question can be taken two ways.") == []


def test_parallel_prose_is_not_an_enumeration():
    """Register statements 2 and 3 ask for short parallel clauses. The
    earlier short-segment rule fired on 9 of 17 live turns, every one of
    them ordinary prose, and was deleting the register it sits beside."""
    assert prose.claim_markers("We lived among them, learned from them, argued with them.") == []


def test_a_repeated_phrase_is_an_enumeration():
    assert "enumeration" in prose.claim_markers(
        "They kept the same hours, the same fasts, the same silence."
    )


# ---------------------------------------------------------- grounding_ratio

def test_a_sentence_of_pure_stopwords_is_fully_grounded():
    """No content words means nothing to ground, and the ratio returns 1.0
    rather than 0.0 - otherwise every "It is so." would be withheld. The
    claim_markers gate normally catches these first; this is the backstop."""
    assert prose.grounding_ratio("It is so.", set()) == 1.0


def test_a_content_word_with_no_citation_behind_it_scores_zero():
    assert prose.grounding_ratio("Antony withdrew.", set()) == 0.0


def test_the_ratio_is_over_the_sentence_own_length():
    """Denominator is the sentence's own content words - unlike
    overlap_coefficient, which uses the smaller of two sets. Two metrics,
    one file, deliberately named apart."""
    sentence = "Antony went to the desert to pray."
    # four content words - "went" is not a stopword - and two are cited
    assert prose.content_words(sentence) == {"antony", "went", "desert", "pray"}
    assert prose.grounding_ratio(sentence, {"antony", "desert"}) == pytest.approx(0.5)


# ------------------------------------------------------------- the floors

def test_the_two_floors_are_separately_settable():
    """They were one constant, GROUNDING_FLOOR, until the split. Same value
    today; the point is that moving one no longer moves the other."""
    assert prose.DEMONSTRATION_TAG_FLOOR == 0.4
    assert prose.WITHHOLD_FLOOR == 0.4


def test_the_two_floors_gate_different_measurements():
    """Why one number could not honestly serve both. The compile-time side
    divides by the SMALLER of sentence and record; the run-time side
    divides by the SENTENCE'S OWN length. Here is a case that clears one
    floor and fails the other on identical inputs: a long sentence whose
    every shared word comes from a short record scores 1.00 at compile time
    and 0.33 at run time. Same 0.4, opposite verdicts."""
    sentence = "Antony withdrew alone into the inner desert to pray and fast for many years."
    record = {"text": "Antony withdrew alone"}

    compile_side = prose.overlap_coefficient(prose.content_words(sentence), record)
    run_side = prose.grounding_ratio(sentence, prose.content_words(prose.all_text(record)))

    assert compile_side == 1.0
    assert run_side == pytest.approx(1 / 3)
    assert compile_side >= prose.DEMONSTRATION_TAG_FLOOR
    assert run_side < prose.WITHHOLD_FLOOR


def test_the_runtime_net_uses_the_shared_ratio_not_its_own_copy():
    """grounding_net.py carried a second, identical implementation of
    grounding_ratio inline. One formula, owned once - otherwise the tests
    above pin a function the live path does not call."""
    import inspect

    from engine.m4 import grounding_net

    source = inspect.getsource(grounding_net.check_turn)
    assert "grounding_ratio(text, cited_words)" in source
    assert "/ len(words)" not in source
