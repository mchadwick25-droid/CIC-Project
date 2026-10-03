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
EDGE_FILES = {"app.py", "deeper_routes.py", "deeper_admission.py", "deeper_ops.py"}
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


def test_the_engines_own_words_never_name_a_code():
    text = (ENGINE / "m4" / "facilitator_turns.py").read_text()
    assert not re.search(r"\bcodes?\b", text), "the Facilitator's text in the engine must not mention a code"


def test_the_grant_types_know_only_numbers():
    tree = ast.parse((ENGINE / "m4" / "grants.py").read_text())
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)} | {n.arg for n in ast.walk(tree) if isinstance(n, ast.arg)}
    assert not names & {"code", "price", "balance", "payment", "stripe", "money"}
    # the only words a grant carries are the ones the caller handed it
    assert {f.name for f in __import__("dataclasses").fields(__import__("engine.m4.grants", fromlist=["TurnGrant"]).TurnGrant)} == {
        "cap", "facilitator_only", "limit_text",
    }


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


def test_a_sitting_driven_to_its_last_exchange_stores_no_code_or_balance_wording(store, usage_store, world_loader, registry, runtime):
    from engine.api.tests.test_deeper_seam import FREE_CAP

    client = RecordingClient()
    free = capped_app(store, usage_store, world_loader, registry, runtime, client)
    free_id, free_auth = open_session(free)
    for i in range(FREE_CAP + 1):
        say(free, free_id, free_auth, f"question {i}")
    code = code_with(runtime, 2)
    paid_id, paid_auth = open_session(free, **{"X-Cic-Code": code})
    for i in range(FREE_CAP + 3):
        say(free, paid_id, paid_auth, f"question {i}")
    assert runtime.meter.status(code).remaining == 0

    def facilitator_texts(session_id):
        return [e.payload["text"] for e in store.read_events(session_id) if e.event_type == "facilitator_turn"]

    assert facilitator_texts(free_id) == facilitator_texts(paid_id), "a paid sitting's stored words differ from a free one's"
    for text in facilitator_texts(paid_id):
        assert not re.search(r"\b(codes?|exchanges?|balance|paused|payment|stripe)\b", text, re.I), text
    for event in store.read_events(paid_id):
        assert not re.search(r"remaining|exchanges_|payment|stripe|x-cic|\bpaid\b", repr(event.payload).lower()), event.event_type


# ---- the guard ---------------------------------------------------------------

REQUIRED = {
    "engine/api/tests/test_deeper_seam.py": [
        "test_the_voice_request_is_identical_off_free_and_paid_at_a_turn_past_the_free_cap",
        "test_the_voice_request_is_identical_on_the_stream_path_past_the_free_cap",
        "test_the_voice_requests_are_identical_for_a_table_round_past_the_free_rounds",
        "test_a_safety_route_is_answered_at_every_limit",
        "test_an_ordinary_message_at_a_limit_gets_a_pause_and_no_voice_call",
        "test_admission_is_decided_before_the_voice_and_never_during_it",
        "test_twenty_five_students_behind_one_address_all_get_through_on_a_group_code",
        "test_a_visitor_past_the_session_limit_gets_one_facilitator_only_sitting_a_day",
        "test_a_spent_code_does_not_lift_the_session_limit",
        "test_an_extra_sitting_opened_by_a_live_code_draws_down_from_its_first_turn",
        "test_the_stored_pause_is_the_same_words_for_a_free_sitting_and_a_paid_one_and_the_reason_is_never_stored",
        "test_a_code_entered_after_the_pause_continues_the_same_conversation",
    ],
    "engine/deeper/tests/test_tokens.py": [
        "test_a_solo_conversation_of_three_rounds_draws_110",
        "test_the_free_grant_is_three_solo_conversations_of_three_rounds",
        "test_the_packs_are_whole_numbers_of_those_conversations",
    ],
    "engine/api/tests/test_deeper_ops.py": [
        "test_the_token_rates_and_packs_are_the_ones_ruled_on_2026_10_03",
        "test_a_bad_token_section_is_refused",
        "test_a_malformed_file_is_refused",
        "test_the_stored_pause_names_no_code_and_no_money",
        "test_the_flag_on_refuses_to_start_on_a_bad_file",
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
        "test_a_sitting_driven_to_its_last_exchange_stores_no_code_or_balance_wording",
        "test_the_engines_own_words_never_name_a_code",
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
            asserts = any(
                isinstance(n, ast.Assert) or (isinstance(n, ast.Call) and re.search(r"raises$|^assert", ast.unparse(n.func).split(".")[-1]))
                for n in ast.walk(node)
            )
            if not asserts:
                problems.append(f"{relative}: {name} asserts nothing")
    assert not problems, problems


def test_no_collection_hook_or_ci_flag_drops_a_proof_from_outside_its_file():
    outside = [REPO / "engine/conftest.py", REPO / "engine/api/tests/conftest.py", REPO / "conftest.py", REPO / ".github/workflows/ci.yml"]
    problems = []
    for path in outside:
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if re.search(r"collect_ignore|pytest_collection_modifyitems|--deselect|--ignore|pytest[^#\n]* -k ", line):
                problems.append(f"{path.relative_to(REPO)}:{number}: {line.strip()}")
    assert not problems, problems
