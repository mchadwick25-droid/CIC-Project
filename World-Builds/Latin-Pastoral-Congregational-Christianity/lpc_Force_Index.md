# Force Index — Latin Pastoral-Congregational Christianity

**Status:** **REVISED after Round 1 — not reviewed, not self-disposed.** Co-output of Construction Step 8 with `Doc_08_Forces_Document.md`; reviewed and disposed of together.
**World file-code:** `lpc` · **Drafted:** 2026-09-15 · **Revised:** 2026-09-15 (Round 1 fix pass)
**Generated from `Doc_08_Forces_Document.md` by `gen_force_index.py`. Never hand-edited. Re-running the generator is the check.**

**[CORRECTED, 2026-09-15 — Round 1's H1.] The previous generator was wrong in three ways and its "cannot drift" claim was false.** It **derived the gravity relation twice from two different sources** — the master table from tokens in each force's prose, the by-gravity view from §5's lists — so the two disagreed about **G4**, whose §5 entry says *"every force in Cell 2A"* in prose the token-scanner could not see. Its confidence pattern was terminated by `**` and so **silently dropped `3A-1`**, whose line ends *"Documented."*, leaving totals that summed to 16 of 17. And it reported **Contested — 0** two lines from prose naming a Contested element.
**The fix is structural, not three patches.** Every relation now has **exactly one derivation**: gravity connections are read from §5 alone and inverted once for the master table, so the two views cannot disagree by construction; confidence is matched terminator-insensitively and an unmatched force is reported as `UNCLASSIFIED` rather than vanishing; and prose set-references like *"every force in Cell 2A"* are expanded rather than ignored. **A derived index that computes the same relation twice is not derived — it is two indexes that happen to agree until they do not.**

**[CORRECTED, 2026-09-15 — Round 1's M4, and one further defect the rewrite exposed.]** The previous index also had **`1B-3` and `2A-2` the wrong way round in the Cross-Cell column**: it sent a reader to §4 for `1B-3`, which has no §4 row at all, and printed a bare *(none)* for `2A-2`, the one force whose absence of connections §4 argues for at length. **`2A-2`'s isolation is a finding; `1B-3`'s is an unexamined blank**, and the two now read differently. `1B-3` is the only force in the matrix that §4 neither connects nor deliberately isolates — carried as an open observation for review, not resolved here.

**[CORRECTED, 2026-09-15 — Round 1's M4.]** The previous generator also **truncated the Force column at a fixed 88 characters and the Connection column at 150**, cutting two Force names and three connection descriptions off mid-word with no ellipsis — so the Index's two longest entries, both of them transmission-related, were the two a reader could not read. **No column is width-limited now.** The cells below carry the source document's full wording.

---

## 1. Master Force Table

| Force ID | Cell | Force | Confidence | Connected Gravities | Cross-Cell Connections | Layer 2 | Transmission |
|---|---|---|---|---|---|---|---|
| **1A-1** | Initiating / External | The Decian persecution and the libelli system (250) | Documented | G1, G2, G8 | → 2B-1 (produces); → 2B-2 (produces); ← 2A-1 (reacts to) | ✓ | no |
| **1A-2** | Initiating / External | The standing legal condition of an unlicensed religion in Romanized provincial North Africa | Widely Accepted | G1 | → 1B-2 (shapes); → 2B-3 (inverts into) | ✓ | no |
| **1B-1** | Initiating / Internal | An already-organized Carthaginian church capable of sustained collective response | Documented | G3, G5 | → 1B-2 (enables); → 2B-4 (enables) | ✓ | no |
| **1B-2** | Initiating / Internal | Congregational acclamation overriding a reluctant convert's preference | Documented | G1 | ← 1A-2 (shapes); ← 1B-1 (enables) | ✓ | no |
| **1B-3** | Initiating / Internal | The inherited Latin theological vocabulary | Widely Accepted | G4 | *(no §4 row)* | ✓ | no |
| **2A-1** | Ongoing / External | Recurring persecution after Decius — the Valerianic persecution (257–258) | Documented | G1, G4 | → 1A-1 (reacts to) | ✓ | no |
| **2A-2** | Ongoing / External | Epidemic disease — the plague of c. 249–262 | Documented | G1, G4 | **none — see §4** | ✓ | no |
| **2A-3** | Ongoing / External | The Donatist schism | Documented | G3, G4, G5, G6 | → 2B-4 (triggers); → 2B-3 (activates) | ✓ | no |
| **2A-4** | Ongoing / External | Manichaeism and Pelagian anthropology as live rival systems | Documented | G4, G7 | → 3B-1 (produces) | ✓ | no |
| **2B-1** | Ongoing / Internal | The recurring contest over how to treat the failed member | Documented | G2, G6 | ← 1A-1 (produces); ← 2B-2 (intensifies) | ✓ | no |
| **2B-2** | Ongoing / Internal | The confessors' claim to grant peace | Documented | G2, G8 | ← 1A-1 (produces); → 2B-1 (intensifies) | ✓ | no |
| **2B-3** | Ongoing / Internal | The illegal-to-established shift in the office's political capacity | Documented *(+Contested)* | — | ← 1A-2 (inverts into); ← 2A-3 (activates) | ✓ | no |
| **2B-4** | Ongoing / Internal | Augustine's engagement with Cyprian's conciliar acts | Documented | G3, G5, G6 | ← 1B-1 (enables); ← 2A-3 (triggers); → 3B-2 (is the sole instance of) | ✓ | no |
| **2B-5** | Ongoing / Internal | Transmission — survival on the institutionally dominant side, through a 19th-century translation apparatus | Documented | — | → 3B-2 (continues) | ✓ | **YES** |
| **3A-1** | Ending-Transforming / External | The Vandal invasion (from 429) and the siege of Hippo | Documented | G1 | → 3B-1 (coincides with, does not cause) | ✓ | no |
| **3B-1** | Ending-Transforming / Internal | The corpus outliving the world | Widely Accepted | G7 | ← 2A-4 (produces); ← 3A-1 (coincides with, does not cause) | ✓ | no |
| **3B-2** | Ending-Transforming / Internal | Transmission — an asymmetrically attested span and a 133-year silence | Documented | — | ← 2B-4 (is the sole instance of); ← 2B-5 (continues) | ✓ | **YES** |

**17 forces** — 1A (2), 1B (3), 2A (4), 2B (5), 3A (1), 3B (2). Every cell populated; **every force carries a written Layer 2**.

---

## 2. By Confidence Level

**Documented** — 14: `1A-1`, `1B-1`, `1B-2`, `2A-1`, `2A-2`, `2A-3`, `2A-4`, `2B-1`, `2B-2`, `2B-3`, `2B-4`, `2B-5`, `3A-1`, `3B-2`
**Widely Accepted** — 3: `1A-2`, `1B-3`, `3B-1`
**Dominant Modern Reconstruction** — 0: *none*
**Contested** — 0: *none*  ·  *carried as a secondary element by:* `2B-3`
**Inferential/Thin** — 0: *none*

**Totals reconcile: 17 classified + 0 unclassified = 17 forces.** That arithmetic is printed because Round 1 found the previous version silently summing to 16. **`2B-3` carries `Contested` as a secondary element** — its external change is Documented; what is contested is the placement of its consequence as internal, and the force entry now says so rather than only §7's summary.

---

## 3. By Connected Gravity — the completion check

**One question, answered at a glance:** does every confirmed gravity from Doc_04 connect to at least one force? An empty row is what the template's §9 calls ecologically incomplete.

**Notation.** `G1`–`G8` are this document's short labels for Doc_04's **Candidate 1**–**Candidate 8**, in Doc_04's own order and with Doc_04's own classifications. Doc_04 uses the "Candidate *n*" form throughout; the correspondence is one-to-one.

| Gravity | Class | Connected Forces | Count | Derivation |
|---|---|---|---|---|
| **G1** — Pastoral Office as Territorial Flock-Keeping | Primary | `1A-1`, `1A-2`, `1B-2`, `2A-1`, `2A-2`, `3A-1` | 6 | §5 list |
| **G2** — Penitential Discipline | Primary | `1A-1`, `2B-1`, `2B-2` | 3 | §5 list |
| **G3** — Collegial Communion Preserved Despite Disagreement | Primary | `1B-1`, `2A-3`, `2B-4` | 3 | §5 list |
| **G4** — Preaching and Catechesis | Supporting | `1B-3`, `2A-1`, `2A-2`, `2A-3`, `2A-4` | 5 | §5 list + prose set-reference expanded |
| **G5** — Conciliar Authority Theory | Supporting | `1B-1`, `2A-3`, `2B-4` | 3 | §5 list |
| **G6** — Sacramental and Ordination Validity | Primary | `2A-3`, `2B-1`, `2B-4` | 3 | §5 list |
| **G7** — Grace and Human Incapacity | Supporting | `2A-4`, `3B-1` | 2 | §5 list |
| **G8** — Confessor-Authority vs. Episcopal-Regulated Peace | Tensional | `1A-1`, `2B-2` | 2 | §5 list |

**Result: all 8 gravities connect; 0 empty rows. The completion requirement is met.**

**`G4`'s row is the one Round 1 caught.** Doc_08 §5 connects it to *"1B-3, 2A-2, and in truth every force in Cell 2A"*; the previous index listed two. **The set-reference is now expanded**, which is why G4 shows five forces — and it matters, because G4 is the channel through which every external pressure reaches an ordinary believer, so a two-force row understated the one mechanism Doc_08 §5 calls this world's characteristic response.

---

## 4. Cross-Cell Connection Map

| From | To | Direction | Connection |
|---|---|---|---|
| `1A-1` | `2B-1` | produces | The Decian edict creates the category of the failed member that the ongoing internal contest is about. Without 1A-1 there is no 2B-1. |
| `1A-1` | `2B-2` | produces | The same edict creates confessors as a class with a claim; 2B-2 has no claimants without it. |
| `1A-2` | `1B-2` | shapes | An office with no legal protection is one a sensible man declines, which is why the acclamation pattern has to override reluctance. |
| `1A-2` | `2B-3` | inverts into | The standing condition of illegality is precisely what the illegal-to-established shift removes. The same fact appears at both ends of the matrix with opposite sign. |
| `1B-1` | `1B-2` | enables | A church organized enough to hold factions is organized enough to elect over a faction's opposition. |
| `1B-1` | `2B-4` | enables | Councils that met and left acts are what Augustine later reads and argues with. |
| `2A-1` | `1A-1` | reacts to | The Valerianic persecution repeats the Decian test on a community that has now built a discipline for it. |
| `2A-2` | *(none)* | — | Deliberately isolated. The plague connects to no other force in this matrix and produced teaching rather than structure. Recorded as a connection that does not exist, per the Named-Tension and Cross-Cell principles. |
| `2A-3` | `2B-4` | triggers | The Donatists' appeal to Cyprian's conciliar acts is what prompts Augustine to read them. External prompt, internal act — the placement judgement examined at 2B-4. |
| `2A-3` | `2B-3` | activates | A rival communion is what makes the newly available state capacity worth using, and is the occasion of the three-phase coercion development. |
| `2A-4` | `3B-1` | produces | The anti-Pelagian corpus generated by 2A-4 is the largest single component of the inheritance at 3B-1. |
| `2B-2` | `2B-1` | intensifies | The confessors' parallel system is why the internal contest had to be settled by a formal process rather than by episcopal say-so. |
| `2B-4` | `3B-2` | is the sole instance of | 2B-4 is the only mechanism this build has found by which formation logic crosses the 133-year silence recorded at 3B-2. |
| `2B-5` | `3B-2` | continues | The same transmission pattern operates in both cells; 3B-2 is 2B-5's effect on the span rather than on the content. |
| `3A-1` | `3B-1` | coincides with, does not cause | The invasion closes the world; the corpus outlives it. Named as coincidence rather than causation — the inheritance was secured by copying, not by the siege. |

**15 connections**, including **1 deliberate non-connection** (`2A-2`) and **one coincidence marked as not causal** (`3A-1` → `3B-1`).

---

## 5. Transmission and Layer-2 Check

| Check | Result |
|---|---|
| Dedicated transmission force in Cell 2B | **YES** — `2B-5` |
| Dedicated transmission force in Cell 3B | **YES** — `3B-2` |
| Every force carries a written Layer 2 | **YES** — all 17 |

**[CORRECTED, 2026-09-15 — Round 1's H4.]** Three Layer 2 entries were previously unwritten, and the omission was certified in Doc_08 §8 as the From-Within Principle applied *"with three stated exceptions."* **The Forces Framework permits none: *"This is not optional. All three layers are required for every force."*** All three are now written — from this world's **own attested transmission-consciousness**, which was available in the vendored sources the whole time: Cyprian directing that his letters be copied and forwarded, assembling a thirteen-letter dossier, and returning a suspect letter for collation because the paper itself suggested it had been altered; Augustine revising his entire corpus in the *Retractationes*. **This column exists so that a blank Layer 2 can never again be reported as a principle.**

---

## Disposition

**Not disposed.** Reviewed and disposed of together with `Doc_08_Forces_Document.md`. `Review-Artifacts/Doc08_Round1_Review.md` returned **SUBSTANTIAL REVISION REQUIRED** (4H 5M 3L 1C); this is the fix pass. Not self-certified. Not Frozen.
