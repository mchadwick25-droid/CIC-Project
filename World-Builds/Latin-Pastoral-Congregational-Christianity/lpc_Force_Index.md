# Force Index — Latin Pastoral-Congregational Christianity

**Status:** **DRAFT — not reviewed, not self-disposed.** Co-output of Construction Step 8 with `Doc_08_Forces_Document.md`; the two are reviewed and disposed of together.
**World file-code:** `lpc` · **Date drafted:** 2026-09-15
**Generated from `Doc_08_Forces_Document.md` by script, not maintained beside it.** Force IDs, names, confidence levels, connected gravities, cross-cell connections and the transmission flags are all parsed out of Doc_08's own prose. **Re-deriving it is the check:** regenerate and diff, and any difference is a real divergence rather than a stale copy. **This file is never hand-edited** — Doc_06's Round 3 found a hand-edited derived index going stale in a way that defeated the very fix that produced it, and the rule is inherited from that finding.
**Format note.** Built in Markdown to match this world's own `Lexicon_Deployment_Index.md`. The `cic-forces-index` standard describes a workbook; **only one of twelve worlds currently carries a Force Index at all**, so there is no settled portfolio practice to match, and Markdown keeps the file diffable in git — which is what the regenerate-and-diff check depends on.

---

## 1. Master Force Table

| Force ID | Cell | Force | Confidence | Connected Gravities | Cross-Cell Connections | Transmission |
|---|---|---|---|---|---|---|
| **1A-1** | Initiating / External | The Decian persecution and the libelli system (250) | Documented | G1, G2, G8 | → 2B-1 (produces); → 2B-2 (produces); ← 2A-1 (reacts to) | no |
| **1A-2** | Initiating / External | The standing legal condition of an unlicensed religion in Romanized provincial North Afr | Widely Accepted | G1 | → 1B-2 (shapes); → 2B-3 (inverts into) | no |
| **1B-1** | Initiating / Internal | An already-organized Carthaginian church capable of sustained collective response | Documented | G2, G3, G5 | → 1B-2 (enables); → 2B-4 (enables) | no |
| **1B-2** | Initiating / Internal | Congregational acclamation overriding a reluctant convert's preference | Documented | G1 | ← 1A-2 (shapes); ← 1B-1 (enables) | no |
| **1B-3** | Initiating / Internal | The inherited Latin theological vocabulary | Widely Accepted | G4 | **none — see §4** | no |
| **2A-1** | Ongoing / External | Recurring persecution after Decius — the Valerianic persecution (257–258) | Documented | G1, G2, G8 | → 1A-1 (reacts to) | no |
| **2A-2** | Ongoing / External | Epidemic disease — the plague of c. 249–262 | Documented | G4 | → *(none)* (—) | no |
| **2A-3** | Ongoing / External | The Donatist schism | Documented | G3, G5, G6 | → 2B-4 (triggers); → 2B-3 (activates) | no |
| **2A-4** | Ongoing / External | Manichaeism and Pelagian anthropology as live rival systems | Documented | G7 | → 3B-1 (produces) | no |
| **2B-1** | Ongoing / Internal | The recurring contest over how to treat the failed member | Documented | G2, G6, G7 | ← 1A-1 (produces); ← 2B-2 (intensifies) | no |
| **2B-2** | Ongoing / Internal | The confessors' claim to grant peace | Documented | G8 | ← 1A-1 (produces); → 2B-1 (intensifies) | no |
| **2B-3** | Ongoing / Internal | The illegal-to-established shift in the office's political capacity | Documented | — | ← 1A-2 (inverts into); ← 2A-3 (activates) | no |
| **2B-4** | Ongoing / Internal | Augustine's engagement with Cyprian's conciliar acts | Documented | G3, G5, G6 | ← 1B-1 (enables); ← 2A-3 (triggers); → 3B-2 (is the sole instance of) | no |
| **2B-5** | Ongoing / Internal | Transmission — survival on the institutionally dominant side, through a 19th-century tra | Documented | — | → 3B-2 (continues) | **YES** |
| **3A-1** | Ending-Transforming / External | The Vandal invasion (from 429) and the siege of Hippo | — | G1 | → 3B-1 (coincides with, does not cause) | no |
| **3B-1** | Ending-Transforming / Internal | The corpus outliving the world | Widely Accepted | G7 | ← 2A-4 (produces); ← 3A-1 (coincides with, does not cause) | no |
| **3B-2** | Ending-Transforming / Internal | Transmission — an asymmetrically attested span and a 133-year silence | Documented | — | ← 2B-4 (is the sole instance of); ← 2B-5 (continues) | **YES** |

**17 forces across six cells** — 1A (2), 1B (3), 2A (4), 2B (5), 3A (1), 3B (2). Every cell is populated.

---

## 2. By Confidence Level

**Documented** — 13: `1A-1`, `1B-1`, `1B-2`, `2A-1`, `2A-2`, `2A-3`, `2A-4`, `2B-1`, `2B-2`, `2B-3`, `2B-4`, `2B-5`, `3B-2`
**Widely Accepted** — 3: `1A-2`, `1B-3`, `3B-1`
**Dominant Modern Reconstruction** — 0: *none*
**Contested** — 0: *none*
**Inferential/Thin** — 0: *none*

**Checkable against Doc_08 §7 rather than asserted there.** No force sits at **Dominant Modern Reconstruction** or **Inferential/Thin** — Doc_08 §7 states why: both phases are anchored in extensive first-person corpora, so no force rests on a modern reconstruction of events the sources do not carry. **2B-3 carries the one Contested element**, and what is contested is its *placement* as internal rather than external, not the fact of it.

---

## 3. By Connected Gravity — the completion check

**This view exists to answer one question at a glance:** does every confirmed gravity from Doc_04 connect to at least one force? A gravity with an empty row is what the template's Section 9 calls ecologically incomplete.

| Gravity | Class | Connected Forces | Count |
|---|---|---|---|
| **G1** — Pastoral Office as Territorial Flock-Keeping | Primary | `1A-1`, `1A-2`, `1B-2`, `2A-1`, `2A-2`, `3A-1` | 6 |
| **G2** — Penitential Discipline | Primary | `1A-1`, `2B-1`, `2B-2` | 3 |
| **G3** — Collegial Communion Preserved Despite Disagreement | Primary | `1B-1`, `2A-3`, `2B-4` | 3 |
| **G4** — Preaching and Catechesis | Supporting | `1B-3`, `2A-2` | 2 |
| **G5** — Conciliar Authority Theory | Supporting | `1B-1`, `2A-3`, `2B-4` | 3 |
| **G6** — Sacramental and Ordination Validity | Primary | `2A-3`, `2B-1`, `2B-4` | 3 |
| **G7** — Grace and Human Incapacity | Supporting | `2A-4`, `3B-1` | 2 |
| **G8** — Confessor-Authority vs. Episcopal-Regulated Peace | Tensional | `1A-1`, `2B-2` | 2 |

**Result: 8 of 8 gravities present, 0 with no connected force.** **All eight connect. The completion requirement is met.**

**The two rows worth reading closely.** **G1** is the most densely connected gravity in the matrix, which matches Doc_05 §9.1's independent finding that it is this ecology's hub. **G5** is the weakest, and Doc_08 §5 states the reason rather than padding the row: every force touching G5 touches it through a third party's citation of a text, not through a pressure on the world's own practice — which carries Doc_04's own incomplete-ecology finding forward rather than resolving it.

---

## 4. Cross-Cell Connection Map

| From | To | Direction | Connection |
|---|---|---|---|
| `1A-1` | `2B-1` | produces | The Decian edict creates the category of the failed member that the ongoing internal contest is about. Without 1A-1 there is no 2B-1. |
| `1A-1` | `2B-2` | produces | The same edict creates confessors as a class with a claim; 2B-2 has no claimants without it. |
| `1A-2` | `1B-2` | shapes | An office with no legal protection is one a sensible man declines, which is why the acclamation pattern has to override reluctance. |
| `1A-2` | `2B-3` | inverts into | The standing condition of illegality is precisely what the illegal-to-established shift removes. The same fact appears at both ends of the matrix with |
| `1B-1` | `1B-2` | enables | A church organized enough to hold factions is organized enough to elect over a faction's opposition. |
| `1B-1` | `2B-4` | enables | Councils that met and left acts are what Augustine later reads and argues with. |
| `2A-1` | `1A-1` | reacts to | The Valerianic persecution repeats the Decian test on a community that has now built a discipline for it. |
| `2A-2` | *(none)* | — | Deliberately isolated. The plague connects to no other force in this matrix and produced teaching rather than structure. Recorded as a connection that |
| `2A-3` | `2B-4` | triggers | The Donatists' appeal to Cyprian's conciliar acts is what prompts Augustine to read them. External prompt, internal act — the placement judgement exam |
| `2A-3` | `2B-3` | activates | A rival communion is what makes the newly available state capacity worth using, and is the occasion of the three-phase coercion development. |
| `2A-4` | `3B-1` | produces | The anti-Pelagian corpus generated by 2A-4 is the largest single component of the inheritance at 3B-1. |
| `2B-2` | `2B-1` | intensifies | The confessors' parallel system is why the internal contest had to be settled by a formal process rather than by episcopal say-so. |
| `2B-4` | `3B-2` | is the sole instance of | 2B-4 is the only mechanism this build has found by which formation logic crosses the 133-year silence recorded at 3B-2. |
| `2B-5` | `3B-2` | continues | The same transmission pattern operates in both cells; 3B-2 is 2B-5's effect on the span rather than on the content. |
| `3A-1` | `3B-1` | coincides with, does not cause | The invasion closes the world; the corpus outlives it. Named as coincidence rather than causation — the inheritance was secured by copying, not by the |

**15 connections**, including **one deliberate non-connection** (`2A-2`, the plague, which produced teaching rather than structure) and **one coincidence explicitly marked as not causal** (`3A-1` → `3B-1`). Recording a connection that does not exist is the Cross-Cell Connection Principle applied, not waived.

---

## 5. Transmission Check

| Required cell | Dedicated transmission force present | Force ID |
|---|---|---|
| **Cell 2B** | **YES** | `2B-5` |
| **Cell 3B** | **YES** | `3B-2` |

**Result: both required entries present as their own forces**, not folded into another entry — which is what the Transmission Specificity Principle requires and what this check exists to catch.

**Layer 2 status of the transmission forces, flagged because it is unusual and deliberate.** Both transmission forces, and `3B-1`, carry **no Layer 2**. Doc_08 §8 states the reason: transmission acted on the record after the world closed, and this world did not know its corpus was becoming an inheritance. **Writing a Layer 2 for either would invent an experience**, so the entries are left unfilled with the reason stated rather than filled at Inferential/Thin.

---

## Disposition

**Not disposed.** Reviewed and disposed of together with `Doc_08_Forces_Document.md` as co-produced Step 8 outputs. Not self-certified. Not Frozen.
