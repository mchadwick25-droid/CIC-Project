import math

from engine.deeper import codes


def test_generate_shape_and_entropy():
    code = codes.generate()
    assert len(code) == 20
    assert set(code) <= set(codes.ALPHABET)
    assert len(codes.ALPHABET) == 32
    assert math.log2(len(codes.ALPHABET)) * codes.CODE_LENGTH == 100


def test_alphabet_has_no_lookalikes():
    for ch in "01OI":
        assert ch not in codes.ALPHABET


def test_generated_codes_differ():
    assert len({codes.generate() for _ in range(200)}) == 200


def test_normalize_forgives_case_and_spacing_only():
    code = codes.generate()
    assert codes.normalize(codes.display(code)) == code
    assert codes.normalize(code.lower()) == code
    assert codes.normalize("  " + codes.display(code).replace(" ", "-") + "\n") == code
    assert codes.normalize(code[:-1]) is None
    assert codes.normalize(code + "2") is None
    assert codes.normalize("0" * 20) is None
    assert codes.normalize(None) is None
    assert codes.normalize(12345) is None


def test_display_groups_of_four():
    assert codes.display("ABCDEFGHJKLMNPQRSTUV") == "ABCD EFGH JKLM NPQR STUV"


def test_hash_is_stable_and_not_the_code():
    code = codes.generate()
    assert codes.hash_code(code) == codes.hash_code(code)
    assert code not in codes.hash_code(code)
    assert codes.hashes_match(codes.hash_code(code), codes.hash_code(code))
    assert not codes.hashes_match(codes.hash_code(code), codes.hash_code(codes.generate()))


def test_redact_shows_four_characters_at_most():
    code = codes.generate()
    assert codes.redact(code) == code[:4] + "..."
    assert codes.redact("not a code") == "invalid"
    assert code not in codes.redact(code)
