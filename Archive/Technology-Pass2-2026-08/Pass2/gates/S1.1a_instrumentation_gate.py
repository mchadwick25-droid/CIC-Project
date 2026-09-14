"""S1.1a gate — instrumentation completeness (blueprint S1.1a, checkpoint G).

Counts every `.invoke(` / `.stream(` call site under cic-poc/backend/app/ and
every `log_llm_usage(` call, pairs them by innermost enclosing function, and
fails unless every LLM call site's function carries exactly as many
log_llm_usage calls as it has call sites.

AST-based, so docstring/comment mentions of .invoke/.stream (mock_llm.py,
usage_logging.py) are invisible to it — no textual false positives.

Allowlist (receivers that are NOT LLM clients, each with its reason):
  - "graph": the compiled LangGraph object (`graph.invoke(initial_state)` in
    main.py) — a graph traversal, not an LLM API call; the LLM calls it
    triggers are the instrumented sites inside the node functions themselves.

Deterministic; re-runnable; exit 0 = gate green. Emits a markdown report on
stdout. Run from the repo root:
    python Archive/Technology-Pass2-2026-08/Pass2/gates/S1.1a_instrumentation_gate.py
"""
import ast
import sys
from pathlib import Path

# parents[0]=gates, [1]=Pass2, [2]=Technology, [3]=Ministry, [4]=repo root
APP_DIR = Path(__file__).resolve().parents[4] / "cic-poc" / "backend" / "app"
if not APP_DIR.is_dir():
    # A gate that scans nothing passes vacuously — refuse to run instead.
    sys.exit(f"FATAL: app directory not found at {APP_DIR}")
ALLOWLIST_RECEIVERS = {"graph"}


def enclosing_function(node, parents):
    n = parents.get(node)
    chain = []
    while n is not None:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            chain.append(n.name)
        n = parents.get(n)
    return ".".join(reversed(chain)) if chain else "<module>"


def scan(path: Path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    parents = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent
    sites, logs, allowlisted = [], [], []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Attribute) and func.attr in ("invoke", "stream"):
            receiver = ast.unparse(func.value)
            entry = (node.lineno, receiver, func.attr, enclosing_function(node, parents))
            if receiver in ALLOWLIST_RECEIVERS:
                allowlisted.append(entry)
            else:
                sites.append(entry)
        elif isinstance(func, ast.Name) and func.id == "log_llm_usage":
            logs.append((node.lineno, enclosing_function(node, parents)))
    return sites, logs, allowlisted


def main() -> int:
    all_rows, failures, allow_rows = [], [], []
    total_sites = total_logs = 0
    for path in sorted(APP_DIR.rglob("*.py")):
        rel = path.relative_to(APP_DIR.parents[2]).as_posix()
        sites, logs, allowlisted = scan(path)
        total_sites += len(sites)
        total_logs += len(logs)
        allow_rows += [(rel, *e) for e in allowlisted]
        by_fn_sites, by_fn_logs = {}, {}
        for line, recv, kind, fn in sites:
            by_fn_sites.setdefault(fn, []).append((line, recv, kind))
        for line, fn in logs:
            by_fn_logs.setdefault(fn, []).append(line)
        for fn, s in sorted(by_fn_sites.items()):
            nlogs = len(by_fn_logs.get(fn, []))
            status = "OK" if nlogs == len(s) else "UNINSTRUMENTED"
            if status != "OK":
                failures.append((rel, fn, len(s), nlogs))
            for line, recv, kind in s:
                all_rows.append((rel, line, f"{recv}.{kind}", fn, f"{nlogs}/{len(s)}", status))

    print("# S1.1a gate report — instrumentation completeness\n")
    print("| file | line | call | enclosing function | logs/sites | status |")
    print("|---|---|---|---|---|---|")
    for row in all_rows:
        print("| " + " | ".join(str(x) for x in row) + " |")
    print(f"\n**LLM call sites:** {len(all_rows)}  |  **log_llm_usage calls:** {total_logs}")
    print("\n**Allowlisted (non-LLM) `.invoke`/`.stream` sites:**")
    for rel, line, recv, kind, fn in allow_rows:
        print(f"- `{rel}:{line}` — `{recv}.{kind}` in `{fn}` (allowlisted receiver: not an LLM client)")
    if failures:
        print("\n## GATE: FAIL — uninstrumented call sites\n")
        for rel, fn, ns, nl in failures:
            print(f"- `{rel}` `{fn}`: {ns} site(s), {nl} log call(s)")
        return 1
    print("\n## GATE: PASS — 0 uninstrumented sites")
    return 0


if __name__ == "__main__":
    sys.exit(main())
