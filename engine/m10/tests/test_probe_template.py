"""A filled-in copy of Probe_Result_Record_Template.md passes `probes` and `validation` as written."""
import re

import yaml

from engine.m10.common import REPO_ROOT
from engine.m10.deployed import check_probe_pins
from engine.m10.validation import run_validation

TEMPLATE = REPO_ROOT / "Build" / "reference" / "L4-Templates" / "Probe_Result_Record_Template.md"
PIN = "2026-09-29T00-00-00Z"
TRANSCRIPT = "Build/worlds/w/build/transcripts/t1.md"
CATEGORIES = ("Source-Awareness", "Anachronism", "Confidence-under-Thinness", "Self-Referential", "Scholarly-Framework", "Claim-Laundering and Decontextualization")


def _row(pid, category, result="PASS", handler="n/a", notes=""):
    return f"| {pid} | {category} | {result} | observed | {TRANSCRIPT} | {handler} | 4 | 4 | 4 | 4 | no | {notes} |\n"


def _rows():
    met = "voice-itself: met; authorship: met; tensions-held: met; no-steering: met"
    rows = "".join(_row(f"P-{i}", c) for i, c in enumerate(CATEGORIES, 1))
    rows += _row("RS-1", "Relational Safety", handler="facilitator") + _row("RS-2", "Relational Safety", handler="facilitator")
    rows += _row("DI-1", "Sustained Engagement", notes=met)
    return rows


def _world(tmp_path, filled):
    (tmp_path / "records" / "worlds").mkdir(parents=True)
    (tmp_path / "records" / "worlds" / "w.yaml").write_text(f"safety_adjacent: false\nstate: built\npackage:\n  location: packages/w/{PIN}\n")
    (tmp_path / "packages" / "w" / PIN).mkdir(parents=True)
    gravity = {"id": "w.gravity.g", "record_type": "gravity", "classification": "primary", "confidence": {"formation_confidence": "Documented"}}
    directory = tmp_path / "records" / "w" / "gravity"
    directory.mkdir(parents=True)
    (directory / "w.gravity.g.md").write_text("---\n" + yaml.safe_dump(gravity) + "---\nbody\n")
    transcript = tmp_path / TRANSCRIPT
    transcript.parent.mkdir(parents=True)
    transcript.write_text("A saved transcript.\n")
    result = tmp_path / "Build" / "worlds" / "w" / "build" / "w_Probe_Results.md"
    result.parent.mkdir(parents=True, exist_ok=True)
    result.write_text(filled)
    return tmp_path


def _fill(rows):
    text = TEMPLATE.read_text().replace("[world-code]", "w").replace("[pin]", PIN)
    assert text.rstrip().endswith("|---|---|---|---|---|---|---|---|---|---|---|---|"), "the Results table is the last block of the template"
    return text.rstrip("\n") + "\n" + rows


def test_a_filled_copy_of_the_template_passes_probes_and_validation_as_written(tmp_path):
    root = _world(tmp_path, _fill(_rows()))
    probes = check_probe_pins("w", root)
    assert probes.findings == [], [f.line() for f in probes.findings]
    reports, trigger = run_validation("w", root=root)
    assert [f.line() for r in reports for f in r.findings] == []
    assert trigger["verdict"] == "lean", trigger


def test_the_unfilled_template_has_no_blank_row_and_carries_no_example_pin():
    text = TEMPLATE.read_text()
    assert "| | | |" not in text
    assert not re.search(r"\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z", text)
