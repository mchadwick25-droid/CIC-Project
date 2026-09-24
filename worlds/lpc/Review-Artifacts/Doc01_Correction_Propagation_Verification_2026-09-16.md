# Doc_01 §2 Correction — Independent Propagation Verification

## Latin Pastoral-Congregational Christianity (`lpc`)

*Independent verification, not an Article 31 substitute. Commissioned by the project lead's ruling of 2026-09-16, whose second limb requires the propagation to be verified by a thread that did not apply it.*

**Correction under verification:** commit `bf0e0d5f`, "lpc: apply the project lead's 2026-09-16 ruling on Doc_01 §2 across the build". Eight files, 25 insertions, 14 deletions.
**Build state verified:** working tree at `bf0e0d5f`, clean, no uncommitted changes in the build folder.
**Verifier:** isolated pass. **I did not apply the correction, did not write the escalation, did not write `Possidius_Full_Read_2026-09-16.md`, and did not read the applying thread's diff until after I had established the source claim myself.**

---

# VERDICT: **NOT VERIFIED**

**4 HIGH · 4 MEDIUM · 6 LOW.**

**The source claim is confirmed.** Possidius *Vita Augustini* ch. VIII says what the build now says it says. Item 1 below establishes that independently, from the body text, in both languages. The correction rests on a real finding and it is the right finding. Nothing here questions the ruling.

**The propagation is incomplete.** The claim the ruling ordered removed is **still stated, uncorrected, at six sites inside four of the eight files the correction touched** — including the origin document `Doc_01` §2 itself, and including the participant-facing body of `Lexicon-Chunks/lpclex011_suffrage.md`. In each of the four the corrected sentence and the uncorrected sentence now sit in the same paragraph, table row, force entry or chunk, saying opposite things. The correction went to one instance per file and stopped.

**Eight files is the right count. Eight corrections is not.** My sweep found no ninth *file*. It found six further *sites* inside files already on the list. The escalation's failure mode was "which files carry it"; the application's failure mode was "how many times does this file say it". The second sweep fixed the first and did not run the second.

**Article 21 is not disturbed.** I agree with the Decision Log on the substance, and say so at item 5. I record one governance observation adjacent to it that the Decision Log does not make.

---

## Method

I established the source before reading anything the build wrote about it.

`possidius_vita-augustini_weiskotten1919.txt` is a bilingual critical edition: Weiskotten's revised Latin and his English alternate by page and both hyphenate across line breaks. I built a de-hyphenated, whitespace-collapsed stream before searching; searching the raw file returns false negatives on every phrase crossing a line.

I bounded Possidius's voice by line number before quoting: the body runs from `PREFACE` at **line 1518** to the `NOTES` heading at **line 5063**. Weiskotten's ~40-page Introduction (lines 122–1517), his apparatus criticus and his endnotes (5063 onward) are outside it. **Every Possidius quotation below is from inside that span, with the facing Latin checked.** Nothing is taken from the Introduction — the trap this build has hit before.

For the Cyprian corpus I resolved works by `title=` on `<div3>`, never by position, and marked and removed `<note>` spans before stripping tags. Epistle XXXIX resolves at offset 2439639 of `anf05_hippolytus-cyprian-caius-novatian.xml`, title `To the People, Concerning Five Schismatic Presbyters of the Faction of Felicissimus.`, 16 note spans removed. The Latin is from `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`, de-hyphenated.

For the sweep I searched every `*.md` in the build folder — all `Doc_*`, `Step0_*`, `Source_*`, `lpc_*`, `Doc09_Claims_Register.md`, `Lexicon_Deployment_Index.md`, both chunk folders and `Review-Artifacts/` — on twenty-one formulations, listed at item 2.

I ran `scripts/check_claims.py` rather than trusting the commit message's report of it.

---

# 1. The source claim, established independently

**Confirmed on all three limbs. The build's reading of ch. VIII is correct, and the Latin supports the English.**

## Chapter VIII — the episcopate

The English body text (`LIFE OF SAINT AUGUSTINE 57`):

> "Later on, accordingly, when Megalius, Bishop of Calama, and at that time primate of Numidia, had come at his request to visit the church at Hippo, unexpectedly to all the bishop Valerius made his desire known to the bishops who happened at that time to be present, and to all the clergy of Hippo and to all the people. But while all who heard rejoiced and clamored most elageriy that this should be done and accomplished, the presbyter refused to accept the episcopate contrary to the custom of the Church, since his bishop was still living. However, when they had convinced him that this was generally done and had appealed to examples from the churches across the sea as well as in Africa, though he had been ignorant of it before, under compulsion and constraint he yielded and accepted the ordination to the higher office."

`elageriy` is the scan's corruption of *eagerly*; the facing Latin confirms it. The Latin (`58 SANCTI AUGUSTINI VITA`, de-hyphenated):

> "Valerio antistite, episcopis qui forte tunc aderant, et clericis omnibus Hipponensibus, et universae plebi inopinatam cunctis suam insinuavit voluntatem: omnibusque audientibus gratulantibus, atque id fieri perficique ingenti desiderio clamantibus, episcopatum suscipere contra morem Ecclesiae suo vivente episcopo presbyter recusabat. Dumque illi fieri solere ab omnibus suaderetur, atque id ignaro transmarinis et Africanis Ecclesiae exemplis provocaretur, compulsus atque coactus succubuit et maioris loci ordinationem suscepit."

The chapter heading is `Designatur episcopus vivo Valerio et a Megalio primate ordinatur`.

| Limb the brief asks about | Found | At |
|---|---|---|
| Announcement to the people | **Yes** | `universae plebi… insinuavit voluntatem` / "and to all the people" |
| Popular clamour | **Yes, with a qualification (item 3, MED-3)** | `omnibusque audientibus… ingenti desiderio clamantibus` / "all who heard… clamored" |
| Augustine's refusal | **Yes** | `presbyter recusabat` / "the presbyter refused to accept the episcopate" |
| Yielding under compulsion | **Yes** | `compulsus atque coactus succubuit` / "under compulsion and constraint he yielded" |
| At the **episcopate** | **Yes** | `episcopatum suscipere`; `maioris loci ordinationem suscepit` |

## Chapter IV — the presbyterate

> "But owing to the increasing demands of ecclesiastical duty he addressed the people of God and exhorted them to provide and ordain a presbyter for the city. The Catholics, already acquainted with the life and teaching of the holy Augustine, laid hands on him — for he was standing there among the people secure and unaware of what was about to happen… So they laid hands on him and, as is the custom in such cases, brought him to the bishop to be ordained, for all with common consent desired that this should be done and accomplished ; ancf they demanded it with great zeal and clamor, while he wept freely."

Latin: `plebem Dei alloqueretur et exhortaretur… manu iniecta… eum ergo tenuerunt et, ut in talibus consuetum est, episcopo ordinandum intulerunt, omnibus id uno consensu et desiderio fieri perficique petentibus, magnoque studio et clamore flagitantibus, ubertim eo flente`. Heading: `Capitur ad presbyterii gradum`. Closing: `Et eorum ut voluerunt completum est desiderium.`

**The same shape, with one honest difference the build should know about.** Ch. IV has the announcement, the clamour and the compulsion (`manu iniecta`, `tenuerunt`, *capitur*), but the reluctance is **tears, not a refusal** — there is no `recusabat` and no `compulsus atque coactus` at the presbyterate. Ch. VIII is the chapter with the explicit verbal refusal. The two are the same pattern; they are not the same wording, and no corrected file claims they are.

## What this settles

`Doc_01` §2's pre-correction finding — that the pattern "recurs at the episcopate for Cyprian and at the presbyterate for Augustine, **not at the same office for both**" — is **refuted by ch. VIII in terms**. The escalation, the Possidius read and the ruling are all correct on the substance. The finding does not fail on its source. It fails on its propagation.

## The residual caution, checked at source (Doc_03's "different words")

Cyprian, Ep. XXXIX §1, notes stripped:

> "retaining that ancient venom against my episcopate, that is, against your suffrage and God's judgment"

Hartel: `antiqua illa contra episcopatum meum immo contra suffragium uestrum et Dei iudicium uenena retinentes` — one occurrence of `suffragium uestrum` in the whole Cyprian corpus.

Against Possidius: **`suffrag*` occurs once in the entire body of the *Vita*, and it is `suffragatori` at ch. XXVII (`Et ne militiae commendatus ac male agens eius culpa suffragatori tribueretur`), about a patron blamed for the conduct of the man he recommended for military service — not the electoral sense.** `acclamat*` occurs **zero** times. Possidius's vocabulary is `clamantibus`, `clamore flagitantibus`, `petentibus`, `ingenti desiderio`.

**Doc_03's residual caution — "different figures and different words, not one term" — is TRUE and is correctly retained.** Cyprian has a technical term; Possidius has untechnical description; they share no word. The narrowing to the offices limb alone is the right narrowing.

---

# 2. The sweep

Twenty-one formulations, whole build folder, `*.md`, case-insensitive: `same office`, `different office`, `offices`, `second acclamation`, `second popular acclamation`, `presbyterate for Augustine`, `episcopate for Cyprian`, `not one term`, `different figures`, `settled office`, `one recurring office`, `different mechanism`, `not at the same`, `second phase at a different`, `loose resemblance`, `two resemblances`, `Megalius`, `acclamation`, `importunity`, `coadjutor`, `entry into clerical office`, `not identically`, `differently worded`, `persuaded him`, `mechanism that appointed`, `reluctant convert`, `against his wishes`, `against his own wishes`.

**No ninth file.** `Doc_02`, `Doc_04`, `Doc_06`, `Doc_09`, `Step0_*`, `Source_Registry.md`, `Source_Acquisition_Manifest.md`, `Doc09_Claims_Register.md`, `lpc_Force_Index.md`, `lpc_Story_Index.md`, `Lexicon_Deployment_Index.md`, all seven `Story-Chunks/` and the other eighteen `Lexicon-Chunks/` were checked and **none carries the claim**. The hits in `Doc_04` ("*other* holders of the same office") and `lpclex004_confessor.md` ("a different office entirely" — a priest who hears confession) are unrelated false positives, checked in context.

`Review-Artifacts/` hits are historical review records of the pre-correction state and are correctly left alone; a review artifact records what was true when it was written.

**Six uncorrected sites, all inside files the correction already touched.** They are the four HIGH findings at item 3.

One near-miss recorded rather than left unstated: `Doc_02_Source_Ecology.md` line 17 restates Augustine's path as "presbyter in 391 'against his own wishes,' by congregational seizure, and bishop in 395/396 by Valerius's own designation as coadjutor and Megalius's consecration". That is scoped explicitly to what Registry row 11 (Letters XXXI, CCXIII) attests, asserts nothing about offices, and denies nothing. **Not a carrier.** I would not correct it.

---

# 3. File-by-file table

| # | File | Carried the claim | Corrected | Correction right | Finding |
|---|---|---|---|---|---|
| 1 | `Doc_01_World_Identification_Boundaries_Orientation.md` §2 | Yes (origin) | **Partly** | New clause true; **old claim left standing in the same block** | **HIGH-1**, LOW-1 |
| 2 | `Doc_01_…Orientation.md` §5 | Restates the refuted picture; asserts Possidius "not vendored" | **No** | — | **MED-2** |
| 3 | `Doc_03_Lexicon_Candidate_List.md` row 29 ("the people") | Yes | Yes | **Right** | — |
| 4 | `Doc_03_Lexicon_Candidate_List.md` row 30 ("suffrage") | Yes, at four cells | **One cell of four** | Corrected cell true; **three cells still assert the refuted claim** | **HIGH-2**, LOW-6 |
| 5 | `Doc_03_Lexicon_Candidate_List.md` §phase-attribution | Yes | Yes | **Right** | — |
| 6 | `Doc_05_Ecological_Reconstruction.md` §4.1 | Yes, both limbs | Yes | **Right — the most careful of the eight** | — |
| 7 | `Doc_07_Integrated_Ecology_Analysis.md` §2F | Yes | Yes | True but **overstated**; citation doubled | **MED-4**, LOW-2 |
| 8 | `Doc_08_Forces_Document.md` Force 1B-2, Layer 3 | Yes | Yes | Right | — |
| 9 | `Doc_08_Forces_Document.md` Force 1B-2, Layer 1 | Yes | **No** | **Contradicts Layer 3 in the same force entry** | **HIGH-3**, LOW-3 |
| 10 | `Lexicon-Chunks/lpclex011_suffrage.md` — Caution | Yes | Yes | Right | — |
| 11 | `Lexicon-Chunks/lpclex011_suffrage.md` — **World Meaning** | Yes | **No** | **Participant-facing text still deploys the refuted claim** | **HIGH-4** |
| 12 | `Lexicon-Chunks/lpclex011_suffrage.md` — Key Sources | Says Possidius unread and "nothing here rests on it" | **No** | **False on both counts after the correction** | **MED-1** |
| 13 | `lpc_World_Profile.md` §4F (×2), §5, §6, §7 | Yes | Yes | **Right** | LOW-4, LOW-5 |
| 14 | `lpc_World_Profile.md` §11 item 4 and Disposition | Bookkeeping | Yes | Counts inconsistent within one paragraph | LOW-4 |

---

# 4. Findings

## HIGH-1 — `Doc_01` §2 still asserts the refuted claim, three clauses before correcting it

The origin document's corrected sentence reads, in full, from line 26:

> "…his own later rise to the *episcopate*, in 395/396, came by a different mechanism entirely — Valerius's own designation as coadjutor and consecration by Megalius, primate of Numidia (…) — **not a second popular acclamation.** The recurring element is congregational demand overriding an initially reluctant convert's own preference at the point of entry into clerical office, and **it recurs at the episcopate for both men** — [Possidius ch. VIII, quoted] — and at the presbyterate for Augustine in addition (*Vita* ch. IV). **The consecration by Megalius and the acclamation are not alternatives**: the *Vita* records both at the same event."

**"not a second popular acclamation" is the refuted claim.** It is the same assertion as "not at the same office for both," stated in the mechanism register instead of the office register, and it is exactly the formulation the applying thread *did* recognise and remove from `Doc_05` §4.1 ("both limbs, including 'not by a second acclamation'", per the commit message). It was removed there and left here, in the document the correction exists to fix.

It is not merely stale, it is **actively contradicted 40 words later by the same paragraph**, which now says the consecration and the acclamation "are not alternatives: the *Vita* records both at the same event." A reader of `Doc_01` §2 is told both that there was no second popular acclamation and that there was.

**This is a carrier the ruling ordered removed, surviving in the origin document.** Everything downstream cites `Doc_01` §2 as the authority for the correction.

## HIGH-2 — `Doc_03` row 30 corrects one cell of four and leaves three asserting the opposite

Row 30, the `"suffrage"` candidate, is a seven-cell table row. The **Deployment** cell was corrected and now reads "attested at the same office in both phases (Possidius, *Vita* ch. VIII…), though still through different figures and different words, not one term." Correct.

The other three cells were not touched:

- **Notes cell:** "Cross-phase pattern, differently worded and **attached to different offices each time** — named as such rather than smoothed into one recurring word or **one recurring office**"
- **Significance cell, opening:** "Doc_01 §2 states plainly that the congregational-demand pattern *'recurs at the presbyterate for Augustine and the episcopate for Cyprian, not at the same office,'* and Augustine's own rise to the episcopate itself came by a different mechanism — Valerius's own designation and Megalius's consecration — *'not a second popular acclamation.'*"
- **Significance cell, closing:** "What remains true: no single fixed vocabulary term recurs verbatim across both instances, and **the two instances are not the same office** … Doc_06 should not present this as one settled term, **or one settled office**, without carrying that caution forward"

Three distinct failures in one row. The Notes cell is an independent statement of the claim. The Significance opening is **a verbatim quotation of `Doc_01` §2's pre-correction wording, left standing after `Doc_01` §2 changed** — the identical defect the applying thread caught in the World Profile and fixed there. The Significance closing asserts the refuted claim as *what remains true after weighing Possidius*, and instructs `Doc_06` to carry it forward.

`Doc_03`'s residual caution on *different words* is sound (item 1). **These three cells are not that caution.** They are the offices limb, which the ruling narrowed away.

## HIGH-3 — `Doc_08` Force 1B-2 contradicts itself across two layers

Layer 3 was corrected. **Layer 1, six lines above it, was not:**

> "**Layer 1 — Historical Event.** … **The pattern recurs in the second phase at a different office:** Augustine was seized into the **presbyterate** at Hippo in 391 against his wishes. **Confidence: Documented** — Epistle XXXIX (row 1); Pontius (row 7, Confidence A); Doc_01 §2."

> "**Layer 3 — Formation Impact.** … the pattern is attested through different figures and different words, not one recurring term — **but at the same office in both phases**…"

Layer 1 says "at a different office"; Layer 3 says "at the same office in both phases". Layer 1 cites `Doc_01` §2 as its authority for a reading `Doc_01` §2 no longer holds. Layer 1 also carries the force's **Confidence: Documented** rating, which is the line a downstream reader checks.

## HIGH-4 — `lpclex011_suffrage.md` still deploys the refuted claim to participants

The brief asks whether this chunk is fit to deploy. **It is not.**

The correction was applied to the **Key Sources → Caution** block at the foot of the file — builder-facing apparatus. The **World Meaning** section, which is the body the Representative draws on, was not touched and still reads:

> "The pattern recurs in the second phase but not identically, and the difference is kept rather than smoothed: Augustine was seized into the **presbyterate** at Hippo against his wishes; **his *episcopate* came by his predecessor's designation and a consecration, with the people one of two things that persuaded him rather than the mechanism that appointed him.**"

That is the refuted claim in its strongest form — it does not merely omit the episcopal clamour, it **expressly denies that the people were the mechanism**. Possidius ch. VIII records the announcement made to all the people, their clamour, the refusal and the compulsion at that same event.

The corrected Caution is four paragraphs below it and says the opposite. **The chunk deploys the wrong half.** A participant asking "did anyone want these jobs?" — the chunk's own `Retrieve-When` trigger — gets the pre-correction answer.

**Do not deploy this chunk as it stands.**

## MED-1 — `lpclex011` Key Sources is false after the correction, in the same file as the correction

> "Possidius's *Vita* (row 192) is vendored but, per Doc_02 §2 and §4, **has not been read in this build beyond one identification**, and **nothing here rests on it**."

Both clauses are now false. The whole *Vita* was read on 2026-09-16 (`Possidius_Full_Read_2026-09-16.md`, thirty-one chapters), and the corrected Caution **in this same file, two paragraphs below, rests on ch. VIII and ch. IV by name**. Collateral damage created by the correction itself.

## MED-2 — `Doc_01` §5, the Article 21 test, restates the superseded picture and calls Possidius unvendored

The Ecological-orientation bullet — the exact test the ruling reasons about — reads:

> "on the evidence this document has examined (§2 above — Cyprian's own election by congregational acclamation and ordination; Augustine's own ordination to the presbyterate by Valerius, Valerius's own subsequent designation of him as coadjutor, and his consecration to the episcopate — by Megalius, primate of Numidia, an identification this world's own vendored corpus carries only as NPNF's editorial note, itself sourced there to **Possidius's *Life of Augustine*, which is not vendored in this corpus**)"

Two problems. The enumeration cross-references "§2 above" for a pathway §2 no longer describes that way. And **"not vendored in this corpus" is flatly false**: `Source_Registry.md` row 192 carries Weiskotten 1919 as **Native, Confidence A**, vendored at `cic/texts/possidius_vita-augustini_weiskotten1919.txt`.

I record that this is **pre-existing, not created by `bf0e0d5f`** — and that it was already flagged. `Doc_02_Source_Ecology.md` line 21 says so in terms: Doc_01's text "still states is 'not vendored in this corpus,' **now stale (flagged for whoever next touches Doc_01**…)". The correction thread touched `Doc_01`, in the adjacent section, and did not take the flag.

## MED-3 — every corrected file narrows ch. VIII's clamour to "the people"; Possidius does not

The subject of the clamour in ch. VIII is `omnibusque audientibus` — "all who heard" — and Possidius has just enumerated who that is: the bishops who happened to be present, **all the clergy of Hippo**, and all the people. `universae plebi` is the dative indirect object of `insinuavit voluntatem`; it is not the subject of `clamantibus`.

`Doc_01` §2 renders this as: *Possidius "records Valerius announcing his intention **'to all the people,'** **the people** **'clamored most [eagerly],'**"*. The second quotation is attached to a subject the source does not supply. The Latin ellipsis used across the build and in `Possidius_Full_Read_2026-09-16.md` — `universae plebi… ingenti desiderio clamantibus` — performs the same splice at the Latin level, joining two different clauses across the elision.

This does **not** refute the correction: the people were expressly among those addressed and among those who heard, and the announcement was made to them. But the build's claim is specifically about *congregational* authority, and ch. VIII gives a mixed assembly of bishops, clergy and people, convened and addressed by the bishop. **Under "quote exactly," the attribution should be repaired.** The honest rendering is that the whole assembly, the people included, clamoured.

## MED-4 — `Doc_07` §2F overstates what ch. VIII warrants

> "at the episcopate for both men — Cyprian's *your suffrage and God's judgment*, and **Augustine's own election by popular clamour, refusal and compulsion** at *Vita* ch. VIII"

Two overstatements. **Ch. VIII records no election.** It records Valerius petitioning the Primate of Carthage by secret letter, obtaining his answer, announcing his own settled intention, and Megalius ordaining. The people assent; they do not elect. Cyprian's case was an election; Augustine's, on this chapter, was not.

**And the compulsion is not attributed by Possidius to the clamour.** The Latin sequences it: `Dumque illi fieri solere ab omnibus suaderetur, atque id ignaro transmarinis et Africanis Ecclesiae exemplis provocaretur, compulsus atque coactus succubuit` — what overcame the refusal was being convinced the thing was customary and shown precedents from the churches overseas and in Africa. The clamour precedes the refusal; the argument from precedent follows it. "Election by popular clamour" compresses all of that away.

`Doc_08`'s Layer 3 makes a milder version of the same compression ("by popular clamour he refused before yielding under compulsion"). `Doc_05` §4.1 is the file that gets it right — it keeps designation and consecration in place and adds the clamour "at that same event" alongside them, which is what the chapter supports.

I raise this as MEDIUM, not HIGH, because the claim the correction exists to make — congregational demand meeting a reluctant candidate at the episcopate — survives all of it. What is overstated is the mechanism, not the pattern.

**A related precision point, recorded and not inflated into a finding.** `Doc_01` §2 characterises the recurring element as "congregational demand overriding an initially reluctant **convert's** own preference." At ch. VIII Augustine is four years a presbyter, not a recent convert, and his stated ground for refusing is canonical — `contra morem Ecclesiae suo vivente episcopo`, that it was against the custom of the Church while his bishop lived — not personal reluctance for office. The characterisation is imported from the Cyprian and ch. IV cases. It is loose rather than wrong, and I would not hold the document for it, but a later round should not treat "reluctant convert" as attested at ch. VIII.

## LOW-1 — `Doc_01` §2's corrected sentence no longer parses

> "…the *Vita* records both at the same event. **and** the document states that precisely rather than let the two 'roughly N years' figures read as comparable when they measure different things."

A full stop followed by a lowercase conjunction. The trailing clause was the tail of the original sentence ("…not at the same office for both, **and** the document states that precisely…"); the correction replaced its head and left it stranded without a subject. Collateral damage, confined to grammar.

## LOW-2 — `Doc_07` §2F cites the same locus twice in one clause

"compulsion **at *Vita* ch. VIII** (Possidius, *Vita* ch. VIII; `Review-Artifacts/…`; corrected on the project lead's ruling…)". The first is also misplaced: it reads as though the election occurred at a chapter rather than at an office.

## LOW-3 — the correction is recorded against the wrong section of `Doc_08`

The commit message, `lpc_Decision_Log.md` and `lpc_World_Profile.md` §11 all cite **"Doc_08 §2"**. `Doc_08` §2 is *Preliminary Forces Identification* (lines 31–38) and carries none of this. The correction is in **Section 3 — The Six-Cell Matrix**, Cell 1B, **Force 1B-2** (lines 83–91). Three records point a later reader at a section that does not contain the edit.

## LOW-4 — `lpc_World_Profile.md` contradicts itself on the count, in one paragraph

§11 item 4: "propagated cleanly **across all six documents**". The Disposition, one paragraph: "**eight files including this one**, all at *Approved to proceed*" and then, four sentences later, "The project lead ruled … that **all six documents** be corrected … the correction is applied at **Doc_01 §2, Doc_03, Doc_05 §4.1, Doc_07 §2F and this document**" — five files listed, `Doc_08` and `lpclex011` omitted, after the same paragraph has said eight.

## LOW-5 — punctuation residue at `lpc_World_Profile.md` §5

"attested through different figures**,** and different words" — the comma is what is left of the deleted "different offices,".

## LOW-6 — `Doc_03` row 30's Sources cell does not carry ch. VIII

The row's Key Sources cell still reads "Row 192 (Possidius, *Vita* **IV** — see below)". The corrected Deployment cell in that row now rests on ch. VIII. The row licenses a source locus it no longer uses and omits the one it does.

---

# 5. Collateral damage

Four items, all above: **LOW-1** (broken sentence in `Doc_01` §2), **MED-1** (`lpclex011` Key Sources falsified by the correction in its own file), **LOW-5** (comma residue), **LOW-6** (source cell not updated with the row it supports). **HIGH-2**'s Significance-cell quotation is the same class as the World Profile case caught during application — a quotation of `Doc_01` §2's pre-correction wording left standing after `Doc_01` §2 changed — and was not caught.

**Cross-reference integrity, checked and clean.** No section moved. `Doc_05` §4.1, `Doc_07` §2F, `Doc_08` Force 1B-2 and the World Profile sections all still exist at the numbers that cite them; the only routing error is LOW-3, and it predates nothing — it was introduced by this commit's own record-keeping.

**Table integrity, checked and clean.** `Doc_03`'s candidate table holds 8 pipes per row across rows 24–30, header included. No cell was split or merged.

**Derived artifacts, checked and clean.** `Doc09_Claims_Register.md`, `Lexicon_Deployment_Index.md`, `lpc_Force_Index.md` and `lpc_Story_Index.md` were **not** modified by `bf0e0d5f`, and I confirm none needed to be: no register entry quotes any of the changed sentences, and the force's name and cell are unchanged. I ran the control rather than take the commit's word for it:

```
claims derived from the deliverables : 142
entries in the register              : 142
of those, carrying a recorded check  : 9
OK — every claim about the record is registered, and every register entry still corresponds to live text.
```

The commit message's "the claims control passes with all nine recorded checks intact" is accurate. Its "Indexes and claims register regenerated" is accurate in effect — nothing changed because nothing needed to.

---

# 6. Article 21

**The determination is not disturbed. I agree with the Decision Log, and I would not escalate this to the project lead as a governance finding.**

`Doc_01` §5's Ecological-orientation test asks whether the two phases show *meaningfully distinct patterns of ecological orientation* — whether a bishop's authority is legitimated by, and exercised as, care for a bounded local community he is answerable to and for. Its named hard case is Augustine's solicitation of imperial coercion; congregational consent enters as supporting evidence that "both bishops' own words carry the same finding directly."

Article 21 is a test for **difference** between phases. The correction **deletes a difference** — it converts "the pattern appears at different offices in the two phases" into "the pattern appears at the same office in both phases." A finding that reduces cross-phase divergence cannot, by the structure of the test, argue for strand plurality. The evidence moves in the direction the existing determination already points. The Decision Log's reasoning — "one pattern at one office across both phases strengthens the strand-singular determination rather than unsettling it" — is right, and it is right for the reason it gives.

I add two qualifications, neither of which changes the answer.

**First, the strengthening is smaller than the commit message implies.** §5's own disclosed weak point is the **conciliar-authority axis**, which §5 calls the "closest call" and does not consider closed, with a reopening caveat routed to `Doc_04`. Congregational consent at ordination is not that axis and does nothing for it. The correction strengthens an axis that was never in contention.

**Second — and this is the one thing here I would put in front of the project lead, as an observation rather than a finding.** `Doc_01` §5 reached the Article 21 determination while stating, in the body of the test itself, that Possidius's *Life of Augustine* "is not vendored in this corpus" (MED-2). It is, and always was: Registry row 192, Native, Confidence A. A Native vendored source bearing directly on the determination's own supporting evidence was excluded from the test by a factual error about the corpus, and the error is still in the text of the test at `bf0e0d5f`. **The determination survives — the source, once read, supports it.** But it was reached on an evidentiary base narrower than the corpus actually offered, and the record should say so rather than leave §5 asserting that the source does not exist. That is a record-accuracy matter for whoever next opens `Doc_01`, not a reopening.

---

# 7. What I did NOT check

Stated so no later round mistakes this artifact's scope.

- **I did not verify the other thirty chapters of the *Vita*.** I read the Preface bounds, chapters IV and VIII in full in both languages, and searched the whole body for the vocabulary at item 1. I did not audit `Possidius_Full_Read_2026-09-16.md`'s §2 and §3 — its nine other findings and its five upheld claims are outside this brief and I take no position on them.
- **I did not verify any claim in the eight files other than this one.** I checked the congregational-consent claim and its immediate neighbours. `Doc_03`'s *plebs* sweep, `Doc_05`'s Pontius and Letter XXXI quotations, `Doc_07`'s Pinianus material and `Doc_08`'s confidence ratings were read for context and not tested.
- **I did not test whether the eight files are otherwise correct, complete or consistent.** This is a propagation check on one correction.
- **I did not read the `Review-Artifacts/` review series.** I confirmed those files carry pre-correction wording and left them; I did not assess whether any of them should have been annotated.
- **I did not check other world-builds.** If `desert`, `don`, `alx` or `hal` carry a parallel claim sourced from `lpc`'s Doc_01 §2, I did not look. The brief scoped me to this build folder.
- **I did not re-derive the Article 3 / gapped-formation question**, which the World Profile Disposition correctly still carries open.
- **I did not check the Cyprian side of the pattern beyond Ep. XXXIX.** Pontius (row 7) is quoted across the build for Cyprian's election; I did not open it. The `suffragium` check at item 1 is Ep. XXXIX only.
- **I ran `check_claims.py` but did not audit it.** I confirm it passes at `bf0e0d5f`; I did not verify that its derivation catches the sentences this correction changed.

---

# 8. Disposition of this artifact

A verification, not a construction document, and **it fixes nothing**. Fourteen findings are recorded above; none is applied. The four HIGHs are carriers of a claim the project lead ruled should be removed from the build, and they are still in it.

**The ruling's second limb is now discharged: the propagation has been verified independently, and it did not pass.** What follows is the applying thread's work or the project lead's call, not this thread's.
