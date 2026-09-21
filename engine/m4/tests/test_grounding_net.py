"""Hermetic tests for grounding_net.py (Live-Generation Design §6, forks
signed off - LIVE-GENERATION-DESIGN.md §9.5). Synthetic records, same
shape/discipline as test_grounding.py's fixtures - not tied to any real
package path, so these run without a compiled package on disk. Real-data
verification (against the current alx/pahc/ijc packages) is a separate,
manual step recorded in the session's own commit history, not repeated
here as a hermetic test.
"""
from engine.m4.grounding_net import build_figure_lexicon, check_turn, parse_tagged, scope_completion, strip_tags, verdict_for_sentence
from engine.m4.grounding_net import _drop_truncated_tail

TERM_RECORD = {
    "id": "fix.term.eucharistia",
    "record_type": "term",
    "plain_meaning": "The thanksgiving meal of bread and cup at the heart of the community's worship.",
}
WITNESS_RECORD = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "text": "We did not claim to have seen him ourselves. We claimed only that the ones who told us could not be talked out of what they had seen.",
}
QUOTE_RECORD = {
    "id": "fix.quote.new-song",
    "record_type": "quote",
    "text": "Behold the might of the new song! It has made men out of stones, men out of beasts.",
}
FIGURE_RECORD = {
    "id": "fix.figure.clement",
    "record_type": "figure",
    "names": [{"name": "Clement", "tag": "in-world"}, {"name": "Titus Flavius Clemens", "tag": "scholarly"}],
}
REPOSITORY = {r["id"]: r for r in (TERM_RECORD, WITNESS_RECORD, QUOTE_RECORD, FIGURE_RECORD)}


def test_grounded_sentence_with_correct_tag_is_ok():
    text = "What reached everyone was the thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]]."
    result = check_turn(text, REPOSITORY)
    assert result["sentences"][0]["verdict"] == "ok"
    assert result["substantive_survives"] is True


def test_specific_claim_with_no_tag_is_withheld():
    text = "The community held three separate meals every week without exception."
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert "no citation tag" in entry["why"]


def test_specific_claim_wrongly_tagged_is_withheld_on_ratio():
    # Fabricated claim - real content words don't overlap the tagged record.
    text = "The community held three separate meals under armed guard every week [[fix.term.eucharistia]]."
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert "grounded in its own tags" in entry["why"]


def test_invented_record_id_is_withheld_at_tag_resolution():
    text = "This is a specific claim about something [[fix.term.nonexistent]]."
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert "unresolvable record id" in entry["why"]


def test_verbatim_quote_correctly_tagged_passes():
    text = "As it was sung, 'Behold the might of the new song! It has made men out of stones, men out of beasts.' [[fix.quote.new-song]]"
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "ok"
    assert "verbatim" in entry["why"]


def test_coined_quote_under_real_tag_is_withheld():
    text = "As it was sung, 'Behold the wonder of the ancient hymn, made new for us.' [[fix.quote.new-song]]"
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert "not found verbatim" in entry["why"]


def test_quote_with_no_tag_is_withheld_even_if_verbatim():
    text = "As it was sung, 'Behold the might of the new song! It has made men out of stones, men out of beasts.'"
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert "no citation tag" in entry["why"]


def test_sentence_initial_figure_name_is_caught_via_lexicon():
    # "Clement" at sentence-start defeats the capitalization heuristic;
    # the figure lexicon is what makes this a checkable claim at all.
    text = "Clement wrote a whole book defending marriage against those who despised it."
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert "figure-name" in entry["why"]


def test_interpretive_framing_with_no_claim_is_ok_untagged():
    text = "We must be honest about what our own record does and does not say."
    result = check_turn(text, REPOSITORY)
    assert result["sentences"][0]["verdict"] == "ok"


def test_quote_split_across_sentence_boundary_is_remerged():
    # The naive splitter would break inside the quotation; quote-aware
    # merging must keep the tag attached to the whole claim.
    text = "As it was sung: 'Behold the might of the new song! It has made men out of stones, men out of beasts.' [[fix.quote.new-song]]"
    parsed = parse_tagged(text)
    assert len(parsed) == 1
    assert parsed[0]["tags"] == ["fix.quote.new-song"]


def test_strip_tags_removes_all_tags_for_participant_display():
    text = "Grounded text here [[fix.term.eucharistia]] and more [[fix.quote.new-song]]."
    assert "[[" not in strip_tags(text)
    assert "Grounded text here" in strip_tags(text)


def test_figure_lexicon_uses_in_world_names_only():
    lexicon = build_figure_lexicon(REPOSITORY)
    assert "clement" in lexicon
    # Scholarly-form words (from the non-in-world name variant) must not
    # leak in as false figure signals.
    assert "flavus" not in lexicon and "titus" not in lexicon


def test_scope_completion_walks_tension_with_both_directions():
    gravity_a = {"id": "fix.gravity.a", "record_type": "gravity", "relations": [{"type": "tension-with", "target": "fix.gravity.b"}]}
    gravity_b = {"id": "fix.gravity.b", "record_type": "gravity", "relations": [{"type": "tension-with", "target": "fix.gravity.a"}]}
    unrelated = {"id": "fix.gravity.c", "record_type": "gravity", "relations": []}
    records = {r["id"]: r for r in (gravity_a, gravity_b, unrelated)}

    assert scope_completion(["fix.gravity.a"], records) == ["fix.gravity.b"]
    # Seeding the far side finds its way back too (both-directions walk).
    assert scope_completion(["fix.gravity.b"], records) == ["fix.gravity.a"]
    assert scope_completion(["fix.gravity.c"], records) == []


def test_scope_completion_never_returns_the_seed_itself():
    gravity_a = {"id": "fix.gravity.a", "record_type": "gravity", "relations": [{"type": "tension-with", "target": "fix.gravity.a"}]}
    records = {gravity_a["id"]: gravity_a}
    assert scope_completion(["fix.gravity.a"], records) == []


# ---- the three narrowings (2026-08-23) -------------------------------------
# Each of these fired on real live output and deleted prose that invented
# nothing. Counts are from 17 measured turns / 68 withheld sentences.

def test_parallel_prose_is_not_an_enumeration():
    # 9 of 68 withholds. Short parallel clauses are what register statements
    # 2 and 3 ask the voice to write; the old short-segment count deleted them.
    from engine.prose import claim_markers as _claim_markers
    assert _claim_markers("We lived among them, learned from them, argued with them.") == []
    assert _claim_markers("That, too, I can show you.") == []
    # the repeated-phrase signal the rule was actually built for survives
    assert "enumeration" in _claim_markers("The same water, the same bread.")


def test_common_words_are_not_treated_as_names():
    # 10 of 68. "scripture" was already exempt and "Scriptures" was not.
    from engine.prose import claim_markers as _claim_markers
    assert _claim_markers("We held that the Scriptures are alive, not a closed book.") == []
    assert _claim_markers("To become a Christian among us was to be changed.") == []
    # a real name still marks the sentence as checkable
    assert any("proper-noun" in m for m in _claim_markers("Later, Athanasius put it in one sentence."))


def test_counting_the_readings_of_a_question_is_not_a_figure():
    # 7 of 68, and always the OPENING sentence - so the participant was
    # handed a list starting at item two.
    from engine.prose import claim_markers as _claim_markers
    assert _claim_markers("I hear two ways to take your question, and I want to answer the one you meant.") == []
    assert _claim_markers("Your question can be heard three ways, and I must ask which you mean.") == []


def test_a_counted_doctrine_is_still_a_figure():
    # The first draft of the rule above freed this. It is a claim about the
    # world, not about the ask, and must stay checkable.
    from engine.prose import claim_markers as _claim_markers
    assert "number" in _claim_markers("He would read a passage three ways, for body, soul, and spirit.")
    assert "number" in _claim_markers("For the first three centuries of our window, persecution came in waves.")
    assert "number" in _claim_markers("The boy was seventeen when his father was killed.")


def test_a_tagged_sentence_is_checked_even_with_no_claim_marker():
    """The tag IS the claim. claim_markers only sees a proper noun, a number
    or a repeated phrase; over 36 live turns that left 242 of 388 sentences
    unexamined, 192 of them carrying a tag the net never verified."""
    records = {"fix.term.agape": {"id": "fix.term.agape", "record_type": "term",
                                  "plain_meaning": "the common meal the household ate together"}}
    result = check_turn("We ate the common meal together [[fix.term.agape]].", records)
    sentence = result["sentences"][0]
    assert sentence["verdict"] == "ok"
    assert sentence["why"] == "tagged claim, shares ground with its own records"


def test_a_tag_sharing_no_word_with_its_record_is_withheld():
    """Zero overlap is the one line here that is not a chosen number: a
    citation to a record with which the sentence shares not one content word
    asserts nothing. Seen live seven times, every one framing - "That is what
    mattered most." tagged to hal.gravity.hebraica-veritas."""
    records = {"fix.gravity.reading": {"id": "fix.gravity.reading", "record_type": "gravity",
                                       "description": "how the household read scripture aloud together"}}
    result = check_turn("That is what mattered most [[fix.gravity.reading]].", records)
    sentence = result["sentences"][0]
    assert sentence["verdict"] == "withhold"
    assert "no content word" in sentence["why"]


def test_the_tag_gate_does_not_use_the_withhold_floor():
    """WITHHOLD_FLOOR was calibrated on name-and-number sentences, which sit
    lexically close to their source. A long tagged sentence drawing one fact
    from a record scores far below it and is still a real citation - applying
    the floor here would strip roughly 29 legitimate ones to catch 10
    over-tags."""
    records = {"fix.term.agape": {"id": "fix.term.agape", "record_type": "term",
                                  "plain_meaning": "the common meal"}}
    long_one = ("We gathered in the evening after work was done and shared what little "
                "each household could bring to the common table [[fix.term.agape]].")
    sentence = check_turn(long_one, records)["sentences"][0]
    assert sentence["verdict"] == "ok"          # one shared word is enough
    assert "ratio" not in sentence              # and no ratio was computed


def test_an_untagged_sentence_with_no_marker_is_still_never_checked():
    """Unchanged, and deliberately: with no marker and no tag there is
    nothing asserted to check against."""
    sentence = check_turn("But it was never the whole of us.", {})["sentences"][0]
    assert sentence["verdict"] == "ok"
    assert sentence["why"] == "no checkable claim - interpretive/connective framing"


# ---- truncation (2026-09-19) -----------------------------------------------
# A generation call cut off by Bedrock's own stop mid-tag leaves an opener
# with no closing "]]" anywhere after it - a shape _TAG's own well-formed
# grammar can never match, so it used to reach strip_tags' output verbatim.
# Real case, don's round-1 turn-1 of the 2026-09-19 rzg+don Table round:
# "...never to preach it again [[don.dw.room-for-diss" with nothing after.

_TRUNCATED_REAL_CASE = (
    "In the second room, a layman of ours named Tyconius worked out from "
    "Scripture that the church is spread across the whole earth - which, if "
    "true, meant we were the ones who had cut ourselves off from something "
    "real. He was told by our own bishop at Carthage never to preach it "
    "again [[don.dw.room-for-diss"
)


def test_drop_truncated_tail_backs_off_to_last_finished_sentence():
    text, truncated = _drop_truncated_tail(_TRUNCATED_REAL_CASE)
    assert truncated is True
    assert text == (
        "In the second room, a layman of ours named Tyconius worked out from "
        "Scripture that the church is spread across the whole earth - which, if "
        "true, meant we were the ones who had cut ourselves off from something "
        "real."
    )
    # the unfinished clause and the dangling tag are both gone
    assert "[[" not in text
    assert "He was told" not in text


def test_drop_truncated_tail_leaves_ordinary_text_unchanged():
    text = "A complete turn with a real tag [[fix.term.eucharistia]]."
    assert _drop_truncated_tail(text) == (text, False)


def test_drop_truncated_tail_on_an_all_fragment_turn_returns_empty():
    # No prior sentence ever finished, so nothing is confirmed complete.
    text, truncated = _drop_truncated_tail("Something cut off mid [[fix.term.eu")
    assert truncated is True
    assert text == ""


def test_strip_tags_removes_a_dangling_unclosed_tag_and_its_fragment():
    result = strip_tags(_TRUNCATED_REAL_CASE)
    assert "[[" not in result
    assert "He was told" not in result
    assert result.endswith("something real.")


def test_check_turn_reports_truncation_and_never_sees_the_dropped_fragment():
    result = check_turn(_TRUNCATED_REAL_CASE, {})
    assert result["truncated"] is True
    joined = " ".join(s["sentence"] for s in result["sentences"])
    assert "He was told" not in joined
    assert "[[" not in joined


def test_check_turn_reports_no_truncation_on_an_ordinary_turn():
    result = check_turn("But it was never the whole of us.", {})
    assert result["truncated"] is False


# M-1 (witt go-live adversarial review, 2026-09-20): the scaffold exemption
# used to cover a whole sentence the moment any SCAFFOLD_MARKERS phrase
# appeared anywhere in it - real cases from that live run.

def test_a_chronological_claim_riding_a_scaffold_phrase_is_no_longer_exempt():
    """The exact defect: 'we cannot speak its own words' at the sentence's
    own tail used to wave through an embedded, ungrounded year/place claim
    earlier in the same sentence."""
    text = (
        "What we can say is only this: in 1525, in the same years when we were "
        "forming households around the catechism and defending our teaching at "
        "Augsburg, our founder wrote against the peasants' rising, and that "
        "writing is part of our own history even when we cannot speak its own words."
    )
    result = check_turn(text, {})
    entry = result["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert "no citation tag" in entry["why"]


def test_a_pure_scaffold_sentence_with_no_other_claim_still_exempts():
    text = "We must be careful here, and honest about the shape of what we actually hold."
    result = check_turn(text, {})
    assert result["sentences"][0]["why"] == "exempt: honesty scaffolding / sanctioned self-naming"


def test_a_scaffold_sentence_whose_marker_clause_is_first_still_exempts():
    text = (
        "We do not have the records that would tell us whether he was right "
        "about how bad it really was, only that he believed it and said so."
    )
    result = check_turn(text, {})
    assert result["sentences"][0]["why"] == "exempt: honesty scaffolding / sanctioned self-naming"


def test_the_sanctioned_self_naming_line_still_exempts():
    text = "I am a representative of Lutheran Wittenberg and its congregations."
    result = check_turn(text, {})
    assert result["sentences"][0]["why"] == "exempt: honesty scaffolding / sanctioned self-naming"


def test_a_grounded_claim_beside_a_scaffold_phrase_still_passes_on_its_own_tag():
    """Narrowing the exemption must not start withholding sentences that
    were always properly grounded - a real tagged claim in its own clause,
    beside a scaffold phrase, should clear the normal pipeline rather than
    get caught by the fallout."""
    text = (
        "We must be honest: the thanksgiving meal of bread and cup at the "
        "heart of the community's worship is what reached everyone [[fix.term.eucharistia]]."
    )
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "ok"
    assert entry["why"] != "exempt: honesty scaffolding / sanctioned self-naming"


def test_a_scaffold_phrase_grammatically_fused_with_a_tagged_claim_still_gets_checked():
    """The clause splitter works on punctuation (M-1's own actual defect
    shape - a dangling clause joined by a comma), not on subordinating
    conjunctions, so 'We must be honest THAT x' fuses the marker and the
    claim into one un-split clause and the punctuation-based residual
    alone would miss it. Caught anyway here because the sentence carries a
    citation tag - a tag is itself a claim ("this sentence came from that
    record"), checked on that basis regardless of what clause it sits in."""
    text = (
        "We must be honest that the thanksgiving meal of bread and cup at the "
        "heart of the community's worship is what reached everyone [[fix.term.eucharistia]]."
    )
    result = check_turn(text, REPOSITORY)
    entry = result["sentences"][0]
    assert entry["verdict"] == "ok"
    assert entry["why"] == "tagged claim, shares ground with its own records"


def test_verdict_for_sentence_matches_check_turn_called_on_the_same_sentence():
    """Build-Plan.md Stage 1 (D1 grounding measurement) needs to run the
    exact per-sentence verdict logic directly against a constructed
    (sentence, tags) pair, without round-tripping through tagged-text
    reconstruction and re-parsing - this is the seam that makes that
    possible. Proven here by equivalence, not just by check_turn's own
    tests still passing unchanged: the same sentence run both ways must
    land on the identical verdict."""
    text = "What reached everyone was the thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]]."
    via_check_turn = check_turn(text, REPOSITORY)["sentences"][0]

    figure_names = build_figure_lexicon(REPOSITORY)
    parsed = parse_tagged(text)[0]
    direct = verdict_for_sentence(
        parsed["text"], parsed["tags"],
        repository_records=REPOSITORY, figure_names=figure_names,
        thin_topics=None, grounding_floor=0.4,
    )

    assert direct == via_check_turn


def test_verdict_for_sentence_withholds_an_unresolvable_tag_with_no_turn_context_needed():
    """The whole point of the extraction: callable for a single synthetic
    sentence with no surrounding turn at all."""
    entry = verdict_for_sentence(
        "This claims a record that does not exist.", ["fix.term.nonexistent"],
        repository_records=REPOSITORY, figure_names=set(),
        thin_topics=None, grounding_floor=0.4,
    )
    assert entry["verdict"] == "withhold"
    assert "unresolvable" in entry["why"]
