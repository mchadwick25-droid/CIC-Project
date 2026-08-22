# Desert Monasticism — Doc_08 Index (Forces)

**Derived from:** 12 force records (`records/desert/force/`) — this index is generated against those files and re-checked against them; the records are the source of truth. Re-derivation base: the prior build's cleared Doc_08 (`World-Builds/Desert-Monasticism/CiC_W3_Doc08_Forces_Document.md`, three review rounds, a fully-tested six-cell matrix with twelve force entries and a gravity-force synthesis table) — carried into the new record schema, with every force's Layer 1/2/3 content, confidence rating, and gravity-trace re-checked against this build's own step-2/3a/3b/3c records rather than carried forward unread.

**Schema note:** `force` carries `name`, `kind` (enum: `initiating`/`ongoing`/`ending`), `description`, `manifestations[]` — three values, not Doc_08's own six cells (1A/1B/2A/2B/3A/3B, crossing the initiating/ongoing/ending axis with an internal/external axis the schema does not carry). Following the convention already established in the Alexandria build's own force records (e.g. `alx.force.persecution`'s `name: "... [2A - ongoing/external]"`), every force's own cell code is carried in its `name` field as a bracketed suffix, not inferred from `kind` alone. `force` is not compiled-facing (no jargon-leak discipline applies, matching the precedent already established for `gravity` at Step 3b): build-apparatus vocabulary, gravity-number and cell-code cross-references are legitimate in every field.

## The Six-Cell Matrix

| Cell | Force | kind | Confidence |
|---|---|---|---|
| 1A (initiating/external) | `desert.force.martyrdom-unavailable` — the end of persecution, closing off martyrdom | initiating | Documented (event) / Reported-Experience (world's-own-experience) |
| 1B (initiating/internal) | `desert.force.village-ascetic-culture` — a pre-existing village-level ascetic culture | initiating | Contested |
| 1B (initiating/internal) | `desert.force.scriptural-address` — inherited scriptural formation logic | initiating | Contested |
| 1B (initiating/internal) | `desert.force.formation-at-scale` — the formation-at-scale problem, Pachomius's innovation | initiating | Widely Accepted |
| 2A (ongoing/external) | `desert.force.economic-embeddedness-ongoing` — ongoing economic/administrative embeddedness | ongoing | Contested (Layer 1 mixed: Documented for Kellia, Documented-but-caveated for Nepheros) |
| 2A (ongoing/external) | `desert.force.melitian-rivalry` — the Melitian schism as a persistent rival movement | ongoing | Contested |
| 2B (ongoing/internal) | `desert.force.authority-tension-ongoing` — the unresolved person-vs-office authority tension | ongoing | Widely Accepted |
| 2B (ongoing/internal) | `desert.force.evagrian-intensification` — intellectual intensification within Strand C | ongoing | Widely Accepted |
| 3A (ending/external) | `desert.force.origenist-controversy` — episcopal/conciliar intervention, 399-400 | ending | Documented (synod/expulsion) / Contested (Theophilus's motives) |
| 3A (ending/external) | `desert.force.centralization-trend` — the longer imperial-ecclesiastical centralization trend | ending | Widely Accepted (general trend) / Inferential-Thin (Shenoute causal chain) |
| 3B (ending/internal) | `desert.force.authority-tension-vulnerability` — the authority tension as a standing vulnerability | ending | Widely Accepted |
| 3B (ending/internal) | `desert.force.oral-to-written-shift` — the shift from oral to written, compiled anthology | ending | Documented (chronology) / Inferential-Thin (selection criteria) |

Twelve forces across six cells, matching Doc_08's own count and distribution exactly (1A: 1; 1B: 3; 2A: 2; 2B: 2; 3A: 2; 3B: 2).

## Gravity-Force Synthesis

Per Forces Framework Section 4 (Step 8): every confirmed gravity from Doc_04/GRAVITY-INDEX.md is traceable to at least one force.

| Gravity | Classification | Traced to force(s) |
|---|---|---|
| `desert.gravity.withdrawal` | Primary | `martyrdom-unavailable` (the generating force); `village-ascetic-culture` (the substrate it intensified) |
| `desert.gravity.spiritual-combat` | Primary | `martyrdom-unavailable` (martyrdom's own vocabulary relocated to interior struggle) |
| `desert.gravity.elder-authority` | Primary | `village-ascetic-culture` (the inherited old-man tradition Antony drew on, per Doc_08's own trace); `authority-tension-ongoing` (its ongoing tension with office-based authority) |
| `desert.gravity.manual-labor` | Primary | `economic-embeddedness-ongoing` |
| `desert.gravity.diakrisis` | Primary | `authority-tension-ongoing`, `evagrian-intensification` (the ongoing internal discipline required to calibrate the combat/systematization gravities against each other) — Doc_08's own flagged weakest linkage in its synthesis table: *diakrisis* functions more as a cross-cutting regulative skill than as a force-generated gravity in the same direct sense as the others; this trace shows traceability-in-principle, not a tight causal derivation, and no force record declares a relation to `desert.gravity.diakrisis` for that reason - the trace is recorded here, in this index, rather than manufactured as a record-level relation neither force entry's own evidence actually supports |
| `desert.gravity.koinonia` | Supporting | `formation-at-scale` — itself the origin of `authority-tension-ongoing`'s own dynamic |
| `desert.gravity.scriptural-engagement` | Primary | `scriptural-address` |
| `desert.gravity.economic-embeddedness` | Tensional | `economic-embeddedness-ongoing` (the same force generating manual labor, read for its own under-documented Layer 2 gap); `melitian-rivalry` |
| `desert.gravity.evagrian-systematization` | Supporting | `evagrian-intensification` (its own internal intensification and structural narrowness); `origenist-controversy` (the external force that later exploited that narrowness) — the clearest cross-cell case in this corpus |
| `desert.gravity.authority-tension` | Tensional | `authority-tension-ongoing` (its ongoing form); `authority-tension-vulnerability` (its role in this corpus's own conjunctural closing synthesis, below) |

**Cross-cell interaction, beyond the individual force entries above:** the single most important cross-cell finding in this corpus is that `evagrian-systematization` and `authority-tension` are not independent stories — the systematization gravity's own concentration (an ongoing, internal dynamic) made it vulnerable to the Origenist controversy's external action specifically because the authority tension meant this world had never developed an internal mechanism, cross-strand or otherwise, for adjudicating exactly this kind of dispute before an outside authority did so instead. This is `desert.force.authority-tension-vulnerability`'s own stated synthesis, reasoned from the evidence assembled at the two force records it draws on, not an independently attested historical claim.

## Closing synthesis: internal or external?

Doc_07 §10 (Step 3c-era build, already cleared) reserved this exact question for the forces step: whether this world's eventual closing was primarily internally or externally driven. `desert.force.authority-tension-vulnerability`'s own body answers it as **conjunctural**, matching Doc_08's own answer exactly: an internal structural vulnerability (the never-resolved authority tension, meaning no internal body existed that could have contained the Origenist dispute before it required external intervention) combined with an external trigger (episcopal action) that specifically exploited that vulnerability. Neither force alone explains the outcome; their interaction does. This is offered as this corpus's own reasoned interpretation, not settled historical fact, matching Doc_08's own explicit flag that it should be tested at a later Validation stage alongside this build's other interpretive claims.

## Canon cells

| record | canon_cells |
|---|---|
| `desert.force.martyrdom-unavailable` | F1-I, F4-P |
| `desert.force.village-ascetic-culture` | F4-E |
| `desert.force.scriptural-address` | F2-I |
| `desert.force.formation-at-scale` | F4-I, F3-I |
| `desert.force.economic-embeddedness-ongoing` | F5-E, F5-I |
| `desert.force.melitian-rivalry` | F3-T |
| `desert.force.authority-tension-ongoing` | F3-I |
| `desert.force.evagrian-intensification` | F4-P |
| `desert.force.origenist-controversy` | F6-I, F3-I |
| `desert.force.centralization-trend` | (none) |
| `desert.force.authority-tension-vulnerability` | F3-I |
| `desert.force.oral-to-written-shift` | F2-E |

`force` is not in `engine/m1/canon.py`'s `substantive_types()` (`{"doctrinal_witness", "term", "story", "quote"}`), so none of the cells above are gate-visible for canon-coverage purposes — matching the precedent already established for `gravity`/`figure`/`contested_claim` at Steps 3b/3c. Populated as authored, per this build's own CANON_CELLS discipline, not retrofitted.

## Reciprocity and referential integrity

Every relation this step added is reciprocated, re-derived mechanically from the record files rather than read off this list: **36** directed relation ends involving a force record, over **18** distinct pairs, all `associated-with` and correctly symmetric, zero dangling. Seventeen pairs connect a force to a pre-existing gravity, figure, or contested_claim record (`withdrawal` ↔ `martyrdom-unavailable`, `withdrawal` ↔ `village-ascetic-culture`, `spiritual-combat` ↔ `martyrdom-unavailable`, `scriptural-engagement` ↔ `scriptural-address`, `koinonia` ↔ `formation-at-scale`, `figure.pachomius` ↔ `formation-at-scale`, `manual-labor` ↔ `economic-embeddedness-ongoing`, `economic-embeddedness` ↔ `economic-embeddedness-ongoing`, `economic-embeddedness` ↔ `melitian-rivalry`, `contested.strand-porousness` ↔ `melitian-rivalry`, `authority-tension` ↔ `authority-tension-ongoing`, `authority-tension` ↔ `authority-tension-vulnerability`, `evagrian-systematization` ↔ `evagrian-intensification`, `evagrian-systematization` ↔ `origenist-controversy`, `figure.evagrius` ↔ `evagrian-intensification`, `contested.alexandria-continuity` ↔ `origenist-controversy`, `figure.sarah` ↔ `oral-to-written-shift`); one pair is force-to-force (`origenist-controversy` ↔ `authority-tension-vulnerability`, carrying this corpus's own conjunctural-closing synthesis). Full gate battery re-run after every edit in this step: 82 records, 0 non-coverage findings.

## Open items carried forward from Doc_08 (re-derivation basis, not yet resolved by this step)

1. The "white martyrdom" reading (`desert.force.martyrdom-unavailable`) remains without a specific anchoring citation (Doc_01 §11 item 7, still open) — documented under Reported-Experience Status rather than resolved, and the phrase itself is not used in this record's own compiled fields for that reason.
2. Goehring's specific documentary claims underlying `desert.force.economic-embeddedness-ongoing`'s own Layer 2 gap remain independently unverified (Doc_01 §11 item 6; Doc_02 §11 item 4; Doc_04 §8 item 2) — still open, carried at `desert.source.goehring-ascetics`'s own standing rule.
3. The Melitian/Nicene-communion organizational-indistinguishability question (`desert.force.melitian-rivalry`) remains open (Doc_01 §11 item 1; Doc_02 §11 item 5; `desert.contested.strand-porousness`'s own Melitian-identity axis) and bears directly on this force's own Layer 3 limits.
4. Whether the longer imperial-ecclesiastical centralization trend (`desert.force.centralization-trend`) has a directly traceable causal path to Shenoute's later model remains Inferential/Thin and unresolved - flagged, not asserted, matching Doc_01's own explicit exclusion of Shenoute from this world's core scope.
5. The conjunctural (internal-plus-external) synthesis of this world's closing (`desert.force.authority-tension-vulnerability`) is offered as reasoned interpretation, not settled historical fact, and should be tested at a later Validation stage alongside this build's other interpretive claims already flagged across Steps 3b/3c.

## Review rounds note (applied)

*(populated after this step's own adversarial review rounds, per this build's standing discipline)*
