"""tools/check_live_commentary.py on the Library (cic/texts/), Sandbox/, the
two public sites' reader text, the provenance shapes added with them, and
the narrow carve-outs for text a program or template writes out."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools import check_live_commentary as clc

HEADER = (
    "Title: A Work\n"
    "Creator: An Author\n"
    "Source: Internet Archive item x, supplied by Mark, 2026-09-05.\n"
    "{extra}"
    "\n---\n\n"
    "{body}"
)


def _scan(tmp_path: Path, rel: str, text: str, surface: str = "engine") -> list[clc.Hit]:
    path = tmp_path / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return clc.scan_file(tmp_path, path, surface)


@pytest.fixture
def site_repo(tmp_path, monkeypatch):
    (tmp_path / "records" / "ijc").mkdir(parents=True)
    (tmp_path / "records" / "worlds").mkdir(parents=True)
    census = {"movements": [{"id": "alexandria-catechetical"}, {"id": "donatism"}]}
    (tmp_path / "cic-website" / "data").mkdir(parents=True)
    (tmp_path / "cic-website" / "data" / "world-census.json").write_text(json.dumps(census), encoding="utf-8")
    monkeypatch.setattr(clc, "REPO", tmp_path)
    clc._SLUG_CACHE.clear()
    yield tmp_path
    clc._SLUG_CACHE.clear()


# --- Library -------------------------------------------------------------

def test_library_and_sandbox_are_surfaces():
    assert clc.surface_of(Path("cic/texts/REGISTRY.yaml")) == "cic-texts"
    assert clc.surface_of(Path("Sandbox/answering-library/index/card.py")) == "sandbox"


def test_a_clean_intake_header_is_clean_and_its_dates_are_data(tmp_path):
    text = HEADER.format(extra="Provenance note: header prepended; nothing altered.\n", body="")
    assert _scan(tmp_path, "cic/texts/a_work_x1900.txt", text) == []


def test_review_history_in_an_intake_header_is_flagged(tmp_path):
    extra = "Provenance note: Note (independent review, Round 18; extended, Round 19): spelling normalised.\n"
    hits = _scan(tmp_path, "cic/texts/a_work_x1900.txt", HEADER.format(extra=extra, body=""))
    assert [h.category for h in hits] == ["REWRITE"]
    assert hits[0].line == 4


def test_a_ruling_attribution_in_an_intake_header_is_flagged(tmp_path):
    extra = "Content note: SECOND WITNESS (Mark's OCR ruling, 2026-09-25): garbled OCR.\n"
    hits = _scan(tmp_path, "cic/texts/a_work_x1900.txt", HEADER.format(extra=extra, body=""))
    assert [h.category for h in hits] == ["REWRITE"]


def test_the_source_text_itself_is_never_scanned(tmp_path):
    body = "TODO is no word of ours. Per Mark the evangelist, in round 3 of the games, 2026-01-01.\n"
    assert _scan(tmp_path, "cic/texts/a_work_x1900.txt", HEADER.format(extra="", body=body)) == []


def test_the_older_boxed_header_ends_at_its_closing_rule(tmp_path):
    rule = "     " + "_" * 60 + "\n"
    text = rule + "\n  Title: A Work\n  Acquisition history: corrected at Round 2 Opus review\n" + rule + "\nper Mark in the body\n"
    hits = _scan(tmp_path, "cic/texts/a_work_x1900.txt", text)
    assert [(h.line, h.category) for h in hits] == [(4, "REWRITE")]


def test_registry_notes_are_protected_but_its_header_comments_are_scanned(tmp_path):
    text = (
        "# WHY IT MOVED HERE (Mark's sign-off).\n"
        "- filename: a_work_x1900.txt\n"
        "  supplied_by: Mark\n"
        "  notes: >-\n"
        "    corrected in Round 2 Opus review.\n"
        "- filename: b.txt\n"
        "  supplied_by: Mark\n"
    )
    hits = _scan(tmp_path, "cic/texts/REGISTRY.yaml", text)
    assert [(h.line, h.category) for h in hits] == [(1, "REWRITE"), (5, "PROTECTED")]


def test_generated_library_indexes_are_reported_at_their_source(tmp_path):
    hits = _scan(tmp_path, "cic/texts/README.md", "corrected in Round 2 Opus review\n")
    assert [h.category for h in hits] == ["PROTECTED"]


def test_intake_folder_is_not_a_live_surface():
    assert not clc._is_scannable(Path("cic/texts/_intake/a_work_x1900.txt"))
    assert clc._is_scannable(Path("cic/texts/a_work_x1900.txt"))
    assert not clc._is_scannable(Path("cic/texts/anf01.xml"))


# --- new provenance shapes -------------------------------------------------

@pytest.mark.parametrize("line", [
    "# The evidence lookup is #440's own fix.\n",
    "# proved live across two battery runs (#419, #420).\n",
    "# Representative identity (records/worlds.yaml, PR #13).\n",
    "# Derived from Doc_09. Critic Finding 5 implemented here.\n",
    "# exempt under the accounts change order.\n",
    "# Promoted from the prototype (claude/cic-design-assignment-ecoxh2).\n",
    "# see /root/.claude/plans/linear-popping-dawn.md\n",
    "# The Mark-approved resources text is reused verbatim.\n",
    "# re-confirmed by the project lead at this step.\n",
    "# correcting it is the project lead's own call, not this build thread's.\n",
    "# what an earlier version of this docstring got wrong.\n",
])
def test_provenance_shapes_are_flagged(tmp_path, line):
    hits = _scan(tmp_path, "engine/x.py", line)
    assert [h.category for h in hits] == ["REWRITE"], hits


@pytest.mark.parametrize("line", [
    "color: #333;\n",
    "Project Gutenberg eBook #6400.\n",
    "# The project lead assigns Frozen.\n",
    "# change the order of the probes.\n",
    "Source: supplied by Mark.\n",
])
def test_ordinary_text_does_not_match_the_new_shapes(tmp_path, line):
    hits = _scan(tmp_path, "engine/x.md", line)
    assert [h for h in hits if h.category in clc.BLOCKING_CATEGORIES] == [], hits


# --- the public sites --------------------------------------------------------

def test_a_record_id_in_site_reader_text_is_flagged(site_repo):
    line = '"how": "Leo stands behind ijc.force.leo-rejects-canon-28 here.",\n'
    hits = _scan(site_repo, "cft-website/index.html", line, "cft-website")
    assert [h.category for h in hits] == ["REWRITE"] and "record-slug" in hits[0].patterns


def test_a_census_id_in_site_reader_text_is_flagged(site_repo):
    line = "<p>It grew out of alexandria-catechetical teaching.</p>\n"
    hits = _scan(site_repo, "cft-website/tree/x.html", line, "cft-website")
    assert [h.category for h in hits] == ["REWRITE"]


@pytest.mark.parametrize("line", [
    '{"id": "alexandria-catechetical--desert-monasticism", "source_id": "ijc.source.ambrose-epistles"},\n',
    '<a href="tree/alexandria-catechetical.html" data-id="alexandria-catechetical">Alexandria</a>\n',
    '<audio src="audio/docstory-ijc.story.milan-edict.mp3"></audio>\n',
    "<p>Donatism was a schism in North Africa.</p>\n",
])
def test_ids_in_markup_and_data_plumbing_are_not_reader_text(site_repo, line):
    assert _scan(site_repo, "cft-website/index.html", line, "cft-website") == []


@pytest.mark.parametrize("phrase", [
    "whose record sits at", "that record never names", "the same province's church",
    "consulted via", "known to me, not consulted", "the census row ends here",
])
def test_story_card_builder_phrases_are_flagged_on_the_sites(site_repo, phrase):
    hits = _scan(site_repo, "cic-website/story.html", f'"how": "Cyprian, {phrase}, writes."\n', "cic-website")
    assert [h.category for h in hits] == ["REWRITE"]


def test_builder_phrases_are_only_a_site_rule(site_repo):
    assert _scan(site_repo, "engine/x.md", "the edition was consulted via a summary\n") == []


# --- text a program or a template writes out ---------------------------------

def test_a_todo_slot_in_program_output_is_not_a_note(tmp_path):
    text = 'out.append(\n    "    rights_basis: null   # TODO - verify against the host\\n"\n)\n'
    hits = _scan(tmp_path, "Build/worlds/_cross-world/helper.py", text, "worlds")
    assert [h.category for h in hits] == ["KEEP"]


def test_a_todo_comment_in_code_is_still_flagged(tmp_path):
    hits = _scan(tmp_path, "engine/x.py", "x = 1  # TODO: fix this later\n")
    assert [h.category for h in hits] == ["ROUTE"]


def test_a_todo_docstring_is_still_flagged(tmp_path):
    hits = _scan(tmp_path, "engine/x.py", 'def f():\n    """TODO: handle the empty case."""\n')
    assert [h.category for h in hits] == ["ROUTE"]


def test_template_section_names_and_placeholders_are_not_open_items(tmp_path):
    text = (
        "### 7. Open Items Carried Forward\n\n"
        "**Testing notes:**\n"
        "[What was tested. If testing has not yet been conducted,\n"
        "write PENDING.]\n\n"
        "This template has not yet been tested against a live build.\n"
    )
    hits = _scan(tmp_path, "Build/reference/L9-Templates/X_Template.md", text, "reference")
    assert [(h.line, h.category) for h in hits] == [(1, "KEEP"), (4, "KEEP"), (7, "ROUTE")]


def test_has_not_yet_been_needs_a_process_verb(tmp_path):
    assert _scan(tmp_path, "Build/worlds/w/x.md", "a person who has not yet been formed by it\n", "worlds") == []
    hits = _scan(tmp_path, "Build/worlds/w/x.md", "this edition has not yet been collated\n", "worlds")
    assert [h.category for h in hits] == ["ROUTE"]


def test_the_freeze_as_a_stage_name_is_not_narration(tmp_path):
    assert _scan(tmp_path, "engine/x.py", 'note = "identity, the freeze, the admission read"\n') == []
    hits = _scan(tmp_path, "engine/x.md", "This was corrected at the Freeze.\n")
    assert [h.category for h in hits] == ["REWRITE"]


@pytest.mark.parametrize("line", [
    '"toldWithin": "alexandria-catechetical",\n',
    '  "alexandria-catechetical": {\n',
    '.card[data-id="alexandria-catechetical"] .pic{background:#917752}\n',
])
def test_bare_identifier_values_and_stylesheets_are_not_reader_text(site_repo, line):
    rel = "cic-website/assets/chooser.css" if line.startswith(".card") else "cic-website/data/world-census.json"
    assert _scan(site_repo, rel, line, "cic-website") == []


def test_a_date_inside_a_one_name_code_span_or_a_fenced_command_is_a_name(tmp_path):
    text = "## `baseline/pilot-2026-08-24` — the voice to return to\n\n```\ngit checkout baseline/pilot-2026-08-24\n```\n"
    assert [h.category for h in _scan(tmp_path, "engine/BASELINES.md", text)] == ["KEEP"]
    hits = _scan(tmp_path, "engine/x.md", "Decided on 2026-08-24 in `the review`.\n")
    assert [h.category for h in hits] == ["REWRITE"]


def test_a_conversation_turn_is_not_the_build_thread(tmp_path):
    assert _scan(tmp_path, "engine/x.py", "# the figure ids a prior turn already bridged\n") == []


def test_a_dated_file_name_in_a_registry_note_does_not_hide_the_added_column(tmp_path):
    text = (
        "| # | Source | Note | Added |\n|---|---|---|---|\n"
        "| 30 | Wessel | Identified via `Archive/X/Critique_2026-07-06.md`'s own correction | 2026-07-20; 2026-08-05 (title confirmed) |\n"
        "| 31 | Pietri | Title confirmed 2026-08-05 in review | 2026-07-20 |\n"
    )
    hits = _scan(tmp_path, "Build/worlds/w/Source_Registry.md", text, "worlds")
    assert [(h.line, h.category) for h in hits] == [(3, "KEEP"), (4, "REWRITE")]


def test_a_boxed_header_longer_than_120_lines_is_still_scanned(tmp_path):
    rule = "     " + "_" * 60 + "\n"
    text = rule + "\n  Title: A Work\n" + "  Content note: plain.\n" * 130 + "  WHY: after an adversarial review found it\n" + rule + "body\n"
    hits = _scan(tmp_path, "cic/texts/a_work_x1900.txt", text)
    assert [h.category for h in hits] == ["REWRITE"] and hits[0].line == 134


def test_a_stale_not_yet_vendored_note_is_an_open_item(tmp_path):
    extra = "Content note: NOT YET VENDORED, flagged for a future round: the earlier article.\n"
    hits = _scan(tmp_path, "cic/texts/a_work_x1900.txt", HEADER.format(extra=extra, body=""))
    assert [h.category for h in hits] == ["ROUTE"]


def test_the_source_line_names_the_fetcher_and_the_intake_pr_but_no_other_line_does(tmp_path):
    extra = (
        "Source: fetched directly by this build thread, pushed to cic/texts/_intake/ (PR #1583).\n"
        "Provenance note: rewritten by this build thread after PR #1583's own review.\n"
    )
    hits = _scan(tmp_path, "cic/texts/a_work_x1900.txt", HEADER.format(extra=extra, body=""))
    assert [(h.line, h.category) for h in hits] == [(5, "REWRITE")]


def test_a_dated_repair_in_a_header_is_flagged(tmp_path):
    extra = "Provenance note: (Fixed 2026-09-03: the original header named the wrong item.)\n"
    hits = _scan(tmp_path, "cic/texts/a_work_x1900.txt", HEADER.format(extra=extra, body=""))
    assert [h.category for h in hits] == ["REWRITE"]


def test_ocr_and_the_evangelist_are_not_project_history(tmp_path):
    extra = (
        "Content note: The book headings are not caught by the OCR.\n"
        "Content note: Mark's own disputed shorter ending after 16:8 is preserved.\n"
    )
    assert _scan(tmp_path, "cic/texts/a_work_x1900.txt", HEADER.format(extra=extra, body="")) == []
    hits = _scan(tmp_path, "engine/x.md", "Mark's own standing rule applies here.\n")
    assert [h.category for h in hits] == ["REWRITE"]


def test_registry_data_fields_are_protected_and_a_cue_marks_only_its_own_line(tmp_path):
    text = (
        "- date_added: '2026-09-02'\n"
        "  filename: c.txt\n"
        "  supplied_by: Claude (Library thread, 2026-10-23)\n"
        "  apparatus:\n"
        "    - name: x\n"
        "      evidence: >-\n"
        "        checked against the file, 2026-09-02\n"
        "  rights: CORRECTION per Mark\n"
        "  title: A Work\n"
    )
    hits = _scan(tmp_path, "cic/texts/REGISTRY.yaml", text)
    assert {h.line: h.category for h in hits} == {1: "PROTECTED", 3: "PROTECTED", 7: "PROTECTED", 8: "REWRITE"}


def test_links_checkboxes_and_blank_lines_end_a_template_placeholder(tmp_path):
    text = (
        "See [the guide](guide.md) and [ ] tick.\n"
        "This template has not yet been tested.\n"
        "[An unclosed placeholder\n"
        "\n"
        "This template has not yet been tested.\n"
    )
    hits = _scan(tmp_path, "Build/reference/L9-Templates/X_Template.md", text, "reference")
    assert [(h.line, h.category) for h in hits] == [(2, "ROUTE"), (5, "ROUTE")]


def test_a_bare_date_in_backticks_is_still_a_date(tmp_path):
    hits = _scan(tmp_path, "engine/x.md", "Ruled on `2026-09-25` in session.\n")
    assert [h.category for h in hits] == ["REWRITE"]


def test_an_adverb_before_the_process_verb_is_still_an_open_item(tmp_path):
    hits = _scan(tmp_path, "Build/worlds/w/x.md", "This has not yet been comprehensively assessed.\n", "worlds")
    assert [h.category for h in hits] == ["ROUTE"]


# --- ACCEPTED_OPEN waivers -----------------------------------------------------

def test_a_waived_line_is_reported_and_never_blocks(site_repo):
    line = '"note": "Cyprian\'s letter, consulted via summaries only."\n'
    hits = _scan(site_repo, "cft-website/index.html", line, "cft-website")
    assert [h.category for h in hits] == ["WAIVED"]
    assert "waiver:story-source-notes" in hits[0].patterns


def test_a_waiver_is_narrow_to_its_file_and_field(site_repo):
    line = '"how": "Cyprian\'s letter, consulted via summaries only."\n'
    assert [h.category for h in _scan(site_repo, "cft-website/index.html", line, "cft-website")] == ["REWRITE"]
    note = '"note": "consulted via summaries only."\n'
    assert [h.category for h in _scan(site_repo, "cic-website/x.html", note, "cic-website")] == ["REWRITE"]


def test_a_waiver_that_matches_nothing_is_stale(site_repo):
    (site_repo / "cft-website").mkdir(exist_ok=True)
    (site_repo / "cft-website" / "index.html").write_text('"note": "consulted via summaries only."\n', encoding="utf-8")
    used = clc.Waiver("used", ("cft-website/index.html",), clc.re.compile(r'^\s*"note":'), "test")
    unused = clc.Waiver("unused", ("cft-website/index.html",), clc.re.compile(r'^\s*"never":'), "test")
    assert clc.stale_waivers(site_repo, (used, unused)) == [
        "ACCEPTED_OPEN waiver 'unused' matches no line any more: remove it (test)"
    ]


def test_every_registered_waiver_names_its_owner():
    for waiver in clc.ACCEPTED_OPEN:
        assert waiver.owner and ("Open-Gaps" in waiver.owner or "PR #" in waiver.owner)
