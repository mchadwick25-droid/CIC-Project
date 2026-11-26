# Recheck of the second-grade fixes: The Latin Apologists

Checks `Fixes_Grade2.md` against `Grades2/listener.md` and `Grades2/Grades.md` (latin-apologists: "Opening: missing when"; one thread-losing sentence), `Grades2/Held_Findings.json` and Mark's ruling "make fixes" (Decision-Log, "Batch 11: second-grade fixes": craft-only pass for the Latin Apologists). Lines are file lines in `cic/texts/`; abbreviations as in `Source_Sheet.md`.

**Verdict: FIX.**

## What holds

- **Sources, opened.** NPNF2-3 40493-40499: Tertullian "from the city of Carthage in the province of Africa … flourished chiefly in the reign of the emperor Severus and Antoninus Caracalla" (later, Jerome; Widely Accepted for "around 200"). NPNF2-3 41022-41025 and 41033-41038: Arnobius and Lactantius "during the reign of Diocletian" (later, Jerome; Documented). The span "from around 200 to the emperor Diocletian's reign" stands on them, as the fix pass says. ANF4 18836-18843: "when we undertook to defend and protect some sacrilegious and incestuous persons, and even parricides, did not think that these (Christians) were to be heard at all. Sometimes even … we were more cruelly violent against them, so as to torture them when they confessed, that they might deny". MinLat 3180-3184: "nos tamen cum sacrilegos aliquos et incestos, parricidas etiam defendendos et tuendos suscipiebamus … nonnumquam etiam miserantes eorum crudelius saeuiebamus, ut torqueremus confitentes ad negandum". Own words (Octavius, as Minucius writes him); Documented.
- **Change 2 (the Octavius sentence)** fixes the thread-losing sentence. "As lawyers" now goes only with the defending, and "they" plainly do the torturing. Each part says no more than the source, and each runs under 25 words.
- **Old strings.** Each of the three brief old strings occurs exactly once. On a scratch copy the fix pass's full set counts 674 by `wc -w`, as it says. No gap-only tell, no new claim, and the heart, the charges, the torture, the burning and leveling, the torture order, the credited witnesses, Q1-Q3 and the Part 1 glosses all stand.

## Findings

**BLOCKING 1. Change 1 turns the opening into a summary opener.** The new first sentence is "From around 200 to the emperor Diocletian's reign, Christians of Rome and Roman Africa defended their faith in Latin." That is the essence, a span and a group, said before any moment. The kind kit says "Open on one moment from the record", and its Traps list "An encyclopedia entry". Kit Part 1 says "Open on one moment, image or line from the record, in about three sentences … Then say the essence plainly." The fix reverses that order. The shore at Ostia is no longer the opening; it is the scene after a summary. "the only when the old sources give for the scene" is "after Octavius died" and the grape-harvest holiday (ANF4 17198-17204, 17247-17255; MinLat 112-116, 210-222). The record gives the scene no era (sheet, section 6: "no old source fixes it"; Do not say: "Any clause naming the Octavius's unknown date"). So the opening already carries the only when it can hold. The span belongs right after the scene, at the head of the essence. It still comes within the first minute (sentences 5-6). Kit Part 1 asks for that: "Let time, place and tradition come in a clause at a time." Drop changes 1 and 1a. Split the old essence sentence instead (replacement B1 below). That also eases the listener's drift note ("the scene stops for a definition"), because its 34-word sentence becomes two of 13 and 20. The listener's "missing when" stays partly unmet in the first three sentences, because the record holds no when for them. The caller should know this.

**MINOR 2. Change 2 drops the source's "sometimes".** Standing alone, "But they tortured Christians who confessed" reads as what they always did. The source says "Sometimes even" (ANF4 18839), "nonnumquam etiam" (MinLat 3182). Once the sentence stands on its own, the qualifier carries weight. Restore it (B2). With B1 at −1, the brief comes to 673.

**MINOR 3. Word counts and one citation in `Fixes_Grade2.md` are off.** Change 1a is −18, not −19: the new text has 16 words. Change 2 is −1, not 0: the fix's new text has 29 words. The net 0 and the 674 still hold. The fix cites MinLat 3179-3182, but the torture clause "ut torqueremus confitentes ad negandum" is at MinLat 3183. The sheet's row (line 59) cites MinLat 3138-3148, which stops at 28.2 and holds neither the defending nor the torture. Both should cite MinLat 3180-3184.

**Noted, not a finding.** `Held_Findings.json` holds one finding for this story: "the emperor's officers burned the Christians' Scriptures … on a day picked to end Christianity" (asks why; weight 1, both readers). Mark's ruling makes this a craft-only pass, so it is outside it. `Fixes_Grade2.md` does not say why it is left.

## Exact replacements

### Brief (`latin-apologists.brief.txt`). Apply these two only, not the fix pass's three.

| # | Old | New |
|---|---|---|
| B1 | `Minucius was one of the Latin Apologists, Christians of Rome and Roman Africa who, from around 200 to the reign of the emperor Diocletian, defended their faith in Latin to the educated who despised it.` | `Minucius was one of the Latin Apologists, Christians of Rome and Roman Africa. From around 200 to the emperor Diocletian's reign, they defended their faith in Latin to the educated who despised it.` |
| B2 | `He and others like him, Octavius says, had once believed them too, and as lawyers had defended the worst criminals but tortured Christians who confessed, to make them deny it.` | `He and others like him, Octavius says, once believed them too. As lawyers they had defended the worst criminals. But sometimes they tortured Christians who confessed, to make them deny it.` |

Each old string occurs once. On a scratch copy the result counts **673** by `wc -w` (limit 674): B1 −1 (34 to 33), B2 0 (30 to 30). New sentences: 13, 20, 11, 8 and 12 words. The opening stays the four-sentence scene at Ostia. The essence's span comes next, still the brief's own words ("the reign of the emperor Diocletian" becoming "the emperor Diocletian's reign", the fix pass's own wording).

### Outline (`Outline.md`)

**Openings 1.** Do not apply the fix pass's change; it stays as it is.

**Beat 2.** Old:

> They had once believed the same things: as lawyers they defended the worst criminals but would not hear Christians, and tortured them to make them deny.

New:

> They had once believed the same things. As lawyers they defended the worst criminals, but would not hear Christians. Sometimes they tortured them, when they confessed, to make them deny (ANF4 18834-18843; MinLat 3180-3184).

**Cut first** (append after the last paragraph). New:

> **To hold 674 after the second-grade fixes (2026-11-25, `Fixes_Grade2.md`, `Recheck_Grade2.md`).** Paragraph 2's essence sentence is split in two after the opening scene (−1), and the Octavius sentence is split in three, with the source's "sometimes" kept (0). The span never opens the story and never dates the scene. 673 by `wc -w`. No Cut first item is applied.

### Source sheet (`Source_Sheet.md`), line 59

Old: `| ANF4 18824-18848; MinLat 3138-3148 | own | Documented |`

New: `| ANF4 18824-18848; MinLat 3138-3150, 3180-3184 | own | Documented |`
