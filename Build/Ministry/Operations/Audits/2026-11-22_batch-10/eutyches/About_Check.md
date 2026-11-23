# eutyches: "What it was about" check

**PASS** (no blocking findings; four minor).

Checked against the cited lines in `cic/texts/` (Perry, Leo, Councils, Zach, Evag-E). Every quoted phrase in items 3, 4, 7, 8, 9, 11-14 is at its cited lines and says what the item says. Items 1, 2, 6, 11-14 were already in the brief and remain explained. All six batch-scan gaps and the whole-tree Theodoret gap are answered. Spot-check of "not held": nothing in Leo, Evagrius, Zach or the Councils volume gives where or when he died (Leo 11331 is an editor's summary of a letter urging further banishment), so the brief's closing claim holds.

**Count.** I applied every Room for it edit and cut to a copy of `eutyches.brief.txt` and counted twice (`wc -w`, and a regex count of non-space tokens): 671 both ways. With the fixes below: 673, under 675. No heart, force, conflict, needed credit or carrying scene is cut. The cut sentences (Nestorius's deposition, Eusebius's past, the setting at Chalcedon, the "old heresies" phrase, Theodoret) are events or names, and the judges' charge survives in its own content through item 4.

## Findings

1. **MINOR. Cut 1 leaves a stray comma.** As written, the cut removes "for reviving, in his judges' words, old heresies" and leaves "his place in the church,." Replace the cut line with:
   > 1. Item 5, left out: ", for reviving, in his judges' words, old heresies" (8); the sentence ends "and his place in the church."

2. **MINOR. Item 7's "It" is heard against the wrong noun.** The sentence before ends "judged Eutyches very unwary and exceedingly ignorant", so heard once "It taught" can attach to the last thing named. Replace the item 7 edit line with:
   > - item 7: after "very unwary and exceedingly ignorant.", add "The letter taught one Christ in two natures, each keeping its own character." (+13);

   And in the Sibling section, so the outline does not contradict itself, replace the `leo-of-rome` line with:
   > - `leo-of-rome` (live): tells the Tome and Leo's verdict on 449. Here, Leo appears as a judge answering Eutyches's appeal; the Tome's content is given in one plain line only (What it was about, item 7), not retold.

3. **MINOR. Item 9's "deposed for changing the faith" can be heard as the narrator's verdict.** "Changed the faith" is the ruling of the 449 council (Perry 24114-24118, 24146-24148), from the side that restored Eutyches. The credit in the sentence before ("Its minutes, kept by the side that restored him") helps, but the ruling should sound like a charge, not a fact. Replace the second half of the item 9 edit line with:
   > "Flavian deposed" becomes "Flavian deposed, charged with changing the faith" (+5).

4. **MINOR. Item 10's reason is wrong; its "leave it out" still stands.** The charge against Theodoret is held: Perry's English of the 22 August 449 session carries his deposition (Perry 2129ff, per its content note at line 8). The leave-out is sound because the story does not need him, not because the charge is missing. Replace item 10 with:
   > 10. **Theodoret of Cyrrhus deposed "with others".** Leave out: not needed. His deposition and its grounds are held (the 22 August 449 session in Perry, from 2129; Evag-E 1786-1787 gives only the act), but they are a second case to explain, and the `theodoret-of-cyrrhus` story carries it.

**Count after, with these fixes:** 671 + 1 (finding 2) + 1 (finding 3) = 673 words, under 675. Update the Room for it totals to "Explanations add 50" and "671 + 50 - 48 = 673".
