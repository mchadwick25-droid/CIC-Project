"""The provider token check, against tokens signed with a key made here."""
import base64
import json

import pytest
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from engine.api.provider_tokens import CANONICAL_ISSUER, ProviderVerifier

NOW = 1_790_000_000
CLIENT = "client-123.apps.example"
NONCE = "nonce-abc"


def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _int(n: int) -> str:
    return _b64(n.to_bytes((n.bit_length() + 7) // 8, "big"))


@pytest.fixture(scope="module")
def key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def _jwks(key, kid="k1"):
    numbers = key.public_key().public_numbers()
    return {"keys": [{"kty": "RSA", "kid": kid, "n": _int(numbers.n), "e": _int(numbers.e)}]}


def _token(key, *, kid="k1", alg="RS256", **overrides):
    claims = {"iss": "https://accounts.google.com", "aud": CLIENT, "exp": NOW + 600, "iat": NOW, "nonce": NONCE, "sub": "1234"}
    claims.update(overrides)
    claims = {k: v for k, v in claims.items() if v is not None}
    head = _b64(json.dumps({"alg": alg, "kid": kid}).encode())
    body = _b64(json.dumps(claims).encode())
    signature = key.sign(f"{head}.{body}".encode(), padding.PKCS1v15(), hashes.SHA256())
    return f"{head}.{body}.{_b64(signature)}"


@pytest.fixture
def verifier(key):
    calls = []

    def fetch(url):
        calls.append(url)
        return _jwks(key)

    v = ProviderVerifier({"google": CLIENT, "apple": "com.example.web"}, fetch=fetch, clock=lambda: NOW)
    v.calls = calls
    return v


def test_a_genuine_token_gives_the_issuer_and_subject(verifier, key):
    assert verifier.verify("google", _token(key), NONCE) == (CANONICAL_ISSUER["google"], "1234")


def test_google_s_second_issuer_spelling_is_accepted(verifier, key):
    assert verifier.verify("google", _token(key, iss="accounts.google.com"), NONCE) == (CANONICAL_ISSUER["google"], "1234")


@pytest.mark.parametrize("change", [
    {"iss": "https://evil.example"}, {"aud": "someone-else"}, {"aud": [CLIENT]}, {"exp": NOW - 61}, {"exp": None},
    {"exp": True}, {"iat": NOW + 3600}, {"nonce": "other"}, {"nonce": None}, {"sub": ""}, {"sub": None}, {"sub": 1234},
    {"sub": "x" * 256},
])
def test_a_token_with_a_wrong_claim_is_refused(verifier, key, change):
    assert verifier.verify("google", _token(key, **change), NONCE) is None


def test_a_token_signed_by_another_key_is_refused(verifier):
    other = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    assert verifier.verify("google", _token(other), NONCE) is None


def test_a_changed_body_is_refused(verifier, key):
    head, body, signature = _token(key).split(".")
    forged = _b64(json.dumps({"iss": "https://accounts.google.com", "aud": CLIENT, "exp": NOW + 600, "nonce": NONCE, "sub": "other"}).encode())
    assert verifier.verify("google", f"{head}.{forged}.{signature}", NONCE) is None


@pytest.mark.parametrize("alg", ["none", "HS256", "RS512", "rs256"])
def test_only_rs256_is_accepted(verifier, key, alg):
    assert verifier.verify("google", _token(key, alg=alg), NONCE) is None


def test_an_unsigned_token_is_refused(verifier, key):
    head = _b64(json.dumps({"alg": "none"}).encode())
    body = _b64(json.dumps({"iss": "https://accounts.google.com", "aud": CLIENT, "exp": NOW + 600, "nonce": NONCE, "sub": "1"}).encode())
    assert verifier.verify("google", f"{head}.{body}.", NONCE) is None


@pytest.mark.parametrize("junk", ["", "a.b", "a.b.c.d", "not a token", "....", "e30.e30.e30", "!!!.!!!.!!!"])
def test_junk_is_refused_without_an_error(verifier, junk):
    assert verifier.verify("google", junk, NONCE) is None


def test_a_token_for_a_provider_not_set_up_is_refused(key):
    only_apple = ProviderVerifier({"apple": "com.example.web"}, fetch=lambda url: _jwks(key), clock=lambda: NOW)
    assert only_apple.verify("google", _token(key), NONCE) is None and not only_apple.available("google")


def test_a_google_token_does_not_pass_as_an_apple_token(verifier, key):
    assert verifier.verify("apple", _token(key), NONCE) is None


def test_an_empty_nonce_never_matches(verifier, key):
    assert verifier.verify("google", _token(key, nonce=""), "") is None


def test_keys_are_cached_and_an_unknown_key_id_refetches_at_most_every_five_minutes(key):
    now = [NOW]
    calls = []

    def fetch(url):
        calls.append(url)
        return _jwks(key)

    v = ProviderVerifier({"google": CLIENT}, fetch=fetch, clock=lambda: now[0])
    assert v.verify("google", _token(key), NONCE)
    assert v.verify("google", _token(key), NONCE)
    assert len(calls) == 1
    assert v.verify("google", _token(key, kid="rotated"), NONCE) is None
    assert len(calls) == 1  # within five minutes of the last fetch
    now[0] += 301
    assert v.verify("google", _token(key, kid="rotated"), NONCE) is None
    assert len(calls) == 2


def test_a_failed_key_fetch_refuses_the_token_and_does_not_raise(key):
    def fetch(url):
        raise OSError("down")

    v = ProviderVerifier({"google": CLIENT}, fetch=fetch, clock=lambda: NOW)
    assert v.verify("google", _token(key), NONCE) is None


def test_keys_already_held_still_work_when_a_refetch_fails(key):
    now = [NOW]
    state = {"fail": False}

    def fetch(url):
        if state["fail"]:
            raise OSError("down")
        return _jwks(key)

    v = ProviderVerifier({"google": CLIENT}, fetch=fetch, clock=lambda: now[0])
    assert v.verify("google", _token(key, exp=NOW + 10_000), NONCE)
    state["fail"] = True
    now[0] += 400
    assert v.verify("google", _token(key, exp=NOW + 10_000), NONCE)


def test_key_sets_are_fetched_over_https_only():
    from engine.api.provider_tokens import fetch_keys

    with pytest.raises(ValueError):
        fetch_keys("http://www.googleapis.com/oauth2/v3/certs")
