"""Hermetic tests for grounding_net.py (Live-Generation Design §6, forks
signed off - LIVE-GENERATION-DESIGN.md §9.5). Synthetic records, same
shape/discipline as test_grounding.py's fixtures - not tied to any real
package path, so these run without a compiled package on disk. Real-data
verification (against the current alx/pahc/ijc packages) is a separate,
manual step recorded in the session's own commit history, not repeated
here as a hermetic test.
"""
from engine.m4.grounding_net import build_figure_lexicon, check_turn, parse_tagged, scope_completion, strip_tags

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


# ---------------------------------------------------------------------------
# Double-quoted spans.
#
# For a long time only the straight SINGLE quote was recognised, because that
# is the convention the records corpus was written in. A live model quotes
# with " far more readily, whatever the prompt around it does - and the
# corpus itself already held 249 paired double-quoted spans. Every test above
# this line uses ' and so passed throughout.
# ---------------------------------------------------------------------------
from engine.m1.gates_experimental import _quoted_spans


def test_double_quoted_span_is_found_at_all():
    """The precondition for everything below: a double-quoted span used to
    return no spans whatsoever, so the verbatim branch never ran."""
    assert _quoted_spans('He said: "Behold the might of the new song."') == [
        "Behold the might of the new song."
    ]


def test_double_quoted_verbatim_quote_correctly_tagged_passes():
    """The verbatim branch is the LENIENT path - it exists so framing words
    around a real quote can never sink a real quote. With no span found, a
    double-quoted sentence skipped it and fell through to the ratio floor
    instead, which is a bar a short quote with long framing routinely
    misses."""
    text = 'As it was sung, "Behold the might of the new song! It has made men out of stones, men out of beasts." [[fix.quote.new-song]]'
    result = check_turn(text, REPOSITORY)
    assert result["sentences"][0]["verdict"] == "ok"
    assert "verbatim" in result["sentences"][0]["why"]


def test_coined_double_quoted_words_under_a_real_tag_are_still_withheld():
    """Recognising " must not become a way to smuggle invented words past
    the check - the same rule applies, it just applies at all now."""
    text = 'As it was sung, "Behold the wonder of the ancient hymn, made new for us." [[fix.quote.new-song]]'
    assert check_turn(text, REPOSITORY)["sentences"][0]["verdict"] == "withhold"


def test_double_quote_split_across_a_sentence_boundary_is_remerged():
    """The defect as a participant met it. The naive splitter broke after
    "new song!", orphaning `It has made men out of stones, men out of
    beasts".` - which then reached a participant on its own while its
    opening clause ("Clement... called him the New Song:") was silently
    withheld for having no tag. Seen live, 2026-08-23, alx, "Who was Jesus
    to your people?\""""
    text = 'Clement called him the New Song: "Behold the might of the new song! It has made men out of stones, men out of beasts." [[fix.quote.new-song]]'
    parsed = parse_tagged(text)
    assert len(parsed) == 1
    assert parsed[0]["tags"] == ["fix.quote.new-song"]
    assert check_turn(text, REPOSITORY)["sentences"][0]["verdict"] == "ok"


def test_an_apostrophe_is_still_never_a_quote():
    """The regression the single-quote guards exist for, re-asserted now
    that there are more families to get wrong."""
    assert _quoted_spans("God's own Word, and the teachers' own work") == []


def test_a_double_quoted_span_nested_in_a_single_quoted_one_pairs_within_its_own_family():
    """Walked per family, so a ' opener can never be closed by a " - and the
    nested span is reported alongside its container, which is stricter (both
    must be verbatim), never looser."""
    spans = _quoted_spans("""He wrote: 'the one they called "the Physician" healed us.'""")
    assert 'the one they called "the Physician" healed us.' in spans
    assert "the Physician" in spans
