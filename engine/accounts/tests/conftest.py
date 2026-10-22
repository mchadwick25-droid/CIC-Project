import pytest

from engine.accounts.keys import KeyRing
from engine.accounts.service import AccountsService, Limits
from engine.accounts.store import AccountStore

ADDRESS_KEY = "a" * 40
SESSION_KEY = "s" * 40
START = 1_790_000_000


class FakeMailer:
    def __init__(self):
        self.sent: list[tuple[str, str]] = []
        self.fail = False

    def send_code(self, address: str, code: str) -> None:
        if self.fail:
            raise RuntimeError("provider down")
        self.sent.append((address, code))

    def last_code(self, address: str) -> str:
        return [c for a, c in self.sent if a == address][-1]


class FakeVerifier:
    """A token is "<subject>|<nonce>"; one for another nonce, or one with no subject, is refused."""

    def __init__(self, available=("google", "apple")):
        self._available = available

    def available(self, provider):
        return provider in self._available

    def verify(self, provider, id_token, nonce):
        subject, _, given = id_token.rpartition("|")
        if not subject or given != nonce:
            return None
        return (f"https://{provider}.example", subject)


class Clock:
    def __init__(self, now=START):
        self.t = now

    def __call__(self):
        return self.t

    def advance(self, seconds):
        self.t += seconds


@pytest.fixture
def clock():
    return Clock()


@pytest.fixture
def mailer():
    return FakeMailer()


@pytest.fixture
def store(tmp_path):
    s = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    yield s
    s.close()


@pytest.fixture
def keys():
    return KeyRing(ADDRESS_KEY, SESSION_KEY)


@pytest.fixture
def svc(store, keys, mailer, clock):
    return AccountsService(store, keys, mailer, clock=clock, verifier=FakeVerifier())


def start_sign_in(svc, mailer, address="ada@example.org", network="203.0.113.5"):
    result = svc.start_sign_in(address, network)
    assert result.status == "sent", result.status
    return result.challenge, mailer.last_code(address.strip().lower())


def sign_in(svc, mailer, address="ada@example.org", network="203.0.113.5"):
    challenge, code = start_sign_in(svc, mailer, address, network)
    result = svc.finish_sign_in(challenge, address, code, network, True)
    assert result.status == "ok", result.status
    return result.cookie


def stepped_up_session(svc, mailer, clock, address="ada@example.org", network="203.0.113.5"):
    cookie = sign_in(svc, mailer, address, network)
    session = svc.session(cookie)
    started = svc.step_up_start(session, address, network)
    assert started.status == "sent"
    assert svc.step_up_finish(session, started.challenge, mailer.last_code(address), network).status == "ok"
    return svc.session(cookie), cookie


def provider_sign_in(svc, provider="google", subject="g-ada", network="203.0.113.5", over_18=True):
    nonce = svc.provider_start(network).challenge
    result = svc.provider_sign_in(provider, f"{subject}|{nonce}", nonce, network, over_18)
    assert result.status == "ok", result.status
    return result.cookie


def provider_token(svc, subject, network="203.0.113.5"):
    nonce = svc.provider_start(network).challenge
    return f"{subject}|{nonce}", nonce
