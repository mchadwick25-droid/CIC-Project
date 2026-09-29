from engine.m10.reviewfile import HEADER_FIELDS, SIMULATED_REVIEW_LABEL, check_review_file

from .fixture_world import review_text, write


def _check(tmp_path, text, name="Doc_01_Review_Round1.md"):
    path = write(tmp_path, name, text)
    return check_review_file(path, tmp_path)


def _ids(findings):
    return {f.check for f in findings}


def test_valid_file_passes(tmp_path):
    assert _check(tmp_path, review_text()) == []


def test_ascii_dash_and_missing_period_still_read_as_the_label(tmp_path):
    text = review_text().replace(SIMULATED_REVIEW_LABEL, "Simulated review - informational only, not an Article 31 substitute", 1)
    assert _check(tmp_path, text) == []


def test_label_must_be_first_line(tmp_path):
    assert "reviewfile-label" in _ids(_check(tmp_path, "# Review\n" + review_text()))


def test_missing_label(tmp_path):
    text = review_text().replace(SIMULATED_REVIEW_LABEL, "Independent review")
    assert "reviewfile-label" in _ids(_check(tmp_path, text))


def test_each_field_is_required(tmp_path):
    for name in HEADER_FIELDS:
        text = "\n".join(line for line in review_text().splitlines() if not line.startswith(name + ":"))
        findings = _check(tmp_path, text)
        assert any(name in f.reason for f in findings), name


def test_reviewer_must_be_opus_5_5(tmp_path):
    text = review_text().replace("Reviewer model: claude-opus-5-5", "Reviewer model: claude-sonnet-5-5")
    assert "reviewfile-reviewer" in _ids(_check(tmp_path, text))


def test_reviewer_and_drafter_must_differ(tmp_path):
    text = review_text().replace("Drafter model: claude-sonnet-5-5", "Drafter model: claude-opus-5-5")
    assert "reviewfile-independence" in _ids(_check(tmp_path, text))


def test_truncation_methods_must_be_two_and_independent(tmp_path):
    same = review_text().replace("section count against the table of contents", "final line of every section read")
    assert "reviewfile-truncation" in _ids(_check(tmp_path, same))
    blank = review_text().replace("Truncation check, method 2: section count against the table of contents", "Truncation check, method 2:")
    assert "reviewfile-field" in _ids(_check(tmp_path, blank))


def test_round_must_be_a_number_and_match_the_file_name(tmp_path):
    assert "reviewfile-round" in _ids(_check(tmp_path, review_text().replace("Round: 1", "Round: first")))
    assert "reviewfile-round" in _ids(_check(tmp_path, review_text(2), name="Doc_01_Review_Round1.md"))


def test_bold_field_names_are_accepted(tmp_path):
    text = review_text().replace("Reviewer model:", "**Reviewer model:**")
    assert _check(tmp_path, text) == []


def test_missing_file(tmp_path):
    assert _ids(check_review_file(tmp_path / "nope.md", tmp_path)) == {"reviewfile-exists"}
