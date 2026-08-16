#!/usr/bin/env python3
"""The gate that keeps the relational-safety transcript trim from touching
the conversation.

Rule: `build_public_transcript` may be narrowed by exactly one caller -
`classify_relational_safety` - and its default output must stay byte-identical
to the shared 2+10 window it has always produced.

WHY THIS GATE EXISTS
--------------------
`build_public_transcript` has six consumers, and five of them shape the
encounter itself:

    _prepare_representative_turn  -> conversation_context for lexicon and
                                     story retrieval (UNGATED - active in
                                     single-voice), and the Representative's
                                     view of the table in multi-world
    stream_facilitator_bridge     -> the Facilitator's bridge turn
    select_next_speaker           -> who speaks next in multi-voice
    classify_wind_down            -> closing detection
    stream_closing_turn           -> the closing turn
    classify_relational_safety    -> the safety classifier   <- the only one
                                                                that narrows

The cost saving lives entirely in the last one. Narrowing the shared
TRANSCRIPT_RECENT_WINDOW instead would change which lexicon entries and
stories are retrieved, and therefore what the Representative can draw on -
a conversation-quality change wearing a cost change's clothes.

The `recent_window=None` default makes that isolation structural: a call site
has to opt in to narrowing. This gate makes it *enforced* - it fails if a
second caller ever opts in, or if the default drifts.

Run: python cic/checks/transcript_window.py    (exit 0 = isolated)
"""
import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # cic/
RUNTIME = ROOT / "runtime"

# The one function permitted to narrow the window, and the value it may use.
PERMITTED_CALLER = "classify_relational_safety"
EXPECTED_NARROW_ARG = "RELATIONAL_SAFETY_RECENT_WINDOW"

# The shared window, pinned. The behavioural check below compares the render
# against a reimplementation that reads these same constants, so it cannot by
# itself notice the constants moving - pinning them here is what catches
# "narrow the shared window" being done directly.
EXPECTED_SHARED_PREFIX = 2
EXPECTED_SHARED_WINDOW = 10

# Files that call build_public_transcript. Listed rather than globbed so a new
# consumer in a new file is a deliberate edit here, not a silent addition.
CALLER_FILES = (
    RUNTIME / "app" / "graph" / "nodes.py",
    RUNTIME / "app" / "graph" / "closing_sequence.py",
)


def _enclosing_function(tree: ast.Module, node: ast.AST) -> str:
    """Name of the innermost function containing `node`, or '<module>'."""
    best, best_span = "<module>", None
    for candidate in ast.walk(tree):
        if not isinstance(candidate, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        start, end = candidate.lineno, getattr(candidate, "end_lineno", candidate.lineno)
        if start <= node.lineno <= end:
            span = end - start
            if best_span is None or span < best_span:
                best, best_span = candidate.name, span
    return best


def check_call_sites() -> list[str]:
    """Every build_public_transcript call, and who is allowed to narrow."""
    failures, narrowing, total = [], [], 0

    for path in CALLER_FILES:
        if not path.is_file():
            failures.append(f"{path.relative_to(ROOT)}: expected caller file is missing")
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", None)
            if name != "build_public_transcript":
                continue
            total += 1
            kwarg = next((k for k in node.keywords if k.arg == "recent_window"), None)
            # A positional third argument would narrow the window too.
            positional_narrow = len(node.args) >= 3
            if kwarg is None and not positional_narrow:
                continue

            where = _enclosing_function(tree, node)
            narrowing.append(where)
            loc = f"{path.relative_to(ROOT)}:{node.lineno} ({where})"

            if positional_narrow:
                failures.append(
                    f"{loc}: narrows the window positionally. Pass "
                    f"recent_window=... by keyword so the intent is greppable.")
            if where != PERMITTED_CALLER:
                failures.append(
                    f"{loc}: narrows the public-transcript window, but only "
                    f"{PERMITTED_CALLER} may. Five of the six consumers shape "
                    f"the conversation - narrowing one of those changes what "
                    f"the Representative can draw on. See this file's header.")
            elif kwarg is not None and getattr(kwarg.value, "id", None) != EXPECTED_NARROW_ARG:
                failures.append(
                    f"{loc}: narrows with something other than "
                    f"{EXPECTED_NARROW_ARG}. Keep the value in the named "
                    f"constant so it is documented in one place.")

    if total == 0:
        failures.append("found no build_public_transcript calls at all - this "
                        "gate is looking in the wrong files and is not "
                        "protecting anything.")
    if narrowing.count(PERMITTED_CALLER) == 0:
        failures.append(f"{PERMITTED_CALLER} no longer narrows the window. If "
                        "the trim was reverted, delete this gate too rather "
                        "than leaving it passing vacuously.")
    return failures


def check_default_unchanged() -> list[str]:
    """The default render must equal the shared 2+10 window, byte for byte.

    Compared against an independent reimplementation of the pre-change
    algorithm rather than a stored golden string, so this keeps testing the
    real behaviour if the render's formatting legitimately changes.
    """
    sys.path.insert(0, str(RUNTIME))
    from langchain_core.messages import AIMessage, HumanMessage

    from app.graph.nodes import (TRANSCRIPT_RECENT_WINDOW,
                                 TRANSCRIPT_STABLE_PREFIX,
                                 build_public_transcript)

    class _State:
        def __init__(self, messages):
            self.messages = messages

    def reference(lines: list[str]) -> str:
        """The windowing algorithm exactly as it stood before the parameter."""
        if len(lines) <= TRANSCRIPT_STABLE_PREFIX + TRANSCRIPT_RECENT_WINDOW:
            return "\n\n".join(lines)
        elided = len(lines) - TRANSCRIPT_STABLE_PREFIX - TRANSCRIPT_RECENT_WINDOW
        return "\n\n".join(
            lines[:TRANSCRIPT_STABLE_PREFIX]
            + [f"[... {elided} earlier turn(s) not shown ...]"]
            + lines[-TRANSCRIPT_RECENT_WINDOW:])

    failures = []
    if (TRANSCRIPT_STABLE_PREFIX, TRANSCRIPT_RECENT_WINDOW) != (
            EXPECTED_SHARED_PREFIX, EXPECTED_SHARED_WINDOW):
        failures.append(
            f"the SHARED window changed: TRANSCRIPT_STABLE_PREFIX="
            f"{TRANSCRIPT_STABLE_PREFIX} (expected {EXPECTED_SHARED_PREFIX}), "
            f"TRANSCRIPT_RECENT_WINDOW={TRANSCRIPT_RECENT_WINDOW} (expected "
            f"{EXPECTED_SHARED_WINDOW}). That window feeds lexicon and story "
            "retrieval, so changing it changes which sources the "
            "Representative can draw on - a conversation change, not a cost "
            "one. If it is genuinely intended, update the pins in this gate "
            "in the same commit so the decision is on the record.")
        return failures

    # 0 through 40 lines: covers empty, under the window, exactly at the
    # boundary, and well past it.
    for n in range(0, 41):
        messages, rendered = [], []
        for i in range(n):
            if i % 2 == 0:
                messages.append(HumanMessage(content=f"question {i}"))
                rendered.append(f"Participant: question {i}")
            else:
                messages.append(AIMessage(content=f"answer {i}", name="chloe"))
                rendered.append(f"Chloe: answer {i}")

        got = build_public_transcript(_State(messages))
        want = reference(rendered)
        if got != want:
            failures.append(
                f"default render changed at {n} line(s).\n"
                f"    expected: {want[:120]!r}\n"
                f"    got:      {got[:120]!r}")
            break

        # And the narrowed call must actually narrow, or the saving is fiction.
        if n > TRANSCRIPT_STABLE_PREFIX + TRANSCRIPT_RECENT_WINDOW:
            narrowed = build_public_transcript(_State(messages), recent_window=4)
            if len(narrowed) >= len(got):
                failures.append(
                    f"recent_window=4 did not shorten the render at {n} lines "
                    f"({len(narrowed)} >= {len(got)} chars) - the parameter is "
                    "not doing anything.")
                break
    return failures


def main() -> int:
    failures = check_call_sites() + check_default_unchanged()
    if failures:
        print("TRANSCRIPT WINDOW GATE: FAIL\n")
        for f in failures:
            print(f"  - {f}")
        print("\nThe public transcript feeds retrieval, the Representative's "
              "view of the table,\nspeaker selection, and the closing "
              "sequence. Only the safety classifier may\nsee less of it.")
        return 1
    print("TRANSCRIPT WINDOW GATE: PASS")
    print(f"  only {PERMITTED_CALLER} narrows the window")
    print("  default render byte-identical to the shared 2+10 window "
          "across 0-40 lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
