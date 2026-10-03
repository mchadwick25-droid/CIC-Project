"""The module imports the standard library and itself, nothing else: no
conversation engine, no world, record, voice or quote code."""
import ast
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]


def _imports(path: Path):
    tree = ast.parse(path.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            yield from (a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            assert node.level == 0, f"{path.name}: relative import"
            yield node.module


def test_the_module_imports_only_the_standard_library_and_itself():
    sources = [p for p in PACKAGE.rglob("*.py") if "tests" not in p.relative_to(PACKAGE).parts]
    assert sources
    for path in sources:
        for module in _imports(path):
            root = module.split(".")[0]
            assert root in sys.stdlib_module_names or module == "engine.deeper" or module.startswith("engine.deeper."), (
                f"{path.name} imports {module}"
            )
