# Doc_01 §2 Correction — Independent Verification, Round 3

## Latin Pastoral-Congregational Christianity (`lpc`)

*Closing verification of the third correction pass. Commissioned after `Review-Artifacts/Doc01_Correction_Verification_Round2_2026-09-16.md` returned NOT VERIFIED a second time, on fifteen findings.*

**Under verification:** the third correction pass, identified in the brief as commit `c981f773`. **The work is not in that commit.** `c981f773` changes one word in `lpc_Decision_Log.md`. Every substantive edit of the third pass — `Doc_01` §2 and §5, `Doc_03` rows 29–30, `Doc_05` §4.1 and §11 item 10, `Doc_06` §5 item 2, `Doc_07` §8 item 7, and the four new Decision Log entries — is in **`86c3e73a`**, whose message records only the project lead's naming ruling. See LOW-1.
**Build state verified:** working tree at `c981f773`, clean, no uncommitted changes anywhere in the repository, before and after I ran the three control scripts.
**Verifier:** isolated pass. **I did not apply any of the three corrections, did not write the escalation, did not write `Possidius_Full_Read_2026-09-16.md`, and did not write either prior verification.** I derived the source and ran my own sweep before opening any diff, and I designed the sweep without reading the third pass's description of its own.

---

# VERDICT: **VERIFIED WITH FINDINGS**

**0 HIGH · 1 MEDIUM · 2 LOW.**

**The ruling's first limb is discharged.** The claim the project lead ruled should be removed from this build — that congregational demand overriding a reluctant candidate occurs "not at the same office for both" — **is not live anywhere in the build**. I ran my own sweep, designed independently of all three prior sweeps and of both prior verifications, over every `.md` file in the build folder. It found no ninth file, no eighth phrasing, and no surviving carrier in any register: not in the office register, not in the mechanism register, not by omission. **This is the first pass in the sequence of which that can be said, and it should be said plainly.**

**The third pass did what the first two did not: it swept the class, not the site.** Round 2's diagnosis was that each pass went to the instance the verification named and stopped. This pass closed both HIGHs, then corrected four further sites inside the same cells and notes that no finding had named, and its outward sweep is reproducible — I reproduced its result by a different method and reached the same answer.

**Its handling of the one genuine trap is correct and I confirm it at both ends.** `Doc_05`'s open item 10 was closed with its original wording preserved verbatim inside the closure. `Doc_09` line 128's quotation and claims-register entry `35371a96` both still resolve against `Doc_05`'s live text, character for character. See §5.

**Everything the third pass newly wrote is true against the source.** I checked every ch. VIII characterization in the build — thirty-five of them across eight files — limb by limb against the body span in both languages. None overstates what ch. VIII supports; none understates it. The Megalius correction, which is the pass's own initiative rather than a finding's, is right: Possidius names Megalius, Calama and the primacy of Numidia in his own text, in the chapter heading and in the narrative, in both languages.

**The one MEDIUM is the tail of that same Megalius correction.** Having removed from `Doc_01` the disclosure that this world's corpus carries the Megalius identification only as NPNF's editorial note, the pass left **five live statements in three other files reporting that `Doc_01` still carries it**, and **discharged two standing flags without recording the discharge**. This is the correct fix, propagated one document short. It is **MED-1** below.

**Nothing in this round reaches a participant.** `Lexicon-Chunks/lpclex011_suffrage.md` was verified fit to deploy at Round 2 and is unchanged since. I re-read it in full and reach the same judgement.

---

## Method

I established the source before opening any build file, and I did not read the third pass's account of its own source work until after mine was complete.

`possidius_vita-augustini_weiskotten1919.txt` is bilingual, Weiskotten's revised Latin with his facing English, and hyphenates across line breaks in both. I bounded the body span at **Possidius's own `PREFACE`, line 1518**, through the `NOTES` heading at **line 5063** — 202,884 characters raw — and **de-hyphenated line-break hyphens before searching**, yielding a 201,572-character stream. Weiskotten's Introduction (lines 122–1517), his endnotes (5063–6138) and his indexes are outside that bound and nothing below is taken from them. Chapter VIII is the span between the `CAPUT VIII` and `CAPUT IX` headings; I read it entire in both languages, and read ch. IV's English entire as well.

For Cyprian I resolved the work by `title=` on `<div3>`, never by position: `To the People, Concerning Five Schismatic Presbyters of the Faction of Felicissimus.` at offset 2439639 of `anf05_hippolytus-cyprian-caius-novatian.xml`, 17,626 characters, **16 `<note>` spans marked and removed before tags were stripped**. I also resolved Pontius by `title=` on `<div2>` — `The Life and Passion of Cyprian, Bishop and Martyr. By Pontius the Deacon.` at offset 2088371, 44,842 characters, 16 `<note>` spans removed — which neither prior verification opened.

For the sweep I did **not** reuse any prior pass's phrase list. My design is at §4.

I ran `gen_force_index.py`, `gen_story_index.py` and `check_claims.py` myself, with before-and-after checksums, rather than trusting any report of them.

**A count correction, for the record.** The brief describes Round 2 as returning sixteen findings — "2 HIGH, 5 MEDIUM, 8 LOW, plus the one new defect it identified." Round 2 returned **fifteen**. The new defect is its own MED-3 and is already inside the five MEDIUM; Round 2's §9 says "Fifteen findings are recorded above." I dispositioned fifteen.

---

# 1. The source, derived here

**Confirmed, in both languages, on all five limbs the brief names.**

| Limb | English body, de-hyphenated | Facing Latin |
|---|---|---|
| **Announcement to bishops, clergy and all the people** | "unexpectedly to all the bishop Valerius made his desire known **to the bishops who happened at that time to be present, and to all the clergy of Hippo and to all the people**" | `episcopis qui forte tunc aderant, et clericis omnibus Hipponensibus, et universae plebi inopinatam cunctis suam insinuavit voluntatem` |
| **The clamour and its subject** | "But while **all who heard** rejoiced and clamored most elageriy **that this should be done and accomplished**" | `omnibusque audientibus gratulantibus, atque **id fieri perficique** ingenti desiderio clamantibus` |
| **The refusal** | "**the presbyter refused to accept the episcopate** contrary to the custom of the Church, since his bishop was still living" | `episcopatum suscipere contra morem Ecclesiae suo vivente episcopo presbyter recusabat` |
| **The yielding, and what it is attributed to** | "However, **when they had convinced him that this was generally done and had appealed to examples from the churches across the sea as well as in Africa**, though he had been ignorant of it before, **under compulsion and constraint he yielded** and accepted the ordination to the higher office" | `Dumque illi fieri solere ab omnibus suaderetur, atque id ignaro **transmarinis et Africanis Ecclesiae exemplis** provocaretur, **compulsus atque coactus succubuit**` |
| **Megalius named in the chapter** | heading: "He is chosen bishop while Valerius is still living, and **is ordained by the primate Megalius**"; narrative: "when **Megalius, Bishop of Calama, and at that time primate of Numidia**, had come at his request to visit the church at Hippo" | heading: `Designatur episcopus vivo Valerio et **a Megalio primate ordinatur**`; narrative: `tunc primate Numidiae **Megalio Calamensi episcopo**` |

**The subject of the clamour is `omnibus audientibus`, "all who heard" — the mixed assembly just enumerated, not `universae plebi`,** which is the dative indirect object of `insinuavit voluntatem` in the preceding clause. Every build site that names a subject names this one. `elageriy` is the scan's corruption of *eagerly*; the build's bracketed `[eagerly]` is the correct handling, and where the build writes "clamoured eagerly" unbracketed it is paraphrase, not quotation.

**The office is the episcopate**, explicitly: `episcopatum suscipere … recusabat`, and `maioris loci ordinationem suscepit` — the ordination to the higher office. **Chapter IV independently attests the same dynamic at the presbyterate**: "they laid hands on him … for all with common consent desired that this should be done and accomplished; an[d] they demanded it with great zeal and clamor, while he wept freely." **The refuted finding is refuted at source.** Both men's *episcopal* entry is by congregational demand over reluctance; Augustine's presbyterate is an additional instance, not the only one.

**No electoral vocabulary in the chapter.** I re-ran the test independently over the isolated ch. VIII span: `elig*` / `elect*` / `suffrag*` / `acclam*` / `vot*` — **zero**. The heading's verb is `Designatur`. Weiskotten's "He is chosen bishop" renders `designatur` and is not independent evidence of an election. `Doc_07` §2F's "the *Vita* records no election" is exact.

**The Cyprian side, derived here for the second time in this sequence and the first by `title=` on both works.**

> Ep. XXXIX: "retaining that ancient venom **against my episcopate**, that is, **against your suffrage and God's judgment**"
> Pontius: "that **by the judgment of God and the favour of the people, he was chosen to the office of the priesthood and the degree of the episcopate while still a neophyte**, and, as it was considered, a novice."

Both build quotations are exact, and both are at the episcopate. Round 2 did not open Pontius; I did, and it holds.

**The source outranks everything below and it supports what the build now says.**

---

# 2. Round 2's fifteen findings, dispositioned

| # | Round 2 finding | Disposition |
|---|---|---|
| 1 | **HIGH-1** — `Doc_05` line 169's Construction note states the refuted claim two sentences after correcting it | **CLOSED** |
| 2 | **HIGH-2** — `Doc_03` row 30 quotes `Doc_01` §2's superseded wording as what it "states plainly" | **CLOSED** |
| 3 | **MED-1** — three live assertions that Possidius is unread | **CLOSED**, all three |
| 4 | **MED-2** — three live sites say the Megalius identification exists here only as NPNF's note | **CLOSED at the three named sites; the class is not closed** — see MED-1 below |
| 5 | **MED-3** — the LOW-3 fix corrupted `Doc_08 §2B-5` | **CLOSED** (repaired at `11526c3d`, before this pass; I confirm no residue anywhere) |
| 6 | **MED-4** — `Doc_01` §2 narrates ch. VIII twice; and the Latin splice in the Decision Log | **CLOSED IN PART** — the `Doc_01` §2 limb is closed; the Latin splice survives and is **not** in the pass's "Not touched" list — see LOW-2 |
| 7 | **MED-5** — `Doc_01` §5's enumeration omits the episcopal acclamation | **CLOSED** |
| 8 | **LOW-1** — `Doc_01` §2's "a different mechanism entirely" | **CLOSED** |
| 9 | **LOW-2** — `Doc_03` row 30's "or one recurring office" / "or one settled office" | **CLOSED**, both |
| 10 | **LOW-3** — `Doc_03` rows 29 and 30's Sources cells license only *Vita* IV | **CLOSED**, both rows |
| 11 | **LOW-4** — `lpc_World_Profile.md` §5's comma residue | **OUT OF SCOPE AND DISCLOSED** — still open, accurately recorded |
| 12 | **LOW-5** — `Doc_07` §2F's doubled ch. VIII citation | **OUT OF SCOPE AND DISCLOSED** — still open, accurately recorded |
| 13 | **LOW-6** — `Doc_08` §2 in the Decision Log; the World Profile locus mislabelled | **OUT OF SCOPE AND DISCLOSED** — still open, accurately recorded |
| 14 | **LOW-7** — the count statements disagree | **OUT OF SCOPE AND DISCLOSED** — still open, accurately recorded |
| 15 | **LOW-8** — the Decision Log has no entry for the verification or the second pass | **CLOSED** |

**Closed: 10. Closed in part: 1. Out of scope and disclosed: 4. Closed wrongly: 0. Still open and undisclosed: 0, except the one limb at LOW-2.**

**The claim that what was left is recorded, verified.** The third pass's Decision Log entry closes with a "**Not touched, and why**" bullet. I checked each item it names against the live text:

- *"this entry's own stale counts and loci"* — the entry heading still reads "across six documents"; the ruling as recorded still reads "correct all six documents"; *What it refuted* still cites `Doc_08` §2; *Applied at* still labels the World Profile locus "5 (Force 2A-2)". **All four confirmed present, and all four named in the entry's own "Second limb" bullet as known and uncorrected.** Accurate.
- *"`Doc_07` §2F's doubled ch. VIII citation"* — confirmed still doubled at line 124, two closing parentheses in a row, both contents correct. Accurate.
- *"`lpc_World_Profile.md` §5's comma residue"* — line 292 still reads "different figures**,** and different words". Accurate.
- *"its Disposition's five-of-eight file list"* — line 768 still says "eight files including this one" and then lists five. Accurate.
- *"`Doc_04` §3's Confidence/Gravity Cross-Check, which still excludes row 192 as unread"* — line 34 confirmed unchanged. Accurate, and I agree with both prior verifications that correcting it is a Doc_04 act.
- *"`lpc_World_Profile.md` line 764's report … is now stale as to `Doc_07` §2C"* — confirmed: line 764 still names three superseded statements as standing uncorrected, and `Doc_07` §2C is now corrected. Accurate.

**The record of what was left is accurate at every item it names.** Its only defect is an omission — the Latin splice at LOW-2.

---

# 3. What the third pass newly wrote

**Judgement: true against the source, consistent across files, and neither over- nor under-stated.** I checked every one of the twenty-eight ch. VIII references in the build against the span I derived at §1.

**`Doc_01` §2, the origin sentence.** The duplicate second narration is gone, and with it the splice that attached the direct quotation *"clamored most [eagerly]"* to "the people," a subject the Latin does not supply. What survives is the single correct narration. Each limb checks: the announcement's three recipients, `"all who heard"` as the clamour's subject, the refusal at the episcopate, the yielding attributed to transmarine and African precedent, `"under compulsion and constraint"` exact. **"Came by a different mechanism entirely" is replaced by "came by a different combination, not by a different pattern"** — which is both grammatical and exactly right on the evidence: the combination did differ (designation and consecration are not features of Cyprian's election), the pattern did not.

**The Megalius correction, at all three sites the pass names.** `Doc_01` §2 now reads "an identification Possidius names directly in his own text, *Vita* ch. VIII, in the chapter heading and in the narrative alike, in both the Latin and the facing English." **True, and I verified all four elements** — heading, narrative, Latin, English. `Doc_01` §5 and `Doc_05` line 169 carry the same correction in their own words, and `Doc_05`'s adds the right qualification — *"it remains an identification rather than Augustine's own statement"* — which keeps the editorial-apparatus discipline the section exists to enforce. **Neither overstates: none of the three claims Augustine says it.** This is the pass's own initiative, it is correct, and `Source_Acquisition_Manifest.md` line 29 had predicted the gain four sections of the build ago. Its incompleteness is MED-1.

**`Doc_01` §5's enumeration.** Now gains "and, at that same event, the popular acclamation ch. VIII records, which he refused before yielding under compulsion." **This is the Article 21 test's own evidence paragraph and the addition strengthens rather than unsettles the finding it supports** — which is what the Decision Log says and what Round 2 said. The clause parses; the sentence is long but the enumeration's three members remain parallel.

**`Doc_03` rows 29 and 30.** HIGH-2's false quotation is replaced by a paraphrase — "Doc_01 §2 states plainly, as corrected …, that the congregational-demand pattern recurs at **the episcopate for both men**, and at the presbyterate for Augustine in addition." **I checked this against `Doc_01` §2's live text and it is accurate as an attribution**: §2 contains "it recurs at the episcopate for both men, and at the presbyterate for Augustine in addition" in those words. Both Sources cells now carry ch. VIII; both "office" residues are gone; the "different words" limb of the caution is retained everywhere, correctly, because it remains true — *suffragium* is Cyprian's word and Possidius uses none like it.

**The three "Possidius is unread" closures.** `Doc_05` §11 item 10, `Doc_06` §5 item 2 and `Doc_07` §8 item 7 are closed and each now cites the full read. I re-checked the five sites Round 2 found already cleared — `Doc_01` §5, `Doc_05` lines 169 and 225, `Doc_07` line 74, `lpclex011` Key Sources — **all five still true**. `Doc_06`'s closure adds a claim I tested: that `lpclex011` "now rests its account of his two offices on the *Vita*'s chapters IV and VIII." `lpclex011`'s Key Sources says exactly that. True.

**Consistency across files.** Eight files carry an account of ch. VIII. Five carry the long form with the clamour's subject and the persuasion clause (`Doc_01` §2, `Doc_03` row 30, `Doc_08` Force 1B-2, `lpc_World_Profile.md` §4F, `lpc_Decision_Log.md`). Four compress to "popular clamour" or "the acclamation of all who heard it" (`Doc_05` §4.1, `Doc_07` §2F, `lpclex011`, `lpc_World_Profile.md` §5). **The compressions tell the reader nothing false and I do not raise them**, on the same reasoning Round 2 gave. One observation for a later condensing pass: four sites write "popular clamour … **which he refused**", where Possidius has him refusing *the episcopate*, not the clamour. Functionally identical — he refused what the clamour demanded — and not a finding.

**One characterization I tested hardest, because it is the only place the build asserts a relation between two different sources' accounts of the same act.** `Doc_05` §4.1 says the ch. VIII clamour is "consistent with his own words that the people were one of the two things that persuaded him," and its Construction note says the *"importunity of the people"* passage "sits alongside, not against" the corrected finding. Possidius attributes the yielding to transmarine and African precedent; Augustine (Letter XXXI §4) attributes his acceptance to Valerius's love and the people's importunity. **These are two different accounts of the persuasion, and the build does not claim they are one.** "Sits alongside, not against" is the correct strength, and `Doc_07` §2F states Possidius's own attribution explicitly so the difference is recoverable. Correctly handled.

---

# 4. My own sweep

**Design, arrived at without reading the third pass's.** Fixed-phrase matching is what failed three times; the claim has now appeared in at least eleven phrasings, and a twelfth cannot be enumerated in advance. So I did not enumerate.

1. **Sentence-unit decomposition of every `.md` in the build folder outside `Review-Artifacts/` — 47 files, 13,296 sentence units.**
2. **Structural candidate selection, on four independent predicates**, any one of which qualifies a unit: *(a)* it contains the word **office** at all; *(b)* it pairs a **mechanism/appointment** word (`mechanism`, `appoint`, `came by`, `rose to`, `raised to`, `elevat`) with a **congregational** word (`acclam`, `clamour`, `suffrag`, `popular`, `congregational`, `the people`, `plebs`, `demand`); *(c)* it names **both Cyprian and Augustine** together with any contrast marker (`not`, `rather than`, `different`, `same`, `instead`, `whereas`, `unlike`, `only`, `but`); *(d)* it pairs a congregational word with a contrast marker and an office word. **396 candidates. I read all 396.**
3. **Concept-anchored second pass, on a different predicate**: every sentence containing `acclam|clamour|suffrag|congregational demand|congregational consent|importunity|seizure|popular`. **140 sentences. I read all 140.**
4. **An under-statement pass, which no prior sweep ran.** A carrier need not assert the claim; it can enact it by omission. I selected every sentence that describes Augustine's accession (`designat`, `consecrat`, `coadjutor`, `ordained bishop`, `raised to`, `rise to`, `elevation`) **and contains no congregational term at all**. **15 candidates, all read; all concern rival-consecration validity, provincial placement or chronology. None is an account of his accession that omits the acclamation.**
5. **A ch. VIII fidelity pass**: every reference to the chapter in the build, windowed and checked against the source span.
6. **A class pass on the collateral**: every sentence in the build pairing `unvendored | not vendored | NPNF … editorial note | editorial apparatus | unread | not been read` with `Megalius | Possidius | row 192 | Vita`. This is the pass that produced MED-1.

**Result: no ninth file. No eighth phrasing. No surviving carrier, in any register.**

The files the sweep clears positively, having surfaced candidates in each and found none to be carriers: `Doc_02`, `Doc_04`, `Doc_06`, `Doc_09`, `Doc09_Claims_Register.md`, `Step0_Movement_Scope_Confirmation.md`, `Source_Registry.md`, `Source_Acquisition_Manifest.md`, `Datus_Portrait_Prompt.md`, `Lexicon_Deployment_Index.md`, `lpc_Force_Index.md`, `lpc_Story_Index.md`, `lpc_Gapped_Formation_Precedent.md`, `Doc_04_Superseded_Claims.md`, all seven `Story-Chunks/` and the other eighteen `Lexicon-Chunks/`.

**Two live sentences I examined closely and cleared, because a mechanical sweep would flag them and a careless reader could mistake them.**

- `lpc_World_Profile.md` line 232 opens "at the episcopate for Cyprian … and at the presbyterate for Augustine" and is followed immediately by "**This is corrected against Possidius, on the project lead's ruling of 2026-09-16**" and the full corrected account, closing "**That is the same pattern at the same office**." The opening clause states nothing false — both halves are true — and the correction is in the same breath. This is the World Profile's own stated-then-corrected house convention, used throughout that document. **Not a carrier.**
- `Doc_01` §2 line 26's "the popular-acclamation pathway itself recurs at a different point in his own career … ordained *presbyter* … in 391". True as stated, and the same sentence goes on to give the episcopate its acclamation. **Not a carrier.**

**The remaining hits are historical records and are correctly left standing** — `lpc_Decision_Log.md` lines 388, 430 and 1760, and `lpc_World_Profile.md`'s Disposition, each quoting the refuted wording as what an earlier round said or what the ruling refuted. I apply the same rule both prior verifications applied.

**I independently confirm the third pass's own sweep result.** It is the first of the three to be right about its own reach.

---

# 5. The attribution-resolution check

**Every attribution resolves. Exactly.**

`Doc_05` §11 item 10 is closed in the form `Doc_09` §8 item 9 already uses — a **CLOSED** stamp, then "The original item read:" and the superseded wording preserved verbatim. I verified the precedent exists and matches: `Doc_09` item 9 is closed in that form and has been since before this correction.

Three texts, checked character for character:

| Where | Text |
|---|---|
| `Doc_05_Ecological_Reconstruction.md` line 369, live | The original item read: *"Possidius's Vita Augustini (row 192) is **vendored and unread beyond one identification**."* |
| `Doc_09_Story_Inventory.md` line 128, live | Doc_05's open item 10 records the *Vita* as *"**vendored and unread beyond one identification**"* |
| `Doc09_Claims_Register.md` entry `35371a96`, live | Doc05's open item 10 records the Vita as "**vendored and unread beyond one identification**" |

**The quoted string occurs exactly once in each of the three files and is identical in all three.** `Doc_09`'s quotation resolves against `Doc_05`'s live text. The claims-register entry resolves against `Doc_09`'s live text — and `check_claims.py` confirms it independently, since it is one of the 142 entries it reconciles against live deliverable text.

**A second downstream reference also resolves**: `Doc_09` §8 item 9 cites "Doc_05 open item 10", but does so *inside* its own preserved "The original item read:" quotation, so it is a record of what was written and needs nothing.

**Judgement: this is the best thing the third pass did.** It recognised that rewriting item 10 would have manufactured a fresh instance of exactly the defect HIGH-2 was — a downstream document quoting an upstream document that no longer says it — and it chose a closure form that keeps every attribution live. The reasoning is recorded in the Decision Log in those terms.

**One observation, deliberately not raised as a finding.** `Doc_09` line 128 calls it "Doc_05's **open** item 10", and item 10 is now closed. I do not raise this. `Doc_05` §11 is titled "**Open Items** and Handoff"; the phrase reads naturally as "item 10 of Doc_05's open-items list," which is where it is; `Doc_09`'s own item 9 sits closed inside its own open-items list on the identical convention; and `Doc_09` line 128 goes on in its next sentence to state that the *Vita* has been read at source. Nothing false reaches a reader. Recorded so that the next thread knows it was looked at and judged, not missed.

---

# 6. Findings

## MED-1 — The Megalius correction is right and is propagated one document short: five live statements now report a disclosure `Doc_01` no longer carries, and two standing flags were discharged without record

The third pass removed from `Doc_01` both halves of the disclosure that this world's vendored corpus carries the Megalius identification only through NPNF. I confirmed by `git show` across the sequence that **both halves survived `bf0e0d5f`, `f01b4212` and `11526c3d` and were removed at `86c3e73a`** — so this is this pass's own consequence, not an inherited one.

The Decision Log records the fix as "**The Megalius identification corrected at all three live sites**." Those were the three sites *Round 2 named*. My class sweep finds **five more live statements**, in three files the pass did not open, each reporting in the present tense that `Doc_01` still discloses what `Doc_01` no longer discloses:

| Site | Text |
|---|---|
| `Source_Registry.md` line 59 (row 45) | "the source, via NPNF's own editorial note, for the Megalius/primate-of-Numidia identification **Doc_01 §5 and §9 both disclose as unvendored**" |
| `Source_Registry.md` line 249 (row 192) | "is the underlying source, via NPNF's own editorial apparatus, for the Megalius/primate-of-Numidia identification **Doc_01 §5 and §9 both disclose as resting on an unvendored work**" |
| `Source_Registry.md` line 195 (row 147) | "**Licensed for** `Source_Acquisition_Manifest.md` G3 (Possidius) and the Megalius/primate-of-Numidia geographic question **Doc_01 §5/§9 already discloses as resting on an unvendored source**" |
| `Source_Acquisition_Manifest.md` line 29 | "the underlying source, via NPNF's own editorial apparatus, for the Megalius/primate-of-Numidia identification **Doc_01 §5 and §9 both already disclose as resting on an unvendored work**" |
| `Doc_02_Source_Ecology.md` line 21 | "an identification **Doc_01 discloses as carried in this world's vendored corpus *"only as NPNF's own editorial note"*** … which Doc_01's own text **formerly** stated was *"not vendored in this corpus"* — **corrected at Doc_01 §5 on 2026-09-16, this flag discharged**" |

The last is the sharpest instance: **the sentence marks one half of its own subject as corrected on 2026-09-16 and leaves the other half, corrected the same day, standing in the present tense eleven words earlier.** That is the same shape Round 2 found at `Doc_01` §5 and this pass repaired there.

**And two standing flags are now discharged with nothing recording it:**

| Site | Text |
|---|---|
| `Source_Registry.md` line 249, row 192's Verification Note | "Now that this row is vendored, **Doc_01 §5's and §9's own 'unvendored' disclosure of the Megalius identification's source needs updating to reflect this — flagged here for whoever next touches Doc_01** as a post-disposition edit, not made unilaterally by this row" |
| `lpc_Decision_Log.md` line 252 | "**Flagged, not made unilaterally:** Doc_01 §5's and §9's own disclosure that the Megalius identification rests on *'an unvendored work'* **is now stale** — row 192's own Verification Note flags this for whoever next touches Doc_01" |

**`Doc_01` has now been touched, and the edit those flags asked for has been made.** Neither flag records it. A reader of row 192 is told the update is outstanding; a reader of `Doc_01` finds it done.

Two further sites of the same class I examined and **do not raise**, following Round 2's own rule: `Doc_02` line 59 (§2) and line 83 (§4) scope themselves to *"this pass"* and *"this session"* — Doc_02's own drafting session of 2026-09-08 — and are stale rather than false. They are the disclosures `Doc_04` line 34 relies on, which Round 2 recorded and declined for the same reason.

**Why MEDIUM and not LOW.** It is a live factual inaccuracy at five sites in this world's own instruments of record — the Source Registry, which every chunk's Key Sources cites, and the Acquisition Manifest. It is not the refuted claim, it is not in a participant-facing file, and it does not affect any finding. But it is the diagnosed failure mode, reproduced in a smaller register: **the pass swept the office claim outward and did not sweep the Megalius claim outward**, and then reported the Megalius class closed. Nothing about it is hard to fix, and it should be fixed by whoever next opens `Source_Registry.md`, together with `Doc_02` line 21.

## LOW-1 — The third pass's work is in a commit whose message describes something else

The brief, and the Decision Log's own framing, identify the third pass as `c981f773`. **`c981f773` changes one line**: it edits "per the second Round 2 verification's LOW-6 and LOW-7" to "per the Round 2 verification's LOW-6 and LOW-7". Its 44-line message describes twelve edits across six files, the sweeps, the controls and the trap handling — none of which is in it.

All of that work is in **`86c3e73a`**, committed twenty seconds earlier, whose message records only the project lead's naming ruling and does not mention the correction at all. `86c3e73a` touches `Datus_Portrait_Prompt.md` (naming), `lpc_Decision_Log.md` (both the naming entry and the four correction entries), and `Doc_01`, `Doc_03`, `Doc_05`, `Doc_06` and `Doc_07` (correction only, nothing to do with naming).

**Consequences, stated precisely.** The work exists, is committed, and is correct; nothing is lost. **No document asserts a false hash** — the Decision Log's third-pass entry names no commit, unlike its second-pass entry which correctly names `f01b4212`. The damage is to auditability: `git show c981f773` shows a reviewer a one-word edit under a message claiming a twelve-site correction, and `git log -S` for any corrected string lands on a commit about naming. Round 1 verified `bf0e0d5f` and Round 2 verified `f01b4212` by reading their diffs; a fourth round attempting the same on `c981f773` would find nothing and could wrongly conclude the pass did not run.

**Not a defect in the build's content.** Graded LOW on that basis. The remedy is a Decision Log note naming `86c3e73a` as the commit that carries the third pass; the commits themselves should not be rewritten.

## LOW-2 — MED-4's surviving limb is not in the "Not touched" list

Round 2's MED-4 had two limbs. The first — `Doc_01` §2's duplicate narration, which attached *"clamored most [eagerly]"* to "the people" — is **closed, and closed well**. The second survives:

`lpc_Decision_Log.md` line 1759, the ruling entry's own statement of the finding:

> Latin: `universae plebi… ingenti desiderio clamantibus… recusabat… compulsus atque coactus succubuit`.

Round 2 named this precisely: the ellipsis joins the **dative indirect object** of one clause (`universae plebi`, governed by `insinuavit voluntatem`) to the **ablative absolute** of the next (`ingenti desiderio clamantibus`, whose subject is `omnibus audientibus`), producing a Latin reading in which the people are the clamour's subject. **I re-derived this and confirm it: all four fragments are in the text, and the join is wrong.** The same bullet's English rendering of the same passage is correct and names "all who heard."

**The finding is the disclosure, not the Latin.** The entry's "Second limb" bullet states that the bullets above are left unretrofitted and then enumerates three specific consequences — the "six documents" count, the `Doc_08` §2 locus, the World Profile locus. This is a fourth, in the same bullets, named by the verification the entry is answering, and it is not in the list. The "Not touched, and why" bullet does not carry it either. **Of everything Round 2 raised, this is the one item that is neither closed nor recorded.**

LOW because no build document depends on the Decision Log's Latin, because the English beside it is right, and because the entry does carry a general unretrofitted caveat. It is named here so it is not lost a third time.

---

# 7. `lpclex011_suffrage.md` — fitness to deploy

**FIT TO DEPLOY. Unchanged since Round 2 judged it so, and I reach the same judgement independently.**

I read the whole chunk. The World Meaning uses **"the acclamation of all who heard it"** — the correct subject, which two builder-facing documents still compress away. The Key Sources block states row 192 read in full and names chs. IV and VIII as what the entry rests on; I verified both against `Doc_06` §5 item 2's new claim about this chunk and they agree. The Caution now carries the same-office finding explicitly. World Meaning and Caution do not contradict each other.

The `Aliases` line still carries "popular election," which is exact for Cyprian and not for Augustine's episcopate. An alias is a retrieval key and the body it retrieves does not call Augustine's episcopate an election. I take Round 2's position and would leave it.

**No error in this correction reaches a person.**

---

# 8. Collateral and controls

**Parsing — clean.** I read every passage the third pass wrote or altered, in full, for stranded conjunctions, orphaned subordinate clauses, broken emphasis markers and dangling citations. There are none. `Doc_01` §2's replacement clause "came by a different combination, not by a different pattern" parses and is a real improvement on what it replaced. `Doc_01` §5's enumeration remains parallel across its three members after the addition. A mechanical scan of all seven touched files for empty parentheses, doubled dashes, doubled commas, stranded periods and malformed table pipes returned only house-style artifacts — ellipses inside quotations and adjacent bold spans — and nothing introduced by this pass.

**Duplication — none.** `Doc_01` §2's double narration is gone and no file has acquired one. A cross-file scan for repeated sentences over ninety characters returned only four intentional repetitions inside `lpc_Decision_Log.md`, all of them boilerplate across separate round entries, all predating this pass.

**Cross-references — all resolve.** `Doc_05` §11 item 10's "What remains open is item 7" resolves; item 7 exists and is open. `Doc_06` §5 item 2's pointer to `Lexicon-Chunks/lpclex011_suffrage.md` resolves and its claim about that file is true. `Doc_09` §8 item 9's form is the precedent `Doc_05` item 10 now follows and it exists. `Possidius_Full_Read_2026-09-16.md` exists and is cited consistently at every site. **MED-3's corruption is fully repaired**: `lpc_Decision_Log.md` line 1327 reads "Doc_08 Force 2B-5", and no `§3 (Force 1B-2)B-5` string survives anywhere in the build.

**Contradictions between files — none introduced; four of Round 2's five removed.** `Doc_05` §4.1's body no longer contradicts its own Construction note; `Doc_03` row 30's Significance opening no longer contradicts its close; `Doc_03`'s office residues are gone; `Doc_01` §5's clause no longer contradicts itself eleven words later; `Doc_01` §2's "different mechanism entirely" no longer contradicts the clause after it. **The one new inconsistency between files is MED-1**, and it is between `Doc_01` and three documents that report on `Doc_01`.

**Table integrity — clean.** `Doc_03`'s candidate table holds **28 table lines at a uniform 7 fields each**, headers and separators included. No cell split, merged or dropped by the row 29 and row 30 edits. (Round 2 reported nine fields per row on a counting convention that includes the two empty edges; the uniformity is the point and it holds.)

**Derived artifacts and controls — run by me, with checksums, not assumed.**

```
md5 before : lpc_Force_Index.md  7e9a60ccf9a489ce75e4b76931731088
             lpc_Story_Index.md  5298392e517b76d38706e19ec2787b96

$ python3 scripts/gen_force_index.py
wrote lpc_Force_Index.md  (17 forces, 15 connections, 8 gravities)
$ python3 scripts/gen_story_index.py
wrote lpc_Story_Index.md  (7 stories; tiers 1:6, 2:0, 3:1, 4:0)

md5 after  : lpc_Force_Index.md  7e9a60ccf9a489ce75e4b76931731088
             lpc_Story_Index.md  5298392e517b76d38706e19ec2787b96
```

**Both indexes regenerate byte-identical. Confirmed.**

```
$ python3 scripts/check_claims.py
claims derived from the deliverables : 142
entries in the register              : 142
of those, carrying a recorded check  : 9

OK — every claim about the record is registered, and every register entry still corresponds to live text.
NOTE: 133 claim(s) are registered but still UNVERIFIED.
exit 0
```

**142/142. Confirmed.** Note what this control does and does not establish: it confirms that entry `35371a96` still corresponds to live text in `Doc_09`, which is one half of the attribution check at §5; it does not reach `Doc_05`, and I verified that half by direct string comparison.

**Working tree — clean.** `git status --porcelain` empty before the controls and empty after, which is itself the byte-identical result restated.

---

# 9. The Decision Log

**Accurate, including about the failures. This is the strongest part of the pass.**

The ruling's second limb no longer reads "Outstanding… Not performed." It now reads: "**Second limb, discharged twice and failed twice, then a third correction pass.**" Four entries follow, and I checked each against the artifacts and commits it describes:

- **Verification Round 1** — records the verdict as NOT VERIFIED on 4 HIGH, 4 MEDIUM, 6 LOW. `Doc01_Correction_Propagation_Verification_2026-09-16.md` is 302 lines and returns those counts. Accurate. It also records what Round 1 got right — the source confirmation and the deployment-chunk discovery — rather than only the verdict.
- **Second pass, `f01b4212`** — names the commit, the scale, the six/six/two disposition, and **records the defect it introduced in technical detail**: a `Doc_08 §2` → `§3 (Force 1B-2)` replacement run without a word boundary matching the prefix of `Doc_08 §2B-5`, repaired at `11526c3d`. Accurate at every particular; I verified the mechanism against the diff.
- **Verification Round 2** — records NOT VERIFIED, 2 HIGH, 5 MEDIUM, 8 LOW, quotes the diagnosis verbatim, and records that the round found a carrier three sweeps had missed. Accurate.
- **Third pass** — records the source re-derivation, the two HIGHs, the four outward-sweep sites, the Megalius correction, the §5 enumeration, the three unread closures, the trap and why it was handled that way, the sweeps, the controls, and a "Not touched, and why" list. **Verified accurate at every item except the omission at LOW-2.** It closes "**Not self-certified.** This thread applied the fixes. It does not judge whether they hold."

**The log now records its own failures rather than only its successes**, including a corruption one pass introduced. That is the property a governing record needs and it did not have it three commits ago.

**Two accuracy notes, neither a finding.** The third-pass entry names no commit hash, where the second-pass entry names `f01b4212` — which is how LOW-1 stays undetected from inside the log. And the entry heading still reads "across six documents" where the sweep found eight, which the entry itself discloses as known and uncorrected, correctly.

---

# 10. Article 21

**Not disturbed, and this round does not touch it.** I agree with both prior verifications and with the Decision Log: a correction that converts "the pattern appears at different offices in the two phases" into "the pattern appears at the same office in both phases" deletes a difference, and a test for cross-phase difference cannot be argued toward plurality by the deletion of one. The evidence moves in the direction the existing determination already points.

Round 2's governance observation — that `Doc_01` §5 reached its determination while stating, inside the test's own evidence paragraph, something a vendored Native Confidence A source disproves — **is now fully repaired in the text of the test.** §5's clause no longer says the corpus carries the Megalius identification only as an editorial note, and the enumeration now carries the acclamation. MED-1 is the same claim surviving in documents that *report on* §5, not in §5. That is a record-accuracy matter for whoever next opens `Source_Registry.md`, not a reopening, and I take the same position both prior rounds took.

---

# 11. What I did NOT check

- **I did not read the other twenty-nine chapters of the *Vita*.** I bounded the body, read ch. VIII entire in both languages, read ch. IV's English entire, and ran the vocabulary tests over the whole body span. **I did not audit `Possidius_Full_Read_2026-09-16.md`** and take no position on its other findings. Several build statements now rest on it (the thirty-one-chapter claim, the ch. V presbyteral counter-instance at `lpc_World_Profile.md` line 232, the ch. XIX–XXVII material in `Doc_09`); I verified none of those.
- **I did not re-verify chapter IV's Latin.** Round 1 did. I read its English and confirmed the build's *Vita* IV quotation against it; I did not collate the facing Latin.
- **I did not verify any claim in the affected files other than this one and its immediate neighbours.** `Doc_03`'s *plebs* sweep and its corpus frequency counts, `Doc_05`'s Letter CXXVI and confessor-sweep material, `Doc_07`'s Pinianus material, `Doc_08`'s confidence ratings, and `lpclex011`'s Letter CXXVI material were read for context and not tested.
- **I did not check the Cyprian corpus beyond Ep. XXXIX and Pontius.** Ep. LXVII's "suffrage of the whole brotherhood" corroboration, which `Doc_09` and `lpcstory001` both carry, I read in those files and did not resolve at source.
- **I did not assess `Doc_04`'s Confidence/Gravity Cross-Check.** Its exclusion of row 192 is stale; both prior verifications declined it as a Doc_04 act and so do I. A later round should reach it.
- **I did not read the `Review-Artifacts/` review series** beyond the two verifications this round follows. I confirmed by sampling that they carry pre-correction wording and left them, on the rule both prior verifications applied.
- **I did not check other world-builds.** If `desert`, `don`, `alx` or `hal` carry a claim sourced from `lpc`'s Doc_01 §2, I did not look. Nor did I check `records/`, `canon/` or the corpus map.
- **I did not audit the three control scripts.** I ran them and report their output. `check_claims.py` did not catch Round 2's HIGH-1, which had been live since `Doc_05`'s first draft; I confirm it passes and do not claim its derivation reaches the sentences this correction changed.
- **I did not re-derive the Article 3 / gapped-formation question**, which the World Profile Disposition correctly still carries open.
- **I did not verify the naming ruling** recorded at `lpc_Decision_Log.md` and applied at `Datus_Portrait_Prompt.md`, which shares a commit with the correction. It is outside this brief; I read its diff only far enough to establish LOW-1.

---

# 12. Disposition of this artifact

A verification, not a construction document, and **it fixes nothing.**

**Three findings: one MEDIUM, two LOW. No HIGH. None is a carrier of the refuted claim, and none reaches a participant.** Of Round 2's fifteen, ten are closed, one is closed in part, four are out of scope and accurately disclosed, and **none is closed wrongly**.

**The ruling's first limb is discharged.** The claim the project lead ruled should be removed from this build is not in it. I established the source myself before opening a build file and it supports what the build now says, on every limb. I designed my own sweep and it found nothing three prior sweeps missed. The attributions the third pass went out of its way to protect all resolve, exactly.

**The ruling's second limb is discharged a third time, and this time it holds.**

**The correction can be called closed.** What remains is not the correction: it is a five-site record-accuracy tail on the collateral fix the third pass volunteered, a mislabelled commit, and one Latin ellipsis in a log entry. They are named above, with their loci, so that the next thread to open `Source_Registry.md` and `lpc_Decision_Log.md` can close them in a few minutes and without re-deriving anything.

**One thing should be said plainly, because the first two passes did not earn it.** The third pass was given a diagnosis — you fix the site the finding names and stop — and it did not do that. It swept the class, it found four sites no finding had named, it recognised a downstream-attribution trap that nobody had flagged to it and solved it correctly rather than conveniently, it asserted an exact expected match count before every write after the second pass's unbounded replacement, it ran its own controls, it recorded its predecessors' failures in the governing log alongside its own work, and it declined to certify itself. **Its one substantive miss is the outward sweep it ran on the finding it was given and did not run on the fix it volunteered.** That is a materially better failure than the two before it.
