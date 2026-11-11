# R5 — Common-names recheck (targeted), 2026-11-11

Scope: only the sentences changed between `<id>.pre.*` and `<id>.*` in `scratchpad/names/`, plus first-mention ambiguity the drafter missed. Diffed independently (sentence-level difflib on briefs, flattened field diff on cards). Card `sources` blocks identical pre/post; card keys identical; every quoted string (double and single quotes) identical pre/post in all 16 files.

## Score block (scratchpad/score.py → engine.m7.turn_readability.score_turn)

| brief | words pre→post | FK pre→post | FRE pre→post | fails |
|---|---|---|---|---|
| origen | 374→382 | 8.6→8.8 | 62.5→61.7 | none |
| athanasius-of-alexandria | 325→330 | 8.4→8.3 | 63.3→63.0 | none |
| john-chrysostom | 360→371 | 8.5→8.8 | 61.5→60.3 | none |
| gregory-of-nyssa | 346→348 | 8.9→9.0 | 63.3→63.0 | none |
| gregory-of-nazianzus | 307→311 | 8.9→9.1 | 61.2→60.7 | none |
| constantine-the-great | 312→318 | 8.4→8.6 | 67.6→66.9 | none |
| ephrem-the-syrian | 269→274 | 8.4→8.6 | 66.9→66.0 | none |
| methodius-of-olympus | 222→224 | 8.1→8.1 | 61.9→61.8 | none |

All in band (FK 8–10, FRE ≥ 60). The fixes below add at most a few syllables; chrysostom (60.3) is the one to re-score after applying.

## Verdicts

| person | verdict |
|---|---|
| origen | APPROVED |
| athanasius-of-alexandria | APPROVED WITH FIXES (F1) |
| john-chrysostom | APPROVED WITH FIXES (F2, F3, F4) |
| gregory-of-nyssa | APPROVED |
| gregory-of-nazianzus | APPROVED |
| constantine-the-great | APPROVED WITH FIXES (F5, F6, F7) |
| ephrem-the-syrian | APPROVED WITH FIXES (F8) |
| methodius-of-olympus | APPROVED |

No BLOCKING findings. All findings are STANDARD.

## Findings

**F1 — STANDARD — athanasius-of-alexandria brief — "Constantine" at first mention (drafter's open question).**
First and only naming of the emperor in the brief, in the 335 Trier exile. Constantine II also ruled from Trier and is the emperor who sent Athanasius home in 337, so a bare "Constantine" can point to the wrong man. The emperor in 335 is Constantine the Great (Socrates I.35, S2:5365–5372, within the Constantine reign). "Constantine the Great" also matches the person page id.
- Old: `But the price was high. Constantine sent him to Trier, Socrates says,`
- New: `But the price was high. Constantine the Great sent him to Trier, Socrates says,`

**F2 — STANDARD — john-chrysostom card — `legacy.remembered[2]`: the split dropped "while" and with it Socrates's contrast.**
Socrates sets the two dates against each other (S2:21475–21479: "the former was excommunicated by Theophilus about two hundred years after his decease; while the latter was restored to communion by Proclus in the thirty-fifth year"). As split, the second sentence reads as a separate, unattributed fact and the point is lost. One sentence of 28 words keeps attribution and contrast and also drops the clumsy possessive "Theophilus of Alexandria's".
- Field: `legacy.remembered[2]`
- Old: `Socrates notes that Theophilus of Alexandria's condemnation of Origen came about two hundred years after Origen's death. John was restored to communion in the thirty-fifth year after his deposition.`
- New: `Socrates notes that Theophilus of Alexandria condemned Origen about two hundred years after Origen's death, while John was restored to communion in the thirty-fifth year after his deposition.`

**F3 — STANDARD — john-chrysostom brief — Flavian at first mention (drafter left it for length).**
"Flavian" is shared by a better-known later bishop, Flavian of Constantinople (Council of Ephesus 449). "Old Bishop Flavian" gives role but not place; the reader must infer Antioch. Length is not a reason to skip (Mark's ruling); the fix makes the sentence 29 words, within "about 28". Support: S2:17819 ("Flavian bishop of Antioch").
- Old: `until old Bishop Flavian won the emperor's pardon.`
- New: `until Flavian, the city's old bishop, won the emperor's pardon.`

**F4 — STANDARD — john-chrysostom card — Eutropius bare at first mention in the card.**
The card is treated as standalone elsewhere in this pass (Socrates, Sozomen, Proclus get their roles in the cards even where the brief has them). Here Eutropius first appears bare, and the name is shared by the fourth-century historian Eutropius. Support: S2:17325 ("Eutropius was the chief eunuch of the imperial bed-chamber"); the brief already uses "the emperor's chief eunuch".
- Field: `uncertain[0]`
- Old: `Socrates reports that the sermon over Eutropius struck some as cruel.`
- New: `Socrates reports that the sermon over Eutropius, the emperor's chief eunuch, struck some as cruel.`

**F5 — STANDARD — constantine-the-great card — `uncertain[1]`: "Silvester of Rome ... at Rome" is clumsy, and the changed sentence is 45 words.**
The new identifier is right (zachariah-rhetor_chronicle_hamiltonbrooks1899.txt:752 "Silvester, Patriarch of Rome"; :974–975 "his conversion by Silvester is also preserved in writing and in pictures at Rome"), but "Rome" twice in one clause jars for the ear. Split at the colon; keep "since", which carries the chronicle's argument. Second sentence 29 words. Nothing inside quotation marks; meaning unchanged.
- Field: `uncertain[1]`
- Old: `A Syriac chronicle that goes under Zachariah's name says Eusebius got it wrong: the emperor was not baptized at the end of his life, it says, since the story of his conversion by Silvester of Rome is kept in writing and in pictures at Rome.`
- New: `A Syriac chronicle that goes under Zachariah's name says Eusebius got it wrong. The emperor was not baptized at the end of his life, it says, since the story of his conversion by Rome's bishop, Silvester, is kept there in writing and in pictures.`

**F6 — STANDARD — constantine-the-great card — Alexander bare at first mention (missed).**
The card's first mention is the keyWorks[1] title "Letter to Alexander and Arius", and the about line never says who Alexander is. "Alexander" is about as common a name as there is. The title follows the source's own chapter heading (S1:63879), so fix the about line. Support: S1:1676 ("Alexander was bishop of Alexandria, the Arian controversy broke out"); S1:4429 ("To Alexander, bishop of Alexandria"); the brief already calls Arius "the presbyter Arius".
- Field: `keyWorks[1].about`
- Old: `calls their quarrel trifling and asks both to forgive`
- New: `to Bishop Alexander of Alexandria and the presbyter Arius; calls their quarrel trifling and asks both to forgive`

**F7 — STANDARD — constantine-the-great card — `legacy.traces[1]`: bare "Eusebius" directly after two Eusebiuses are named.**
Not a first mention, but `traces[0]` has just named Eusebius of Nicomedia and Eusebius of Caesarea, so "wrote to Eusebius" cannot be resolved by the reader. The letter is Life of Constantine IV.36, "to Eusebius" (S1:67060–67076), in Eusebius of Caesarea's own book. Later bare "Eusebius" in the card then reads as Caesarea.
- Field: `legacy.traces[1]`
- Old: `Constantine also wrote to Eusebius asking`
- New: `Constantine also wrote to Eusebius of Caesarea asking`

**F8 — STANDARD — ephrem-the-syrian brief and card — "Palladius of Galatia" is unconventional and comes from catalogue metadata, not the source.**
"Palladius of Galatia" is the CCEL creator field (palladius_lausiac-history_clarke1918.txt:4), not the translator's text. Galatia is true as his homeland ("a stranger who started out from Galatia", :423) and the province of his later see, Aspuna. But no standard reference calls him that, and "X of [place]" reads as a see. The conventional identifier is Palladius of Helenopolis, and the vendored Moore edition states it plainly: "Palladius, Bishop of Helenopolis (Drepanum, in Bithynia), is known to us as the author of the Lausiac History" (palladius_dialogue-life-of-chrysostom_moore1921.txt:775–777). Moore also notes that Palladius "was by no means an uncommon name" (:893), so the identifier matters. Not BLOCKING, because nothing in it is false.
- Brief — Old: `Palladius of Galatia tells what came next.` New: `Palladius of Helenopolis tells what came next.`
- Card — Field: `uncertain[1]` — Old: `Palladius of Galatia says he died` New: `Palladius of Helenopolis says he died`

## Check lines

- Identifiers verified against vendored sources (grep -n / sed -n):
  - Epiphanius of Cyprus: S2:16792 "Epiphanius, bishop of Cyprus". Salamis is the conventional see; "of Cyprus" is true and clearer. OK.
  - Evagrius Scholasticus: walford1846:5. He is the historian of the 553 anathemas, as distinct from Evagrius Ponticus. OK.
  - Gennadius of Marseilles: S3:3611. OK.
  - Epictetus of Corinth: S4:70618. OK.
  - Silvester of Rome: Zachariah :752. Identifier OK; see F5 for the wording.
  - Eustathius of Antioch, Methodius of Olympus: S2:18141–18144. OK.
  - The Alexandrian priest Isidore: S2:42753. OK.
  - Bishop Alexander of Alexandria: S2:4009. OK.
  - The historian Rufinus: S2:5655, plus Rufinus's Church History as the source of the boy-bishop story. True and not misleading. OK.
  - Gregory the Wonderworker: S6:16659. OK.
  - Meletius of Antioch: S2:13930, 13997; he presided at the 381 council. OK.
  - Severian of Gabala: S2:17922. Proclus of Constantinople: S2:21269, 48076. Cyril of Alexandria, Theophilus of Alexandria and Basil of Caesarea (S3:42470): all OK.
- No added identifier makes a new claim beyond role or place.
- Apollinaris (origen card `legacy.remembered[0]`): Socrates VI.13 (S2:18143) gives no see, the editor's note (S2:1097) gives none, and the index lists the Laodicean only at other pages. Leaving him bare is the correct call under source fidelity, so this is not a finding. If Mark wants "of Laodicea", it needs an outside source; the vendored text does not carry it.
- Theophilus (chrysostom brief): first mention is already "Theophilus of Alexandria". OK.
- First mentions are now correct in all briefs and cards, apart from F1, F3, F4, F6 and F7. Card field order is assumed to be keyWorks → legacy.traces → legacy.remembered → uncertain.
- Splits and joins:
  - Athanasius brief "Athanasius showed both." is a clean short beat; "both" still refers to "his hands".
  - Athanasius card traces[2]: "He sent transcripts" refers to Cyril. Clean.
  - Athanasius card uncertain[0]: "He says Arsenius" is clean, and the quoted "as it is said" is untouched.
  - Chrysostom card traces[2]: "He laid it in" is clean.
  - Chrysostom card remembered[1]: the split at Sisinnius is clean, and the single-quoted saying is untouched.
  - Chrysostom card remembered[2]: see F2.
- Changed sentences over about 28 words: only constantine uncertain[1] (45, F5). Everything else changed is 28 or under.
- Out of scope, for the record only: chrysostom remembered[2] says "after his deposition", while Socrates says "after his death" at S2:21478 but "after his deposition" at S2:21465. The source is inconsistent and the wording is pre-existing; no action in this round.
- Mechanical: all eight edited `.txt` files end with a trailing newline, and the published `.pre.txt` files do not. This is harmless to content, but the apply step should match the published file's ending.
