## Council profiles, era 7 batch 1: review round 1, Part A — Diet of Worms 1521

**Council.** `diet-of-worms-1521`
**Files.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-worms-1521.brief.txt`, `audio/diet-of-worms-1521.audio.txt`, `diet-of-worms-1521.entry.json`, `records.json` key `diet-of-worms-1521` (104 claims, 10 contested claims, 9 absent details), `README.md` (the "Diet of Worms (about 2:30)" line).
**Brief.** 401 words by `wc -w` and the batch's `grade.py` (2.51 min at 160 wpm, one word over the 400-word ceiling). `grade_text`: FK 6.83, Flesch 68.75. Longest sentence 23 words ("In the Wartburg, Buchheim writes, ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Reviewer.** Independent Opus, full effort, first sight of these drafts. No profile file edited. No model calls, no network, no paid services. `git diff origin/main -- cic/texts/` is empty, so every line number below is good on main.

Abbreviations under `cic/texts/`: FOXE4 = `foxe_acts-and-monuments-v4_cattley-townsend1837.txt`; PALL1 = `pallavicino_istoria-del-concilio-di-trento-parte1-ita_1664.txt`; MIRBT = `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`; TT = `luther_table-talk_bell1886.txt`; FP = `luther_first-principles-reformation_wace-buchheim1885.txt`; WAT = `council-of-trent_canons-and-decrees_waterworth1848.txt`; SARPI = `sarpi_history-of-the-council-of-trent_brent1676.txt`; ARM = `arminian-magazine_vol-1_1778.txt`; LV2 / LV3 / LV4 = `luther_works-v2-selected_jacobs-spaeth1916.txt` / `-v3-selected_various1930.txt` / `-v4-selected_various1931.txt`; LHYM = `luther_hymns_bacon-allen.txt`; ZINZ = `zinzendorf_sammlung-oeffentlicher-reden-pennsylvania-deu_buedingen1746.txt`; SCHW = `schwenckfeld_corpus-schwenckfeldianorum-v1-earliest-letters-deu-eng_hartranft1907.txt`.

**Verdict: REVISE.** The brief is a strong piece of writing: it opens in the room, tells both sides from their own held witnesses, quotes Foxe and Buchheim verbatim, and reads clean with no AI tells. Every quotation in the brief and entry checks out against its file, and the German and Italian renderings are faithful but for one list (M6). Three blocking findings. The brief's "Here I stand" sentence leans on Luther's Table Talk as if it told the speech of 18 April. It does not: its "next day" is the talks with the bishops. The same sentence also hides its one named witness behind "later tellings". The brief calls Buchheim "a Protestant editor", which no held line supports. And the entry says no other held witness names the Edict's drafter, when Herrnschmid (in damaged print) does, as the entry's own `uncertain` list says. Four substantial findings follow. One concerns the first-hearing dispute: it is miscast in the records, but the brief's "17 April" stands. Twelve minor findings close the list. On the length test, the brief earns its length (see "Length test" below), but the README's reason for it is worded wrongly.

A scratch copy of the brief with every brief fix applied is at `/tmp/claude-0/-home-user-CIC-Project/961c4153-8c1b-50d3-a603-34620231affd/scratchpad/w/worms.fixed.txt`: 400 words, FK 7.03, Flesch 67.90, longest sentence 23 words. The audio script must be regenerated from the fixed brief.

---

## Blocking

**A-B1. Blocking (misleading evidence for a contested point, and a role standing in for the named witness).** Brief, paragraph 5: `Later tellings give the German "Hier stehe ich," but his own memory of the day, in his Table Talk, does not.`
- The Table Talk does not tell the speech of 18 April. After the first hearing it says: "Then they gave me one day and one night. The next day I was cited by the Bishops and others, who were appointed to deal with me touching my revocation" (TT l.3563-3565). It goes on to the talks with Joachim, Cochlaeus and the doctor of Baden, the talks Foxe puts after St George's day (FOXE4 l.22178-22200). It has no speech before the Diet at all. So its silence on "Hier stehe ich" tells the listener nothing about the words. The brief offers that silence as the counter-witness.
- "Later tellings" (plural, unnamed). Only one held telling gives the German "Hier stehe ich": Herrnschmid in Wesley's magazine, "He added these German words, 'Hier flehe ich: ich kan nicht anders: Gott helfe mir! Amen.'" (ARM l.9300-9311, OCR "flehe"). The entry's own `record` note says the same: "The one held telling that gives the German 'Hier stehe ich'". Zinzendorf has "da ſtehe ich" (ZINZ l.30869-30870) and Carlyle has English (LHYM l.651). Who checklist item 5: no role standing in for a named witness.
- Fix, brief (replace the sentence; 19 words): `Of our sources, only Herrnschmid's Life of Luther, printed by John Wesley in 1778, gives the German "Hier stehe ich."`
- Fix, entry `uncertain[2]`: "The words are absent from Pallavicino, Sarpi, Waterworth and Buchheim. Luther's Table Talk gives no speech before the Diet: its 'next day' is the talks with 'the Bishops and others'. No held editor discusses whether he said them."
- Fix, records `contested_claims[0]` sides: move the Table Talk out of "Held tellings without it" and add: "Luther's Table Talk tells no speech of the second hearing; its 'next day' is the talks with 'the Bishops and others' (luther_table-talk_bell1886.txt l.3563-3565)."

**A-B2. Blocking (a label no held line gives).** Brief, paragraph 8: "Buchheim, a Protestant editor, says it went out without the Diet's formal consent." Entry `record` note for Buchheim: "Protestant and openly hostile to Charles."
- No held line gives Buchheim's confession. The title page gives only "C. A. BUCHHEIM Ph.D. PROFESSOR OF THE GERMAN LANGUAGE AND LITERATURE IN KING'S COLLEGE LONDON", in a volume from the "LUTHERAN PUBLICATION SOCIETY" for "the fourth centenary of Luther's birth" (FP l.106-121). I searched FP, the `cic/texts` README, AUTHORS.md and the three other files that name him (LV2 l.1937, 6448, 11188; the Skála and Wyclif files). None says what church he belonged to. This is the "D:r Beyer" fault: an identity given to a real person that no held line supplies, and one that may be wrong.
- His side is derivable, and that is what the pattern asks to be marked. He calls Charles "a bigoted Roman Catholic at heart" (FP l.2358) and the Edict "the illegally issued Edict" (FP l.2529-2530). He praises "Luther's manly, nay heroic, conduct" (FP l.2576).
- Fix, brief: `Buchheim, an 1885 historian on Luther's side, says it went out without the Diet's formal consent.` (15 words)
- Fix, entry `record` Buchheim note: "Writes for Luther's side, in a Lutheran Publication Society volume for Luther's fourth centenary, and is openly hostile to Charles ('a bigoted Roman Catholic at heart'). Quotes Charles's declaration in English and says the Edict was put out on 25 May." (This also carries M10.)

**A-B3. Blocking (false absence in the entry).** Entry `decided[10]`: "Pallavicino says Aleander drew up the Edict, which the emperor's councils then revised. No other held witness names its drafter."
- Herrnschmid names Aleander. ARM l.9403-9406: "Jefe Worms on the 26th of April. And quickly after, ... ublithed his Decree of, Banifhment againtt him, ... jleander. the Pope's Legate: in which it 'is af- / drawn ys i at his Writings breathe nothing..." The print is damaged, but "drawn" and "Aleander the Pope's Legate" stand in the same clause. The entry's own `uncertain[10]` says "Herrnschmid seems to say the same, but the print is damaged", and records `contested_claims[7]` says so too. `decided[10]` contradicts both.
- Fix, entry `decided[10]`: "Pallavicino says Aleander drew up the Edict, which the emperor's councils then revised. Herrnschmid seems to say Aleander drew it up, but the print is damaged. No held witness names another drafter."

---

## Substantial

**A-S1. Substantial (an act's words given to the wrong subject).** Entry `issue[1]`: "Sarpi gives the Edict as saying Luther was fetched by a herald. He came 'not to know and judge the things that concern Faith, which belongeth to the Pope alone'."
- SARPI l.9743-9746: "he reſolved to ſend to fetch him by one of his Heralds, not to know and judge the things that concern Faith, which belongeth to the Pope alone, but to bring him into the right way with good perſwaſions." The purpose is the emperor's, in sending for Luther. It is not Luther's purpose in coming. "He came" makes Luther the one who came "not to know and judge", which reverses the sense.
- Fix: "Sarpi gives the Edict as saying the emperor sent a herald to fetch Luther, 'not to know and judge the things that concern Faith, which belongeth to the Pope alone', but to bring him back by persuasion."

**A-S2. Substantial (a first name and title no held line gives, and a title that contradicts the held line).** Entry `people`: `"Hieronymus Vehus" ... "Chancellor of Baden; spoke for the princes at the talks (Foxe's 'Dr. Voeus')"`. Entry `decided[5]`: "Their spokesman, Vehus, ...". Records `claims[33]`: "... Peutinger and Vehus".
- Foxe gives "Dr. Voeus, the marquis of Baden's chaplain" (FOXE4 l.22193). The Table Talk gives "a Doctor unto me, belonging to the Marquis of Baden" (TT l.3598). A search of all `cic/texts` for "vehus" finds no line naming him, and neither "Hieronymus" nor "chancellor" is held for him. The held title is "chaplain", so "Chancellor of Baden" is not just unsupported but against the held line.
- Fix, entry `people`: `{"name": "Dr. Voeus, chaplain of the marquis of Baden", "verdict": "NOT SCORED", "part": "Spoke for the princes at the talks (Foxe); 'a Doctor ... belonging to the Marquis of Baden' in Luther's Table Talk"}`. Entry `decided[5]`: "Their spokesman, Dr. Voeus, the marquis of Baden's chaplain, said ...". Records `claims[33]`: replace "Vehus" with "Dr. Voeus".

**A-S3. Substantial (a contested claim that names the wrong dispute; the brief's date stands).** Records `contested_claims[2]` "The day of the first hearing", with 17 April (Pallavicino, Sarpi, Waterworth) against Foxe's "the fourth day after his repair". The same framing appears in entry `uncertain[4]` and `datesNote`.
- Foxe gives no calendar date for either hearing. He gives "The fourth day after his repair" (FOXE4 l.21734), counted from an arrival "about seventeen days after Easter" (l.21696-21697). His other anchors are "Upon the Friday following" for the emperor's letter (l.22133), talks "The morrow after St. George's day" (l.22178-22186) and departure "April the 26th" (l.22479). No held witness gives the hearing a calendar day other than 17 April. Pallavicino gives 17 April (PALL1 l.10012-10013), Sarpi "the ſeventeenth of April" (SARPI l.9617), Waterworth arrival on the 16th and appearance "the seventeenth of April" (WAT l.1719-1724), and Herrnschmid "April 16. The next day" (ARM l.9148-9149). What differs is the time between arrival and hearing: one day, or four. So the brief's "At the first hearing, on 17 April" and its opening "18 April" tell no contested point as settled. The records and entry should name the dispute that is really there, so that no later round adds a needless hedge to the brief.
- Fix, records `contested_claims[2]`: claim "How soon after his arrival the first hearing came"; sides "The day after: Pallavicino, 17 April (l.10012-10014); Sarpi, 17 April (l.9617); Waterworth, arrived 16 April and appeared on the 17th (l.1719-1724); Herrnschmid, 'April 16. The next day' (arminian-magazine_vol-1_1778.txt l.9148-9149). The fourth day after: Foxe (l.21734), who gives no calendar date for either hearing." Keep Contested.
- Fix, entry `uncertain[4]`: "How soon the first hearing came. Pallavicino, Sarpi and Waterworth put it on 17 April, the day after Luther arrived. Foxe puts it 'the fourth day after his repair', and gives no calendar date for it."
- Fix, entry `datesNote`, the sentence "Pallavicino, Sarpi and Waterworth put the first hearing on 17 April, the day after; Foxe says 'the fourth day after his repair'": keep it, and add "Foxe gives no calendar date for either hearing."

**A-S4. Substantial (an editor's summary given as the act).** Records `claims[14]`: "Exsurge threatened Luther with penalties unless he recanted within 60 days of publication", witness MIRBT l.15508-15512, `witness_kind` "acts", Documented.
- Those lines are Mirbt's own German summary of what follows in the bull, not the bull's words: "Es folgen die Verdammung der Schriften Luthers, ... und die Strafandrohungen für Luther selbst und seine Anhänger, falls sie nicht binnen 60 Tagen nach Veröffentlichung der Bulle ... Widerruf leisten" (MIRBT l.15509-15512). This is the "wrong-preface citation" fault.
- Fix, records `claims[14]`: `witness_kind` "modern reconstruction"; claim "Mirbt summarizes the bull's sentence: penalties for Luther and his followers unless they recanted within 60 days of its publication". Keep Documented (the summary is Mirbt's, plainly told). Entry `issue[2]` already says "(Mirbt)" and can stand.

---

## Minor

**A-M1. Minor (wording that implies the rest of the Edict is lost).** Brief, paragraph 2: "Part of its Edict survives in German, in Carl Mirbt's collection." The Edict survives whole: Mirbt prints an excerpt "Deutsche Reichstagsakten II 640 ff." (MIRBT l.15588), and the records' `absent_details[1]` says so. Fix: `Carl Mirbt's collection prints part of its Edict, in German.`

**A-M2. Minor (the witness's date).** Brief, paragraph 2: "a Jesuit who wrote in 1664". Entry `uncertain[0]`: "a Jesuit writing in 1664". The held file is "the author's revised edition ... the first edition appeared in 1656-1657" (PALL1 l.3), as records `claims[9]` says. He did not write it in 1664. Fix, brief: `a Jesuit whose 1664 history draws on the papal envoy Aleander's letters.` Fix, entry `uncertain[0]`: "... through Pallavicino, a Jesuit whose history of 1656-1657, revised in 1664, draws on Aleander's letters."

**A-M3. Minor (what Pallavicino says Charles did).** Brief, paragraph 6: "Next morning, Pallavicino says, Charles wrote in his own hand that he would hear Luther no more." Pallavicino says Charles read out that morning a paper in his own hand ("legger vna ſcrittura di ſua mano ben lunga vn foglio", PALL1 l.10137-10142). He does not say when it was written. Buchheim likewise has it "declared to the Diet" that morning (FP l.2467-2469). Fix: `Next morning, Pallavicino says, Charles read out a paper in his own hand. He would hear Luther no more, and would proceed against him as a notorious heretic.`

**A-M4. Minor (one word over the ceiling).** The brief is 401 words, over the 400-word line the brief sets. Fix (also tightens the partisan marking into one place): replace "Luther's speech comes down in Foxe's English, drawn from Melanchthon and others. Foxe wrote as a Protestant." with `Foxe, a Protestant, gives Luther's speech in English, drawn from Melanchthon and others.` (Foxe's source note: "Ex Histor. Philip. Melancth.; ex Sleidano...", FOXE4 l.22529, footnote to the close of the Worms account, l.22491.) With A-B1, A-B2 and A-M1 to A-M3, the brief comes to 400 words.

**A-M5. Minor (one term for one thing, Who item 9).** The elector Palatine is "Louis" in `attended[2]` and `people`, but "Lewis" in `decided[4]`. The held line is "Lewis Count Elector Palatine" (SARPI l.9672). Fix: use "Lewis, elector Palatine" in all three, or "Louis" in all three with "(Sarpi's 'Lewis')" at first use.

**A-M6. Minor (a translated list that drops and reorders).** Entry `traditions[0].note`: "'followers, adherents, harborers, supporters, patrons' (Mirbt's German; our English)". MIRBT l.15629-15631: "mitverwandten, anhengern, enthaltern, fürschiebern, gönnern und nachvolgern", six words. The English renders five and puts "followers" first. Fix: "'associates, adherents, harborers, supporters, patrons and followers' (Mirbt's German; our English)".

**A-M7. Minor (a paraphrase that shifts the witness's word).** Entry `issue[8]`: "He would recant only if shown wrong by Scripture and plain reason (Foxe; his own Table Talk)." Foxe has "testimonies of the Scriptures, and by probable reasons" (FOXE4 l.22073-22074). The Table Talk speaks of Scripture only (TT l.3565-3569). Fix: "He would not recant unless convinced 'by testimonies of the Scriptures, and by probable reasons' (Foxe). His Table Talk gives Scripture alone."

**A-M8. Minor (an unsourced summing-up line).** Entry `issue[0]` ends "It was no church council." The sentence names no witness and adds no fact beyond the two before it (Who items 1 and 4, "tails and beat lines"). Fix: delete it.

**A-M9. Minor (wording).** Entry `teaser`: "The emperor's imperial diet heard Martin Luther". "Emperor's imperial" is a doublet. Fix: "Worms, 1521. The imperial diet of Charles V heard Martin Luther, who would not take back his books. The Edict of Worms then declared him an open heretic and outlaw."

**A-M10. Minor (citation slip).** Entry `record` Buchheim note: "dates the signing of the Edict to 25 May". Buchheim says "promulgated on May 25" (FP l.2518-2519), as `uncertain[6]` correctly has it ("put out on 25 May"). Fix: carried in A-B2's replacement note.

**A-M11. Minor (the README's reason, as worded, does not hold).** README: "Both sides are held in their own voices: the Edict in German, Luther's speech in Foxe's English and his own later account, and the emperor and the papal envoy through Pallavicino. Telling each side from its own witnesses, with the contested Edict date, takes the full length." Two problems. The emperor and Aleander reach us *through* Pallavicino, which is not "their own voices". And the brief does not tell a contested Edict date: it gives Mirbt's dating only. What it tells as a dispute is the Diet's consent (Buchheim against Pallavicino). Fix: "**Diet of Worms (about 2:30).** The Edict is held in its German text, Luther's speech in Foxe's English with his own later words, and the emperor and the papal envoy through Pallavicino, a Jesuit writing from the envoy's letters. Each side told from its own witnesses, with the dispute over whether the Diet consented to the Edict, takes the full length."

**A-M12. Minor (an absence note that misdescribes its hits, and two name forms).**
- Records `absent_details[3]` lists the "aleand" hits as Pallavicino, Waterworth, Sarpi, Foxe, Buchheim and Beza's editors. Luther's 1930 editors also report an Aleander letter to the pope from Aix-la-Chapelle, 23 October 1520 (LV3 l.293-294), and the Loyola letters' editors annotate him (`ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt` l.9858, 11088-11090). Neither is a Worms dispatch, so the absence holds. Fix: add "Luther's 1930 editors (luther_works-v3 l.293-294) report one 1520 letter from Aix, not from Worms."
- Name forms. The held lines read "John Daniel Hernnfehmid" (ARM l.3492, OCR) and "Riccardo Grieffeclau" (PALL1 l.10214, OCR). The entry's "Herrnschmid" and "Richard von Greiffenklau" are repairs, and "von" is in no held line. Fix: in records, note each held OCR form beside the claim that names him (Herrnschmid at `claims[50]` and `claims[97]`; Greiffenklau where the talks are cited). In `people`, write "Richard Greiffenklau (Pallavicino's 'Riccardo Grieffeclau'), archbishop of Trier".

---

## Length test

The brief earns its length. Each paragraph carries a sourced point the reader needs, and none repeats another:
- the scene (Foxe);
- the record and its partisans (C2);
- the stakes (Mirbt's bull, Aleander through Pallavicino, the summons);
- the first hearing (Eck's question, and Charles's remark from the papal side);
- the speech (Foxe) and the "Here I stand" question;
- the emperor's resolve (Pallavicino);
- the Wartburg (staged, by the Catholic witness);
- the Edict: its own words, the consent dispute told from both sides, and Luther's later word;
- the close (Buchheim).

I tried the obvious cuts. "Then he was asked again to take back his books" sets the stake in the opening scene. "The next evening he answered" is the only bridge back to the scene. "The Edict, dated 8 May, was signed on 26 May" carries the act's dating with its modern witness named, as pattern rule 4 asks. None can go without losing a sourced point or the story's turn. No Substantial length finding. The one word over the ceiling is fixed by A-M4. The README's reason needs the rewording in A-M11.

---

## Verified

- **Audio.** `diff` of the brief with `[calmly] ` prefixed against the audio script: one difference, `[warmly] ` before the last paragraph. No other tags.
- **Every quote in the brief**, against file and line, whitespace- and OCR-tolerant:
  - "almost smothered for the press" (FOXE4 l.21843);
  - "My conscience is so bound and captived in these Scriptures and the word of God" (l.22075-22076);
  - "Hereupon I stand and rest: I have not what else to say. God have mercy upon me!" (l.22077-22079);
  - "had to be changed at the diet at Nuremberg" (LV4 l.15970-15971), where "so harsh" paraphrases "so horrible", fairly;
  - "the great work of his life, the translation of the Bible from the original text" (FP l.2598-2600).
  
  Each is read in context: who speaks, which assembly, which year.
- **Every quoted string in the entry.** A script matched 46 English strings in their files. Every hit that failed (10 claims) is OCR (long s, letter-spacing) or a translation, and each was read by eye. The translations from MIRBT (l.15598-15604, 15612-15625, 15566) and PALL1 (l.9938-9943, 9971-9974, 10015-10017, 10170-10177, 10392-10404) are faithful except A-M6.
- **Brief claims, each with its witness:**
  - two hours' wait from after four till six (FOXE4 l.21838-21841);
  - Exsurge 15 June 1520 (MIRBT l.15393);
  - the bull burned 10 December 1520 (FOXE4 l.21652-21657);
  - Aleander's "vn' Eretico notorio già ſentenziato dal Papa non doueua eſſer'vdito" (PALL1 l.9938-9939);
  - the summons in the name of emperor and estates, with safe-conduct (FP l.2394-2402);
  - Eck as Trier's official (FOXE4 l.21752-21753; TT l.3551; PALL1 l.10015-10017), with the identity dispute rightly kept out of the brief and in `uncertain`;
  - "The books lay on a table which he showed unto me" (TT l.3553-3554);
  - Charles's "Coſtui certamente non mi farebbe mai diuentar' Eretico" at the first appearance (PALL1 l.10008-10010);
  - "come notorio eretico" (PALL1 l.10176-10177);
  - the staged seizure and Frederick able "veracemente giurare à Ceſare, che gli era ignoto doue Lutero dimoraſſe" (PALL1 l.10392-10405), the brief faithful to this;
  - Edict dated 8 May and signed 26 May (MIRBT l.15590-15591), and "offenbarn ketzer", "nit hauset, hoffet, etzt" (l.15603-15604, 15620);
  - "without the formal sanction of the Diet" (FP l.2518-2519);
  - Brandenburg answering "à nome comune, che ciò à tutti piaceua" (PALL1 l.10494-10497).
- **18 April** is given by Buchheim (FP l.2464-2466), Köstlin via LV3 (l.10567), and Pallavicino's and Sarpi's 17 April plus "the next day". There is no dispute on the calendar day (see A-S3).
- **C1 to C8.**
  - C1: every `record` witness has a kind and a side.
  - C2: acts lost, said once, early, with the stand-in named.
  - C3: Luther in Foxe's English and his own Table Talk and 1530 words.
  - C4: counts (a hundred horse and eight, about twenty-five books, four hundred against one hundred and four articles) each with its witness. Mirbt's and Steimle's dates are named.
  - C5: issue, decided and outcome are separate, and the Edict is told as little enforced.
  - C6: not applicable.
  - C7: tradition form with "Major council".
  - C8: a story from a scene, at 2:30.
- **Who items.**
  - 1 and 2: pass except A-B1 and A-B2.
  - 3: no invented feeling or speech.
  - 4: no "X, not Y", colon-reveal or beat line in the brief.
  - 5: fails only at "later tellings" (A-B1).
  - 6: Foxe, Pallavicino and Buchheim marked.
  - 7: consent dispute told both ways.
  - 8: Frederick, Eck, Aleander, Leo X and Pallavicino placed at first mention.
  - 9: fails at A-M5.
  - 11: FK 6.83, Flesch 68.75.
  - 13: tags only in audio.
- **People and verdicts.** Every name on the Who click was grepped in `Who_Scan_Era7.md` and `Who_Scan_Supplement.md`. Only Martin Luther is scored there (WHO). None of the 21 NOT SCORED names has a row, Bucer and Jonas included. Melanchthon (WHO) is rightly left off: Buchheim places him at Wittenberg (FP l.2611).
- **Census** (`origin/main:cic-website/data/world-census.json`). `lutheran-wittenberg-and-its-congregations` (1517-1580) and `the-tridentine-church` (1517-1650) exist at 1521, with names matching. `modernCountries` Q183 matches census rows. Rivers "Latin West, Protestant" match the major-councils table (`Councils_Scan.md` l.94). The live tree mentions the Diet only in `martin-luther`, and the entry and brief agree with every statement there. The census says "began" the Bible, and the brief's "worked at" follows Buchheim's "busy ... with". Parties at the Diet with no census tradition: the estates of the empire, which are no church tradition. Open-Gaps candidate, as the dossier notes: no census entry describes the Latin church *at 1521* (the Tridentine text begins with Trent). This is a text gap only, not a defect of this profile.
- **CFT-Wants.** The Worms row is present at l.368, as `absent_details[0]` says.
- **Held but unused (no finding; noted for completeness).** SCHW l.28112-28114 has Casimir going to Worms on 6 January 1521, and dean Sander at Worms "in attendance upon the Emperor" (l.27804). It also has a grievance from the Worms gravamina against itinerant indulgence sellers (l.26684-26692). The editor does not give the Diet's opening day.

## Searches run (absences)

All over `cic/texts/*.txt` unless named, with patterns tolerant of double spacing, long s as f or ſ, hyphen breaks, and English, German, Latin, Italian and French forms.
- "Hier stehe ich" and variants (`h\s*i\s*e\s*r\s+s\s*t\s*e\s*h\s*e`, `hier\s+fteh`, `[sſf]tehe ich` near anders/GOtt, `da stehe ich`, `here i stand`, `here stand i`, `kan(n) nicht anders`). Held tellings are ARM l.9309 (the only "Hier"), ZINZ l.30869-30870 ("da ſtehe ich") and LHYM l.651 (Carlyle). Comenius's *Labyrinth* l.7225 ("Here I stand; I cannot speak differently") is Simplicity's speech, not a telling of Luther. This confirms A-B1.
- An editor's judgment on "Here I stand". I searched every `luther_*` file, FOXE4, WAT, ARM, ZKG 14 and SCHW for spurious, doubtful, legend, apocryph, authentic, unecht, zweifelhaft, "später zus", "later addition" or "tradition" within 150 characters of here-I-stand, stehe ich, or Worms. None found, so the absence holds.
- The speech in Latin or German: `revocare (neque|nec)`, `nec possum nec volo`, `testimoniis scripturarum`, `ratione evidente`, `Wormser Rede`, `Rede (zu|in) Worms`. The only hit about the speech is the ZKG 14 note (l.25849; index l.34735), so the absence holds.
- Aleander: `aleand` with a Luther/Worms co-occurrence count per file. The hits are PALL1, WAT, FP, SARPI, ZKG 7, LV3 (a 1520 letter from Aix) and the Loyola editors. No dispatch from Worms, so the absence holds (A-M12).
- Charles's French declaration: `tr[eè]s chr[eé]stiens empereurs`, `roys catholiques d'Espa`, `descendu des`, `mes prédécesseurs` near Constance or Luther. Only unrelated hits, so the absence holds.
- Who drafted the Edict: read ARM l.9398-9430 against PALL1 l.10448-10454. This gives A-B3.
- A held tellings census: every file with Worms/Wormes/Wormat/Vormaz within 300 characters of Luther and a Diet or emperor word (26 files). Each new one was opened: Zwingli vol. 2 l.4557 is the 868 council; Universalist l.2547 is a passing mention; Brandt vol. 3 has no 1521 matter; SCHW is as noted. No other held telling of the hearings was found.
- The Reichstagsakten, Kidd, Köstlin, Kalkoff, Förstemann, Balan, Brieger, Sleidan, Cochlaeus, Weimar, Erlangen, Enders and Luther's correspondence: file-name search. None held.
- The Wartburg letters: `ex eremo`, `ex Pathmo`, Patmos near Luther, `Junker Georg|Jörg`. No letters held. Buchheim's "Junker Georg" (FP l.2598) is narrative.
- The opening day: `6. Jan(uar) 1521`, `January 6, 1521`, "6th of January" with 1521, Epiphany or Dreikönig near Worms. The only new hit is SCHW l.28112 (Casimir's journey, not the opening). `absent_details[8]` holds.
- Vehus: `vehus|voeus|vehe\b` in FOXE4, PALL1, all `luther_*` and SARPI. Only "Dr. Voeus ... chaplain" (FOXE4 l.22193). This gives A-S2.
- Buchheim's confession: `buchheim` in all files, and `protestant` in FP. No line gives it. This gives A-B2.

## Counts

Blocking 3 (A-B1 to A-B3). Substantial 4 (A-S1 to A-S4). Minor 12 (A-M1 to A-M12). Total 19.
