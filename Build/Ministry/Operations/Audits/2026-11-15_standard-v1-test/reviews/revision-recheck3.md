# Confirmation pass: v4 briefs and references.md

This is a recheck of changes only. I made no model calls and changed no repo file.

## 1. The Eusebius finding

**Confirmed in substance.** The new sentence rests on Gregory's own words:
- History I.38 (Dalton l.1286–1288): Hilary, bishop of Poitiers, banished "at the persuasion of the heretics".
- Glory of the Confessors 3 (Arndt-Krusch l.56917): "Eusebius vero Vercellensis episcopus magnum huic Helario adiutorium contra hereses fuit". "His great helper against heresy" renders that faithfully.

In references.md, Glory of the Confessors 3 is now under What the brief draws on, and the uncertain Eusebius entry is gone. The blocking finding on the references is **cleared**.

**BLOCKING (mechanical, one character).** The v4 brief reads `...that which Hilary and Eusebius taught," These were Hilary...`. The quotation closes on a comma and the next sentence opens with a capital. This is a punctuation error in text the participant sees. It should read `taught." These were Hilary`. That is the only fix needed.

## 2. The non-blocking items

| Item | Status |
|---|---|
| Gregory's opening | **Applied.** "...in the church of Merovingian Gaul, a land split among rival Frankish kings at war with one another." The term is now glossed in place. "Kings were growing more cruel, he writes." follows cleanly. |
| Benedict's sentence 2 | **Applied.** Split at "study." The second sentence opens "There he saw...", which keeps the detail inside Gregory's telling. |
| Paul the Deacon | **Applied.** Now III.1, which is correct (Foulke l.5074 sits before CHAPTER II at l.5106). "Paul wrote in the late 700s, about two centuries after Gregory" is added. That is widely accepted and fine. |
| Census lines | **Applied** for both traditions, matching the census names. |
| "Only Life" and "to show the miracles" | **Applied, with a wording note (NON-BLOCKING).** See below. |
| II.31 and IV.30 | **Applied.** II.31 is dropped. IV.30 now reads "Theodoric, king of the Goths in Italy", which fits the chapter "Of the death of the Arian king Theodoricus" (l.542). |
| Cassian | **Applied.** Now under What the brief draws on: "Institutes and Conferences: his own title for the Conferences of the Fathers". It is no longer listed as uncertain. |
| Gasquet's 480 | **Applied.** "Gardner gives ... about 480, and Francis Gasquet in 480" matches Gasquet l.172–173 and records.json. |
| Estinnes | **Applied.** "The edition records that Hefele and Hahn held ... Carloman's and Pippin's together; its editor argues it was Carloman's." This matches Pertz l.2355–2366. |

**The "only Life" and "to show the miracles" line, in detail.**
- Book II's title, "The Second Book of the Life and Miracles of St. Bennet" (gardner1911 l.3402–3404), supports "to show the miracles of a holy man".
- The absent_details in records.json (era3/batch2) say "A second early witness to his life" is absent and that Book II is "the only surviving Life" (from the Library's file note, gardner1911 l.15). The references line says "the only Life of Benedict". Later medieval Lives exist, so that slightly overstates. Read it as "the only early Life", which matches the absent_details wording.

## 3. Readability (engine.m1.profile_readability --report)

| Brief | Words | Grade | Grade, names out | Reading ease, names out | Words a sentence | Joining words per 100 | Short sentences | Result |
|---|---|---|---|---|---|---|---|---|
| Gregory v4 | 400 | 9.7 | 8.4 | 74.1 | 22.2 | 1.2 | 11% | pass |
| Benedict v4 | 423 | 9.0 | 7.2 | 79.1 | 20.1 | 0.7 | 5% | pass |

## Verdict

- **Gregory of Tours v4 brief: DOES NOT CLEAR, on the punctuation error alone.** Change `taught," These` to `taught." These`. With that one character fixed it clears, and needs no further review.
- **Gregory of Tours references: CLEAR.**
- **Benedict of Nursia v4 brief: CLEARS.**
- **Benedict of Nursia references: CLEAR.** One non-blocking note: "the only Life" should read "the only early Life".
