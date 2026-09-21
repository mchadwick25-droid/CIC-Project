"""engine/api/config.py's admin-token entropy floor (2026-09-21, closing
adversarial review of Tech-Readiness P1-Security). Settings.from_env
reads os.environ directly, so these tests monkeypatch it rather than
build a full Settings object by hand."""
import pytest

from engine.api.config import Settings, WeakAdminTokenError


def _env(monkeypatch, **overrides):
    monkeypatch.setenv("CIC_API_REGION", "us-east-1")
    for key, value in overrides.items():
        monkeypatch.setenv(key, value)


def test_no_admin_token_set_is_fine(monkeypatch):
    _env(monkeypatch)
    monkeypatch.delenv("CIC_API_ADMIN_TOKEN", raising=False)
    settings = Settings.from_env()
    assert settings.admin_token is None


def test_a_short_admin_token_is_refused_loudly(monkeypatch):
    _env(monkeypatch, CIC_API_ADMIN_TOKEN="too-short")
    with pytest.raises(WeakAdminTokenError):
        Settings.from_env()


def test_a_long_enough_admin_token_is_accepted(monkeypatch):
    token = "a" * 32
    _env(monkeypatch, CIC_API_ADMIN_TOKEN=token)
    settings = Settings.from_env()
    assert settings.admin_token == token
