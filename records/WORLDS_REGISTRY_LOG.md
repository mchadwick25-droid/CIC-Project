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

**Census content enriched, 2026-09-14.** Following the Gallic Salvian
expansion's own precedent, Mark asked for the same treatment across the
other live worlds. A research-only subagent read `records/alx/` in full
against the live census entry and proposed sourced additions; every
proposed claim was independently re-verified against its own cited
record (quote text, figure dates, confidence tier) before being applied.
Six fields changed: `sourcing` (the untranslated Stromateis III gap),
`floorNote` (a real correction - the in-lifetime Demetrius/Origen rupture
was over his ordination, not the doctrines later condemned in 553, which
the prior text had conflated), `longDescription` (Clement never
describing a formal school he headed; the Nepos/Dionysius allegory
dispute), and `voices` (Dionysius's own plague-nursing quote; Didymus's
Tura-papyri absence and the unattested "headed the school" claim
softened to "later tradition"; Potamiaena named as the concrete instance
behind "no woman's own words"). Diff scoped and verified with
`node tools/validate-census.mjs` (0 errors).

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

**Census content enriched, 2026-09-14.** Same pass as alx's own entry
above. Five fields changed: `sourcing` (this world's own fleet-largest
quote shelf, 59 records, directly counted against every sibling world
before being stated); `longDescription` (a real correction - Kellia's
own commercial center, showing the settlements' real economic ties to
nearby villages; the popular Byzantine-Hesychast conflation named and
distinguished, citing the term's own `false_friend` field); `legacy`
(the same hesychia correction restated where a reader would meet the
later tradition); `voices[1]` (Pachomius's own sister's house across the
river, its rule against the two communities ever seeing each other's
faces, and the burial exception - her own name withheld, per the
source record's own explicit instruction that the tradition's later
name for her is not attested in this text). Verified clean.

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

**Census content enriched, 2026-09-14.** Same pass as alx's own entry
above. Two fields changed: `voices` (the two enslaved deaconesses,
named only by Pliny's own word for their office, tortured c. 112 to
learn what Christians did - the earliest outside evidence women held a
formal title here at all); `longDescription` (a real correction - "a
ten-soldier guard" read Ignatius's own metaphor, "ten leopards," as a
literal headcount; corrected against the vendored source directly, plus
the Pliny/Trajan material newly surfaced as the movement's one outside,
non-Christian witness). Verified clean.

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

**SUPPLEMENTAL SOURCE REVIEW, checked and closed with no action,
2026-09-09.** A discovery pass flagged that the Syriac Palladius
recension (`hal.source.palladius-paradise-syriac`) and Sulpitius
Severus's Dialogues (`hal.source.sulpitius-dialogues`) never made it
into the older `World-Builds/Hieronymian-Ascetic-Literary/Story-Chunks/`
and `Lexicon-Chunks/` deployment layer. Verified before touching
anything: that older layer predates this world's `records/hal/` regime
and is not what ships - `records/worlds.yaml`'s hal entry pins
`packages/hal/2026-09-04T16-41-54Z`, compiled by `engine/m2`'s
`compile_world` exclusively from `records/hal/*` (confirmed directly in
`engine/m1/loader.py`/`engine/m2/compiler.py` - neither reads
`World-Builds/` at all), and this world's own registry entry above
already states plainly that the new-regime records "supersede... the
prior framework['s]" work. Checked the live layer itself, not just the
premise: both sources are already thoroughly integrated there - each
has its own `records/hal/source/*.md` record, and both are drawn on by
multiple quote records (`hal.quote.paula-escaped-his-envy` and
`hal.contested.paula-jerome-relationship` for the Syriac Palladius
recension, with a full cross-recension divergence analysis against
`hal.source.palladius-lausiac`'s Greek text already on record;
`hal.quote.a-man-truly-catholic`, `hal.quote.always-at-his-books`, and
`hal.contested.hebrew-fluency` for Sulpitius's Dialogues I.8-9, covering
the full cited passage range). No unused corroborating material found
sitting idle in either vendored text. **No records changed, no
recompile needed** - the discovery pass's premise (a real gap in a
deployment layer) did not survive contact with which layer actually
ships. Logged here rather than left as a silent non-finding.

**Census content enriched, 2026-09-14.** Same pass as alx's own entry
above. Four fields changed: `sourcing` (a real correction - Palladius's
Greek reporting Jerome's own jealousy toward Paula hardens, in the
Syriac recension of the same passage, into a flat claim she died to
escape it; the two witnesses' own disagreement, not either one's
account, is what the field now states); `longDescription` and `legacy`
(Augustine's own Oea congregation nearly rioting over one changed word
in Jonah; Augustine's own final, published non-acceptance of the
Vulgate, quoted verbatim); `voices` (Fabiola added as a sixth voice -
her divorce/remarriage/public penance held to the same standard the
teaching applied to men, and the "first hospital" claim attributed to
Jerome's own single, uncorroborated letter rather than stated as fact).
Verified clean.

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

**Census content enriched, 2026-09-14.** Same pass as alx's own entry
above. Three fields changed: `sourcing` (the registry's own thinness
finding stated specifically rather than generically); `longDescription`
(the two conflicting primary witnesses on Jacob of Nisibis's death year
named directly, the dispute itself left open; Yazdegerd I named as the
Persian king whose favor enabled the 410 synod); `legacy` (the
Diatessaron's own displacement by the Peshitta under Rabbula, with his
personal causation stated as the historians' own live dispute, not
settled); `voices` (Simeon bar Sabbae added as a seventh voice - tax
refusal, martyrdom, the disputed year of his death named as disputed).
Verified clean.

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

**2026-09-09 post-admission source recompile (ijc only).** Two
`search_record`s added to `records/ijc/` — `ijc.search.philostorgius-homoian-fit`
and `ijc.search.opus-imperfectum-english` — recording two negative results
from a post-admission source check, so both are visible in the record layer
rather than only in the world-build folder. Neither creates a source record;
no existing record was edited; Doc_04 is unchanged and the world's Homoian
self-testimony gap remains open and remains disclosed in the
`thinness_statement`. Recompiled from 184 records (was 182):
`packages/ijc/2026-09-09T02-58-39Z`, manifest
`sha256:4ca056f2…`, superseding `packages/ijc/2026-09-04T18-49-02Z` (kept on
disk per this repo's manifest-only-tracked convention). **All 18 gates pass,
0 findings; determinism check passed; fleet staleness sweep clean across all
eight worlds.** Mark authorised the recompile in session, 2026-09-09, after
being given the option to leave the findings in the world-build folder
only — recorded here in this thread's own words rather than quoted, as an
off-repository instruction. Full working and five rounds of independent
adversarial review:
`World-Builds/Imperial-Juridical-Christianity/Post_Admission_Source_Finding_Philostorgius_OpusImperfectum_2026-09-09.md`.

Recompile history: **LEXICON LABEL PASS**, 2026-08-30: homoousios, homoios,
concilium, primatus, Tomus labeled. **FIVE-WORLD TRANSPARENCY READ**,
2026-08-30: tome-that-would-not-bend +C-T. **BAR SWEEP**, 2026-08-30, same
standard as alx.

**Census content enriched, 2026-09-14.** Same pass as alx's own entry
above. Added a `teaser` field (absent before this pass, matching the
fleet convention only Cappadocian and Gallic had carried). Four other
fields changed: `sourcing` (women's own absence named alongside the
ordinary-believer and Homoian silences, matching the registry's own
`thinness_statement`); `longDescription` (a real correction - the
world's own signature line, "the emperor is within the Church, not
above it," is Ambrose's own words from the 386 basilica standoff, not
the 390 Thessalonica penance the prior text attributed it to; both real
events are now named, in their real order); `legacy` (the same 386
vigil's own lasting liturgical legacy, Augustine's own eyewitness quote
on congregational hymn-singing); `voices` (Justina's own coercive
measures named with the source's own stated ambiguity over whether
Ambrose's letter or the record's chronology is the more reliable
witness to her role; the anonymous Homoian fragment's likely author
named, on the dominant scholarly identification, as Mercurinus
Auxentius). One internal date inconsistency found and left unresolved
rather than guessed at: `longDescription` gives Constantine's toleration
as 313, `entry.tile` and the registry's own `time_window` give 312; no
ijc record disambiguates which specific act each date names. Verified
clean.

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

## gallic (Gallic Monastic-Ascetic Christianity)

Everything about this world's own build is tracked in
`World-Builds/Gallic-Monastic-Ascetic-Christianity/` (Doc_01-Doc_10, the
Source Registry, the Representative Construction Notes, and this world's
own B-9 and Phase C scoping notes) - those documents are the record of
truth for this world; nothing further is duplicated here except the facts
a registry reader needs quickly:

- **G4 (Article 29 living-tradition determination): CONFIRMED, 2026-09-12**
  - Mark, in session, in direct response to the drafted presentation:
    "Confirm as drafted." Recorded in full in
    `gallic_Representative_Construction_Notes_Renatus.md` Section 6 and its
    Document Log. `living_tradition_flag: true` is the plain factual data
    point (this world's monastic tradition genuinely continues in living
    communities today) the confirmed determination itself relies on.
  - Five documented divergences from present-day living tradition; YES,
    moderately broad correspondence (later Western monasticism generally,
    the Roman Catholic cult of Martin of Tours, the Lerins-Marseilles
    line's continuation into the Merovingian church, the Vincentian
    canon's afterlife).
- **B-8 (2026-09-12):** first-ever compile, `state: built`. `census_id` is
  deliberately `null` - Atlas/census linking is real, later, post-admission
  work (per Cappadocian's own precedent, above), not yet done.
- **B-9 (2026-09-12):** scoped and disposed - contributes nothing beyond
  B-8, for a first-ever build with no prior hand-authored deployment to
  swap away from. Full reasoning:
  `gallic_B9_Scoping_Note.md`.
- **Phase C (2026-09-13):** scoped, not completed. The governing process
  document's own Phase C checklist describes deleted infrastructure (the
  same class of finding B-6/B-7a/B-8/B-9 each already made). The real
  remaining wiring (frontend `worlds.ts` registration, the site's portrait
  page, census linking) is confirmed structurally deferred to post-M3
  admission by direct fleet precedent, and is additionally blocked by the
  Representative portrait, which does not exist yet (a separately-deferred
  identity decision, not decided here). Full reasoning:
  `gallic_PhaseC_Scoping_Note.md`.
- **M3 admission run (2026-09-13):** 28/28 sealed probes passed, real live
  Bedrock generation (`LiveModelAnswerer`, not the fixture stand-in), one
  per fleet canon cell. Report:
  `engine/m3/reports/live-admission-report-gallic-2026-09-13.json`. Zero
  failing probes, so no raw generated answer text was preserved to
  hand-read (the script's own by-design behavior) - a real, honestly-named
  limit on this step's own verification depth, not fixed after the fact.
- **ADMITTED, 2026-09-13.** Mark's own word, in session, in direct response
  to the M3 report above: "yes, admit it."
- **Phase D live Deep Interview (2026-09-13):** a real, threaded,
  six-question conversation against the admitted package (matching
  Cappadocian's own SS38 precedent) found a genuine register defect - the
  voice broke strict we-voice under direct "which one are you - Martin or
  Cassian?" pressure. Full account:
  `gallic_PhaseD_LiveDeepInterview_2026-09-13.md`.
- **Self-reference base fix (2026-09-13), package re-pinned.** Per Mark's
  own instruction on receiving that finding ("the representative should
  not have insight to anything outside their world and all fixes should
  be base fixes not fix on fix"), `gallic.voice.craft.md`'s
  "self-reference" flavor_note was rewritten wholesale three times (never
  a bullet appended beside a prior one), each pass re-verified with a real
  recompile and live conversation. Full account, including where the
  first two passes fell short before the third held clean:
  `gallic_SelfReference_BaseFix_2026-09-13.md`. Current pin:
  `manifest_hash sha256:53b4750e53ca7f2fe0299cc5fece66b7b06c53d3a9a5a4d51ef676ddf3106f96`,
  `packages/gallic/2026-09-13T16-06-19Z`.
- **Phase D round 2, fresh questions (2026-09-13):** an independent
  re-verification against the re-pinned package - six entirely new
  questions, none reused from round 1. Zero pronoun-family output_defects
  across all four turns that reached the voice, including a fresh
  phrasing of the exact identity-collision risk the base fix targeted.
  One separate, unrelated, unfixed finding named (a markdown-heading
  formatting artifact, generic fleet infrastructure, confirmed unrelated
  to the self-reference fix by its own inconsistent appear/disappear
  pattern across every fix pass). Full account:
  `gallic_PhaseD_LiveDeepInterview_Round2_2026-09-13.md`.
- **Representative portrait locked and wired, 2026-09-13.** Mark's own
  word, in session: "yes, lock it in." A grounding brief
  (`gallic_Representative_Portrait_Grounding_Brief.md`, Cappadocian SS35
  format) was drafted, reviewed against a candidate image for
  authenticity and connection, and corrected in place once (an "undyed"
  tunic claim was checked against the source record and found to be this
  brief's own inference, not a source word - corrected, disclosed
  in-line, not silently rewritten). Two further revisions corrected the
  art directly against all seven other live portraits' own image files
  (not just their text descriptions) after a genuine distinctness risk
  was found against Chilo (Cappadocian) - hair recolored white/silver,
  belt changed to a plain rope, both confirmed against the actual image
  files. Final portrait wired to both live-serving locations
  (`cic-website/assets/portraits/gallic.jpg`,
  `cic-poc/frontend/public/images/portraits/gallic.jpg`, 720x720
  quality-85 JPEG, same pipeline as every prior world's own portrait) and
  registered in `cic-poc/frontend/src/data/worlds.ts`
  (`WORLD_ORDER`/`WORLD_ASSETS`, accent `#5A6B74`). The
  `app-world-assets/gallic`/`app-world-order/gallic` accepted-open
  disclosures in `engine/m1/cross_world.py` closed accordingly (removed,
  not left stale).
- **Census link, content upgrade, tradition page, homepage card
  (2026-09-13).** Mark: "yes, start on 1-4." `records/worlds.yaml`'s
  `census_id` set to the census's own existing entry id
  (`gallic-monastic-ascetic-christianity`, already on record from the
  2026-08-26 G0 case, not newly authored). `cic-website/data/
  world-census.json`'s `sourcing` and `why` fields upgraded against this
  build's actual findings, same discipline as Cappadocian's own SS31: the
  case document's own word-count arithmetic error corrected (502,441
  words excluding Hilary of Poitiers, not the 366,371 first reported -
  that smaller figure was actually the total with Cassian excluded
  instead, per `gallic_Doc01_World_Identification.md`'s own correction),
  the strand-singular finding folded in, construction-complete status
  named. New page `cic-website/traditions/
  gallic-monastic-ascetic-christianity.html` built to the fleet's own
  template, its four sample questions and both honest-limits paragraphs
  grounded directly in this build's own records (`gallic.gravity.
  soldier-of-christ`, `gallic.gravity.grace-and-effort`, `gallic.story.
  election-at-tours`, `gallic.limit.only-on-paper`), not invented copy.
  Homepage card added to `cic-website/index.html`'s era-2 group.
  **Found, not assumed:** `cic-website/index.html` is static markup, not
  driven by `world-census.json` at request time - adding the homepage
  card makes Renatus visibly clickable on the live production homepage
  the moment this is pushed and deployed, regardless of the census
  entry's own `status` field. `engine/m1/cross_world.py`'s own
  `check_census_link` (exercised directly, not assumed) confirms the
  `talk.html?worlds=gallic-monastic-ascetic-christianity` deep link both
  the new card and the new tradition page use cannot actually resolve
  until `world-census.json`'s `status` for this entry reads `"Built &
  Live"` - so the card and page are staged, not yet load-bearing.
  `census-id/gallic`'s accepted-open text was rewritten to name this
  precisely (not deleted - the underlying condition changed but is still
  real); `registry-null-field/gallic.census_id` closed outright, since
  `census_id` is no longer null. The status flip itself (`status`,
  `entry` block) is deliberately not done here, matching Cappadocian's
  own distinct SS30-SS32 sequence - held for Mark's own explicit word,
  not self-disposed.
- **Status flip: "Built & Live," 2026-09-13.** Mark's own word, in
  session: "yes, flip it." `cic-website/data/world-census.json`'s gallic
  entry: `status` -> `"Built & Live"`, `chip` -> `"live"`, `glyph` ->
  `null`, `statusWord` -> `"Open for conversation"`, `statusDescription`
  -> `"A completed formation world, admitted to the fleet and open for
  conversation."`, `living` -> `true` (matching registry
  `living_tradition_flag: true`), and the `entry` block populated
  (`representativeId: "renatus"`, `representativeName: "Renatus"`,
  `representativeTitle: "Bishop"`, `worldName: "The Monk-Bishops of
  Gaul"` matching registry `card_name`, `subtitle` matching registry
  `display_name`, `color: "#8FA3AC"` - the brighter on-dark variant of
  the accent already fixed for the portrait/frontend, matching how every
  prior world's own `entry.color` uses its dark-ground tint rather than
  its base hex, `tile` matching the registry's own `doorway_description`
  verbatim, `icon: "assets/portraits/gallic.jpg"`). Verified with a
  targeted line-level edit (not a full JSON round-trip), diff confirmed
  scoped to only this one movement entry, 23 lines. Full gate battery,
  `engine.m1.cross_world`, and `engine.m2.cli staleness-check` all
  re-run clean: 0 new defects, `census-id/gallic` closed (confirmed live
  against the real registry+census files, not assumed), all 10
  `test_cross_world.py` tests pass including the two that had been
  disclosed-open since Phase C. The now-fully-closed four-entry
  `ACCEPTED_OPEN` block for gallic (`registry-null-field/
  gallic.census_id`, `census-id/gallic`, `app-world-assets/gallic`,
  `app-world-order/gallic`) is gone from `engine/m1/cross_world.py`
  entirely, not left stale - the world is now fully wired end to end:
  registry, package, portrait, census, tradition page, homepage card,
  all agreeing.
- **Salvian material expanded: three new records, 2026-09-14.** Prompted
  by the project lead's own observation, in session, that Doc_05's own
  §10A Proportionality Assessment rates "ordinary believers / rustics"
  **under** relative to probable ecology, and that this world's one real
  lead for thickening it without inventing anything - Salvian of
  Marseilles, "the one Native voice whose whole work is addressed
  outward to the lapsed layperson rather than inward to the monk"
  (Doc_05 §5) - was under-used (licensed narrowly, cited only in brief
  single lines inside `gallic.force.barbarian-fiscal-ruin`). This build
  thread read Gov. V.4-6, VI.5-7, and VI.13/15 directly and in full
  (fresh reads, not secondhand from the existing force record's own
  citations) and authored three new records, none part of the original
  Doc_06/Doc_09 batches:
  - `gallic.term.bagaudae` - ordinary rural Gallic Christians' own
    experience of tax exaction, corrupt officials, and flight to or
    revolt with the barbarians; the one place in this world's whole
    record where the rural poor appear as a subject, not a mission
    field (contrast `gallic.term.heathen-rustics`).
  - `gallic.term.church-or-circus` - Salvian's charge that ordinary lay
    Christians in the cities deserted church services mid-service for
    public games; the one description in this world's record of
    ordinary lay worship attendance, as distinct from a monk's own
    interior "lukewarmness."
  - `gallic.story.circuses-amid-the-ruins` - Salvian's own eyewitness
    account ("a sight that I myself endured") of Trier's repeated sack
    and the city's surviving notables petitioning the emperors for
    circus games afterward. A genuine internal inconsistency in
    Salvian's own text (three vs. four sacks) is disclosed rather than
    resolved; the story's own actors are named as the city's elite, kept
    distinct from `church-or-circus`'s broader lay-population claim
    rather than conflated with it.

  Licensing checked against `gallic.source.salvian-on-the-government-of-
  god`'s own restriction (not licensed for the grace/free-will
  controversy) - all three draw on unrelated material, on the same basis
  the existing `government-of-god` and `lukewarmness` terms already used
  his text. Recompiled clean (`sha256:9f7211822ac9771b1b22175d492675973
  d954a36f15f297daec54d9f06b6c8f8`, `packages/gallic/2026-09-14T15-25-
  13Z`), determinism-check and staleness-check pass, `engine.m1.cross_
  world` 0 new defects (retrieval-hint-coverage now 105/105, up from
  102/102), full `pytest` suite (34 tests) green. Package re-pinned in
  `records/worlds.yaml`. **Not yet re-admitted**: Cappadocian's own
  precedent re-ran the live M3 sealed-probe battery after a content
  addition of this kind, which is real billed spend - held for the
  project lead's own word before spending rather than run
  unilaterally.
- **Re-admission after the Salvian expansion: 28/28, 2026-09-14.** Mark's
  own word, in session: "yes, run it." Preflight confirmed against
  `us.anthropic.claude-sonnet-4-5-20250929-v1:0` (us-east-1) before
  spending - cache engaged on both the non-streaming and streaming
  paths, matching spec SS7. Live sealed-probe battery re-run against
  the re-pinned package (`sha256:9f7211822ac9771b1b22175d492675973
  d954a36f15f297daec54d9f06b6c8f8`, `packages/gallic/2026-09-14T15-25-
  13Z`, the package carrying the three new Salvian records): 28/28
  passed, 0 failing probes. Report:
  `engine/m3/reports/live-admission-report-gallic-2026-09-14.json`.
  Real token counts recorded (13,770 input / 15,221 output / 35,797
  cache-write / 966,519 cache-read); no $/token or $/turn figure
  quoted, per spec principle 13, until reconciled against a real AWS
  invoice.
