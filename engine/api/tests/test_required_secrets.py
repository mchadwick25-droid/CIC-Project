"""engine.api.required_secrets: one list of what each switch needs, checked
all at once at start-up and against render.yaml itself."""
import pytest

from engine.api import app as app_module
from engine.api import required_secrets as rs
from engine.api.config import REPO_ROOT

KEY = "k" * 32
RENDER_YAML = REPO_ROOT / "render.yaml"


def test_every_missing_secret_is_named_at_once():
    env = {"CIC_API_ANON_CAP_ENABLED": "1", "CIC_DEEPER_ENABLED": "1"}
    with pytest.raises(rs.MissingSecrets) as caught:
        rs.check(env)
    assert [p.name for p in caught.value.problems] == [
        "CIC_API_ANON_VISITOR_SECRET", "CIC_DEEPER_WEBHOOK_SECRET", "CIC_DEEPER_FREE_KEY",
    ]
    assert "CIC_DEEPER_FREE_KEY" in str(caught.value) and "CIC_API_ANON_VISITOR_SECRET" in str(caught.value)


def test_a_complete_environment_passes():
    rs.check({
        "CIC_API_ANON_CAP_ENABLED": "1", "CIC_API_ANON_VISITOR_SECRET": "s",
        "CIC_DEEPER_ENABLED": "1", "CIC_DEEPER_WEBHOOK_SECRET": "w", "CIC_DEEPER_FREE_KEY": KEY,
        "CIC_API_ADMIN_TOKEN": KEY,
    })


def test_switches_that_are_off_need_nothing():
    rs.check({"CIC_DEEPER_ENABLED": "on", "CIC_API_ANON_CAP_ENABLED": "0"})


@pytest.mark.parametrize(
    ("env", "name"),
    [
        ({"CIC_DEEPER_ENABLED": "1", "CIC_DEEPER_WEBHOOK_SECRET": "w", "CIC_DEEPER_FREE_KEY": KEY}, "CIC_API_ANON_CAP_ENABLED"),
        ({"CIC_DEEPER_ENABLED": "yes", "CIC_DEEPER_WEBHOOK_SECRET": "w", "CIC_DEEPER_FREE_KEY": "short",
          "CIC_API_ANON_CAP_ENABLED": "1", "CIC_API_ANON_VISITOR_SECRET": "s"}, "CIC_DEEPER_FREE_KEY"),
        ({"CIC_API_ADMIN_TOKEN": "short"}, "CIC_API_ADMIN_TOKEN"),
    ],
)
def test_each_refusal_the_components_raise_is_in_the_list(env, name):
    assert [p.name for p in rs.problems_in(env)] == [name]


@pytest.mark.parametrize("service", ["cic-engine", "cic-engine-staging"])
def test_render_yaml_declares_what_every_switch_it_turns_on_needs(service):
    assert rs.declared_gaps(rs.service_env(RENDER_YAML, service)) == []


def test_a_switch_turned_on_without_its_secret_declared_is_caught():
    env_vars = [{"key": "CIC_DEEPER_ENABLED", "value": "1"}, {"key": "CIC_DEEPER_FREE_KEY", "sync": False}]
    assert [g.name for g in rs.declared_gaps(env_vars)] == ["CIC_DEEPER_WEBHOOK_SECRET", "CIC_API_ANON_CAP_ENABLED"]


def test_checklist_splits_needed_from_other_hand_set_values():
    env_vars = [
        {"key": "CIC_API_ANON_CAP_ENABLED", "value": "1"},
        {"key": "CIC_API_ANON_VISITOR_SECRET", "sync": False},
        {"key": "CIC_API_BACKUP_BUCKET", "sync": False},
    ]
    assert rs.checklist(env_vars) == (["CIC_API_ANON_VISITOR_SECRET"], ["CIC_API_BACKUP_BUCKET"])
    assert rs.checklist([{"key": "AWS_ACCESS_KEY_ID", "sync": False}]) == (["AWS_ACCESS_KEY_ID"], [])


def test_cli_prints_the_checklist_for_a_service(capsys):
    assert rs._cli(["--service", "cic-engine", "--render-yaml", str(RENDER_YAML)]) == 0
    out = capsys.readouterr().out
    needed, other = out.split("Other hand-set values")
    assert "[ ] CIC_API_ANON_VISITOR_SECRET" in needed and "[ ] AWS_ACCESS_KEY_ID" in needed
    assert "[ ] CIC_API_BACKUP_BUCKET" in other


def test_production_start_up_checks_before_anything_else(monkeypatch):
    monkeypatch.setattr(app_module.os, "environ", {"CIC_API_REGION": "us-east-1", "CIC_DEEPER_ENABLED": "1"})
    with pytest.raises(rs.MissingSecrets):
        app_module._build_real_app()
