# R4 cap check: era 4 batch 8

One targeted Opus check of only the strings changed after round 3, under Mark's standing ruling of 2026-11-14, by an agent that had not seen the drafting or the earlier rounds. It does not count toward the cap. Given as the reviewer wrote it.

## Era 4 Who batch 8, R4 cap check

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md, R3_changes.md and R3_recheck.md, then ran `git show 6bb99631 -- …/era4/batch8`. That diff touches nine files, which hold the seven R3 strings plus the two rebuilt audio scripts. I opened every cited source span in cic/texts:
- MAI l.7390-7520
- BAL l.7915-7942
- ASS2 l.36700-36800, where the key lines are 36744-36747 and 36779-36782
- MAL l.14140-14175
- YULE l.2988-3003
- MAC l.13268-13320
- PL96 l.69756-69822

I searched with whitespace-tolerant matching and allowed for long-s and OCR noise. I ran `engine.m1.gates.grade_text` on the two changed briefs. I also rebuilt each audio script from its brief by adding "[calmly] " at the start and "[warmly] " before the last paragraph, and compared the result with the file on disk.

**Per string**
- **R3-M1, Elias brief** ("In his own preface to those rules, Elias prays for the soul of Elias I, who died in 1049."): CLEAR.
  - MAI l.7406-7411: Ebedjesu says he will copy out the rules "quas … Elias Sobensis … collegit ex opere … Eliae patriarchae". At l.7437-7438 he introduces "Sobensis (Eliae) verba".
  - Elias then speaks at l.7441-7458: "Mar Eliae patriarchae, cuius animae requiem precamur". So the preface is Elias's own, to those rules, and the prayer is his.
  - The sentence is 18 words. "his own … Elias" resolves within the sentence, and "those rules" plainly means the inheritance rules.
  - "1049" was not changed in this commit.
- **R3-M2, al-Baladhuri brief** ("During the siege of Damascus, al-Baladhuri reports, the commander Khalid wrote terms at the bishop's request."): CLEAR.
  - BAL l.7926-7932: the bishop says "let us make terms for this city", and "Khalid called for an inkhorn and parchment and wrote". The quoted "security for their lives, property and churches" (l.7935-7936) is verbatim.
  - The sentence is 16 words, and it removes the 'Umar "he" drift.
- **R3-M3, Adam card, uncertain[3]**: CLEAR.
  - ASS2 l.36744-36745: "Mar Jazedbuzid Presbyter … erexit hanc tabulam lapideam".
  - MAL l.14158-14162, Kircher's reading: "the Lord Jazedbuzid, Priest … set up this tablet".
  - YULE l.3000: "Adam (King-tsing), who erected the monument". This is Cordier's bracketed note.
  - The Papa misreading is gone from the card.
- **R3-M4, Adam records.json claim**: CLEAR.
  - ASS2 l.36746-36747: "in hujus Jazedbuzidi dignitate, patre, patria, & gestis plurimum hallucinatur".
  - ASS2 l.36778-36782: a second "Septimo" heads "ipse ubique legit Papa, & hunc tabulam illam lapideam erexisse affirmat: Constituit tabulam hanc Papa".
  - "throughout" is a fair rendering of "ubique", and "second item numbered Septimo" is exact. The quotes match the OCR text once cleaned, and the claim says "(OCR cleaned)". The witness range l.36746-36783 covers all of this.
- **R3-M5, Yahya card, remembered[1]** ("Schlumberger says Yahya's chronicle has only lately shown … lasted four whole years. It ran from about 991 to 995."): CLEAR.
  - MAC l.13280-13290: "toute cette … campagne de Bulgarie … qui dura, nous le savons depuis peu, grâce à la Chronique de Yahia, quatre années entières".
  - MAC l.13308-13314 (Schlumberger, "Idem, ibid., p. 57"): "inauguré dans l'hiver de 990 à 991 … ne se termina que dans les premiers mois de l'année 995". "About 991 to 995" is fair for that.
  - The sentences are 22 and 7 words. "It" follows "lasted four whole years" and reads as the campaign.
- **R3-M6, Bugga card, dates** ("…Bregwin of Canterbury gives the burial day of an abbess Bugga as 27 December, with no year"): CLEAR.
  - PL96 l.69763 has "Lullo episcopo Bregwinus". PL96 l.69812-69814: "Diem … depositionis … Buggan celebramus, quae fuit honorabilis abbatissa, cujus etiam dies depositionis fuit vi Kal. Jan.".
  - VI Kal. Jan. is 27 December, and no year is given.
  - "An abbess Bugga" leaves the identification open, which matches uncertain[2] and remembered[2]. The sentence is 21 words.
- **R3-M7, README** ("The card gives all three"): CLEAR. The Elias card's dates field gives Assemani "after 1049", Chabot "soon after it" and Macler "about 1056".
- **Audio, elias-of-nisibis.audio.txt**: CLEAR. It matches the brief exactly, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph.
- **Audio, al-baladhuri.audio.txt**: CLEAR. It matches the brief exactly in the same way.

**Briefs against the gates**

| Brief | Words | FK | Flesch | Result |
|---|---|---|---|---|
| elias-of-nisibis | 372 | 6.11 | 72.13 | passes; within about 365 and the README's 350-372 range |
| al-baladhuri | 368 | 7.84 | 64.95 | passes |

All the changed sentences are 22 words or fewer. None has a "not X but Y" contrast or an AI tell.

**Two notes outside the changed strings (not counted, non-blocking).** Each is for the coordinator to log if they want.
- **al-Baladhuri brief, para 7.** The next sentence, "He also gives the terms the Christians of Najran made with Muhammad", was not changed. Its nearest male subject is Khalid, and heard aloud "gives the terms" can sound like Khalid granting terms. Replacing "He also gives" with "Al-Baladhuri also gives" fixes it with no change in word count. R3-M2 makes al-Baladhuri the reporter the listener is already following, so this is minor.
- **Adam card.** uncertain[1] spells "King-Tsing", while uncertain[3] and [4] spell "King-tsing", following YULE. This dates from before this commit.

**Verdict: CLEAR.** No blocking point. All seven R3 strings and both rebuilt audio scripts match their sources and the pattern.
