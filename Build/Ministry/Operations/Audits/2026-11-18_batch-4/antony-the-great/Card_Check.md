# Card check: Antony the Great

Checker, 2026-11-18. Starting card: the census `card` for `antony-the-great` in `cic-website/data/world-census.json`.

**Verdict: FIX** (two `briefReferences` parts).

## 1. Edits justified

N1–N5, R1, W1–W6 all confirmed. Gregory, Oration 21 at npnf207 29544-29554; Sozomen at npnf202 27392-27394; Augustine Latin re-read at CSEL 33 13470-13473 and 13501 (the "20" at 13470 is a printed line number; 13474-13500 are footnotes, apparatus and page head). Each W edit removes or corrects only what the brief no longer tells.

## 2. Nothing else moved

Field-by-field diff against the census card: every change is one listed in `Card_Edits.md`. Key order kept.

## 3. References that remain

1. Life §1–2: the apostles who left all; the Gospel reading; fields to villagers; rest sold.
2. Life §3, §7: work with his hands, prayer, bread and salt once a day. **FIX below.**
3. Life, prologue, and Robertson: authorship credited to Athanasius; the date, 356–362 (the dating behind "soon after his death").
4. Life §12, §14–15: fort, door, twenty years, father, "the desert became a city of monks" (verbatim in the brief).
5. Life §49–50: crowds, healings, the mountain.
6. Life §69: the Arians; the Son not created.
7. Life, prologue: a pattern for monks abroad.
8. Robertson: the Latin translation by Evagrius of Antioch. **FIX below.**
9. Life §81: Constantine and his sons.
10. Augustine, Confessions VIII.6.14–15 and VIII.12.29.
11. Gregory of Nazianzus, Oration 21 §5.
12. Sozomen I.13: the disciples' lands.

## 4. Census rules

Allowed keys only; no `briefLength`. One quoted span in the brief (Augustine), one `quotationOriginals` entry; `printed` stands at 13470-13501. All cited files in `sources`. Quotation marks in `briefReferences` only on brief-verbatim words. No audit named. American spelling, except "colonised" and "idealisation" inside verbatim printed quotes. `secondReading` correctly left out of the changed span.

## 5. Not found / left in

No "not found" claims. Nothing clearly wrong left in, other than the two FIXes.

## FIX

1. `briefReferences[1]`. The brief says "fasting"; it names no bread or salt (the Life §7, npnf204 31421-31422, supports fasting).
   - Old: `Life §3, §7: work with his hands, prayer, bread and salt once a day.`
   - New: `Life §3, §7: work with his hands, prayer, fasting.`
2. `briefReferences[7]`. The brief says only "it was soon put into Latin"; it names no translator.
   - Old: `Robertson's introduction: the Latin translation by Evagrius of Antioch.`
   - New: `Robertson's introduction: the Latin translation.`
