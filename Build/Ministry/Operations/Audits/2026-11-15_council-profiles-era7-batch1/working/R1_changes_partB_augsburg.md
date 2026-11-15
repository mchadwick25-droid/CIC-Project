## Council profiles, era 7 batch 1, round 1: changes for Part B (Diet of Augsburg 1530)

Files changed: `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1530.brief.txt`, `diet-of-augsburg-1530.entry.json`, `audio/diet-of-augsburg-1530.audio.txt` (regenerated with `mkaudio.py`), and `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/working/records_diet-of-augsburg-1530.json`. README.md, Open-Gaps.md and records.json were not touched. Both JSON files pass `python -m json.tool`. No entry sentence I touched runs past 25 words. The audio script equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph (checked in Python: True). Before each fix I re-opened its source lines with sed. The brief now matches the reviewer's scratch copy word for word (diff empty). I checked each changed sentence against its source.

Claim numbers below are the review's (0-based, as in the file before this round). C13, C14 and C38 are deleted and one claim is inserted after C47, so later indexes have moved.

### Blocking

**B-B1 (the signed confession is not what is held).** Applied. Confirmed at BENS l.31317-31319 (copies lost), l.31330-31348 (German differs, Latin mainly unchanged, Mainz copy of doubtful accuracy) and BOC l.1466-1468 (Latin editio princeps of 1530-31).
- Brief paragraph 2: "the confession in printed texts, part of the final decree, and the two other confessions."
- Entry `uncertain[0]`: as given, with the added Bensow line split into two sentences to keep each under 25 words.
- Entry `record[0].note`: as given.
- Records: the claim on the printed texts (BENS l.31330-31348, modern reconstruction, Dominant Modern Reconstruction) and the absent detail on the two signed copies (BENS l.31317-31319; BOC l.1466-1468) are added.

**B-B2 (the "How could they assent" quote moved to the wrong moment).** Applied. Confirmed at BOC l.3375-3386 (first demand, copy refused), l.3388 (talks begun) and l.3394-3398 (second demand and the question).
- Brief paragraphs 6 and 7: as in the scratch copy. Melanchthon is named at the refusal, so the quote does not read as Pallavicino's.
- Entry: `decided[9]` now opens "When the emperor demanded it again after the talks, the princes would not assent." It is moved after the talks item, which is now `decided[9]`, and it becomes `decided[10]`.

**B-B3 (false absence: Melanchthon's letters only through Waterworth).** Applied. Confirmed at PALL l.17453-17461 (Melanchthon's letter to the legate, "Nullum dogma teniamo diverso dalla Chiesa Romana", OCR garbled) and WAT l.2461-2462. LW4 l.6232-6247 has the Sermon written at Coburg, finished 15 July, and the letter of 5 July. LW4 l.6298 begins the dedicatory letter.
- Records: the Coburg absent detail is rewritten as given, with the detail renamed "Luther's letters from Coburg about the Diet". The Pallavicino claim is added (PALL l.17453-17461; later narrative; Contested).

### Substantial

**B-S1 (April term from one side; "They refused" without a witness).** Applied. Confirmed at WAT l.2497-2505 and l.2541-2544, FPR l.3487-3497 and PALL l.17567-17569, 17580-17582 and 17600-17601.
- Brief paragraph 8: as in the scratch copy.
- Records K10: the Pallavicino side is added.
- Entry `uncertain[9]`: the Pallavicino sentence is added.

**B-S2 (opposition to the September draft given as refusal of the final decree).** Applied in corrected form. Confirmed at WAT l.2541-2547, PALL l.17600-17601, BOC l.11951-11952 and BOC l.11994.
- Entry `outcome[0]`: the review's wording, except that the Pallavicino sentence reads "the principal Protestants rejected the conditions of a first recess, before a second edict" instead of "rejected its conditions". Pallavicino speaks of the recess he has just described (l.17565-17601). He does not speak of a "September draft", so the equation is kept as the reader's (K10), not put in his mouth.
- Records: C80 now reads "the September draft edict". C81 now gives Melanchthon's words and H. E. Jacobs's identification as two witnesses, the second marked modern reconstruction (BOC l.11994). A Pallavicino claim is added (PALL l.17600-17601; later narrative; Contested).
- Consistency fix, same cause: `traditions[0].note` said the Lutherans "refused the Catholic reply and the decree (Melanchthon; Waterworth)". It now reads "They refused the Catholic reply (Melanchthon) and the September draft decree (Waterworth; Pallavicino)."

**B-S3 (section 4 read as binding the Lutheran estates).** Applied in corrected form. Confirmed at BOSS l.1012-1020: "Darzu dass ... solten ... wie dann unsere churfürsten, fürsten und stände ... verwilliget und zugesagt hätten".
- Entry `decided[14]`: the review's single sentence ran to 41 words, so it is split. It now reads: "Bossert prints its fourth section. It names the elector, five princes and six cities. They should side with the emperor and the other estates 'against those who do not hold the most worthy sacrament, and the Anabaptists'. They were not to separate from them. The other estates, it says, had agreed to this."
- Records C74: as given.

### Minor

**B-M1 (the room).** Applied. "In the same hall" is Bensow's (BENS l.31394-31395), and Waterworth has "read in public Diet" (WAT l.2448-2449). The words are cut from the brief. Entry `decided[6]` keeps the room under Bensow.

**B-M2 (Sarpi and Buchheim unmarked).** Applied: "The Venetian friar Paolo Sarpi" and "the Protestant C. A. Buchheim". The Length test's fold of Bensow's identifier ("writes the Swedish Lutheran editor Oscar Bensow") is applied, and the sentence "Bensow, who edited the Swedish church's confessions, tells the day most fully." is dropped.

**B-M3 (Faber without first name).** Applied: "John Faber" (BOC l.12852-12853). "At Augsburg" is cut from the Uppsala sentence, as in the scratch copy.

**B-M4 (Bensow's hedge dropped).** Applied in corrected form. Confirmed at BENS l.31383-31384 and l.31437-31438. In `decided[5]` the review's wording would have made one 26-word sentence. It now reads "Bensow dates it to 12 July. He adds that the emperor is said to have been angered at how Eck and his fellows had done the work." The Ferdinand `people` line is as given.

**B-M5 (teaser).** Applied as given. Beyer read the confession (BENS l.31293-31298).

**B-M6 (absences and library facts recorded as claims).** Applied. C13, C14 and C38 are deleted. C38's two witnesses go into A2's note: "Pallavicino speaks only of an unusual attendance of princes (PALL l.17036-17037), and Sarpi of a hall holding about 200 (SARPI l.12718)." C13's fact stays in the entry `record[0].note`.

**B-M7 (Tetrapolitan: who presented it).** Applied in corrected form. The split is as given, but the Niemeyer cite for "with Hedio" is corrected from l.3950-3955 to l.3956-3959. That is where Niemeyer has "a Bucero adiuvantibus Casp. Hedione et W. Capitone composita" (OCR garbled). l.3950-3955 is only the title "PRAEFATIO" and blank lines. NIEM l.46380-46384 (the four cities' envoys) and ZW2 l.1975-1977 are confirmed.

**B-M8 (when the commission sat).** Applied. Confirmed at WAT l.2440-2446 (commission, then "On the 13th of July the reply ... was completed"), SARPI l.12918-12920, PALL l.17449, FPR l.3443 and BOC l.3388. A new contested claim, "When the commission of seven a side sat", is added with those sides. The talks item in `decided` now reads: "Talks were tried. Sarpi and Pallavicino put them after the reply was read, Pallavicino in August. Waterworth and Sarpi say seven a side met, then three. Waterworth tells the commission before the reply was finished." The Sarpi and Pallavicino sentences that follow are unchanged.

**B-M9 (Campeggio search too narrow).** Applied in corrected form. A3's note now gives the all-texts search, the 1532 Regensburg letter (Theiner l.46768-46800) and the two Pallavicino lines. Two later-narrative claims are added (PALL l.17759-17766; l.17743-17745; Inferential-Thin). I dropped the review's "later" from "a later letter to Aleander". Pallavicino says only "in una lettera ... all'Aleandro ... Nunzio alla Dieta di Spira" (l.17760-17762) and gives no date, so no held line says the letter came after Augsburg.

**B-M10 (census differences).** Not applied to any file, because Open-Gaps is outside this fixer's remit. The text is below, ready to apply.

**B-M11 (README wording).** Not applied to any file, because README is outside this fixer's remit. The text is below, ready to apply.

**B-M12 (tradition note on the legate).** Applied as given. Confirmed at BENS l.31367-31369 and PALL l.17744-17745.

### Two length-paying edits (from the scratch copy, not findings)

With only the listed fixes applied the brief came to 403 words. The scratch copy's two other edits bring it to 399, and both stay faithful to their sources:
- "stayed behind in the castle of Coburg" became "stayed behind at Coburg castle" (LW4 l.6233-6234, "the castle of Coburg").
- "met at Smalcald to plan a common defense" became "met at Smalcald for common defense". This is closer to Waterworth's "for their mutual defence" (WAT l.2599-2601).

### Brief, new figures

399 words (`wc -w`), 2:29.6 at 160 wpm. FK 7.62, Flesch 60.99. Longest sentence 25 words (the unchanged opening). No sentence over 25 words. `briefLength` "about 2 minutes 30 seconds" still holds.

### README text proposed

- `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/README.md` l.10. Replace "and the Catholic reply known only through its opponent, each need a sentence." with "and the Catholic reply, known through its opponent and Catholic historians, each need a sentence." "(about 2:30)" stays.

### For Open-Gaps

- Census, `lutheran-wittenberg-and-its-congregations` `entry.tile`: it says "a confession signed before the emperor at Augsburg in 1530". Bensow says both copies were signed before the reading (bensow_svenska-kyrkans-bekannelseskrifter-swe_bensow1912.txt l.31282-31284), and no held line has them signed in the emperor's presence. Diet of Augsburg council profile, R1 review, 2026-11-15.
- Census edge `lutheran-wittenberg-and-its-congregations--the-reformed-cities-zurich-and-geneva--2`: it has the Formula say the Zwinglians broke away "when the Augsburg Confession was first read out". The held line says "when this Confession was presented" (book-of-concord_symbolical-books-evangelical-lutheran-church_jacobs1911.txt l.26605-26606). Same review, 2026-11-15.
- Census coverage at 1530, three parties without a fitting tradition. The four Upper German cities (Strasbourg, Constance, Memmingen, Lindau) have no census tradition, and the entry files them under `the-reformed-cities-zurich-and-geneva` with Zurich. The Catholic estates and the legate are filed under `the-tridentine-church`, whose census text does not mention Augsburg. The Anabaptists' census text does not mention the 1530 decree. Same review, 2026-11-15.
