import pytest

from answering_library import curation as cu
from answering_library import markers as mk
from answering_library import ordinals


@pytest.mark.parametrize("token,value", [
    ("CLXXXVIII", 188), ("CCCLXXXVIII", 388), ("MMMDCCCLXXXVIII", 3888), ("MMMCMXCIX", 3999),
    ("xliv", 44), ("IIII", 4), ("XXXX", 40), ("VIIII", 9), ("I", 1), ("MCMXC", 1990),
])
def test_roman_numerals_up_to_the_longest_valid_one(token, value):
    assert mk.roman_value(token) == value


@pytest.mark.parametrize("token", ["", "VX", "IIX", "MIXLCD", "IVIV", "MMMM", "MMMDCCCLXXXVIIIX", "ABC", "IL1"])
def test_non_numerals_are_rejected(token):
    assert mk.roman_value(token) is None


def test_ocr_damage_is_read_through_the_curation_map():
    assert cu.to_int("CLXXXVl", {"l": "I"}) == 186
    assert cu.to_int("Cl", {"l": "I"}) == 101


@pytest.mark.parametrize("word,value", [
    ("Erstes", 1), ("Zweites", 2), ("Dritter", 3), ("Vierte", 4), ("Fünfte", 5), ("Funfte", 5), ("fuenfte", 5),
    ("Zwölfte", 12), ("Zwolfte", 12), ("Neunzehnter", 19), ("Zwanzigste", 20), ("Achtunddreissigster", 38),
    ("Achtunddreißigster", 38), ("Hunderterste", 101),
    ("Premier", 1), ("Première", 1), ("Premiere", 1), ("Second", 2), ("Deuxième", 2), ("Deuxieme", 2),
    ("Troisieme", 3), ("Cinquieme", 5), ("Sixieme", 6), ("Neuvième", 9), ("Douzième", 12),
    ("Vingt-et-unième", 21), ("Soixante-et-onzième", 71), ("Quatre-vingtième", 80), ("Quatre-vingt-dixième", 90),
    ("Primus", 1), ("Tertia", 3), ("Octavus", 8), ("Decimum", 10),
    ("Primo", 1), ("Seconda", 2), ("Settimo", 7), ("Decimo", 10),
    ("Seventh", 7), ("Twelfth", 12),
])
def test_ordinal_words_read_to_their_values(word, value):
    assert ordinals.ordinal_value(word) == value
    assert mk.number_value(word) == value
    assert cu.to_int(word) == value


@pytest.mark.parametrize("word", ["Erstens", "Zweiterr", "Deuxiemes", "Sedecimus", "Banana", "Hundert"])
def test_words_outside_the_tables_have_no_value(word):
    assert ordinals.ordinal_value(word) is None


def test_every_german_and_french_ordinal_up_to_the_table_edge_is_present():
    values = set(ordinals.TABLE.values())
    assert set(range(1, 1000)) <= values
