"""engine/api/config.py's admin-token entropy floor. Settings.from_env
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


# self_revision_enabled's own kill-switch - default ON, the opposite
# sense from CIC_R27_ENFORCE (default off) above, since self-revision
# ships as generation, not staged enforcement.
def test_self_revision_defaults_on_when_the_env_var_is_unset(monkeypatch):
    _env(monkeypatch)
    monkeypatch.delenv("CIC_SELF_REVISION", raising=False)
    assert Settings.from_env().self_revision_enabled is True


@pytest.mark.parametrize("value", ["0", "false", "no"])
def test_self_revision_kill_switch_turns_it_off(monkeypatch, value):
    _env(monkeypatch, CIC_SELF_REVISION=value)
    assert Settings.from_env().self_revision_enabled is False


def test_self_revision_any_other_value_leaves_it_on(monkeypatch):
    _env(monkeypatch, CIC_SELF_REVISION="1")
    assert Settings.from_env().self_revision_enabled is True


# streaming_enabled's own flag - default off, same staging discipline as
# CIC_R27_ENFORCE above, not self-revision's default-on kill-switch shape.
def test_streaming_defaults_off_when_the_env_var_is_unset(monkeypatch):
    _env(monkeypatch)
    monkeypatch.delenv("CIC_API_STREAMING", raising=False)
    assert Settings.from_env().streaming_enabled is False


@pytest.mark.parametrize("value", ["1", "true", "yes"])
def test_streaming_truthy_values_turn_it_on(monkeypatch, value):
    _env(monkeypatch, CIC_API_STREAMING=value)
    assert Settings.from_env().streaming_enabled is True


@pytest.mark.parametrize("value", ["0", "false", "no", "on", ""])
def test_streaming_any_other_value_leaves_it_off(monkeypatch, value):
    _env(monkeypatch, CIC_API_STREAMING=value)
    assert Settings.from_env().streaming_enabled is False
