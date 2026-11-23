# Card check: Rufinus of Aquileia (`rufinus-of-aquileia`)

Checked: `rufinus-of-aquileia.card.json` against `Card.existing.json`, `Card_Edits.md`, the brief, `Outline.md` and `Source_Sheet.md`, with every cited quotation line re-read in its Library file.

## Verdict: FIX

## What holds

1. **Edits justified.** Edit 1 (`legacy.traces[0]`, "only" to "chiefly"): Fremantle says we owe "our knowledge of many of the works of Origen" to his translations (N203 44027-44030). He does not say "only". ANF4 22122-22124 says "chiefly" and 21996-22002 names Greek fragments. The brief says "survive chiefly". The fix is justified and minimal. New traces 5-8 stand at their lines: N203 42467-42470; MOM 27383-27385 with N202 4372-4374; N202 5666-5668; ANF4 22126-22128. New `uncertain` 9 and 10 stand at N203 45702-45706, 45775-45780, 51287-51303, 45693-45694, 44220-44223 and 44550-44555, and at ANF4 21996-22002. New `sources` entries are correct.
2. **Nothing else moved.** `otherNames`, `knownFor`, `datesNote`, `placeNote`, `role`, `keyWorks`, `legacy.remembered`, `legacy.traces[1-3]`, `uncertain[0-7]` and the existing `sources` entries are word for word and in order.
3. **Census rules.** The keys are allowed, with no `briefLength`. There are three quoted spans in the brief and three entries. None is under six words, so none has `secondReading` and none is "checked at card". Each `printed` is verbatim: N206 3941-3942; N203 45775-45780; N203 51325-51331. Quote 3's Latin is verbatim at PL23 31112-31115. Its scan misprints the Greek title, which reads ᾿Αρλῶν for ᾽Αρχῶν (checked by hand). The note says so, and Fremantle's English confirms the reading. The outline renders Quote 3 from the Latin, and the card carries that Latin. Quotes 1 and 2 have no held original. Every cited file is in `sources`. No audit file, review or ruling is named, and there are no quotation marks in `briefReferences`. Run on a scratch copy of the census, the validator reports only the release-time errors: `secondReading` is unset, and the renderings are not yet in `tools/quote_renderings.json`.
4. **Not found.** No claim is listed as not found, and none turned up. No clearly wrong statement is left in.

## FIX: `briefReferences` parts the brief does not tell (check 3)

`Card_Edits.md` put the outline's cut items into `briefReferences` ("Not carried" list). The brief does not tell them, so they come out. Those that belong elsewhere are already there: the priesthood is in `role`, the Pamphilus point is in `uncertain`, and Jerome's version is in `legacy.traces`.

**FIX 1.** `briefReferences[0]` (outline Cut first 15: the brief keeps only the second sentence).
- Old: `The brief quotes the last line on friendship. The line before it says a friend is long sought, hardly found, and with difficulty kept.`
- New: `The brief quotes the last line on friendship.`

**FIX 2.** `briefReferences[1]`. The brief tells no year for the circle or the departure, and does not judge the preface.
- Old: `part of a society of young ascetics at Aquileia in the years 370 to 373; estranged over Origen in Palestine and reconciled before Rufinus left in 397; the preface to On First Principles meant to show Jerome as his forerunner, and the use made of that example hardly justifiable;`
- New: `part of a society of young ascetics at Aquileia; estranged over Origen in Palestine and reconciled before Rufinus left; the preface to On First Principles meant to show Jerome as his forerunner;`

**FIX 3.** `briefReferences[2]` (Cut first 6: the three clergy and the teacher of the creed).
- Old: `living in a monastery, baptized about thirty years before at the hands of Chromatius, Jovinus and Eusebius, all now bishops, and taught the creed by the third.`
- New: `living in a monastery, baptized about thirty years before.`

**FIX 4.** `briefReferences[3]` (Cut first 8: Didymus. The brief names no desert monk).
- Old: `two more, where Didymus lived and among the desert monks Macarius, Isidore and Pambas.`
- New: `two more, among the desert monks.`

**FIX 5.** `briefReferences[5]` (Cut first 4 and 5: the visitors and the priesthood. The brief does not mention Palladius, the fifty virgins or the twenty-seven years). "Returned to Jerusalem" is also not in PAL 501, which says "she founded a monastery in Jerusalem".
- Old: `Palladius, Lausiac History 46: after Melania returned to Jerusalem she founded a monastery and was in charge of a convent of fifty virgins for twenty-seven years, with Rufinus living beside her, later made a priest; they received visitors at their own charges. W. K. Lowther Clarke's note: Palladius takes Rufinus's part in the quarrel with Jerome.`
- New: `Palladius, Lausiac History 46: Melania founded a monastery in Jerusalem and was in charge of a convent, with Rufinus living beside her.`

**FIX 6.** `briefReferences[9]`. The brief does not tell Fremantle's view, which stays in `uncertain[5]`.
- Old: ` Fremantle finds no reason to suppose the bishop passed sentence on him.`
- New: (removed; the entry ends at `neither knows nor wishes to know.`)

**FIX 7.** `briefReferences[10]` (Cut first 2: the span of the added books).
- Old: `and the two books added, running from Constantine to the death of Theodosius.`
- New: `and the two books added.`

**FIX 8.** `briefReferences[13]` (Cut first 11: this stays in `legacy.traces[7]`).
- Old: `; the few Greek fragments show him altering many of Origen's expressions; Jerome's new translation survives only in small portions.`
- New: `; the few Greek fragments show him altering many of Origen's expressions.`

## Second pass check (2026-11-23)

Compared: the card at `db30b801` (before the second pass) with the card now, field by field.

### Verdict: FIX

1. **Checker changes.** FIX 1 to FIX 8 went in word for word. Nothing else in `briefReferences[0]`, `[1]`, `[2]`, `[3]`, `[5]`, `[9]`, `[10]` or `[13]` moved, and no other `briefReferences` entry changed. The only other changes are the three appended `legacy.traces` (8-10) and seven appended `uncertain` entries (10-16). Every other field is word for word and in order.
2. **Items added.** Each was re-read at its lines. Trace 8 (Gennadius, N203 42484-42487), trace 9 (Fremantle, N203 44396-44398) and trace 10 (Palladius, Lausiac History line 501, [6]) hold, each with its witness. `uncertain[10]` (N203 46563-46575), `[11]` (N203 49434-49439, 44084-44088), `[12]` (N203 58776-58787), `[13]` (N203 46070-46071), `[14]` (N203 46149-46150, 44423-44425) and `[15]` (N203 45741-45745, 44208-44211) hold. `uncertain[16]` says more than its source (below).
3. **Outline "to the card" items.** All are on the card: Epiphanius (`legacy.remembered`); the Recognitions and Xystus (trace 1); the Benedictions (trace 8); the History of the Monks (trace 9); birth year and Concordia (`datesNote`, `uncertain[1]`, `[2]`); Cut first 1 (trace 5); 2 (`keyWorks`, `uncertain[12]`); 3 (`uncertain[12]`); 4 (trace 10, and the praise in `legacy.remembered`); 5 (`role`, `knownFor`); 6 (`uncertain[10]`); 8 (`uncertain[11]`); 10 (`uncertain[4]`); 11 (trace 7); 12 (`uncertain[13]`); 13 (trace 4); 14 (trace 6); 16 (`legacy.remembered`); 17 (`uncertain[14]`); 18 (`uncertain[15]`); 19 (`uncertain[16]`). The two skips hold. "Grunnius" is marked only "if wanted", and no held text carries it. Quote 1's first sentence is a printed line that the brief no longer quotes, so it cannot go in `quotationOriginals`, and no other field takes it.
4. **Scan readings.** None were listed, and the first check gave none.
5. **Census rules.** The keys are unchanged and allowed. The new text uses American spelling, and no audit, review or ruling is named. Each new cited file is in `sources`.

**FIX 1.** `uncertain[16]`. Fremantle does not say the party left from Rome. At N203 44434-44439 he says Melania "was either there or with Paulinus at Nola", and that "the whole party were starting by way of Sicily and Africa".
- Old: `Fremantle says the party was leaving Rome by way of Sicily and Africa and that Rufinus joined their religious company.`
- New: `Fremantle says the party was starting out by way of Sicily and Africa and that Rufinus joined their religious company.`


Coordinator (2026-11-23): the second pass check's fix applied word for word.
