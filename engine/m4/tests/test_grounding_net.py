"""Hermetic tests for grounding_net.py (Live-Generation Design §6, forks
signed off - LIVE-GENERATION-DESIGN.md §9.5). Synthetic records, same
shape/discipline as test_grounding.py's fixtures - not tied to any real
package path, so these run without a compiled package on disk. Real-data
verification (against the current alx/pahc/ijc packages) is a separate,
manual step recorded in the session's own commit history, not repeated
here as a hermetic test.
"""
from engine.m4.grounding_net import build_figure_lexicon, check_turn, check_turn_with_paragraph_coverage, drop_flagged_sentences, parse_tagged, scope_completion, split_into_paragraphs, strip_tags, verdict_for_sentence
from engine.m4.grounding_net import _drop_truncated_tail, _groundable_text

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
    "modern_rendering": "Behold the might of the new song! It has made men out of stones, men out of beasts.",
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


NEW_SONG_FULL = "Behold the might of the new song! It has made men out of stones, men out of beasts."


def _placed(lead, record):
    sentence = f"{lead} “{record['modern_rendering']}” [[{record['id']}]]"
    return sentence, {strip_tags(sentence).strip(): record["id"]}


def test_a_quote_placed_by_code_passes_verbatim_to_its_record():
    text, placed = _placed("As it was sung:", QUOTE_RECORD)
    entry = check_turn(text, REPOSITORY, placed=placed)["sentences"][0]
    assert entry["verdict"] == "ok"
    assert entry["placed_quote"] == "fix.quote.new-song"
    assert "verbatim" in entry["why"]


def test_the_same_words_typed_by_the_voice_are_withheld_even_when_verbatim():
    for text in (
        f"As it was sung, '{NEW_SONG_FULL}' [[fix.quote.new-song]]",
        f"As it was sung, “{NEW_SONG_FULL}” [[fix.quote.new-song]]",
        f"As it was sung, '{NEW_SONG_FULL}'",
    ):
        entry = check_turn(text, REPOSITORY)["sentences"][0]
        assert entry["verdict"] == "withhold", text
        assert entry["why"] == "quotation typed by the voice", text


def test_a_coined_quote_under_a_real_tag_is_withheld():
    for text in (
        "As it was sung, 'Behold the wonder of the ancient hymn, made new for us.' [[fix.quote.new-song]]",
        "As it was sung, “Behold the wonder of the ancient hymn, made new for us.” [[fix.quote.new-song]]",
    ):
        entry = check_turn(text, REPOSITORY)["sentences"][0]
        assert entry["verdict"] == "withhold"
        assert entry["why"] == "quotation typed by the voice"


def test_a_placed_sentence_whose_quotation_is_not_its_records_rendering_is_withheld():
    altered = {**QUOTE_RECORD, "modern_rendering": NEW_SONG_FULL.replace("might", "mighty")}
    text, placed = _placed("As it was sung:", altered)
    entry = check_turn(text, REPOSITORY, placed=placed)["sentences"][0]
    assert entry["verdict"] == "withhold"
    assert entry["why"] == "placed quote does not match its record"


def test_archaic_letterforms_match_both_ways_in_a_short_quoted_term():
    archaic_record = {
        "id": "fix.term.archaic-thorn", "record_type": "term",
        "plain_meaning": "Behold þe might of þe new song.",
    }
    repo = {**REPOSITORY, archaic_record["id"]: archaic_record}
    for text in (
        "They sang of “þe new song” [[fix.quote.new-song]].",
        "They sang of “the new song” [[fix.term.archaic-thorn]].",
    ):
        entry = check_turn(text, repo)["sentences"][0]
        assert entry["why"] != "quotation not in records", text
        assert "source_sentence" not in entry, text


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


# ---- the three narrowings ---------------------------------------------------
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


# ---- truncation ---------------------------------------------------------
# A generation call cut off by Bedrock's own stop mid-tag leaves an opener
# with no closing "]]" anywhere after it - a shape _TAG's own well-formed
# grammar can never match, so it used to reach strip_tags' output verbatim.
# Real case, don's round-1 turn-1 of an rzg+don Table round:
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


# The scaffold exemption applies to the marker's own clause, not to the
# whole sentence a SCAFFOLD_MARKERS phrase happens to appear in.

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
    """A properly grounded sentence must not be withheld just because it
    also contains a scaffold phrase - a real tagged claim in its own
    clause, beside a scaffold phrase, should clear the normal pipeline
    on its own tag, independent of the exemption's own narrower scope."""
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


# split_into_paragraphs
# and check_turn_with_paragraph_coverage's own baseline hermetic tests -
# additive, report-only, never touched by check_turn/apply_net's own live
# path (this file's own module docstring: real-data verification is
# separate; these stay synthetic and hermetic like every other test here).
def test_split_into_paragraphs_splits_on_blank_lines():
    assert split_into_paragraphs("para one.\n\npara two.") == ["para one.", "para two."]


def test_split_into_paragraphs_ignores_single_newlines():
    # A single line break inside a paragraph is not a paragraph boundary -
    # only a blank line (two or more \n) is.
    assert split_into_paragraphs("one line\nstill one paragraph.") == ["one line\nstill one paragraph."]


def test_split_into_paragraphs_falls_back_to_the_whole_text_when_no_blank_line():
    assert split_into_paragraphs("just one paragraph, no blank line at all.") == ["just one paragraph, no blank line at all."]


def test_drop_flagged_sentences_removes_only_the_named_sentence_and_its_own_tag():
    text = "First sentence stays [[a.b.c]]. Second sentence is bad. Third sentence stays too [[d.e.f]]."
    assert (
        drop_flagged_sentences(text, {"Second sentence is bad."})
        == "First sentence stays [[a.b.c]]. Third sentence stays too [[d.e.f]]."
    )


def test_drop_flagged_sentences_drops_a_paragraph_whole_when_every_sentence_in_it_is_flagged():
    text = "Keep this one [[a.b.c]].\n\nBad sentence one. Bad sentence two."
    assert drop_flagged_sentences(text, {"Bad sentence one.", "Bad sentence two."}) == "Keep this one [[a.b.c]]."


def test_drop_flagged_sentences_returns_empty_string_when_everything_is_flagged():
    text = "Only sentence, and it is bad."
    assert drop_flagged_sentences(text, {"Only sentence, and it is bad."}) == ""


def test_drop_flagged_sentences_is_a_no_op_when_nothing_matches():
    text = "Nothing here is flagged [[a.b.c]]."
    assert drop_flagged_sentences(text, {"Some other sentence entirely."}) == text


def test_check_turn_with_paragraph_coverage_matches_check_turn_on_sentences_and_truncation():
    # Same equivalence discipline as
    # test_verdict_for_sentence_matches_check_turn_called_on_the_same_sentence
    # above: a caller reading only "sentences"/"substantive_survives"/
    # "truncated" cannot tell this function's result apart from check_turn's
    # own - the module's own docstring promise, proven here rather than
    # just asserted.
    text = "What reached everyone was the thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]]."
    via_check_turn = check_turn(text, REPOSITORY)
    via_paragraph_coverage = check_turn_with_paragraph_coverage(text, REPOSITORY)
    assert via_paragraph_coverage["sentences"] == via_check_turn["sentences"]
    assert via_paragraph_coverage["substantive_survives"] == via_check_turn["substantive_survives"]
    assert via_paragraph_coverage["truncated"] == via_check_turn["truncated"]


def test_check_turn_with_paragraph_coverage_reports_per_paragraph_cited_record_ids():
    text = (
        "What reached everyone was the thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]].\n\n"
        "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."
    )
    result = check_turn_with_paragraph_coverage(text, REPOSITORY)
    coverage = result["paragraph_coverage"]
    assert len(coverage) == 2
    assert coverage[0]["cited_record_ids"] == ["fix.term.eucharistia"]
    assert coverage[0]["wholly_uncited"] is False
    assert coverage[1]["cited_record_ids"] == ["fix.witness.who-is-jesus"]


def test_check_turn_with_paragraph_coverage_a_wholly_uncited_paragraph_is_marked():
    text = "It mattered to everyone who came."
    result = check_turn_with_paragraph_coverage(text, REPOSITORY)
    coverage = result["paragraph_coverage"][0]
    assert coverage["cited_record_ids"] == []
    assert coverage["wholly_uncited"] is True
    assert coverage["inherited_from_preceding"] is False


def test_check_turn_with_paragraph_coverage_a_one_sentence_paragraph_inherits_the_preceding_paragraphs_citations():
    text = (
        "What reached everyone was the thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]].\n\n"
        "It mattered to everyone who came."
    )
    result = check_turn_with_paragraph_coverage(text, REPOSITORY)
    first, second = result["paragraph_coverage"]
    assert first["inherited_from_preceding"] is False
    assert second["inherited_from_preceding"] is True
    assert second["cited_record_ids"] == ["fix.term.eucharistia"]
    # The inherited check actually ran (verdict_for_sentence against the
    # inherited id set, not a rubber stamp) - this sentence shares no
    # content word with fix.term.eucharistia's own text, so the inherited
    # check itself withholds it, exactly the shape find_uncited_paragraphs
    # reports as inherited_ungrounded.
    inherited = second["inherited_verdicts"][0]
    assert inherited["verdict"] == "withhold"


def test_check_turn_with_paragraph_coverage_a_one_sentence_paragraph_never_inherits_from_a_wholly_uncited_predecessor():
    text = "It mattered to everyone who came.\n\nIt mattered again the next day."
    result = check_turn_with_paragraph_coverage(text, REPOSITORY)
    first, second = result["paragraph_coverage"]
    assert first["wholly_uncited"] is True
    assert second["inherited_from_preceding"] is False
    assert second["wholly_uncited"] is True


# ---- _groundable_text: a quote's own grounding pool is modern_rendering
# only, never text (item 3, the modern_rendering-required gate) ------------


def test_groundable_text_for_a_quote_is_modern_rendering_only():
    rec = {"id": "fix.quote.one", "record_type": "quote",
           "text": "An archaic original, never voiced.",
           "modern_rendering": "A modern spoken form."}
    assert _groundable_text(rec) == "A modern spoken form."
    assert "archaic" not in _groundable_text(rec)


def test_groundable_text_for_a_non_quote_record_is_unchanged_all_text():
    rec = {"id": "fix.term.one", "record_type": "term", "plain_meaning": "A term's own plain meaning."}
    assert _groundable_text(rec) == "A term's own plain meaning."


def test_a_generated_span_matching_only_the_archaic_text_does_not_ground():
    """The bug this pins: a generated quotation verbatim-matching a
    record's own archaic `text` but not its modern_rendering was never
    legitimately produced from that record - the voice only ever speaks
    modern_rendering (gate_quote_recording), so a span that only matches
    text should not pass as grounded."""
    quote = {"id": "fix.quote.archaic-only", "record_type": "quote",
             "text": "the elders spoke of paradise restored",
             "modern_rendering": "the elders talked about paradise being brought back"}
    text = 'He said, "the elders spoke of paradise restored." [[fix.quote.archaic-only]]'
    result = check_turn(text, {"fix.quote.archaic-only": quote})
    assert result["sentences"][0]["verdict"] == "withhold"


def test_a_placed_rendering_grounds_and_the_archaic_text_is_never_what_is_placed():
    quote = {"id": "fix.quote.rendering-match", "record_type": "quote",
             "text": "the elders spoke of paradise restored",
             "modern_rendering": "the elders talked about paradise being brought back"}
    text, placed = _placed("He said:", quote)
    entry = check_turn(text, {"fix.quote.rendering-match": quote}, placed=placed)["sentences"][0]
    assert entry["verdict"] == "ok"
    archaic = 'He said: “the elders spoke of paradise restored” [[fix.quote.rendering-match]]'
    entry = check_turn(archaic, {"fix.quote.rendering-match": quote}, placed={strip_tags(archaic).strip(): quote["id"]})["sentences"][0]
    assert entry["why"] == "placed quote does not match its record"


# --- quotation marks and attribution -------------------------------------------

from engine.m4.grounding_net import QUOTATION_DROP_REASONS, QuotationIndex, quoted_span_positions, shown_text

SPEAKER_QUOTE = {
    "id": "fix.quote.clement-song", "record_type": "quote", "speaker_or_author": "fix.figure.clement",
    "text": "Behold the might of the new song! It has made men out of stones, men out of beasts.",
    "modern_rendering": "Behold the might of the new song! It has made men out of stones, men out of beasts.",
}
OTHER_QUOTE = {
    "id": "fix.quote.origen-door", "record_type": "quote", "speaker_or_author": "Origen, as Eusebius reports him",
    "text": "The door was open to everyone who asked.", "modern_rendering": "The door was open to everyone who asked.",
}
DEMO_RECORD = {
    "id": "fix.demo.one", "record_type": "demonstration",
    "exchange": [{"speaker": "representative", "text": "We kept a secret sign that only the teachers ever knew about."}],
}
QUOTE_REPOSITORY = {r["id"]: r for r in (WITNESS_RECORD, FIGURE_RECORD, SPEAKER_QUOTE, OTHER_QUOTE, DEMO_RECORD)}
NEW_SONG = "Behold the might of the new song! It has made men out of stones"
TYPED = "quotation typed by the voice"
ATTRIBUTED = "words attributed without a placed quote"


def _entry(text, repository=QUOTE_REPOSITORY, **kwargs):
    return check_turn(text, repository, **kwargs)["sentences"][0]


def _whys(text, repository=QUOTE_REPOSITORY, **kwargs):
    return [(s["sentence"], s["verdict"], s["why"]) for s in check_turn(text, repository, **kwargs)["sentences"]]


def test_a_quotation_of_four_words_or_more_is_withheld_whatever_record_holds_it():
    for text in (
        f'Our teachers sang: "{NEW_SONG}" [[fix.quote.clement-song]].',
        'We sang "Behold the might of the new song ... men out of beasts" [[fix.quote.clement-song]].',
        "They said 'the sign was never shown to anyone' [[fix.witness.who-is-jesus]].",
        'We kept "a secret sign that only the teachers ever knew about" [[fix.witness.who-is-jesus]].',
        'We must be careful here, and honest about what we hold: "the door was never opened at all".',
    ):
        entry = _entry(text)
        assert entry["verdict"] == "withhold", text
        assert entry["why"] == TYPED, text


# The quotation-mark checks below run on sentences referring back to a quote
# already voiced, so that a tag to an unplaced quote record (refused whole)
# does not decide them.
SONG_VOICED = frozenset({"fix.quote.clement-song"})


def test_a_short_quoted_span_found_in_no_record_loses_its_marks_and_is_withheld():
    entry = _entry('We sang of "the mighty song" [[fix.quote.clement-song]].', voiced=SONG_VOICED)
    assert entry["why"] == "quotation not in records"
    assert entry["sentence"] == "We sang of the mighty song."
    assert entry["source_sentence"].count('"') == 2
    assert entry["quotations_not_in_records"] == ["the mighty song"]
    curly = _entry("We sang of “the mighty song” [[fix.quote.clement-song]].", voiced=SONG_VOICED)
    assert "“" not in curly["sentence"] and "”" not in curly["sentence"]


def test_a_short_quoted_span_found_in_a_record_keeps_its_marks():
    entry = _entry('We sang of "the new song" [[fix.quote.clement-song]].', voiced=SONG_VOICED)
    assert entry["verdict"] == "ok"
    assert "source_sentence" not in entry


def test_a_short_single_quoted_term_is_not_a_claim_of_verbatim_words():
    entry = _entry("They called the meal the 'agape' and kept it weekly [[fix.witness.who-is-jesus]].")
    assert entry["why"] != "quotation not in records"


def test_possessives_and_contractions_are_never_quotations():
    for text in (
        "The community's worship didn't change, and the teachers' rule held [[fix.term.eucharistia]].",
        "We don't claim what we haven't seen, and it's the elders' word we keep [[fix.witness.who-is-jesus]].",
    ):
        assert _entry(text, {**QUOTE_REPOSITORY, "fix.term.eucharistia": TERM_RECORD})["why"] not in (
            "quotation not in records", TYPED,
        )


def test_marks_come_off_only_the_failing_short_span():
    entry = _entry('We sang of "the new song" and then "nobody wrote" [[fix.quote.clement-song]].', voiced=SONG_VOICED)
    assert entry["sentence"] == 'We sang of "the new song" and then nobody wrote.'


def test_shown_text_carries_the_marks_off_sentence_and_keeps_the_rest():
    raw = (
        "We kept the bread each week [[fix.term.eucharistia]]. "
        'Then we kept "nobody\'s line" [[fix.witness.who-is-jesus]]. '
        "That is all we hold."
    )
    repository = {**QUOTE_REPOSITORY, "fix.term.eucharistia": TERM_RECORD}
    result = check_turn(raw, repository)
    assert shown_text(raw, result["sentences"]) == "We kept the bread each week. Then we kept nobody's line. That is all we hold."


def test_a_short_quotation_attributed_to_a_figure_needs_that_figures_quote_record():
    repository = {**QUOTE_REPOSITORY, "fix.witness.songs": {
        "id": "fix.witness.songs", "record_type": "doctrinal_witness", "text": "Our people sang of the new song.",
    }}
    assert _entry('Clement called it "the new song" [[fix.witness.songs]].', repository)["why"] == (
        "words attributed without a quote record"
    )
    assert _entry('Clement put it plainly: "everyone who asked" [[fix.quote.origen-door]].')["why"] == (
        "words attributed without a quote record"
    )
    assert _entry('According to Clement, "the new song" [[fix.witness.who-is-jesus]].')["why"] == (
        "words attributed without a quote record"
    )


def test_a_speaker_without_a_figure_record_is_still_a_named_figure():
    entry = _entry('Origen said: "everyone who asked" [[fix.witness.who-is-jesus]].')
    assert entry["why"] == "words attributed without a quote record"


def test_attributed_figures_reads_the_subject_of_the_verb_only():
    index = QuotationIndex({**QUOTE_REPOSITORY, "fix.figure.origen": {
        "id": "fix.figure.origen", "record_type": "figure", "names": [{"name": "Origen", "tag": "in-world"}],
    }, "fix.figure.gregory": {
        "id": "fix.figure.gregory", "record_type": "figure", "names": [{"name": "Gregory", "tag": "in-world"}],
    }})
    assert index.attributed_figures("Clement wrote to Origen,") == [{"fix.figure.clement"}]
    assert index.attributed_figures("When Origen came, Clement said,") == [{"fix.figure.clement"}]
    assert index.attributed_figures(", Clement told Origen") == [{"fix.figure.clement"}]
    for lead in ("He wrote to Gregory:", "He told Gregory,", "The monk asked Gregory"):
        assert index.attributed_figures(lead) == [], lead
    assert index.attributed_figures(", said Gregory") == [{"fix.figure.gregory"}]
    assert index.attributed_figures("We said") == [] and index.attributed_figures("God said") == []


def test_a_figure_named_inside_the_quoted_words_is_not_the_attributed_figure():
    jerome = {"id": "fix.figure.jerome", "record_type": "figure", "names": [{"name": "Jerome", "tag": "in-world"}]}
    paula = {"id": "fix.figure.paula", "record_type": "figure", "names": [{"name": "Paula", "tag": "in-world"}]}
    quote = {
        "id": "fix.quote.paula-psalms", "record_type": "quote", "speaker_or_author": "fix.figure.jerome",
        "text": "Paula decided to learn Hebrew too.", "modern_rendering": "Paula decided to learn Hebrew too.",
    }
    repository = {r["id"]: r for r in (jerome, paula, quote)}
    text, placed = _placed("Jerome wrote:", quote)
    assert _entry(text, repository, placed=placed)["verdict"] == "ok"


def test_a_placed_quote_whose_lead_in_names_another_speaker_is_withheld():
    repository = {**QUOTE_REPOSITORY, "fix.figure.origen": {
        "id": "fix.figure.origen", "record_type": "figure", "names": [{"name": "Origen", "tag": "in-world"}],
    }}
    text, placed = _placed("Clement put it plainly:", OTHER_QUOTE)
    assert _entry(text, repository, placed=placed)["why"] == "placed quote does not match its record"
    text, placed = _placed("Origen said:", OTHER_QUOTE)
    assert _entry(text, repository, placed=placed)["verdict"] == "ok"


def test_a_group_speaker_does_not_turn_its_articles_into_figure_names():
    council = {
        "id": "fix.quote.council", "record_type": "quote", "speaker_or_author": "The Council of Bagai, in its minutes",
        "text": "We hold the one table.", "modern_rendering": "We hold the one table.",
    }
    witness = {"id": "fix.witness.table", "record_type": "doctrinal_witness", "text": "We hold the one table."}
    repository = {r["id"]: r for r in (council, witness)}
    assert _entry('The elders called it "the one table" [[fix.witness.table]].', repository)["verdict"] == "ok"
    named = _entry('The Council of Bagai called it "the one table" [[fix.witness.table]].', repository)
    assert named["why"] == "words attributed without a quote record"


def test_titles_and_divine_names_are_not_figure_names():
    figure = {"id": "fix.figure.macrina", "record_type": "figure", "names": [{"name": "Macrina, called the Teacher of the Lord", "tag": "in-world"}]}
    index = QuotationIndex({**QUOTE_REPOSITORY, figure["id"]: figure})
    for lead in ("The Lord said,", "Our teacher said,"):
        assert index.attributed_figures(lead) == [], lead


def test_only_the_head_of_a_speaker_field_names_the_speaker():
    repository = {**QUOTE_REPOSITORY, "fix.figure.origen": {"id": "fix.figure.origen", "record_type": "figure", "names": [{"name": "Origen", "tag": "in-world"}]}}
    quote = {**OTHER_QUOTE, "id": "fix.quote.letter", "speaker_or_author": "Clement, Letter to Origen"}
    repository["fix.quote.letter"] = quote
    text, placed = _placed("Origen wrote:", quote)
    assert _entry(text, repository, placed=placed)["why"] == "placed quote does not match its record"


def test_quote_pairing_holds_nested_marks_possessives_and_unpairable_openers():
    assert [s for _a, _b, s in quoted_span_positions(
        'Clement wrote, "The apostles\' teaching was a line I made up," and we kept it.'
    )] == ["The apostles' teaching was a line I made up,"]
    assert [s for _a, _b, s in quoted_span_positions(
        "Origen said, \"We say it plainly: 'I hold this to be clear' and nothing else.\""
    )] == ["We say it plainly: 'I hold this to be clear' and nothing else."]
    for text in (
        "‘Behold the might of the new song and us’ said Clement.",
        "'Behold the might of the new song and us' said Clement.",
    ):
        assert [s for _a, _b, s in quoted_span_positions(text)] == ["Behold the might of the new song and us"], text
    assert [s for _a, _b, s in quoted_span_positions('‘Grace is ours wrote Paul, and "a line nobody wrote".')] == [
        "a line nobody wrote",
    ]


def test_guillemets_and_low_opening_marks_are_quotation_marks():
    for text in (
        "We keep «the ship that crosses the wide sea» [[fix.witness.who-is-jesus]].",
        "We keep « the ship that crosses the wide sea » [[fix.witness.who-is-jesus]].",
        "We keep „the ship that crosses the wide sea“ [[fix.witness.who-is-jesus]].",
    ):
        assert _entry(text)["why"] == TYPED, text


def test_quotation_index_reports_what_it_holds():
    index = QuotationIndex(QUOTE_REPOSITORY)
    assert index.holds("the door was open to everyone who asked")
    assert not index.holds("the door was shut to everyone who asked")
    assert not index.holds("")


def test_words_the_participant_said_may_be_quoted_back():
    text = 'You asked about "the door that was never opened" [[fix.witness.who-is-jesus]].'
    assert _entry(text)["why"] == TYPED
    echoed = _entry(text, quotable_texts=["Tell me about the door that was never opened, please."])
    assert echoed["why"] not in ("quotation not in records", TYPED)
    assert "source_sentence" not in echoed


def test_echoed_words_do_not_stand_in_for_a_quote_record_of_an_attributed_figure():
    text = 'Clement wrote, "the door that was never opened" [[fix.witness.who-is-jesus]].'
    entry = _entry(text, quotable_texts=["the door that was never opened"])
    assert entry["why"] == "words attributed without a quote record"


def test_a_double_quotation_holds_the_double_quotations_nested_inside_it():
    inner = 'Then Germanus said: "The reward is chastity." He said "come, see" and left.'
    text = f"Cassian wrote: “{inner}” [[fix.quote.x]]"
    assert [span for _s, _e, span in quoted_span_positions(text)] == [inner]
    opening = '"Come," he said, "see the old men." We went.'
    assert [span for _s, _e, span in quoted_span_positions(f"“{opening}”")] == [opening]
    assert [span for _s, _e, span in quoted_span_positions('He said "no deception" and "no mixture at all" too.')] == [
        "no deception", "no mixture at all",
    ]


# --- words attributed without a placed quote ------------------------------------

EPHREM = {"id": "w.figure.ephrem", "record_type": "figure", "names": [{"name": "Ephrem", "tag": "in-world"}]}
EPHREM_QUOTE = {
    "id": "w.quote.a", "record_type": "quote", "speaker_or_author": "w.figure.ephrem",
    "text": "The Church is a ship on the wide sea.", "modern_rendering": "The Church is a ship on the wide sea.",
}
CHURCH_WITNESS = {
    "id": "w.witness.church", "record_type": "doctrinal_witness",
    "text": "We hold that the Church is one body, gathered at one table and kept by one faith.",
}
EPHREM_REPOSITORY = {r["id"]: r for r in (EPHREM, EPHREM_QUOTE, CHURCH_WITNESS)}
CLEAN = "We hold that the Church is one body [[w.witness.church]]."


def test_a_sentence_tagged_to_a_quote_record_not_yet_voiced_is_refused_whether_or_not_it_names_the_speaker():
    for text in (
        "Ephrem says the Church is like a vessel crossing the wide sea [[w.quote.a]].",
        "We speak of the Church as a ship on the wide sea [[w.quote.a]].",
    ):
        entry = _entry(text, EPHREM_REPOSITORY)
        assert (entry["verdict"], entry["why"]) == ("withhold", "tagged to a quote record that has not been placed"), text


def test_referring_back_to_a_voiced_quote_is_refused_only_when_it_names_the_speaker():
    voiced = frozenset({"w.quote.a"})
    entry = _entry("Ephrem says the Church is like a vessel crossing the wide sea [[w.quote.a]].", EPHREM_REPOSITORY, voiced=voiced)
    assert entry["verdict"] == "withhold"
    assert entry["why"] == "quote record's speaker named without its placed quote"
    refer_back = _entry("We speak of the Church as a ship on the wide sea [[w.quote.a]].", EPHREM_REPOSITORY, voiced=voiced)
    assert refer_back["verdict"] == "ok"


def test_untagged_attribution_forms_are_refused():
    for text in (
        "Ephrem says, the Church is a ship that crosses the wide sea.",
        "Ephrem: the Church is a ship that crosses the wide sea.",
        "The Church is a ship that crosses the wide sea — Ephrem.",
        "The Church is a ship that crosses the wide sea - Ephrem, Hymns on the Church 12.",
        "As Ephrem wrote, the Church is a ship that crosses the wide sea.",
        "According to Ephrem: the Church is a ship that crosses the wide sea.",
    ):
        whys = _whys(text, EPHREM_REPOSITORY)
        assert whys[0][1:] == ("withhold", ATTRIBUTED), text


def test_put_it_this_way_followed_by_unplaced_words_is_refused_with_the_words():
    whys = _whys(f"Ephrem put it this way. The Church is a ship on the wide sea. {CLEAN}", EPHREM_REPOSITORY)
    assert [w[2] for w in whys] == [
        "introduces words that are not a placed quote",
        "words after an attribution, not a placed quote",
        "words after an attribution, not a placed quote",
    ]


def test_every_sentence_after_an_attribution_colon_goes_not_only_the_first():
    whys = _whys("Ephrem wrote: the Church is a ship. It crosses the wide sea. It does not sink.", EPHREM_REPOSITORY)
    assert [w[2] for w in whys] == [
        ATTRIBUTED,
        "words after an attribution, not a placed quote",
        "words after an attribution, not a placed quote",
    ]
    whys = _whys(f"Ephrem wrote:\n\nThe Church is a ship. It crosses the wide sea.\n\n{CLEAN}", EPHREM_REPOSITORY)
    assert [w[1] for w in whys] == ["withhold", "withhold", "withhold", "ok"]


def test_an_introduction_followed_by_a_placed_quote_stands():
    placed_sentence = f"“{EPHREM_QUOTE['modern_rendering']}” [[w.quote.a]]"
    for text in (f"Ephrem put it this way. {placed_sentence}", f"Ephrem said this:\n\n{placed_sentence}"):
        result = check_turn(text, EPHREM_REPOSITORY, placed={strip_tags(placed_sentence).strip(): "w.quote.a"})
        lead, quote = result["sentences"]
        assert lead["why"] not in QUOTATION_DROP_REASONS, text
        assert quote["verdict"] == "ok" and quote["placed_quote"] == "w.quote.a", text


def test_a_typed_quotation_standing_alone_takes_its_lead_in():
    whys = _whys(f'Ephrem answered the charge. "The Church is a ship on the wide sea." {CLEAN}', EPHREM_REPOSITORY)
    assert [w[2] for w in whys][:2] == ["lead-in to a quotation typed by the voice", TYPED]
    assert whys[2][1] == "ok"


# --- a quote's words, by wording ---------------------------------------------------

QUOTE_WORDS = "gives a quote record's words without placing it"
SHIP_QUOTE = {
    "id": "w.quote.ship", "record_type": "quote", "speaker_or_author": "w.figure.ephrem",
    "text": "The Church is a ship that saileth upon the wide sea of this world.",
    "modern_rendering": "The Church is a ship that sails the wide sea of this world. Her mast is the cross and her pilot is Christ, who brings her safe to harbour.",
    "use_note": {"means": "Ephrem likens the Church to a ship crossing the sea of the world with the cross for its mast."},
}
SHIP_WITNESS = {
    "id": "w.witness.ship", "record_type": "doctrinal_witness",
    "text": "We speak of the Church as a ship whose mast is the cross and whose pilot is Christ, bringing her safe to harbour.",
}
SHIP_REPOSITORY = {r["id"]: r for r in (EPHREM, SHIP_QUOTE, SHIP_WITNESS)}
SHIP_RETOLD = "the Church is a vessel on the wide sea of the world, the cross her mast and Christ her pilot"


def test_a_quotes_words_in_other_words_are_refused_and_name_the_quote():
    for text in (f"Ephrem sang: {SHIP_RETOLD}.", f"{SHIP_RETOLD[0].upper()}{SHIP_RETOLD[1:]}."):
        entry = _entry(text, SHIP_REPOSITORY)
        assert (entry["verdict"], entry["why"], entry["quote_words_of"]) == ("withhold", QUOTE_WORDS, "w.quote.ship"), text
    assert QUOTE_WORDS in QUOTATION_DROP_REASONS


def test_a_quotes_own_gist_is_not_its_words():
    assert _entry(SHIP_QUOTE["use_note"]["means"], SHIP_REPOSITORY)["why"] != QUOTE_WORDS


def test_a_record_the_sentence_is_tagged_to_may_hold_the_same_words_unless_the_speaker_is_named():
    words = "the Church is a ship whose mast is the cross and whose pilot is Christ, safe to harbour"
    assert _entry(f"For us, {words} [[w.witness.ship]].", SHIP_REPOSITORY)["verdict"] == "ok"
    assert _entry(f"Ephrem sang that {words} [[w.witness.ship]].", SHIP_REPOSITORY)["why"] == QUOTE_WORDS


def test_a_quote_already_voiced_is_not_checked_for_its_words():
    sentence = f"Ephrem sang: {SHIP_RETOLD}."
    assert _entry(sentence, SHIP_REPOSITORY, voiced=frozenset({"w.quote.ship"}))["why"] != QUOTE_WORDS


def test_the_participants_own_words_are_not_a_quotes_words():
    sentence = f"You asked whether {SHIP_RETOLD}."
    asked = [f"Is it true that {SHIP_RETOLD}?"]
    assert _entry(sentence, SHIP_REPOSITORY, quotable_texts=asked)["why"] != QUOTE_WORDS


# --- quotation forms -------------------------------------------------------------


def test_corner_brackets_are_quotation_marks():
    assert [span for _s, _e, span in quoted_span_positions("He said 「no deception」 and『no mixture』.")] == [
        "no deception", "no mixture",
    ]
    entry = _entry("Ephrem wrote 「the Church is a ship that crosses the wide sea」.", EPHREM_REPOSITORY)
    assert entry["why"] == TYPED


def test_a_speaker_named_in_lower_case_is_still_named():
    assert _whys("ephrem says, the Church is a ship that crosses the wide sea.", EPHREM_REPOSITORY)[0][2] == ATTRIBUTED


def test_an_unclosed_guillemet_takes_the_rest_of_its_paragraph():
    whys = _whys("We hold this «The Church is a ship. It crosses the sea.\n\n" + CLEAN, EPHREM_REPOSITORY)
    assert [w[1] for w in whys] == ["withhold", "withhold", "ok"]


def test_a_closed_guillemet_quotation_is_one_sentence_withheld_whole():
    whys = _whys("We hold this «The Church is a ship. It crosses the sea.»\n\n" + CLEAN, EPHREM_REPOSITORY)
    assert [(w[0], w[1]) for w in whys] == [
        ("We hold this «The Church is a ship. It crosses the sea.»", "withhold"),
        ("We hold that the Church is one body.", "ok"),
    ]


def test_the_worlds_own_we_voice_and_ordinary_prose_are_not_attributions():
    for text in (
        "We say it plainly: the Church is one body [[w.witness.church]].",
        "As we said, the Church is one body [[w.witness.church]].",
        "When Ephrem wrote, the Church was gathered at one table [[w.witness.church]].",
        "Ephrem wrote hymns for the Church [[w.witness.church]].",
    ):
        assert _entry(text, EPHREM_REPOSITORY)["why"] not in (ATTRIBUTED, TYPED), text
