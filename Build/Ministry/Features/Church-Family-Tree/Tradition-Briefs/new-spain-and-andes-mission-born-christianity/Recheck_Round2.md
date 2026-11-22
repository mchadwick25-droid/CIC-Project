# Recheck, round 2: new-spain-and-andes-mission-born-christianity

Rechecker: Opus, targeted recheck; wrote neither the brief nor the review. Compared `new-spain-and-andes-mission-born-christianity.v1.txt` with `.brief.txt` line by line (diff), and opened the cited lines in `cic/texts/`.

## Verdict: PASS

No edits made to the brief.

## 1. Findings answered as worded

- **B1** (plagues): paragraph 3 is the reviewer's text word for word. Includes M2 ("many others").
- **B2** (counts): paragraph 6 sentences 2-3 are the reviewer's text word for word.
- **B3** (library claims): paragraph 2 is the reviewer's text word for word, including M1 ("now called New Spain"). All three library sentences are gone.
- **B4** (river scene, Acosta last): the scene now sits after paragraph 4, opening "He also told a smaller scene." The Acosta paragraph is last, in the reviewer's text word for word. Includes M6.
- **M3, M4**: paragraph 4 is the reviewer's text word for word.
- **M7**: "So they made a poor raft of canes. Half in the water and half in their arms, they carried the children across" is the reviewer's text.
- **M5**: left, as the review allowed.
- Nothing else changed. Q1 and Q2 are unchanged character for character.

## 2. The new Acosta Peru lines (`acosta_natural-and-moral-history-of-the-indies-v2_grimston-markham1880.txt`)

| Brief claim | Lines | Result |
|---|---|---|
| "Indians of Peru and Mexico" | 3646 ("In Peru"), 4004 ("The Mexicaines"), 3999 ("The Indians") | Holds |
| customs "resembled the law of Moses, and some came near the Gospel" | 3999-4003 | Holds. The Moors clause is dropped, which takes nothing from the point |
| "In Peru ... people confessed their sins aloud" | 3646-3649 ("In Peru ... they confessed themselves verbally, almost in all provinces") | Holds |
| "and washed in water to cleanse them" | 3683-3706 (the Inca's bath in a running river; others who confessed used these baths, the Opacuna); 4003-4005 ("they did wash themselves in water, to clense them from their sins") | Holds. The Opacuna is the Peruvian bath after confession |
| "The Mexica even had a kind of baptism of newborn children" | 4005-4009 | Holds |
| "mixed with great abomination" | 4060-4063 ("the great abomination they mingle therewithal") | Holds |
| "the devil's pride as the cause of their idol worship" | Book V ch. 1 title, 993-994 ("That the Pride and Malice of the Divell hath been the cause of Idolatrie"); contents 155 | Holds. The Sheet cites 990-991; the title sits at 993-994 |
| "But some priests told him that after the Christians came to Peru, people there confessed even their thoughts" | 3678-3682 ("They accused not themselves of any secret actes and sinnes. But, according to the report of some Priests, after the Christians came into that countrey, they accused themselves of their thoughts") | Holds. "But" is Acosta's. "Even" carries his contrast with "not ... secret actes". "Some priests told him" fairly renders "according to the report of". The brief does not say to whom they confessed, nor that it was Christian confession, so it does not go past him |
| "some fifty years later, around 1590" | Not new in this round (v1 had it; the review held it from Sheet W2) | Unchanged |

On the final "But": in the brief it follows Acosta's judgment of abomination, so it is heard as a turn after the Christians came. That is what the reported change is: a change in practice after the Christians came, credited to "some priests". It does not claim belief or conversion. Faithful.

## 3. The plague paragraph (`motolinia_historia-de-los-indios-de-la-nueva-espana-spa_sanchez-garcia1914.txt`)

- "ten plagues": 2942-2944 ("con diez plagas trabajosas"); the ten run 2946-3204+. Holds.
- hunger: 3064 ("La tercera plaga fue una muy gran hambre"). Holds; it comes after smallpox (1st) and war (2nd).
- tribute: 3106 (fifth). slavery: 3160 (eighth, "los esclavos que hicieron para echar minas"). mines: 3121 (sixth, "las minas del oro"), 3179 (ninth, "el servicio de las minas"). Holds. "Forced work in the gold mines" fairly joins the sixth and ninth.
- "the weight of Spanish rule" sums the fourth to tenth, which are all Spanish rule. Holds.
- "Many houses, he wrote, stood empty": 3249-3251 ("de las revueltas y plagas ya dichas, que quedaron muchas casas yermas"), after all ten. Holds, credited.

## 4. The moved river scene and the three totals

- River scene 6871-6898 unchanged in substance from v1 apart from M7, which holds (6896-6898: "medio por el agua y medio en los brazos pasaronlos").
- "three totals for the same fifteen years": four million, 1521 to "esto escribo ... 1536" (6900-6903); close to five million "hasta hoy dia", in "este ano de 1536" (7005, 7011-7013); nine million "en este tiempo que digo, que seran quince anos", after Lent 1536 (7026-7031). All three end in 1536 and run from the conquest; 1521-1536 is fifteen years. Supported.

## 5. Fresh hearing

- Order: 1536 hook, 1523 arrival, the plagues, Motolinia's reading, the river scene, the counts of 1536, Acosta around 1590. It now runs forward with no jump back after the essence. The only step back is the hook to 1523, which v1 had and the review accepted.
- Told twice: "more than four million" (hook and list) is M5, allowed. "more than nine million" in the list and then the quote: the quote is the third total spoken; it lands as the point, not a repeat. Acceptable.
- No sentence past 30 words; the longest is 29.

## 6. Scorer

`python -m engine.m1.profile_readability Build/Ministry/Features/Church-Family-Tree/Tradition-Briefs/new-spain-and-andes-mission-born-christianity/new-spain-and-andes-mission-born-christianity.brief.txt`

> 487 words, grade 5.9 (names out 5.2), reading ease names out 82.7, 13.9 words a sentence, 0.6 joining words per 100, 29% short sentences, longest sentence 29 words - pass (note: grade 5.9 is under 8: the listener read checks it is not flat)

Listener read: not flat. The plagues paragraph is now joined, and the matter (killing, slavery, abomination) is adult.

## Notes for the Sheet (not the brief)

- Sheet line 68 cites the devil's-pride chapter at 990-991; it is at 993-994. The Peru report runs 3678-3682, not 3678-3680 ("thoughts" is on 3682).
