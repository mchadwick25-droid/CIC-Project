from engine.m5.anachronism import anachronistic_term_ids, resolve_term_ids, terms_in_message

WINDOW = {"start": 150, "end": 400}

TERMS = {
    "_fleet.modern.trinity": {"id": "_fleet.modern.trinity", "record_type": "modern_term", "origin_year": 325},
    "_fleet.modern.rapture": {"id": "_fleet.modern.rapture", "record_type": "modern_term", "origin_year": 1830},
    "_fleet.modern.unknown_year": {"id": "_fleet.modern.unknown_year", "record_type": "modern_term", "origin_year": None},
    "_fleet.canon.c-i-01": {"id": "_fleet.canon.c-i-01", "record_type": "canon_question"},
}


def test_term_within_window_not_anachronistic():
    assert "_fleet.modern.trinity" not in anachronistic_term_ids(TERMS, WINDOW)


def test_term_after_window_is_anachronistic():
    assert "_fleet.modern.rapture" in anachronistic_term_ids(TERMS, WINDOW)


def test_unknown_origin_year_not_flagged():
    assert "_fleet.modern.unknown_year" not in anachronistic_term_ids(TERMS, WINDOW)


def test_non_modern_term_records_ignored():
    ids = anachronistic_term_ids(TERMS, WINDOW)
    assert "_fleet.canon.c-i-01" not in ids


DISPLAY_TERMS = {
    "_fleet.modern.trinity": {
        "id": "_fleet.modern.trinity",
        "record_type": "modern_term",
        "origin_year": 325,
        "display_terms": ["Trinity", "Trinitarian"],
    },
    "_fleet.modern.born_again": {
        "id": "_fleet.modern.born_again",
        "record_type": "modern_term",
        "origin_year": 1730,
        "display_terms": ["born again"],
    },
    "_fleet.canon.c-i-01": {"id": "_fleet.canon.c-i-01", "record_type": "canon_question", "display_terms": ["Trinity"]},
}


def test_the_readers_invented_id_is_replaced_by_the_fleet_record_id():
    """The live failure this exists to prevent: the reader
    returned term_id "trinity_doctrine" for a Trinity question, routing
    intersected it against fleet record ids, found nothing, and bridge_turn
    - built and passing its own tests - was unreachable by any session."""
    resolved = resolve_term_ids([{"term_id": "trinity_doctrine", "display": "the Trinity"}], DISPLAY_TERMS)
    assert resolved[0]["term_id"] == "_fleet.modern.trinity"


def test_the_readers_own_id_is_kept_alongside_not_erased():
    resolved = resolve_term_ids([{"term_id": "trinity_doctrine", "display": "the Trinity"}], DISPLAY_TERMS)
    assert resolved[0]["reader_term_id"] == "trinity_doctrine"
    assert resolved[0]["display"] == "the Trinity"


def test_an_alternate_display_term_on_the_same_record_resolves_to_it():
    resolved = resolve_term_ids([{"term_id": "whatever", "display": "Trinitarian language"}], DISPLAY_TERMS)
    assert resolved[0]["term_id"] == "_fleet.modern.trinity"


def test_a_multi_word_display_term_matches_only_as_a_contiguous_run():
    hit = resolve_term_ids([{"term_id": "x", "display": "being born again"}], DISPLAY_TERMS)
    assert hit[0]["term_id"] == "_fleet.modern.born_again"
    miss = resolve_term_ids([{"term_id": "x", "display": "born, and again"}], DISPLAY_TERMS)
    assert miss[0]["term_id"] == "x"


def test_a_term_with_no_matching_record_keeps_the_readers_id():
    resolved = resolve_term_ids([{"term_id": "personal_savior", "display": "personal Lord and Savior"}], DISPLAY_TERMS)
    assert resolved[0]["term_id"] == "personal_savior"
    assert "reader_term_id" not in resolved[0]


def test_non_modern_term_records_are_not_matchable():
    """The canon_question above carries a display_terms field on purpose -
    only record_type modern_term may lend an id to a bridge."""
    resolved = resolve_term_ids([{"term_id": "x", "display": "Trinity"}], DISPLAY_TERMS)
    assert resolved[0]["term_id"] == "_fleet.modern.trinity"


def test_no_flagged_terms_resolves_to_nothing():
    assert resolve_term_ids([], DISPLAY_TERMS) == []
    assert resolve_term_ids(None, DISPLAY_TERMS) == []


def test_the_word_in_the_message_is_found_without_the_reader():
    """The live failure this exists to prevent: same world, same day, same
    question in identical words - the reader flagged "Trinity" twice and
    returned modern_terms: [] the third time. An id fix cannot help a flag
    that never came."""
    found = terms_in_message("How did your community understand the Trinity?", DISPLAY_TERMS)
    assert [t["term_id"] for t in found] == ["_fleet.modern.trinity"]
    assert found[0]["source"] == "message_scan"


def test_a_multi_word_term_is_found_across_the_message():
    found = terms_in_message("were any of you born again the way people mean now", DISPLAY_TERMS)
    assert [t["term_id"] for t in found] == ["_fleet.modern.born_again"]


def test_a_message_with_no_fleet_term_finds_nothing():
    assert terms_in_message("who was Jesus to your people", DISPLAY_TERMS) == []


def test_a_term_the_reader_already_resolved_is_not_carried_twice():
    resolved = resolve_term_ids([{"term_id": "trinity_doctrine", "display": "the Trinity"}], DISPLAY_TERMS)
    extra = terms_in_message("about the Trinity", DISPLAY_TERMS, already_found={t["term_id"] for t in resolved})
    assert extra == []


def test_matching_is_whole_token_not_prefix():
    """Stated limit, not an oversight: an inflection a record wants matched
    goes in that record's own display_terms."""
    assert terms_in_message("what about Trinitarianism", DISPLAY_TERMS) == []
    assert [t["term_id"] for t in terms_in_message("Trinitarian language", DISPLAY_TERMS)] == ["_fleet.modern.trinity"]


def test_only_modern_term_records_are_scanned_for():
    """The canon_question in the fixture carries a display_terms field on
    purpose - a record type that is not modern_term may not fire a bridge."""
    found = terms_in_message("the Trinity", DISPLAY_TERMS)
    assert all(t["term_id"] == "_fleet.modern.trinity" for t in found)
