"""Every setting `Settings.from_env` parses is handed to the app by
`_build_real_app`. A parsed setting the app never reads makes the deploy
file's value for it do nothing, silently."""
import ast
import dataclasses
import inspect
from pathlib import Path

from engine.api import app as app_module
from engine.api.config import Settings

# Parsed but not yet read by any code path. Each entry names why; an entry
# that becomes read fails the stale check below and is removed.
KNOWN_UNREAD: dict[str, str] = {}


def _build_real_app_node() -> ast.FunctionDef:
    tree = ast.parse(Path(app_module.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "_build_real_app":
            return node
    raise AssertionError("_build_real_app not found in engine/api/app.py")


def _settings_attributes_read(node: ast.FunctionDef) -> set[str]:
    return {
        n.attr
        for n in ast.walk(node)
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "settings"
    }


def _settings_fields() -> set[str]:
    return {f.name for f in dataclasses.fields(Settings)}


def test_every_parsed_setting_is_read_by_the_app():
    unread = _settings_fields() - _settings_attributes_read(_build_real_app_node()) - set(KNOWN_UNREAD)
    assert not unread, f"parsed in Settings but never read by _build_real_app: {sorted(unread)}"


def test_known_unread_settings_are_still_unread():
    stale = set(KNOWN_UNREAD) & _settings_attributes_read(_build_real_app_node())
    assert not stale, f"now read by _build_real_app, remove from KNOWN_UNREAD: {sorted(stale)}"


def test_known_unread_names_are_real_settings():
    assert set(KNOWN_UNREAD) <= _settings_fields()


def test_settings_passed_to_create_app_land_on_a_real_parameter():
    params = set(inspect.signature(app_module.create_app).parameters)
    for call in ast.walk(_build_real_app_node()):
        if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == "create_app"):
            continue
        for kw in call.keywords:
            assert kw.arg in params, f"create_app has no parameter {kw.arg!r}"


def test_self_revision_setting_reaches_create_app():
    for call in ast.walk(_build_real_app_node()):
        if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == "create_app":
            passed = {
                kw.arg: kw.value.attr
                for kw in call.keywords
                if isinstance(kw.value, ast.Attribute) and isinstance(kw.value.value, ast.Name)
                and kw.value.value.id == "settings"
            }
            assert passed.get("self_revision_enabled") == "self_revision_enabled"
            return
    raise AssertionError("_build_real_app never calls create_app")
