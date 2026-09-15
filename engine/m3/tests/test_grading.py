from engine.m3.grading import register_check, source_boundedness_check
from engine.m3.masking import mask_for_grading

_BASE = dict(probe_id="p1", cell="C-I", probe_text="probe text")


def _transcript(citations):
    return mask_for_grading(**_BASE, answer_text="an answer", citations=citations)


def test_a_citation_that_resolves_to_a_source_passes_with_no_findings():
    result = source_boundedness_check(_transcript(["w.source.a"]), known_source_ids={"w.source.a"})
    assert result.passed
    assert result.findings == []


def test_a_citation_to_neither_path_still_fails():
    """The evidence-status category must not become a laxer
    source_boundedness in disguise - a citation naming nothing real, by
    either path, is still a fabrication finding."""
    result = source_boundedness_check(
        _transcript(["w.invented.nothing"]), known_source_ids={"w.source.a"}
    )
    assert not result.passed
    assert "w.invented.nothing" in result.findings[0]


def test_no_citations_at_all_still_passes_with_no_findings():
    result = source_boundedness_check(_transcript([]), known_source_ids={"w.source.a"})
    assert result.passed
    assert result.findings == []


def test_a_citation_to_an_evidence_status_id_passes_but_is_named_as_such():
    """The fleet's third citation category (engine.m1.canon.evidence_status_
    types): a search record is definitionally sourceless - it documents the
    looking itself - so citing one grounds an honest evidence-of-absence
    claim. Found live (hal, 2026-08-28): the voice answered an evidence-
    pressure probe with "the richness is in the letters, not in the stones"
    and cited hal.search.latin-critical-texts (result: not_found) - a real,
    apt citation the check then called fabricated. Like the scaffold
    category, passing this way is named, never silent."""
    result = source_boundedness_check(
        _transcript(["w.search.absent-thing"]), known_source_ids=set(), evidence_status_ids={"w.search.absent-thing"}
    )
    assert result.passed
    assert len(result.findings) == 1
    assert "accepted as evidence-status disclosure" in result.findings[0]
    assert "w.search.absent-thing" in result.findings[0]


def test_a_citation_clearing_no_category_fails_even_with_both_supplied():
    result = source_boundedness_check(
        _transcript(["w.invented.nothing"]),
        known_source_ids={"w.source.a"},
        evidence_status_ids={"w.search.absent-thing"},
    )
    assert not result.passed
    assert "w.invented.nothing" in result.findings[0]


def test_a_mix_of_source_and_evidence_status_citations_names_only_the_latter():
    result = source_boundedness_check(
        _transcript(["w.source.a", "w.search.absent-thing"]),
        known_source_ids={"w.source.a"},
        evidence_status_ids={"w.search.absent-thing"},
    )
    assert result.passed
    assert len(result.findings) == 1
    assert "evidence-status" in result.findings[0] and "w.search.absent-thing" in result.findings[0]


def test_omitting_evidence_status_ids_keeps_the_strict_behavior():
    """Same backward-compatible contract as the scaffold default: a caller
    that never heard of the category gets the stricter check."""
    result = source_boundedness_check(_transcript(["w.search.absent-thing"]), known_source_ids=set())
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


def test_miscopied_address_downgrades_to_review_fabrication_still_fails():
    """Option A (Mark's ruling, 2026-08-29): an invented ADDRESS on a
    sentence whose content lives in the world's records passes with a
    review finding; invented CONTENT still fails. Fixtures are the two
    real cases from live-admission-report-revert-final-2026-08-29."""
    from engine.m3.grading import source_boundedness_check
    from engine.m3.masking import mask_for_grading

    repo = {
        "w.gravity.elder-authority": {"id": "w.gravity.elder-authority", "description":
            "An unresolved tension between elder-based authority and office-based authority, "
            "the solitary pattern and the Rule-governed pattern differing in how authority was held."},
        "w.core.world": {"id": "w.core.world", "cautions":
            "Nearly everything known of the women reaches readers through one man's pen, in letters "
            "and memorials he chose to write and keep - the central structural limit on every claim."},
    }
    known = {"w.gravity.elder-authority", "w.core.world"}

    # miscopied address: content verifies against the gravity record
    t = mask_for_grading(
        probe_id="p1", cell="F4-I", probe_text="q", answer_text="...",
        citations=["w.limit.authority-tension"],
        citation_entries=[{"sentence": "The solitary pattern and the Rule-governed pattern differed, "
                                       "an unresolved tension between elder-based and office-based authority.",
                           "record_ids": ["w.limit.authority-tension"]}],
    )
    r = source_boundedness_check(t, known, repository_records=repo)
    assert r.passed and "MISCOPIED ADDRESS" in r.findings[0] and "w.gravity.elder-authority" in r.findings[0]

    # fabricated content: verifies nowhere -> fails exactly as before
    t2 = mask_for_grading(
        probe_id="p2", cell="F4-I", probe_text="q", answer_text="...",
        citations=["w.limit.zebra-quills"],
        citation_entries=[{"sentence": "Our elders rode zebras across the frozen sea each winter solstice.",
                           "record_ids": ["w.limit.zebra-quills"]}],
    )
    r2 = source_boundedness_check(t2, known, repository_records=repo)
    assert not r2.passed and "w.limit.zebra-quills" in r2.findings[0]

    # no carrying sentence locatable -> fails (never downgraded blind)
    t3 = mask_for_grading(
        probe_id="p3", cell="F4-I", probe_text="q", answer_text="...",
        citations=["w.limit.orphan"], citation_entries=[],
    )
    r3 = source_boundedness_check(t3, known, repository_records=repo)
    assert not r3.passed

    # legacy caller without repository_records -> old strict behavior
    r4 = source_boundedness_check(t, known)
    assert not r4.passed
