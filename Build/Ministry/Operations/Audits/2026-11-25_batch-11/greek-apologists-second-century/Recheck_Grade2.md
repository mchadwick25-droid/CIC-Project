# Recheck of the second-grade fixes: The Second-Century Greek Apologists

Checks `Fixes_Grade2.md` against the live brief, `Outline.md`, `Source_Sheet.md`, `Grades2/Grades.md`, `Grades2/listener.md` (two bare statements), `Grades2/Held_Findings.json` and Mark's ruling "make fixes" (Decision-Log, "Batch 11: second-grade fixes": "what the new decrees did; who the wicked men were"). I did not write the fixes. Every cited line below was opened in `cic/texts/`.

**Verdict: FIX.**

## What holds

- **The source findings.** npnf201 25818–25826: "being driven about in Asia by new decrees. For the shameless informers … taking occasion from the decrees, openly carry on robbery night and day". npnf201 25834–25838: "if … this new decree … be not from thee". otto1872 20996–21029: καινοῖς ἐλαυνόμενον δόγμασι … τὴν ἐκ τῶν διαταγμάτων ἔχοντες ἀφορμήν, Latin "ex illis edictis occasionem nacti" (OCR). No term of the decrees is given anywhere. npnf201 21048–21049: "because certain wicked men had attempted to trouble the Christians"; otto1872 17518–17520: πονηροί τίνες ἄνδρες τοὺς ἡμετέρους ἐνοχλεῖν ἐπειρῶντο. Jerome, npnf203 39898–39901: "those who hated the Christians took opportunity … to harass the believers", naming no one. The fix pass reads all of these rightly, with the right witness kinds (Melito own, quoted by Eusebius; Eusebius later; Jerome later and dependent) and confidence. Setting aside Jerome and the Granianus and Fundanus letters is right.
- **The absences are real** and belong on the sheet as `kind: absence` rows.
- **Old strings.** All nine brief old strings occur exactly once. On a scratch copy the fix pass's full set counts 675 by `wc -w`, as it says.

## Findings

**BLOCKING 1. "Melito does not say what the decrees ordered." is a gap-only sentence.** Kit Part 1, Craft: "No sentence that only says what is missing." Explain it: where the sources give only the act, "tell it as they give it … no word on the missing one … do not announce it unless the gap is itself the story." The terms of the decrees are not this story's subject. The story is the charges and the answers. The sentence says nothing the record holds. The content the record does hold is already in the brief's own sentence: informers used the decrees to rob the innocent night and day. That sentence also answers what the decrees did, as far as Melito tells it. Withdraw change 1 and keep that sentence word for word. The fix pass's "used them" would lose its referent once the gap sentence goes, so the old wording is the right one. The Alexandria recheck in this batch cut a line of the same kind ("but Eusebius never says so outright") on the same rule.

**BLOCKING 2. "Eusebius, a church historian, names neither them nor their deeds." is a gap-only sentence.** It is the same fault. It only says what is missing, and who the wicked men were is not the story. It also breaks the beat's event-then-defence order with a sentence about the record instead of the people. "Wicked men were trying to trouble the Christians" is the act as Eusebius gives it, and Part 1 says to tell it that way. That is the fallback the fix pass itself names (0 words). Withdraw change 2, and with it 2a: once 2 goes, the gloss "a church historian" is already at Eusebius's first mention. Keep "certain": it is Eusebius's τινες, and nothing needs to be paid for now.

**MINOR 3. Cuts 3–8 pay for nothing once 1 and 2 go, and cut 3 strains the outline.** With no words added, nothing needs cutting, and the Alexandria recheck withdrew unneeded cuts on the same ground. Cut 3 ("condemned and") also goes against the outline's own Do not say line, which says to tell only "condemned for refusing to sacrifice to the gods and obey the emperor's command" (Acts 5). Cut 4 sends a source word, πανταχοῦ, to the card for no gain. Withdraw 3–8. The outline line 64, 65 and 68 changes and Cut first item 25 go with them.

**Noted, not a finding.** The Do not say line on Melito's "examine the authors of such strife" says "the Greek is not held". otto1872 now holds it (OCR). That is outside this pass.

## Exact replacements

### Brief

Apply none of the fix pass's brief rows (1, 2, 2a, 3–8). The brief stands as it is: **675** by `wc -w` (limit 675), checked a second way by a whitespace split (675). Readability on the scratch copy: grade 8.4, ease 72.2, pass. The sentences that stand:

- "Long before, under Hadrian, certain wicked men were trying to trouble the Christians." (13 words)
- "In the passages Eusebius copied, Melito wrote that informers, people who laid charges against others and took their goods, used the decrees to rob the innocent night and day." (29 words, an old sentence the outline check passed; its gloss of "informers" is required by Part 1.)

### `Outline.md`

Apply none of the fix pass's outline changes to lines 63, 64, 65, 66 or 68, and do not add Cut first item 25. Lines 63 and 66 stand, and the absences go into Do not say instead, so no writer fills or announces them. After the line `- "were troubling the Christians" → "were trying to trouble" (Eusebius: "had attempted").`, add:

`- who the "wicked men" were or what they did (Jerome's "those who hated the Christians", the Granianus and Fundanus letters), or any line saying Eusebius does not name them → only "certain wicked men were trying to trouble the Christians" (npnf201 21048–21049; otto1872 17518–17520). No held old source says; tell it as given, with no word on the missing (Grades2, both readers; absence).`
`- what the new decrees ordered, or any line saying Melito does not say → only that informers used the decrees to rob the innocent (npnf201 25818–25826; otto1872 20996–21029, ἀφορμήν). No held source gives their terms; tell it as given, with no word on the missing (Grades2, both readers; absence).`

### `Source_Sheet.md`

The two new rows (after line 41 and after line 69) and the line 176 Library-sweep change apply as the fix pass gives them, except that in each new row, after "Absence (kind: absence)", the text adds "; not told in the brief (Kit Part 1, Explain it)". Exact:

- Quadratus row: old `Absence (kind: absence): Eusebius names neither;` → new `Absence (kind: absence); not told in the brief (Kit Part 1, Explain it): Eusebius names neither;`
- Melito row: old `Absence (kind: absence): Melito gives no terms,` → new `Absence (kind: absence); not told in the brief (Kit Part 1, Explain it): Melito gives no terms,`

Each old string occurs once in the fix pass's new rows.
