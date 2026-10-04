"""The CI-blocking gate (Library Access Gate D3 SS4.2): the day the confinement
battery stops being report-only. Runs `engine.m1.gates.run_all` AND
`engine.m9.confinement.run_all` for every world the registry says is
`built`/`admitted`/`open` - the same `STALENESS_CHECKABLE_STATES` set
`engine/m2/checks.py`'s own staleness sweep uses, reused rather than
re-declared - and fails the run on anything not named in ACCEPTED_OPEN.

ACCEPTED_OPEN here is a *different* registry from engine/m1/cross_world.py's
own ACCEPTED_OPEN (RF-10): that one is `dict[str, str]`, a finding key to a
one-line reason; this one is `dict[str, Waiver]`, because a library-access
waiver additionally carries a deadline and an owner (SS4.2) - the same
spirit (a defect stays visible, not suppressed), a different shape,
because these are different scopes. A key here is `<layer>:<check>/<world>`,
e.g. `"m1:reciprocity/don"`, `"m9:voicing-pair/don"`.

GRANDFATHERED_WORLDS is the fixed set of worlds built before this gate
existed - it only ever shrinks, never grows (SS4.2). A waiver naming a
world outside it is itself a hygiene failure: grandfathering is closed. The
one way through is an exception the project lead has approved: the waiver
then carries both an owning finding (`owner`) and `approved_by` naming
PROJECT_LEAD, and without both it stays a failure.
`fix` is deliberately absent from that set and gets no special-case code
to keep it out of enforcement - the fixture world must already be 100%
clean, so if it ever isn't, that is exactly the kind of drift this gate
exists to catch (SS4.4).

Two named, disclosed exceptions, not a quiet reopening of the rule: `rzg`
was added directly by the project lead, not self-granted by that world's
own build/go-live thread, after that thread found rzg's own content
fully clean on every check but `m9:shelf-row` - the same project-wide
CM-1 gap every one of the worlds above also carries, blocked on
infrastructure that does not exist yet for any world, not a quality gap
specific to rzg. `witt` was added the same
way and for the identical reason - `m9:shelf-row` only, same CM-1 gap,
same project-lead sign-off - the standard held is the best quality,
whatever it takes - given in answer to whether to also waive witt's own
`m9:emic-vendored-only` findings the same way rzg's shelf-row exception
did; the answer there was no, fix the 27 records, so witt's own
grandfathering stays scoped to shelf-row alone, same as rzg's). Every
other check stays fully un-waivable for a genuinely new world; neither
exception is a precedent for admitting a world with real, world-specific
findings unwaived.

The one written-in exception is R-4: `m9:voicing-pair` findings on a
NEW (non-grandfathered) world are demoted to report-only, never blocking
and never requiring a waiver, for as long as `cic/corpus-map/PAIRS.yaml`
carries no real (non-fixture) pair ruling yet - checked live against the
file each run, not hardcoded, so the carve-out ends itself the day
corpus-map lands its first one. Every other check stays fully un-waivable
for a new world.
"""
from __future__ import annotations

import datetime
import sys
from dataclasses import dataclass

from engine.m1 import gates
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import load_registry
from engine.m2.checks import STALENESS_CHECKABLE_STATES

from . import loader
from .confinement import run_all as confinement_run_all

GRANDFATHERED_WORLDS = frozenset(
    {"alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "pahc", "syr", "rzg", "witt"}
)

# Not a world - the registry key gate_readability_fleet's own findings are
# reported under (engine/m1/gates.py). Fleet content (fleet_voice,
# modern_term) is checked once, not once per world, so it needs a stable
# key of its own rather than being folded into any single real world's
# count; exempted from the GRANDFATHERED_WORLDS membership check below for
# the same reason - it was never admitted as a world and grandfathering
# was never a question that applied to it.
FLEET_PSEUDO_WORLD = "_fleet"


PROJECT_LEAD = "project lead"


@dataclass(frozen=True)
class Waiver:
    count: int
    deadline: str  # ISO "YYYY-MM-DD" - the day this waiver must be gone
    owner: str  # the finding and thread that own the repair
    approved_by: str = ""  # required, and must name PROJECT_LEAD, for any world outside GRANDFATHERED_WORLDS


def new_world_waiver_problem(waiver: Waiver) -> str | None:
    """Why a waiver on a world outside GRANDFATHERED_WORLDS is not allowed,
    or None when it carries both an owning finding and the project lead's
    own approval."""
    if not waiver.owner.strip():
        return "it names no owning finding"
    if waiver.approved_by.strip() != PROJECT_LEAD:
        return f"it lacks approved_by: {PROJECT_LEAD!r}"
    return None


# Populated from the first real run against the fleet, not from D3 SS4.3's
# own table - that table was written before engine/m9/confinement.py
# existed to measure anything, and says so itself ("the exact values come
# from the first real run, not from here"). At increment 4, the real run
# was smaller than SS4.3 predicted for the m9: side: `shelf-row`,
# `emic-vendored-only`, `voicing-pair` and `shelf-confidence` were all
# silent on every real world, because no real source record had
# `kind`/`shelf_row` set yet - checks gated on those fields had nothing to
# resolve against, so they found nothing to report, correctly, not
# because the library was clean. The kind-only migration is closing that
# gap one world at a time via `Build/tools/set_source_kind.py`: `gallic` is
# migrated first (the
# worked pattern - it has the fleet's only `kind: absence`-eligible real
# records to prove the tool handles correctly by skipping them), and each
# world's move from `source-kind` alone to `source-kind` (reduced) +
# `shelf-row` + `emic-vendored-only` is a fresh, real measurement against
# that world's own post-migration data - never copied from another
# world's numbers, never predicted in advance.
#
# The m1: side is LARGER than D3 SS4.1's own narrative named. That section
# says only "don ships with 52 reciprocity findings, syr with 1
# voice-perspective finding" - true as far as it went, but D3 was frozen
# before this file ever ran engine.m1.gates.run_all() across every
# built/admitted/open world. The first real run found three more worlds
# already carrying live m1 findings nobody had written up:
# `m1:readability/gallic` (3), `m1:reciprocity/desert` (1),
# `m1:reciprocity/gallic` (14), `m1:reciprocity/pahc` (2),
# `m1:voice-perspective/cappadocian` (1), `m1:voice-perspective/gallic`
# (2). None of these are new - they predate this workstream entirely and
# CI has been green through all of them (today no gate blocks anything,
# D3 SS4.1) - but root CLAUDE.md is explicit that a known fleet defect not
# being fixed right now gets a dated waiver, not a free pass by omission.
# Waived here on that basis, each owned by its own world's build thread.
ACCEPTED_OPEN: dict[str, Waiver] = {
    "m9:shelf-row/alx": Waiver(count=25, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:shelf-row/desert": Waiver(count=18, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:emic-vendored-only/desert": Waiver(count=20, deadline="2026-12-14", owner="desert's own build thread - each emic record needs re-grounding in a vendored primary source or its citation removed"),
    "m9:source-kind/gallic": Waiver(count=2, deadline="2026-12-14", owner="the two gallic.*-absence records - kind: absence + real absence_probes still need an editorial pass (increment 7's own remaining item); gallic's build thread"),
    "m9:shelf-row/don": Waiver(count=60, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:emic-vendored-only/don": Waiver(count=20, deadline="2026-12-14", owner="don's own build thread - each emic record needs re-grounding in a vendored primary source or its citation removed"),
    "m9:shelf-row/gallic": Waiver(count=21, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:emic-vendored-only/gallic": Waiver(count=10, deadline="2026-12-14", owner="gallic's own build thread - each emic force/term/limit record needs re-grounding in a vendored primary source or its citation removed"),
    "m9:shelf-row/cappadocian": Waiver(count=54, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:emic-vendored-only/cappadocian": Waiver(count=62, deadline="2026-12-14", owner="cappadocian's own build thread - each emic record needs re-grounding in a vendored primary source or its citation removed"),
    "m9:shelf-row/hal": Waiver(count=28, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:shelf-row/ijc": Waiver(count=29, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:emic-vendored-only/ijc": Waiver(count=2, deadline="2026-12-14", owner="ijc's own build thread - each emic record needs re-grounding in a vendored primary source or its citation removed"),
    "m9:shelf-row/pahc": Waiver(count=23, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:shelf-row/syr": Waiver(count=24, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:emic-vendored-only/syr": Waiver(count=38, deadline="2026-12-14", owner="syr's own build thread - each emic record needs re-grounding in a vendored primary source or its citation removed"),
    "m1:reciprocity/desert": Waiver(count=1, deadline="2026-12-14", owner="pre-existing, unwritten-up until this run; desert's own build thread"),
    "m1:reciprocity/don": Waiver(count=52, deadline="2026-12-14", owner="D2 SS1.3(e) - don's own known reciprocity gap; don's build thread"),
    "m1:reciprocity/gallic": Waiver(count=14, deadline="2026-12-14", owner="pre-existing, unwritten-up until this run; gallic's own build thread"),
    "m1:reciprocity/pahc": Waiver(count=2, deadline="2026-12-14", owner="pre-existing, unwritten-up until this run; pahc's own build thread"),
    "m1:voice-perspective/cappadocian": Waiver(count=1, deadline="2026-12-14", owner="pre-existing, unwritten-up until this run; cappadocian's own build thread"),
    "m1:voice-perspective/syr": Waiver(count=1, deadline="2026-12-14", owner="D2 SS1.3(e) - syr's own known voice-perspective gap; syr's build thread"),
    "m9:shelf-row/rzg": Waiver(count=11, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m9:shelf-row/witt": Waiver(count=47, deadline="2027-03-15", owner="CO-5/RF-6: blocked until corpus-map's CM-1 lands - no row_id exists to copy before then and the no-guessing rule forbids inventing one; date is a ceiling, not a real target - revisit when CM-1 lands"),
    "m1:quote-verbatim/gallic": Waiver(count=1, deadline="2026-12-14", owner="gallic.quote.salvian-on-the-unburied-dead - one footnote-marker artifact in cic/texts/salvian_on-the-government-of-god_sanford1930.txt (a bare closing curly quote glued to \"captures,\" with no matching open, unlike this edition's other two now-registered apparatus patterns) isn't a safe edition-wide regex (41 real opening curly quotes and legitimate closing-quote usage elsewhere in this same file); needs a narrower, structurally-anchored rule, not a blanket strip - Decision 8B's own gallic thread"),
    # gate_readability covers every field engine/m1/spoken_fields.py
    # declares under an instruction/voice-diet/evidence-head/
    # facilitator-spoken role, not just term/honest_limit/
    # quote.modern_rendering/voice_craft. None of these eleven counts is
    # new drift - every one is pre-existing content the narrower gate
    # never graded, mostly concentrated in doctrinal_witness.positions
    # and gravity/force.description across the fleet.
    "m1:readability/alx": Waiver(count=20, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; alx's own build thread"),
    "m1:readability/cappadocian": Waiver(count=302, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; cappadocian's own build thread"),
    "m1:readability/desert": Waiver(count=153, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; desert's own build thread"),
    "m1:readability/don": Waiver(count=330, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; don's own build thread"),
    "m1:readability/gallic": Waiver(count=100, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; gallic's own build thread"),
    "m1:readability/hal": Waiver(count=161, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; hal's own build thread"),
    "m1:readability/ijc": Waiver(count=156, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; ijc's own build thread"),
    "m1:readability/pahc": Waiver(count=160, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; pahc's own build thread"),
    "m1:readability/rzg": Waiver(count=134, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; rzg's own build thread"),
    "m1:readability/syr": Waiver(count=153, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; syr's own build thread"),
    "m1:readability/witt": Waiver(count=194, deadline="2026-12-14", owner="pre-existing spoken-field content exceeds the FK/FRE ceiling; witt's own build thread"),
    # gate_readability_fleet's own findings (fleet_voice and modern_term
    # spoken fields) - counted once against the
    # FLEET_PSEUDO_WORLD key, never against any single real world's own
    # count, for the reason gate_readability_fleet's own docstring gives.
    "m1:readability-fleet/_fleet": Waiver(count=7, deadline="2026-12-14", owner="pre-existing fleet_voice/modern_term spoken-field content exceeds the FK/FRE ceiling; fleet-content build thread"),
    # Slice 5 (System Hub decision 40): the status, cells-required and horizon
    # gates' findings on content that predates them.
    "m1:cells-required/alx": Waiver(count=4, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; alx's own build thread"),
    "m1:horizon/alx": Waiver(count=1, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; alx's own build thread"),
    "m1:cells-required/cappadocian": Waiver(count=91, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; cappadocian's own build thread"),
    "m1:horizon/cappadocian": Waiver(count=5, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; cappadocian's own build thread"),
    "m1:status-ready/desert": Waiver(count=1, deadline="2027-03-15", owner="slice 5 status gate: each draft record is finished and marked ready, or marked voice: analytic; desert's own build thread"),
    "m1:cells-required/desert": Waiver(count=5, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; desert's own build thread"),
    "m1:horizon/desert": Waiver(count=1, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; desert's own build thread"),
    "m1:status-ready/don": Waiver(count=25, deadline="2027-03-15", owner="slice 5 status gate: each draft record is finished and marked ready, or marked voice: analytic; don's own build thread"),
    "m1:cells-required/don": Waiver(count=30, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; don's own build thread"),
    "m1:status-ready/gallic": Waiver(count=3, deadline="2027-03-15", owner="slice 5 status gate: each draft record is finished and marked ready, or marked voice: analytic; gallic's own build thread"),
    "m1:cells-required/gallic": Waiver(count=119, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; gallic's own build thread"),
    "m1:horizon/gallic": Waiver(count=5, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; gallic's own build thread"),
    "m1:cells-required/hal": Waiver(count=5, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; hal's own build thread"),
    "m1:horizon/hal": Waiver(count=1, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; hal's own build thread"),
    "m1:cells-required/ijc": Waiver(count=4, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; ijc's own build thread"),
    "m1:horizon/ijc": Waiver(count=1, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; ijc's own build thread"),
    "m1:status-ready/pahc": Waiver(count=2, deadline="2027-03-15", owner="slice 5 status gate: each draft record is finished and marked ready, or marked voice: analytic; pahc's own build thread"),
    "m1:cells-required/pahc": Waiver(count=8, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; pahc's own build thread"),
    "m1:horizon/pahc": Waiver(count=6, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; pahc's own build thread"),
    "m1:cells-required/rzg": Waiver(count=9, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; rzg's own build thread"),
    "m1:cells-required/syr": Waiver(count=9, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; syr's own build thread"),
    "m1:horizon/syr": Waiver(count=1, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; syr's own build thread"),
    "m1:cells-required/witt": Waiver(count=50, deadline="2027-03-15", owner="slice 5 cells-required gate: each voiced record names the canon cells it serves, or is marked voice: analytic; witt's own build thread"),
    "m1:horizon/witt": Waiver(count=2, deadline="2027-03-15", owner="slice 5 horizon gate: each post-window mention is rewritten from inside the window, or its record marked voice: analytic; witt's own build thread"),
    "m1:use-note-present/desert": Waiver(count=3, deadline="2027-03-15", owner="slice 6 use-note gate: each voiced citable record carries a use note (means, not_for, years), drafted and Opus-reviewed against the vendored source; desert's own build thread"),
    "m1:use-note-present/hal": Waiver(count=1, deadline="2027-03-15", owner="slice 6 use-note gate: each voiced citable record carries a use note (means, not_for, years), drafted and Opus-reviewed against the vendored source; hal's own build thread"),
    "m1:use-note-present/ijc": Waiver(count=1, deadline="2027-03-15", owner="slice 6 use-note gate: each voiced citable record carries a use note (means, not_for, years), drafted and Opus-reviewed against the vendored source; ijc's own build thread"),
    "m1:use-note-present/pahc": Waiver(count=1, deadline="2027-03-15", owner="slice 6 use-note gate: each voiced citable record carries a use note (means, not_for, years), drafted and Opus-reviewed against the vendored source; pahc's own build thread"),
    "m1:use-note-present/witt": Waiver(count=1, deadline="2027-03-15", owner="slice 6 use-note gate: each voiced citable record carries a use note (means, not_for, years), drafted and Opus-reviewed against the vendored source; witt's own build thread"),
}


def _voicing_pair_carve_out_active() -> bool:
    """R-4: alive only while PAIRS.yaml has no real (non-fixture) pair."""
    pairs_list, _ = loader.read_pairs()
    return not any(
        not (str(p.get("a", "")).startswith("fixture") and str(p.get("b", "")).startswith("fixture"))
        for p in pairs_list
    )


def collect_findings(registry: dict | None = None) -> dict[str, dict[str, list[str]]]:
    """world -> "<layer>:<check>" -> findings, both batteries, run fresh."""
    registry = registry if registry is not None else load_registry()
    fleet = load_fleet_records()
    by_world: dict[str, dict[str, list[str]]] = {}
    for world_key, entry in sorted(registry.items()):
        if entry.get("state") not in STALENESS_CHECKABLE_STATES:
            continue
        records = load_world_records(world_key)
        merged: dict[str, list[str]] = {}
        for name, findings in gates.run_all(records, fleet, registry).items():
            merged[f"m1:{name}"] = findings
        # gate_readability_floor is not in GATES (see its own docstring) -
        # collected here under its own key, which hygiene_problems() below
        # permanently excludes from the waiver mechanism: a sub-8 field is
        # reported, never failed, so it needs no waiver to stay green.
        merged["m1:readability-floor"] = gates.gate_readability_floor(records, fleet, registry)
        shelf = loader.load_shelf(world_key=world_key, census_id=entry["census_id"], records=records)
        for name, findings in confinement_run_all(records, shelf).items():
            merged[f"m9:{name}"] = findings
        by_world[world_key] = merged
    # gate_readability_fleet grades the fleet records once, not once per
    # world (see that function's own docstring) - collected here, outside
    # the per-world loop above, under FLEET_PSEUDO_WORLD's own key.
    by_world[FLEET_PSEUDO_WORLD] = {
        "m1:readability-fleet": gates.gate_readability_fleet(fleet),
        "m1:readability-floor": gates.gate_readability_floor_fleet(fleet),
    }
    return by_world


def hygiene_problems(by_world: dict[str, dict[str, list[str]]], *, today: str | None = None) -> list[str]:
    """Every reason `engine.m9.cli check` would exit 1: an unwaived finding,
    a stale or expired waiver, or a waiver naming a world grandfathering has
    closed to. `by_world` is `collect_findings()`'s own return shape, passed
    in rather than recomputed so a test can hand this a fixed snapshot."""
    today = today or datetime.date.today().isoformat()
    carve_out = _voicing_pair_carve_out_active()

    live: dict[str, int] = {}
    for world_key, checks in by_world.items():
        for name, findings in checks.items():
            if not findings:
                continue
            if name == "m1:readability-floor":
                continue  # gate_readability_floor: FK < 8 is reported, not failed - permanent, never needs a waiver
            if name == "m9:voicing-pair" and world_key not in GRANDFATHERED_WORLDS and carve_out:
                continue  # R-4: report-only until corpus-map lands its first real pair
            live[f"{name}/{world_key}"] = len(findings)

    problems: list[str] = []
    for key, count in sorted(live.items()):
        world_key = key.rsplit("/", 1)[1]
        waiver = ACCEPTED_OPEN.get(key)
        if waiver is None:
            problems.append(f"{key}: {count} unwaived finding(s) - new, undocumented drift")
            continue
        if world_key not in GRANDFATHERED_WORLDS and world_key != FLEET_PSEUDO_WORLD:
            reason = new_world_waiver_problem(waiver)
            if reason is not None:
                problems.append(f"{key}: waived, but {world_key!r} is not grandfathered - grandfathering is closed, and {reason}")
                continue
        if waiver.count != count:
            direction = "the waiver is stale - tighten it" if waiver.count > count else "new drift beyond the waiver"
            problems.append(f"{key}: waiver says {waiver.count}, this run found {count} - {direction}")
        if waiver.deadline < today:
            problems.append(f"{key}: waiver deadline {waiver.deadline} has passed")

    for key in sorted(ACCEPTED_OPEN):
        if key not in live:
            problems.append(f"{key}: ACCEPTED_OPEN names a finding that no longer fires - delete it")

    return problems


def report_only(by_world: dict[str, dict[str, list[str]]]) -> list[str]:
    """Findings hygiene_problems() above deliberately never blocks on, but
    that should still be visible somewhere: the R-4 carve-out's own
    voicing-pair findings on a new world (temporary - ends itself once
    corpus-map lands a real pair), and every world's readability-floor
    observations (permanent - gate_readability_floor's own docstring)."""
    lines = []
    carve_out = _voicing_pair_carve_out_active()
    for world_key, checks in sorted(by_world.items()):
        if carve_out and world_key not in GRANDFATHERED_WORLDS:
            findings = checks.get("m9:voicing-pair") or []
            if findings:
                lines.append(f"m9:voicing-pair/{world_key}: {len(findings)} finding(s) - report-only under R-4 (no real PAIRS.yaml pair yet)")
        for finding in checks.get("m1:readability-floor") or []:
            lines.append(f"m1:readability-floor/{world_key}: {finding}")
    return lines


def main(argv: list[str] | None = None) -> int:
    by_world = collect_findings()
    problems = hygiene_problems(by_world)
    observations = report_only(by_world)

    if observations:
        print(f"{len(observations)} report-only observation(s):\n")
        for line in observations:
            print(f"  {line}")
        print()

    if problems:
        print(f"library access gate: {len(problems)} problem(s)\n")
        for line in problems:
            print(f"  {line}")
        return 1

    print("library access gate: clean - every finding is waived, every waiver is live and current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
