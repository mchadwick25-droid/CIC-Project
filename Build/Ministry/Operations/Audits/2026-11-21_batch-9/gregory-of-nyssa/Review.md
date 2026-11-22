# Review: Gregory of Nyssa (batch 9)

Brief reviewed: `gregory-of-nyssa.brief.txt` (identical to `gregory-of-nyssa.brief.approved.txt`). Approved before the kit, live and recorded; judged under the change order of 2026-11-19 (approved wording kept wherever it passes). No outline or source sheet: traced to `2026-11-16_eight-standard-v1/drafts/gregory-of-nyssa.refs.md`, the card's `quotationOriginals` and `briefReferences`, and `cic/texts/`. Essence from the census entry `gregory-of-nyssa`.

## The test, from one hearing

1. **Who:** Gregory, bishop of Nyssa in Cappadocia, Basil's younger brother, a Nicene bishop sent into exile under Valens and called home in 378.
2. **What happened:** made bishop by force and hauled up on charges; after Basil died he took over the fight with Eunomius, saying God is above every name and the Spirit is of equal rank; in 381 an imperial law named him as a mark of the true faith; he taught endless growth toward the good and a final restoration.
3. **Why it matters:** in 553 the emperor named him among the holy Fathers the council followed, and in 692 his canons became church law.

All three lines come from one hearing. Test met.

**Essence** (census `why`, `teaser`, `floorNote`; card `knownFor`): Basil's younger brother, who finished Basil's unfinished answer to Eunomius and was named in 381 as a standard of the Nicene faith. **Also told:** his writing against those who denied the Spirit was God; his teaching on the soul, death and the resurrection; and the life of his sister Macrina, the only one we have (the census teaser: "who wrote his sister's life and finished his brother's fight").

- Hook: three sentences (378, Valens dead, the exiles recalled, "One of them was Gregory"). It names him and leads on. Pass.
- Essence: the Eunomius inheritance at word 98, God above every name at 131, the Spirit at 145, the law of 381 at 153-178. Within the first minute. Pass.
- Order after the essence: consecration and summons (c. 372-375), Basil's death, Eunomius, 381, the Great Catechism (undated), 553, 692. Told once, no jump back (the 378 hook reaching ahead is allowed). Pass.
- Also told: the Spirit, yes; restoration and endless growth, yes; **Macrina and the dialogue on the soul and the resurrection, absent** (finding 1).
- Ending: on the council in Trullo, an institution, not the person (finding 4).
- Names heard once that neither act nor link: none. Valens, Gratian, Justinian act; Basil, Eunomius link.
- Where I got lost: "It named Gregory as one whose communion marked them" is abstract on one hearing but recoverable; "the one who brought evil in" does not say who that is (finding 3). Nowhere reads as a children's book or talks down.

## Score

`python -m engine.m1.profile_readability ...gregory-of-nyssa.brief.txt`: 295 words, grade 9.1 (names out 7.7), reading ease names out 71.0, 17.4 words a sentence, longest sentence 33 words, **pass**.

- **Voice 4.** Documentary register, adult, plain. One line reports on the record rather than telling it ("The sources we have do not show...").
- **Craft 3.** Strong hook and an essence on time, but it closes on an institution, and one of the census's two defining points (his sister's life) is missing.
- **Rigor 4.** Every told claim traces to a held text and all three quotes are verbatim. The restoration line drops the painful cleansing the same sentence of Gregory's puts first; the card mislabels one quote's book.
- **Accessibility 4.** Grade 9.1, ease 71. Two phrases are hard to follow on one hearing (see above).

## Verdict: REVISE

## Findings

### 1. BLOCKING: missing essential material (Macrina, and the soul and the resurrection)

The census gives his sister's life as one of the two things he is on the tree for (`teaser`: "who wrote his sister's life and finished his brother's fight"; `why`: "He also wrote the only life we have of his sister"). The card's `knownFor` adds "wrote on the soul, death and the resurrection", and its key works include *On the Soul and the Resurrection* and the *Life of Macrina*. The brief tells neither work and never names Macrina, who is a link on the tree (`macrina-the-younger`).

Smallest change, which keeps the length near the approved 299 (net about +11 words): replace the last sentence of paragraph three.

- Replace: "The sources we have do not show what came of this teaching in his own day."
- With: "He also wrote the life of his sister Macrina, and a dialogue on the soul and the resurrection in which she, near death, answers his grief."

Held by: *On the Soul and the Resurrection*, opening, npnf205_gregory-nyssa-dogmatic-treatises.txt 38083-38103 (after Basil's death he goes to his sister, "lying in a state of prostration even unto death", who "tried to check me by speaking"); *Life of Macrina*, gregory-nyssa_life-of-macrina_clarke1916.txt (his own account, e.g. 184, 214). Gregory's own witness; Macrina is known only through him (census `voices`). The sentence it replaces is a stock how-we-know line (Kit, Rigor: "No stock how-we-know sentence"). Its point stays on the card, whose `uncertain` already says the restoration question is argued. The brief tells Gregory's words and never claims he taught that all are saved, so it does not present the dispute as settled.

**Do not say** (for the outline, if one is drawn): "Do not cut the Life of Macrina and the dialogue On the Soul and the Resurrection for length: they are in the census teaser and `why`. Do not say 'the only life we have' unless a held source says it; say 'he wrote the life of his sister Macrina'."

### 2. MINOR: the restoration line leaves out the cleansing (take it with the re-record)

Great Catechism 26 (npnf205 44413-44418): "after long periods of time ... when there has been a restoration of those who are now lying in Sin ... a harmony of thanksgiving will arise from all creation, as well from those who in the process of the purgation have suffered chastisement". The brief's "those now lying in sin are restored" drops the long, painful purgation that Gregory sets first. This softens his own teaching a little, but it is not false. Since the brief is re-recorded for finding 1:

- Replace: "those now lying in sin are restored and all creation gives thanks"
- With: "those now lying in sin are restored, after long and painful cleansing, and all creation gives thanks"

### 3. MINOR: "the one who brought evil in"

Source: "healing even the introducer of evil himself" (npnf205 44425-44426). In Great Catechism 26 the introducer is the devil. Heard once, a listener cannot tell who is meant. Optional, with the re-record: "heals even the one who brought evil in" becomes "heals even the devil, who brought evil in".

### 4. MINOR: the ending is on an institution

The brief ends on Trullo (692). The kit allows that only when the later institution is the story's point. These are his own canons, so the close is not wrong and does not fail the bar. No change under the change order.

### 5. MINOR: longest sentence 33 words

"When an imperial official, a friend of heretics in Basil's words, had him summoned ... ordained him." This is slightly past "about 30" and nested. The tool passes it and it is approved wording. No change.

### 6. MINOR (card, for step 6): wrong book number for "is above every name"

The card's `quotationOriginals[1].work` and the matching `briefReferences` line say "Against Eunomius XII". The cited lines, npnf205 8957-8958 ("that which is above every name"), are in **Book II** (Book II starts at line 8727 and Book III at 11996; Book XII is 21359-22219). Change "Against Eunomius XII" to "Against Eunomius II" in both places. Note: `refs.md` cites 29665-29667 for this quote. That passage is *On "Not Three Gods" (To Ablabius)*, not Against Eunomius, so do not use those lines. The brief's wording ("the Deity" outside the marks, "is above every name" inside) is held by Book II at 8953-8958, where the uncreated nature of Father, Son and Spirit "surpasses all significance of names".

## Source check (all other sentences pass)

- Valens killed fighting the Goths, 378: Socrates IV.38, npnf202 14630-14647 (consulate and Olympiad). Gratian recalls the exiles: Socrates V.2, 14756-14764. Gregory among the exiles: Life of Macrina, CL 214 ("my exile at the hands of the Emperor Valens on account of the faith").
- Made bishop by force; the official orders him "haled before your judgment seat"; church funds and "canonical order"; "the responsibility lies with the consecrators": Basil, Letter 225 to Demosthenes, Vicar of Pontus, npnf208 39515-39574. "Friend of heretics": Letter 237, npnf208 40844-40852.
- "inherited the controversy with Eunomius": printed "received the legacy of Eunomius' controversy", npnf205 2788. This is the approved modern rendering, recorded in the eight-standard comparison (Q15) and the card.
- Eunomius on ungeneracy as essence: npnf205 25203-25208; the Son "unlike in being to the Father", 4799. Credited "as Gregory reports him".
- "is above every name": npnf205 8957-8958, verbatim (see finding 6).
- "of the same rank as the Father and the Son": npnf205 27944, verbatim.
- 381 law: Codex Theodosianus 16.1.3, codex-theodosianus_latinlibrary.txt 6886 ("unius maiestatis ... gregorio episcopo nysseno", 30 July 381). No reason given: correct.
- Great Catechism 21, the made-able-to-change line: npnf205 44050-44061. Ch. 26: 44413-44426.
- 553: Constantinople II, the emperor's letter, npnf214 23134-23138 (after Hefele's asterisked abridgment ends). 692: Trullo canon 2, npnf214 26715-26747 ("we set our seal ... of Gregory, Bishop of Nyssa").
- Sibling overlap: no quote shared with `basil-of-caesarea` or `eunomius-of-cyzicus` (`Overlap_Report.txt`: clear). Basil's brief ("He made his brother bishop of Nyssa") and Eunomius's (the unbegotten argument, Gregory's answer after Basil's death) agree with this one.
