from datetime import date

import pytest

from engine.accounts.keys import AccountsKeyError, KeyRing, PreviousKey, normalise_address, parse_previous

A, S = "a" * 40, "s" * 40


def test_an_address_is_normalised_before_it_is_hashed():
    assert normalise_address("  Ada@Example.ORG ") == "ada@example.org"
    assert normalise_address("ada+news@example.org") == "ada+news@example.org"
    assert normalise_address("ａｄａ@example.org") == "ada@example.org"


@pytest.mark.parametrize("bad", [None, 5, "", "ada", "ada@", "@example.org", "ada@example", "a b@example.org",
                                 "ada@@example.org", "ada@example..org", "ada@.example.org", "ada@example.org.",
                                 "ada\x00@example.org", "a" * 65 + "@example.org", "x@" + "a" * 260 + ".org"])
def test_what_cannot_be_an_address_is_refused(bad):
    assert normalise_address(bad) is None


def test_the_hash_is_stable_keyed_and_carries_its_key_id():
    one = KeyRing(A, S).address_hash("ada@example.org")
    assert one == KeyRing(A, S).address_hash("ADA@example.org")
    assert one.startswith("k1:") and "ada" not in one
    assert KeyRing("b" * 40, S).address_hash("ada@example.org") != one


def test_keys_must_be_long_distinct_and_named_sensibly():
    with pytest.raises(AccountsKeyError):
        KeyRing("short", S)
    with pytest.raises(AccountsKeyError):
        KeyRing(A, A)
    with pytest.raises(AccountsKeyError):
        KeyRing(A, S, key_id="K 1")
    with pytest.raises(AccountsKeyError):
        KeyRing(A, S, previous=[PreviousKey("k1", "p" * 40, date(2030, 1, 1))])
    with pytest.raises(AccountsKeyError):
        KeyRing(A, S, previous=[PreviousKey("k0", A, date(2030, 1, 1))])


def test_an_old_key_still_verifies_until_its_retirement_date():
    old = KeyRing("o" * 40, S, key_id="k0")
    old_hash = old.address_hash("ada@example.org")
    previous = [PreviousKey("k0", "o" * 40, date(2027, 1, 31))]
    live = KeyRing(A, S, key_id="k1", previous=previous, today=lambda: date(2027, 1, 31))
    assert old_hash in live.candidate_hashes("ada@example.org")
    assert live.candidate_hashes("ada@example.org")[0] == live.address_hash("ada@example.org")
    assert not live.is_current(old_hash)
    retired = KeyRing(A, S, key_id="k1", previous=previous, today=lambda: date(2027, 2, 1))
    assert old_hash not in retired.candidate_hashes("ada@example.org")


def test_previous_keys_parse_and_reject_bad_specs():
    assert parse_previous("") == []
    assert parse_previous("k0:" + "o" * 40 + ":" + date(2027, 1, 31).isoformat())[0].retire_on == date(2027, 1, 31)
    with pytest.raises(AccountsKeyError):
        parse_previous("k0:secret")
    with pytest.raises(AccountsKeyError):
        parse_previous("k0:secret:soon")


def test_a_cookie_carries_a_token_and_a_tag_that_cannot_be_forged():
    keys = KeyRing(A, S)
    cookie = keys.sign_cookie("tokentoken")
    assert keys.open_cookie(cookie) == "tokentoken"
    assert keys.open_cookie(cookie[:-1] + ("0" if cookie[-1] != "0" else "1")) is None
    assert keys.open_cookie("tokentoken") is None
    assert KeyRing(A, "t" * 40).open_cookie(cookie) is None
