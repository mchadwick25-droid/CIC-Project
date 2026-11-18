# Card edits: the Council of Nicaea (325)

Base: the census `council` object for `council-of-nicaea-325` in `cic-website/data/world-census.json` (not the folder copy). Output: `council-of-nicaea-325.card.json`, the full council object. Every field other than `briefReferences` and `quotationOriginals` is word for word and in order. No `briefLength` (the census validator does not allow it on a council); the brief is 556 words by whitespace count.

## Clearly wrong

None. No card statement is contradicted by a held source or by the finished brief. Checked in passing: "Melitius of Lycopolis" (npnf204 25347, "I, Meletius of Lycopolis"); the editor's dates "14 June to 25 August" in `howItWorked` (npnf201 64400-64402).

## Quotation originals

Kept, with their second readings copied (modern wording and source unchanged), each re-read in its lines:

- "We are persecuted because we said, 'The Son has a beginning, but God has no beginning.'" THDG 70615-70616; English npnf203 6045-6046.
- "For I count civil strife in the church of God worse than any war or fierce battle." Heikel 11167-11168; English npnf201 64468-64470.
- "of one being". npnf214 2412-2413.
- "from God". npnf204 27877-27878.
- "begotten, not made". npnf214 2411-2412.
- "there was a time when he was not". npnf214 2418-2421. The brief also uses these words for the synodal letter's charge (paragraph 1); they stand verbatim there too (npnf214 6345), so the one entry covers both.
- "pre-eminent". npnf214 20217-20220.
- "the whole world groaned, and was astonished to find itself Arian." npnf206 32412-32413.

Removed (the brief no longer quotes it):

- "God of God, Light of Light".

Changed, awaiting second reading:

- Old modern "318 fathers ... shall not be set aside"; new modern "shall not be set aside". The brief now quotes only these words ("the faith of the 318 fathers, its name for Nicaea, "shall not be set aside""). Printed, work, file and lines unchanged (npnf214 13970-13972); `secondReading` left out.

New, awaiting second reading (no `secondReading`):

- "a creature". Printed: "saying also that he is a creature." (npnf214 6346-6347, the synodal letter). Brief: "and that he is "a creature"."
- "whispering ... and winking". Printed: "they were caught whispering to each other and winking with their eyes," (npnf204 27991-27992, De decretis 20; chapter mark at 27984). Brief: "They were caught "whispering ... and winking"."
- "in the sight of all". Printed: "the impious writing had been torn up in the sight of all," (npnf203 6395-6396, Eustathius in Theodoret I.8). Brief: "a written statement was torn up "in the sight of all"."

Order: the kept entries stay in their old order; new entries sit beside the passage they belong to.

## Brief references

Kept word for word: Arius's letter; Life of Constantine III.4-7; Life III.12; De decretis 19-20; Socrates I.8 and Sozomen I.20; Constantinople and Chalcedon; Jerome; the African code.

Changed (the card rule: no quotation marks unless the words stand verbatim in the brief):

1. Eusebius's Letter to his church. Old: `"one in essence" added`. New: `"of one being" added`. Evidence: brief, "the emperor asked for one word to be added: homoousios, "of one being"". "one in essence" is not in the brief.
2. The creed, synodal letter and canons. Old: `"God of God, Light of Light", "begotten, not made", "of one substance";`. New: `"begotten, not made", "of one being";`. Evidence: brief, "calls the Son "begotten, not made", of one being with the Father"; the other two quoted phrases are not in the brief.

Removed (the brief no longer draws on them):

3. "Socrates I.6 (npnf202, 2391-2396): the people divided, some siding with one party and some with the other; Christianity ridiculed even in the theaters."
4. "Council of Antioch, canon 1 (npnf214): the Easter decree of Nicaea enforced."

New, each re-read in its file:

5. Synodal letter (npnf214 6343-6347): the charge, from things that are not, "there was a time when he was not", "a creature". Brief paragraph 1.
6. Life of Constantine III.6-8 (npnf201 64282-64288, 64360-64361): public post and horses; more than 250 bishops; Eustathius (npnf203 6387-6389) and Athanasius (npnf204 26762-26763) give about 270 and about 300. Brief: "let them travel by the imperial post, with horses. More than 250 came by Eusebius's count, though other witnesses gave higher numbers."
7. De decretis 20 (npnf204 27989-27995): "whispering ... and winking". Brief paragraph 4.
8. Eustathius in Theodoret I.8 (npnf203 6390-6396): the formulary torn up "in the sight of all". Brief paragraph 4.
9. Life III.14 (npnf201 64525-64527) and Socrates I.8 (npnf202 2950-2954): the signatures, and a few who would not receive the creed. Brief: "All but a few signed the creed".
10. Constantine's letter against Arius, in Socrates I.9 (npnf202 3382-3384): death for hiding a book by Arius and not burning it. Brief paragraph 5.
11. Canons 4 and 11 (npnf214 3115-3118, 4124-4128). Brief: "from how a bishop is made to mercy for those who had fallen away under the emperor Licinius without being forced."
12. Constantinople, canon 1 (npnf214 13972-13977): the newer heresies named. Brief: "meeting over newer heresies".
13. Braun's introduction (maruta-of-maipherqat Braun 1898, 857-866): Marutha reads the volume of the canons; the Persian bishops declare under an anathema that they will accept them. Brief: "a Persian synod, a modern scholar reports, swore to accept them."

## Not found

None.


## Card check fixes applied verbatim, 2026-11-18

- `briefReferences[0]`: "driven out by Alexander;" removed.
- `[5]`: now "the emperor's advice to add \"of one being\"."
- `[6]`: line range 28015-28018 and "the words written more distinctly" removed.
- `[10]`: "as at Rome and Alexandria; canon 13..." removed.
- `[14]`: Chalcedon recital clause removed.

- secondReading "same" set from Second_Readings.md B4-11, 2026-11-18.

- secondReading "same" set from Second_Readings.md B4-12, 2026-11-18.

- secondReading "same" set from Second_Readings.md B4-13, 2026-11-18.

- secondReading "minor" set from Second_Readings.md B4-14, 2026-11-18.
