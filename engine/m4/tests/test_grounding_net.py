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
# check_display_text - the finished string a participant reads.
#
# Every other check here runs on a record, a sentence, or a tag. These are
# the things that reached real participants across 49 live turns.
# ---------------------------------------------------------------------------
from engine.m4.grounding_net import check_display_text


def test_markdown_emphasis_reaching_a_reader_is_reported():
    """Seen in 5 of 49 live turns - a participant reads the asterisks."""
    found = check_display_text("They called this deeper reading *allegoria* - the spiritual sense.")
    assert [f["kind"] for f in found] == ["markdown_emphasis"]
    assert found[0]["excerpt"] == "*allegoria*"


def test_a_horizontal_rule_opening_an_answer_is_reported():
    """Seen once: the model echoed the question, the net withheld the echo,
    and the rule under it survived attached to the next sentence."""
    assert [f["kind"] for f in check_display_text("---\n\nWhat we had of Jesus was one command.")] == ["markdown_rule"]


def test_a_malformed_tag_survives_strip_tags_and_is_reported():
    """The citation contract promises tags are never shown. strip_tags keeps
    that promise only for tags the model spells correctly - its pattern is
    [a-z0-9_.-] with no spaces."""
    text = "The texture of daily life is missing [[THIN GROUND: ordinary, daily life]]."
    assert strip_tags(text) == text, "precondition: strip_tags cannot remove this"
    assert [f["kind"] for f in check_display_text(text)] == ["residual_tag"]


def test_ordinary_prose_is_clean():
    assert check_display_text("A real man, really killed, really raised, and now the one through whom we give thanks.") == []


def test_an_asterisk_used_as_arithmetic_is_not_emphasis():
    assert check_display_text("We paid 5 * 3 denarii and moved on.") == []


# ---- the three narrowings (2026-08-23) -------------------------------------
# Each of these fired on real live output and deleted prose that invented
# nothing. Counts are from 17 measured turns / 68 withheld sentences.

def test_parallel_prose_is_not_an_enumeration():
    # 9 of 68 withholds. Short parallel clauses are what register statements
    # 2 and 3 ask the voice to write; the old short-segment count deleted them.
    from engine.m1.gates_experimental import _claim_markers
    assert _claim_markers("We lived among them, learned from them, argued with them.") == []
    assert _claim_markers("That, too, I can show you.") == []
    # the repeated-phrase signal the rule was actually built for survives
    assert "enumeration" in _claim_markers("The same water, the same bread.")


def test_common_words_are_not_treated_as_names():
    # 10 of 68. "scripture" was already exempt and "Scriptures" was not.
    from engine.m1.gates_experimental import _claim_markers
    assert _claim_markers("We held that the Scriptures are alive, not a closed book.") == []
    assert _claim_markers("To become a Christian among us was to be changed.") == []
    # a real name still marks the sentence as checkable
    assert any("proper-noun" in m for m in _claim_markers("Later, Athanasius put it in one sentence."))


def test_counting_the_readings_of_a_question_is_not_a_figure():
    # 7 of 68, and always the OPENING sentence - so the participant was
    # handed a list starting at item two.
    from engine.m1.gates_experimental import _claim_markers
    assert _claim_markers("I hear two ways to take your question, and I want to answer the one you meant.") == []
    assert _claim_markers("Your question can be heard three ways, and I must ask which you mean.") == []


def test_a_counted_doctrine_is_still_a_figure():
    # The first draft of the rule above freed this. It is a claim about the
    # world, not about the ask, and must stay checkable.
    from engine.m1.gates_experimental import _claim_markers
    assert "number" in _claim_markers("He would read a passage three ways, for body, soul, and spirit.")
    assert "number" in _claim_markers("For the first three centuries of our window, persecution came in waves.")
    assert "number" in _claim_markers("The boy was seventeen when his father was killed.")
