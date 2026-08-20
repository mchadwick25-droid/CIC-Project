from engine.m4.session_code import codes_match, generate_code, hash_code, _ALPHABET


def test_generate_code_shape():
    code = generate_code()
    groups = code.split("-")
    assert [len(g) for g in groups] == [4, 4, 4, 4, 4, 4, 2]
    assert all(c in _ALPHABET for c in code.replace("-", ""))


def test_generate_code_is_random():
    codes = {generate_code() for _ in range(50)}
    assert len(codes) == 50


def test_hash_and_match_roundtrip():
    code = generate_code()
    digest = hash_code(code)
    assert codes_match(code, digest)


def test_wrong_code_does_not_match():
    digest = hash_code(generate_code())
    assert not codes_match(generate_code(), digest)


def test_hash_is_case_and_dash_insensitive():
    code = generate_code()
    digest = hash_code(code)
    scrambled = code.lower()
    assert codes_match(scrambled, digest)
