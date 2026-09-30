from engine.m10.rounds import ROUTE_MESSAGE, check_rounds, review_files

from .fixture_world import write


def _world(tmp_path, names):
    for n in names:
        write(tmp_path, f"Build/worlds/w/{n}", "x")
    return tmp_path


def test_counts_each_naming_convention(tmp_path):
    root = _world(tmp_path, [
        "Doc_03_Review_Round1.md",
        "w_Doc03_Review_Round2.md",
        "w_Doc03_SpotCheck_Round3.md",
        "Doc_04_Review_Round1.md",
        "Doc_030_Review_Round1.md",
        "Doc03_Correction_Verification_Round2_2026-09-16.md",
    ])
    assert sorted(review_files("w", 3, root)) == [1, 2, 3]
    assert sorted(review_files("w", 4, root)) == [1]


def test_round_first_naming_and_review_artifacts_dir(tmp_path):
    write(tmp_path, "Build/worlds/w/Review-Artifacts/Doc02_Round1_Review.md", "x")
    write(tmp_path, "Build/worlds/w/Doc_02_Review_Round1.md", "x")
    write(tmp_path, "Build/worlds/w/Review-Artifacts/Doc02_Round2_Review.md", "x")
    assert sorted(review_files("w", 2, tmp_path)) == [1, 2]


def test_step_zero_files(tmp_path):
    root = _world(tmp_path, ["Step0_Movement_Scope_Confirmation_Review_Round1.md", "Step0_Review_Round2.md"])
    assert sorted(review_files("w", 0, root)) == [1, 2]


def test_three_rounds_pass(tmp_path):
    root = _world(tmp_path, [f"Doc_05_Review_Round{i}.md" for i in (1, 2, 3)])
    findings, count = check_rounds("w", 5, root)
    assert findings == [] and count == 3


def test_fourth_round_file_routes_to_project_lead(tmp_path):
    root = _world(tmp_path, [f"Doc_05_Review_Round{i}.md" for i in (1, 2, 3, 4)])
    findings, count = check_rounds("w", 5, root)
    assert count == 4
    assert findings and ROUTE_MESSAGE in findings[0].reason


def test_check_new_blocks_the_fourth_file_before_it_is_written(tmp_path):
    root = _world(tmp_path, [f"Doc_05_Review_Round{i}.md" for i in (1, 2, 3)])
    findings, _ = check_rounds("w", 5, root, check_new=True)
    assert findings and ROUTE_MESSAGE in findings[0].reason


def test_check_new_allows_the_third_file_and_rewriting_an_existing_one(tmp_path):
    root = _world(tmp_path, ["Doc_05_Review_Round1.md", "Doc_05_Review_Round2.md"])
    assert check_rounds("w", 5, root, check_new=True, new_round=3)[0] == []
    full = _world(tmp_path, ["Doc_05_Review_Round3.md"])
    assert check_rounds("w", 5, full, check_new=True, new_round=3)[0] == []


def test_check_new_blocks_an_explicit_fourth_round(tmp_path):
    root = _world(tmp_path, ["Doc_05_Review_Round1.md"])
    findings, _ = check_rounds("w", 5, root, check_new=True, new_round=4)
    assert findings and ROUTE_MESSAGE in findings[0].reason


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
    assert sorted(review_files("w", 1, root)) == [1, 2, 3, 4, 5, 6]


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
