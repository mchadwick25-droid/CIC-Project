from engine.m5.anachronism import anachronistic_term_ids, resolve_term_ids

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
    """The live failure this exists to prevent: on 2026-08-24 the reader
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
