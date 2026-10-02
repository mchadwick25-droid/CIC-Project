# Doc_05 Spot-Check — Round 2 (bounded)

**Document checked:** `gallic_Doc05_Ecological_Reconstruction.md`, status "Round 1 review complete; fix round applied (2026-09-10)", 512 lines.
**Checker:** independent, fresh context; no part in drafting Doc_01–Doc_05, in the Round 1 review, or in the Round 1 fix round.
**Date:** 2026-09-10.
**Scope:** bounded verification that the Round 1 fix list (S1–S10, C1–C13) actually landed in the live file, that each fix matches its own stated remedy, and that no fix introduced a new error or a new internal contradiction. **Not** a re-run of Round 1's substantive research; no classification, confidence rating or lens argument re-assessed.
**Read in full:** `gallic_Doc05_Review_Round1.md`; the whole live Doc_05; `gallic_Doc04_SpotCheck_Round2.md` (for format).
**Primary sources opened directly this pass:** `cic/texts/eucherius-lyon_de-laude-eremi_migne-pl50.txt`; `cic/texts/hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt`; `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (via the same flattened working copy with `@@DIV` ids the drafter and Round 1 reviewer used); plus `gallic_Source_Registry.md` (rows 9, 26, 31, 39), `gallic_Doc01_World_Identification.md` §4, `gallic_Doc03_Lexicon_Candidates.md` (entry 4.10 and §9.3). The pre-fix version of Doc_05 was recovered from git (`551ed39`) and diffed against the live file, so that "was this actually changed" is answered from the diff and not from the §11 log.

---

## VERDICT

**DOES NOT FULLY CLEAR — three defects, all narrow, two of them single-line.**

**All ten substantial fixes (S1–S10) are physically present in the body of the document, in the right place, and each matches what the Round 1 remedy actually asked for.** I re-verified every touched quotation and locus against the vendored files independently rather than trusting the document's restated claim: the Eucherius *quae*-clause and its subject, the thirty-three chapters of *Institutes* XII and XII.33's closing sentence, the *Caput II* location and dual Latin of the "sollicita custodia" phrase, *Inst.* IV.2's antecedent and IV.3's "repelled and scorned," Registry rows 9/26/31/39, Gibson's two notes at *Inst.* II.8, Doc_01 §4's [Widely Accepted] rating, and *Inst.* V.5's fasting-capacity subject. **All of them check out.** The one invented detail Round 1 found ("spat on") is gone from the body; "visibly contemplates women's houses," "the last eleven chapters," "the closing statement of the whole formation manual" and "the closing frame" survive nowhere in the document. S5's correction propagated to **all five** downstream locations plus the original, and the five now say something accurate and mutually consistent. Both S3 loci (§2.4(v) and §10C item 2) were fixed and agree with each other. All three tables the fixes touched (§2.2, §7.3, §10A) are structurally intact.

**What is wrong is, once again, this build's named failure mode, plus one fix that was applied faithfully to a remedy that was itself mistaken.**

1. **C3's fix broke a statement that was correct before it** (R1 below). The reviewer's C3 checked the wrong Doc_03 locus; the fix round applied the remedy without re-checking it, and the document now misstates Doc_03.
2. **S8's correction was applied in §3 and left standing in the inhabited passage at §2.4** (R2), so the document now asserts, in the inhabited layer, exactly the claim it labels an editor's inference four sections later — and that sentence is not covered by its own anchor list.
3. **S3's remedy included an explicit §11 instruction that was not carried out** (R3): the search_record still records only XII.9–19, and §2.5(c) still says XII.30's "text not read," although the fix-round log states XII.20–33 were read in full. The *Inst.* IV.1–IV.9 re-read (S5) is likewise absent from the search_record, while the Eucherius re-read (S1) got a proper row.

**Recommendation:** a micro-fix pass on R1–R3, then **self-dispose to Approved to Proceed without a further review round**. Nothing found here touches a classification, a confidence rating, the one-world input, §10C item 2's disposition, or any Doc_04 gravity.

---

## Part A — the assigned fix list, item by item

### S1 — Eucherius's *Lérins* image given to Honoratus ✔ LANDED CLEAN

Inhabited passage 4 (§8) now reads: "**The island takes in what the sea throws up; that is what it is for — it opens its most loving arms to those the world's shipwrecks have cast out.**" The pre-fix clause "Honoratus took the shipwrecked in his arms — that is how they say it of him" is gone (verified against the git diff, not the log). The Honoratus material that remains in the passage ("would not go up to the dignity … put its fillet on the fugitive") is anchored to Hilary, not to Eucherius.

**Independently re-verified in `eucherius-lyon_de-laude-eremi_migne-pl50.txt`:**
- L718: "men Lirinum [Vulg. Lerinam] meam honore com-"
- L722: "piissimis ulnis receptat venientes : ab illo szculi"
- The relative is feminine *quæ* ("quie procellosi naufragiis mundi effusos"), taking *Lirinum/Lerinam* as antecedent ✔ — the island, not the man, is the grammatical subject.
- L728: "disciplinis Bonorato auctore fundata sit" ✔ — a separate clause, **six lines later**, exactly as §11's new search_record row states.

§2.1's and §7.1's already-correct renderings are undisturbed, and §2.1 now adds "row 26, re-read this fix round — the island, not a person, is Eucherius's grammatical subject."

Remedy part (b) was taken in its first form: **§11's search_record gained a dated row** (2026-09-10) recording the row 26 re-read *and* disclosing plainly that "row 26 was reused from Doc_04 at first draft without being re-read at its own locus (Review Round 1, S1)." That is the honest version of the disclosure, and it makes Discipline 2 true rather than papering over it. Remedy part (c) is C9, below. (One residue, not charged: §0's "Built from" list still does not name the Eucherius file among the primary texts read — R4.)

### S2 — the night-office passage voicing Egypt's observance as Gallic "we" ✔ LANDED CLEAN

The passage is substantially re-voiced. Every locus Round 1 named as the failure is now hedged into received teaching:

| Round 1's charge | Live text now |
|---|---|
| "the rest of us sit low, because we have fasted and worked all day" (II.12, Egyptian) | "the rest, **the fathers say**, sit low, because **they** have fasted and worked all day" ✔ |
| "no one coughs, no one sighs aloud … a yawn is not" (II.10, "by the Egyptians") | "No one **there** coughs, **the book says**, no one sighs aloud" ✔ |
| "Between the verses **we** rise and pray standing … not before and not after" (II.7 — the practice II.7 says Gaul fails at) | "Between the verses **they** rise and pray standing … **I have heard it said that some of us in this country cannot wait so long, and hurry to the ground before the psalm is fairly ended**" ✔ |

The frame sentence now reads "so the book teaches, and so we are told to keep it" — which is remedy option (i)'s own formula. The Gloria is kept as the single Gallic-owned first-person element ("this much truly is ours"), which II.8 licenses. **Re-verified in `npnf211` at `iv.iii.ii.vii`:** "when the Psalm is ended they do not hurry at once to kneel down, **as some of us do in this country, who, before the Psalm is fairly ended, make haste to prostrate themselves for prayer, in their hurry to finish the service**" ✔ — the passage now voices this as Gaul's own failing, exactly as the text has it, rather than claiming the Egyptian success. The passage's Cross-world check note was rewritten to match what the passage now does, rather than left asserting the opposite. (One residue at the passage's last two sentences — R6.)

### S3 — the *Institutes* XII chapter-extent claim ✔ LANDED CLEAN in both loci — **but see R3**

**Independently re-verified by full div enumeration of `iv.iii.xii.*`:** Book XII has **thirty-three** chapters, `iv.iii.xii.i` (L21503) through `iv.iii.xii.xxxiii` (L22389), with `iv.iv` (the *Conferences*) opening immediately after ✔. XII.19 is at L22013 and fourteen chapters follow it ✔.

**XII.33's closing sentence, read directly (L22405–22410):** "…not only to acknowledge that **we cannot possibly perform anything connected with the attainment of perfect virtue without His assistance and grace, but also truly to believe that this very fact that we can understand this, is His own gift.**" The document's quotation at §2.4(v) and §10C item 2 is **verbatim** ✔.

Both restatements were fixed and they agree:
- **§2.4(v):** "eleven chapters (IX–XIX, `iv.iii.xii.ix`–`xix`, **all new this pass**) of a thirty-three-chapter book, **not its closing section**"; "still fourteen chapters from the book's actual end"; "Chapters XX–XXXII continue the treatise on pride (examples, its species, its remedies — one of them, XII.30, already cited at §2.5(c) … which is itself the check that XII.19 cannot be the book's end)."
- **§10C item 2:** "occupying eleven chapters of the *Institutes*' thirty-three-chapter final book (XII.9–19) … so the grace-and-effort teaching frames both the treatment of the last fault and the work's own end, **not 'the last eleven chapters' as first stated** (§2.4 v corrects this)."

IX–XIX inclusive is eleven chapters ✔. I read the titles of XX–XXXII: XX–XXII and XXVIII are examples, XXIV–XXV/XXVII/XXIX are species, XXIII and XXXI–XXXIII are remedies — the document's three-word characterization is accurate ✔. XII.30's title, quoted at §2.5(c) and §7.3, is verbatim: "How when a man has grown cold through pride he wants to be put to rule other people" ✔.

The finding's substance survives and is genuinely stronger than the version Round 1 reviewed. **The one part of the remedy not carried out is its last sentence** — R3.

### S4 — the "sollicita custodia" phrase ✔ LANDED CLEAN

§2.1 now reads that the phrase "is **pre-Lérins and dual** — it sits inside *Caput II* (the brothers' homeland, before Venantius's death and before Honoratus ever reaches the island in *Caput III*) and its Latin is plural throughout (*illos*, *eorum*), describing Honoratus **and Venantius** together, not Honoratus alone or the Lérins community," and cross-refers to §1.1's already-correct statement.

**Independently re-verified in the Latin file:**
- Chapter headings by grep: `CAPUT PRIMUM` L185, **`CAPUT 1I` (II) L414**, **`CAPUT 1]` (III) L604**.
- CAPUT II's own heading, L415–418: "Cum Venantio fratre peregrinatur. — Hujus obitus. — Honoratus et Venantius patria abscedunt." ✔
- CAPUT III's heading, L605–608: "Honoratus, fratre mortuo, venit in Italiam … — **Lirinam insulam ingreditur.**" ✔
- The phrase at L460–462: "quam sollicita custedia erga **eorum** salutem qui se doctrine **eorum** mancipaverant" ✔ — inside CAPUT II.
- Dual/plural in the surrounding lines as the document claims: "erga **illos** patria" (L448), "**illis**" (L449), "**eorum** vita" (L451), "**alter alterum**" (L453), "**utrumque**" (L455), "**illorum** gravitas" (L457) ✔. Venantius's death at Methone is narrated at L560–566 — still inside CAPUT II ✔.

The remedy offered a choice; the document took the second option (retain in §2.1, explicitly labelled) and also did the follow-through the remedy asked for: **§10A's Lérins row now reads** "thinner than first drafted: Vincent's one sentence, Sanford's editorial paraphrase of the tutelage chain, and Gennadius's/Hilary's attestations of the episcopate only — the Hilary phrase once read as Lérins-specific is pre-Lérins and about two brothers, not the house" ✔ — near-verbatim what S4's remedy specified. The "**under**, seriously" rating is retained, correctly.

### S5 — the guest-house-year claim and "spat on" ✔ LANDED CLEAN, in all six places

**Independently re-verified in `npnf211`, *Inst.* IV.1–IV.9 read in full (L16296–16520):**
- IV.2's own chapter title is "Of the way in which among them men remain in the monasteries even to extreme old age," and its subject is "their **untiring perseverance and humility and subjection**,—how **it** lasts for so long … for it is so great that we cannot recollect any one who joined our monasteries keeping **it** up unbroken even for a year" ✔ — the antecedent is the perseverance, exactly as the fix now says.
- IV.3: "of set purpose **repelled and scorned** by all of them"; "covered with many **insults and affronts**" ✔ — **no spitting anywhere in the chapter**.
- IV.7 confirms the guest-house year is introduced separately, five chapters later, with Gibson's own note "Cassian stands alone in mentioning a full year as the duration of this service" ✔.

The inhabited sentence now reads: "The fathers of Egypt lay ten days at the door and **were turned away and scorned** … We in this country do not keep up what they keep up; Cassian says he cannot remember one of us who **held to it, whatever it was, unbroken even a year**." The anchor block was rewritten to spell out the antecedent correction and the absence of spitting.

**All five downstream restatements, checked one by one against the git diff:**

| Locus | Pre-fix | Live now |
|---|---|---|
| §2.5(a) | (quote already accurate; C7 over-claim attached) | quote unchanged and accurate; C7 fixed ✔ |
| §3, closing paragraph | "the unkept year (IV.2)" | "the Egyptian perseverance IV.2 says no Gallic monk has matched 'unbroken even for a year'" ✔ |
| §7.3 table row | "Cassian's Egyptian probation, unkept in Gaul (IV.2)" | "The Egyptians' lifelong perseverance and humility, unmatched in Gaul 'even for a year' (IV.2)" ✔ |
| §10A | "if Cassian's Gallic uptake was as thin as IV.2 admits" | "if Cassian's Gallic uptake **of the Egyptians' perseverance** was as thin as IV.2 admits" ✔ |
| §10B, uncertain relationships | "IV.2 says not for a year" | "IV.2 says no Gallic monk matched the Egyptians' perseverance 'unbroken even for a year'" ✔ |

All five, plus the inhabited original, now say the same accurate thing. This is the cleanest of the ten fixes. (One unlisted sixth touchpoint at §4.1 — R7, not charged.)

### S6 — the Lérins "Cell" evidence ✔ LANDED CLEAN

§2.2's Cell/Lérins cell now reads: "**not attested** (corrected, Review Round 1 S6: the sentence at `iii.i` is Cardinal Noris's, 1673 — Registry row 39, general reference only, not a licensed specific claim — quoted, not authored, by Heurtley; see §10D)." The de-licensed quotation itself is not restated, so no row 39 claim is imported.

**Re-verified in `npnf211`:** L10339 "ubique insula, exstructis cellulis, unum velut monasterium", L10341 "**Noris, Histor. Pelag. p. 251.**" ✔ — Heurtley is quoting, not authoring.

**Re-verified against Registry row 39:** "**general reference only, not a specific licensed claim**, until Doc_02 next draws on him directly" (Round 2 N16) ✔. The fix's "not attested" is consistent with that restriction, and consistent with every other Lérins cell in the same column. The remedy's second half — "flag the Licensed For question for the Registry owner in §10D" — is discharged by a **new §10D item 15**, which states the problem, names N16, and correctly says "until then it licenses no specific claim, and this document draws none." ✔

### S7 — the editorial Lérins/abbot identification ✔ LANDED CLEAN

§2.1 now reads: "the *Conferences* XI–XVII were dedicated to two 'holy brothers,' one presiding over a large monastery (Cassian's own text) — the identification of that house as Lérins is the editorial apparatus's (row 17, row 9's own caveat), not Cassian's, and it is **the only traffic in formation-content the sources point to** between the two southern houses, **at editorial strength for the Lérins identification**." Both halves of the remedy, essentially verbatim. "its abbot" and "the only **documented** traffic" are gone.

**Re-verified against Registry row 9's Licensed For:** "Cassian's own text names two 'holy brothers,' one presiding over 'a large monastery' — unnamed. The Lérins/abbot identification is the editorial apparatus's (row 17) … **not for the Cassian-dedication link itself** (Round 2 N4 …)" ✔. The live sentence no longer reverses N4.

### S8 — "the Gloria after every psalm … dozens of times a day" ⚠ LANDED IN §3, **NOT IN THE INHABITED PASSAGE** — see R2

The §3 fix itself is exactly right, and it is the most careful piece of writing the fix round produced:

> "The Gallic Gloria, sung 'with a loud voice' by all, **ends the psalmody in this country** — Cassian's own words are that it usually closes 'the whole Psalmody,' **not that it recurs after each individual psalm** — and it is a practice, he says, the East never heard (II.8); **Gibson's note** reads the Gallic custom as after every psalm … but Gibson's own note at the same locus also warns that Cassian's *Antiphona* here means the whole psalmody of the office, which cuts against a per-psalm reading — the after-every-psalm frequency and the 'dozens of times a day' claim are therefore **this editor's inference** … not Cassian's own statement."

**Re-verified in `npnf211` at `iv.iii.ii.viii`, with both Gibson notes read in full:** Cassian's text — "But with this hymn in honour of the Trinity only **the whole Psalmody** is usually ended," with Gibson's inline note "*Antiphona*. The word must certainly be used here not in the later sense of 'antiphon,' but as descriptive of **the whole of the Psalmody of the office**." And separately Gibson's own: "at the close of each of which the Gloria is said, and not, as in the West, **after every Psalm**. This Western custom which Cassian here notices **seems to have originated in Gaul**." ✔ The document's distinction between Cassian's text and Gibson's inference is exactly accurate in both directions, and "dozens of times a day" survives nowhere in the body.

**But the inhabited passage at §2.4 was not touched** — R2 below.

### S9 — trace 1's "Saint-Sauveur" and its confidence ✔ LANDED CLEAN

§1.3(b) trace 1 now reads: "**A women's house at Marseilles** — 'one for men and one for women, which are still standing' (Gennadius ch. LXII, ancient text, c. 495). **Documented.** (Its identification as **Saint-Sauveur**, alongside Saint-Victor, is Doc_01 §4's, at **Widely Accepted**, without a Registry row of its own — carried at that strength, not this one.)" That is the remedy's own split, essentially verbatim.

**Re-verified in `gallic_Doc01_World_Identification.md`:** §4 (L95) "Cassian's foundation at Marseilles explicitly included a women's house, **Saint-Sauveur**, alongside the men's Saint-Victor **[Widely Accepted]**" ✔, and Doc_01 cites no Registry row for it ✔. The confidence level the fix states matches Doc_01's exactly.

### S10 — "sex" at *Inst.* V.5 ✔ LANDED CLEAN in both loci

**Re-verified in `npnf211` at `iv.iii.v.v`:** chapter title "That one and the same rule of fasting cannot be observed by everybody," and the whole chapter is fasting capacity — "a difference of time, manner, and quality of the refreshment in proportion to the difference of condition of the body, the age, and sex," followed by sickness, old age, moistened beans, fresh vegetables, dry bread, two pounds / one pound / six ounces ✔. Nothing in it concerns women's houses or any female subject ✔.

- **§1.2** now: "*Inst.* V.5 … **a chapter about variation in fasting capacity, not about women's communities**; the one place in the dietary rule a female subject is contemplated at all, carried to §1.3 at that strength and no further." The phrase "visibly contemplates women's houses" survives nowhere in the document (grep: zero hits) ✔.
- **§1.3 trace 9** now: "a fasting-capacity chapter naming 'the condition of the body, the age, and sex' as what varies the rule, not a chapter about women's communities; **what it implies about women's houses is not stated and is not inferred here**" — and it correctly reassigns the women-near-the-house trace to IV.16's "familiarity with women," exactly as the remedy specified ✔.

§1.3(c)'s bounded reconstruction was left alone, correctly (the remedy said it needed no change) ✔.

### C1–C13

| | Status |
|---|---|
| **C1** *Inst.* II.3 Egyptian frame | ✔ §2.4(iv) now: "monasteries stand, '**throughout the whole of Egypt and the Thebaid**,' 'not … at the fancy of every man…'". Verified at `iv.iii.ii.iii`: "And so throughout the whole of Egypt and the Thebaid, where monasteries are not founded at the fancy of every man" — exact |
| **C2** II.5 "lukewarm" | ✔ §2.3 now: "the primitive Church, before 'the fervent faith of the few had … grown lukewarm by being dispersed among the many' (II.5 …, **correctly a historical clause about the apostolic community rather than a rule laid on this monastery**)". Verified at `iv.iii.ii.v` — it is the Acts iv / Evangelist Mark frame ✔. (Residue at §8 — R5) |
| **C3** fourfold-sense tier | ✗ **applied, and now wrong — see R1** |
| **C4** row 34's column | ✔ both loci: §10C item 10 "Registry row 34's **Verification Note** (not the Comparandum Note, corrected…)" and §10D item 5 "in its **Verification Note** (not the Comparandum Note…)" |
| **C5** row 24 grep / item 12 | ✔ §10C item 2 now: "**A negative on two spellings of one place-name does not exclude a self-location by other means** (*insula*, *in monasterio*, a named abbot), so this grep cannot show a self-location either way … and **Doc_04 §10 item 12's question is not answered by this pass**"; and "a post-window text can still report in-window teaching, so the chronology alone does not close the question either." §10C item 12 carries no "answered" claim ✔ |
| **C6** "said the one" | ✔ §6A now "'Never,' **said he**, 'has the sun seen me eating'". Verified at `npnf211` L18489: "“Never,” said he, “has the sun seen me eating,”" — exact |
| **C7** novelty over-claim | ✔ both loci restricted to the office loci: §2.5(a) "The first three (II.7, II.8, III.5) are the first direct, ancient, first-person evidence of Gallic monastic *worship* … (IV.2 and the climate clauses were already in hand from Doc_04 G2 and Registry row 7)"; §3 "Four of these (II.7, II.8, III.4, III.5) are the first direct statements about Gallic monastic *worship*… IV.2 and the climate clauses (I.10, IV.10–11) were already in hand from Doc_04 G2." The two enumerations differ (three vs four) only because the two sentences quote different loci; neither is wrong |
| **C8** *npnf101* omission reason | ✔ §7.3 cell now splits it: "221–224 (Augustine's own) omitted as 'miscellaneous smaller letters'; 225–226 omitted as not Augustine's own." Verified against **Registry row 31**, which states exactly that division ✔ |
| **C9** row 26 in §10D item 13 | ✔ "**26 (lines 700–730 read this fix round — see Review Round 1 S1; not read at first draft, when its material was carried from Doc_04 unre-read)**". Verified row 26's Licensed For still reads "Not yet examined beyond location," so the disclosure is the right one |
| **C10** row 7 extension | ✔ §10D item 13 now reads "*Inst.* II, III, **V.1–28**, IV.3–9, IV.16–20, X.2, and now XII.9–19 and XII.33 read" |
| **C11** OCR normalization | ✔ all three loci disclose it: §1.1 ("the Latin below is normalized from the OCR, whose own spellings differ, **disclosed here rather than left for the reader to discover by grep**"), §1.3 trace 11, §2.1 |
| **C12** Sanford's layer | ✔ §4.1 now "(Eucherius's phrase, **quoted — not paraphrased — by Sanford**, p. 12; editorial layer, no Registry row of its own)" |
| **C13** two line ranges | ✔ both reconciled in the body: §3's *Vita* IX now "file lines **766–787** … reconciled with §11's search_record"; §1.1's Hilary window now "**428–462** (reconciled with §11's search_record)". (One stale residue in §11's own review-requirement block — R5) |

---

## Part B — findings

### R1. The C3 fix introduced an error into a statement that was correct before it

Doc_05 §6C item 4 **before** the fix:

> "The fourfold sense (*Conf.* XIV.8, Doc_03 4.10) — attested, Cassian-only, **held at Tier 3 by Doc_03 pending this lens**…"

Doc_05 §6C item 4 **now**:

> "…held at **Tier 2** by Doc_03 (corrected, Review Round 1 C3) **pending this lens**…"

`gallic_Doc03_Lexicon_Candidates.md` **§9.3, "Terms considered and deliberately not carried"** (L765) says, in its own words:

> "**The four senses of Scripture** (*Conf.* XIV.8) — attested and technical, but the Gibson footnote's medieval mnemonic is editorial; **held at Tier 3 under 4.10** rather than as its own entry, **pending Doc_05's interpretive-ecology lens**."

The pre-fix sentence was a near-verbatim restatement of that line, "pending this lens" included. Round 1's C3 checked a different thing — Doc_03 **entry** 4.10's own tier line, which does read "**Tier (est.). 2**" — but entry 4.10 is *contemplation / practical vs. theoretical knowledge*, not the fourfold sense; §9.3 is the place where Doc_03 rules on the fourfold sense specifically, and it rules Tier 3. So C3 was a mistaken finding, and the fix round applied it without re-opening Doc_03 to check. **The document now misstates Doc_03 in the one sentence where it reports Doc_03's holding on this term** — and it does so with a "corrected, Review Round 1 C3" stamp on it, which will discourage the next reader from checking.

This is the sharper version of the build's failure mode, in an unusual direction: not a fix claimed and not applied, but a fix applied faithfully to a remedy that should have been resisted. Nothing in the ecology turns on it — §6C item 4's substantive finding ("present but not organizing") is this document's own and is unaffected — but Doc_06 inherits tier estimates from exactly this kind of sentence.

**Fix:** restore "Tier 3," citing Doc_03 §9.3 rather than entry 4.10, and record in §11 that Round 1's C3 was checked against Doc_03 and not sustained. (A disagreement-log entry is the right home for it; §11's disagreement log currently says "none.")

### R2. S8's correction was applied in §3 and left standing in the inhabited passage at §2.4 — the document now contradicts itself in the layer Round 1 called its weakest

§3, "How worship shapes theology," **after** the fix:

> "…Cassian's own words are that it usually closes 'the whole Psalmody,' **not that it recurs after each individual psalm** … the after-every-psalm frequency … is therefore **this editor's inference** … **not Cassian's own statement**."

§2.4, inhabited passage 2, **untouched by the fix round** (identical in the pre-fix and live files):

> "We stand and sing 'Glory be to the Father' together **after every psalm**; he says the East never heard it."

That sentence is a Marseilles junior asserting, in the first person, as his own house's practice, the exact frequency the document now says is Gibson's editorial reading of Cassian rather than Cassian's text. Three separate disciplines the document sets for itself are engaged at once: Discipline 3 ("Gibson's … apparatus … named as editorial wherever drawn on and **never counted as an ancient voice**"), Discipline 6 (each passage "built **only** from loci cited immediately after it"), and the drafter's own review requirement (d) ("any sentence not covered by the anchor list beneath it"). The passage's anchor for this sentence is "II.8 (Gloria 'never heard anywhere throughout the East')" — which supports the second half of the sentence and not the first.

Round 1's S8 locus line named §3 and §2.5(a), so the fix round can claim technical compliance with the enumerated remedy. But this is precisely the Doc_04 R3 shape — a correction made in the analytical layer and left standing where the same claim lives elsewhere — and here it lands in the inhabited layer, which Doc_10 inherits and which Round 1 identified as the document's weakest.

**Fix:** one clause. Either "We all stand and sing 'Glory be to the Father' at the end of the psalms; he says the East never heard it," which is what II.8 supports, or keep the frequency and mark it as told rather than kept. No anchor needs to change.

### R3. S3's remedy included an explicit §11 instruction that was not carried out, and the fix round's own new reading is not in the search_record

Round 1's S3 remedy closes: "**Record XII.20–33 as read or as still unread in §11, whichever is true.**"

§11's search_record (L489) is byte-identical to the pre-fix version on this point. Its `npnf211` row still reads "**XII.9–19** (`iv.iii.xii.ix`–`xix`, lines 21715–22030)" and nothing else about Book XII. No fix-round row was added for `npnf211` at all — the only row the fix round added (L492) is the Eucherius one, which is exemplary and shows the drafter knew how to do this.

Three consequences, all small, all in the same direction:

1. **§11 no longer matches what the document rests on.** §2.4(v) now characterizes XII.20–XXXII substantively ("examples, its species, its remedies") and quotes XII.33 as the *Institutes*' terminus; §10C item 2's re-grounded disposition rests on XII.33. None of that reading is recorded. Round 1's own disposition asked the spot-check to verify "that §11's search_record now matches what the document actually rests on"; on this point it does not.
2. **§2.5(c) still says XII.30's "text not read"** — "(XII.30, title, `iv.iii.xii.xxx`, **seen this pass in the div index; text not read**)". If XII.20–33 were read in full this fix round, as §11's log entry states twice, that clause is now false. It is a leftover from the first draft's read scope that the fix did not sweep.
3. **§10D item 13's row 7 extension records "XII.9–19 and XII.33"** — omitting XII.20–32, which the fix round read and which §2.4(v) uses.

The same omission applies to S5's new reading: the log states "*Inst.* IV.1–IV.9 re-read in full this fix round," and nothing in the search_record records it.

**Fix:** add one search_record row dated 2026-09-10 for `npnf211` (XII.20–33 read in full, lines 22030–22410; IV.1–IV.9 re-read, lines 16296–16520), strike "text not read" at §2.5(c), and extend §10D item 13's row 7 entry to "XII.9–19 and XII.20–33."

### Minor residues (noted, not charged — none is a failed fix)

**R4. §0's "Built from" list still omits the Eucherius file.** L9 names `npnf211`, `npnf203`, the Salvian, the Hilary of Arles and the Faustus files as "the vendored primary texts, read directly this pass," but not `eucherius-lyon_de-laude-eremi_migne-pl50.txt`, which §11's new row now records as read. Round 1's S1(b) asked only for the search_record entry, so this is not a missed fix — but §0 is the list a reader consults first.

**R5. Two stale strings the fixes did not sweep.** (i) §11's review-requirement (i) still says "Hilary of Arles, **file lines 447–462**," the very range C13 reconciled to 428–462 in the body. (ii) §8's "Fears" paragraph still opens "The fear this world names most is not damnation but *cooling*: 'lukewarm by being dispersed among the many' (II.5)" — the same primitive-Church clause C2 restated at §2.3, here still doing duty as a communal fear. §8 was not a C2 locus and the framing is looser than §2.3's was, so this is an observation about completeness, not a failed fix.

**R6. Inhabited passage 3's last two sentences keep an unhedged first person over explicitly Egyptian material.** "He who came late stands outside till **we** are dismissed…"; "Whoever is suspended prays with no one; **if I pray with him** I go where he has been sent." *Inst.* II.16 frames that discipline as the Egyptians' ("if one **of them** has been suspended…"), verified at `iv.iii.ii.xvi`. The passage's own frame sentence ("so the book teaches, **and so we are told to keep it**") is remedy option (i)'s formula and does license first-person statements of what the house is told to keep, so I do not charge this — but it is the one place in the re-voiced passage where the hedge is carried by the opening sentence alone rather than locally.

**R7. §4.1 carries a sixth, unlisted IV.2 restatement that the fix did not reach.** "The whole apparatus is prescriptive; how much of it any Gallic house kept, Cassian himself doubts (IV.2)." IV.2 doubts Gallic *perseverance and humility*, not the apparatus. This is looser than the five restatements Round 1 enumerated, it was not on the fix list, and after the S5 correction it is no longer contradicted by anything — but it is the same drift in a milder form.

---

## Part C — sanity check on the §11 "Round 1 fix round" log

The log entry (L498–509) is accurate in its substance: **ten substantial fixes are described and ten are genuinely in the body, each doing what the entry says it does**, and the C1–C13 roll-up at L509 describes thirteen fixes that are all physically present. Nothing is claimed as present that is wholly absent — the sharper version of this build's recurring failure did **not** recur here. The S1 entry's disclosure that row 26 "was reused from Doc_04 at first draft without being re-read at its own locus" is voluntarily self-incriminating and is the right way to record it.

Four claims in the log do not survive checking:

1. **L498, "each fix grep-verified against the live file before being logged here."** The same sentence Doc_04's fix round used, and with the same over-reach. A grep for "after every psalm" returns the §3 fix *and* the untouched inhabited passage on the same screen (R2); a look at the search_record while writing "XII.20–33 read in full" would have surfaced R3 immediately. The verification claim is broader than what was actually verified.
2. **L498 and L501, "*Inst.* XII.20–33 read in full this fix round."** I have no reason to doubt this was done — XII.33's quotation is verbatim and the XX–XXXII characterization is accurate, which is hard to fake — but the document's own bookkeeping (§11's search_record, §2.5(c)'s "text not read," §10D item 13) does not record it (R3).
3. **L506's S8 entry, "the parallel over-claim at §2.5(a) (also C7) corrected."** §2.5(a) never carried the S8 over-claim; the pre-fix text there quotes II.8 accurately and carries no "after every psalm" or "dozens of times a day." What was corrected at §2.5(a) is C7's novelty claim, which is a different finding. The entry merges two findings and, in doing so, reports S8 as corrected in two places when it was corrected in one — while the place it actually still needs correcting (the inhabited passage) is not mentioned.
4. **L503's S5 entry, "all four downstream restatements (§2.5(a)/C7, §3, §10A, §10B, §7.3)"** — the parenthesis lists five, and all five are in fact fixed. A miscount in the safe direction, unlike the other three.

**Disposition claim at L512** ("all 10 substantial and all 13 cosmetic findings fixed and self-verified") is accurate for S1, S2, S4, S5, S6, S7, S9, S10 and for C1, C2, C4–C13; **overstated for S3** (fixed in the body, not in the record), **overstated for S8** (fixed in the analytical layer, left standing in the inhabited one), and **wrong for C3** in a way the phrase "self-verified" makes worse rather than better.

---

## SUMMARY

| | Result |
|---|---|
| Substantial fixes (S1–S10) present in the body | **10 of 10** |
| Substantial fixes matching their own stated remedy | **10 of 10** |
| Substantial fixes leaving a self-contradiction | **1** (S8 → R2) |
| Substantial fixes with an unapplied part of their own remedy | **1** (S3's §11 instruction → R3) |
| Cosmetic fixes (C1–C13) applied | **13 of 13** |
| Cosmetic fixes that introduced a new error | **1** (C3 → R1) |
| S5's propagation to its five downstream loci + the original | **6 of 6, mutually consistent** |
| S3's two restatements (§2.4(v), §10C item 2) agreeing with each other | ✔ |
| Quotations/loci re-verified against vendored sources this pass | 21 (all touched by S1, S3, S4, S5, S6, S8, S9, S10, C1, C2, C6, C8) |
| Re-verified quotations found wrong | **0** |
| Registry rows / prior documents re-read to check a fix's claim | 6 (rows 9, 26, 31, 39; Doc_01 §4; Doc_03 entry 4.10 + §9.3) |
| Prior-document claims found misstated by a fix | **1** (Doc_03 §9.3 → R1) |
| Tables disturbed by a fix (§2.2, §7.3, §10A) | **0** — all three structurally intact |
| Classifications, confidences, cross-node statuses or §10B input disturbed | **0** |

**Single most important finding: R1** — the one fix that made the document less accurate than it was before, applied to a Round 1 finding that was itself mistaken, and stamped "corrected" in the text so the next reader will not look.

**Runner-up: R2** — S8's over-read was corrected in the analytical layer and left standing in the inhabited layer, where the same document now says the opposite thing about the same practice, in a sentence its own anchor list does not cover. This is the identical shape as Doc_04's R3, one document later.

**Third: R3** — the one enumerated instruction in a remedy that the fix round did not execute, and the reason §11's search_record no longer matches what §2.4(v) and §10C item 2 rest on.

**All three defects are one- or two-line edits and none reopens anything.** The evidentiary substance of this fix round is genuinely good: the Eucherius subject, the thirty-three chapters, the *Caput II* location, IV.2's antecedent, the Noris attribution, Gibson's two notes and Doc_01's confidence rating were all checked at their own loci by the fix round and all of them are right. What failed is what has failed in every prior document of this build — the last ten per cent of a fix: the other place the claim lives, and the record of what was read.

---

## DOCUMENT LOG

- **Checker:** independent, fresh context; no drafting involvement in Doc_01–Doc_05, no part in the Round 1 review or the Round 1 fix round.
- **Scope:** bounded spot-check of the enumerated Round 1 fix list (S1–S10, C1–C13); confirmation that each fix matches its own stated remedy; independent re-verification against the vendored primary sources of every quotation and locus the fixes touched; a targeted check of S3's two restatements against each other and of S5's five claimed downstream propagations; a disturbance sweep for new internal inconsistencies, including a full pre/post diff against the pre-fix file recovered from git; and an accuracy audit of §11's "Round 1 fix round" log entry against the document body.
- **Method:** every ✔ above was checked in the live file or by grep-and-context against `eucherius-lyon_de-laude-eremi_migne-pl50.txt`, `hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt`, the flattened `npnf211`, `gallic_Source_Registry.md`, `gallic_Doc01_World_Identification.md` or `gallic_Doc03_Lexicon_Candidates.md`. The document's own restatement of a source was never accepted as the check, and the §11 log was never accepted as evidence that a fix was applied — "was this changed" was answered from a git diff of `551ed39` against the live file. *Institutes* Book XII's chapter count was established by full div enumeration, not by reading the last chapter cited.
- **Not done:** no re-run of Round 1's substantive research; no re-assessment of any classification, confidence rating, gravity, or §10B one-world input; no reading of unvendored sources; no live research; no check of Salvian, `npnf203`, or the Faustus file, which no fix touched; no independent re-derivation of the eleven-dimension mapping at §0 or of §10A/§10B's assessments.
- **Disposition: MICRO-FIX PASS on R1–R3, then self-dispose to Approved to Proceed.** No further review round is warranted — R1 and R2 are single-clause edits, R3 is one search_record row plus two stale clauses, R4–R7 are optional, and nothing found here touches the classification layer that Doc_06, Doc_07 and Doc_08 consume. R1 additionally warrants a line in §11's disagreement log, which currently reads "none": Round 1's C3 was checked against Doc_03 this pass and is not sustained.
