import subprocess
import sys

from engine.m10.rounds import DECISION_LOG, ROUTE_MESSAGE, check_rounds, counted_review_files, is_review_name, latest_review, review_files, round_number

from .fixture_world import write


def _world(tmp_path, names):
    for n in names:
        write(tmp_path, f"Build/worlds/w/{n}", "x")
    return tmp_path


def _names(root, doc):
    return [p.name for p in review_files("w", doc, root)]


def test_counts_each_naming_convention(tmp_path):
    root = _world(tmp_path, [
        "Doc_03_Review_Round1.md",
        "w_Doc03_Review_Round2.md",
        "w_Doc03_SpotCheck_Round3.md",
        "Doc_04_Review_Round1.md",
        "Doc_030_Review_Round1.md",
        "Doc03_Correction_Verification_Round2_2026-09-16.md",
    ])
    assert len(review_files("w", 3, root)) == 4
    assert _names(root, 4) == ["Doc_04_Review_Round1.md"]


def test_every_review_type_file_counts_not_distinct_round_numbers(tmp_path):
    root = _world(tmp_path, [
        "Doc_05_Review_Round1.md",
        "Doc_05_Recheck_Round1.md",
        "Doc_05_SpotCheck.md",
        "Doc_05_Independent_Check_2026-09-29.md",
    ])
    write(root, "Build/worlds/w/Review-Artifacts/Doc05_Round1_Review.md", "x")
    findings, count = check_rounds("w", 5, root)
    assert count == 5
    assert findings and ROUTE_MESSAGE in findings[0].reason and "5 review files" in findings[0].reason


def test_files_that_are_not_review_files_do_not_count():
    for name in ("Doc_05_Prereview_Notes.md", "Doc_05_TruncationCheck_Confirmation.md", "Doc_05_Revision_History.md", "Doc_05_Source_Ecology.md"):
        assert not is_review_name(name), name
    for name in ("Doc_05_Review.md", "Doc05_Round2_Review.md", "Doc_05_SpotCheck.md", "Doc_05_Recheck_Round2.md", "Doc_05_Independent_Check_2026-09-29.md"):
        assert is_review_name(name), name


def test_round_first_naming_and_review_artifacts_dir(tmp_path):
    write(tmp_path, "Build/worlds/w/Review-Artifacts/Doc02_Round1_Review.md", "x")
    write(tmp_path, "Build/worlds/w/Doc_02_Review_Round1.md", "x")
    write(tmp_path, "Build/worlds/w/Review-Artifacts/Doc02_Round2_Review.md", "x")
    assert len(review_files("w", 2, tmp_path)) == 3


def test_step_zero_files(tmp_path):
    root = _world(tmp_path, ["Step0_Movement_Scope_Confirmation_Review_Round1.md", "Step0_Review_Round2.md"])
    assert len(review_files("w", 0, root)) == 2


def test_three_files_pass_and_four_route_to_the_project_lead(tmp_path):
    root = _world(tmp_path, [f"Doc_05_Review_Round{i}.md" for i in (1, 2, 3)])
    assert check_rounds("w", 5, root) == ([], 3)
    write(root, "Build/worlds/w/Doc_05_Recheck.md", "x")
    findings, count = check_rounds("w", 5, root)
    assert count == 4 and findings and ROUTE_MESSAGE in findings[0].reason


def test_check_new_blocks_the_fourth_file_before_it_is_written(tmp_path):
    root = _world(tmp_path, [f"Doc_05_Review_Round{i}.md" for i in (1, 2, 3)])
    findings, _ = check_rounds("w", 5, root, check_new=True)
    assert findings and ROUTE_MESSAGE in findings[0].reason


def test_check_new_blocks_three_files_that_share_a_round_number(tmp_path):
    root = _world(tmp_path, ["Doc_05_Review_Round1.md", "Doc_05_Recheck_Round1.md", "Doc_05_SpotCheck_Round1.md"])
    findings, _ = check_rounds("w", 5, root, check_new=True)
    assert findings and ROUTE_MESSAGE in findings[0].reason


def test_check_new_allows_the_third_file(tmp_path):
    root = _world(tmp_path, ["Doc_05_Review_Round1.md", "Doc_05_Review_Round2.md"])
    assert check_rounds("w", 5, root, check_new=True)[0] == []


def test_no_reviews_yet(tmp_path):
    root = _world(tmp_path, ["Doc_05_Ecological_Reconstruction.md"])
    assert check_rounds("w", 5, root) == ([], 0)


TITLE = "The three-round cap counts from significant new material"
LOG = "Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md"


def _log(root, title=TITLE):
    write(root, LOG, f"# Library decision log\n\n## 2026-09-29 \u2014 {title}\n\n**Ruling.** x\n")


def _reset(root, name, round_no, field=None):
    from .fixture_world import review_text

    field = TITLE if field is None else field
    text = review_text(round_no).replace("Round:", f"Cycle reset: {field}\nRound:", 1)
    write(root, f"Build/worlds/w/{name}", text)


def _cleared(root, n):
    from .fixture_world import review_text

    write(root, f"Build/worlds/w/Doc_01_Round{n}_Review.md", review_text(n))


def _earned_world(tmp_path, upto=3):
    root = tmp_path
    _log(root)
    for n in range(1, upto + 1):
        _cleared(root, n)
    return root


def test_without_a_reset_field_the_cycle_starts_at_round_one(tmp_path):
    # syr Doc_01 case: only the second and third rounds exist; a fourth must still be blocked
    root = _world(tmp_path, ["Doc_01_Round2_Review.md", "Doc_01_Round3_Review.md"])
    assert check_rounds("w", 1, root, check_new=True, new_round=4)[0] != []
    assert check_rounds("w", 1, root)[1] == 2


def test_an_earned_reset_restarts_the_count_and_keeps_every_file(tmp_path):
    root = _earned_world(tmp_path)
    _reset(root, "Doc_01_Round4_Review.md", 4)
    for n in (5, 6):
        write(root, f"Build/worlds/w/Doc_01_Round{n}_Review.md", "x")
    findings, count = check_rounds("w", 1, root)
    assert findings == [] and count == 3
    assert sorted(round_number(p) for p in review_files("w", 1, root)) == [1, 2, 3, 4, 5, 6]


def test_cap_still_applies_inside_the_new_cycle(tmp_path):
    root = _earned_world(tmp_path)
    _reset(root, "Doc_01_Round4_Review.md", 4)
    for n in (5, 6, 7):
        write(root, f"Build/worlds/w/Doc_01_Round{n}_Review.md", "x")
    findings, count = check_rounds("w", 1, root)
    assert count == 4 and findings and ROUTE_MESSAGE in findings[0].reason


def test_latest_earned_reset_wins(tmp_path):
    root = _earned_world(tmp_path)
    _reset(root, "Doc_01_Round4_Review.md", 4)
    _cleared(root, 5)
    _cleared(root, 6)
    _reset(root, "Doc_01_Round7_Review.md", 7)
    for n in (8, 9):
        write(root, f"Build/worlds/w/Doc_01_Round{n}_Review.md", "x")
    assert check_rounds("w", 1, root)[1] == 3


def test_check_new_counts_inside_the_cycle(tmp_path):
    root = _earned_world(tmp_path)
    _reset(root, "Doc_01_Round4_Review.md", 4)
    assert check_rounds("w", 1, root, check_new=True, new_round=6)[0] == []
    assert check_rounds("w", 1, root, check_new=True, new_round=7)[0] != []


def _ignored(root, expected, count_=6):
    for n in (5, 6):
        write(root, f"Build/worlds/w/Doc_01_Round{n}_Review.md", "x")
    findings, count = check_rounds("w", 1, root)
    assert count == count_
    assert findings and ROUTE_MESSAGE in findings[0].reason and "not honoured" in findings[0].reason and expected in findings[0].reason


def test_a_placeholder_reset_is_ignored(tmp_path):
    root = _earned_world(tmp_path)
    _reset(root, "Doc_01_Round4_Review.md", 4, field="TBD")
    _ignored(root, "placeholder")


def test_a_reset_that_cites_no_existing_ruling_is_ignored(tmp_path):
    root = _earned_world(tmp_path)
    _reset(root, "Doc_01_Round4_Review.md", 4, field="the builder judged the new material significant")
    _ignored(root, "exact title")


def test_a_cited_title_missing_from_the_log_is_ignored(tmp_path):
    root = tmp_path
    for n in (1, 2, 3):
        _cleared(root, n)
    write(root, LOG, "# Library decision log\n")
    _reset(root, "Doc_01_Round4_Review.md", 4)
    _ignored(root, "exact title")


def test_a_reset_after_a_round_that_did_not_clear_is_ignored(tmp_path):
    from .fixture_world import review_text

    root = _earned_world(tmp_path)
    write(root, "Build/worlds/w/Doc_01_Round3_Review.md", review_text(3, cleared=False))
    _reset(root, "Doc_01_Round4_Review.md", 4)
    _ignored(root, "did not clear")


def test_a_reset_with_no_round_before_it_is_ignored(tmp_path):
    root = tmp_path
    _log(root)
    for n in (1, 2):
        _cleared(root, n)
    _reset(root, "Doc_01_Round4_Review.md", 4)
    _ignored(root, "did not clear", 5)


def test_a_ministry_decision_log_title_is_accepted(tmp_path):
    root = tmp_path
    for n in (1, 2, 3):
        _cleared(root, n)
    write(root, "Build/Ministry/Operations/Standing/Some_Decision_Log.md", "## 2026-09-30 \u2014 Reset after a merged candidate\n\nx\n")
    _reset(root, "Doc_01_Round4_Review.md", 4, field="Reset after a merged candidate")
    for n in (5, 6):
        write(root, f"Build/worlds/w/Doc_01_Round{n}_Review.md", "x")
    assert check_rounds("w", 1, root) == ([], 3)


def test_latest_review_is_the_highest_round_or_the_last_unnumbered_file(tmp_path):
    root = _world(tmp_path, ["Doc_05_Review_Round1.md", "Doc_05_Review_Round2.md", "Doc_05_Independent_Check.md"])
    assert latest_review(review_files("w", 5, root))[0] == "round 2"
    other = _world(tmp_path / "b", ["Doc_05_Independent_Check.md"])
    assert latest_review(review_files("w", 5, other))[0] == "Doc_05_Independent_Check.md"


def test_the_command_exits_nonzero_with_three_files_and_check_new(tmp_path):
    root = _world(tmp_path, [f"Doc_05_Review_Round{i}.md" for i in (1, 2, 3)])
    run = lambda *extra: subprocess.run([sys.executable, "-m", "engine.m10.cli", "roundcount", "w", "5", "--root", str(root), *extra], capture_output=True, text=True).returncode  # noqa: E731
    assert run() == 0
    assert run("--check-new") == 1


THREE = ["Doc_03_Review_Round1.md", "Doc_03_Recheck_Round2.md", "Doc_03_Recheck_Round3.md"]
FOURTH = "Doc_03_SpotCheck_Round4.md"


def _ruling(root, heading, body):
    write(root, DECISION_LOG, f"# Log\n\n## {heading}\n\n{body}\n\n## 2026-10-01 - Another entry\n\nNothing here.\n")


def test_a_review_named_in_a_cap_ruling_after_three_files_does_not_count(tmp_path):
    root = _world(tmp_path, [*THREE, FOURTH])
    _ruling(root, "2026-09-30 - Cap ruling: Doc_03", f"The project lead ordered `{FOURTH}` after the escalation.")
    assert [p.name for p in counted_review_files("w", 3, root)] == THREE
    findings, count = check_rounds("w", 3, root)
    assert count == 3 and findings == []
    assert len(review_files("w", 3, root)) == 4


def test_a_cap_ruling_never_excuses_a_file_inside_the_first_three(tmp_path):
    root = _world(tmp_path, THREE[:2] + [FOURTH])
    _ruling(root, "2026-09-30 - Cap ruling: Doc_03", f"Orders `{FOURTH}`.")
    assert len(counted_review_files("w", 3, root)) == 3


def test_only_the_files_a_ruling_names_are_excused(tmp_path):
    root = _world(tmp_path, [*THREE, FOURTH, "Doc_03_Recheck_Round5.md"])
    _ruling(root, "2026-09-30 - Cap ruling: Doc_03", f"Orders `{FOURTH}`.")
    findings, count = check_rounds("w", 3, root)
    assert count == 4 and findings and "4 review files" in findings[0].reason


def test_a_name_in_an_entry_that_is_not_a_cap_ruling_excuses_nothing(tmp_path):
    root = _world(tmp_path, [*THREE, FOURTH])
    _ruling(root, "2026-09-30 - Round notes", f"Mentions `{FOURTH}`.")
    assert len(counted_review_files("w", 3, root)) == 4


def test_a_name_after_the_ruling_entry_ends_is_not_covered(tmp_path):
    root = _world(tmp_path, [*THREE, FOURTH])
    write(root, DECISION_LOG, f"## 2026-09-30 - Cap ruling: Doc_03\n\nOrders a review.\n\n## Later\n\n`{FOURTH}` again.\n")
    assert len(counted_review_files("w", 3, root)) == 4


def test_a_cap_ruling_and_an_earned_cycle_reset_work_together(tmp_path):
    root = _earned_world(tmp_path)
    _reset(root, "Doc_01_Round4_Review.md", 4)
    for n in (5, 6, 7):
        write(root, f"Build/worlds/w/Doc_01_Round{n}_Review.md", "x")
    # Without a ruling the cycle holds four files and routes to the project lead.
    findings, count = check_rounds("w", 1, root)
    assert count == 4 and findings and ROUTE_MESSAGE in findings[0].reason
    # A Cap ruling that names the last file excuses it: three counted files of the cycle precede it.
    write(root, DECISION_LOG, "## 2026-09-30 - Cap ruling: Doc_01\n\nThe project lead ordered `Doc_01_Round7_Review.md`.\n")
    assert check_rounds("w", 1, root) == ([], 3)
    assert [p.name for p in counted_review_files("w", 1, root)] == ["Doc_01_Round4_Review.md", "Doc_01_Round5_Review.md", "Doc_01_Round6_Review.md"]
    # Every file, in every cycle, stays on record.
    assert len(review_files("w", 1, root)) == 7
    # The ruling covers only the file it names, and only once three counted files of the cycle precede it.
    write(root, DECISION_LOG, "## 2026-09-30 - Cap ruling: Doc_01\n\nThe project lead ordered `Doc_01_Round6_Review.md`.\n")
    findings, count = check_rounds("w", 1, root)
    assert count == 4 and findings and ROUTE_MESSAGE in findings[0].reason
