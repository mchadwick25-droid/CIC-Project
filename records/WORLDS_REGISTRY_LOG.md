# World Registry Log

The provenance, rulings, and decision history that used to live as inline
comments inside `records/worlds.yaml`. Moved out 2026-09-01 (Mark: "the file
should be clean of any added comments, corruption or build information, it
should be clean... you can keep a separate log"). `worlds.yaml` itself now
holds only the working registry data; this file holds why it says what it
says.

## fix

Synthetic negative-control world, never one of the formation worlds, never
admitted or open. Current package pin (`packages/fix/2026-08-29T10-26-51Z`)
is "THE REVERT" recompile, 2026-08-29 - Mark: "take it back to when it was
working... make sure there are not other things that are forced saying."
`fleet_voice` restored to fleet-parity plus only the pronoun frame clause;
`register_hold`, `story_quote_reach`, and the citation-address addendum
removed; the Table exact-sentence prescription removed (wiring). pahc
additionally: the Trinity aside trimmed from the jesus-as-god witness and
demo (out-of-window vocabulary; the Facilitator owns the time-bridge).
Source breadth is now the evidence layer's job (`_diverse_take`). Live
batteries run against this pin.

## Fleet-wide facts that apply to every admitted world

**Admission (2026-08-28).** All six original worlds (alx, desert, pahc, hal,
syr, ijc) were admitted the same day, Mark in session: "yes i admit all six
worlds." Certificate: the fleet-parity battery that day, 28/28 sealed
probes, corrected admission instrument (`engine.m4.turn.apply_net`, grading
byte-for-byte what a participant receives); report
`engine/m3/reports/live-admission-report-fleet-parity-2026-08-28.json`. The
read was Mark's own, not ceremonial - he read every flagged and failing
answer the fleet produced that day (alx's register line and his statement-6
ruling; desert's corrected witness and re-run; pahc's Bagnall disclosure;
hal's letters-not-stones answer and its fix; syr's advisories), plus three
full live Table conversations. The pinned `manifest_hash` on each world IS
the frozen artifact from that day.

**Doors-open / `CIC_ENFORCE_ADMISSION`.** `render.yaml` (the file Render's
Blueprint actually deploys) has carried `CIC_ENFORCE_ADMISSION: "1"` since
Mark's 2026-08-28 flip ("open the doors, flip the switch") - fleet-wide,
for the six worlds admitted that day. This is a global setting, not
per-world. An earlier note on Cappadocian's own registry entry claimed the
flag was still "0" pending a separate flip - that was wrong, and was never
actually checked against the deployed config before being written. Full
correction: `World-Builds/Cappadocian/CAPPADOCIAN_BUILD_LEDGER.md` §32.

**2026-09-01 schema-gap recompile (alx, desert, pahc, hal, syr, ijc).**
Earlier the same day, `modern_rendering` was added to the quote schema
(`engine/m1/schemas.py`, commit `c16f3e63`) - a real, additive fix for a
fleet-wide `gate_schema_validation` false-positive. The fix was verified
against live gate runs at the time but never propagated to these six
worlds' *compiled, pinned* packages, so CI's staleness check later flagged
all six as stale. Recompiled all six from their own unchanged records
(`packages/<world>/2026-09-01T11-51-3xZ`) - proved first, not just
asserted, that this touches nothing but the validation artifact: a
controlled before/after compile with identical package_id/records_commit/
compiler_version, only `schemas.py` swapped, showed zero byte differences
anywhere except `validation/gates-report.json` and the derived
`manifest.json`. Determinism-check passed for all six. No file under any
of their `records/<world>/` trees was edited; `engine/m2/compiler.py` and
`engine/m2/builders.py` were not touched. Full account:
`CAPPADOCIAN_BUILD_LEDGER.md` §34.

Per-world result: alx, hal, and ijc recompiled fully clean (0 findings, all
15 gates). desert and pahc and syr turned up pre-existing findings that had
been masked by the `modern_rendering` noise - real, unrelated content gaps,
named here rather than fixed (Mark's own instruction that day: don't touch
other worlds' content):
- **desert**: `desert.limit.communal-wrong-unrepaired` carries an
  undeclared `demo_tag` field (schema-validation), and that same record's
  `associated-with` link back from `desert.story.moses-leaking-jug` is
  missing (reciprocity).
- **pahc**: `pahc.limit.enslaved-voices`, `pahc.limit.ordinary-majority`,
  and `pahc.limit.womens-own-words` each carry an undeclared `demo_tag`
  field (schema-validation, three findings); `pahc.limit.enslaved-voices`
  and `pahc.limit.womens-own-words` each declare `associated-with ->
  pahc.quote.two-female-slaves-who-were-called-deaconesses` without the
  link declared back (reciprocity, two findings).
- **syr**: `syr.limit.ritual-sequence` carries an undeclared `demo_tag`
  field (schema-validation).

Superseded pins from this recompile (kept on disk, not deleted, per this
repo's manifest-only-tracked convention): `packages/alx/2026-08-30T11-03-37Z`,
`packages/desert/2026-08-30T11-03-39Z`, `packages/pahc/2026-08-30T10-56-37Z`,
`packages/hal/2026-08-30T11-03-43Z`, `packages/syr/2026-08-30T11-03-41Z`,
`packages/ijc/2026-08-30T11-03-44Z`.

## alx (Alexandrian Christianity)

`doorway_place` matches `place` deliberately - `place` is model-facing (it
compiles into the voice capsule's own "Place:" line), so the split only
earns different values where a world's model-facing locator differs from
its doorway subtitle (desert's build catalogue; syr's restated horizon).
`doorway_description` is registry-owned per Mark's 2026-08-28 direction
("simple modern english that introduces scholor terms when approptiate")
- the doorway used to reuse the world_core's own model-facing `horizon`
verbatim, which read like an abstract.

`card_name`/`display_name`: both name registers are Mark's ruling,
2026-08-28 - `card_name` the friendly participant-facing name ("the right
picture in their mind"), `display_name` the scholarly one ("to show
rigor"). The registry owns both; the census derives from them
(`cross_world` checks the correspondence).

`representative`: name and role (Theon, Catechetical Teacher) ruled by
Mark, 2026-08-21, in session.

`census_id`: verified directly against the running Atlas frontend, not
guessed from the spec's own illustrative example - `atlas-v3.html`'s
"Interview <rep>" button sends `data-aid="${m.id}"` (the census entry's
own `id` field, not `atlasId`), so that's the value the real deep link
needs. Matches this world's `world_id` independently.

`living_tradition_flag`: prior-framework confirmation by Mark, 2026-07-17
- Coptic Orthodox Church as primary heir; carried forward, re-confirmation
under the new spec flagged as pending. The doorway carries the
living-tradition distinction meanwhile (fail toward disclosure).

Recompile history before the 2026-09-01 schema-gap pass (fleet-wide facts
above): **LEXICON LABEL PASS**, 2026-08-30 (plain meaning first, the
world's own word after as a label, fleet rollout after Mark's pahc read):
eucharistia, anastasis, apokatastasis, pistis, martys, psyche labeled;
remaining terms skipped honestly (no grounded home in the spoken corpus).
Before that, **FIVE-WORLD TRANSPARENCY READ**, 2026-08-30 (Mark: "go ahead
with the change order and the five world read"; V1.2 birth condition
applied to the existing fleet): john-young-robber +C-P, kanon-pisteos +C-E.
Before that, **BAR SWEEP**, 2026-08-30 (Mark: "much better thats the bar" -
`Ministry/Technology/CiC_Register_Bar_2026-08-29.md`): every flagged spoken
field swept to the approved sample - short sentences, everyday words;
quotes character-exact; renderings at the bar.

## desert (Desert Monasticism)

`doorway_place` is Mark's plain-English doorway direction (2026-08-28);
`place` stays untouched as model-facing (proven by diffing a trial
recompile) - the strand catalogue (Nitria/Kellia/Scetis, Pispir, Tabennesi/
the Pachomian federation) is exactly the precision the model should keep.

`representative`: Papnoute, Abba (Elder) - confirmed by Mark in chat,
2026-08-22, carrying forward the prior-framework decision
(`World-Builds/Desert-Monasticism/CiC_W3_Representative_Identity_Preliminary_Decision.md`):
drawn from Strand C's own richest cross-strand-attested material, with a
binding "whole-world representation" instruction that the Representative
speak for Strands A, B, and C together. "Abba (Elder)" preserves the prior
decision's own reasoning (this world's native, popularly-recognized address
term) alongside Mark's plain-English gloss. Re-checked against this build's
completed content canon (Steps 2-4, Doc_08) and found to hold on every
axis, with one axis (whole-world representation via the demonstration set)
found only partially exercised and named honestly rather than certified -
see `records/desert/voice_craft/desert.voice.craft.md`'s own trailing
confirmation note, including one further cost: three distinct historical
men named Paphnutius appear in this build's own source/force apparatus,
never in compiled-facing content.

`census_id`: set 2026-08-26 by the cross-system consistency audit - this
was the one formation world carrying `null` here, and null is not "no
Atlas entry" for a world the census lists as Built & Live, it's a deep link
that can never match. `cic-website/index.html` sends `?worlds=${w.id}` and
`atlas-v3.html` sends `data-aid="${m.id}"`, both the census entry's own id;
`cic-poc/frontend`'s `App.tsx` matches that against this field
(`findWorldByCensusId`), so with `null` here every "Launch an Interview
with Papnoute" click landed a participant on the world list instead of
Papnoute's doorway, while the other five went straight through.

`living_tradition_flag`: set as plain fact per Doc_09c §4's own words -
"Desert Monasticism's direct historical descendants (Coptic Orthodox
monasticism, and more broadly the Eastern and Western monastic traditions
descending in part from this world via Cassian's transmission)...
constitute a living tradition." The living-tradition-differentiation review
Doc_09c §4 named as a required, unperformed freeze-eligibility gate (distinct
from this underlying factual claim) has been performed and closed clean,
2026-08-22: every compiled-facing field checked directly for present-day/
living-tradition conflation, zero genuine instances, cross-checked
independently by two parties - see Doc_09c §4's own addendum and
`World-Builds/Desert-Monasticism/CiC_W3_Living_Tradition_Differentiation_Review.md`.
External Scholarly Review (Doc_09c §4's other named freeze-eligibility
gate) remains open and unperformed.

Recompile history before the schema-gap pass: **LEXICON LABEL PASS**,
2026-08-30: logismoi, hesychia, nepsis, diakrisis, apophthegma, apatheia
labeled. **FIVE-WORLD TRANSPARENCY READ**, 2026-08-30: antony-call +C-P;
`demo.center-coming-to-belief` opening speaks the plain name (Moses).
**BAR SWEEP**, 2026-08-30, same standard as alx.

## pahc (Post-Apostolic House-Church Christianity)

`representative`: Chloe, Household Leader - step 5a deliverable (Mark's
per-world touchpoint), re-confirmed directly against the new-regime records
(`records/pahc/voice_craft/pahc.craft.chloe-voice.md`) at Step 11, not
carried forward unexamined.

`census_id`: the census entry's own `id` field, same deep-link convention
verified for alx.

`living_tradition_flag`: prior-framework determination confirmed by Mark,
2026-07-31 - universal descent (every later church looks back to rooms
like these), with a strict non-identity discipline (a bounded historical
reconstruction, not any present-day church's self-account). Carried
forward with re-confirmation under the new spec pending.

Recompile history: **LEXICON LABEL PASS**, 2026-08-30 (Mark: "yes it should
be give thanks over the cup, eucaruest (in purple)"): eucharistia,
episkopos, presbyterion, presbyteros, diakonos, baptisma, ministrae,
ekklesia labeled at their natural homes; prophetes/agape/hetaeria/
pertinacia skipped honestly. **CENTER-CELL OPENING**, 2026-08-30 (Mark:
"make the record edit," after four live probes showed the compiled
exemplar reproducing its "One of us, Ignatius" opening verbatim on later
mentions): three spoken openings now speak the plain name -
`witness.jesus-as-god`, `demo.center-jesus-as-god`,
`demo.center-who-was-jesus`; introduction is the system's own job
(name-bridge marks first meeting, already-introduced signal after).
**CENTER-CELL MAPPING**, 2026-08-30 (Mark's pilot read: the center cells
had no story or term to offer): four canon_cells additions -
grandsons-before-domitian +C-E, didache-eucharist +C-I, eucharistia +C-I,
pliny-interrogation +C-T; C-P deliberately left empty (nothing genuinely
belongs). **BAR SWEEP**, 2026-08-30, same standard as alx.

**G05 SUPPLEMENTAL SOURCE INTEGRATION**, 2026-09-09 (read-only discovery
pass flagged G05/boundary-drawing as resting on Ignatius alone despite two
already-vendored, already-compiled sources - `pahc.source.second-third-
century-remains` [Melito of Sardis] and `pahc.source.anti-montanist-
fragments` - never having been checked against it). Verified both directly
against the vendored texts before touching anything. Added both as
`sources[]` on `pahc.gravity.boundary-drawing.md` with two new illustrating
quote records: `pahc.quote.melito-no-phantom` (Melito's Fragment VII, "On
the Nature of Christ" - makes the same anti-docetic argument as Ignatius,
but flagged rather than counted as resolving Repetition, since it survives
only via Anastasius of Sinai, 7th c., not Eusebius as most of this
fragment collection does) and `pahc.quote.asia-rejected-new-prophecy`
(the anti-Montanist fragment's account of Asia's bishops synodically
rejecting the New Prophecy - a genuine independent primary-voice witness
to a *different* named contemporary rival, corroborating the gravity's
broader title-level claim without touching the anti-docetic-specific
Repetition score). Classification unchanged (Tensional); Doc_04's own
six-test findings not re-argued, only added to, per this project's own
build-cycle discipline. No escalation category applied (not an identity
decision, not portfolio-level, not governance, no unresolved
cross-review tension) - disposed of by the build thread itself.

Independent adversarial review (`Review-Artifacts-Records-Build/
Step5_G05_Supplemental_Source_Review_Round1.md`): SUBSTANTIAL REVISION
REQUIRED, narrow - two locus/line-number errors (Melito's cited range
covered only half the quotation; the anti-Montanist locus was off by
three lines) and one silently-altered punctuation mark (a colon typed as
a dash inside a `verified-direct` quote - traced to a YAML plain-scalar
constraint, not a deliberate change) - all landed at round 2, self-
verified directly against the vendored files (this project's own Step 5
precedent for narrow, mechanical fixes). A further available-but-unused
witness (Apollonius's own anti-Montanist fragments, same source record)
was disclosed in that source record's own "NOT DRAWN ON" list rather
than built out, to keep this pass narrow, per the reviewer's own
recommendation. Two cosmetic findings landed (rounding fixes); two
logged and deliberately deferred, not dropped: the anti-Montanist
fragments have no corpus-map row in `post-apostolic-house-church.yaml`
(their only corpus-map presence is in the unrelated `montanism-the-new-
prophecy.yaml`) - confirmed non-blocking (outside the compile path, not
a `gates.run_all` gate) but a real bookkeeping gap for a future pass;
and a one-clause "primary-in-content vs. direct-in-transmission" gloss
for the anti-Montanist quote's `modern_lens_note`, left at the drafter's
discretion.

Full `engine.m1.gates.run_all` battery clean both before and after the
round-2 fixes, aside from the two pre-existing, deliberately-untouched
`enslaved-voices`/`womens-own-words` reciprocity findings documented
above (2026-09-01 schema-gap recompile) and in
`World-Builds/Cappadocian/CAPPADOCIAN_BUILD_LEDGER.md`.
`world-build-docs/pahc/GRAVITY-INDEX.md` regenerated (boundary-drawing's
source count 1→3; byte-identical re-generation confirmed, isolated: 0,
non-reciprocal: 0). **Disposition: Approved to proceed** (build-thread
self-disposition per CO-022/CO-024b; no escalation category applies).

**Recompile, 2026-09-09** (commit `fa07b2e`): `python -m engine.m2.cli
build pahc` -> `packages/pahc/2026-09-09T02-57-17Z`, manifest_hash
`sha256:915b959ef22a3e0b30fb3c13d4dec0c402ccb3c536a627c0f223a264ec365f34`.
Determinism-check passed (byte-identical on a second compile).
Manifest-level diff against the prior pin (`2026-09-04T16-41-56Z`)
confirmed the changed/added file set is exactly what this pass touched
(the two new quote records; the edited gravity and source records; their
legitimate downstream ripple - `compiled/quotes.json`, `coverage.json`,
`indexes/canon-map.json`, the rebuilt FAISS indexes, `validation/*` -
plus provenance-only hash churn in files that merely embed
`records_commit`, e.g. `compiled/frame.json`, `compiled/media/
portrait.svg`). `records/worlds.yaml`'s pahc package pin updated to this
new location/hash; the superseded pin (`2026-09-04T16-41-56Z`) kept on
disk, not deleted, per this repo's own convention.

**M3 admission: rerun warranted, not run here.** pahc's registry
`state` is `admitted` (a live 28-probe sealed-battery certificate
already exists from an earlier content state - the most recent M3
report mentioning pahc predates this world's 2026-08-30 BAR SWEEP/
CENTER-CELL passes, let alone this one). This pass adds two new,
real quote records (not a mechanical/metadata-only recompile like the
2026-09-01 schema-gap pass, which was proven byte-identical in content
and explicitly did not need a fresh M3 run) - the same shape of change
Cappadocian's own precedent (`CAPPADOCIAN_BUILD_LEDGER.md` lines 767,
787: "this run re-certifies that the added quote material didn't
introduce any new grounding, isolation, or register failure") treats as
warranting a fresh live run. M3 admission requires real AWS Bedrock
spend and Mark's own explicit per-run authorization
(`engine/m3/live_admission_run.py`'s own docstring; every fleet
precedent) - not something a build thread runs on its own judgment.
Flagged here for Mark's decision, not executed.

## hal (Hieronymian Ascetic-Literary Christianity)

`census_id`: the census entry's own `id` field is what the Atlas deep link
sends (per the alx verification); matches this world's `world_id`
independently.

`representative`: Albina, Widow of the Household - Mark's ruling,
2026-08-22, step-5a touchpoint: a voice of the Bethlehem circle speaking as
a widow of the household, formed by renunciation and the scholarly labor of
testing Scripture's Latin words against the Hebrew they were first given
in, carrying the circle's whole life from Rome to Bethlehem. Deliberately
not one of this corpus's documented named figures (Marcella, Paula,
Eustochium, Fabiola, et al.) - a sanctioned Representative voice per spec
principle 14, kept distinct from their own verified quotes/stories.
Supersedes the prior framework's preliminary decision
(`hal_Representative_Identity_Preliminary_Decision.md`), not carried into
the new spec.

`living_tradition_flag`: PROVISIONAL, set toward disclosure (spec
principle 6) - the living-tradition determination is Mark's own per-world
touchpoint and has not been made for this world under the new spec. This
is a bounded historical reconstruction of one specific 382-420 network, not
today's church of any name - but Jerome, the Vulgate, and Latin monasticism
are all claimed inheritances of living traditions (Roman Catholic above
all), so the doorway carries the distinction until Mark rules otherwise.

Recompile history: **LEXICON LABEL PASS**, 2026-08-30: the translation
labor (Vulgata), Hebraica veritas, vidua, monasterium, renuntiatio,
epistula labeled. **FIVE-WORLD TRANSPARENCY READ**, 2026-08-30:
ciceronian-dream +C-P, vulgata +C-E. **BAR SWEEP**, 2026-08-30, same
standard as alx.

## syr (Syriac Christianity, Edessa/Nisibis)

`doorway_place` responds to Mark's own screen read, 2026-08-28, which
flagged the arrival card as "restated or to accedemic" - the old subtitle
duplicated the horizon's opening phrase word for word. `place` stays
untouched as model-facing (proven by diffing a trial recompile).

`representative`: Mar Yausep, Teacher of the Covenant Order - ruled by
Mark, 2026-08-28, in session ("yes i like mar yousep, role teacher of the
convenant order"), closing a foundation-audit identity finding: the prior
value carried the honorific alone in the role slot (name Yausep, role_label
Mar), which made the Facilitator's door sentence ungrammatical ("Yausep,
Mar of Syriac Christianity") and split one person across two names between
the Atlas card ("Mar Yausep") and the room. The census already carried this
ruling's values; the registry now owns them (registry wins, Mark
2026-08-28). Prior history: name and role confirmed by Mark under the new
spec, in chat, 2026-08-22, carrying forward the prior-framework decision
(`Representative_Identity_Preliminary_Decision.md` + Phase Two Formation
Calibration, 2026-07-07/08: name Yausep; role revised Malpana -> Deacon ->
Mar by Mark's own rulings).

`census_id`: same deep-link convention verified for alx; matches this
world's `world_id` independently.

`living_tradition_flag`: prior-framework confirmation by Mark, 2026-07-11
(Living Tradition Status CONFIRMED - the Syriac churches, Church of the
East, Syriac Orthodox, Eastern Catholic heirs, are living heirs); carried
forward with re-confirmation under the new spec flagged as pending.

Recompile history: **LEXICON LABEL PASS**, 2026-08-30: ihidaya, madrasha,
qyama, raza+shrara, tahwyata, Ewangeliyon da-Mhallete labeled.
**FIVE-WORLD TRANSPARENCY READ**, 2026-08-30: abgar-addai-legend +C-E,
jacob-nicaea +C-T, ihidaya +C-I, raza-shrara +C-T. **BAR SWEEP**,
2026-08-30, same standard as alx.

## ijc (Imperial and Juridical Christianity)

`representative`: Marius, Deacon of the Letters - carried from Mark's own
prior-framework decisions, both on the verifiable record: name Marius
chosen by Mark directly, 2026-07-20
(`World-Builds/Imperial-Juridical-Christianity/Open_Gaps_Tracking.md` item
13, overriding the build's own "Marcus" recommendation for his own stated
reason); participant-facing title "Apocrisiarius - Deacon of the Letters"
chosen by Mark, 2026-07-22 (same log, item 15). Confirmed by Mark,
2026-08-22, in session, at step 5 (spec 4.3): checked against this build's
full content canon (142 answer-canon records, three independent Opus
adversarial reviews plus two further confirmation passes, 13/13 M1 gates
green throughout) and found to hold without qualification. See
`records/ijc/voice_craft/ijc.voice.craft.md` and `BUILD-LOG.md` for the
full disposition.

`census_id`: verified against the census file directly, same id-field
convention alx documents; shortName "Church & Empire" is the
participant-facing card name Mark chose 2026-07-20 (`Open_Gaps_Tracking.md`
item 12).

`living_tradition_flag`: NOT yet a determination - Living Tradition Status
is pending Mark's own confirmation (Doc_01 §1; Constitution Art. 29). Set
true meanwhile so the doorway carries the distinction (fail toward
disclosure, same direction as alx): this world's Strand A content runs
directly into the present-day papacy's own claimed lineage, Strand B's
into Eastern Orthodoxy's self-understanding.

Recompile history: **LEXICON LABEL PASS**, 2026-08-30: homoousios, homoios,
concilium, primatus, Tomus labeled. **FIVE-WORLD TRANSPARENCY READ**,
2026-08-30: tome-that-would-not-bend +C-T. **BAR SWEEP**, 2026-08-30, same
standard as alx.

## cappadocian (Cappadocian Christianity)

Everything about this world's own build, rename, admission, Representative
decision, portrait, and every recompile is tracked in full in
`World-Builds/Cappadocian/CAPPADOCIAN_BUILD_LEDGER.md` (39 sections as of
2026-09-01) - that ledger is the record of truth for this world; nothing
further is duplicated here except the two facts the registry itself needs
a reader to know quickly:

- `world_id` was `nicene-cappadocian` and `display_name` was
  "Nicene-Cappadocian Christianity" until the 2026-08-31 full-alignment
  rename (Mark: "the name should reflect the world and christian tradition,
  not an old naming convention... fix it right"). Full reasoning: ledger
  §28.
- `representative.name` was `Eumathios` until the 2026-09-01 rename to
  `Chilo` (Mark: "go with Chilo," after raising that he wasn't part of the
  original name decision and that Eumathios was hard to remember). Full
  reasoning: ledger §33, and `cappadocian_Representative_Identity_Options.md`'s
  own addendum.

`census_id` (`cappadocian-nicene-pastoral-monastic-tradition`) is
deliberately NOT renamed to match the WRS `world_id` despite carrying
"nicene" in its own id string - it's a stable key five other census `edges`
entries already reference by exact string, and every sibling world's own
`census_id` already diverges from its `world_id` in exactly this same way
(e.g. ijc's census id is `imperial-juridical-christianity`, its `world_id`
is `imperial-juridical`). The entry's own participant-facing `name`/
`informalName` fields were updated to drop "Nicene"; only the internal
`id` string stays as first assigned.
