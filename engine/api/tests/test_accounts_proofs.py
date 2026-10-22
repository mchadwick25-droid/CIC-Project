"""The standing proofs of accounts. Each one fails the build.

A guard at the foot of this file fails if any named proof is deleted, skipped
or marked expected-to-fail."""
import ast
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ENGINE = REPO / "engine"

REQUIRED = {
    "engine/accounts/tests/test_imports.py": [
        "test_the_module_imports_only_the_standard_library_and_itself",
        "test_the_conversation_engine_and_the_meter_import_nothing_from_accounts",
    ],
    "engine/accounts/tests/test_schema.py": [
        "test_no_column_in_either_file_names_anything_personal",
        "test_the_durable_file_holds_no_time_finer_than_a_day",
        "test_a_file_made_before_recovery_was_removed_loses_its_recovery_tables",
        "test_the_account_files_hold_no_meter_code_hash_and_no_payment_id",
    ],
    "engine/accounts/tests/test_signin.py": [
        "test_a_code_works_once",
        "test_a_challenge_proves_only_the_address_and_kind_it_was_made_for",
        "test_a_code_dies_at_ten_minutes",
        "test_five_wrong_tries_burn_the_code_even_for_the_right_one",
        "test_start_reply_is_the_same_whether_or_not_an_account_exists",
        "test_a_no_to_the_age_click_gets_no_account_and_nothing_is_stored",
        "test_only_a_plain_yes_opens_an_account",
        "test_a_yes_opens_the_account_in_the_adult_band",
        "test_no_date_of_birth_is_asked_or_kept",
        "test_a_network_may_open_only_so_many_new_accounts_a_day",
    ],
    "engine/accounts/tests/test_providers.py": [
        "test_a_provider_sign_in_opens_an_account_with_no_address_on_file",
        "test_a_new_provider_id_is_asked_the_age_click_first_and_a_no_stores_nothing",
        "test_a_nonce_works_once",
        "test_a_token_for_another_nonce_or_a_made_up_nonce_is_refused",
        "test_a_provider_id_is_stored_only_as_a_keyed_hash",
        "test_the_email_a_provider_reports_is_never_read_or_kept",
        "test_a_matching_email_never_joins_an_address_account_to_a_provider_account",
        "test_linking_needs_a_step_up_and_clears_every_other_session",
        "test_a_provider_id_already_on_another_account_cannot_be_linked",
        "test_the_last_way_in_cannot_be_unlinked",
        "test_deleting_an_account_removes_its_provider_links",
        "test_a_provider_cannot_stand_in_for_the_address_code_on_an_account_that_has_an_address",
        "test_two_unlinks_at_once_cannot_leave_a_provider_only_account_with_no_way_in",
        "test_issuing_a_nonce_writes_nothing_and_many_networks_cannot_lock_sign_in_out",
        "test_a_forged_or_changed_nonce_is_refused",
        "test_a_file_made_when_every_account_had_an_address_is_rebuilt_with_the_address_optional",
    ],
    "engine/api/tests/test_provider_tokens.py": [
        "test_a_genuine_token_gives_the_issuer_and_subject",
        "test_a_token_with_a_wrong_claim_is_refused",
        "test_a_token_signed_by_another_key_is_refused",
        "test_only_rs256_is_accepted",
        "test_an_unsigned_token_is_refused",
    ],
    "engine/accounts/tests/test_contacts.py": [
        "test_the_account_file_still_holds_no_address",
        "test_deleting_an_account_deletes_its_contact",
        "test_a_restored_backup_does_not_bring_a_deleted_contact_back",
        "test_a_row_moved_to_another_account_does_not_open",
        "test_a_wrong_key_reads_nothing",
        "test_no_log_line_holds_the_kept_address",
    ],
    "engine/accounts/tests/test_recovery.py": [
        "test_a_recovery_waits_seven_days_tells_the_old_address_and_shows_a_banner",
        "test_after_seven_days_the_new_address_signs_in_to_the_same_account_and_old_sessions_end",
        "test_the_start_reply_is_the_same_for_a_right_and_a_wrong_recovery_code",
        "test_the_owner_cancels_with_the_code_in_the_notice_and_the_thief_s_new_recovery_code_dies",
        "test_cancelling_sends_no_mail_and_works_with_every_sending_limit_used_up",
        "test_a_recovery_moves_nothing_when_the_new_address_gets_an_account_during_the_wait",
        "test_deleting_an_account_removes_its_recovery_rows",
    ],
    "engine/api/tests/test_contact_cipher.py": [
        "test_a_sealed_address_opens_with_its_key_and_context_only",
        "test_the_contact_file_holds_no_address_in_the_clear",
        "test_a_deleted_contact_leaves_no_bytes",
    ],
    "engine/accounts/tests/test_concurrency.py": [
        "test_concurrent_wrong_guesses_cannot_beat_the_try_limit",
        "test_two_simultaneous_right_codes_open_exactly_one_session",
    ],
    "engine/accounts/tests/test_sessions.py": [
        "test_the_cookie_points_to_a_session_and_holds_no_account_value",
        "test_a_session_ends_at_the_absolute_limit_however_active",
        "test_sensitive_actions_need_a_fresh_step_up",
        "test_a_step_up_challenge_cannot_be_used_by_another_account",
    ],
    "engine/accounts/tests/test_address_change.py": [
        "test_an_address_change_needs_the_old_address_then_a_code_to_the_new_one",
        "test_the_replies_never_say_whether_an_address_has_an_account",
        "test_a_challenge_for_one_account_s_change_cannot_finish_another",
        "test_many_accounts_cannot_send_more_than_a_few_codes_to_one_inbox",
        "test_an_owner_can_always_prove_their_address_however_full_the_shared_budgets_are",
    ],
    "engine/accounts/tests/test_deletion.py": [
        "test_the_ledger_holds_a_hash_of_the_random_id_never_the_address",
        "test_a_restored_backup_does_not_bring_a_deleted_account_back",
        "test_neither_file_holds_an_address_after_a_hundred_sign_ins",
        "test_a_deleted_account_s_bytes_are_overwritten",
        "test_deleting_an_account_forgets_its_address_hash_in_the_ephemeral_file",
        "test_no_log_line_holds_an_address_or_a_code",
    ],
    "engine/api/tests/test_accounts_routes.py": [
        "test_flag_off_mounts_no_accounts_route",
        "test_every_post_needs_the_header_and_json_and_a_matching_origin",
        "test_start_up_refuses_with_no_key_a_short_key_or_no_mail",
        "test_no_log_line_holds_an_address_a_code_or_a_cookie",
        "test_address_change_replies_and_limits_are_the_same_for_a_taken_and_a_free_address",
        "test_a_queued_send_never_blocks_the_reply_and_logs_no_address",
    ],
    "engine/api/tests/test_accounts_proofs.py": [
        "test_only_the_api_edge_imports_the_accounts_module",
    ],
}


def _imports(path: Path):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Import):
            yield from (a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            yield node.module


def test_only_the_api_edge_imports_the_accounts_module():
    allowed = {ENGINE / "api" / "app.py", ENGINE / "api" / "accounts_routes.py"}
    outside = []
    for path in ENGINE.rglob("*.py"):
        relative = path.relative_to(ENGINE)
        if "tests" in relative.parts or relative.parts[0] == "accounts" or path in allowed:
            continue
        if any(m.startswith("engine.accounts") for m in _imports(path)):
            outside.append(str(relative))
    assert not outside, outside


def _decorator_text(node) -> str:
    return " ".join(ast.unparse(d) for d in node.decorator_list)


def test_every_named_proof_exists_and_none_is_skipped_or_expected_to_fail():
    problems = []
    for relative, names in REQUIRED.items():
        text = (REPO / relative).read_text()
        functions = {n.name: n for n in ast.walk(ast.parse(text)) if isinstance(n, ast.FunctionDef)}
        if re.search(r"pytestmark\s*=.*(skip|xfail)", text):
            problems.append(f"{relative}: module-level skip or xfail")
        for name in names:
            node = functions.get(name)
            if node is None:
                problems.append(f"{relative}: {name} is missing")
                continue
            if re.search(r"skip|xfail", _decorator_text(node)):
                problems.append(f"{relative}: {name} is skipped or expected to fail")
            if re.search(r"pytest\.(skip|xfail)\(|importorskip", ast.unparse(node)):
                problems.append(f"{relative}: {name} skips itself")
            asserts = any(
                isinstance(n, ast.Assert) or (isinstance(n, ast.Call) and ast.unparse(n.func).split(".")[-1] == "raises")
                for n in ast.walk(node)
            )
            if not asserts:
                problems.append(f"{relative}: {name} asserts nothing")
    assert not problems, problems


def test_no_collection_hook_or_ci_flag_drops_an_accounts_proof_from_outside_its_file():
    outside = [ENGINE / "conftest.py", ENGINE / "api" / "tests" / "conftest.py", REPO / "conftest.py", REPO / ".github/workflows/ci.yml"]
    problems = []
    for path in outside:
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if re.search(r"collect_ignore|pytest_collection_modifyitems|--deselect|--ignore|pytest[^#\n]* -k ", line):
                problems.append(f"{path.relative_to(REPO)}:{number}: {line.strip()}")
    assert not problems, problems
