"""What each runtime mechanism needs from a world's records - Tier 3, T3-A.

WHY. Tier 2 shipped two grounding checks that compare a generated turn
against the world's own vetted records. Both are generic: one mechanism
reads every world's data, no per-world code. But measuring them across the
six built worlds (2026-08-15) found five of twelve (world x check) cells
where the check runs and can find nothing to check against - and pahc,
where BOTH sit inert, so the whole grounding gate is decorative there.

Every build gate reported green throughout. They were not wrong: they
validate the records that exist, and a world with no quote records has no
quote record to fail. The gap is that a mechanism's dependency on record
data lived only inside that mechanism's own source, so nothing at build
time could know it existed, let alone that a world failed to satisfy it.

The control case proves the shape of it. The figure bridge works in all
six worlds, because its dependency (`bridge_line`) was written into the
World-Build Completion Standard's figure row when the bridge was built.
check_figure_chronology's dependency was not, because that check did not
exist when the row was written. At six worlds a human can hold that in
their head. At six hundred the failure mode is a world that passes every
gate and has half its safety net inert, and nobody notices.

So: this file is where a mechanism DECLARES what it reads. Adding a
mechanism is a row here, not a new gate - which is the only version of
this that survives hundreds of worlds.

WHAT IT IS NOT. Not a gate, and it blocks nothing. It is a table plus the
counting function over it; gates.py's gate_mechanism_coverage (T3-B) is
its only consumer, and that gate reports. Deliberately NOT part of the
gate package, so declaring a new mechanism is an ordinary change rather
than one bound by the gate-integrity rule (gates.py's own SS0 rule 4).

THE SEAM, stated plainly. The predicates here read RECORDS
(cic/records/<world>/<type>/*.md, front-matter shape); the runtime checks
read DEPLOY VIEWS (cic/deploy/<world>/*.json, built shape). Those are
different shapes for the same underlying fact, so a predicate here can in
principle drift from the runtime test it stands for, and the gate would
then certify coverage the runtime cannot actually use. Two mitigations,
neither of them clever: each dependency names its runtime counterpart in
`runtime_test` so the pair is greppable, and the two were cross-checked
empirically when this landed (both sides independently counted 14 dated
figures fleet-wide, agreeing per world: alexandria 1, desert 0,
hieronymian 5, imperial_juridical 8, pahc 0, syriac 0). Re-run that
cross-check when either side's matching rule changes.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable

# ---------------------------------------------------------------------------
# Predicates. Each answers one question about ONE record, in the record's own
# front-matter shape: does this record carry what the mechanism needs?
# ---------------------------------------------------------------------------

# An isolated 3-4 digit number inside a parenthetical - deliberately narrower
# than "a parenthetical containing a digit", because several worlds carry
# non-date parentheticals that would otherwise count as dates: "Pliny the
# Younger (Letters 10.96-97)", "Tacitus (Annals 15.44)". Their numbers are
# 1-2 digits, never 3-4, so they never match. Every real date string in the
# corpus ("d. 399/400", "r. 306-337", "bishop 189-232", "c. 260-339") carries
# at least one 3-4 digit token.
_YEAR_IN_PARENS = re.compile(r"\([^)]*\b\d{3,4}\b[^)]*\)")


def _figure_has_attested_date(rec: dict) -> bool:
    """Structured `dates` (T3-D) first, the legacy name string as fallback.

    Both count as coverage, because both are readable by Check A - a world
    is not less covered for having authored its dates before the structured
    slot existed. The fallback is what keeps hieronymian at 5/9 and
    imperial_juridical at 8/9 through this change rather than dropping them
    to 0 and manufacturing a fleet-wide regression out of a schema addition.
    """
    dates = rec.get("dates")
    if isinstance(dates, dict) and (dates.get("display") or "").strip():
        return True
    return any(_YEAR_IN_PARENS.search(n.get("name") or "")
               for n in (rec.get("names") or []))


def _figure_has_bridge_line(rec: dict) -> bool:
    return bool((rec.get("bridge_line") or "").strip())


def _quote_has_translation(rec: dict) -> bool:
    return bool((rec.get("text_translation") or "").strip())


# ---------------------------------------------------------------------------
# The manifest.
# ---------------------------------------------------------------------------

# How a mechanism behaves on a world that satisfies none of its dependency.
# This is not cosmetic: the two Tier 2 checks fail in OPPOSITE directions,
# and a reader of the logs cannot tell either one from a clean result without
# knowing which. SILENT is the more dangerous of the two - it looks like a
# pass.
INERT_SILENT = "silent"   # logs a clean-looking outcome; the miss is invisible
INERT_NOISY = "noisy"     # flags everything; real findings drown in build gaps


@dataclass(frozen=True)
class Dependency:
    """One mechanism's claim on one record type."""
    mechanism: str          # the runtime function that reads this
    label: str              # short human name, used in gate output
    record_type: str        # which record type it needs
    field: str              # the field carrying it (human orientation)
    requirement: str        # what counts as usable, in words
    predicate: Callable[[dict], bool]
    inert_mode: str         # INERT_SILENT | INERT_NOISY
    inert_consequence: str  # what actually happens to a world with none
    runtime_test: str       # the counterpart check, for the drift seam above


DEPENDENCIES: tuple[Dependency, ...] = (
    Dependency(
        mechanism="app.graph.nodes.check_figure_chronology",
        label="Tier 2 Check A (figure chronology)",
        record_type="figure",
        field="dates.display (or a year in names[].name)",
        requirement="a structured `dates` block (T3-D), or - legacy - a name "
                    "string with a parseable year like 'Fabiola of Rome "
                    "(d. 399/400)'",
        predicate=_figure_has_attested_date,
        inert_mode=INERT_SILENT,
        inert_consequence="every turn logs outcome=no_dated_figures, which "
                          "reads in the log exactly like a clean turn - the "
                          "check is doing nothing and says so in the same "
                          "words it uses when there is nothing to say",
        runtime_test="_DATED_NAME_PATTERN in app/graph/nodes.py, against "
                     "figure_registry.json's flattened names[]",
    ),
    Dependency(
        mechanism="app.graph.nodes.check_quotation_grounding",
        label="Tier 2 Check B (quotation attribution)",
        record_type="quote",
        field="text_translation",
        requirement="a non-empty translated text to match a quoted span "
                    "against",
        predicate=_quote_has_translation,
        inert_mode=INERT_NOISY,
        inert_consequence="every quotation-marked span in every turn is "
                          "logged UNLICENSED with reason "
                          "no_licensed_quotes_for_world - build gaps wearing "
                          "the costume of model errors, and the real findings "
                          "are buried in them",
        runtime_test="quote_index.licensed_quotes in app/prompts/, against "
                     "quotes.json",
    ),
    Dependency(
        mechanism="app.prompts.figure_bridge.find_figures_used",
        label="Figure bridge (participant name panels)",
        record_type="figure",
        field="bridge_line",
        requirement="a plain sentence saying who this was; composite and "
                    "community figures correctly have none",
        predicate=_figure_has_bridge_line,
        inert_mode=INERT_SILENT,
        inert_consequence="no name panels render for the world - the "
                          "transparency gap this bridge was built to close "
                          "reopens silently",
        runtime_test="build_figure_registry.py's own bridge_line filter "
                     "('Only figures with a bridge_line appear')",
    ),
)


# NOT DECLARED, deliberately - recorded here so the absences are decisions
# rather than oversights, and so nobody adds a wrong row later:
#
#   find_glosses_used      - reads confirmed_glosses.yaml, a curated
#                            vocabulary table, NOT a record type. Its
#                            coverage question is real but has a different
#                            shape and does not belong in a per-record-type
#                            count.
#   filter_grounded_citations
#                          - its candidates come from retrieval across
#                            source/term/story, so its dependency is "the
#                            world has retrievable records at all", which
#                            every built world satisfies by a wide margin. A
#                            row for it would always read green and would
#                            teach the reader to skim this table.


def coverage(records: dict) -> list[tuple]:
    """Per declared dependency, how many of that world's records satisfy it.

    `records` is one world's records keyed by id - exactly the shape
    run_gates.py already assembles. Returns one
    (dependency, n_satisfying, n_of_type) row per dependency, in manifest
    order.

    Counts the denominator too, not just the numerator: "0 dated figures"
    and "0 dated figures out of 13" are different findings, and only the
    second one tells you whether the world has figures at all.
    """
    out = []
    for dep in DEPENDENCIES:
        of_type = [r for r in records.values()
                   if r.get("record_type") == dep.record_type]
        satisfying = [r for r in of_type if dep.predicate(r)]
        out.append((dep, len(satisfying), len(of_type)))
    return out
