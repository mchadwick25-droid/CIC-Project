---
id: fix.front.fixture-synthetic
world_id: fixture-synthetic
record_type: world_front
schema_version: 2
status: draft
register: etic
census_id: fixture-synthetic
skim:
  tile:
    text: "Testland's own record speaks for itself: \"We never asked who you'd been before. We only asked what you carried afterward.\""
    grounded_in: [fix.quote.identity-collision-saying]
orientation:
  relations_summary:
    text: "This is a synthetic fixture world, built only to exercise the gate battery, the M2 compiler, and the admission harness - never a real formation world."
    grounded_in: [fix.core.fixture-world]
---
Website V2 world_front design (approved to proceed 2026-09-19): a real,
schema-valid world_front example living in the fixture world, quoting
fix.quote.identity-collision-saying's own modern_rendering field
correctly (gate_quote_mark_fidelity, engine/m1/gates.py, passes it
cleanly - proven directly by engine/m1/tests/test_world_front_gates.py,
though that gate is implemented and unit-tested rather than yet added to
GATES/run_all; see its own registration comment for why).

Deliberately minimal - one skim.tile unit and one orientation unit, both
mode 1, both grounded in real fixture records. No world (fixture or real)
has been migrated to a full world_front yet; that is a separate,
later stage. This record exists to prove the schema, not to model a
complete world_front's own eventual shape.

No Representative content appears in this record, and none ever will:
world_front is excluded from every path that feeds the Representative's
own prompt/capsule/chunks/repository.json (engine/m2/builders.py -
CHUNK_DIR_BY_TYPE, build_prompt, build_capsule, and _PACKAGE_EXCLUDED_
RECORD_TYPES) - see engine/m2/tests/test_voice_assembly_exclusion.py for
the regression proof.
