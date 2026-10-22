"""The module imports the standard library and itself, nothing else."""
import ast
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]


def _imports(path: Path, *, strict: bool = True):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Import):
            yield from (a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            if strict:
                assert node.level == 0, f"{path.name}: relative import"
            if node.module:
                yield node.module


def test_the_module_imports_only_the_standard_library_and_itself():
    sources = [p for p in PACKAGE.rglob("*.py") if "tests" not in p.relative_to(PACKAGE).parts]
    assert sources
    for path in sources:
        for module in _imports(path):
            root = module.split(".")[0]
            assert root in sys.stdlib_module_names or module == "engine.accounts" or module.startswith("engine.accounts."), (
                f"{path.name} imports {module}"
            )


def test_the_conversation_engine_and_the_meter_import_nothing_from_accounts():
    engine = PACKAGE.parent
    for sub in ("deeper", "m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10"):
        for path in (engine / sub).rglob("*.py"):
            if "tests" in path.parts:
                continue
            for module in _imports(path, strict=False):
                assert not module.startswith("engine.accounts"), f"{path} imports {module}"
