# Priscillian: card check, the modern pass

Check pass of `roles/card.md` on `priscillian.card.json`. Starting card: `Card.pass3.json`. Edit list: `Card_Edits.md`, **Fourth pass: no modern opinion (2026-11-23)**. Brief: `priscillian.brief.txt` as it now stands. The checker did not write the card.

## Verdict: FIX

## What holds

- **Nothing else moved.** A `diff` of the two cards shows only the listed changes: `uncertain[4]` and `uncertain[8]` (indexes count from 0 throughout), and `briefReferences` edits 3 to 9.
- **Quotations.** The brief quotes the same three spans in the same words, and `quotationOriginals` is unchanged.
- **Cited lines.** All re-read and all hold: Pr 80-93 (preface), 4334, 4347, 4363-4392, 4415-4417, 4636-4638, 4655-4656, 4672-4677; SulpE 11490-11508, 11528-11532, 11544-11548; Pros 53277-53287 (Arcadius and Bauto, margin 385); Hyd 1143-1145 (VIIII, margin 387) and 1916-1918 (margin 447); Mansi3 96555 (Era 438) and 96780-96781.
- **Reference edits.** Edits 3 to 9 are justified. The Hefele entry is rightly removed, and the file stays in `sources.about` because `uncertain` still uses it. The new Prosper and Hydatius entry quotes "sixty years on" verbatim from the brief.
- **Titles.** The Tractate II title, *Liber ad Damasum episcopum*, is the manuscript's own heading (Pr 4318, 4326), so the title is fine. The Canons are named Priscillian's in the manuscripts' *Prologus Priscilliani* and in Peregrinus's revision (Pr 1704, 7822), which is an old attribution, so that entry stands.
- **Card rules.** No audit file is named, and spelling is American outside printed wording.

## What fails

The edit list's "Not changed, listed" note keeps Schepss's attribution "word for word as outside this pass". That does not hold. The role corrects any statement that contradicts the finished brief. The brief now says "Priscillian's party carried a book", "The book says" and "the book says", and gives the treatises no author. So each line below that states the book or the treatises as Priscillian's own, uncredited, contradicts the brief. One small correction to the note: the `keyWorks` entries say "his appeal" and "his defense", not "Priscillian, in his book to Damasus". That wording is in `uncertain[1]` and `uncertain[2]`.

In each fix, the attribution either goes, with the line saying "the book", or stays credited by name to Georg Schepss as a modern judgment. The full statement already stands in `uncertain[4]` (the Würzburg item).

The check also found the following:
- Two lines are clearly wrong in other ways: a `briefReferences` phrase that reverses the brief, and a sentence about "the story" that the brief no longer tells.
- One sentence the pass added says more than its source.
- Several modern views are credited by name but not marked as modern.

## Changes, exact

### A. Schepss's attribution, uncredited, against the brief

**A1. `datesNote`**
- Old: `Sulpicius Severus says he was condemned at Saragossa, which he denied; put to death at Trèves under Maximus; Ernest Cushing Richardson dates him flourished 379, died 385`
- New: `Sulpicius Severus says he was condemned at Saragossa, which the book to Damasus denies; put to death at Trèves under Maximus; Jerome's modern translator Ernest Cushing Richardson dates him flourished 379, died 385`
- Evidence: brief paragraph 5, "The book says no charge was laid against his group there"; Pr 4382-4392. The second change belongs to section B.

**A2. `keyWorks[0].about` (Tractate I)**
- Old: `his defense of his faith, cursing the Patripassians, the Manichaeans and other heresies`
- New: `a defense of the faith, cursing the Patripassians, the Manichaeans and other heresies; unsigned, and judged Priscillian's by Georg Schepss, its modern editor`
- Evidence: Pr 85-93. The manuscript carries no author's name, and the attribution is Schepss's.

**A3. `keyWorks[1].about` (Tractate II)**
- Old: `his appeal to Damasus of Rome, saying that at Saragossa none of his group was accused, convicted or condemned`
- New: `his party's appeal to Damasus of Rome, saying that at Saragossa none of his group was accused, convicted or condemned; Georg Schepss, its modern editor, judged it Priscillian's own`
- Evidence: brief paragraph 1, "Priscillian's party carried a book"; Pr 4384-4386 ("qui libellum tradidimus", "nemo e nostris"); Pr 85-93.

**A4. `uncertain[1]`**
- Old: `Priscillian, in his book to Damasus, says no one of his group was accused, convicted or condemned there.`
- New: `The book to Damasus says no one of his group was accused, convicted or condemned there.`
- Evidence: brief paragraph 5; Pr 4386-4389.

**A5. `uncertain[2]`, first and second sentences**
- Old: `Priscillian, in his book to Damasus, says Hydatius gave the council some memorandum that set down, as it were, a rule for living, and that none of his group was censured under it. He does not say what it forbade.`
- New: `The book to Damasus says Hydatius gave the council some memorandum that set down, as it were, a rule for living, and that none of his group was censured under it. The book does not say what it forbade.`
- Evidence: Pr 4390-4392.

**A6. `uncertain[14]` (the Sulpicius-traces item), two clauses**
- Old: `Priscillian's own book denies the heresies and curses them.`
- New: `The book to Damasus denies the heresies and curses them.`
- Old: `Priscillian says Ydacius had won his rescript by a false petition that hid their names.`
- New: `The book to Damasus says Ydacius had won his rescript by a false petition that hid their names.`
- Evidence: brief paragraphs 4 and 6; Pr 4636-4638 ("dissimulatis nominibus nostris rescribtum ... petit").

**A7. `uncertain[15]` (Liber apologeticus), last sentence**
- Old: `Schepss's attribution of the tractates to Priscillian is the only one held.`
- New: `Schepss's modern attribution of the tractates to Priscillian is the only one held.`

**A8. `briefReferences[0]`, opening words**
- Old: `Priscillian's book to Damasus (Tractate II), ed. Georg Schepss:`
- New: `The book to Damasus (Tractate II), ed. Georg Schepss:`
- Evidence: the entry's own bracket "(a book of Priscillian's party, not shown to be his own)" and brief paragraph 1. The possessive contradicts both.

**A9. `sources.ownWords[0].title`**
- Old: `Tractates I to XI, the Canons on Paul and the fragment kept by Orosius, edited by Georg Schepss`
- New: `Tractates I to XI, unsigned and judged Priscillian's by Georg Schepss, their modern editor; the Canons on Paul; and the fragment kept by Orosius, edited by Schepss`
- Evidence: Pr 85-93. The title sits under "own words", so without the credit it states Schepss's judgment as fact.

### B. Modern views named but not marked as modern

**B1. `uncertain[2]`, third sentence**
- Old: `Karl Josef von Hefele, in Oxenham's English, supposes`
- New: `Karl Josef von Hefele, a modern historian, in Oxenham's English, supposes`

**B2. `uncertain[8]` (the year item)**
- Old: `The year of his death is not fixed. Richardson's note to Jerome gives 385.`
- New: `The year of his death is not fixed. Of the modern editors, Richardson's note to Jerome gives 385.`
- Old: `the Roman year in each is an editor's margin.`
- New: `the Roman year in each is a margin by their modern editor, Theodor Mommsen.`
- Evidence: both chronicles are in Mommsen's editions (`sources.about`); Pros 53277 and Hyd 1143 carry the years as margins.

**B3. `uncertain[9]` (the first-execution item)**
- Old: `rests on editors alone`
- New: `rests on modern editors alone`
- Old: `reports the view of Bernays`
- New: `reports the view of the modern scholar Bernays`

**B4. `uncertain[16]` (the Jerome item)**
- Old: `in a letter that Fremantle dates 415`
- New: `in a letter that its modern translator Fremantle dates 415`

### C. Other lines clearly wrong

**C1. `uncertain[4]` (the Würzburg item, added this pass)**
- Old: `This is a modern judgment, his alone.`
- New: `This is a modern judgment, and his is the only one held.`
- Evidence: Pr 89, "mox mihi et aliis persuasi". Schepss says he persuaded others too, so "his alone" says more than the line holds. The new words match `uncertain[15]`.

**C2. `uncertain[11]` (the date of Sulpicius's Chronicle)**
- Old: `No held source dates Sulpicius's Chronicle. The story says he wrote some years after the deaths because he says the quarrel after them had gone on for fifteen years; that is an inference from his words.`
- New: `No held source dates Sulpicius's Chronicle.`
- Evidence: the brief no longer says "some years after the deaths". It was in v1 to v3, line 5, and was cut before v4. The sentence now names wording the story does not have.

**C3. `briefReferences[2]` (Sulpicius)**
- Old: `the quarrel among his own side`
- New: `the quarrel among the other side`
- Evidence: brief paragraph 10, "The deaths split the other side. Its bishops above all quarreled"; the card's own `uncertain[10]` (*inter nostros*, Sulpicius's side). In this entry, "his" means Priscillian ("his wealth and learning"), so the phrase reverses the brief.

## Not changed, noted

- `legacy.traces[3]` says "held in about 400", where the brief says "In 400". The hedge is looser than the brief, but it does not contradict it.
- `uncertain[17]` says "an editor's note in Mansi". The editor is not named in the held lines. The note is marked as an editor's, so it stays.
