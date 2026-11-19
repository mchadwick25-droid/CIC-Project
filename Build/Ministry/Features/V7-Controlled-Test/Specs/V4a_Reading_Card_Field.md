# V4a: the reading-card field

**Owner:** engine thread. **Model:** Opus. This is a schema change on canonical records.

**Purpose.** Add an optional `reading_card` field to quote and story records, holding the lines in `../Test_Plan.md` §3. Production must not see it.

**Change order.** `Schema_Change_Order_Reading_Card.md` in `Build/Ministry/Features/Answering-From-Sources/`, in the form of the existing schema change orders there. It records:
- the fields;
- the rule that every line names its source;
- that `whose_view` is prose, not a rank;
- that the field is stripped at compile.

**Design.**
- **Schema.** `engine/m1/schemas.py` gets `reading_card` with properties `setting`, `source_says`, `historians_conclude` (text plus a `confidence` from the five-level vocabulary), `contributes`, `whose_view`, `open`, `reads_differently_today`, `complicated_by` (record ids) and `sources`. `sources` maps each line to the source id and locus, or the construction document and section, that supports it.
- **Gate.** In `engine/m1/gates.py`, each line present must name a source. `complicated_by` ids must exist. The whole card must be 120 words or fewer.
- **Compile.** The compiler adds `reading_card` to `_PACKAGE_STRIPPED_FIELDS` (`engine/m2/builders.py:719`), so `prompt.txt` and `repository.json` are unchanged.
- **Test-time access.** A small loader reads cards and lens notes from `records/<world>/` for the test only.

**May touch.** `engine/m1/schemas.py`, `engine/m1/gates.py`, `engine/m2/builders.py` (the strip set only), a loader module, tests, and the change order. **Must not touch.** Any record's content, `render.yaml`, the turn path.

**Tests written first.**
1. A card missing the source for a line fails the gate.
2. A card over 120 words fails.
3. A `complicated_by` id that does not exist fails.
4. Compiling alx with a fixture card leaves `prompt.txt` and `repository.json` byte-equal.
5. The loader returns the card and the lens note for a fixture record.

**Done when.** The tests pass, the fleet gates are unchanged on every world, and the change order is filed.

**Cost.** None.
