# Council profiles, era 4: review round 3, targeted recheck (2026-11-15)

## Scope and method

- **Scope.** This is the last round under the review-cycle cap. It covers only what changed after round 2: every string in `git diff HEAD~1` (commit 323f916e) under `Build/Ministry/Features/Church-Family-Tree/`. That means two briefs, two audio scripts, six entries, `records.json` and Open-Gaps 266. It was read against `R2_recheck.md` and `R2_changes.md`. Unchanged text was not re-reviewed, except where a round 2 fix left the same fault standing in a sister field.
- **Reviewer.** Independent Opus. Not the drafter and not a round 1 or round 2 reviewer. No file was edited except this report.
- **Standard.** `Council_Profile_Pattern.md`; `Who_Profile_Pattern.md` items 1-9, 11 and 13; CLAUDE.md "Trust and source fidelity" and "Accessible and rigorous".
- **Sources opened at the cited lines, tolerant of OCR and long s.**
  - Mansi 10: session III opens l.96690 ff.; the Ekthesis is produced at l.100080-100110, before Secretarius IV at l.101575; the Typos is at l.103680-103687; the acts begin at l.88609.
  - Mansi 15 l.63849; Mansi 17-18 l.52593 (Actio sexta) and l.53308-53309 (the seventh session, 13 March).
  - Duchesne's Liber Pontificalis t.1 l.170975-170990 (Sergius) and l.174288-174291, 174583-174586 (John VII).
  - PG 108 l.1700-1716 and l.1816 (the Life of Theophanes).
  - The Pedalion l.33218-33232, 33296-33346 and 33384-33396.
  - Ormanian l.9782; PL 80 header; Mansi 11 header; PG 99 l.4346-4348; William of Tyre v2 l.26911-26918.
  - Bede: Plummer l.24130-24170; Giles l.10282-10288.
  - NPNF 14 l.38098-38104.
- **Audits and data for Open-Gaps 266.** I spot-checked `Who_Scan_Era4.md` l.114, 153, 201 and 224, and `Councils_Scan.md` l.62-67, 226 and 251-253. In `cic-website/data/world-census.json` I counted by script the places that name the Quinisext and Nicaea II, and read the `byzantine-imperial-church-heraclian-iconoclast` and `gregory-of-nyssa` texts. I also checked `Who-Profiles/era4/batch2/records.json` l.1396-1397 and `Decision-Log.md`.
- **Readability and audio.**
  - All six briefs were scored with `engine.m1.gates.grade_text`, and their sentences were split by script.
  - Each audio script was compared by script with its brief, plus `[calmly] ` at the start and `[warmly] ` before the last paragraph. All six match exactly, with two tags each.
  - The R3-CP3-1 replacement was applied to a scratch copy and rescored: `/tmp/claude-0/-home-user-CIC-Project/3fc04891-4b0e-5b02-a097-fe39a900e3e5/scratchpad/R3/cp3.fixed.txt` (398 words, FK 7.66, FRE 66.88).
- No model calls, no network, no paid services.

## Per-council tables

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| lateran-council-649 | 398 | 7.44 | 67.64 | yes | CLEAR |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| third-council-of-constantinople-680 | 398 | 7.66 | 66.88 | yes | CLEAR WITH MINORS |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| synod-of-whitby-664 | 398 | 6.26 | 75.45 | yes | CLEAR |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| quinisext-council-692 | 400 | 7.79 | 62.23 | yes | CLEAR WITH MINORS |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| second-council-of-nicaea-787 | 401 | 7.88 | 61.06 | yes | CLEAR WITH MINORS |

| Council | Words | FK | FRE | Audio ok | Verdict |
|---|---|---|---|---|---|
| councils-of-constantinople-861-880 | 402 | 7.95 | 62.20 | yes | CLEAR WITH MINORS |

- The two changed briefs match `R2_changes.md`: Constantinople 680 has 398 words, FK 7.66 and FRE 66.88; the Quinisext has 400 words, FK 7.79 and FRE 62.23.
- Their longest sentences are 25 and 22 words.
- All six briefs pass FK 10 or below and FRE 60 or above, at the cap.
- The Whitby FK below 8 was accepted in round 2 and is unchanged.

## Round 2 findings

- **R2-CP3-1: CLOSED.**
  - Brief: "The condemned reach us mostly through their opponents' records. Michael the Syrian … sides with one will against the council." "Mostly" is now true. Michael has Macarius show "que c'est une hérésie d'admettre deux volontés" (MICH l.34505-34510), so his record is friendly to the condemned. The pronoun "tells it" is gone.
  - Entry `uncertain[0]` now has "takes Macarius's side and reports his argument, but not his words". `records.json` l.544 has "who takes Macarius's side". Both are right.
  - The new brief wording has a minor clarity fault (R3-CP3-1).
- **R2-NIC-1: CLOSED.**
  - The false absence is gone. The Life printed in PG 108 says he was called to the council and set out: "ad eam ipse quoque cum aliis Patribus vocatus est … ipse solito cilicino sacco indutus, asinae insidens, laetus iter suscepit. Sed cum omnes viderent eum" (l.1705-1711). "Came" rests on "cum omnes viderent eum".
  - The line credits the Life, so a hagiographer's report is not told as settled.
  - The new line has a minor wording fault (R3-NIC-1).
- **R2-LAT-1: CLOSED.**
  - `issue[3]`: "the Typos, an edict that would destroy the catholic teaching". Martin: "typum exponere, qui catholicum dogma destrueret" (M10 l.89929-89931).
  - The optional part is done too. "Quoted in" replaces "read into" in `record[0]` and `uncertain[0]`.
  - The new `issue[0]` "read out in session III" is right. The Ekthesis is produced and ordered read at l.100080-100110, inside the session dated "sub die decimo sexto Calendas Novembris" (l.96690 ff.) and before "SECRETARIUS IV" (l.101575).
- **R2-WHI-1: CLOSED.** `uncertain[0]` now begins "No acts of the synod survive."
- **R2-QUI-1: CLOSED.** The brief has "Malachia Ormanian, a modern Armenian patriarch, dates it to 726". Ormanian has "of Manazkert in 726" (l.9782).
- **R2-QUI-2: CLOSED, with a sister-field remnant (R3-QUI-1).**
  - John VII: "the emperor sent him the volumes again, and he returned them uncorrected". This matches LP t.1 l.174288-174291 and l.174585-174586 ("hos nequaquam … emendans … direxit ad principem").
  - Anastasius of Jerusalem: "Signed; not named among the patriarchs by the Book of the Popes".
  - John of Porto, "carried off … by the emperor's order, in contempt of the pope", and Boniface, "carried off … with John of Porto". Both match "Sergium magistrianum in spretum praenominati pontificis Romam mittens, Iohannem … Portuensem episcopum seu Bonifatium consiliarium apostolicae sedis … in regiam abstulit urbem" (l.170982-170984).
- **R2-NIC-2: CLOSED.** The double "survives … only" is gone. The new sentence repeats a word (R3-NIC-2).
- **R2-PHO-1: CLOSED.** The heading is now "861 (canons only)". The entry now has "the Pedalion says they had been sent against the iconoclasts", which matches "ἀποσταλέντες κατὰ τῶν εἰκονομάχων" (l.33227).
- **R2-PHO-2: CLOSED, with two citation faults in the new records (R3-PHO-1, R3-PHO-2).**
  - The split is right: the canons are filed as acts, and the editors' statements as modern reconstruction.
  - Binius now reads "'ut ipsi jactabant', as they boasted", which matches "ut ipfi ja@abant" (M15 l.63849). The gloss is outside the marks.
- **R2-GEN-1: CLOSED.** Open-Gaps 266 holds the Ignatius verdict question and the witness-kind gap, among the other items. Three minor corrections to it are below (R3-GEN-1 to R3-GEN-3).
- **R2-GEN-2: CLOSED.**
  - A word-bounded search of all six entries and briefs finds "held" only in its ordinary sense, as in "a synod should be held" or "they still held that".
  - "The Library, codex 20" is the title of Photius's own work.

## Open-Gaps 266: spot-check

These statements were checked against the files they name and are right:
- **Lateran acts.** The acts begin at Mansi 10 l.88609 ("CONCILIUM LATERANENSE ROMANUM"). `Councils_Scan.md` l.226 has "~96715".
- **Whitby overstatement.** `Councils_Scan.md` l.63 has "The English, Irish and Welsh churches were brought onto the Roman Easter".
- **Mansi 15-17.** `Councils_Scan.md` l.67 and l.251-253 call them not held. The files are vendored: `…tomus-15-…`, `…tomus-16-…` and `…tomus-17-18-…`.
- **Quinisext in the census.** By script, the census names it in four places: edge 91, `gregory-of-nyssa`, `council-of-sardica-343`, and `byzantine-imperial-church-heraclian-iconoclast` ("the canons issued at Constantinople in 692"). The scan says two.
- **Nicaea II in the census.** Six edges name it (5, 234, 236, 237, 238, 239) and seven entries (melkite, iconophile, heraclian-iconoclast, basil, gregory-of-nyssa, john-moschus, sophronius). The scan says "about 20".
- **Theophanes.** `Who_Scan_Era4.md` l.114 has "WANTED … Not held". The Chronographia file is vendored.
- **Hatfield.** `Who_Scan_Era4.md` l.201 has "17 Oct 680". Giles l.10286 has "seventeenth of October". Bede's Latin reads "sub die XV Kalendas Octobres", which is 17 September. The cited line is wrong (R3-GEN-1).
- **Tarasios.** The Tarasios row's l.38101 is Percival's "(Labbe, Conc., Tom. VII., col. 165)", not the letter.
- **Ignatius.** The row at `Who_Scan_Era4.md` l.224 is quoted rightly.
- **Typos.** It forbids argument over one will or two: "non habere licentiam … de una voluntate aut una operatione, aut duarum voluntatum, aut duarum operationum qualemcumque proferre altercationem" (M10 l.103676-103689). The census text says Constans II "imposed" the doctrine of one will (it sits in the Maximus story).
- **Gregory of Nyssa.** The census has "Father of Fathers"; no match was found in NPNF 14.
- **Sixth and seventh sessions.** The Photius batch 2 records label Mansi 17 l.53399-53432 the "sixth session". The Actio sexta heading is at l.52593, and the next session opens at l.53308-53309 ("Mense Martio, die XIII … die Dominica"). So l.53399 lies in the seventh session.
- **William of Tyre.** The text is vendored, and the Maronite passage is at l.26911 ff.
- **Library headers.**
  - The PL 80 header does not mention Columbanus.
  - The Mansi 11 content note ends "The volume ends with the life of Pope Conon".
  - PG 99 l.4346-4348 has "Beda … qui synodum erraticam" in the prefatory matter.

## New findings

### R3-CP3-1. Minor (CLAUDE.md, terms introduced before use; Who pattern item 6, heard aloud). third-council-of-constantinople-680

- **Exact text.** Brief l.3: "Michael the Syrian, a Syriac Orthodox patriarch of the 1100s, sides with one will against the council."
- **Evidence.**
  - "One will" is the dispute's term, but the brief first explains it in the next paragraph: "bishops of Constantinople had taught one will in Christ". A listener who hears "sides with one will" here has not yet been told that the quarrel is over wills in Christ.
  - The sentence also no longer says that Michael writes. Its link to the sentence before it, which names him as the exception to "their opponents' records", is left to inference.
  - The facts are right, so this is not substantial.
- **Replacement.** "Michael the Syrian, a Syriac Orthodox patriarch of the 1100s, writes from the side of the condemned." This keeps the same 17 words. The brief stays at 398 words, FK 7.66, FRE 66.88 (scratch copy). The audio script takes the same change.

### R3-NIC-1. Minor (item 9, wording). second-council-of-nicaea-787

- **Exact text.** Entry `people`, Theophanes the Confessor (l.181): "Called to the council and came, in a hair shirt and riding a donkey, by the Life printed with his Chronicle; chronicler of the broken meeting of the year before and of the council".
- **Evidence.** "Riding a donkey, by the Life" reads at first as a route or a means. The credit to the witness comes last and is easy to misparse.
- **Replacement.** "The Life printed with his Chronicle says he was called to the council and came in a hair shirt, riding a donkey; chronicler of the broken meeting of the year before and of the council".

### R3-NIC-2. Minor (register; repetition). second-council-of-nicaea-787

- **Exact text.** Entry `issue[0]` (l.31): "We draw on Percival's English summary of it, drawn mostly from Hefele."
- **Replacement.** "We draw on Percival's English summary of it, which mostly follows Hefele."

### R3-QUI-1. Minor (sister field of R2-QUI-2). quinisext-council-692

- **Exact text.** Entry `outcome[2]` (l.56): "Later popes, as the Book of the Popes tells it: John VII, sent the volumes again, returned them uncorrected, \"humana fragilitate timidus\", fearful in human weakness; …"
- **Evidence.** The people line was corrected so that the emperor sends the volumes (LP t.1 l.174288-174291). This line still reads most naturally as John VII sending them.
- **Replacement.** "Later popes, as the Book of the Popes tells it: the emperor sent John VII the volumes again, and he returned them uncorrected, \"humana fragilitate timidus\", fearful in human weakness; …" The rest of the line is unchanged.

### R3-PHO-1. Minor (citation). councils-of-constantinople-861-880

- **Exact text.** `records.json` l.1071, `"witness": "nikodemos-hagiorite_pedalion-canons-grc_1886.txt l.33300, 33330 ff."`. The same "l.33300, 33330 ff." appears in the note at l.1127.
- **Evidence.** Line 33330 is inside the editors' footnotes, which begin "(1) Ἐν τῇ α'. δὲ συνελεύσε. αὐτῖς καθαιρεῖται μὲν ὁ Ἰ.νά-" (l.33314, OCR) and run to l.33346. The canons begin under "ΟΙ ΙΖ. ΚΑΝΟΝΕΣ ΤΗΣ ΕΝ ΤΩ ΝΑΩ ΤΩΝ ΑΓΙΩΝ ΑΠΟΣΤΟΛΩΝ ΣΥΣΤΑΣΗΣ ΣΥΝΟΔΟΥ" at l.33392. The error was carried from round 2's own suggested wording, and before that from R1.
- **Replacement.** In both places: "l.33300, 33392 ff."

### R3-PHO-2. Minor (records wording and citation). councils-of-constantinople-861-880

- **Exact text.** `records.json` l.1076-1077: "The Pedalion's editors: the synod of 861 met in 861, issued its canons at its second meeting, its minutes are not found, and it said nothing against Photius", witness "l.33222-33228, 33335-33345".
- **Evidence.**
  - "The synod of 861 met in 861" says the same thing twice.
  - The statement about the second meeting is at l.33296-33300 ("Ἐν δὲ τῇ Β΄. αὐτῆς συνελεύσει ἐξεδόθησαν καὶ οἱ παρόντες ιζ'. κανόνες"), which the witness does not cite.
- **Replacement.**
  - Claim: "The Pedalion's editors: the synod in the Holy Apostles met in 861 and issued its canons at its second meeting; its minutes are not found; it said nothing against Photius".
  - Witness: "nikodemos-hagiorite_pedalion-canons-grc_1886.txt l.33222-33228, 33296-33300, 33335-33345".

### R3-GEN-1. Minor (Open-Gaps 266, citation)

- **Exact text.** "where Bede's Latin gives 17 September (Plummer l.24152-24154)".
- **Evidence.** Lines 24148-24156 hold variant footnotes and a running head. The date is at l.24162-24163 ("suh clic XV Kahndas Octohres", OCR for "sub die XV Kalendas Octobres"). The margin "Sept. 17" is at l.24135.
- **Replacement.** "(Plummer l.24162-24163, 'sub die XV Kalendas Octobres')".

### R3-GEN-2. Minor (Open-Gaps 266, a scan correction left out)

- **Evidence.** The Who scan's own Photian council row says "Not held: Mansi 16 and 17 are not in the Library (file list checked)" (`Who_Scan_Era4.md` l.224). Both volumes are vendored. Entry 266 corrects this for the Councils scan only.
- **Replacement.** Add to the "Who scan, era 4" list: "the Photian council row (l.224) says Mansi 16 and 17 are not in the Library; both are held (`mansi_…tomus-16-…`, `mansi_…tomus-17-18-…`)."

### R3-GEN-3. Minor (Open-Gaps 266, a cross-reference to an entry not yet written)

- **Evidence.** Entry 266 cites "Decision-Log, 'Major councils, era 4' (2026-11-14)". `Decision-Log.md` has entries for eras 1 and 2 (l.2620) and era 3 (l.2710), but none for era 4. The entry's "approved to proceed" was also written while round 2 still had two councils NOT CLEAR.
- **Fix.** Write the Decision-Log entry, citing this round's result, in the same commit that applies these minors. Use era 3's entry as the model. If the date of the entry differs, make the Open-Gaps reference match it.

## Checks that passed on the new wording

- **Quotations.** No new quotation appears in either brief. The new entry Latin ("ut ipsi jactabant") and the Greek cited for the Pedalion are verbatim, allowing for OCR.
- **Renderings.** No English rendering of a foreign source sits inside quotation marks in a changed string.
- **Contested or editors' views.** The Life of Theophanes is credited by name, and so are the Pedalion's editors and Ormanian's modern date. Nothing contested is told as settled.
- **Absences and "only".** "No source we draw on gives a month", "no list of names survives" and "No acts or canons survive" are true of the vendored witnesses. No new false "only" appears.
- **AI tells.**
  - The changed brief strings have no "not X but Y", "X, not Y", colon-reveal, tail line or hedge.
  - The changed brief sentences have 17 and 12 words.
  - The one pronoun fault from round 2 is gone.
- **Project vocabulary.** "Held" and "the Library" no longer appear as project words in any participant-facing field (R2-GEN-2 above).
- **Item 13.** The tags appear only in the audio scripts, at the start and before the last paragraph.

## Counts

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| lateran-council-649 | 0 | 0 | 0 |
| third-council-of-constantinople-680 | 0 | 0 | 1 |
| synod-of-whitby-664 | 0 | 0 | 0 |
| quinisext-council-692 | 0 | 0 | 1 |
| second-council-of-nicaea-787 | 0 | 0 | 2 |
| councils-of-constantinople-861-880 | 0 | 0 | 2 |
| Open-Gaps 266 (GEN) | 0 | 0 | 3 |
| **Total** | **0** | **0** | **9** |

- **Round 2 findings.** All 11 are CLOSED: 2 substantial and 9 minor.
- **Verdicts.** No blocking or substantial finding remains. Lateran 649 and Whitby 664 are CLEAR. The other four are CLEAR WITH MINORS.
- **Applying the minors.** Each minor has exact replacement wording. They can be applied as worded, with no further review round. Only R3-CP3-1 touches a brief, and it leaves the word count and scores unchanged. R3-GEN-3 should be done before the era is recorded as approved to proceed.
