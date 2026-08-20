from engine.m5.anachronism import anachronistic_term_ids

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
