# R3 recheck: era 4 batch 8

Round 3, the last review round, by a fresh Opus agent that had not seen the drafting or the earlier rounds, at full effort. Given as the reviewer wrote it.

## Era 4 Who batch 8, round 3 recheck

**Scope.** This is round 3, the last round. I covered all six profiles (eadburga-of-thanet, abbess-bugga, yahya-ibn-said-of-antioch, elias-of-nisibis, adam-jingjing, al-baladhuri). For each I read the brief, the card, the audio script and the records.json entry, and I also read the README. I edited no files.

**Method.**
- **Reading.** I read CLAUDE.md, Who_Profile_Pattern.md (the 14-point checklist and the outside-witness section), R1_review.md, R1_changes.md, R2_recheck.md and R2_changes.md. I used batch 6 R3_recheck.md as the format model.
- **Diff.** I ran `git diff --word-diff 0ff701a2 HEAD` on the batch and checked every round 2 change against its cited lines, read in context:
  - ASS2 l.36620-36800, the whole Kircher error list, with both "Septimo" items
  - MAL l.14140-14180
  - YULE l.2990-3002
  - MAI l.7385-7520
  - ASS1 l.46170-46222
  - SYN l.1726-1738
  - MAC l.610-622 and 13200-13325
  - PO18 l.44370-44390 and 44590-44810
  - PL96 l.69795-69825
  - AASS3 l.126340-126375
  - BONI l.3895-3935
  - BAL l.620-690, 722-795 and 8120-8180
- **Final read.** I reread all six briefs and cards sentence by sentence against their sources. Beyond the lines above, that covered:
  - Kylie: letters IV, VIII, IX, XIII, XIV, XV, XXII, XXIII, XXVIII, XXIX and XXXVIII, and intro l.920-930, 1070-1110, 1180-1195 and 1555-1570
  - the Alcuin index and its spurious-poems note (l.60690-60700, 115010-115026, 116650-116668)
  - Plummer (l.1180-1200, 5860-5875)
  - Brooks's preface (ELI l.80-218) and the life note and part 2 opening (ELI l.8455-8862)
  - Bar Hebraeus (BH3 l.15970-16000)
  - Assemani on the Grammar
  - the PO18 Jerusalem chapter (l.50310-50530) and manuscript list (l.44390-44470)
  - Vasiliev in PO5 (l.29400-29416)
  - Wylie's stele text (MAL l.13565-13700)
  - Hitti (BAL l.895-935, 4530-4565, 7465-7491, 7915-7945)
- **Quotes.** I checked every quotation in the briefs and cards by script against its vendored file, normalized for case, punctuation, whitespace and hyphen breaks. All match. The one exception is Bugga's closing line, which I checked by eye across the page break and running head (BONI l.2451-2459). It is verbatim.
- **Scores.** I rescored each brief with `engine.m1.gates.grade_text`, measured sentence lengths by script in the briefs and in every card string, and rescored every replacement wording below.
- **Audio.** I checked by script that each script equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Each has two tags only. All six pass.
- **Writing.** I found none of the following in the narrator's prose: "not X but Y" or "X, not Y", "never" contrasts, rhetorical questions, aphorisms, thesis openers, tails or colon-reveals. Every colon introduces a quotation. Spelling is American; "honoured" appears only inside quotations.

---

### Round 2 findings

| R2 finding | Status | Note |
|---|---|---|
| R2-B1 | RESOLVED (brief); PARTLY (card, records) | The brief (para 9) now reads ASS2 l.36709-36711 and MAL l.14162-14165 correctly, and "King-tsing" follows YULE l.3000. The card's added last sentence and the records' "once" each misstate Assemani. See R3-M3 and R3-M4. |
| R2-B2 | RESOLVED | MAC l.13276-13314 says "toute cette … campagne de Bulgarie … quatre années entières", from "l'hiver de 990 à 991" to "les premiers mois de l'année 995". The brief and card now say "one campaign". The card sentence is now 31 words. See R3-M5. |
| R2-B3 | RESOLVED | MAI l.7395-7412 and 7506-7508. "Elias gathered rules on inheritance from a work of the catholicos Elias I" matches "collegit ex opere … Eliae patriarchae". The card's remembered[1] and keyWorks[2] are right. The brief's next sentence now has a pronoun drift. See R3-M1. |
| R2-B4 | RESOLVED | ASS1 l.46200-46202 has "post … obitum" (after) and SYN l.1733-1734 has "peu de temps après" (soon after). The brief, card dates, uncertain[2] and the three records sides all match. The README has one stale word. See R3-M7. |
| R2-M1 | RESOLVED | AASS3 l.126368-126371 supports "another name of Abbess Eadburga, to whom Boniface wrote about a vision" ("Creditur Eadburga, cognomento Buggan"; "Extant plures S. Bonifacii ad eam epistolae"). |
| R2-M2 | RESOLVED | PL96 l.69812-69814 has "celebramus". "Bregwin and his church, he wrote, kept" is correct, and the card's "his own church" is too. |
| R2-M3 | RESOLVED | BONI l.3914-3922. The thanks comes before the request, and "already" fits. |
| R2-M4 | RESOLVED | "papas of China" is cut from the brief, and Yule's "Bishop and Pope" stands. The card keeps "papas" beside Kircher's "Pope", which is clear enough read by eye. |
| R2-M5 | RESOLVED | PO18 l.44383-44384 names "L'Épopée byzantine à la fin du dixième siècle". The brief and card are fixed. |
| R2-M6 | ACCEPTED | Brooks is named, and the card and records carry Kugener's 1008. Nothing is told as settled. |
| R2-M7 | RESOLVED, with a side effect | BAL l.8146-8152. The fix puts 'Umar's "he" just before para 7's "he reports". See R3-M2. |
| R2-M8 | RESOLVED | BAL l.736: "From these sources we learn that". |
| R2-M9 | RESOLVED | BAL l.629-630: "as he himself acknowledges". Both brief and card are fixed. |

**Process note, not a finding.** R2_changes.md says two "small cuts" took out "In 1020 Isho'yahb son of Ezekiel was made catholicos" and "Frédéric Macler gives about 1056". Both sentences are still in the Elias brief, and the diff shows they were reworded, not removed. The brief is right; the log describes the change wrongly. The coordinator may want R3_changes to note this.

---

### New findings

No blocking findings.

**R3-M1 (elias-of-nisibis, brief para 9: "In his preface" now follows Ebedjesu).**
- **Problem.** "Ebedjesu of Soba, which is Nisibis, copied them into his book of canons. In his preface, Elias prays for the soul of Elias I."
  - The R2-B3 rewrite made Ebedjesu the nearest antecedent, so a listener first hears "his preface" as Ebedjesu's.
  - Two Eliases then come in one sentence.
- **Source.** MAI l.7451-7458: "Sobensis (Eliae) verba hic attexenda duximus. Si quis, inquit … Mar Eliae patriarchae, cuius animae requiem precamur". The preface is Elias of Nisibis's own, to the inheritance rules.
- **Fix:** "In his own preface to those rules, Elias prays for the soul of Elias I, who died in 1049." The brief comes to 372 words, FK 6.11, Flesch 72.13.

**R3-M2 (al-baladhuri, brief para 7: "he reports" now follows the caliph 'Umar).**
- **Problem.** After the R2-M7 fix, para 5 has "and he ordered the part taken from their church returned", where "he" is 'Umar. Para 7 then opens "During the siege of Damascus, he reports, …". The last male "he" is now 'Umar, and al-Baladhuri was last named in para 3.
- **Source.** BAL l.7926-7938 is al-Baladhuri's own narrative.
- **Fix:** "During the siege of Damascus, al-Baladhuri reports, the commander Khalid wrote terms at the bishop's request." The brief stays at 368 words, FK 7.84, Flesch 64.95.

**R3-M3 (adam-jingjing, card uncertain[3]: the last sentence can be read as a different setter-up).**
- **Problem.** "Assemani lists among Kircher's errors a reading in which the Papa set it up." Item [2] just before it gives Kircher's Adam as "Pope". A reader will likely take "the Papa" to be Adam, which brings back in a softer form the error R2-B1 removed.
- **Source.** ASS2 l.36746-36783.
  - The whole list falls under "in hujus Jazedbuzidi dignitate, patre, patria, & gestis plurimum hallucinatur". The Papa item ("Septimo, … ipse ubique legit Papa, & hunc tabulam … erexisse affirmat") is one of Kircher's errors about Jazedbuzid's rank. It is not a rival setter-up.
  - Malech's English of Kircher has Jazedbuzid set the tablet up (MAL l.14162-14165).
- **Fix.** Replace the item with: "Who set up the stone. The Syriac, in Assemani's Latin and in Kircher's reading in Malech, says the priest Jazedbuzid set it up. Cordier says King-tsing erected it." The Papa point stays in records.json.

**R3-M4 (adam-jingjing, records claim at records.json l.470: "once" contradicts "ubique").**
- **Problem.** "Kircher once read the Papa as setting up the tablet". Assemani says "ipse ubique legit Papa" (everywhere: in both the Prodromus and China Illustrata). "Seventh" is as printed, but the list has two items marked "Septimo", and this is the second.
- **Source.** ASS2 l.36746-36783.
- **Fix:** "Kircher, as Assemani reports, reads 'Papa' throughout (\"ipse ubique legit Papa\") and has the Papa set up the tablet, \"Constituit tabulam hanc Papa\"; Assemani lists this among Kircher's errors about Jazedbuzid (\"plurimum hallucinatur\"), as the second item numbered \"Septimo\" (OCR cleaned); other Adams in the name lists."

**R3-M5 (yahya-ibn-said-of-antioch, card remembered[1]: 31 words, from the R2-B2 fix).**
- **Problem.** "Schlumberger says that only lately, through Yahya's chronicle, has it been known that one campaign of the emperor Basil II in Bulgaria, from about 991 to 995, lasted four whole years." At 31 words it is well past the about-25 limit. R2 said no card sentence was over 25 words, but its own fix wording broke that.
- **Source.** MAC l.13276-13314.
- **Fix:** "Schlumberger says Yahya's chronicle has only lately shown that one campaign of the emperor Basil II in Bulgaria lasted four whole years. It ran from about 991 to 995." (22 and 7 words.)

**R3-M6 (abbess-bugga, card dates: an unsure identification told as settled; checklist 7 and 12).**
- **Problem.** The card dates say "Bregwin of Canterbury gives her burial day as 27 December, with no year". uncertain[2] on the same card asks "Whether Bregwin's Bugga is she". The brief says only "an abbess named Bugga".
- **Source.** PL96 l.69812-69818: "Buggan … quae fuit honorabilis abbatissa". It names no house, mother or letters.
- **Fix, card dates:** "Eighth century. Edward Kylie dates her letter to between 720 and 722, and the last letter about her to between 748 and 754. Bregwin of Canterbury gives the burial day of an abbess Bugga as 27 December, with no year".

**R3-M7 (README, "Corrections", "Elias's death year": "both" is now stale).**
- **Problem.** After R2-B4 the entry gives three positions (Assemani after 1049, Chabot soon after, Macler about 1056), then says "The card gives both".
- **Fix:** "The card gives all three and tags the death year as contested."

---

### Checks that pass, beyond the table
- **Eadburga.** Paras 1 to 11 hold against BONI l.1188-1190, 3441-3460, 3908-3930, 3951-3975, 4464-4500, 4545-4551 and 5166-5185. The card traces and remembered items hold against BONI l.1104-1109, Plummer l.1186-1191, ALC l.60695-60697 and AASS3.
- **Bugga.**
  - Paras 1 to 13 hold against BONI l.2432-2481, 2865-2960, 3118-3195, 5275-5295 and 6036-6060.
  - "Heavier sorrows" tells "more numerous and pressing sorrows" fairly.
  - Kylie's "only Bugga survived" (l.1564) supports remembered[1].
  - The Alcuin index ("Bugga filia regis Centwini … An eadem, cujus exstat epistola ad S. Bonifacium") and the spurious-poems note ("regnante Ina") support uncertain[4].
- **Yahya.**
  - The Jerusalem story matches PO18 l.50312-50510: the governor's extra demands, the refusal at Pentecost, the burned doors and fallen dome, the oil cistern the next day, the pillar.
  - The plan, the two revisions, the move to Antioch in AH 405 and the middle way all match l.44590-44806.
  - The three manuscripts are at l.44430-44452, and Vasiliev on Krumbacher at PO5 l.29409-29412.
- **Elias.**
  - The year 397 schism is at ELI l.8462-8473 and Brooks's 1019 at l.88-89. "For its last years it names none" matches l.211-212.
  - The life note (l.8576-8590: 975, 994, 1002, 1008) is marked as added by others at l.8594.
  - The Bar Hebraeus details are at BH3 l.15974-15988, Assemani's "fortiter restitit … simoniacum" at ASS1 l.46186-46189, and "o frater noster dilecte" at ELI l.8848-8850.
- **Adam.**
  - Para 1, para 5 and the closing quotation match MAL l.13570-13645, and "Olopun … 635 … Chang-an" is at l.13687-13690.
  - Kircher's two renderings and the deacon misreading are at ASS2 l.36641-36650, and Cordier's note at YULE l.3000-3002.
- **al-Baladhuri.**
  - The Saint John's story matches BAL l.8128-8172, including "It is reported", the robe of yellow silk and the al-Ghutah exchange. "An orchard district" rests on l.7491.
  - Khalid's terms are at l.7926-7938 and the Najran terms at l.4559-4560.
  - Hitti's life and judgments are at l.736-789, the method at l.622-640, Medina at l.643-650 and al-Mas'udi at l.918-922.
  - The outside-witness rules hold: the card's Tradition line reads "Outside the church", the label sits beside the role, the brief has no "fought for" beat, and the doubts name Hitti.
- **Pronouns and story.** Apart from R3-M1 and R3-M2, I found no pronoun whose antecedent shifted in round 2, no turning point dropped and no new loose witness.
- **Card sentences.** Three card sentences run 26 to 27 words (Bugga remembered[2]; Elias remembered[1] and keyWorks[2]). That is within "about 25", so I have not counted them as findings. With R3-M6 and R3-M5 applied, no card sentence is past 27 words.

### Scores

Current files, then the same briefs with the R3 fixes applied.

| Brief | Words | FK | Flesch | Longest sentence | After fixes: words / FK / Flesch | Blocking | Minor | Verdict |
|---|---|---|---|---|---|---|---|---|
| eadburga-of-thanet | 350 | 6.43 | 71.89 | 25 (closing quotation) | unchanged | 0 | 0 | CLEAR |
| abbess-bugga | 372 | 8.35 | 62.53 | 25 | unchanged (card only) | 0 | 1 (R3-M6) | CLEAR once R3-M6 is applied |
| yahya-ibn-said-of-antioch | 370 | 7.38 | 67.12 | 25 | unchanged (card only) | 0 | 1 (R3-M5) | CLEAR once R3-M5 is applied |
| elias-of-nisibis | 368 | 6.08 | 72.07 | 24 | 372 / 6.11 / 72.13 | 0 | 1 (R3-M1) | CLEAR once R3-M1 is applied |
| adam-jingjing | 361 | 7.14 | 67.88 | 24 | unchanged (card and records only) | 0 | 2 (R3-M3, R3-M4) | CLEAR once R3-M3 and R3-M4 are applied |
| al-baladhuri | 368 | 7.75 | 65.55 | 21 | 368 / 7.84 / 64.95 | 0 | 1 (R3-M2) | CLEAR once R3-M2 is applied |
| README | | | | | | 0 | 1 (R3-M7) | CLEAR once R3-M7 is applied |

Every brief passes `grade_text` (FK 10 or below, Flesch 60 or above) before and after the fixes. All are within about 365 words: Bugga and Elias reach 372, which matches the README's stated 350 to 372 range. After the Elias and al-Baladhuri edits, rebuild those two audio scripts from their briefs.

### Count
- **Round 2 findings, 13 in all:**
  - Resolved: 9 (R2-B2, R2-B3, R2-B4, R2-M1, R2-M2, R2-M3, R2-M4, R2-M5, R2-M8, R2-M9, counting R2-B3, R2-B4 and R2-M7 as resolved with side effects logged as new findings). Strictly, that is 11 resolved, 1 accepted (R2-M6) and 1 partly resolved (R2-B1, in the card and records only).
  - Not resolved: 0.
- **New blocking: 0.**
- **New minor: 7.**
  - R3-M1: Elias, "In his preface" now follows Ebedjesu.
  - R3-M2: al-Baladhuri, "he reports" now follows 'Umar.
  - R3-M3: Adam, the card's Papa sentence can be read as a different setter-up.
  - R3-M4: Adam, the records' "once" contradicts "ubique".
  - R3-M5: Yahya, a 31-word card sentence.
  - R3-M6: Bugga, the card dates treat Bregwin's Bugga as settled.
  - R3-M7: README, "both" is stale.
- **Process note: 1.** R2_changes.md describes the Elias "cuts" wrongly.

None of the seven minor points is wrong on the scholarship in the briefs except R3-M3 and R3-M4, which are on the card and records. No fourth round is needed. The batch can proceed once the seven exact wordings above are applied and the two audio scripts are rebuilt.

**Files reviewed** (under /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/):
- the six `<id>.brief.txt` files
- the six `<id>.card.json` files
- the six `audio/<id>.audio.txt` scripts
- records.json
- README.md

The earlier rounds are in /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch8/ (R1_review.md, R1_changes.md, R2_recheck.md, R2_changes.md).
