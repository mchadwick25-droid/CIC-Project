# Doc_01 §2 Correction — Independent Verification, Round 2

## Latin Pastoral-Congregational Christianity (`lpc`)

*Closing verification of the second correction pass. Commissioned after `Review-Artifacts/Doc01_Correction_Propagation_Verification_2026-09-16.md` returned NOT VERIFIED on fourteen findings.*

**Under verification:** commit `f01b4212`, "lpc: complete the Doc_01 §2 propagation — verification returned NOT VERIFIED". Ten files, 318 insertions, 16 deletions, of which 302 insertions are the prior verification artifact itself; the substantive change is **16 insertions and 16 deletions across nine build files**.
**Build state verified:** working tree at `f01b4212`, clean, no uncommitted changes anywhere in the repository.
**Verifier:** isolated pass. **I did not apply either correction, did not write the escalation, did not write `Possidius_Full_Read_2026-09-16.md`, and did not write the Round 1 verification.** I formed my view of every file from its current text before opening `git diff bf0e0d5f f01b4212`.

---

# VERDICT: **NOT VERIFIED**

**2 HIGH · 5 MEDIUM · 8 LOW.**

**Of the fourteen prior findings, six are closed, six are closed in part, and two are untouched.** No prior finding was closed wrongly. Every edit `f01b4212` made is, in itself, correct and an improvement; several are precisely right. The failure is not in what was changed but in what was again left beside it.

**The second pass repeated the first pass's failure mode one level down.** The first correction went to one instance per file and stopped. This one went to the instance the verification named and stopped — including inside the same paragraph, the same bracketed note and the same table cell. `Doc_03` row 30's Significance cell had three defects named in one finding; two were fixed and the third, the one the prior verification singled out as the most serious, was not touched. `Doc_05` §4.1's Construction note had its first sentence corrected and its third sentence, which says the opposite, left standing.

**My independent sweep found a carrier neither prior sweep nor the prior verification caught.** `Doc_05_Ecological_Reconstruction.md` line 169 states the refuted claim in terms — *"popular pressure is one named factor in his acceptance, not the mechanism of his appointment"* — two sentences after the correction, in the file the Round 1 verification called "the most careful of the eight". It has been in that file since its original draft (`8c246652`) and has survived two sweeps, one correction, one verification and one closing pass. It is **HIGH-1** below.

**The deployment chunk is fit to ship.** `Lexicon-Chunks/lpclex011_suffrage.md` is the one file where an error reaches a person, and it is the one file this pass fixed completely. See §5.

**The source claim is confirmed a second time, independently.** I re-derived ch. VIII from the body text in both languages before reading any build file's account of it. The correction rests on a real finding, and the standard formulation the second pass introduced is **accurate to the source**. See §3.

**One new defect was introduced.** A string replacement made for LOW-3 corrupted an unrelated and correct cross-reference in `lpc_Decision_Log.md`. It is **MED-3** below.

---

## Method

I established the source before reading any build account of it.

`possidius_vita-augustini_weiskotten1919.txt` is bilingual, Weiskotten's revised Latin facing his English, hyphenating across line breaks in both. I built a de-hyphenated, whitespace-collapsed stream of the **body span only** — `PREFACE` at line **1518** to the `NOTES` heading at line **5063**, 201,624 characters — before searching. Weiskotten's Introduction (lines 122–1517) and his endnotes and index (5063–6294) are outside it and nothing below is taken from them. I isolated chapter VIII by extracting the span between the `CAPUT VIII` and `CAPUT IX` headings (6,814 characters) and ran the vocabulary tests inside that span.

For Cyprian I resolved the work by `title=` on `<div3>`, never by position: `To the People, Concerning Five Schismatic Presbyters of the Faction of Felicissimus.` at offset 2439639 of `anf05_hippolytus-cyprian-caius-novatian.xml`, 17,856 characters, **16 `<note>` spans marked and removed before tags were stripped**.

For the sweep I searched every `*.md` in the build folder except `Review-Artifacts/` — 47 files — on the seven formulations named in the brief plus thirty-eight further ones of my own, listed at §2. I ran the sweep before reading the diff, and I ran a second and third pass from different angles afterwards.

I ran `scripts/check_claims.py` rather than trusting any commit message's report of it.

---

# 1. The fourteen prior findings, dispositioned

| # | Prior finding | Disposition |
|---|---|---|
| 1 | **HIGH-1** — `Doc_01` §2 still says "not a second popular acclamation" | **CLOSED** |
| 2 | **HIGH-2** — `Doc_03` row 30 corrects one cell of four | **STILL OPEN in part** — two of three limbs closed; the verbatim quotation of `Doc_01` §2's superseded wording is untouched |
| 3 | **HIGH-3** — `Doc_08` Force 1B-2 Layer 1 contradicts Layer 3 | **CLOSED**, and well |
| 4 | **HIGH-4** — `lpclex011` World Meaning deploys the refuted claim | **CLOSED**, and well |
| 5 | **MED-1** — `lpclex011` Key Sources false after the correction | **CLOSED** |
| 6 | **MED-2** — `Doc_01` §5 restates the superseded picture; calls Possidius unvendored | **STILL OPEN in part** — "not vendored" fixed; the enumeration unchanged, and the repaired clause now contradicts itself |
| 7 | **MED-3** — the clamour narrowed to "the people" | **STILL OPEN in part** — fixed at five sites; the misattributed quotation survives at `Doc_01` §2 and the Latin splice survives in the Decision Log |
| 8 | **MED-4** — `Doc_07` §2F overstates ch. VIII | **CLOSED**, and verified at source |
| 9 | **LOW-1** — `Doc_01` §2's corrected sentence does not parse | **CLOSED** |
| 10 | **LOW-2** — `Doc_07` §2F cites the same locus twice | **STILL OPEN in part** — the misplacement fixed, the doubling not |
| 11 | **LOW-3** — correction recorded against `Doc_08` §2 | **STILL OPEN in part, and one fix went wrong** — see MED-3 below |
| 12 | **LOW-4** — `lpc_World_Profile.md` contradicts itself on the count | **STILL OPEN in part** — one of four count statements fixed |
| 13 | **LOW-5** — punctuation residue at `lpc_World_Profile.md` §5 | **STILL OPEN** — untouched |
| 14 | **LOW-6** — `Doc_03` row 30's Sources cell does not carry ch. VIII | **STILL OPEN** — untouched |

**Closed: 6. Closed in part: 6. Untouched: 2. Closed wrongly: 0.**

The six closures are real closures, not restatements. HIGH-3, HIGH-4, MED-1 and MED-4 in particular were fixed with more care than the finding required — `Doc_08` Layer 1 gained the correct clamour subject, the persuasion sequence and an updated source list in one edit, and `Doc_07` §2F gained an explicit *"the *Vita* records no election"*, which I confirm at source at §3.

---

# 2. My own sweep

Forty-five formulations, every `*.md` in the build folder except `Review-Artifacts/`, case-insensitive. Beyond the seven the brief named: `different mechanism entirely`, `rather than acclamation`, `by designation rather than`, `not acclamation`, `one recurring office`, `one settled office`, `attached to different offices`, `different office each`, `second phase at a different`, `not identically`, `two resemblances`, `loose resemblance`, `differently worded`, `smoothed into one`, `not one recurring`, `one recurring word`, `coadjutor`, `designation as coadjutor`, `not an acclamation`, `no acclamation`, `without acclamation`, `only … designation`, `persuaded him rather`, `one of two things`, `two things that persuaded`, `not the electing`, `not elected`, `no popular`, `did not elect`, `assented rather`, `different point in his career`, `the difference is kept`, `rise to the episcopate`, `raised to the episcopate`, `came to the episcopate`, `accepted the episcopate`, `entry into the episcopate`, `elevation to the episcopate`.

**No ninth file.** `Doc_02`, `Doc_04`, `Doc_06`, `Doc_09`, `Doc09_Claims_Register.md`, `Step0_*`, `Source_Registry.md`, `Source_Acquisition_Manifest.md`, `lpc_Force_Index.md`, `lpc_Story_Index.md`, `lpc_Gapped_Formation_Precedent.md`, `Doc_04_Superseded_Claims.md`, `Datus_Portrait_Prompt.md`, `Lexicon_Deployment_Index.md`, all seven `Story-Chunks/` and the other eighteen `Lexicon-Chunks/` carry no form of the office claim. I confirm the Round 1 verification's judgement that `Doc_02` line 17 is **not a carrier** — it is scoped to what Registry row 11 attests and denies nothing — and I would not correct it either.

**One live carrier the prior sweeps and the prior verification all missed: `Doc_05` line 169.** It is HIGH-1 below. `git log -S` confirms the sentence has been in the file since `8c246652`, the original Doc_05 draft, and was touched by neither `bf0e0d5f` nor `f01b4212`.

**Two further classes the sweep surfaced that the ruling's own terms reach**, both at §4: three live assertions that Possidius is unread (MED-1), and three live assertions that the Megalius identification exists in this corpus only as NPNF's editorial note (MED-2), which the vendoring and full read of row 192 falsified and which the correction itself now contradicts in the same sentence at two of the three.

**`lpc_Decision_Log.md` lines 388 and 430 quote the pre-correction wording and are correctly left alone.** They are round-by-round records of what earlier review passes did, superseded in the log's own 2026-09-16 entry. A record of what was true when it was written is not a carrier. I apply the same rule the Round 1 verification applied to `Review-Artifacts/`.

---

# 3. The source check

**Confirmed. The standard formulation the second pass introduced is accurate to the body text in both languages.**

The formulation, as it appears at `Doc_01` §2, `Doc_03` row 30 and `Doc_08` Force 1B-2:

> "Possidius *Vita* ch. VIII records Valerius announcing his intention to the bishops present, the whole Hippo clergy and **all the people**; *"all who heard"* rejoiced and clamoured eagerly for it; Augustine **refused** the episcopate while his own bishop lived; and, persuaded by transmarine and African precedent, he yielded *"under compulsion and constraint"*."

Checked limb by limb against the body span, de-hyphenated:

| Limb | Source, English body | Source, facing Latin |
|---|---|---|
| Announced to bishops, clergy and people | "made his desire known to the bishops who happened at that time to be present, and to all the clergy of Hippo and to all the people" | `episcopis qui forte tunc aderant, et clericis omnibus Hipponensibus, et universae plebi inopinatam cunctis suam insinuavit voluntatem` |
| **Subject of the clamour** | "But while **all who heard** rejoiced and clamored most elageriy that this should be done and accomplished" | `omnibusque audientibus gratulantibus, atque id fieri perficique ingenti desiderio clamantibus` |
| Refusal | "the presbyter refused to accept the episcopate contrary to the custom of the Church, since his bishop was still living" | `episcopatum suscipere contra morem Ecclesiae suo vivente episcopo presbyter recusabat` |
| **Cause of the yielding** | "when they had convinced him that this was generally done and had appealed to examples from the churches across the sea as well as in Africa… under compulsion and constraint he yielded" | `Dumque illi fieri solere ab omnibus suaderetur, atque id ignaro transmarinis et Africanis Ecclesiae exemplis provocaretur, compulsus atque coactus succubuit` |

`elageriy` is the scan's corruption of *eagerly*; the build's bracketed `[eagerly]` is the correct handling.

**Is the clamour's subject stated correctly? Yes, at every site the second pass wrote, and at one it did not.** The subject is `omnibusque audientibus` — "all who heard" — the mixed assembly Possidius has just enumerated, not `universae plebi`, which is the dative indirect object of `insinuavit voluntatem`. The new formulation gets this right, and `lpc_World_Profile.md` §4F states it flatly and correctly: *"**all who heard** — not the people alone"*. **The misattribution survives at exactly one live site, `Doc_01` §2, in a second narration the second pass added text alongside without removing** — MED-4 below.

**Does anything still record ch. VIII as an election, or attribute the yielding to the clamour? No, and `Doc_07` §2F now says so explicitly — correctly.** I tested chapter VIII's 6,814-character span for electoral vocabulary directly:

```
elig* / elect* / suffrag* / acclam* / vot* in CAPUT VIII : 0
suffrag* in the whole body of the Vita               : 1  (suffragatori, ch. XXVII)
acclam*  in the whole body of the Vita               : 0
```

The chapter's own heading is `Designatur episcopus vivo Valerio et a Megalio primate ordinatur` — *designated*, not elected. Weiskotten renders it "He is chosen bishop", which is a translation of `designatur` and not independent evidence of an election. `Doc_07` §2F's parenthetical — *"the yielding follows persuasion from transmarine and African precedent, and the *Vita* records no election"* — is exactly right on the Latin. MED-4 is properly closed.

**Is the account consistent across the files that carry it? Not quite.** Three sites carry the full standard formulation with the correct subject and the persuasion clause (`Doc_01` §2's first narration, `Doc_03` row 30, `Doc_08` Layer 1). Two more state the subject correctly in their own words (`lpclex011` World Meaning, `lpc_World_Profile.md` §4F and Disposition). **Four state a bare "popular clamour" with neither qualifier** — `Doc_05` §4.1, `Doc_07` §2F, `lpclex011`'s Caution, `lpc_World_Profile.md` §5. Those four are compressions, not errors, and I do not raise them as a finding; the reader of any of them is not told anything false. I record the divergence because the brief asks, and because a later condensing pass should standardise on the longer form rather than the shorter.

**The Cyprian side, re-verified independently.** Ep. XXXIX, resolved by title, 16 note spans removed:

> "retaining that ancient venom against my episcopate, that is, against your suffrage and God's judgment"

The build's Cyprian-side quotation is exact, and it is at the episcopate. The two halves of the corrected claim are both sound.

---

# 4. Findings

## HIGH-1 — `Doc_05` §4.1's Construction note states the refuted claim two sentences after correcting it *(new; missed by both sweeps and the Round 1 verification)*

Line 169, the bracketed Construction note that closes §4.1. Read in order:

> "Possidius's *Vita* (row 192) is vendored and **has been read in full** (`Review-Artifacts/Possidius_Full_Read_2026-09-16.md`, all thirty-one chapters, 2026-09-16); §4.1's account of Augustine's episcopate now rests on its ch. VIII. The *"importunity of the people"* passage is Augustine's own and sits alongside, not against, **Doc_01's finding that the episcopate came by designation rather than acclamation: popular pressure is one named factor in his acceptance, not the mechanism of his appointment.**"

Three failures in one sentence.

**It is the refuted claim.** "Popular pressure is … not the mechanism of his appointment" is the same assertion as "not at the same office for both", stated in the mechanism register. It is the phrasing that survived every pattern-match run so far.

**It contradicts the corrected sentence in its own section.** §4.1's body, two lines above, now reads: "raised to the episcopate in 395/396 by Valerius's designation and Megalius's consecration — **and, per Possidius *Vita* ch. VIII, by popular clamour at that same event, which he refused before yielding under compulsion**". A reader of §4.1 is told the acclamation was part of how he came to the office, and then told it was not the mechanism that appointed him.

**It attributes to `Doc_01` a finding `Doc_01` no longer makes.** `Doc_01` §2 now says, in terms: "The designation, the consecration and the acclamation are one event, not alternatives." The Construction note cites the opposite as "Doc_01's finding". This is the same class of defect as HIGH-2 — a downstream document quoting or paraphrasing `Doc_01` §2's superseded position after `Doc_01` §2 changed — and it is the second instance of that class to survive a verification.

**The sentence the second pass corrected and the sentence stating the opposite are adjacent, inside one bracketed note.** This is the strongest single piece of evidence that the propagation is still being run as a search-and-replace against named findings rather than as a read of each affected passage.

## HIGH-2 — `Doc_03` row 30 still quotes `Doc_01` §2's superseded wording as what `Doc_01` §2 "states plainly"

The prior verification named three defective cells. Two were fixed. The Significance cell's opening — the one it called "the identical defect the applying thread caught in the World Profile and fixed there" — is **byte-for-byte unchanged**:

> "Doc_01 §2 states plainly that the congregational-demand pattern *'recurs at the presbyterate for Augustine and the episcopate for Cyprian, not at the same office,'* and Augustine's own rise to the episcopate came by Valerius's designation and Megalius's consecration **together with popular acclamation at the same event** — …"

The second half of that sentence was corrected. **The first half, an attributed direct quotation of the claim the ruling ordered removed, was not.** `Doc_01` §2 does not contain that sentence and has not since `bf0e0d5f`. The quotation is now false as an attribution and false as a statement, and it sits in the same sentence as its own correction, joined by "and".

I confirm from the word-diff that the second pass edited this exact sentence — it changed `— "not a second popular acclamation."` to `**together with popular acclamation at the same event**` and appended the ch. VIII narration — **and did not touch the quotation forty words to its left.**

The two closed limbs are properly closed: the Notes cell's "attached to different offices each time" is gone, and the Significance closing now reads "though the two instances are now attested at the same office".

## MED-1 — Three live assertions that Possidius has not been read; the five named ones are cleared, these are the sixth, seventh and eighth

The brief asks whether the five named sites are now true and whether there is a sixth. **The five are all true.** `Doc_01` §5, `Doc_05` §1 (line 169) and §6.3 (line 225), `Doc_07` §2C (line 74) and `lpclex011` Key Sources all now state that row 192 is vendored and has been read in full, and all cite `Possidius_Full_Read_2026-09-16.md`. `Doc_02_Source_Ecology.md` line 21's flag is **properly discharged** and its discharge is accurate.

**There are three more, all live and all now false:**

| Site | Text |
|---|---|
| `Doc_05_Ecological_Reconstruction.md` line 369 (§7 open item 10) | "**Possidius's *Vita Augustini* (row 192) is vendored and unread beyond one identification.** It is this world's only biographical memory of its second phase (§6.3), and reading it would bear on §1, §4.1 and §6.3 directly." |
| `Doc_06_Full_Lexicon_Development.md` line 121 | "**Possidius's *Vita Augustini* (Registry row 192) is vendored and unread beyond one identification**, and it is the natural source for the *suffrage* entry's Augustine half. That entry currently rests on Augustine's own letters, and says so." |
| `Doc_07_Integrated_Ecology_Analysis.md` line 251 (§8 item 7) | "**Possidius's *Vita Augustini* (row 192) is unread beyond one identification** — the natural source for §2C's thinnest corner." |

Two of the three are **inside files the correction touched**, in an open-items list the correcting thread did not open. `Doc_05`'s item 10 names §1, §4.1 and §6.3 — the three sections the same commit corrected, on the basis of the read it says has not happened. `Doc_07`'s item 7 points at §2C, which the same commit corrected. `Doc_06`'s is in a file neither pass touched and names `lpclex011`'s own entry as what a read would strengthen; `lpclex011` now rests on chs. IV and VIII.

**A fourth site, reported rather than raised as a finding.** `Doc_04_Gravity_Discovery.md` line 34 excludes Possidius from Candidate 1's Confidence/Gravity Cross-Check: "Possidius's *Vita* (Registry row 192, vendored 2026-09-05) is not part of this re-verification — Doc_02 §2 and §4 both disclose it has not been read this session beyond the Megalius-consecration identification — and is not counted toward this Cross-Check." The disclosure it reports is still literally present at `Doc_02` §2 and §4, which scope themselves to *"this pass"* and *"this session"* — Doc_02's own drafting session of 2026-09-08. So the sentence is stale rather than false, and its exclusion no longer reflects the evidence available. **I do not hold it as a finding**: it is outside the ruling, predates both commits, and correcting a Confidence Cross-Check is a Doc_04 act, not a propagation act. A later round should reach it.

**Also stale, recorded not raised:** `lpc_World_Profile.md` line 764 says three superseded statements "stand uncorrected in their own documents", naming `Doc_07` §2C among them. `Doc_07` §2C is now corrected.

## MED-2 — Three live sites still say the Megalius identification exists in this corpus only as NPNF's editorial note; ch. VIII carries it directly

Verified at source, from the body span, in both languages:

> `CAPUT VIII  Designatur episcopus vivo Valerio et a Megalio primate ordinatur`
> `…tunc primate Numidiae Megalio Calamensi episcopo…`

> "CHAPTER VIII  He is chosen bishop while Valerius is still living, and is ordained by the primate Megalius"
> "…when Megalius, Bishop of Calama, and at that time primate of Numidia, had come at his request to visit the church at Hippo…"

Possidius names Megalius, names Calama, and names him primate of Numidia, in his own text. Since row 192 was vendored on 2026-09-05 the identification has been carried in this corpus by a Native, Confidence A source directly — not only by NPNF's note. Three live sites say otherwise:

- **`Doc_01` §2**, *inside the corrected sentence*: "consecration by Megalius, primate of Numidia (**an identification carried in this world's own vendored corpus only as NPNF's editorial note**) — **and, at that same event, popular acclamation as well**: Possidius *Vita* ch. VIII records…". The parenthesis and the clause that follows it cite the same chapter for opposite propositions.
- **`Doc_01` §5**, *inside the clause the second pass repaired*: "an identification this world's own vendored corpus **carries only as NPNF's editorial note**, itself sourced there to Possidius's *Life of Augustine*, Registry row 192, **vendored and read in full**". The repair and the error are eleven words apart in one clause.
- **`Doc_05`** line 169: "**The Megalius consecration is carried in this world's vendored corpus only as NPNF's own editorial note** (Doc_01 §2)".

`Source_Acquisition_Manifest.md` line 29 anticipated exactly this: acquiring G3 "would let this document independently verify the Megalius identification at its own source rather than only through NPNF's editorial note." It did. No document has recorded it.

This is collateral of the correction rather than a carrier of the refuted claim, and I grade it MEDIUM on that basis. But at `Doc_01` §5 it is now a self-contradiction created by this commit's own edit, and at `Doc_01` §2 it sits inside the sentence the whole ruling is about.

## MED-3 — The LOW-3 fix corrupted an unrelated, correct cross-reference *(new defect, introduced by `f01b4212`)*

`lpc_Decision_Log.md` line 1327 now reads:

> "A dossier assembled by its own author in his own lifetime — which is what **Doc_08 §3 (Force 1B-2)B-5** shows Cyprian doing — is not a community's remembered collection."

The original text was **"Doc_08 §2B-5"**, a correct reference to `Doc_08`'s **Force 2B-5** — *Transmission: survival on the institutionally dominant side*, the entry that carries Cyprian's thirteen-letter dossier. `Doc_08` uses `§2B-5` as its own shorthand for that force (line 476: "§2B-5 *discusses* the phenomenon"), and `lpc_Story_Index.md` line 45 and `Doc_09_Story_Inventory.md` line 66 both still cite it correctly in that form.

A replacement of `§2` with `§3 (Force 1B-2)` was run without checking what each `§2` referred to. The result is a reference that is syntactically broken and semantically wrong: it now points a reader at **Force 1B-2, the acclamation force**, for a claim about Cyprian's letter dossier. Force 1B-2 says nothing about it.

This is the one thing in `f01b4212` that made a file worse than it was at `bf0e0d5f`.

## MED-4 — `Doc_01` §2 now narrates chapter VIII twice, and the second narration carries the error the first corrects

The second pass inserted a correct narration and did not remove the one already there. The bullet now reads, in sequence:

> "…**and, at that same event, popular acclamation as well**: Possidius *Vita* ch. VIII records Valerius announcing his intention to the bishops present, the whole Hippo clergy and **all the people**; *"all who heard"* rejoiced and clamoured eagerly for it; Augustine **refused** the episcopate while his own bishop lived; and, persuaded by transmarine and African precedent, he yielded *"under compulsion and constraint"*. **The designation, the consecration and the acclamation are one event, not alternatives.** The recurring element is congregational demand overriding an initially reluctant convert's own preference at the point of entry into clerical office, and **it recurs at the episcopate for both men** — Possidius *Vita* ch. VIII records Valerius announcing his intention *"to all the people,"* **the people** *"clamored most [eagerly],"* Augustine *"refused to accept the episcopate,"* and *"under compulsion and constraint he yielded"* (…), and at the presbyterate for Augustine in addition (*Vita* ch. IV). **The consecration by Megalius and the acclamation are not alternatives**: the *Vita* records both at the same event."

The same chapter, summarised twice in one bullet, from the same source, in two different renderings; and "not alternatives" stated twice in eighty words.

**MED-3 of the prior verification is therefore closed everywhere except here, where the correction that closed it elsewhere was placed next to the text carrying it.** The second narration still attaches the direct quotation *"clamored most [eagerly]"* to "the people" — a subject the Latin does not supply — and this is the origin document every other file cites.

The Latin-level form of the same splice also survives, in `lpc_Decision_Log.md` line 1759: `universae plebi… ingenti desiderio clamantibus`, an ellipsis that joins the dative indirect object of one clause to the ablative absolute of the next. That entry's *English* rendering of the same passage is correct.

## MED-5 — `Doc_01` §5's enumeration is unchanged and the repaired clause now contradicts itself

The "not vendored" error is fixed and that was the substantive half of the prior MED-2. What remains:

> "on the evidence this document has examined (**§2 above** — Cyprian's own election by congregational acclamation and ordination; Augustine's own ordination to the presbyterate by Valerius, Valerius's own subsequent designation of him as coadjutor, and his consecration to the episcopate — by Megalius, primate of Numidia, an identification this world's own vendored corpus carries only as NPNF's editorial note, itself sourced there to Possidius's *Life of Augustine*, Registry row 192, **vendored and read in full** at `Review-Artifacts/Possidius_Full_Read_2026-09-16.md`)"

The enumeration cross-references §2 for Augustine's pathway and omits the one element §2 was corrected to add — the episcopal acclamation. This is an omission, not an assertion, and it omits evidence that would **strengthen** the Ecological-orientation finding it is offered in support of. It is the Article 21 test's own evidence paragraph, so the omission is worth repairing rather than tolerating. The self-contradiction inside the same clause is MED-2 above.

## LOW-1 — `Doc_01` §2 still says the episcopate "came by a different mechanism entirely"

The clause survives immediately before its own contradiction: "came by **a different mechanism entirely** — Valerius's own designation as coadjutor and consecration by Megalius … — **and, at that same event, popular acclamation as well**". If the acclamation was present at the same event, the mechanism was not different *entirely*. The word was load-bearing before the correction and is now false.

## LOW-2 — `Doc_03` row 30 warns against smoothing into "one recurring office" and "one settled office" in cells that now assert the same office

Two residues left where the correction went in:

- Notes cell: "Cross-phase pattern, differently worded but attested at **the same office in both phases** … named as such rather than smoothed into one recurring word **or one recurring office**"
- Significance closing: "the two instances are **now attested at the same office** … Doc_06 should not present this as one settled term, **or one settled office**, without carrying that caution forward"

Both cells now caution `Doc_06` against a conclusion the same cell has just drawn. The "different words" limb of Doc_03's caution is sound and correctly retained; the office limb was narrowed away by the ruling and these two clauses are its tail.

## LOW-3 — `Doc_03`'s Sources cells still license only *Vita* IV *(prior LOW-6, untouched, and it extends to row 29)*

Row 30 Key Sources: "Row 192 (Possidius, *Vita* **IV** — see below)". Row 29 Key Sources: "Row 192 (Possidius, *Vita* **IV**, quoted above)". Both rows' Notes and Significance cells now rest on **ch. VIII**. Neither Sources cell carries it. The prior verification named row 30; row 29 has the identical defect and was not named.

## LOW-4 — `lpc_World_Profile.md` §5's comma residue *(prior LOW-5, untouched)*

Line 292: "attested through different figures**,** and different words". Unchanged. The comma is what is left of the deleted "different offices,". Every other site in the build reads "different figures and different words".

## LOW-5 — `Doc_07` §2F still cites *Vita* ch. VIII twice, now as two adjacent parentheticals

> "…which he refused before yielding *"under compulsion and constraint"* **(*Vita* ch. VIII; the yielding follows persuasion from transmarine and African precedent, and the *Vita* records no election) (Possidius, *Vita* ch. VIII; `Review-Artifacts/Possidius_Full_Read_2026-09-16.md`; corrected on the project lead's ruling of 2026-09-16, `lpc_Decision_Log.md`)** — and at the presbyterate for Augustine besides."

The misplacement the prior verification flagged is fixed. The doubling is not, and is now two closing parentheses in a row. The content of both is correct.

## LOW-6 — `Doc_08` §2 survives in the Decision Log, and the World Profile locus is mislabelled *(prior LOW-3, partly)*

Fixed at `lpc_World_Profile.md` ×2 and at the Decision Log's **Applied at** bullet. Still wrong at the Decision Log's **What it refuted** bullet, four lines above it:

> "carried at `Doc_03` (three sites), `Doc_05` §4.1, `Doc_07` §2F, **`Doc_08` §2** and `lpc_World_Profile.md`"

And the **Applied at** bullet, in the act of being corrected, mislabels a different locus: "`lpc_World_Profile.md` Sections 4F (×2), **5 (Force 2A-2)**, 6, 7". The World Profile's Section 5 entry is explicitly **Cell 1B**, Force **1B-2**. Force 2A-2 is the plague.

## LOW-7 — the count statements still disagree

Fixed: §11 item 4 now reads "across all eight files".

Not fixed:

- `lpc_World_Profile.md` Disposition, one paragraph: "**eight files including this one**" … then "the correction is applied at Doc_01 §2, Doc_03, Doc_05 §4.1, Doc_07 §2F and this document" — **five files listed**, `Doc_08` and `lpclex011` still omitted.
- `lpc_Decision_Log.md` line 1757, the entry heading: "corrects Doc_01 §2's congregational-consent finding **across six documents**".
- `lpc_Decision_Log.md` line 1762, the ruling itself as recorded: "correct **all six documents**". The same bullet's body elsewhere says eight.

## LOW-8 — the Decision Log has no entry for the verification or the second pass

`lpc_Decision_Log.md`'s 2026-09-16 entry still closes:

> "**Outstanding:** independent verification of the propagation, per the ruling's own second limb. **Not performed by the thread that applied it.**"

The verification was performed, returned **NOT VERIFIED** on fourteen findings, and was answered by `f01b4212`. The log records none of it: not the verdict, not the second pass, not which findings it closed. The only change `f01b4212` made to the log was two cross-reference substitutions, one of which is MED-3. The governing record of this correction currently reports the ruling's second limb as outstanding and says nothing about the two rounds that discharged and then failed it.

---

# 5. `lpclex011_suffrage.md` — fitness to deploy

**FIT TO DEPLOY. This is the one file in the build that this pass fixed completely, and it is the file where it mattered most.**

I read the whole chunk — front-matter, Quick Meaning, World Meaning, Ecological Function, Distortion Risk, Key Sources, Caution, Final Assembly Instruction.

**The World Meaning is corrected and correct:**

> "The pattern recurs in the second phase but not identically, and the difference is kept rather than smoothed: Augustine was seized into the **presbyterate** at Hippo against his wishes; his **episcopate** came by his predecessor's designation and a consecration — and, at the same event, **by the acclamation of all who heard it**, which he refused before yielding under compulsion."

The clause the prior verification called "the refuted claim in its strongest form" — *"with the people one of two things that persuaded him rather than the mechanism that appointed him"* — is gone. The replacement uses **"all who heard"**, which is the correct subject and which four builder-facing documents do not manage. "but not identically" remains true and is doing honest work: the presbyterate seizure is an additional instance Cyprian has no counterpart to, and the words differ.

**The Key Sources block is now true on both counts it was false on:** row 192 is stated as read in full, and the entry states what it rests on — "chapters IV and VIII are what this entry's account of Augustine's two offices rests on".

**World Meaning and Caution now agree.** The chunk's two halves no longer say opposite things. The `Retrieve-When` trigger the prior verification tested — *"participant asks whether anyone wanted these jobs"* — now returns the corrected answer from the body the Representative draws on.

**Two observations, neither a bar to deployment and neither raised as a finding.**

The Caution compresses to "popular clamour" where the World Meaning says "all who heard"; the chunk is internally slightly uneven, and the builder-facing half is the looser one. That is the safe direction for the asymmetry to run.

The Aliases line carries "popular election". For Cyprian that is exactly right — Ep. XXXIX and Pontius both describe an election. For Augustine's episcopate it is not, and `Doc_07` §2F now says so. An alias is a retrieval key, not a claim, and the World Meaning it retrieves does not call Augustine's episcopate an election. I would leave it.

**I would deploy this chunk as it stands.**

---

# 6. Collateral

**Parsing — clean.** Every sentence `f01b4212` wrote or altered parses. LOW-1 of the prior round is genuinely closed: `Doc_01` §2's tail now reads "The document states that precisely rather than letting the two 'roughly N years' figures read as comparable when they measure different things" — a complete sentence with a subject. I read each of the nine altered passages in full for stranded conjunctions, orphaned subordinate clauses and dangling citations; there are none. `Doc_08` Layer 1's "and at the **episcopate** Possidius *Vita* ch. VIII records…" is awkward but grammatical.

**Duplication — one instance, MED-4.** `Doc_01` §2 narrates ch. VIII twice and states "not alternatives" twice. No other file duplicates.

**Cross-references — one broken, one mislabelled, both in `lpc_Decision_Log.md`.** MED-3 and LOW-6. Every other reference altered by this commit resolves: `Doc_08` Section 3 exists and contains Force 1B-2 at lines 83–91; `Doc_05` §4.1, `Doc_07` §2F, `Doc_07` §2C, `Doc_01` §2 and §5 and the World Profile sections all exist at the numbers that cite them. `Review-Artifacts/Possidius_Full_Read_2026-09-16.md` exists and is cited consistently across nine sites.

**Contradictions within a file created or left by the correction — five.** `Doc_05` §4.1 body against its own Construction note (HIGH-1); `Doc_03` row 30's Significance opening against its own closing (HIGH-2); `Doc_03` row 30's two "office" residues against the corrected clauses in the same cells (LOW-2); `Doc_01` §5's "carries only as NPNF's editorial note" against "vendored and read in full" eleven words later (MED-2); `Doc_01` §2's "a different mechanism entirely" against "and, at that same event, popular acclamation as well" (LOW-1).

**Table integrity — clean.** `Doc_03`'s candidate table holds 9 fields per row across all 28 table lines, header and separator included. No cell split or merged.

**Derived artifacts — clean, control run rather than assumed.**

```
claims derived from the deliverables : 142
entries in the register              : 142
of those, carrying a recorded check  : 9
OK — every claim about the record is registered, and every register entry still corresponds to live text.
NOTE: 133 claim(s) are registered but still UNVERIFIED.
```

`Doc09_Claims_Register.md`, `Lexicon_Deployment_Index.md`, `lpc_Force_Index.md` and `lpc_Story_Index.md` were not modified by `f01b4212` and I confirm none needed to be. `lpc_Force_Index.md`'s Force 1B-2 row carries name, cell, confidence and gravity link, none of which changed. `Lexicon_Deployment_Index.md`'s row 11 carries `lpclex011`'s tags and source rows, none of which changed.

**Working tree — clean.** `git status --porcelain` is empty at `f01b4212`.

---

# 7. Article 21

**Not disturbed, and nothing in this round touches it.** I agree with the Round 1 verification's reasoning and with the Decision Log's: a correction that converts "the pattern appears at different offices in the two phases" into "the pattern appears at the same office in both phases" deletes a difference, and a test for cross-phase difference cannot be argued toward plurality by the deletion of one. The evidence moves in the direction the existing determination already points.

The Round 1 verification's one governance observation — that §5 reached the determination while stating that a Native, Confidence A vendored source bearing on its own supporting evidence "is not vendored in this corpus" — **is now repaired in the text of the test**, and that was the right repair. I record for the project lead that the repair is incomplete in the manner MED-2 describes: the same clause still says the corpus carries the Megalius identification only as an editorial note, which is false and which the newly-repaired half of the clause disproves. That is a record-accuracy matter for whoever next opens `Doc_01`, not a reopening, and I take the same position the Round 1 verification took.

---

# 8. What I did NOT check

- **I did not re-verify the other twenty-nine chapters of the *Vita*.** I bounded the body, extracted and read ch. VIII in full in both languages, read ch. IV's English, and ran the vocabulary tests over the whole body. I did not audit `Possidius_Full_Read_2026-09-16.md`; its other findings are outside this brief and I take no position on them.
- **I did not re-verify chapter IV's Latin.** The Round 1 verification did, and no file's ch. IV claim changed in `f01b4212`.
- **I did not verify any claim in the affected files other than this one and its immediate neighbours.** `Doc_03`'s *plebs* sweep, `Doc_05`'s Pontius and Letter XXXI quotations, `Doc_07`'s Pinianus material, `Doc_08`'s confidence ratings and `lpclex011`'s Letter CXXVI material were read for context and not tested.
- **I did not check the Cyprian side beyond Ep. XXXIX.** Pontius (row 7) is quoted across the build for Cyprian's election; I did not open it. The Ep. XXXIX check above is the only Cyprian-corpus derivation in this artifact.
- **I did not assess `Doc_04`'s Confidence/Gravity Cross-Check.** MED-1 reports its stale exclusion and stops there; whether Candidate 1's rating should now count row 192 is a Doc_04 question.
- **I did not read the `Review-Artifacts/` review series.** I confirmed they carry pre-correction wording and left them, on the same rule the Round 1 verification applied.
- **I did not check other world-builds.** If `desert`, `don`, `alx` or `hal` carry a claim sourced from `lpc`'s Doc_01 §2, I did not look.
- **I did not re-derive the Article 3 / gapped-formation question**, which the World Profile Disposition correctly still carries open.
- **I ran `check_claims.py` but did not audit it.** I confirm it passes at `f01b4212`; I did not verify that its derivation reaches the sentences either correction changed. It did not catch HIGH-1, which has been live since Doc_05's first draft.

---

# 9. Disposition of this artifact

A verification, not a construction document, and **it fixes nothing.** Fifteen findings are recorded above: two HIGH, five MEDIUM, eight LOW. **Eight of them restate findings the previous round already made and this round found still standing** — HIGH-2, MED-4, MED-5, LOW-3, LOW-4, LOW-5, LOW-6 and LOW-7. **Seven are new** — HIGH-1, MED-1, MED-2, MED-3, LOW-1, LOW-2 and LOW-8 — and one of the seven, MED-3, was created by this commit.

**The ruling's first limb is still not discharged.** A claim the project lead ruled should be removed from the build remains in it, at `Doc_05` line 169 and `Doc_03` row 30, each contradicting the corrected sentence beside it.

**The ruling's second limb is discharged twice over and has now failed twice.** What follows is the applying thread's work or the project lead's call, not this thread's.

**One thing should be said plainly for the record: the participant-facing chunk is fixed.** Whatever else is outstanding, no error in this correction now reaches a person.
