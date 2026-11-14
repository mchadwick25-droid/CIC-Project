# R2 recheck: era 4 batch 4

Round 2 ran in two parts, each a targeted recheck by a fresh Opus agent that had not seen the drafting or round 1, at full effort. The parts follow, unchanged.

## R2 recheck, part 1: Humbert of Silva Candida, Hincmar of Reims, Prudentius of Troyes, Jonas of Bobbio

Reviewer: independent Opus, first sight of these files, at full effort. I edited no profile, records, README or repo file. I made no git, web, paid or model calls, and used local scripts only. Inputs: `R1_review.md` parts A and B, `R1_changes.md`, the four `<id>.brief.txt`, `<id>.card.json`, `audio/<id>.audio.txt`, their `records.json` entries and the README. I found the changed brief text by diffing each brief against the R1 scored copies (`review/partA/humbert.fixed.txt`, `review/partA/hincmar.fixed.txt`, `review/partB_*.fixed.brief.txt`). Prudentius and Jonas match their scored copies exactly. Humbert differs in one sentence ("The pope never sent the envoys, the edict adds"). Hincmar differs in P3 and P4, the coordinator's extension, which I checked in full as a first review, along with the rest of his brief and card. I opened every cited line again in its vendored file and read it in context, folding two-column interleave, long s and hyphen breaks.

Files reopened: Will's Acta et scripta ("WILL" l.4072-4153, 14800-14830, 15262-15290, 15636-15662); Mansi 16 ("MANSI16" l.53110-53140, the Douzy synodal letter l.66365-66420 and 66850-66958, Hincmar's letter to Hadrian l.66960-67200, Cellotius l.75385-75420); Mansi 15 l.5418-5430, 7608-7618, 91235-91300; Mansi 17-18 l.36790-36892; Mommsen AA11 l.3734-3741; the Annales Bertiniani ("BERT" l.128-162, 200-265); PL115 l.79374-79400, 79600-79634; SRM3 l.7772, 31897-31899; AASS-Mar3 header and l.197376-197490. Absence check: the AASS Life of Attala (10 March) is in no held Acta Sanctorum volume (held: March 1 and 3, May 6, June 5, August 1), so "which is not held" on the Jonas card stands.

Scratch copies with my proposed brief fixes, scored with `engine.m1.gates.grade_text` from the repo root: `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/r2p1/<id>.r2.txt`.

**Mechanical checks (all four).** Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph (script, all PASS). Card keys are in the batch order; `legacy` is traces then remembered; `sources` is ownWords then about; no null or empty field; 3 keyWorks each; every cited file exists. Card sentences over 25 words: one, Hincmar `sources.ownWords[2].title` (28 words, R2-1-M6). Source-entry key order: one fault, Jonas `sources.about[1]` (R2-1-M11).

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence | Audio = brief |
|---|---|---|---|---|---|---|
| Humbert of Silva Candida (major) | 398 | 2:27 | 7.11 | 70.73 | 24 | PASS |
| Hincmar of Reims (major) | 404 | 2:30 | 6.50 | 74.79 | 24 | PASS |
| Prudentius of Troyes | 327 | 2:01 | 7.67 | 64.14 | 24 | PASS |
| Jonas of Bobbio | 327 | 2:01 | 8.04 | 67.97 | 25 | PASS |

---

### Humbert of Silva Candida

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B1 (24 June given to the envoys' arrival) | RESOLVED | Brief P3 "Will dates the embassy to January 1054" ("mittere non neglexit (m. Januario 1054)", WILL l.4075-4077); P4 gives 24 June to Nicetas, "the account says" (the main verb "anathematizavit", "ante praesentiam praefati imperatoris", l.14803-14810); card `dates` 1 and `uncertain` 7 ("No held source gives the day the envoys arrived"). |
| A-B2 (the day told as settled) | RESOLVED | P1 "On a Saturday in July"; P2 "Will reads its date as 16 July 1054, and Carl Mirbt gives 13 July." |
| A-B3 (the envoys' side of the failed meeting told as fact) | RESOLVED | P5 gives both accounts; card `uncertain` 3; records add the contested claim. |
| A-B4 ("unless they repent" dropped) | RESOLVED | P5. |
| A-B5 (the Edict's answer on the creed missing) | RESOLVED | P6, "The Greeks will not corrupt the creed, it says, for they hold that the Spirit proceeds from the Father" ("adulterare nolumus … sed ex Patre dicimus procedere", l.15380-15388). |
| A-M1 (the pope's death left vague) | RESOLVED, but the sentence now floats at the end of P7, out of order (R2-1-M1) | |
| A-M2 (bread of the Mass) | RESOLVED in the brief. The records claim still says "'the bread of the Mass' renders 'De azymo'" (R2-1-M3). | |
| A-M3 (Gfrörer's side) | RESOLVED. The card names him bare (R2-1-M2). | |
| A-M4 (forged letters, not seals) | RESOLVED | P6. |
| A-M5 (floating P8, "this curse") | RESOLVED | P8 cut; P9 and `remembered` 3 as proposed. |
| A-M6 (three Leos) | RESOLVED | "Pope Leo IX", "Leo, archbishop of Ohrid", then "Leo of Ohrid"; Leo of Ostia is gone from the brief. |
| A-M7, A-M8, A-M9, A-M12 | RESOLVED | Card as proposed; title now 17 words. |
| A-M10 | DECLINED-ACCEPTABLE | No change was asked. |
| A-M11 (records) | PARTLY RESOLVED | The note locators and the new claims are in. Two stale strings remain (R2-1-M3). |

**The changed sentence.** "The pope never sent the envoys, the edict adds." holds: "ipsi ex se advenerant nullo modo a papa missi" (l.15645-15646). It also fixes the pronoun.

**Is 1054 now told fairly from both sides?** Yes. Each side is heard on doctrine and on conduct, and each contested reading has an owner. On doctrine, the Latin sentence gives simony and the creed (P5), and the Edict gives the Greek answer on the creed (P6). On conduct, the envoys say the patriarch avoided them, and Michael says they would not greet him, bow or sit below his bishops (P5). Each side's forgery charge is given (P6, P7). Both curses are told: the Latin one keeps its condition, and the synod's falls on "the paper and its makers". Will is marked as taking the envoys' side (P7, card `uncertain` 1), and the dates he sets are told as his. The Edict's insults (darkness, wild boar) are its own words, and the Latin side is likened to old heretics in its own words, so neither side is given only insults. I found no held Greek line the brief needs that it leaves out.

#### New findings

- **R2-1-M1 MINOR (brief P7, last sentence, and audio; item 4; a statement with no context, told out of order).** "Will dates Pope Leo's death to 19 April, before the sentence." comes after the July events and is joined to nothing around it. Put it with the other dates, in P3. Fix, P3 second sentence: "Will dates the embassy to January 1054, and Pope Leo's death to 19 April." (13 words.) Then delete the P7 sentence. Scored copy: 394 words, about 2:26, FK 7.24, Flesch 70.57, longest sentence 24.
- **R2-1-M2 MINOR (card `keyWorks` 3, `uncertain` 2, `sources.about` 4 to 6; items 8 and 12).**
  - `keyWorks` 3 names "Gfrörer" bare. Will prints "A. Fr. Gfroereri historia ecclesiastica" (l.1351). Fix: "Will reports that the church historian A. F. Gfrörer thought it was brought from Rome." (15 words.)
  - `uncertain` 2 is Argyrus's first card mention, with no gloss. Fix: "…that they came on the advice of Argyrus, the Greek governor in Italy, …" (the records already cite "catapanum graecum", l.4151).
  - The Wibert, Leo of Ostia and Sigebert/Ekkehard entries in `sources.about` have no `date`, while every other entry has one. Add `"date": "1861"` after `author` (Will's volume, which quotes them).
- **R2-1-M3 MINOR (records).** Claim 6 still ends "'the bread of the Mass' renders 'De azymo'". The brief now says "unleavened bread at Mass", so that ending should read "'unleavened bread at Mass' renders 'De azymo'". Claim 14 ends "The brief now gives Will's date for the death (19 April) instead of Leo of Ostia's line". That is process narration in a claim (lessons §2, "Records and notes"). Replace it with "Will's date for the death is used".

**Verdict, Humbert of Silva Candida: CLEAR on the blocking bar. All 5 R1 blocking points are resolved. There are 0 new blocking points and 3 minor ones (R2-1-M1 in the brief and audio; R2-1-M2 card; R2-1-M3 records).**

---

### Hincmar of Reims

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B6 (Pertz's preface given to Waitz) | RESOLVED | Brief P2 and P6, card `keyWorks` 1, `remembered` 1, `uncertain` 1, `sources.about` 1; "G. H PERTZ." BERT l.249, caution l.247-248. |
| A-B7 (845 and 882 falsely absent) | RESOLVED | P2; card `dates`, `uncertain` 4; MANSI15 l.5421-5428 ("ordinatus est Hincmarus"), AA11 l.3738-3739 ("finientes anno quo hic obiit 882"); Mommsen in `sources`. |
| A-B8 (the nephew's own complaint falsely absent) | RESOLVED | P5 ("violentia hostili in medio itinere segregatus sum", MANSI17 l.36797-36798; "ferro vinctus … Duobus annis ferme peractis, insuper caecatus sum", l.36887-36889); card `uncertain` 1 and 2; sources. |
| A-B9 (the saints' protection in the narrator's voice) | RESOLVED | P1 last sentence as proposed. |
| A-B10 (Antonio made to blame Hincmar) | RESOLVED on this card (`remembered` 3). The same fault stands on the Prudentius card (R2-1-B2). | |
| A-B11, A-B12 | RESOLVED | `traces` 3, `uncertain` 3. |
| A-M13, A-M14, A-M15, A-M16, A-M17, A-M19, A-M20, A-M21, A-M22 | RESOLVED | Applied as proposed. "J. D. Mansi" at the first card mention (`dates`); "Charles the Bald"; Krusch moved to `sources.about`; the README line is added; the records hold all the new claims. |
| A-M18 (Cellotius not marked) | PARTLY RESOLVED | He is marked in `traces` 2, but by surname only at his first card mention (R2-1-M6). |

**The new text, checked as a first review.**
- P3, "The bishops at Douzy wrote that the uncle had raised him as an orphan, taught him his letters and made him a bishop." This holds. The synodal letter to Hadrian has "metropolitanus suus, qui orfanum benigne illum nutrivit, in clericum totondit, litteris erudivit, per singulos gradus … ad apicem episcopatus provexit" (MANSI16 l.66386-66391). Hincmar's own letter has "illum me ordinare in episcopum", which supports "made him a bishop". The order and the marking are R2-1-M4.
- P4, the warning. "si forte … cujuscumque suggestione vel postulatione, apostolicae sedi surreptum fuerit, ut idem … in gradu restitutus … quicquid vellet, licenter agere posset, sciens nos de singulis Romam mittere non posse" (l.66904-66915). "Tricked" fits "surreptum". The "knowing" is the nephew's, since "sciens" agrees with "idem", and the brief keeps it his. The letter is dated "VIII. Idus Sept. … 4. Indictionis" (l.66955-66956).
- P4, "The pope had blamed the uncle for leaving his nephew without help." This holds. Hincmar quotes the pope's letter: "Hincmarus nepos … non minima in ecclesia sua sustineat detrimenta: si me tepescente nullam potuit consolationem invenire" (l.67135-67140).
- P4, "Hincmar answered that he wished he had never seen the man, still less ordained him." The words hold: "Quem utinam non vidissem, minime autem illum me ordinare in episcopum contigisset" (l.67153-67154). In the left column "Quem" is the nephew ("cum illo", l.67150). The framing is R2-1-M5.
- P4, "Hadrian rejected the sentence, a note in Mansi says, but Pope John VIII later wrote that it was just." This holds (l.53133-53137, 53945-53951). The note adds that Hadrian's letter to the synod is printed among his letters (l.53138-53140; Mansi 15 l.7615 and from about l.90676). That is not an absence, so it is not a finding.
- Records: the two new claims cite l.66365-66390, 66901-66916, 66960, 67136-67141 and 67153-67155. All are within a line or two and correctly tagged Documented.

**Whole brief, read as a listener.** P1, P2, P5 and P6 are faithful as R1 found them. The extension replaced the brief's only predestination sentence. Hincmar's quarrel with Gottschalk and Prudentius now appears only on the card (`dates`, `traces` 3, `uncertain` 3). The brief still tells a position he fought for: the limits on appeals to Rome. Nothing in it is wrong, so I raise no finding. The lead may still want the predestination sentence back if room is found.

#### New findings

- **R2-1-B1 BLOCKING (brief P2, "he carried on the royal annals"; card `knownFor`, `keyWorks` 1 `about`; and audio; item 7; a contested point told as settled, carried over from the sister profile).** Round 1 ruled "royal annals" blocking on the Prudentius profile (B-B3). Waitz reports the point as disputed: "Hos annales sub imperatoris Ludovici et regis Karoli Calvi auspiciis scriptos esse, ut seriem annalium publica auctoritate susceptorum continuarent, alii contenderunt, alii in dubium vocaverunt" (BERT l.250-253). He leans against it and thinks Hincmar kept the codex himself, not the court (l.254-265). Prudentius's profile was fixed. Hincmar's still calls them the royal annals three times, so the two cards now disagree.
  - Brief P2: "From 861 he carried on the annals that Prudentius of Troyes had kept." (13 words, one fewer.)
  - `knownFor` sentence 1: "Archbishop of Reims in Frankish Gaul who carried on the annals now called the Annals of Saint-Bertin from 861 to 882." (21 words.)
  - `keyWorks` 1 `about`: "the annals he carried on after Prudentius of Troyes. Georg Waitz says some have held them to be official annals and others have doubted it. G. H. Pertz, an earlier editor, says hardly anyone but Hincmar could have told some of what they hold, such as his flight to Épernay" (9, 16 and 25 words).
- **R2-1-M4 MINOR (brief P3 and P4, and audio; items 6 and 10; the deposing synod's letter heard as neutral, and before the deposition).** "The bishops at Douzy wrote…" comes two sentences before the listener learns that they deposed the nephew. The letter is in the name of "Hincmarus, Harduicus, Remigius …", with the uncle named first (l.66371). Then "The bishops wrote to Pope Hadrian II." sounds like a second letter, but it is the same one. Fix, P3 and P4 as follows (scored copy):
  - P3: "He fought for years with his nephew and namesake, Hincmar, bishop of Laon. The annals call the nephew a bishop in name only, a man of singular insolence, who rebelled against the king and scorned his archbishop. At Douzy in 871 a synod deposed him." (13, 24 and 9 words.)
  - P4 opening: "Its bishops, with the uncle named first, wrote to Pope Hadrian II. The uncle had raised the nephew as an orphan, they said, taught him his letters and made him a bishop." (12 and 21 words.) Then "If anyone tricked Rome…" as it stands.
- **R2-1-M5 MINOR (brief P4, "Hincmar answered that he wished…", and audio; item 1; framing a little stronger than the source).** The wish is in his letter to Hadrian, but he says he had already answered the pope's charge in an earlier letter: "Unde jure vestrae auctoritati rescripsi, quod non est modo necesse repetere" (l.67143-67144). Fix: "In his own letter, Hincmar wished he had never seen the man, still less ordained him." (16 words.)
  - After R2-1-B1, M4 and M5 the scored copy has 406 words, about 2:30, FK 6.50, Flesch 74.88, longest sentence 24.
- **R2-1-M6 MINOR (card; items 8 and 12, and length).**
  - `sources.ownWords[2].title` runs 28 words. Fix: "Council of Douzy, letters to Pope Hadrian II, and writings of both Hincmars, in Sacrorum conciliorum collectio 16" (18 words).
  - `traces` 2 has "the writings of both Hincmars of 868", which reads as if 868 were part of their names. It also has bare "Cellotius" at his first card mention. The heading is "OPUSCULA HINCMARI UTRIUSQUE PORRECTA CAROLO REGI APUD PISTAS. Anno … DCCCLXVIII … mense Augusto", "opera ac studio R. P. Ludovici Cellotii Parisini, e societate JESU" (MANSI16 l.75398-75411). Fix: "Mansi's volumes print the writings both Hincmars put before King Charles the Bald in August 868. Ludovicus Cellotius, a Jesuit who wrote to the uncle's credit, says the uncle then fought for his nephew against outside force." (17 and 21 words.) `uncertain` 2 can then read "Cellotius, a Jesuit who took the uncle's side, …".
  - `dates` is Nicolás Antonio's first card mention, with no time. A reader takes his 849 report as a ninth-century witness, the B-B4 fault on the sister card. Fix: "…, says Nicolás Antonio, a Spanish scholar writing after 1650."

**Verdict, Hincmar of Reims: NOT CLEAR. All 7 R1 blocking points are resolved, and 9 of 10 minor ones (A-M18 partly). There is 1 new blocking point (R2-1-B1, in the brief, card and audio) and there are 3 minor ones (R2-1-M4 and R2-1-M5 in the brief and audio; R2-1-M6 card).**

---

### Prudentius of Troyes

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-B1 (Pertz and Bouquet given to Waitz) | RESOLVED | Brief P3; card `dates`, `traces` 1, `uncertain` 3, `sources.about` 1; records. |
| B-B2 (Lebeuf's signs) | RESOLVED | P3: "by the custom of his homeland" ("Prudentium ex Hispania oriundum, patrio more", BERT l.155-156). |
| B-B3 ("royal annals") | RESOLVED here. It was not carried to Hincmar (R2-1-B1). | |
| B-B4 (Antonio with no time) | RESOLVED | P2 and card `dates`. |
| B-M1 to B-M6, B-M8 to B-M11 | RESOLVED | As proposed. The B-M5 sentence brought in a pronoun fault (R2-1-M7). |
| B-M7 (caveat order, loose item 1) | RESOLVED in order. The new item 2's "defenders who answered Hincmar" is part of R2-1-B2. | |
| B-M12 (records) | RESOLVED | One locator is still short by a line (R2-1-M9). |

#### New findings

- **R2-1-B2 BLOCKING (card `remembered` 2, "Nicolás Antonio calls Hincmar's verdict a slander"; brief P5, and audio; card `uncertain` 2; records "Antonio's answer"; item 1; a witness made to say more, the A-B10 fault left on this card).** Antonio does not give the 861 notice to Hincmar. He sets Hincmar apart from it. Hincmar, "ipsum adversarium", calls the dead Prudentius "dominum Prudentium" with honour. "Sed Bertinianus Anonymus, Hincmari metropolitae … velificatus partibus … iniquissime agit" (PL115 l.79616-79627; "laudatus auctor Annalium Bertinianorum", l.79379-79380). The Hincmar card was corrected for this in round 1 (`remembered` 3). This card still puts "Hincmar's verdict" in Antonio's mouth, so the two cards disagree. In the brief, "Hincmar took over the annals. His entry for 861 says … Antonio calls this a slander" lets the listener hear Antonio answering Hincmar. It also tells Pertz's attribution, which Antonio disputes, with no owner.
  - Brief P5 (scored copy): "After Prudentius died, Hincmar took over the annals, Pertz says. The entry for 861 says Prudentius had once resisted Gottschalk, but later turned in bitterness into a fierce defender of the heresy. Antonio calls this a slander, and blames an unnamed annalist on Hincmar's side. He says Prudentius never opposed Gottschalk." (11, 22, 14 and 6 words. "His entry" becomes "The entry" because "His" would now point at Pertz.)
  - Card `remembered` 2: "Nicolás Antonio calls the annal on him a slander. He gives it to an unnamed annalist on Hincmar's side, and says Prudentius never opposed Gottschalk." (9 and 16 words.)
  - Card `uncertain` 2: "Most of what is told of his life comes through Hincmar, his opponent, and the annals, and through defenders who answered them, such as Nicolás Antonio." (25 words.)
  - Records, "Antonio's answer": add "'Sed Bertinianus Anonymus, Hincmari metropolitae … velificatus partibus' (l.79622-79627); Antonio sets Hincmar's own honouring of Prudentius against it (l.79616-79622)". Add a contested claim, "Who wrote the 861 notice", with two sides: Pertz, Hincmar "extra dubium" (BERT l.203-205); Antonio, an anonymous annalist on Hincmar's side.
  - After R2-1-B2 and R2-1-M7 the scored copy has 339 words, about 2:06, FK 7.92, Flesch 63.21, longest sentence 24.
- **R2-1-M7 MINOR (brief P2, "In verses for a Gospel book, he calls himself…", and audio; item 4; pronoun, brought in by the B-M5 fix).** The last man named is Hincmar ("Hincmar, archbishop of Reims, names him Galindo…"), so "he" points to him first. Fix: "In his own verses for a Gospel book, Prudentius calls himself born in Hesperia and brought to the Celts." (19 words.)
- **R2-1-M8 MINOR (card `legacy.traces` 1; item 4; "his" pointing wrongly).** "Hincmar took over the annals after his death, G. H. Pertz says." The card field stands alone, so "his death" reads as Hincmar's. Fix: "Hincmar took over the annals after Prudentius's death, G. H. Pertz says." (12 words.)
- **R2-1-M9 MINOR (records).** The Camusat claim quotes "ex alicujus fortasse capite" but cites l.82847-82866. The phrase is at l.82867. Make it l.82847-82867.

**Verdict, Prudentius of Troyes: NOT CLEAR. All 4 R1 blocking points are resolved. There is 1 new blocking point (R2-1-B2, in the card, brief, audio and records) and there are 3 minor ones (R2-1-M7 in the brief and audio; R2-1-M8 card; R2-1-M9 records).**

---

### Jonas of Bobbio

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-B5 (Susa and the hedged abbacy falsely absent) | RESOLVED | Card `place`, `dates`, `uncertain` 2 to 4, `sources.about` 3; records. "natione non Hibernus, sed Italus Segusii, vulgo Susae, ad radices Alpium … natus" and "forsan huic … successit" (AASS-Mar3 l.197480-197486); "postea Bobolenus et forsan Jonas" (l.197381). The editors' names match the file header ("G. Henschenius and D. Papebrochius"). The Life of Attala of 10 March is not held (searched). |
| B-M13 to B-M17 | RESOLVED | Brief as proposed. |
| B-M18, B-M19, B-M21, B-M22 | RESOLVED | |
| B-M20 (Mansi date) | PARTLY RESOLVED | The date is added, but after `file` (R2-1-M11). |

**Card dates.** "before 642" is Krusch's "ante a. 642" (SRM3 l.31899), and "about 640" is his "c. a. 640" (l.7772). Both are owned.

#### New findings

- **R2-1-M10 MINOR (brief P2, and audio; item 4; pronoun).** "His translator, Dana Munro, says he entered it three years after Columbanus died. Some three years before the preface, he had promised at Abbot Bertulf's command…". The second "he" points first to Munro, the subject just named (the lessons' Mommsen case). Fix: "Some three years before the preface, Jonas had promised at Abbot Bertulf's command to write the saint's deeds." (18 words, no change in count.) Scored copy: 327 words, FK 8.08, Flesch 67.71.
- **R2-1-M11 MINOR (card `sources.about[1]`; item 12; key order).** The keys run `title, author, language, file, date`. Move `date` after `author`.

**Verdict, Jonas of Bobbio: CLEAR on the blocking bar. The one R1 blocking point is resolved. There are 0 new blocking points and 2 minor ones (R2-1-M10 in the brief and audio; R2-1-M11 card).**

---

### Writing checks on the changed text and the whole briefs

I read all four briefs again in full as a listener. I looked for AI tells, narrator "X, not Y", "not X but Y" and "X and never Y" contrasts, colon-reveals, tails and beat lines, triads, unearned adjectives, status register, choppy runs, undefined terms, confusable names and sentences over about 25 words.

- **Contrasts.** The contrasts in the briefs belong to the sources and are attributed: "No wall or human hand … he wrote, but God's power…" (Hincmar), "came to him but would not greet him" (Michael), and the card's "Italian, not Irish" (the Acta Sanctorum editors' "non Hibernus, sed Italus").
- **Closes.** Each close adds a fact, a witness's judgment or the subject's own words. None is a beat line.
- **Pronouns.** The faults are R2-1-M7 and R2-1-M10, and one fault my own R2-1-B2 fix would have added ("His entry" after "Pertz says"), which I have avoided.
- **Order.** The faults are R2-1-M1 and R2-1-M4.
- **Names.** I found no undefined term or confusable name beyond these. The three Leos are kept apart, and the two Hincmars are kept apart by "the uncle" and "the nephew".
- **Length.** Every brief sentence is 25 words or fewer.

### Counts

| Profile | Blocking | Minor | In the brief and audio |
|---|---|---|---|
| Humbert of Silva Candida | 0 | 3 (R2-1-M1 to M3) | M1 |
| Hincmar of Reims | 1 (R2-1-B1) | 3 (R2-1-M4 to M6) | B1, M4, M5 |
| Prudentius of Troyes | 1 (R2-1-B2) | 3 (R2-1-M7 to M9) | B2, M7 |
| Jonas of Bobbio | 0 | 2 (R2-1-M10, M11) | M10 |

### Verdicts

- **Humbert of Silva Candida: CLEAR on the blocking bar, with 3 minor points to apply.** All 17 R1 findings are resolved, partly resolved (A-M11) or declined acceptably (A-M10). 1054 is now told fairly from both sides.
- **Hincmar of Reims: NOT CLEAR.** All 17 R1 findings are resolved except A-M18 (partly). The new Douzy text and Hincmar's letter are faithful to Mansi 16. R2-1-B1 is blocking: "royal annals" is still told as settled, against Waitz, and it contradicts the corrected Prudentius card. There are 3 minor points.
- **Prudentius of Troyes: NOT CLEAR.** All 16 R1 findings are resolved. R2-1-B2 is blocking: the card has Nicolás Antonio call "Hincmar's verdict" a slander, when Antonio blames an unnamed annalist and sets Hincmar apart from it. The brief lets the listener hear the same thing. There are 3 minor points.
- **Jonas of Bobbio: CLEAR on the blocking bar, with 2 minor points to apply.** All 11 R1 findings are resolved except B-M20 (partly).

---

## R2 recheck, part 2: Braulio of Zaragoza, Ildefonsus of Toledo, Julian of Toledo, Beuno

Reviewer: independent Opus, first sight of these files. I edited no profile, records or notes file. I made no git, web, paid or model calls, and used local scripts only. Inputs: `R1_review.md` parts C and D, `R1_changes.md` parts C and D, the four `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, their `records.json` entries and the README lines on them. I opened every cited line again in its vendored file and read it in context, folding two-column interleaves, long s and OCR noise: PL80 (Braulio's letters l.52855-52912, 53686-53845, 54556-54600; Antonio's notice and its note l.51530-51560, 51955-52065); PL96 (Antonio on Ildefonsus l.630-800, 894-912; Julian's Elogium and Cixila l.3640-3880; Cerratensis l.4115-4206; Antonio on Julian l.36858-36912; Felix and the Toledo notes l.37345-37450, 37500-37582, 37660-37675; the Prognosticon preface and letter l.38160-38332; the dedication to Ervig l.45545-45640; contents l.405-430); HISP (Toledo VI canon III l.41720-41780; Toledo XV l.51978-51996, 52560-52585); MGH11 (l.16355-16368, 21940-21952, 31300-31315, 32600-32690); PL85 l.93245-93262; REES (l.318-326, 13395-13465, 13515-13700, 13770-13790); Mirk l.9392.

Fix copies scored by `engine.m1.gates.grade_text` from the repo root: `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/R2p2/braulio-of-zaragoza.brief.R2fix.txt`, `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/R2p2/julian-of-toledo.brief.R2fix.txt`, `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/R2p2/beuno.brief.R2fix.txt`.

**Mechanical checks (all four).** grade_text passes on all four. Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and nothing else (script). Card keys are in batch order; `legacy` is `traces` then `remembered`; `sources` is `ownWords` then `about` (Beuno has `about` only, rightly); at most 3 keyWorks; no null or empty field; every cited file exists; no card sentence over 25 words (script, splitting on . ! ? ;; Julian `uncertain` 2 sentence 2 is exactly 25). One source entry is out of key order (R2-2-M6).

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence | Audio = brief |
|---|---|---|---|---|---|---|
| Braulio of Zaragoza | 327 | 2:01 | 6.83 | 70.37 | 24 | yes |
| Ildefonsus of Toledo | 328 | 2:01 | 7.53 | 67.56 | 23 | yes |
| Julian of Toledo | 337 | 2:05 | 6.87 | 72.94 | 23 | yes |
| Beuno | 342 | 2:07 | 4.88 | 80.97 | 23 | yes |

**On the laws and writings against Jews.** I read Toledo VI canon III whole again (HISP l.41727-41775; heading "De custodia fidei judaeorum"), Braulio's letter to Honorius (PL80 l.53689-53845) and Julian's dedication to Ervig (PL96 l.45560-45640). Braulio's brief P5 is fair and exact: the canon's praise of Chintila, who "nec sinit degere in regno suo eum qui non sit catholicus", is told as the council's; the oath is told without softening; the bishops' "artificioso temperamento ... Christianis blanditiis flecteremus" is told as Braulio's. The card's rumor item now keeps "superstitionem suae religionis" as "what it calls their superstition". One pronoun in P5 needs fixing (R2-2-M1). Julian's P5 now gives the surgeon image with "credo" and "dixerim" and keeps the healthy limbs, so it is exact to the letter. But it tells the Jews' own argument in the narrator's voice, when the only witness to it is Julian's polemic (R2-2-B2). Ildefonsus's files carry no law on Jews; the card's "a Jew" as the third unbeliever follows Antonio's "Judaeus quidam, sectae suae tantum appellatus nomine" (PL96 l.897-904), fairly.

---

### Braulio of Zaragoza

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-B1 (the dumb-dogs answer misreported) | RESOLVED | P5 now: "The pope's rebuke had called them dumb dogs that cannot bark. That did not fit them at all, Braulio answered." The letter: "quae in objurgationem nostri vestra sanctitas indebite protulit ... nihil omnino respectet ... Canes muti non valentes latrare, ad nos ... nullo modo pertinet" (PL80 l.53781-53787). |
| C-B2 (the Praenotatio dispute missing) | RESOLVED, with one hedge to restore (R2-2-M3) | Card `uncertain` 5 and the records give both sides. The note: Mayansius "falso eam Praenotationem Braulioni tributam asserit" (l.52007-52008, 52036-52040); against him, the consensus "veterum quotquot viderim Codicum, ac bibliographorum fere omnium" (l.52054-52058). |
| C-M1 (the king's hedge) | RESOLVED | "he trusted this was God's will" for "si ista in Dei voluntate, ut confidimus, persistunt" (l.54565-54566). |
| C-M2 (the join heard as fact) | RESOLVED in the brief | P2 ends "Ildefonsus does not name Braulio." The card still states the join in `traces` 3, which R1 did not flag. See R2-2-B1. |
| C-M3, C-M4 (no time in the who-line; "see") | RESOLVED | P1 opens "In seventh-century Visigothic Spain"; P3 has "served". |
| C-M5 ("that law") | RESOLVED, with a pronoun to fix (R2-2-M1) | "swear to keep it so" fits "hanc se catholicam non permissurum eos violare fidem ... quod magnopere nostro est tempore conquisitum, debeat illibatum perseverare" (HISP l.41763-41768). |
| C-M6 (Taio framing) | RESOLVED | "me causa joci ... de illo asino" (l.52863-52866); "me posse remordere si velim" (l.52896-52897); "magis volumus sequi eum qui ait: Dorsum meum posui ad flagella ... non remaledicebat" (l.52906-52909). |
| C-M7 (the chronicle's owner and wording) | PARTLY RESOLVED | The source entry, Mommsen and "devout" are in. The split left `remembered` 2 opening on a bare "It", gave the chronicle council numbers it does not give, and turned "pervenientis ad a. 754" into a date. See R2-2-M2. |
| C-M8 (Mommsen's range) | RESOLVED | "obiit sub Chindasuintho rege a. 641-652 teste Ildefonso" (MGH11 l.21948-21949), in `uncertain` 4 and the records. |
| C-M9 (keyWorks 2 pronouns) | RESOLVED | "memoriam hujus et virtutem illius sancti viri" (PL96 l.17096-17098). |
| C-M10 (Antonio's first mention) | RESOLVED | No change needed: `remembered` 1 gives "Nicolás Antonio, in his Bibliotheca Hispana vetus" before `uncertain`. |
| C-M11 (the rumor softened) | RESOLVED | "oraculis venerabilis Romani principis permissum esse Judaeis baptizatis reverti ad superstitionem suae religionis" (l.53835-53838). |

**Changed sentences checked and found faithful.** P1 s3 (l.54565-54572); P2 last; P3 (Ildefonsus XII: "Habuit sacerdotium fere viginti annis ... temporibus Sisenandi, Chintilae, Tulganis, et Chindasvinthi", PL80 l.51530-51533); P5 (above; "In 638" is the note's "aera 676, seu Christi anno 638", PL80 l.52025-52026, and the acts' era 676); P6. Card `uncertain` 3 and 4.

#### New findings

- **R2-2-B1 BLOCKING (card `legacy.traces` 3; item 7; an inference told as fact, against the card's own `uncertain` 2 and the records).** "Eugenius, the archdeacon he gave up to King Chindaswinth, appears in Ildefonsus's book as Eugenius the second, bishop of Toledo." `uncertain` 2 says the match "rests on these two accounts", and records `absent_details` 2 says "No held line joins them in so many words". I found no held line that joins them: Ildefonsus XIV names no Braulio (PL96 l.17048-17067), and Antonio says only that his Eugenius was a Toledo cleric who took the habit at Zaragoza (PL96 l.709-712). The brief was fixed for this in R1 (C-M2). The card was not.
  - Fix, `traces` 3: "Ildefonsus's book tells of a Toledo cleric named Eugenius who became a monk at Zaragoza and then bishop of Toledo, Eugenius the second. He may be the archdeacon Braulio gave up to King Chindaswinth." (23 and 11 words.)

- **R2-2-M1 MINOR (brief P5 s4, and audio; item 4; "Its" points to the wrong noun).** "...who would let no one who was not Catholic live in his kingdom. Its canon on the Jews..." The nearest noun is "his kingdom", so "Its canon" can be heard as the kingdom's. Fix: "The council's canon on the Jews made every later king swear to keep it so." (15 words; +1.) Scored copy: 328 words, about 2:01, FK 6.86, Flesch 70.19, longest sentence 24.

- **R2-2-M2 MINOR (card `remembered` 1 to 3; items 1 and 20; a carried-in dangling "It", numbers the chronicle does not give, and an end year told as a date).**
  - (a) `remembered` 2 opens "It says", and the last noun in item 1 is "the name".
  - (b) The chronicle gives no council numbers. It names Sisenand's council of sixty-six bishops, which Mommsen's note 5 identifies as Toledo IV of era 671, 633 (MGH11 l.32609-32614, 32673-32675). For the council "under Chintila" it gives no number (l.32619-32626). The "sixth" is Antonio's, and Antonio adds that Rodericus calls it the fifth: "sextae, juxta nostrarum editionum ordinem, quam ipse tamen quintam vocat" (PL80 l.51558-51560).
  - (c) Mommsen writes "continuationis historiarum Isidorianarum pervenientis ad a. 754" (MGH11 l.16361-16363). He gives the year it runs to, not its date.
  - Fix, `remembered` 1, sentence 2: "Theodor Mommsen, who edits it, says it runs to 754 and calls the name false." (15 words.)
  - Fix, `remembered` 2: "The chronicle says Braulio shone at a council of Toledo under King Sisenand, which Mommsen identifies as the fourth. Rome later marveled at his eloquence through a letter, it adds." (19 and 12 words.)
  - Fix, `remembered` 3: "At a later council under King Chintila, which Antonio takes as the sixth, the chronicle says he poured devout teaching into Christian minds. It adds that the church still read his short works." (23 and 10 words.) "short works" is right: Mommsen prints "opuscula" (l.32626); Antonio's quotation has "opus" (PL80 l.51553).
  - Records, the chronicle claim: add "council numbers: Mommsen's note 5 (MGH11 l.32673-32675) for IV; Antonio's 'sextae ... quam ipse tamen quintam vocat' (PL80 l.51558-51560) for VI".

- **R2-2-M3 MINOR (card `uncertain` 5; records `contested_claims` side 2; item 1; a hedge dropped in the C-B2 fix).** The note's writer cites the consensus "veterum quotquot viderim Codicum", the old manuscripts he has seen, not all old manuscripts (PL80 l.52054-52055). Fix: "The note keeps it as his, as all the old manuscripts its writer had seen and nearly all bibliographers agree." (20 words.) In the records, read "the consensus of all the old codices he has seen and nearly all bibliographers".

**Verdict, Braulio of Zaragoza: NOT CLEAR. All 13 R1 findings are resolved or partly resolved. There is 1 new blocking point (R2-2-B1, card) and 3 minor ones (R2-2-M1 in the brief and audio; R2-2-M2 and R2-2-M3 on the card and in the records).**

---

### Ildefonsus of Toledo

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-B3 (false absence: birth and family) | RESOLVED | Records claim and card `uncertain` 2: "Natum Toleti ex nobilissimis parentibus Stephano et Lucia Hildefonsum fama fert ... anno hujus saeculi septimo. Lucia soror germana dicitur fuisse Eugenii III" (PL96 l.704-708). Antonio makes this Eugenius his predecessor ("Eugenio ejus avunculo, diem suum obeunte", l.725-727), so "the bishop before him" holds. Antonio's role is in `dates`. |
| C-B4 (false absence: where Agali stood) | RESOLVED | Card `place` and records: "in sanctorum Cosmae et Damiani monasterio, quod et Agaliense audiit, ejusdem urbis" (l.715-718); Cerratensis, "in suburbio sita est Toletano, quae antiquitus Agaliense monasterium dicebatur" (l.4200-4203); the Monitum dates Cerratensis "saeculo xiii" (l.3651). |
| C-M12 to C-M14 | RESOLVED | "Julian's account is a short tribute to him"; "Then he attacked the monastery, sword in hand" for "Armata deinde manu Agaliensem cellam impetens gladio" (l.3713-3714); "held the office"; "his church". |
| C-M15 (Cixila's "fertur") | RESOLVED in the brief and records | "She is said to have thanked God" for "talia fertur depromere vota" (l.3844-3848). The card's `remembered` 1 still drops it (R2-2-M5). |
| C-M16 (the death day) | PARTLY RESOLVED | The Missale side is in (PL85 l.93258, in the January list: XI Vincent, X Ildefonsus). But the "possibly OCR" reading is not borne out. See R2-2-M4. |
| C-M17 (the signatures) | RESOLVED | "inde Toletano concilio viii, anno quinquagesimo tertio, necnon et ix, circa annum 657, ut e subscriptionibus constat" (l.731-734). |
| C-M18 to C-M20 | RESOLVED | keyWorks 1 (l.897-904); `uncertain` 5; `traces` 1 ("in appendice ad librum de Viris illustribus ab ipso Hildefonso conscriptum", l.3663); `traces` 2 ("missam superscriptam, quae in ejus laude decantaretur, perfecit, quae est septima", l.3870-3873). |

**Changed sentences checked and found faithful.** P1 last; P2 s3; P3 ("held the office for nine years and about two months"); P4 last; P5 last. Card `dates`, `place`, `uncertain` 2 to 5, keyWorks 1, `traces` 1 and 2. "He built a convent for women" rests on "Coenobium quoque virginum in Deibiensi villula construxit" (l.3725).

#### New findings

- **R2-2-M4 MINOR (card `uncertain` 3; records `contested_claims` side 2; item 1; a witness's side told as a likely misprint, carried in by the C-M16 fix).** The card says "Nicolás Antonio quotes Julian's day, but the held copy of his notice prints 25 January". The records say "possibly OCR or a slip". The same notice gives 25 January again where it cites Tamayo's Spanish martyrology, "Martyr. Hisp., die 25 Jan." (PL96 l.724), its note (b) cites the Astorga breviary "apud Tamaium, 25 Januar." (l.767), and a later note has "Tamaius hac die 25 Januarii" (l.862). Antonio also ties his day to the Roman Martyrology: "die Januarii 25, ad quem diem refertur ejus memoria in Romano Martyrologio" (l.659-661). The 25 is his reading, backed by named calendars. It is not a likely OCR fault.
  - Fix, `uncertain` 3, last sentence: "Nicolás Antonio quotes Julian's day, yet gives 25 January, the day he says the Roman Martyrology keeps his memory." (19 words.)
  - Fix, records side 2: "Nicolás Antonio: 'die Januarii 25, ad quem diem refertur ejus memoria in Romano Martyrologio' (PL96 l.659-661), in a sentence quoting Julian's X Kal. Feb.; the notice cites Tamayo's martyrology at 25 January (l.724, 767, 862)". The lead should withdraw the Open-Gaps OCR flag R1 raised on this "25".

- **R2-2-M5 MINOR (card `remembered` 1; item 1; a hedge dropped).** "...rises from her tomb before King Reccesvinth and thanks God that her Lady lives through the life of Ildefonsus." Cixila hedges the words, "talia fertur depromere vota" (l.3844), and the brief keeps the hedge. Fix: "Cixila, a bishop of Toledo under Muslim rule, wrote a later Life. In it Saint Leocadia rises from her tomb before King Reccesvinth. She is said to have thanked God that her Lady lived through the life of Ildefonsus." (12, 10 and 17 words.)

- **R2-2-M6 MINOR (card `sources.about` 5, the Missale mixtum; item 12; key order).** The keys run `title`, `language`, `file`, `date`. Every other entry runs `title`, (`author`), `date`, `language`, `file`. Fix: move `"date": "1862"` before `"language"`.

**Verdict, Ildefonsus of Toledo: NOT CLEAR. All 11 R1 findings are resolved or partly resolved. There are 0 new blocking points and 3 minor ones (R2-2-M4 to R2-2-M6, all on the card and in the records).**

---

### Julian of Toledo

| R1 finding | Verdict | Evidence |
|---|---|---|
| D-B1 (the dedication told loosely) | PARTLY RESOLVED | The surgeon image now matches the letter: "Hujus admirabilis medelae peritiam credo vestram ... voluisse imitari clementiam" (PL96 l.45597-45599); "ne locus vulneris sana membra contingat" (l.45592); "Horum igitur membrorum evitandam putredinem linguas dixerim Judaeorum" (l.45610-45611). The title is right ("De Comprobatione aetatis sextae Libri tres", l.413). But the Jews' argument is now told in the narrator's voice. See R2-2-B2. |
| D-B2 (a dead pope told as the one answered) | RESOLVED | "Pope Benedict, now dead, had raised points ... two years before" for "ante hoc biennium beatae memoriae Romanus papa Benedictus" (HISP l.51988-51990). README line reworded and true. |
| D-B3 (false absence: Felix's death notice) | RESOLVED; one more held side noted (R2-2-M9) | "annis decem obtinuit, mense uno, diebus septem ... anno tertio Egicanis principis, pridie Nonas Martii, aera septingentesima vigesima octava" (PL96 l.37355-37358); the note, "pridie Nonas Martii (scilicet die vi) aera 728 (hoc est anno Dom. 690) ... consecratum fuisse anno 680, die 29 Januarii" (l.37362-37367). The `dates` and `uncertain` 3 items are true. |
| D-M1 (a hedge and a verb) | RESOLVED | "Tunc ego, ni fallor, urgentibus vobis, accito notario" (l.38302-38303); "recordari me contigit. Egi ergo ... quae promisi" (l.38322-38326). |
| D-M2 (no time in the who-line) | RESOLVED | "a seventh-century bishop of Toledo"; the preface's "saeculo septimo vixerat" (l.38181-38182). |
| D-M3 (the Prognosticon year) | RESOLVED | "Quod si conjectura aliquid assequi possumus, ad annum 688 vel 689 ... referenda videtur ... non constat Toletum venisse, praeterquam ad concilium Toletanum xv" (l.38168-38172). |
| D-M4 (Isidore Pacensis; Lorenzana) | RESOLVED | "Increbuit apud posteros fama ... subdubitari a quibusdam video. Plures tamen Roderico credunt nec temere" (l.36870-36875); "Caveat itaque lector, ut facile Isidoro Pacensi credat ... e quibus enim monumentis illud acceperit, adhuc ignoramus" (l.37574-37577); "medio saeculo post Felicem auctor" (l.45586-45587). One gloss is past Mommsen's held view (R2-2-M8). |
| D-M5 (the four signatures) | RESOLVED | Records cite HISP l.49064, 50783, 51683, 52960 with Antonio (PL96 l.36894-36899), tagged Documented. |
| D-M6 (length) | DECLINED-ACCEPTABLE | The Wamba sentence was cut instead of Gudila's. Wamba stays on the card (keyWorks 3). The brief runs 337 words, about 2:05. |

**Changed sentences checked and found faithful.** P2 s2 and s3; P3 s1; P5 s1, s3 and s4; P6 s1 to s3. Card `dates`, keyWorks 2 s1 and s3, `remembered` 2 ("non solum in Breviario Toletano die 8 Martii ... sed et apud Usuardum 6 ejusdem", l.36901-36903; the note's "dies sexta Martii, non octava obitus S. Juliani", l.37405-37406), `uncertain` 2 to 4.

#### New findings

- **R2-2-B2 BLOCKING (brief P5 s2, and audio; card keyWorks 2 `about` s2; items 1 and 6; a polemicist's account of his opponents told in the narrator's voice).** "They counted the years from Creation and said the world was still in its fifth age, so Christ had not yet come." The only witness is Julian's dedication, which puts the argument in his own hostile terms: the Jews "pestilentiosis objectibus garrientes, quod sumpta annorum supputatio ab initio mundi secundum Hebraeos codices quintam adhuc saeculi aetatem insinuet, et necdum adhuc Christum venisse, quem in sexta credunt aetate saeculi advenire" (PL96 l.45614-45619). R1 had the content right. Its fix (D-B1) put the argument before "In the opening letter, Julian says...", so a listener hears it as the narrator's own account of what Jews of the day held. The card's "They reckoned" has the same fault. The book's account must be told as the book's (lessons 1.17), and a hostile witness must be marked.
  - Fix, brief P5, sentences 2 and 3 (replace "They counted ... healthy limbs."): "In the opening letter, Julian says they counted the years from Creation. By that count, they said, the world was still in its fifth age, so Christ had not yet come. He says he believes the king follows the surgeon, who cuts away rot before it reaches healthy limbs." (12, 18 and 18 words; +5.) Scored copy: 342 words, about 2:07, FK 6.63, Flesch 73.89, longest sentence 23.
  - Fix, card keyWorks 2 `about`: "three books written at King Ervig's command, against Jews of his day. The opening letter says they reckoned the world was still in its fifth age, so Christ had not yet come. It calls their tongues the rot a surgeon cuts away before it reaches healthy limbs" (11, 20 and 15 words.)

- **R2-2-M7 MINOR (card `dates` s2; item 4; undefined term).** "...died in the third year of King Egica, in era 728." "Era" is never glossed on this card. Fix: "in the Spanish era 728", as the Braulio and Ildefonsus cards write it. (+2 words; 26 words. To stay at 25 or under, drop "King" or split: "Felix says he held the see ten years, one month and seven days. He died in the third year of King Egica, in the Spanish era 728." 13 and 15 words.)

- **R2-2-M8 MINOR (card `uncertain` 2 s2; item 1; a held judgment on the name left out).** The card makes "Isidore Pacensis" "a chronicler of half a century after Felix". Theodor Mommsen, in a held edition, prints that chronicle as the "Continuatio Hispana a. DCCLIV" and calls the name "ficticio" (MGH11 l.16361-16363, 31309). The Braulio card in this batch already says so. Fix: "Nicolás Antonio reports this as a story among later writers, from Rodericus of Toledo and the chronicle under the name of Isidore Pacensis." (23 words.) Then add: "That chronicle runs to 754, Theodor Mommsen says, and the name is false." (13 words.) Add the MGH11 file to `sources.about`, as on the Braulio card.

- **R2-2-M9 MINOR (records `contested_claims`, "When he became bishop"; card `uncertain` 3 optional; item 7; a held side missing).** The Toledo note also reports Ambrosio Morales. Using a faulty codex, Morales held that the start of Julian's episcopate could not be fixed, and he gave him no more than nine years, four months and five or six days. The note rejects this: "Non est itaque audiendus Ambrosius Morales, qui vitiato Codice usus ... neque amplius quam novem annos, quatuor menses et quinque sexve dies in Toletana cathedra sedenti esse attribuendos" (PL96 l.37392-37397). Fix, records: add a third side, "Ambrosius Morales, as reported and rejected by the Toledo note: no fixed start, at most nine years, four months and five or six days (l.37392-37397)". The card may stay as it is.

**Verdict, Julian of Toledo: NOT CLEAR. Of the 9 R1 findings, 7 are resolved, 1 is partly resolved (D-B1) and 1 is declined acceptably (D-M6). There is 1 new blocking point (R2-2-B2, in the brief, audio and card) and 3 minor ones (R2-2-M7 to R2-2-M9, on the card and in the records).**

---

### Beuno

| R1 finding | Verdict | Evidence |
|---|---|---|
| D-B4 (no time for his life until the end) | RESOLVED, with a name clash carried in (R2-2-M10) | P3 now places him through the note: "He lived in the sixth century, and his life extended to the following, as it is recorded that he founded a religious society, at Clynog Fawr ... in the year 616 ... — Professor Rees's Welsh Saints, page 268" (REES l.13452-13462). P6 is true. |
| D-B5 (Mirk's date from the header) | RESOLVED | Card `remembered` 2 has no year; "a holy heremyt that was callet Bewnow" (Mirk l.9392). The records say the year is the header's only. |
| D-M7 ("monk") | RESOLVED | "took orders, and became a clergyman" (REES l.13439-13440), in the brief, `knownFor` and `role`. |
| D-M8 ("held") | RESOLVED | "The few other accounts of him are late as well." |
| D-M9 (two Reeses) | PARTLY RESOLVED | The note is now "a note in W. J. Rees's edition, quoting a Professor Rees". But the brief then says "Rees" alone twice, after both men are named. See R2-2-M10. |
| D-M10 (Cadwallon) | RESOLVED | "Cadwallon his son, who was king after him", Cadvan "king of North Wales" (l.13636-13639). |
| D-M11 (the death day) | RESOLVED | "on the seventh day after Easter, he saw heaven opening" (l.13782-13784); festival "April 21" (l.13457). |

**Changed sentences checked and found faithful.** P2 last; P3 s1 to s2; P4 s1; P6. Card `knownFor`, `dates`, `role`, `remembered` 2, `uncertain` 2. The note ends "— Professor Rees's Welsh Saints, page 268", the way the note on Bugi ends "— T. WAKEMAN." (l.13462; l.13421), so "quoting a Professor Rees" is fair. The note's own words are "a religious society"; "religious house" is close enough for one community at one place.

#### New finding

- **R2-2-M10 MINOR (brief P4 last-but-two sentence and P5 last sentence, and audio; card `uncertain` 1; item 8; a name a listener can confuse, carried in by the D-B4 fix).** After P3 names both "W. J. Rees" and "a Professor Rees", the brief says "in Rees's English" (P4) and "Rees places it in Flintshire" (P5). Either Rees could be meant. The card's `uncertain` 1 ("manuscripts Rees printed ... and Rees thought") follows `dates`, which names the professor.
  - Fix, brief: "he said, in W. J. Rees's English." and "W. J. Rees places it in Flintshire." (+4 words.) P6's "The same note" still points to P3's note, since P5 no longer says "note". Scored copy: 346 words, about 2:08, FK 4.32, Flesch 82.63, longest sentence 23.
  - Fix, card `uncertain` 1, s2: "The Welsh Life is from manuscripts W. J. Rees printed in 1853, and he thought such Lives were probably compiled about the twelfth century." (24 words.)

**Verdict, Beuno: NOT CLEAR. All 7 R1 findings are resolved or partly resolved. There are 0 new blocking points and 1 minor one (R2-2-M10, in the brief, audio and card).**

---

### Writing checks on the changed text and the whole briefs

I read all four briefs again in full, as a listener, for AI tells, narrator contrasts ("X, not Y", "not X but Y", "X and never Y"), colon-reveals, tails and beat lines, triads, unearned adjectives, status register, choppy runs, undefined terms and names a listener could confuse.

- The contrasts that remain belong to the sources: "had burst ... rather than been cut" (Braulio's "disrupto potius quam scisso", PL80 l.54597) and "He would rather follow Christ" ("magis volumus sequi eum", l.52908).
- I found no colon-reveal, rhetorical question or aphorism.
- Julian's close ("Felix calls him a man full of the fear of the Lord.") is a sourced line, not a beat.
- The fixes cause no choppy runs. Braulio P1 and Beuno P4 keep their mix of long and short sentences.
- "Kalends" is on the Ildefonsus card only, glossed as a day ("which is 23 January").
- "see" now appears on cards only (Ildefonsus keyWorks 2, Julian `dates`), where it is read, not heard.
- The pronoun faults and name clashes are R2-2-M1 and R2-2-M10.
- Julian's brief runs 337 words, and 342 with R2-2-B2. Beuno's runs 342, and 346 with R2-2-M10. Both are a little over the 325 to 340 band for a standard brief, which still reads as about 2:05 to 2:08. I make no finding on that.

### Counts

| Profile | Blocking | Minor | In the brief and audio |
|---|---|---|---|
| Braulio of Zaragoza | 1 (R2-2-B1) | 3 (R2-2-M1 to M3) | R2-2-M1 |
| Ildefonsus of Toledo | 0 | 3 (R2-2-M4 to M6) | none |
| Julian of Toledo | 1 (R2-2-B2) | 3 (R2-2-M7 to M9) | R2-2-B2 |
| Beuno | 0 | 1 (R2-2-M10) | R2-2-M10 |

### Verdicts

- **Braulio of Zaragoza:** NOT CLEAR. All 13 R1 findings are resolved or partly resolved (C-M7 partly). There is 1 new blocking point (R2-2-B1: card `traces` 3 states the archdeacon-to-bishop join as fact) and there are 3 minor ones.
- **Ildefonsus of Toledo:** NOT CLEAR. All 11 R1 findings are resolved or partly resolved (C-M16 partly). There are 0 new blocking points and 3 minor ones.
- **Julian of Toledo:** NOT CLEAR. Of the 9 R1 findings, 7 are resolved, D-B1 is partly resolved and D-M6 is declined acceptably. There is 1 new blocking point (R2-2-B2: the Jews' argument told in the narrator's voice, in the brief and card) and there are 3 minor ones.
- **Beuno:** NOT CLEAR. All 7 R1 findings are resolved or partly resolved (D-M9 partly). There are 0 new blocking points and 1 minor one.
- **For the lead (Open-Gaps):** withdraw the R1 flag that Antonio's "25" in the Ildefonsus notice may be OCR (R2-2-M4). The notice gives 25 January four times, with named calendars.
