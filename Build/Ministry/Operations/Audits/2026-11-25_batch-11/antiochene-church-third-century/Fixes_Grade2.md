# Fixes from the second batch grade: antiochene-church-third-century

Source of the findings: `Grades2/listener.md` (antiochene-church-third-century: one bare statement, one thread-losing sentence) and `Grades2/Held_Findings.json` (two Supporting, both "missing why", both readers). Ruling: Mark, "make fixes" (Decision-Log, "Batch 11: second-grade fixes"). The brief, outline and sheet are not edited here; these are the exact replacements to apply.

Count: the live brief is 671 words (`wc -w`). With all changes below applied it is 675 words (`wc -w` on a scratch copy), at the ruled cap. `python -m engine.m1.profile_readability --report` on that copy: 675 words, grade 7.5 (names out 6.7), reading ease names out 76.0, 16.5 words a sentence, longest sentence 37 words (paragraph 3, the essence, unchanged), pass, with the scorer's note that grade 7.5 is under 8 and the listener read should check it is not flat. Live brief: grade 8.1, 74.2, 17.7, pass. The drop comes from the shorter sentences in fixes 1 and 3; no sentence is flattened in substance.

## What the sources hold

**The church house (fix 1).** One witness only: Eusebius, HE 7.30.18-19, later (a generation or two), Documented (`Source_Sheet.md` A1, line 118).
- Who refused: Paul. "But as Paul refused to surrender the church building" (`cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` 42324-42325); Greek "μηδαμῶς ἐκστῆναι τοῦ Παύλου τοῦ τῆς ἐκκλησίας οἴχου ϑέλοντος" (`eusebius_werke-bd2-2-historia-ecclesiastica-vi-x-rufinus-x-xi-grc-lat_schwartz-mommsen1908.txt` 12114-12115).
- Who petitioned: **no held source names anyone.** The Greek is passive, "βασιλεὺς ἐντευχϑεὶς Αὐρηλιανὸς", "the emperor Aurelian, being appealed to" (E-Gk 12115-12116; E-Eng 42325-42326, "the Emperor Aurelian was petitioned"). The brief therefore says "the case went to the emperor Aurelian", which names no petitioner and adds none.
- Who got it and why: the house went "to those to whom the bishops of Italy and of the city of Rome should adjudge it" (E-Eng 42326-42328); Greek "τούτοις ... οἷς ἂν οἱ κατὰ τὴν Ἰταλίαν καὶ τὴν Ῥωμαίων πόλιν ἐπίσκοποι τοῦ δόγματος ἐπιστέλλοιεν", "to those to whom ... should write" (E-Gk 12116-12118). Who that side was: the bishops' letter, addressed "To Dionysius [of Rome] and Maximus, and to all our fellow-ministers throughout the world" (M5, line 105; E-Eng 42003-42027, contemporary, Documented), had appointed a new bishop and asked them "that you may write to him, and may receive letters of communion from him. But let this man write to Artemas" (M6, line 106; E-Eng 42274-42314, E-Gk 12018-12026, contemporary, Documented). Eusebius then says Domnus "became bishop of the church at Antioch" (E-Eng 42314-42316) and, after the ruling, "Thus this man was driven out of the church ... by the worldly power" (E-Eng 42328-42330; E-Gk 12118-12120, "οὕτω δῆτα").
- Why Aurelian so ruled, in his own mind: no motive is held. Eusebius says only that he judged "most equitably" (αἰσιώτατα, E-Gk 12116), already on the card (Ruled 4). The why the listener lacked is the mechanism, and that is held: the bishops of Italy and Rome had been asked to write to the new bishop, not to Paul. The outline's Do not say (line 159) bars "in communion with Rome" and "judged the faith"; the new wording uses neither.

**Lucian out of communion (fix 2).** No held source gives a reason. Two pre-1931 English translations of the one witness, Alexander of Alexandria's letter (later, c. 320s, Arius's enemy, Documented as his charge):
- Theodoret's text, trans. Jackson 1892: "Lucianus, his successor, withdrew himself from communion with these bishops during a period of many years" (`cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` 5759-5762; `Source_Sheet.md` L4, line 134).
- ANF vol. 6, 1886: "To whom Lucian succeeding, remained for many years separate from the communion of three bishops" (`cic/texts/anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml` 28778-28779). New to the sheet; it says how many bishops, not why.
- The editors' notes (Thdt note 295, 5760-5768; ANF6 note 2429, 28779-28781) are modern and give no reason either.
- Library search: 410 files in `cic/texts/` mention Lucian; a search for Lucian within 120 characters of "communion" or "separat" found only these two witnesses (and one unrelated Mansi line, 42863). The sentence therefore says, as the letter's own limit, that the letter gives no reason.

## Brief changes (`antiochene-church-third-century.brief.txt`)

| # | Old | New | Words old / new / net |
|---|---|---|---|
| 1 | Paul would not leave the church's house. The emperor Aurelian was petitioned, and he ordered that the house go to the side the bishops of Italy and Rome wrote to. So those bishops' letters decided it, and Paul was driven out of the church by the worldly power. | Paul would not leave the church's house, so the case went to the emperor Aurelian. He gave the house to whichever side the bishops of Italy and Rome wrote to. Paul's judges had named a new bishop and asked them to write to him, not Paul. So Paul was driven out of the church by the worldly power. | 48 / 58 / +10 |
| 2 | That bishop set Lucian in a line from Paul to Arius: Lucian, he wrote, kept out of communion with the bishops for many years, and Arius and his party were shoots of the same root. | That bishop set Lucian in a line from Paul to Arius. Lucian, he wrote, kept out of communion with the bishops for many years, but his letter does not say why. Arius and his party, he wrote, were shoots of the same root. | 35 / 43 / +8 |
| 3 (cut) | questioned Paul while shorthand writers took the debate down, and Eusebius says he alone could catch out a man who hid his mind. | questioned Paul while shorthand writers took the debate down. | 23 / 9 / -14 |

Net +4: 671 to 675.

What each fixes:
- Fix 1. Who refused: Paul, the subject. Who petitioned: not said, because no source says; the active "the case went to" stops the listener asking. Who got it: the side the bishops of Italy and Rome wrote to, which the next sentence names as the new bishop's, from the judges' own letter (M5, M6). Why: those bishops had been asked to write to him and not to Paul, so the ruling went against Paul, as Eusebius's "thus" gives it. "So" now follows a reason the listener has heard. Sentences: 15, 16, 16, 11 words. The new bishop is told by role only; Domnus's name stays on the card (Cut first 7).
- Fix 2. The old 35-word sentence is split in three. "But his letter does not say why" is the source's limit, said once in seven words, inside Alexander's own sentence. "He wrote" keeps the root image in Alexander's mouth, as the outline requires (line 73, line 109). Sentences: 11, 21, 11 words.

## Cuts and where each goes

| Cut | Words | Goes to | Why it is safe |
|---|---|---|---|
| Eusebius's judgment on Malchion, "and Eusebius says he alone could catch out a man who hid his mind" (M2, `Source_Sheet.md` line 102; E-Eng 41977-41984) | 14 | the card | A judgment in Eusebius's voice, not an event. Not the heart (`Outline.md` line 9), not the record's force, not a Part 1 explanation. The Never-cut line keeps "Malchion's questioning", and the questioning before shorthand writers stays. |

The 14 words cut pay for the 18 added beyond the old text, with the remaining 4 inside the 675 cap. Nothing from the Never-cut list (`Outline.md` line 216), the heart, the ruling and its plain sense, or Alexander's charge as a charge is touched.

## Outline and sheet lines to change

**`Outline.md` line 71 (beat 4).**
Old:
> Eusebius says he alone could catch out a man who hid his mind (M2; a judgment, credited to Eusebius).

New:
> Eusebius says he alone could catch out a man who hid his mind (M2; a judgment, credited to Eusebius). [cut: card, Grade 2]

**`Outline.md` line 72 (beat 5).**
Old:
> The emperor Aurelian, who defeated Zenobia, queen of the East, near Antioch (S6, Jerome's Chronicle; a clause, Cut first 5) [cut: Leave out], was petitioned. He ordered the house given to those to whom the bishops of Italy and Rome wrote (A1, Greek).

New:
> So the case went to the emperor Aurelian (A1, ἐντευχϑεὶς, passive: no source names who petitioned; name none). The clause that he defeated Zenobia, queen of the East, near Antioch (S6, Jerome's Chronicle; Cut first 5) [cut: Leave out]. He gave the house to whichever side the bishops of Italy and Rome wrote to (A1, Greek). Paul's judges had named a new bishop and asked them to write to him, not Paul (M5, M6; the new bishop by role, his name Domnus on the card, Cut first 7).

**`Outline.md` line 73 (beat 6).**
Old:
> Lucian, he wrote, kept out of communion with the bishops for many years (L4, L4-Gk).

New:
> Lucian, he wrote, kept out of communion with the bishops for many years, but his letter does not say why (L4, L4-Gk, L4-ANF; no held source gives a reason; add none).

**`Source_Sheet.md`, after line 135 (L4-note), a new row.**
New:
> | L4-ANF | Alexander's same letter in a second English: Lucian, succeeding Paul, stayed separate from the communion of three bishops for many years; no reason given | ANF6 28778-28779 (editor's note 2429, 28779-28781, modern, not used) | later (c. 320s), Arius's enemy; English printed 1886 | Documented as Alexander's charge | "To whom Lucian succeeding, remained for many years separate from the communion of three bishops." |

**`Source_Sheet.md` line 123 (Explain it, "Aurelian's ruling"), appended to the end of its bullet.**
Old (end of the bullet):
> He judged who held communion, not what was true about Christ.

New:
> He judged who held communion, not what was true about Christ. Who the bishops of Italy and Rome were asked to write to: the new bishop, not Paul (M5, M6). Who petitioned: the Greek is passive (ἐντευχϑεὶς, E-Gk 12115); no held source names anyone.

## Totals

Applied in this file as exact replacements: 2 fixes and 1 cut. Brief ends at 675 words. Nothing was added that no held source gives: no petitioner, no motive for Aurelian, no reason for Lucian.
