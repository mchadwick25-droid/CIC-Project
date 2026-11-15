# Council profiles, era 4: review round 2, targeted recheck (2026-11-15)

## Scope and method

- **Scope.** The six era 4 major-council profiles in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era4/`. Only what round 1 changed was rechecked: every string in `git diff HEAD~1` (commit 8c7b3261) across the briefs, entries, audio scripts and `records.json`, against `R1_review.md` and `R1_changes.md`. Unchanged text was not re-reviewed, except where a round 1 fix left the same fault standing in a sister field.
- **Reviewer.** Independent Opus, not the drafter and not a round 1 reviewer. No profile file was edited.
- **Standard.** `Council_Profile_Pattern.md` C1-C8; `Who_Profile_Pattern.md` items 1-9, 11, 13; CLAUDE.md "Trust and source fidelity" and "Accessible and rigorous".
- **Sources.** Every new or changed claim was opened at its cited file:line under `cic/texts/` and read in context, tolerant of OCR and long-s. Files: Mansi 10, 11, 15, 31; Theophanes PG 108 (Chronographia and the Life printed before it); Michael the Syrian t.2 (Chabot); Foulke's Paul the Deacon; Mirbt; NPNF 14; PL 80 (Columbanus); Bede in Giles; Stephen in Raine; Serpos's Dissertazione; Duchesne's Liber Pontificalis t.1 and t.2; the Pedalion; PG 99; PG 100.
- **Absence checks.** Searched for Deusdedit's collection (not held), for an Armenian answer to Trullo earlier than Serpos (Chamich, Issaverdens, Langlois, RHC Arméniens, Rycaut: none), and for Theophanes at Nicaea (found, R2-NIC-1).
- **People verdicts.** Checked against `Who_Scan_Era4.md` l.153 (Tarasios LISTED, spot-check confirmed) and l.160 (Peter, Theodore of Pharan LISTED), `Who_Scan_Era6.md` l.119 (Mark of Ephesus WHO), and the eras 4-5 rescore (Theophanes WHO as recorder, Theodore the Studite WHO).
- **Readability and audio.** Each brief was scored with `engine.m1.gates.grade_text`. Sentences were split and counted; none is longer than 25 words. Each audio script was compared by script with its brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph. All six match exactly, with two tags each.
- **Scratch copies.** The two brief fixes proposed below were applied to scratch copies and rescored: `/tmp/claude-0/-home-user-CIC-Project/3fc04891-4b0e-5b02-a097-fe39a900e3e5/scratchpad/R2/third-council-of-constantinople-680.fixed.txt` (398 words, FK 7.66, FRE 66.88) and `/tmp/claude-0/-home-user-CIC-Project/3fc04891-4b0e-5b02-a097-fe39a900e3e5/scratchpad/R2/quinisext-council-692.fixed.txt` (400 words, FK 7.79, FRE 62.23).
- No model calls, no network, no paid services.

## Per-council tables

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| lateran-council-649 | 398 | 7.44 | 67.64 | yes | CLEAR WITH MINORS |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| third-council-of-constantinople-680 | 400 | 7.66 | 67.01 | yes | NOT CLEAR (R2-CP3-1) |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| synod-of-whitby-664 | 399 | 6.26 | 75.45 | yes | CLEAR WITH MINORS |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| quinisext-council-692 | 399 | 7.77 | 62.36 | yes | CLEAR WITH MINORS |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| second-council-of-nicaea-787 | 401 | 7.88 | 61.06 | yes | NOT CLEAR (R2-NIC-1) |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| councils-of-constantinople-861-880 | 402 | 7.95 | 62.20 | yes | CLEAR WITH MINORS |

The scores match `R1_changes.md`. All six pass FK 10 or below and FRE 60 or above, and all sit at the 400-word cap. Whitby's FK of 6.26 is below the grade 8 floor (see "Not taken", below).

## Round 1 substantial findings

- **LAT-1: CLOSED.**
  - Brief l.15: "Theophanes says Constans, in fury, had Martin and Maximus brought to Constantinople and tortured. Martin died in exile at Cherson." Theophanes: "Martinum et Maximum Cpolim adduci jussit, eosque tormentis excruciatos in exsilium deportari" (THEO l.60843-60847). Martin's death "in eadem exulatione Chersonae" is in his clergyman's account (M10 l.88326-88340). The joint exile to Cherson is no longer told in the narrator's voice.
  - The entry's `outcome[1]`, the Maximus people line, `uncertain[5]` and the new records claim all agree. The Binius and Foulke lines added for LAT-8 say what is claimed (M10 l.117080-117103; FOULKE l.9938-9939).
- **CP3-1: OPEN, in part.** The brief now reads: "The condemned reach us only through their opponents' records. Michael the Syrian … tells it from a church that rejected the council." Michael is not an opponent of the condemned. He reports Macarius's case with approval: "Macarius d'Antioche disputa longuement … et montra clairement que c'est une hérésie d'admettre deux volontés ou opérations dans le Christ" (MICH l.34505-34510). The "only" is therefore still false, one witness narrower than before. See R2-CP3-1.
- **WHI-1: CLOSED.**
  - Columbanus's letters are where cited. Letter I is to Gregory (PL 80 l.20268-20280). Letter II reads "plus credo traditioni patriae meae juxta doctrinam et calculum lxxxiv annorum et Anatolium … quam juxta Victorium" (l.20791-20796).
  - The entry's `issue[3]`, `record`, `sources` and `uncertain[0]` and the corrected absent detail are right. The brief's "The Irish side reaches us only through these two" is about the meeting and stands.
- **QUI-1: CLOSED.**
  - The brief says "No Armenian answer from the time survives in the books we draw on."
  - Serpos calls the council a "Pseudosinodo" gathered "senza veruna autorità, non avendovi prestato il suo consenso il Pontefice Romano", and says its canons rebuke the Armenians ("sono semplicemente ripresi") but "non mai si anatematizza la Nazione" (Serpos l.1036-1072). No earlier Armenian answer was found (see Method).
- **QUI-2: CLOSED.** The close gives Percival's side: "Percival says the signatures show they were not the same bishops." This matches "the bishops were not the same, as can readily be seen by comparing the subscriptions" (NPNF l.26420-26422). The close stays sourced and does not sum up.
- **PHO-1: CLOSED.**
  - The Pedalion has the seventeen canons of the second meeting: "ἐξεδόθησαν καὶ οἱ παρόντες ιζ’. κανόνες" (l.33300). It says the minutes are not found: "ταύτης οὐχ εὑρίσκονται πρακτικά" (l.33335-33336). It sends the envoys "κατὰ τῶν εἰκονομάχων" (l.33227). Its date is right ("ἐν ἔτει 861", l.33223).
  - The Book of the Popes gives both errands: the question of images, and inquiry into Ignatius's case (LP t.2 l.48974-48976, 49600-49604).
  - Deusdedit's collection is not held. "Mainly through Photius's enemies" is true.
  - Two sister-field remnants are in R2-PHO-1 and R2-PHO-2.

## Round 1 minor fixes marked fixed

The minor fixes were checked against their files. These are right as made:
- LAT-3 to LAT-11.
- CP3-2 to CP3-9. Michael: "malgré eux, ils signèrent de force la définition" (MICH l.34515-34516); NPNF l.24647-24648 "more or less"; Foulke l.11253-11283; Mirbt l.8038.
- WHI-2 to WHI-6 and WHI-8 to WHI-12. Bede: "it is said to have happened" (l.7895-7897); "about eighty years after they had sent Aidan" (l.15030); "built a monastery in the isle of Hii" (l.15269). Stephen names Agatho and Wilfrid (Raine l.5138-5140); "Hec ratio discipline Apostolice sedis est, et pene totius mundi" (l.5149).
- QUI-3 to QUI-9, QUI-11 and QUI-12. Mansi's preface: eight leading signers, then "ducentorum & quinque subsunt episcoporum subscriptiones" (M11 l.89062-89077).
- NIC-1 to NIC-9. Percival l.41521-41523 (after Irene's death in 803); the Life of Methodius l.103893-103897 ("Tunc … firmam obtinuit auctoritatem"); PG 99 l.69540-69541; Percival l.37900-37901 (Michaud).
- PHO-2 to PHO-10, PHO-12 and PHO-13. LP t.2 l.53405-53409; Pagi in M15 l.63993-64011; Mark in M31 l.53790-53799.

Four fixes were made in one field and left undone in a sister field, or were left part-done without a reason. They are R2-LAT-1 (LAT-2), R2-WHI-1 (WHI-7), R2-PHO-2 (PHO-11) and R2-QUI-2 (QUI-10, Boniface).

## Round 1 "not taken": judged

- **QUI-10, Tarasius LISTED. Accepted.** The scan row "Tarasios (patriarch) … LISTED … LISTED spot-check: confirmed" (`Who_Scan_Era4.md` l.153) settles it, for the Nicaea entry too.
- **QUI-6, the name explained. Accepted.** The brief never uses the word "Quinisext", so it leaves no undefined term, and the cap is reached.
- **CP3-4, "Simon Magus". Accepted.** It is the narrator's identifier, not a quotation ("Novo Simoni anathema", M11 l.57936-57937), and it lets the listener place the name.
- **PHO-8, Florence. Accepted.** Percival's "the Council of Florence (1438)" is the common name, and the people line says Ferrara-Florence.
- **PHO-9, Ignatius NOT SCORED. Accepted on the merits.** But see R2-GEN-1: the Open-Gaps entry it relies on was not written.
- **Whitby FK 6.26. Accepted.** The short sentences are mostly Bede's spoken exchange. Joining them would push sentences past 25 words or pad the brief. Era 3's Toledo 589 is the precedent.

## New findings

### R2-CP3-1. Substantial (C3; items 1, 6; a false "only"; ambiguous pronoun). third-council-of-constantinople-680

- **Exact text.** Brief l.3: "The condemned reach us only through their opponents' records. Michael the Syrian, a Syriac Orthodox patriarch of the 1100s, tells it from a church that rejected the council."
- **Evidence.**
  - Michael is on the side of one will. He has Macarius show "clairement que c'est une hérésie d'admettre deux volontés ou opérations dans le Christ" (MICH l.34505-34510). He ends by calling the council's teaching "l'hérésie pernicieuse de Maximus" (l.34521-34522). So the condemned reach us through a friendly record as well, and "only" is false.
  - The entry's `uncertain[0]` (entry l.257) makes the same point and calls Michael "from outside both parties", which hides his side.
  - Records `absent_details` (records.json l.544) is right in substance: Michael reports Macarius's argument but not his words.
  - Heard aloud, "tells it" has no clear antecedent. The last "this" was the Zeuxippus scene one paragraph back.
- **Fix, brief.** "The condemned reach us mostly through their opponents' records. Michael the Syrian, a Syriac Orthodox patriarch of the 1100s, sides with one will against the council." That is −2 words: 398 words, FK 7.66, FRE 66.88 (scratch copy).
- **Fix, entry `uncertain[0]`.** "The acts are the winners' record. The condemned reach us mostly through their opponents: these acts, the Roman acts of 649 and Maximus's debate with Pyrrhus. Michael the Syrian, of a church that rejected the council, takes Macarius's side and reports his argument, but not his words."
- **Fix, records l.544.** "None found; Michael the Syrian, who takes Macarius's side, reports his argument but not his words; Honorius's letter survives through these acts."

### R2-NIC-1. Substantial (items 1, 7; a false absence in a line added for NIC-3). second-council-of-nicaea-787

- **Exact text.** Entry `people`, Theophanes the Confessor (l.181): "Not present at Nicaea; chronicler of the broken meeting of the year before and of the council".
- **Evidence.**
  - The Life printed with his Chronicle in the file the brief cites says he was called to this council and went to it: "Cum enim Nicaeae synodus secundo coacta esset, ad eam ipse quoque cum aliis Patribus vocatus est … ipse solito cilicino sacco indutus, asinae insidens, laetus iter suscepit. Sed cum omnes viderent eum …" (`theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt` l.1705-1716, continued at l.1816). The Greek reads "τῆς γὰρ κατὰ Νίκαιαν συνόδου συστάσης τὸ δεύτερον" (l.1772-1773, OCR).
  - The line tells as settled an absence that the held Life contradicts, for a WHO figure who opens the brief.
- **Fix.** "Called to the council and came, in a hair shirt and riding a donkey, by the Life printed with his Chronicle; chronicler of the broken meeting of the year before and of the council". No brief change is needed. The brief calls him only "a Greek chronicler for the images".

### R2-LAT-1. Minor (item 1; LAT-2 not carried to the entry). lateran-council-649

- **Exact text.** Entry `issue[3]` (l.35): "Martin told the synod that Paul had persuaded the emperor to issue the Typos to destroy the catholic teaching". This is the gloss LAT-2 removed from the brief. Martin says "typum exponere, qui catholicum dogma destrueret" (M10 l.89929-89931). He names the edict's effect, not Paul's aim.
- **Fix.** "… had persuaded the emperor to issue the Typos, an edict that would destroy the catholic teaching …".
- **Optional.** `record[0]` note and `uncertain[0]` still say the documents are "read into" the acts. Make both "quoted in", as the brief now says.

### R2-WHI-1. Minor (item 9; WHI-7 not carried). synod-of-whitby-664

- **Exact text.** Entry `uncertain[0]` (l.195): "No record of the synod survives. Both accounts, Bede's of 731 and Stephen's Life of Wilfrid, are …". The brief now says "No acts of the meeting survive", and the next words of this field name two records.
- **Fix.** "No acts of the synod survive."

### R2-QUI-1. Minor (C4; the R1 cut hid a modern witness). quinisext-council-692

- **Exact text.** Brief l.13: "Malachia Ormanian, an Armenian patriarch, dates it to 726." The year 726 is the modern dating; Stephen of Taron gives none (`ormanian_church-of-armenia_gregory1912.txt`, 1912). Once "former … of Constantinople" was cut, a listener who has just heard of a synod of the 700s can take Ormanian for a patriarch of that time. C4 asks that a year no ancient witness gives be told as the modern historian's.
- **Fix.** "Malachia Ormanian, a modern Armenian patriarch, dates it to 726." That is +1 word: 400 words, FK 7.79, FRE 62.23 (scratch copy).

### R2-QUI-2. Minor (C7; people lines added for QUI-10). quinisext-council-692

- **John VII (l.196).** "Pope; sent the volumes again, returned them uncorrected" says John sent the volumes. The emperor sent them to him by two metropolitans (LP t.1 l.174288-174291). Fix: "Pope; the emperor sent him the volumes again, and he returned them uncorrected".
- **Anastasius of Jerusalem (l.171).** "Signed in the signatures" repeats itself. Fix: "Signed; not named among the patriarchs by the Book of the Popes".
- **Boniface.** R1 named Boniface, counselor of the apostolic see, with John of Porto: "Iohannem … Portuensem episcopum seu Bonifatium consiliarium apostolicae sedis … in regiam abstulit urbem" (LP t.1 l.170987-170988). He was left out with no reason given. Fix: add "Boniface, counselor of the apostolic see, NOT SCORED, taken to Constantinople by the emperor's order". John of Porto's part could also say "carried off to Constantinople, in contempt of the pope", which is closer to "in spretum".

### R2-NIC-2. Minor (item 4; wording of the NIC-8 fix). second-council-of-nicaea-787

- **Exact text.** Entry `issue[0]` (l.31): "Its decree survives only in the acts of 787, read out in Session VI to be answered, and survives here only in Percival's English summary". The sentence says "survives … only" twice, about two different things.
- **Fix.** "… read out in Session VI to be answered. We draw on Percival's English summary of it, drawn mostly from Hefele."

### R2-PHO-1. Minor (items 1, 9; PHO-1 sister fields). councils-of-constantinople-861-880

- **`decided[0]` (l.44).** It is still headed "861 (no acts)" while it gives the seventeen canons, which the pattern counts as acts. Fix: "861 (canons only)".
- **`issue[1]`.** "The Pedalion says they were in the city against the iconoclasts" drops "sent" ("ἀποσταλέντες κατὰ τῶν εἰκονομάχων", l.33227). Fix: "the Pedalion says they had been sent against the iconoclasts".

### R2-PHO-2. Minor (C1; records). councils-of-constantinople-861-880

- **records.json l.1064-1066.** The new claim mixes two witnesses under kind "acts": the canons, and the Pedalion editors' statements of 1800 ("its minutes are not found; it said nothing against Photius"). The entry's `record` rightly calls the Pedalion "modern reconstruction". Fix: split it into "The seventeen canons of 861 (l.33300, 33330 ff.)" with kind acts, and the editors' statements (l.33222-33228, 33335-33345) with kind modern reconstruction.
- **records.json l.1079.** The contested claim on the count still has "Binius: 318, 'as they boasted'". This is the English rendering in quotation marks that PHO-11 removed from the entry. Fix: "Binius: 318, 'ut ipsi jactabant', as they boasted".

### R2-GEN-1. Minor (CLAUDE.md, "Track gaps"; R1 tracking). All

`R1_changes.md` says two items were logged in Open-Gaps:
- the missing witness kind for a writer earlier than the meeting (WHI-1, Columbanus);
- Ignatius's verdict, left to the coordinator (PHO-9).

`Open-Gaps.md` was not changed in commit 8c7b3261, and neither item is in it. Fix: add both as a numbered Open-Gaps entry, citing this round by subject and date, before the era is approved to proceed.

### R2-GEN-2. Minor (register; the TOL-4 rule applied to four entries but not these two). synod-of-whitby-664, quinisext-council-692

Round 1 removed the project word "held" from the participant-facing fields of Lateran, Constantinople 680, Nicaea and the Photian councils. It still stands, unchanged, in the other two entries:
- Whitby `datesNote` (l.25), "No held source gives a month or day"; `attended[2]` (l.38), "no list of names is held"; `decided` (l.42), "No acts or canons are held"; `uncertain` (l.201), "no held source gives a month".
- Quinisext `datesNote` (l.30), "No held source gives a month"; `attended[0]` (l.39), "The signatures are held in Mansi"; the Percival `record` note (l.120), "Hefele's own volume for this council is not held".

Fix: "survives", "our sources", "in the books we draw on", as in the other four entries. For example: "The signatures are printed in Mansi"; "no list of names survives"; "Hefele's own volume for this council is not among our sources".

## Checks that passed on the new wording

- **Quotations.** No new quotation in any brief. New entry quotations are verbatim: "ut ipsi jactabant" (M15 l.63849), Columbanus's Latin and the Serpos summary, which is given without marks.
- **Rendering.** No English rendering of Latin, Greek or Italian is set in quotation marks in a brief or entry. The one left is in records (R2-PHO-2).
- **Contested and editors' views.** Nothing contested is told as settled in the new brief text, and every editor's view is credited: Percival on the signatures, Percival on the emperors after Irene, the Life of Methodius on 843, and Theophanes on the tortures.
- **No AI tells in the new brief wording.**
  - No "not X but Y", colon-reveal, rhetorical question, tail line or hedge filler.
  - The PHO-7 colon-reveal is gone.
  - Whitby's question-shaped sentence is now reported speech: "Asked if he could show such power given to Columba, the founder of Iona, he answered, "None.""
  - The longest new sentences are 25 words.
  - New terms are defined at first use: "anathematized, or cursed"; "Iconoclast, or image-breaking"; "the Pedalion, a Greek book of church law of 1800".
- **Pronouns.** The Nicaea close's "its acts" points to "The council" in the sentence before. The Photian "his envoys" is Nicholas's. The one ambiguous pronoun is R2-CP3-1.
- **Item 8.** "Wilfrid of Ripon" at first mention in the brief and teaser; "Nicetas the Paphlagonian"; "Paul of Constantinople (bishop in 692)"; "Alfrid, son of Oswy".
- **C7.** New people lines carry the right verdicts: Theodore of Pharan and Peter LISTED (scan l.160); Mark of Ephesus WHO (era 6 l.119); Theophanes and Theodore the Studite WHO (rescore); Tarasius LISTED (l.153). Theodore the Studite's "later doubted, then accepted, the council's standing" rests on NPNF l.41526-41537, his letter of 826 with Neale's "afterwards changed his opinion".
- **Item 13.** The tags are only in the audio scripts, at the start and before the last paragraph.

## Counts

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| lateran-council-649 | 0 | 0 | 1 |
| third-council-of-constantinople-680 | 0 | 1 | 0 |
| synod-of-whitby-664 | 0 | 0 | 1 (+ GEN-2) |
| quinisext-council-692 | 0 | 0 | 2 (+ GEN-2) |
| second-council-of-nicaea-787 | 0 | 1 | 1 |
| councils-of-constantinople-861-880 | 0 | 0 | 2 |
| All (GEN-1, GEN-2) | 0 | 0 | 2 |
| **Total** | **0** | **2** | **9** |

Round 1 substantial findings: 5 of 6 CLOSED; CP3-1 OPEN in part, carried as R2-CP3-1. Both R2 substantial findings have exact fixes within the cap. Per the review-cycle cap, the third round should be a targeted recheck of R2-CP3-1 and R2-NIC-1 and of whichever minor fixes are taken.
