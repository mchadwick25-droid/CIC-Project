# Lexicon Deployment Index — Latin Pastoral-Congregational Christianity

**Status:** **REVISED after Round 1 — not self-disposed.** Co-output of Construction Step 6 with `Doc_06_Full_Lexicon_Development.md` and the nineteen `Lexicon-Chunks/` files; the three are reviewed and disposed of together. See Doc_06's own Disposition.
**World file-code:** `lpc`
**Date drafted:** 2026-09-14 · **Revised:** 2026-09-15 (Round 1 fix pass)
**Generated from the chunk files, not maintained alongside them.** Every row is parsed directly out of `Lexicon-Chunks/lpclex*.md` — Tier, all seven tag columns, Aliases, Related-Terms, the Registry rows cited anywhere in the chunk, and the CT, Reported-Experience and Author-Gravity flags. **Re-deriving it is the check:** regenerate and diff.
**[CORRECTION, 2026-09-15 — Round 1's H1.]** The generator's row-matching pattern captured only the *first* number after *"rows"*, so `lpclex001`'s cell printed *Rows 1, 19* where the chunk cites rows 1, 2, 3, 5 and 19. **That single wrong cell falsified this index's central claim** — an index advertised as safe to diff is worth nothing if the derivation is lossy. The pattern now captures every number in a run, and the flock's cell is the worked proof. Round 1 re-derived all 18×13 cells and found this one and no other.

---

## 1. Master Table

| # | Term | Tier | AS | SC | DR | TC | RT | PV | CT | Aliases | Related-Terms | Source Registry Cross-Reference | Author-Gravity-Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | the flock | 1 | – | Y | Y | – | Y | – | – | flock, shepherd, pastor, the congregation, my people, pastoral office | the lapsed, reconciliation / penitential discipline, confessor, communion, preaching, catechesis, the people, suffrage, bishop of bishops (negated), the one episcopate, schism, compel them to come in, certificates | Rows 1, 2, 3, 5, 19 | **Yes** |
| 02 | the lapsed | 1 | – | Y | Y | – | Y | Y | – | the fallen, those who sacrificed, apostates, the compromised, lapsi | the flock, reconciliation / penitential discipline, confessor, communion, grace, libelli (sacrifice-certificates), libellatici / sacrificati, certificates | Rows 1, 2 | **Yes** |
| 03 | reconciliation / penitential discipline | 1 | – | Y | – | Y | Y | Y | – | penance, penitential process, readmission, restoration to communion, peace, being received back | the flock, the lapsed, confessor, communion, heresy, grace, the people, the one episcopate, libelli (sacrifice-certificates), libellatici / sacrificati, certificates | Rows 1, 2, 7 | **Yes** |
| 04 | confessor | 1 | – | Y | Y | Y | Y | Y | – | confessors, those who confessed under interrogation, survivors of the persecution | the flock, the lapsed, reconciliation / penitential discipline, communion, certificates | Rows 1, 2 | **Yes** |
| 05 | communion | 1 | – | Y | Y | – | Y | – | – | fellowship, being in communion, the right of communion, standing, excommunication (as its negation) | the flock, the lapsed, reconciliation / penitential discipline, confessor, heresy, preaching, catechesis, the people, bishop of bishops (negated), plenary Council, the one episcopate, schism, compel them to come in, certificates | Rows 4, 12, 13 | No |
| 06 | heresy — validity of baptism and ordination outside the church | 1 | – | Y | Y | Y | – | – | – | heresy, rebaptism, validity outside the church, baptism by heretics, the rebaptism controversy | reconciliation / penitential discipline, communion, catechesis, bishop of bishops (negated), plenary Council, the one episcopate, schism, compel them to come in | Rows 1, 3, 4, 13 | No |
| 07 | grace | 1 | – | Y | Y | Y | Y | Y | Y | grace, gratia, prevenient grace, unmerited help, the necessity of grace | the lapsed, reconciliation / penitential discipline, preaching, catechesis, compel them to come in | Rows 23 | **Yes** |
| 08 | preaching | 2 | – | Y | – | – | Y | – | – | preaching, the sermon, the homily, the weekly address | the flock, communion, grace, catechesis, the people | Rows 5, 19, 21 | No |
| 09 | catechesis | 2 | – | Y | – | Y | Y | – | – | catechesis, catechumenate, instruction of catechumens, preparation for baptism, the catechumen | the flock, communion, heresy, grace, preaching | Rows 5, 9, 15, 18 | No |
| 10 | "the people" — the congregation as the consenting, electing body | 2 | – | Y | Y | – | – | – | – | the people, the congregation (as an acting body), the laity, popular acclamation, the crowd | the flock, reconciliation / penitential discipline, communion, preaching, suffrage | Rows 1, 11 | No |
| 11 | "suffrage" — a bishop called to office against his own preference | 2 | Y | – | – | – | – | – | – | suffrage, acclamation, popular election, being seized for office, calling against one's will | the flock, the people, the one episcopate | Rows 1, 7, 11, 192 | No |
| 12 | "bishop of bishops" (negated) — Cyprian's egalitarian conciliar formula | 2 | Y | – | – | Y | – | Y | – | bishop of bishops, no bishop of bishops, proper right of judgment, conciliar equality, Cyprian's conciliar principle | the flock, communion, heresy, plenary Council, the one episcopate | Rows 4 | No |
| 13 | "plenary Council" — Augustine's hierarchical conciliar formula | 2 | – | Y | – | Y | – | Y | – | plenary council, plenary Councils, general council, the authority of councils, correction of earlier councils | communion, heresy, bishop of bishops (negated), the one episcopate | Rows 13 | **Yes** |
| 14 | "the one episcopate" | 2 | Y | – | – | – | – | Y | – | the one episcopate, episcopatus unus est, the undivided office, the college of bishops | the flock, reconciliation / penitential discipline, communion, heresy, suffrage, bishop of bishops (negated), plenary Council, schism | Rows 3 | No |
| 15 | schism | 2 | – | Y | – | Y | – | – | Y | schism, division, separation, breaking communion, rival hierarchy | the flock, communion, heresy, the one episcopate, compel them to come in | Rows 3, 13 | No |
| 16 | "compel them to come in" — Augustine's coercion doctrine | 2 | Y | – | Y | – | – | Y | Y | compel them to come in, coercion, religious compulsion, the parable of the feast, state force against schismatics | the flock, communion, heresy, grace, schism | Rows 12, 43 | **Yes** |
| 17 | *libelli* (sacrifice-certificates) | 2 | Y | – | – | Y | – | Y | – | libellus, libelli, certificate, sacrifice-certificate, certificate of compliance | the lapsed, reconciliation / penitential discipline, libellatici / sacrificati, certificates | Rows 8 | No |
| 18 | *libellatici* / *sacrificati* — the lapsed, two-way | 2 | Y | – | – | Y | – | Y | – | libellatici, sacrificati, the two classes of lapsed, those who bought certificates, those who sacrificed | the lapsed, reconciliation / penitential discipline, libelli (sacrifice-certificates) | Rows 8 | No |
| 19 | "certificates" — the martyrs' and confessors' letters of peace | 2 | – | Y | Y | Y | Y | Y | – | certificate, letters of peace, letter of peace, libellus pacis, the martyrs' letters, a certificate from the confessors | the flock, the lapsed, reconciliation / penitential discipline, confessor, communion, libelli (sacrifice-certificates) | Rows 1 | **Yes** |

**Source Registry Cross-Reference** lists every Registry row cited anywhere in that chunk, including rows named in a caution or a negative disclosure — a row named as *not* relied on still appears, because a reviewer checking provenance needs to reach it.

---

## 2. By Tier

**Tier 1 — Full Entries** (7 of 19) — full ecological treatment.

- `lpclex001_the-flock.md` — the flock
- `lpclex002_the-lapsed.md` — the lapsed
- `lpclex003_reconciliation-penitential-discipline.md` — reconciliation / penitential discipline
- `lpclex004_confessor.md` — confessor
- `lpclex005_communion.md` — communion
- `lpclex006_heresy.md` — heresy — validity of baptism and ordination outside the church
- `lpclex007_grace.md` — grace

**Tier 2 — Standard Entries** (12 of 19) — same structure, compressed depth — per LDF Part III, depth compresses but structure does not fragment.

- `lpclex008_preaching.md` — preaching
- `lpclex009_catechesis.md` — catechesis
- `lpclex010_the-people.md` — "the people" — the congregation as the consenting, electing body
- `lpclex011_suffrage.md` — "suffrage" — a bishop called to office against his own preference
- `lpclex012_bishop-of-bishops.md` — "bishop of bishops" (negated) — Cyprian's egalitarian conciliar formula
- `lpclex013_plenary-council.md` — "plenary Council" — Augustine's hierarchical conciliar formula
- `lpclex014_the-one-episcopate.md` — "the one episcopate"
- `lpclex015_schism.md` — schism
- `lpclex016_compel-them-to-come-in.md` — "compel them to come in" — Augustine's coercion doctrine
- `lpclex017_libelli.md` — *libelli* (sacrifice-certificates)
- `lpclex018_libellatici-sacrificati.md` — *libellatici* / *sacrificati* — the lapsed, two-way
- `lpclex019_certificates-letters-of-peace.md` — "certificates" — the martyrs' and confessors' letters of peace

**Tier 3 — Reference Entries** (0 of 19) — Quick Meaning and a single Distortion Risk pairing only.

- *(none — see the note below)*

**Proportion check.** Tier 1 is 7 of 19. LDF Part III: *"a lexicon in which most entries are Tier 1 should be treated as a signal that tiering discipline has not actually been applied."* Tier 1 is a minority; `Doc_06_Full_Lexicon_Development.md` §2 gives the reasoning for every entry that moved from the tier Doc_03 proposed.

**Why there are no Tier 3 entries, stated rather than left as an absence.** Both former Tier 3 entries — *libelli* and *libellatici / sacrificati* — were reclassified to Tier 2 at Round 1's M1. The template omits Key Sources at Tier 3, and for both entries the source disclosure *is* the justification for how they are treated: one records that its Latin headword is absent from this world's vendored corpus, the other that its whole classification is a 19th-century editorial endnote. LDF Part III's own remedy governs — *"A Tier 3 entry that begins to require these should be reclassified to Tier 2 rather than expanded in place."* **A lexicon with no Tier 3 entries is a result, not a gap:** this world's eighteen-term candidate list, having been generated from gravity-bearing vocabulary, contained nothing genuinely peripheral enough to sit at reference depth.

---

## 3. By Tag

**[AS] Signature Vocabulary** — 6: "suffrage" — a bishop called to office against his own preference; "bishop of bishops" (negated) — Cyprian's egalitarian conciliar formula; "the one episcopate"; "compel them to come in" — Augustine's coercion doctrine; *libelli* (sacrifice-certificates); *libellatici* / *sacrificati* — the lapsed, two-way

**[SC] Shared Vocabulary** — 13: the flock; the lapsed; reconciliation / penitential discipline; confessor; communion; heresy — validity of baptism and ordination outside the church; grace; preaching; catechesis; "the people" — the congregation as the consenting, electing body; "plenary Council" — Augustine's hierarchical conciliar formula; schism; "certificates" — the martyrs' and confessors' letters of peace

**[DR] High Distortion Risk** — 9: the flock; the lapsed; confessor; communion; heresy — validity of baptism and ordination outside the church; grace; "the people" — the congregation as the consenting, electing body; "compel them to come in" — Augustine's coercion doctrine; "certificates" — the martyrs' and confessors' letters of peace

**[TC] Technical Concept** — 11: reconciliation / penitential discipline; confessor; heresy — validity of baptism and ordination outside the church; grace; catechesis; "bishop of bishops" (negated) — Cyprian's egalitarian conciliar formula; "plenary Council" — Augustine's hierarchical conciliar formula; schism; *libelli* (sacrifice-certificates); *libellatici* / *sacrificati* — the lapsed, two-way; "certificates" — the martyrs' and confessors' letters of peace

**[RT] Likely Runtime Term** — 9: the flock; the lapsed; reconciliation / penitential discipline; confessor; communion; grace; preaching; catechesis; "certificates" — the martyrs' and confessors' letters of peace

**[PV] Plural Voices** — 11: the lapsed; reconciliation / penitential discipline; confessor; grace; "bishop of bishops" (negated) — Cyprian's egalitarian conciliar formula; "plenary Council" — Augustine's hierarchical conciliar formula; "the one episcopate"; "compel them to come in" — Augustine's coercion doctrine; *libelli* (sacrifice-certificates); *libellatici* / *sacrificati* — the lapsed, two-way; "certificates" — the martyrs' and confessors' letters of peace

**[CT] Contested Tradition** — 3: grace; schism; "compel them to come in" — Augustine's coercion doctrine

**[RT] is the runtime priority set** (LDF Part V) and **[DR] is the correction set** — each [DR] entry carries a Modern Hearing / World Hearing pairing a Representative can draw on directly when a participant's question reveals the anticipated modern assumption.

---

## 4. CT Contest Type Check Sheet

| Term | CT tagged | CT Contest Type section present | Contest type(s) stated |
|---|---|---|---|
| grace | Yes | **Yes** | Relationship to present-day traditions; secondarily Meaning |
| schism | Yes | **Yes** | Application to this world; secondarily Historical scope |
| "compel them to come in" — Augustine's coercion doctrine | Yes | **Yes** | Relationship to present-day traditions; secondarily Meaning |

**Result: 3 CT-tagged, 3 completed, 0 mismatches.** **Doc_03 assigned [CT] to three terms and stated a contest type for none of them**; supplying the type is Doc_06's own work and is done in all three. Round 1 verified all three as specific and non-templated.

---

## 5. Related-Terms Reciprocity Check

**Result: 122 links across 19 entries — 61 reciprocal pairs, zero one-way.** Verified by re-parsing the chunks from disk after the cross-reference pass, and independently re-verified by Round 1, which parsed all chunks itself rather than reading this claim.

**This check has found real defects twice and both are on the record.** The first pass authored each chunk's list independently and produced **27 one-way or broken links** — the Development Workflow's step 5 cross-reference pass had not been run. Two defects then surfaced *inside* the repair: a matcher that substring-matched into Aliases and reported 35 failures that were not real, and a repair that inserted canonical terms containing commas into a comma-separated field. Related-Terms uses a **comma-free reference handle** for every term, so the field cannot be fragmented by its own contents.

---

## 6. Author-Gravity Cross-Check

| Term | Author-Gravity-Risk | What the chunk's Key Sources actually says |
|---|---|---|
| the flock | **Yes** | dense verbal evidence is Cyprian's; Augustine's use is real but far less frequent |
| the lapsed | **Yes** | the regulating voice throughout is Cyprian's own; no lapsed believer's own account survives |
| reconciliation / penitential discipline | **Yes** | Epistles XX–XXI are the rare non-episcopal voice; the reconciled believer still does not speak |
| confessor | **Yes** | evidence base is essentially one Registry row read through one lexicon entry |
| grace | **Yes** | entire base is one voice within one evidence stream; no Pelagian first-person answer survives |
| "plenary Council" — Augustine's hierarchical conciliar formula | **Yes** | spoken in defence of overturning Cyprian's ruling; institutional interest runs opposite |
| "compel them to come in" — Augustine's coercion doctrine | **Yes** | known only through Augustine's own advocacy, in his own defence |
| "certificates" — the martyrs' and confessors' letters of peace | **Yes** | the confessors' own certificates do not survive; Cyprian quotes and objects to them |

**8 of 19 entries carry an Author Gravity note.** The column is derived from the presence of that note in each chunk, so it cannot disagree with the chunk. Round 1 verified every Yes and every No against the chunks.

---

## 7. Editorial-Apparatus Register

**Six entries rest near 19th-century editorial matter printed inside or beside the primary text, and each names it rather than absorbing it.** Doc_05 §11 item 11 found the problem is corpus-wide and routed it to the project lead; this register is the local instance list.

| Entry | The editorial matter | Why it matters |
|---|---|---|
| the flock | *"[This exercise of jurisdiction, vice episcopi, is to be noted.]"* inside Cyprian's watch-keeping sentence | an editor's gloss on the office, inside the quoted sentence |
| bishop of bishops (negated) | *"Of course this implies a rebuke to the assumption of Stephen…"* inside the 256 preface | a substantive claim about Cyprian's **motive** |
| the people | the only three occurrences of *plebs* in the vendored Cyprian corpus are in the editor's prose | the term is therefore **not** a headword |
| compel them to come in | the volume's own preface calls the doctrine *"a false exegesis"* and *"least satisfactory to Protestant readers"* | a 19th-century Protestant editor's **theological verdict** |
| libellatici / sacrificati | the entire two-way classification is an editorial endnote on a different, Confidence-C text | disclosed as editorial throughout |
| **the lapsed** *(added 2026-09-15, Round 1's H3)* | that same two-way classification, narrated as flat fact in a **Tier 1 World Meaning** | **the register listed five and missed this one**; Doc_05 had flagged the identical sentence and the chunk dropped the flag |

**The sixth entry is the one worth dwelling on.** It was not a new bleed-through but a **regression**: the upstream document had caught it, marked it, and the lexicon chunk un-marked it. A register that lists only the instances its author remembered is not a control.

---

## 8. Cross-Build Sheet

**Phase attribution**, carried from Doc_03 and confirmed against Doc_05 §7's phase table.

- **Cyprian-phase only:** the lapsed; reconciliation / penitential discipline; confessor; certificates (letters of peace); *libelli*; *libellatici* / *sacrificati*; bishop of bishops (negated); the one episcopate
- **Augustine-phase only:** grace; plenary Council; compel them to come in
- **Cross-phase:** the flock; preaching; catechesis; the people; suffrage; communion; heresy; schism

**`suffrage` is cross-phase and its tagging now agrees with that.** Round 1's H2 found the chunk carrying **[PV]**, which Doc_03 rules out by name — *"it does not sit on 'suffrage,' which is a cross-phase pattern rather than a single-phase term"* — and which contradicted this very sheet. The tag is removed.

**`confessor`'s phase bound was established by a check, not assumed:** twenty stem occurrences across all eight vendored Augustine volumes against roughly 150 in Cyprian's one, none in this sense (Doc_05 §2.3).

---

## Disposition

**Not disposed.** Reviewed and disposed of together with `Doc_06_Full_Lexicon_Development.md` and the nineteen chunk files as co-produced Step 6 outputs. `Review-Artifacts/Doc06_Round1_Review.md` returned **REVISION REQUIRED** (3H 3M 2L); all applied. Not self-certified. Not Frozen.
