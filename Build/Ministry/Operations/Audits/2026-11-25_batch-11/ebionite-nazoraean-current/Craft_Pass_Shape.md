# Craft pass (shape): The Ebionites and Nazoraeans

The one checked craft pass under Mark's ruling "a" (Decision-Log, "Batch 11: the two rebuilt stories ship"). Backup before any change: `ebionite-nazoraean-current.brief.v5.txt` (never edited, 674 words by `wc -w`). Only the listeners' blocking faults (`Listen_Shape_FirstTime.md`, `Listen_Shape_Skeptic.md`) and MINOR items a plain word fixes. No other sentence reopened.

## Changed sentences

### 1. Origen's "poverty of their Law" (BLOCKING, both listeners)

- **Old:** In his last years Origen, the teacher from Alexandria, said that their very name came from the poverty of their Law, for Ebion is Hebrew for "poor".
- **New:** In his last years Origen, the teacher from Alexandria, said that their name came from Ebion, Hebrew for "poor".
- **Source:** `Outline.md`, Words to explain, "the poverty of their Law" row: "he does not say there what was poor" (ANF4 39116–39121). The clause is cut, as the first-time listener's fallback gives it. The scorn stays in the next sentence, unchanged ("poor in understanding", ANF4 34023–34025). `Outline.md` "Who they were": "from the Hebrew for 'poor', Origen" (C2).

### 2. Symmachus: why the connection matters (BLOCKING, skeptic)

- **Old:** One of them, Symmachus, put the Hebrew Scriptures into Greek, and their opponents read his version.
- **New:** One of them, Symmachus, put the Hebrew Scriptures into Greek, and the writers who called them heretics used his version.
- **Source:** `Outline.md`, Connection to carry: "the writers who called them heretics were also the ones who kept and used their books" (G1, G4). `Source_Sheet.md` G1 (Origen set it in his columns), G4 (Jerome uses Symmachus's renderings), D6 (Jerome's "heresy of ... Ebion"). No reason why they used it is added: G2b holds none.

### 3. The Hebrew gospel: why it mattered (BLOCKING, skeptic; new sentence)

- **Old:** (none) Between "...and says he put it into Greek and Latin." and "In it, after the resurrection..."
- **New:** Its words survive only in their opponents' quotations.
- **Source:** `Source_Sheet.md` line 29 (head note): "Their own words reach us only as quotations made by opponents: their gospel (F)". `Outline.md` "What they believed": "Words from the gospels they used survive only as their opponents quote them (Jerome, F6, F9...)"; Connection to carry: "what survives of the gospels they used survives in their opponents' quotations". It ties the James scene to them through what was done, not a "this matters because" line.

### 4. Epiphanius's repeated "he says" (MINOR, skeptic 5.4)

- **Old:** They were Jews in everything, he says: they read the Law and the prophets in Hebrew, ...
- **New:** They were Jews in everything: they read the Law and the prophets in Hebrew, ...
- **Source:** the paragraph's first sentence already credits him ("says Epiphanius"); `Outline.md` Beat 4, B11. "He says" stays on "he cannot tell" and on the curse (the outline's credit count names it for the curse).

### 5. The doubled curse (MINOR, skeptic 3.4)

- **Old:** In the synagogues, he says, the Jews cursed them three times a day, praying God to curse the Nazoraeans, because they were Jews who preached that Jesus is the Christ.
- **New:** In the synagogues, he says, the Jews prayed three times a day that God would curse the Nazoraeans, because they were Jews who preached that Jesus is the Christ.
- **Source:** `Outline.md` Beat 4: "the Jews cursed them three times a day, ... praying that God would curse the Nazoraeans" (D3). Same act, said once.

## Not done, and why

- Jerome's role ("the Latin scholar", Beat 5): it fit the outline but took the brief to 678, past the 675 cap. Left out.
- "the Lord's cup", "Nazareth" as Jesus's town: the outline holds no plain sense for either. "James the Just", "Son of Man", "Pontius Pilate": inside quotes. "I answered" in Quote 1: the rendering's own wording.
- "as Eusebius later recorded": kept; the Do not say table requires it. "Elsewhere he calls it": kept, same reason. "as he wrote in 392": kept, it anchors "Elsewhere".
- The first-time listener suggests a Do not say line on "the poverty of their Law"; with the clause cut, none was added (outline not edited in this pass).

## Count and scorer

- `wc -w`: **675** (cap 675).
- `python -m engine.m1.profile_readability .../ebionite-nazoraean-current.brief.txt`: 672 words, grade 8.2 (names out 7.2), reading ease names out 77.5, 19.2 words a sentence, 0.6 joining words per 100, 14% short sentences, longest sentence 33 words - pass.

## Craft check fixes applied

- Change A (delete " Its words survive only in their opponents' quotations."): applied.
- Change B (replace `their name came from Ebion, Hebrew for "poor".` with `their name came from the Hebrew word for "poor".`): applied.
- Change C (replace "and the writers who called them heretics used his version." with "and writers who called them heretics used his version."): applied.
- Outline.md: none of the three targets is named there; unchanged.
- Count: `wc -w` 667.
- Scorer: 664 words, grade 8.3 (names out 7.3), reading ease names out 77.8, 19.5 words a sentence, longest sentence 33 words - pass.
