# R3 recheck: era 4 batch 4

Round 3, the last, ran in two parts, each a targeted recheck by a fresh Opus agent that had not seen the drafting or the earlier rounds, at full effort. The parts follow, unchanged.

## R3 recheck, part 1: Humbert of Silva Candida, Hincmar of Reims, Prudentius of Troyes, Jonas of Bobbio

Reviewer: independent Opus, first sight of these files, at full effort. I edited no profile, records, README or repo file. I made no git, web, paid or model calls, and used local scripts only. Inputs: `R1_review.md` (parts A and B), `R1_changes.md`, `R2_recheck.md` part 1, `R2_changes.md` part 1, the four `<id>.brief.txt`, `<id>.card.json`, `audio/<id>.audio.txt`, their `records.json` entries and the README. I found the changed brief text by diffing each brief against the R2 scored copies (`review/r2p1/<id>.r2.txt`). Humbert, Prudentius and Jonas match them exactly. Hincmar differs in one word: "so weak that he had" became "so weak he had" (P1), which is R2_changes' stated cut. I checked every card string R2_changes names as changed, and then read each whole brief and card once more in full. I opened every cited line again in its vendored file and read it in context, folding two-column interleave, long s and hyphen breaks.

Files reopened: Will's Acta et scripta ("WILL" l.1345-1356, 4068-4155, 8345-8351, 15630-15662); the Annales Bertiniani ("BERT" l.95-150, 196-266); PL115 Nicolás Antonio's notice (l.79255-79310, 79370-79400, 79420-79436, 79600-79645); Mansi 16 (l.66362-66395, 67128-67160, 75395-75456).

Scratch copies with my proposed brief fixes, scored with `engine.m1.gates.grade_text` from the repo root: `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/r3p1/<id>.r3.txt`.

**Mechanical checks (all four).** Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph (script, all PASS). Card keys are in the batch order; `legacy` is traces then remembered; `sources` is ownWords then about; every source entry runs title, author, date, language, file; no null or empty field; 3 keyWorks each; every cited file exists; no card sentence over 25 words (script); no "brief", "header" or "scan" on any card. No narrator "X, not Y", "not X but Y" or "and never" contrast and no colon in any brief (script, then by ear).

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence | Audio = brief |
|---|---|---|---|---|---|---|
| Humbert of Silva Candida (major) | 394 | 2:26 | 7.24 | 70.57 | 24 | PASS |
| Hincmar of Reims (major) | 405 | 2:30 | 6.50 | 74.84 | 24 | PASS |
| Prudentius of Troyes | 339 | 2:06 | 7.92 | 63.21 | 24 | PASS |
| Jonas of Bobbio | 327 | 2:01 | 8.08 | 67.71 | 25 | PASS |

---

### Humbert of Silva Candida

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-1-M1 (Pope Leo's death out of order) | RESOLVED | P3 now reads "Will dates the embassy to January 1054, and Pope Leo's death to 19 April." The P7 sentence is gone. Will's note gives "mortem Leonis noni XIII Cal. Maj. 1054" (WILL l.4111-4112), which is 19 April. The embassy date is "mittere non neglexit (m. Januario 1054)" (l.4075-4077). |
| R2-1-M2 (card names and dates) | RESOLVED | `keyWorks` 3 now reads "the church historian A. F. Gfrörer" (Will l.1351 "A. Fr. Gfroereri historia ecclesiastica"; l.8350 "id quod Gfrörer … opinatur"). `uncertain` 2 now has "Argyrus, the Greek governor in Italy" ("Árgyroum catapanum graecum in Italiam", l.4151-4152; the Edict "consilis Argyri, ipsi ex se advenerant nullo modo a papa missi", l.15645-15646). The Wibert, Leo of Ostia and Sigebert/Ekkehard entries now carry `"date": "1861"`, placed after `author`. |
| R2-1-M3 (records) | RESOLVED | Claim 5 ends "'unleavened bread at Mass' renders 'De azymo'". Claim 13 ends "Will's date for the death is used". |

**Changed card text, checked as new.** The `uncertain` 2 split ("The edict says the pope never sent the envoys. They came on the advice of Argyrus, the Greek governor in Italy, it says, and their letters bore false seals.") keeps "it says", so the witness is not cut loose. The seals are the Edict's ("litterarum sigilla adulterata esse deprehensa sunt", l.15651-15654).

**Whole brief and card, read again.** The brief is faithful and fair to both sides, as R2 found. Each date has its owner (Will, Mirbt), and "in the city" in P3 points to Constantinople, named one sentence earlier. Each close adds a witness's judgment. I found no new fault.

**Verdict, Humbert of Silva Candida: CLEAR. All 3 R2 findings are resolved. There are 0 new blocking points and 0 new minor ones.**

---

### Hincmar of Reims

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-1-B1 ("royal annals" told as settled) | RESOLVED | Brief P2 now reads "From 861 he carried on the annals that Prudentius of Troyes had kept." `knownFor` now reads "the annals now called the Annals of Saint-Bertin". `keyWorks` 1 gives Waitz's report of the dispute ("alii contenderunt, alii in dubium vocaverunt", BERT l.250-253). "Royal" is gone from the brief, card and audio. The two cards now agree. |
| R2-1-M4 (Douzy letter order and marking) | RESOLVED | P3 ends "At Douzy in 871 a synod deposed him." P4 opens "Its bishops, with the uncle named first, wrote to Pope Hadrian II." The letter's address has "Hincmarus, Harduicus, Remigius …" (MANSI16 l.66371-66372). "Its" can only point to the synod. "The uncle had raised the nephew as an orphan, they said, taught him his letters and made him a bishop" holds ("qui orfanum benigne illum nutrivit … litteris erudivit … ad apicem episcopatus provexit", l.66386-66390). |
| R2-1-M5 (framing of the wish) | RESOLVED, but "Hincmar" is now ambiguous between uncle and nephew (R3-1-M1) | "Quem utinam non vidissem, minime autem illum me ordinare in episcopum contigisset" (l.67153-67154). |
| R2-1-M6 (card) | RESOLVED | `sources.ownWords[2].title` now runs 18 words. `traces` 2 now reads "Mansi's volumes print the writings both Hincmars put before King Charles the Bald in August 868" ("OPUSCULA HINCMARI UTRIUSQUE PORRECTA CAROLO REGI APUD PISTAS. Anno … DCCCLXVIII … mense Augusto", l.75398-75403). "Ludovicus Cellotius, a Jesuit who wrote to the uncle's credit" is supported ("e societate JESU", l.75411; "illustrius aliquid ad Hincmari Rhemensis gloriam", l.75450-75451). So is "fought for his nephew against outside force" ("pro nepote adversus vim externam pugnat avunculus", l.75418-75419). `dates` now places Antonio "a Spanish scholar writing after 1650". `uncertain` 2 reads "Cellotius, the Jesuit who took the uncle's side", which follows his first mention in `traces` 2. |

**Changed text, checked as new.** In P1, "so weak he had to be carried" is unchanged in sense. The `dates` sentence on 849 holds: Gottschalk was condemned at Quierzy "ad Hincmarum tunc Remensem archiepiscopum fuit remissus, ut in custodia detineretur" (PL115 l.79428-79431). `keyWorks` 1 holds: "official annals" fairly renders "annalium publica auctoritate susceptorum" (BERT l.251-252). Pertz's "vix cuiquam praeter Hincmarum nota … a. 882. de Hincmari fuga Sparnacum" is at l.211-215.

#### New findings

- **R3-1-M1 MINOR (brief P4, and audio; item 9, names a listener could confuse).** P3 introduces "his nephew and namesake, Hincmar, bishop of Laon". After that the brief keeps the two men apart as "the uncle" and "the nephew". But P4 says "In his own letter, Hincmar wished he had never seen the man, still less ordained him." The sentence before is about the nephew, so a listener can hear "Hincmar" as the nephew until "ordained him" corrects it. This is reader-facing (brief and audio). Fix: "In his own letter, the uncle wished he had never seen the man, still less ordained him." (16 words, one more than now.) Scored copy: 406 words, about 2:30, FK 6.50, Flesch 74.88, longest sentence 24.
- **R3-1-M2 MINOR (card `legacy.traces` 3; and records, claim 4; item 7; the authorship of the 861 notice told as settled).** See R3-1-M3 under Prudentius, which covers the same point on both cards. On this card, `traces` 3 reads "His notice of Prudentius's death, in the annals for 861, …". `remembered` 3 then gives Antonio's view that an unnamed annalist wrote it. This is reader-facing (card only).
  - Fix, `traces` 3: "The annals for 861 give Prudentius's Spanish birth and his turn in the predestination quarrel. G. H. Pertz holds that Hincmar wrote the annals from that year." (15 and 13 words.)
  - Fix, records, claim 4: replace "Hincmar's 861 notice ('heresis defensor acerrimus')" with "The 861 notice ('heresis defensor acerrimus'), Hincmar's by Pertz (BERT l.203-205) and an anonymous annalist's by Antonio (PL115 l.79267-79271, 79622-79623)". This is records only.
- **R3-1-M4 MINOR (card `keyWorks` 1, and the same string on the Prudentius card; item 5, a scholar with no role at first card mention).** This card's first mention of Georg Waitz is "Georg Waitz says some have held them to be official annals…", which gives no role. The same item calls Pertz "an earlier editor", so the reader is left to guess that Waitz is the editor. The Prudentius card's first mention of Waitz is also in `keyWorks` 1, with the same words. This is reader-facing (cards). Fix, on both cards: "Georg Waitz, who edited them, says some have held them to be official annals and others have doubted it." (19 words.)

**Whole brief and card, read again.** The Douzy text and the nephew's complaint are faithful. The brief keeps the uncle and nephew apart everywhere except at R3-1-M1. Each partisan witness is marked: the annals are "the uncle's annals" at Troyes, and Cellotius is the Jesuit on the uncle's side. Every brief sentence is 24 words or fewer.

**Verdict, Hincmar of Reims: CLEAR on the blocking bar. All 4 R2 findings are resolved. There are 0 new blocking points and 3 minor ones (R3-1-M1 in the brief and audio; R3-1-M2 and R3-1-M4 on the card; R3-1-M2 also in the records).**

---

### Prudentius of Troyes

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-1-B2 (Antonio made to blame Hincmar) | RESOLVED on its core point. The unowned attribution R2 also named is fixed in P5, but it still stands in P2 and in four card strings (R3-1-M3). | P5 now reads "After Prudentius died, Hincmar took over the annals, Pertz says. The entry for 861 says … Antonio calls this a slander, and blames an unnamed annalist on Hincmar's side. He says Prudentius never opposed Gottschalk." The Latin supports each part: "Cum vero Prudentius anno 861 … obierit" and "annalium inde ab a. 861. auctorem ipsum Hincmarum fuisse, extra dubium venit" (BERT l.150, 204-205); "Sed Bertinianus Anonymus, Hincmari metropolitae … velificatus partibus" and "Nec verum est Prudentium Gotescalcho obstitisse unquam" (PL115 l.79622-79623, 79628-79629). `remembered` 2 is as R2 proposed. In this field "He" can only be Antonio. |
| R2-1-M7 (pronoun "he" in P2) | RESOLVED | "In his own verses for a Gospel book, Prudentius calls himself born in Hesperia and brought to the Celts." |
| R2-1-M8 ("his death" on `traces` 1) | RESOLVED | "after Prudentius's death". |
| R2-1-M9 (records locator) | RESOLVED | The Camusat claim now cites l.82847-82867. |

**Changed text, checked as new.** The post-R2 split of `uncertain` 2 brought in a word stronger than the source (R3-1-M5).

#### New findings

- **R3-1-M3 MINOR (brief P2, and audio; card `dates`, `remembered` 1, `uncertain` 1 and 4; records, claim 1 and contested claim 0; item 7; the 861 notice given to Hincmar with no owner, though the records list its authorship as contested).** R2 added the contested claim "Who wrote the 861 notice of Prudentius": Pertz says Hincmar, "extra dubium". Antonio gives the notice to the "anonymus idem Bertinianus auctor" (PL115 l.79307), whom he sets apart from Hincmar, "ipsum adversarium", who honours "dominum Prudentium" (l.79617-79622). Antonio's anonymous author is the writer "qui ad annum usque 882 res in Francia gestas persecutus est" (l.79270-79271). So the two men disagree about who that writer was, not about which entries he wrote. P5 now gives both sides. But P2 still says "Hincmar, archbishop of Reims, names him Galindo, called Prudentius, a Spaniard by birth", and those are the words of the same 861 notice. The card gives the notice to Hincmar flatly in `dates` ("by Hincmar's entry for that year"), `remembered` 1 ("Hincmar calls him learned…"), `uncertain` 1 ("Hincmar says he first resisted him") and `uncertain` 4 ("Hincmar calls him Galindo"). In `uncertain` 1 the two sides are then "Hincmar says" against "Antonio says", when Antonio's point is that the man who says it is not Hincmar.
  - I rate this MINOR, not BLOCKING, for three reasons. The dispute is told in the brief (P5) and on the card (`remembered` 2). Pertz's side is the dominant one, and he cites Richer of Reims as witness that Hincmar carried the annals on to his own time (BERT l.218-219). And no sentence states anything a held source denies outright. If the lead rules that an unowned side of a recorded contested claim is blocking, this point is blocking, and the fix is the same.
  - This is reader-facing (brief, audio, card) and also in the records.
  - Brief P2, sentence 2: "On his death the annals name him Galindo, called Prudentius, a Spaniard by birth." (14 words, one more than now.) Hincmar's first brief mention then moves to P4, so P4 sentence 2 needs his see: "Prudentius took the side Hincmar of Reims opposed." (8 words, two more.) Scored copy: 342 words, about 2:07, FK 7.81, Flesch 64.23, longest sentence 24. The listener links "the annals" to P3's "He kept the annals of the Frankish kings' deeds", and links "the entry for 861" in P5 back to P2.
  - Card `dates`: "Died in 861, by the annals' entry for that year." (10 words.)
  - Card `remembered` 1: "The annals' notice of his death, which G. H. Pertz gives to Hincmar, his opponent in the predestination quarrel, calls him learned. It says he turned in bitterness into a fierce defender of Gottschalk's heresy." (22 and 14 words.)
  - Card `uncertain` 1: "Whether he ever opposed Gottschalk. The annals' notice of his death says he first resisted him and then took his side. Antonio says he never opposed him." (5, 16 and 6 words.)
  - Card `uncertain` 4, sentence 2: "The annals' notice of his death calls him Galindo, surnamed Prudentius." (11 words.) Antonio himself cites "Annales Bertiniani … ad annum 861" for the name (PL115 l.79267-79269).
  - Records, claim 1: replace the opening "Hincmar, Annals 861:" with "Annals 861 (Hincmar's by Pertz, BERT l.203-205; the 'anonymus … Bertinianus auctor' by Antonio, PL115 l.79267-79271, 79307):". Keep "Hostile witness".
  - Records, contested claim 0, first side: replace "Hincmar, Annals 861 (BERT l.3534-3536): yes; hostile witness" with "The annals for 861 (BERT l.3534-3536), Hincmar's by Pertz: yes; hostile witness".
  - Records, contested claim 2, second side: add "PL115 l.79267-79271, 79307 (Antonio's anonymous author is the one who carried the annals to 882)".
- **R3-1-M4 (Waitz with no role)** applies to this card's `keyWorks` 1 too. The fix is given under Hincmar.
- **R3-1-M5 MINOR (card `uncertain` 2; item 1; a word stronger than the source, brought in by the post-R2 split).** The field reads "Most of what is told of his life comes through Hincmar, his opponent, and the annals. The rest comes through defenders who answered them, such as Nicolás Antonio." "The rest" claims that everything else comes through defenders. But the card itself also draws on his own verses for a Gospel book (`place`), his treatise and letter (`keyWorks` 2 and 3), and Pertz and Lebeuf (`dates`, `uncertain` 3). R2's proposed text said only "and through defenders who answered them". This is reader-facing (card only). Fix, sentence 2: "Some comes through defenders who answered them, such as Nicolás Antonio." (11 words.)

**Whole brief and card, read again.** Apart from R3-1-M3, the brief is faithful. P1's verbs are owned ("he wrote", "he confessed"). P3's Epiphany and eclipse details are framed as Lebeuf's signs. In P4, "Under 859 he wrote" can only point to Prudentius. The close adds Antonio's report. No beat line, triad or tail.

**Verdict, Prudentius of Troyes: CLEAR on the blocking bar. All 4 R2 findings are resolved (R2-1-B2 on its core point). There are 0 new blocking points and 3 minor ones (R3-1-M3 in the brief, audio, card and records; R3-1-M4 and R3-1-M5 on the card).**

---

### Jonas of Bobbio

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-1-M10 (pronoun after Munro) | RESOLVED | "Some three years before the preface, Jonas had promised at Abbot Bertulf's command to write the saint's deeds." ("Memini me ante hoc ferme triennium … Beati Bertulfi Abbatis imperio jubente … fuisse pollicitum", BARRALIS l.36429-36430; OCR "Benulphi".) |
| R2-1-M11 (source key order) | RESOLVED | `sources.about[1]` now runs title, author, date, language, file. |

**Whole brief and card, read again.** The scene keeps "per ora" ("along the shores"). Krusch's dates have their owner ("which Krusch reckons as 659"; "about 640"). The Acta Sanctorum editors' "non Hibernus, sed Italus" is attributed to them on the card. The thin record is said once, on the card (`uncertain` 2). In P2, "says he entered it" sits right after "Dana Munro", but a translator of 1895 entering Bobbio cannot be meant, so I raise no finding. I found no new fault.

**Verdict, Jonas of Bobbio: CLEAR. Both R2 findings are resolved. There are 0 new blocking points and 0 new minor ones.**

---

### Writing checks on the changed text and the whole briefs

I read all four briefs again in full as a listener. I looked for AI tells, narrator contrasts, colon-reveals, tails and beat lines, triads, unearned adjectives, status register, choppy runs, undefined terms and confusable names.

- **Contrasts.** The only contrasts are the sources' own and are attributed: Hincmar's "No wall or human hand … but God's power", and Michael's "came to him but would not greet him".
- **Closes.** Each close adds a witness's judgment or the subject's own words.
- **Names.** The one fault is the uncle and nephew Hincmar (R3-1-M1).
- **Pronouns and "its".** Hincmar P4 "Its bishops" points to the synod. Humbert P5 "They sell the gift of God, it says" points to his party and to the sentence.
- **Length.** Every brief sentence is 25 words or fewer, and every card sentence too (script).

### Counts

| Profile | Blocking | Minor | Reader-facing (brief, audio, card) | Records only |
|---|---|---|---|---|
| Humbert of Silva Candida | 0 | 0 | none | none |
| Hincmar of Reims | 0 | 3 (R3-1-M1, M2, M4) | M1 brief and audio; M2 and M4 card | M2 (claim 4) |
| Prudentius of Troyes | 0 | 3 (R3-1-M3, M4, M5) | M3 brief, audio and card; M4 and M5 card | M3 (claim 1, contested claims 0 and 2) |
| Jonas of Bobbio | 0 | 0 | none | none |

### Verdicts

- **Humbert of Silva Candida: CLEAR.** All 3 R2 findings are resolved, and there are no new findings.
- **Hincmar of Reims: CLEAR on the blocking bar, with 3 minor points to apply.** All 4 R2 findings are resolved, R2-1-B1 among them. R3-1-M1 asks for "the uncle" in place of an ambiguous "Hincmar" in P4.
- **Prudentius of Troyes: CLEAR on the blocking bar, with 3 minor points to apply.** All 4 R2 findings are resolved, R2-1-B2 on its core point. R3-1-M3 gives the 861 notice an owner in P2 and on the card, to match the contested claim R2 added. The lead may rule it blocking, as noted under the finding.
- **Jonas of Bobbio: CLEAR.** Both R2 findings are resolved, and there are no new findings.

---

## R3 recheck, part 2: Braulio of Zaragoza, Ildefonsus of Toledo, Julian of Toledo, Beuno

Reviewer: independent Opus, first sight of these files. I edited no profile, records or notes file. I made no git, web, paid or model calls, and used local scripts only. Inputs: `R2_recheck.md` part 2, `R2_changes.md` part 2, the four `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, their `records.json` entries and the README lines on them. I diffed each brief against the R2 scored copies in `review/R2p2/`: Braulio, Julian and Beuno match them exactly, and Ildefonsus had no brief change in round 2. I opened every line behind a round 2 change again in its vendored file and read it in context, folding two-column interleaves, long s and OCR noise: PL96 l.17040-17100 (Ildefonsus XII and XIV), 650-668, 700-740, 3790-3875, 4192-4206, 36855-36880, 37350-37410, 37565-37580, 45575-45625; PL80 l.51525-51565, 52000-52062; MGH11 l.16352-16368, 31300-31312, 32600-32680; REES l.316-328, 13430-13470, 13658.

No brief fix is proposed in this round, so no scratch copy was scored.

**Mechanical checks (all four).** grade_text passes on all four. Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and nothing else (script). Card keys are in batch order. `legacy` runs `traces` then `remembered`, and `sources` runs `ownWords` then `about` (Beuno has `about` only, and no `keyWorks`, rightly). No card has more than 3 keyWorks or any null or empty field, and every cited file exists. Every source entry now runs `title`, (`author`), `date`, `language`, `file`, so R2-2-M6 is fixed. No card sentence runs over 25 words (script, splitting on . ! ? ;).

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence | Audio = brief |
|---|---|---|---|---|---|---|
| Braulio of Zaragoza | 328 | 2:01 | 6.86 | 70.19 | 24 | yes |
| Ildefonsus of Toledo | 328 | 2:01 | 7.53 | 67.56 | 23 | yes |
| Julian of Toledo | 342 | 2:07 | 6.63 | 73.89 | 23 | yes |
| Beuno | 346 | 2:08 | 4.32 | 82.63 | 23 | yes |

---

### Braulio of Zaragoza

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-2-B1 (the archdeacon-to-bishop join told as fact on the card) | RESOLVED | `traces` 3 now reads "...Eugenius the second. He may be the archdeacon Braulio gave up to King Chindaswinth." Ildefonsus XIV: "Hic cum Ecclesiae regiae clericus esset egregius, vita monachi delectatus est. Qui sagaci [fuga] urbem Caesaraugustanam petens, illic martyrum sepulcris inhaesit, ibique studia sapientiae et propositum monachi decenter incoluit; unde principali violentia reductus, atque in pontificatum ascitus" (PL96 l.17051-17053, 17077-17079, interleaved). The hedge matches `uncertain` 2 and records `absent_details` 2. |
| R2-2-M1 ("Its canon") | RESOLVED | Brief and audio: "The council's canon on the Jews made every later king swear to keep it so." |
| R2-2-M2 (the chronicle's numbers, "It", the end year) | RESOLVED | `remembered` 1: "says it runs to 754 and calls the name false", for "pervenientis ad a. 754 notae hodie sub nomine ficticio Isidori Pacensis" (MGH11 l.16362-16363). `remembered` 2: Mommsen's note 5 is tied to the Sisenand council ("concilium celebravit^)", l.32614; "Decreta concilii Toletani quarti ... aerae 671 (= p. Chr. 633)", l.32673-32675); "cuius eloquentiam Roma ... postmodum per epistolare alloquium satis miravit" (l.32615-32616). `remembered` 3: the Chintila council has no number in the chronicle (l.32619-32626). The "sixth" is Antonio's, against Rodericus's "fifth" ("sextae, juxta nostrarum editionum ordinem, quam ipse tamen quintam vocat", PL80 l.51558-51560); "piam doctrinam Christianis mentibus decenter infundit: cuius et opuscula nunc usque eclesia relegit" (MGH11 l.32625-32626). No field opens on a bare "It". The records add the lines. |
| R2-2-M3 (the "quotquot viderim" hedge) | RESOLVED | `uncertain` 5: "as all the old manuscripts its writer had seen and nearly all bibliographers agree", for "veterum quotquot viderim Codicum, ac bibliographorum fere omnium ... consensionem" (PL80 l.52054-52058). The records read "the consensus of all the old codices its writer had seen". |

**Changed sentences checked and found faithful.** The brief's P5 s4. Card `traces` 3, `remembered` 1 to 3, `uncertain` 5, and the records chronicle claim and contested side 2. Each changed card field stands alone. "Mommsen" in `remembered` 2 follows his naming with a role in `remembered` 1. "Antonio" in `remembered` 3 follows "Nicolás Antonio, in his Bibliotheca Hispana vetus" in `remembered` 1. Nothing a fix carried in cuts a witness loose.

**Whole brief and card, read again.** The brief reads cleanly as a listener. Its contrasts are Braulio's own ("disrupto potius quam scisso"; "magis volumus sequi eum"). It has no colon-reveal, tail, triad or status line. On the card, one name still lacks context at its only mention (R3-2-M1).

#### New finding

- **R3-2-M1 MINOR (card `uncertain` 5 s2, card only; items 8 and 4; a name with no context at its only mention).** "A note printed with Nicolás Antonio's notice says Gregorius Mayansius denied it." A reader is not told who Mayansius is. The note says where he made the denial: "Gregorius Mayansius Siscarius: qui in Nicolai Antonii Vita, immortali Fictitiarum Historiarum ejusdem Censurae praemissa, [p.] 125, falso eam Praenotationem Braulioni tributam asserit" (PL80 l.52038-52040, interleaved with l.52006-52008).
  - Fix, `uncertain` 5 s2: "A note printed with Nicolás Antonio's notice says Gregorius Mayansius, in his Life of Antonio, denied it." (17 words.)

**Verdict, Braulio of Zaragoza: NOT CLEAR. All 4 round 2 findings are resolved. There are 0 new blocking points and 1 minor one (R3-2-M1, card only).**

---

### Ildefonsus of Toledo

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-2-M4 (Antonio's 25 January told as a likely misprint) | RESOLVED | `uncertain` 3: "Nicolás Antonio quotes Julian's day, yet gives 25 January, the day he says the Roman Martyrology keeps his memory." Source: "ad superos abiit anno 669, die Januarii 25, ad quem diem refertur ejus memoria in Romano Martyrologio" (PL96 l.658-661), with Tamayo's martyrology at 25 January (l.724, 767, 862). Records side 2 now cites these lines and drops "possibly OCR". |
| R2-2-M5 (Cixila's "fertur" dropped on the card) | RESOLVED | `remembered` 1: "She is said to have thanked God that her Lady lived through the life of Ildefonsus." Source: "talia fertur depromere vota ... Deo gratias, vivit domina mea per vitam Hildefonsi" (l.3844-3847). Reccesvinth is the king of the scene ("princeps quondam Reccesvinthus", l.3810-3811). |
| R2-2-M6 (key order) | RESOLVED | The Missale entry runs `title`, `date`, `language`, `file`. |

**Changed sentences checked and found faithful.** Card `uncertain` 3, `remembered` 1, records contested side 2. "Agali ... which Nicolás Antonio and a thirteenth-century Life call the monastery of Saints Cosmas and Damian" holds for both (l.715-718; Cerratensis "in ecclesia sanctorum Cosmae et Damiani, quae in suburbio sita est Toletano, quae antiquitus Agaliense monasterium dicebatur", l.4198-4201).

**Whole brief and card, read again.** The brief had no change in round 2. Read as a listener, it is clean. "Then he attacked the monastery" follows "The father" as subject, so "he" is the father. The P3 dates sit under "Julian says". Cixila's Life is marked as later and its wonder as hedged. On the card, the first mention of Cixila is unplaced (R3-2-M2).

#### New finding

- **R3-2-M2 MINOR (card `legacy.traces` 2, card only; item 8; a name unplaced at its first card mention).** `traces` comes before `remembered`, so "Cixila says he composed Masses..." is the card's first mention of Cixila. He is identified only later, in `remembered` 1 ("Cixila, a bishop of Toledo under Muslim rule"). The source: "missam superscriptam, quae in ejus laude decantaretur, perfecit, quae est septima" (PL96 l.3870-3873). The heading reads "A Cixilano ejusdem urbis episcopo edita", and Antonio adds "sub Maurorum tyrannide" (records).
  - Fix, `traces` 2: "Cixila, a later bishop of Toledo under Muslim rule, wrote a Life of him. He says Ildefonsus composed Masses, among them one to be sung in Mary's praise on her feast, which he counts as the seventh." (14 and 23 words.) `remembered` 1 can stay as it is. It names Cixila again, so the field still stands alone.

**Verdict, Ildefonsus of Toledo: NOT CLEAR. All 3 round 2 findings are resolved. There are 0 new blocking points and 1 minor one (R3-2-M2, card only).**

---

### Julian of Toledo

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-2-B2 (the Jews' argument told in the narrator's voice) | RESOLVED | Brief P5 and audio: "In the opening letter, Julian says they counted the years from Creation. By that count, they said, the world was still in its fifth age, so Christ had not yet come." Card keyWorks 2: "The opening letter says they reckoned..." Source: "pestilentiosis objectibus garrientes, quod sumpta annorum supputatio ab initio mundi secundum Hebraeos codices quintam adhuc saeculi aetatem insinuet, et necdum adhuc Christum venisse, quem in sexta credunt aetate saeculi advenire" (PL96 l.45614-45619). The hostile witness is named before the argument. I weighed whether "they said" in the next sentence cuts the frame loose. It does not: the sentence sits in the same paragraph, straight after "Julian says", under a paragraph about the letter, and the next two sentences carry Julian's voice on ("He says he believes"; "he writes"). The surgeon image keeps "credo" and "dixerim" (l.45597-45599, 45610-45611). |
| R2-2-M7 ("era" unglossed; a long `dates` sentence) | RESOLVED | "in the Spanish era 728"; split into 13 and 15 words. Felix: "anno tertio Egicanis principis, pridie Nonas Martii, aera septingentesima vigesima octava" (l.37355-37358). |
| R2-2-M8 (Mommsen's judgment on the name left out) | RESOLVED, with a role to add (R3-2-M3 b) | `uncertain` 2: "the chronicle under the name of Isidore Pacensis. That chronicle runs to 754, Theodor Mommsen says, and the name is false." This matches MGH11 l.16362-16363. Antonio: "Plures tamen Roderico credunt nec temere; cum Isidorus Pacensis iisdem verbis auctor rei fuerit" (PL96 l.36873-36875). MGH11 is now in `sources.about`. But Mommsen has no role at his only card mention. |
| R2-2-M9 (Morales's side) | RESOLVED | Records add the third side. Source: "Non est itaque audiendus Ambrosius Morales, qui vitiato Codice usus ... neque amplius quam novem annos, quatuor menses et quinque sexve dies in Toletana cathedra sedenti esse attribuendos" (l.37391-37396). |

**Changed sentences checked and found faithful.** The brief's P5 s2 to s5. Card keyWorks 2 ("It calls their tongues the rot a surgeon cuts away", where "It" is the letter named in the sentence before), `dates` s2 and s3, `uncertain` 2, and the MGH11 source entry. "The notes of Cardinal Lorenzana's Toledo edition, which Migne follows" rests on "In Editione Antonii Lorenza, quam sequimur" (PL96 l.16518) and on PL83's "Franciscus Lorenzana cardinalis" (R1 D-M4).

**Whole brief and card, read again.** The brief reads cleanly as a listener. The scene is in Julian's own letter, the hedge "if he remembered rightly" is kept, and the dispute sits where it arises. The close is a sourced line. On the card, the `dates` field was rewritten in round 2. It is the card's first mention of Felix, of the Toledo edition and of Nicolás Antonio, and it identifies none of them. Mommsen and Gudila also appear with no role (R3-2-M3).

#### New finding

- **R3-2-M3 MINOR (card `dates`, `uncertain` 2 s3, `uncertain` 5 s2, card only; item 8 and the scholars-get-a-role convention; names with no identifier at first card mention).**
  - (a) `dates`: "Felix says..." is the first card mention of Felix. He is placed only in `place` ("Felix of Toledo"). "The Toledo edition's notes" comes before the edition is named in `uncertain` 2. "Nicolás Antonio has Quiricus dying in 681" is Antonio's first card mention, and it gives no role. The Braulio and Ildefonsus cards give him "in his Bibliotheca Hispana vetus", which the PL96 heading prints as "Biblioth. vet. Hisp." (l.638).
    - Fix, `dates` s2: "Felix of Toledo says he held the see ten years, one month and seven days." (15 words.)
    - Fix, `dates` s4: "The notes of Cardinal Lorenzana's Toledo edition read this as 6 March 690, with his consecration on 29 January 680." (20 words.)
    - Fix, `dates` s5: "Nicolás Antonio, in his Bibliotheca Hispana vetus, has Quiricus dying in 681." (12 words.)
  - (b) `uncertain` 2 s3: Mommsen is named with no role. Fix: "That chronicle runs to 754, says Theodor Mommsen, who edits it, and the name is false." (16 words.)
  - (c) `uncertain` 5 s2: "Felix says he and Gudila wished to be" does not say who Gudila is. Felix calls him "sanctae memoriae collegae sui Gudilanis levitae", and Antonio "una cum Gudila diacono" (PL96 l.36878). Fix: "Felix says he and the deacon Gudila wished to be, but God judged otherwise." (14 words.)

**Verdict, Julian of Toledo: NOT CLEAR. All 4 round 2 findings are resolved (R2-2-M8 with a role to add). There are 0 new blocking points and 1 minor one (R3-2-M3, card only).**

---

### Beuno

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-2-M10 (bare "Rees" after both Reeses are named) | RESOLVED in the brief and audio; PARTLY RESOLVED on the card | Brief: "he said, in W. J. Rees's English" and "W. J. Rees places it in Flintshire" (the editor's footnote, "A celebrated and copious flowing fountain in Flintshire", REES l.13658). Card `uncertain` 1: "manuscripts W. J. Rees printed in 1853, and he thought such Lives were probably compiled about the twelfth century" (l.322-324). But card `traces` 1 ("The note in Rees") and `remembered` 1 ("in Rees") still use the bare name. See R3-2-M4. |

**Changed sentences checked and found faithful.** Brief P4 s6 (the quote is verbatim: "who is in that woman's arms owns that land, and is heir thereof"), P5 s3, card `uncertain` 1. "The same note" in P6 still points back to the P3 note, since P4 and P5 name no other note.

**Whole brief and card, read again.** The brief reads cleanly. The P1 quotes are verbatim, with "abomi nable" a line break (REES). The lateness caveat comes early, in P2. The professor's note is marked as quoted. P2's "Rees thought" comes before the professor is named, so it can only be W. J. Rees.

#### New finding

- **R3-2-M4 MINOR (card `legacy.traces` 1 and `legacy.remembered` 1, card only; items 8 and 20; the same name clash R2-2-M10 fixed elsewhere, left in two fields).** "The note in Rees names eleven churches..." and "The Latin Life of Saint Winefred, in Rees, makes Beuno her teacher..." The card's `knownFor` and `dates` name both W. J. Rees and "Professor Rees's Welsh Saints", which is also a book. So "in Rees" can be read as either. In `traces` 1, "The note" also has no antecedent within its own field. The note is REES l.13452-13462, ending "— Professor Rees's Welsh Saints, page 268". The eleven churches and five counties are as stated.
  - Fix, `traces` 1: "A note in W. J. Rees's edition names eleven churches dedicated to him in Montgomeryshire, Merionethshire, Caernarvonshire, Anglesey and Herefordshire." (20 words.)
  - Fix, `remembered` 1, s1: "The Latin Life of Saint Winefred, printed by W. J. Rees, makes Beuno her teacher, who raised her after she was killed." (22 words.)
  - README only, optional: "The note in Rees puts his life..." could read "The note in W. J. Rees's edition puts his life...".

**Verdict, Beuno: NOT CLEAR. The 1 round 2 finding is resolved in the brief and audio and partly resolved on the card. There are 0 new blocking points and 1 minor one (R3-2-M4, card only).**

---

### Writing checks on the changed text and the whole briefs

I read all four briefs again in full, as a listener. I checked for AI tells, narrator contrasts ("X, not Y", "not X but Y", "X and never Y"), colon-reveals, tails and beat lines, triads, unearned adjectives, status register, choppy runs, undefined terms and names a listener could confuse.

- The round 2 fixes carried in no new pronoun fault, dangling reference or loose witness.
- The contrasts that remain belong to the sources.
- None of the briefs has a colon-reveal, rhetorical question or aphorism.
- All four briefs pass. Every new finding is on a card.
- Julian (342) and Beuno (346) still run a little over the 325 to 340 band for a standard brief, about 2:07 and 2:08. As in round 2, I make no finding on that.

**For the lead (README, batch-wide, not counted against these profiles).** The README file table says the audio has "`[warmly]` before the closing line". The script puts it at the start of the last paragraph, which is more than one line in seven of the eight briefs. Suggested wording: "`[warmly]` at the start of the last paragraph".

### Counts

| Profile | Blocking | Minor | Where |
|---|---|---|---|
| Braulio of Zaragoza | 0 | 1 (R3-2-M1) | card only |
| Ildefonsus of Toledo | 0 | 1 (R3-2-M2) | card only |
| Julian of Toledo | 0 | 1 (R3-2-M3) | card only |
| Beuno | 0 | 1 (R3-2-M4) | card only (plus an optional README line) |

### Verdicts

- **Braulio of Zaragoza:** NOT CLEAR. All 4 round 2 findings are resolved (R2-2-B1, M1 to M3). There are 0 blocking points and 1 minor one (R3-2-M1: Mayansius given no context, card only).
- **Ildefonsus of Toledo:** NOT CLEAR. All 3 round 2 findings are resolved (R2-2-M4 to M6). There are 0 blocking points and 1 minor one (R3-2-M2: Cixila unplaced at his first card mention).
- **Julian of Toledo:** NOT CLEAR. All 4 round 2 findings are resolved (R2-2-B2, M7 to M9). There are 0 blocking points and 1 minor one (R3-2-M3: Felix, the Toledo edition, Antonio, Mommsen and Gudila given no identifier at first card mention).
- **Beuno:** NOT CLEAR. R2-2-M10 is resolved in the brief and audio and partly resolved on the card. There are 0 blocking points and 1 minor one (R3-2-M4: bare "Rees" in two card fields).
- **For the lead.** No blocking point remains in any of the four. Every open item is a card-only wording change, with exact text given above, and no brief, audio or source reading is affected. All four briefs pass as they stand.
