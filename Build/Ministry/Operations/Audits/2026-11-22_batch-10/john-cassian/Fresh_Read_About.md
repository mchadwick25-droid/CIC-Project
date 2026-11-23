# Fresh read, the "what it was about" pass: John Cassian (`john-cassian`)

Batch 10. A fresh hand: no review, revision, check, reply, gaps file or earlier draft opened. Read against `Kit.md` as it now stands, `Outline.md` (with its "What it was about" and "Room for it" sections) and the held texts in `cic/texts/`. Lines re-read 2026-11-23.

## 1. The test, from one hearing

**The four lines.**

- **Who:** John Cassian, a monk who lived for years among the monks of Egypt and later, as a priest at Marseilles in southern Gaul, wrote their rules and their talks in Latin.
- **What happened:** from Bethlehem to the Egyptian desert; made a deacon at Constantinople and sent to Rome with the exiled John Chrysostom's clergy's letters; at Marseilles he founded two houses and wrote the Institutes and twenty-four Conferences; his thirteenth Conference, on grace and free will, drew Prosper's attack; at Leo's request he wrote against Nestorius; he died at Marseilles, year unknown.
- **What it was about:** carrying the desert's way of life to the monks of the West in books, so that they need not go to Egypt; and the quarrel over whether a good will may begin in us or only from God.
- **Why the connection matters:** Latin monks read him. Benedict's Rule set the Conferences first for the evening reading; Gennadius defended him; Cassiodorus kept him but warned against his teaching on free will. Influence through reading, not descent, and with a reservation.

All four are clear from one hearing.

**Every charge, teaching, book, quarrel or decision named, and whether a listener could explain it after one hearing.**

| Named | Explained? |
|---|---|
| The seven Conferences for the two monks | Yes: written so that one need not make the risky journey. |
| The Conferences | Yes: talks with the old monks of the desert. |
| Benedict's Rule and the evening reading | Yes: named the Conferences first for the monks' evening reading. |
| The thirteenth Conference, on grace and free will | Yes: both glossed; the hermit's teaching given with Zacchaeus and the thief, and Q2. |
| Prosper's attack | Yes: in the essence, then explained in beat 7. |
| John Chrysostom's exile | Yes: bishops plotted, soldiers helped drive him out. |
| The Institutes | Yes: dress, prayers and psalms of the Egyptian houses, and the eight chief faults. |
| The eight chief faults | Yes: from greed for food to pride, with their remedies. |
| Prosper's letter to Augustine: "his teaching on God's choosing" | Yes: if God chose before time who would be saved, effort was in vain. |
| Nestorius's teaching | Yes: would not call Mary the Mother of God. |
| Cassian's seven books against Nestorius | Yes: charged him with saying Christ was born a mere man, and tied it to Pelagius's followers. |
| Pelagius's followers' error | Yes: people could live without sin if they liked. |
| The council at Ephesus | Yes: removed Nestorius. |
| Prosper's book against "the Conferencer" | Yes: accepts only that God begins every good thought; rejects that a good will may sometimes begin in us. |
| Gennadius's verdict ("at odds") | Yes, by the beat 7 explanation. |
| Cassiodorus's warning on free will | Yes, by the beat 7 explanation. |

Nothing is named without what it was about.

**The essence and what is also told.** Essence (census entry and outline): he lived among Egypt's monks, then wrote their way of life and talks in Latin at Marseilles; the books carried the desert to the West; Benedict's Rule named the Conferences for evening reading; Conference XIII drew Prosper's attack. The hook (two monks of Gaul who wanted Egypt, three sentences) leads straight into it ("The books made the journey instead"), and the essence is complete at about word 135, inside the first minute. Also told: the Institutes' contents (present, with weight), Conference XIII (present, the strongest passage), Constantinople and Rome (present), Nestorius (present), later readers (Benedict, Gennadius, Cassiodorus present). The Institutes' refusal of wonders and the tempering of Egypt's rules for Gaul, and Gregory of Tours's house, are no longer told; the outline sends each to the card under its own rulings (Cut first 1; "What it was about" items 16 and 17). Not essential material by the bar; noted, not a finding.

**Order.** After the essence the life runs once, in order: Bethlehem and Egypt, Constantinople and Rome, Marseilles and the Institutes, the Conferences (420s), the letter (429), the books against Nestorius (430), Prosper's book and the death, then what came of him. No event twice, no jump back. The Benedict line after the death is what came of him, which the essence reached ahead to; it is not a jump back in the life.

**Ending.** On the person, in his own words (Q1). Good.

**Names heard once that neither act nor link.** None. Zacchaeus and the thief are the hermit's examples. About twelve names, each acting or a link on the tree.

**Where I got lost, or talked down to.** Nowhere lost. Two pronouns made me pause (findings 2 and 3), and "The Rule" four hundred words after Benedict was named made me reach back (finding 1). Nothing reads as a children's book. The readability tool's grade 7.5 is under 8; heard, it is not flat: the opening's frozen Gaul, the broken promise, the soldiers and the hermit's two examples keep the voice.

## 2. The bar

Judged against Kit.md Part 1 and "The bar". No unsupported claim, no misleading implication, no missing essential material, no failure on one hearing, no children's-book stretch.

## 3. The source check

Every sentence traced to `Outline.md`. Quotes re-checked verbatim:

- "frozen, as John Cassian put it, with the cold of Gaul": N211 36729-36730 "frozen as it were with the cold of Gaul". Holds.
- Q2: N211 38028-38030 "These two then; viz., the grace of God and free will seem opposed to each other, but really are in harmony". Rendering holds.
- Q3: N203 43669-43671 "which the church of God finds salutary, but which he brands as injurious". Rendering holds.
- Q1: N211 25950-25952 "setting before you the men themselves incorporated, as it were, in their own Institutes, and what is more to the point, speaking in the Latin tongue". Rendering holds ("rules" for the elders' Institutes, as the outline rules).

Other checks: "bishops had plotted and soldiers had helped drive their bishop out", PAL 2643-2646 ("expelled with the help of the military ... through a plot formed by Acacius of Berea, Theophilus of Alexandria, Antiochus of Ptolemais, and Severianus of Gabala"). Deacon by John, priest at Marseilles, two houses one for men and one for women, N203 43244-43246. Leo and the seven books, N203 43268-43270 and N211 48484-48487. Pelagius's followers, N211 48713-48718. Benedict's evening reading, RB 6838-6846.

## 4. The score

`python -m engine.m1.profile_readability .../john-cassian.brief.txt`: 675 words (cap 675), grade 7.5 (names out 6.0), reading ease 81.5, 16.5 words a sentence, longest sentence 31 words. Pass, with the under-8 note answered above.

## 5. The diff against v3, traced

Nine changed sentences or spans, each traced to "Room for it" and its held text:

| Change | Outline line | Held text |
|---|---|---|
| Opening: "Honoratus and Eucherius," dropped | Room for it, goes 5 | N211 36721; Names allows by role |
| Essence: Institutes clause dropped; "His Conferences were talks with" | goes 4 | Institutes explained in beat 3 (N203 43249-43254) |
| Beat 2: "bishops had plotted and" added | explanation, item 11 | PAL 2643-2646 (plot by four bishops). Holds |
| Beat 3: wonders and tempering sentences dropped | goes 1, 2 | to the card (items 16, 17) |
| Beat 5: "named Chaeremon" dropped | goes 6 | "as Cassian writes him" kept, as Do not say requires |
| Beat 5: "servants of Christ" dropped | goes 7 | GOLD 16932 "Multi ergo seruorum Christi" |
| Beat 5: "If God chose before time who would be saved, they said, effort was in vain." | explanation, item 6 | GOLD 17014-17016 "uel ante mundi initium ... eligendorum et reiciendorum"; 17041 "superfluus labor sit"; 17047-17048 "remoueri ... omnem industriam ... si dei constitutio humanas praeueniat uoluntates". Holds, credited ("they said") |
| Beat 6: "who would not call Mary the Mother of God"; "a council at Ephesus removed Nestorius"; "Cassian charged him with saying Christ was born a mere man" | explanation, items 7, 10 | N202 20737-20739 ("totally rejected the epithet Theotocos"); N214 17278-17280 ("that Nestorius be excluded from the episcopal dignity"); N211 48738-48740 ("who declares that our Lord and Saviour was born a mere man"), credited to Cassian as his charge. Holds; the outline's "removed him" is given as "removed Nestorius", as its note asked |
| Beat 7: "that God begins every good thought. It rejects the rest, among them that a good will may sometimes begin in us" | explanation, item 5 | N211 15782-15785, 15789-15795 (proposition 1, "the initiative ... of our good thoughts comes from God", allowed orthodox), 15810-15814 (proposition 4, "sometimes the first beginnings of a good will arise"). Holds, under the translator's credit |
| What came 1: "The Rule names no author for its Conferences, but the title is Cassian's." | goes 3 | RB 6838-6846; outline: the Rule names no author. Holds |

No changed sentence adds anything the outline does not hold. On Nestorius: his own Bazaar (BAZ 6949-6955) shows him offering "Mother of Christ" in its place, which fits "would not call"; the narrator does not carry the charge forward, which stays Cassian's.

## Scores

- **Voice: 4.** A documentary narrator throughout, the world's own images kept (frozen Gaul, the broken promise, Zacchaeus and the thief). The added explanations sit in the same register; one or two read slightly compressed.
- **Craft: 4.** Clean hook into essence, life once in order, ending on his own hope. "The Rule" after the death paragraph makes the listener reach back, and one changed sentence runs to 31 words.
- **Rigor: 5.** Every sentence and quote holds; each witness credited where it speaks (his own books, Gennadius, the translator, Prosper's letter, Cassiodorus); the hostile book and the enemy's charge are told in their own content; uncertainty (no year of death, the letter not naming him) said plainly.
- **Accessibility: 4.** Every named quarrel and book now explained in a clause; grade 7.5 heard as not flat. Two pronouns ask the listener to work.

## Verdict

**PASS.** No BLOCKING finding.

## Findings

1. **MINOR.** What came 1: "The Rule" comes about four hundred words after Benedict's Rule was named; a listener may not know which rule. Word count unchanged.
   "The Rule names no author for its Conferences, but the title is Cassian's. Benedict's monks did not come from his houses; they read his books." → "Benedict's Rule names no author for its Conferences, but the title is Cassian's. Those monks did not come from his houses; they read his books."
2. **MINOR.** Beat 2: the sentence changed in this pass runs to 31 words, past "about 30", and "his clergy's letters" can be heard as Cassian's clergy. Word count unchanged.
   "When John was sent into exile, Germanus and Cassian carried his clergy's letters to the bishop of Rome, telling how bishops had plotted and soldiers had helped drive their bishop out." → "When John was sent into exile, Germanus and Cassian carried his clergy's letters to the bishop of Rome. They wrote that bishops had plotted and soldiers helped drive their bishop out."
   (Palladius gives it as what the clergy "wrote", PAL 2641-2643, so "They wrote" holds whichever way "They" is heard as the clergy.)
3. **MINOR.** Beat 5: "his teaching" sits between Prosper and Augustine. Word count unchanged.
   "many at Marseilles thought his teaching on God's choosing ran against the Fathers" → "many at Marseilles thought Augustine's teaching on God's choosing ran against the Fathers"

After all three: 675 words, at the cap.
