# Card check: Marcion of Pontus (batch 4)

**Verdict: FIX** (one change below).

## 1. Edits justified

N1-N8 and W1-W8 hold against the brief and the files. Each printed wording stands verbatim:

| Quote | File and lines |
|---|---|
| Justin's Greek | Rauschen 729-731 |
| "κατὰ πᾶν γένος ἀνθρώπων" | Rauschen 732 |
| "the defenders of Judaism" | anf03 29252 |
| Polycarp's words | anf01 39883-39884 |
| The Antitheses line | Oehler 4337-4338 |

- The IV.4 attribution is right.
- The note "Written A.D. 207" stands at anf03 22488-22489.
- Removing the wasps quote, the good tree reference and the martyrs reference is right. The brief tells none of them.
- The quotation marks were rightly dropped where the words are not verbatim in the brief.

## 2. Nothing else moved

I diffed the card against the census `card` for `marcion-of-pontus`. Only `briefReferences` and `quotationOriginals` differ, as listed. Every other field is word for word.

## 3. References that remain

Thirteen of the fourteen hold in full.

In `[1]`, "Antoninus Pius" names the emperor the brief calls "the emperor". That names the same thing, not a new one, so it stays.

`[6]` fails in one part. Its "his third attempt" (anf03 22509-22512) is not in the brief, which says only "Tertullian's own Against Marcion ran to five books". Those lines also never say "five books". The five books stand at anf03 22298 ("The Five Books Against Marcion"), and Book V opens at 36289-36290. So the cite has to move as well. See the FIX below.

## 4. Census rules

- Keys are allowed and there is no `briefLength`.
- The brief has six quoted spans and the card has six entries, one for each, with none left over.
- All cited files are in `sources`.
- There are no quotation marks in `briefReferences`.
- No audit is named, and the spelling is American.
- Two entries are new or changed and carry no `secondReading`. They are awaiting second reading, which is correct.

## 5. Not found / clearly wrong

The writer reported nothing not found, and none is needed. Nothing in the card contradicts the brief or a held source.

## FIX

`briefReferences[6]`
- Old: `Tertullian (anf03, lines 22509-22512): Against Marcion, his third attempt, in five books.`
- New: `Tertullian (anf03, line 22298): Against Marcion, in five books.`
