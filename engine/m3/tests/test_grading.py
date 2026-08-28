from engine.m3.grading import register_check, source_boundedness_check
from engine.m3.masking import mask_for_grading

_BASE = dict(probe_id="p1", cell="C-I", probe_text="probe text")


def _transcript(citations):
    return mask_for_grading(**_BASE, answer_text="an answer", citations=citations)


def test_a_citation_that_resolves_to_a_source_passes_with_no_findings():
    result = source_boundedness_check(_transcript(["w.source.a"]), known_source_ids={"w.source.a"})
    assert result.passed
    assert result.findings == []


def test_a_citation_to_a_voice_scaffold_id_passes_but_is_named_as_such():
    """The fleet's second citation category (engine.m1.canon.voice_scaffold_
    types): a real, honest citation into the voice's own identity/craft
    record - never a source, never expected to be one. Passing must not
    look identical to a source-bounded pass: the finding names WHICH
    category cleared it, so a report reader can tell the two apart."""
    result = source_boundedness_check(
        _transcript(["w.voice.craft"]), known_source_ids=set(), voice_scaffold_ids={"w.voice.craft"}
    )
    assert result.passed
    assert result.findings == [
        "probe p1: citation(s) accepted as voice-scaffold self-attribution, not source evidence: ['w.voice.craft']"
    ]


def test_a_citation_to_neither_category_still_fails():
    """The exemption must not become a laxer source_boundedness in
    disguise - a citation naming nothing real, by either path, is still a
    fabrication finding."""
    result = source_boundedness_check(
        _transcript(["w.invented.nothing"]), known_source_ids={"w.source.a"}, voice_scaffold_ids={"w.voice.craft"}
    )
    assert not result.passed
    assert "w.invented.nothing" in result.findings[0]


def test_a_mix_of_source_and_scaffold_citations_passes_and_names_only_the_scaffold_one():
    result = source_boundedness_check(
        _transcript(["w.source.a", "w.voice.craft"]), known_source_ids={"w.source.a"}, voice_scaffold_ids={"w.voice.craft"}
    )
    assert result.passed
    assert result.findings == [
        "probe p1: citation(s) accepted as voice-scaffold self-attribution, not source evidence: ['w.voice.craft']"
    ]


def test_no_citations_at_all_still_passes_with_no_findings():
    result = source_boundedness_check(_transcript([]), known_source_ids={"w.source.a"}, voice_scaffold_ids={"w.voice.craft"})
    assert result.passed
    assert result.findings == []


def test_omitting_voice_scaffold_ids_keeps_the_old_strict_behavior():
    """Backward-compatible default: a caller that never heard of the
    scaffold category (there is none left in this repo, but the default
    itself is the contract) gets exactly the old, single-category check."""
    result = source_boundedness_check(_transcript(["w.voice.craft"]), known_source_ids=set())
    assert not result.passed


def test_register_coined_aphorism_is_advisory_never_gating():
    """Mark's ruling, 2026-08-28: register statement 6 is direction, not a
    gate - the heuristic keeps detecting (the finding lands, visibly) but
    the check passes. The selftest's seeded-defect proof counts detection
    through this advisory channel."""
    transcript = mask_for_grading(
        **_BASE, answer_text="Faith is the bridge that carries us over the river of doubt.", citations=[]
    )
    result = register_check(transcript, known_quote_texts=set())
    assert result.passed
    assert len(result.findings) == 1
    assert "ADVISORY" in result.findings[0]
    assert "is the bridge that" in result.findings[0]


def test_register_grounded_by_verbatim_quote_stays_silent():
    quote = "faith is the bridge that carries us"
    transcript = mask_for_grading(
        **_BASE, answer_text=f'One of our elders said: "{quote}" - and we held to it.', citations=[]
    )
    result = register_check(transcript, known_quote_texts={quote})
    assert result.passed
    assert result.findings == []


def test_register_plain_prose_stays_silent():
    transcript = mask_for_grading(**_BASE, answer_text="We prayed at dawn and worked with our hands.", citations=[])
    result = register_check(transcript, known_quote_texts=set())
    assert result.passed
    assert result.findings == []
