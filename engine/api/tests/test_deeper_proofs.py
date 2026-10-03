"""The standing proofs of the Go Deeper module. Each one fails the build.

The conversation engine never learns that money exists; the module never
learns about worlds, records, voices or quotes; and no join exists between the
conversation store, the meter and Stripe. A guard at the foot of this file
fails if any named proof is deleted, skipped or marked expected-to-fail."""
import ast
import re
import sqlite3
from pathlib import Path

import pytest

from engine.api.tests.test_deeper_seam import (  # noqa: F401
    RecordingClient,
    capped_app,
    code_with,
    open_session,
    runtime,
    say,
    small_free_cap,
)
from engine.deeper import codes

ENGINE = Path(__file__).resolve().parents[2]
EDGE_FILES = {"app.py", "deeper_routes.py", "deeper_admission.py"}
MONEY_WORDS = re.compile(r"\b(stripe|payment|meter|x-cic)\b", re.I)
ENGINE_CORE = [
    *(ENGINE / name for name in ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10", "provider", "canon")),
    ENGINE / "prose.py",
    ENGINE / "api" / "wiring.py",
    ENGINE / "api" / "table_wiring.py",
]
EDGE_MIDDLEWARE = [ENGINE / "api" / "anon_cap.py", ENGINE / "api" / "ratelimit.py"]


def _sources(roots):
    for root in roots:
        if root.is_file():
            yield root
        else:
            for path in sorted(root.rglob("*.py")):
                if "tests" not in path.relative_to(ENGINE).parts:
                    yield path


def _imports(path: Path):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Import):
            yield from (alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            yield ("." * node.level) + (node.module or "")


# ---- the two sentences, enforced as imports ---------------------------------

def test_the_conversation_engine_imports_nothing_from_the_module():
    offenders = []
    for path in _sources(ENGINE_CORE):
        for name in _imports(path):
            if name == "engine.deeper" or name.startswith(("engine.deeper.", "engine.api.deeper")):
                offenders.append(f"{path.relative_to(ENGINE)} imports {name}")
    assert not offenders, offenders


def test_only_the_api_edge_imports_the_module():
    importers = set()
    for path in _sources([ENGINE / "api"]):
        if any(n == "engine.deeper" or n.startswith(("engine.deeper.", "engine.api.deeper")) for n in _imports(path)):
            importers.add(path.name)
    assert importers <= EDGE_FILES, importers - EDGE_FILES


def test_the_edge_middleware_imports_nothing_from_the_module():
    for path in _sources(EDGE_MIDDLEWARE):
        for name in _imports(path):
            assert not (name == "engine.deeper" or name.startswith(("engine.deeper.", "engine.api.deeper"))), (path.name, name)


def test_the_engine_core_names_no_payment_service_or_balance_header():
    hits = []
    for path in _sources(ENGINE_CORE):
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if MONEY_WORDS.search(line):
                hits.append(f"{path.relative_to(ENGINE)}:{number}")
    assert not hits, hits


def test_the_module_imports_only_the_standard_library_and_itself():
    for path in _sources([ENGINE / "deeper"]):
        for name in _imports(path):
            root = name.split(".")[0]
            assert root in __import__("sys").stdlib_module_names or name == "engine.deeper" or name.startswith("engine.deeper."), (
                f"{path.name} imports {name}"
            )


def test_the_grant_types_know_only_numbers():
    tree = ast.parse((ENGINE / "m4" / "grants.py").read_text())
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)} | {n.arg for n in ast.walk(tree) if isinstance(n, ast.arg)}
    assert not names & {"code", "price", "balance", "payment", "stripe", "money"}


# ---- no join between the stores ----------------------------------------------

def _all_text(db_path: Path) -> str:
    """Every byte the database files hold: rows, free pages and the write-ahead log."""
    chunks = []
    for suffix in ("", "-wal", "-journal"):
        candidate = Path(str(db_path) + suffix)
        if candidate.exists():
            chunks.append(candidate.read_bytes().decode("latin-1"))
    return "\n".join(chunks)


def test_a_paid_sitting_leaves_no_trace_of_the_code_or_the_payment_in_the_conversation_stores(
    store, usage_store, world_loader, registry, runtime, tmp_path
):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client)
    payment_id = "pi_PAYMENT_ID_MARKER_8431"
    reference = "claim-reference-MARKER-9921"
    (code,) = runtime.meter.mint("single", 6, payment_id)
    runtime.claims.put(reference, [code])
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(5):
        assert say(http, session_id, auth, f"question {i}").status_code == 200
    assert runtime.meter.status(code).remaining == 6 - 3

    events_text = "".join(_all_text(tmp_path / name) for name in ("events.db", "usage.db"))
    assert "question 4" in events_text
    for secret in (code, codes.display(code), codes.hash_code(code), payment_id, reference, "X-Cic-Code", "x-cic-code"):
        assert secret not in events_text, secret
    for word in ("exchanges_total", "payment_id", "stripe"):
        assert word not in events_text.lower(), word


def test_the_meter_and_the_claim_file_hold_no_session_visitor_or_conversation_text(
    store, usage_store, world_loader, registry, runtime, tmp_path
):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client)
    code = code_with(runtime, 6)
    runtime.claims.put("claim-reference-MARKER-1102", [code])
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    session_code = auth["Authorization"].split()[1]
    visitor = http.cookies.get("cic_visitor") or ""
    sentence = "a very particular question about the sitting"
    for i in range(4):
        say(http, session_id, auth, f"{sentence} {i}")
    runtime.meter.close()
    runtime.claims.close()
    held = _all_text(tmp_path / "m.db") + _all_text(tmp_path / "c.db")
    assert held
    for forbidden in (session_id, session_code, sentence):
        assert forbidden not in held
    if visitor:
        assert visitor.split(".")[0] not in held


def test_no_event_in_a_paid_sitting_carries_a_money_field(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient())
    code = code_with(runtime, 6)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(5):
        say(http, session_id, auth, f"question {i}")
    events = store.read_events(session_id)
    assert events
    for event in events:
        text = repr(event.payload).lower()
        assert not re.search(r"remaining|exchanges_|payment|stripe|x-cic|\bpaid\b", text), (event.event_type, text[:200])


# ---- the guard ---------------------------------------------------------------

REQUIRED = {
    "engine/api/tests/test_deeper_seam.py": [
        "test_the_voice_request_is_identical_off_free_and_paid_at_a_turn_past_the_free_cap",
        "test_the_voice_request_is_identical_on_the_stream_path_past_the_free_cap",
        "test_the_voice_requests_are_identical_for_a_table_round_past_the_free_rounds",
        "test_a_safety_route_is_answered_at_every_limit",
        "test_an_ordinary_message_at_a_limit_gets_a_close_and_no_voice_call",
        "test_admission_is_decided_before_the_voice_and_never_during_it",
        "test_twenty_five_students_behind_one_address_all_get_through_on_a_group_code",
        "test_a_visitor_past_the_session_limit_gets_one_facilitator_only_sitting_a_day",
        "test_a_spent_code_does_not_lift_the_session_limit",
    ],
    "engine/api/tests/test_deeper_routes.py": [
        "test_flag_off_mounts_no_deeper_route",
        "test_a_bad_signature_is_400_and_mints_nothing",
        "test_a_replayed_webhook_is_idempotent",
        "test_no_code_reference_or_hash_reaches_the_logs",
        "test_pause_stops_the_next_admission_and_unpause_restores_it",
    ],
    "engine/deeper/tests/test_schema.py": [
        "test_meter_columns_name_nothing_personal_and_no_fine_time",
        "test_meter_tables_have_no_rowid",
        "test_meter_holds_no_time_finer_than_a_day",
        "test_the_meter_and_claim_files_share_no_column",
    ],
    "engine/deeper/tests/test_logs.py": ["test_no_full_code_reaches_a_log_line"],
    "engine/deeper/tests/test_imports.py": ["test_the_module_imports_only_the_standard_library_and_itself"],
    "engine/deeper/tests/test_meter.py": ["test_two_concurrent_reserves_on_one_exchange_admit_exactly_one"],
    "engine/api/tests/test_deeper_proofs.py": [
        "test_the_conversation_engine_imports_nothing_from_the_module",
        "test_only_the_api_edge_imports_the_module",
        "test_a_paid_sitting_leaves_no_trace_of_the_code_or_the_payment_in_the_conversation_stores",
        "test_the_meter_and_the_claim_file_hold_no_session_visitor_or_conversation_text",
    ],
}
REPO = Path(__file__).resolve().parents[3]


def _decorator_text(node) -> str:
    return " ".join(ast.unparse(d) for d in node.decorator_list)


def test_every_named_proof_exists_and_none_is_skipped_or_expected_to_fail():
    problems = []
    for relative, names in REQUIRED.items():
        tree = ast.parse((REPO / relative).read_text())
        functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
        module_text = (REPO / relative).read_text()
        if re.search(r"pytestmark\s*=.*(skip|xfail)", module_text):
            problems.append(f"{relative}: module-level skip or xfail")
        for name in names:
            node = functions.get(name)
            if node is None:
                problems.append(f"{relative}: {name} is missing")
                continue
            if re.search(r"skip|xfail", _decorator_text(node)):
                problems.append(f"{relative}: {name} is skipped or expected to fail")
            body = ast.unparse(node)
            if re.search(r"pytest\.(skip|xfail)\(|importorskip", body):
                problems.append(f"{relative}: {name} skips itself")
    assert not problems, problems
