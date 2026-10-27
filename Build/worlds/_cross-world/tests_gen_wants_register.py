"""Tests for gen_wants_register.classify(): each wording the generator reads
off a source record's own fields maps to one kind, and wording it does not
recognise stays `unclassified`.

    python -m pytest Build/worlds/_cross-world/tests_gen_wants_register.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import gen_wants_register as g  # noqa: E402

RESOLVED = "resolved (attested via a vendored source)"
NOT_HELD = "not a held text (nothing to acquire)"
PURCHASABLE = "purchasable (in copyright)"


def kind(edition="", rights="", channel=""):
    return g.classify({"edition": edition, "rights_status": rights, "discovery_channel": channel})


def test_in_copyright_rights_wording_is_purchasable():
    assert kind("In-copyright modern scholarship, not vendored",
                "in-copyright modern scholarship or translation; deliberately excluded") == PURCHASABLE


def test_not_in_copyright_is_not_purchasable():
    assert kind("", "not in copyright; unrelated") == "unclassified"


def test_no_single_text_identified_is_not_a_held_text():
    assert kind("General regional history, no specific text acquired or identified",
                "not applicable - no single specific text has been identified for this row") == NOT_HELD


def test_no_single_text_identified_with_an_edition_wanted_stays_unclassified():
    assert kind("No open English edition of his works as a corpus has been located",
                "not applicable - no single specific text has been identified for this row") == "unclassified"


def test_attested_via_a_vendored_text_without_a_path_is_resolved():
    assert kind("Within cappadocian.source.gregory-nyssa-life-of-macrina (row 48)",
                "public-domain; vendored and independently verified") == RESOLVED


def test_embedded_within_a_vendored_text_is_resolved():
    assert kind('not independently vendored; embedded within "luther_works.txt"',
                "Not independently vendored; this work reaches the build only as quoted or embedded "
                "within a vendored text") == RESOLVED


def test_known_only_via_a_quoted_clause_is_resolved():
    assert kind("No specific edition identified; known only via a quoted clause inside an "
                "already-vendored text (see body note)",
                "not applicable - no single specific text has been identified for this row") == RESOLVED


def test_an_unverified_named_source_stays_unclassified():
    assert kind("Confirmed absent from the vendored npnf205",
                "not independently verified; named for completeness") == "unclassified"
