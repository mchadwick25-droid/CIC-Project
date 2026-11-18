# Recheck at release 50: Council of Nicaea (325)

Round 2 discipline: only what changed between `*.r50.brief.txt` and the revised texts, and the card edits in `council-of-nicaea-325.entry.json` (commit b8b8b607), checked against FIXES.md, Fixes_R50.md, the outline, the source sheet and the held texts.

## One hearing

**Main brief**
- Who or what: a council of bishops from across the Roman Empire, called by Constantine to Nicaea in 325 over Arius's teaching that the Son had a beginning.
- What happened: it wrote a creed calling the Son "of one being" with the Father, cursed those who said "there was a time when he was not", condemned Arius and two bishops, and the emperor exiled them; it also limited Melitius, set one Easter and made twenty rules.
- Why it matters: it did not hold at once and divided the church for decades, but later councils held its faith fixed; today's longer creed is tied to Constantinople, not Nicaea; its written canons were read as law as far as Africa.

**Story (how-nicaea-decided)**
- Who or what: how the council reached its decision, told by men who were there, since no minutes survive.
- What happened: Constantine opened in Latin and let the presidents lead; Eusebius says his creed was read, the emperor urged "of one being", and a new statement was drawn up and questioned; Athanasius says Scripture's words were evaded and rewritten.
- Why it matters: the creed's wording came from argued drafts under the emperor's eye, and Athanasius later defended it as the church's faith, not a new rule.

No line is blank or wrong.

## Verdict: PASS

Every fix-list item is made and sourced. No change outside the fix list was made without need (the cuts serve the length item). The two minor findings below are one-hearing clarity points created by the cuts.

## Fix-list items

1. 325 creed apart from today's creed: made. "The longer creed said in churches today is tied to that later council; Nicaea's own was shorter and ended with its curses." Sheet I1 note; NC 2418-2429 (belief ends "And [we believe] in the Holy Ghost", then the anathema); NC 20225-20230 (Chalcedon keeps the two creeds apart). Checked. "Tied to" is properly loose.
2. "They read the bishops' words as true of every creature…": made followable. ATH 27875-27889 and 28015-28018 checked (Second_Readings 15, 16).
3. Other business as a scene; "did not hold" first: made. The letter's own order (NC 6338-6406) is the honest limit of a scene; the impact now runs failure, then later standing.
4. Length: 497 by `wc`, 494 by the profiler, against "about 450" (was 549). See finding 3.
5. "its defense": fixed to "the creed's defense".
6. Emperor's power: made, from Sozomen (SOC 27956-27960) and Socrates (SOC 2962-2966), both checked (Second_Readings 17).
7. Eusebius epithet: varied in both texts ("wrote in praise of the emperor" / "an eyewitness and an admirer of the emperor"); sheet W2.
8. Story, Eusebius's voice and more than one phrase: made. ATH 19655-19669, 19697-19703 checked (Second_Readings 18).
9. Card, Homoian note: made. The note now says the council condemned Arius "and teachings it named" (NC 2418-2429) and that "The Homoian churches came later" (census row starts 340). Sourced and minimal. The census copy and the "Condemned" part are rightly left to the census owner.
10. Card, Athanasius contradiction: made. Five flat statements now carry "Socrates says" / "by Socrates's account" (SOC 2794-2796, sheet C6). Sourced and minimal; nothing else on the card moved.

Removed for length, checked for softening by omission: Eustathius's torn-up statement and Eusebius's "peace as his aim". The force and conflict stay in the brief (Arius driven out; "whispering" evasions now told as reading words around; curses; condemnation; exile by edict; decades of division). Not softening.

## Findings

1. MINOR (one hearing: who speaks the quotation). The cut turned "the emperor told them" into "he told them" right after "As Eusebius reports it", so the nearest name is Eusebius, not Constantine.
   - Now: "As Eusebius reports it, he told them: "For I count civil strife…""
   - Change to: "As Eusebius reports it, the emperor told them: "For I count civil strife…""

2. MINOR (one hearing: referents after the cuts). "It did not hold at once" now follows the twenty rules, so "It" has no clear antecedent; and "the word" in "For decades the word divided the church" is three paragraphs from homoousios.
   - Now: "It did not hold at once." → Change to: "The settlement did not hold at once."
   - Now: "For decades the word divided the church." → Change to: "For decades the word "of one being" divided the church."

3. MINOR (length). 497 words is about 10% over "about 450" (about 3 min 38 s at 137 words a minute; the card's "about 3 minutes 40 seconds" still fits). Not blocking: every remaining paragraph carries an outline beat. If Mark holds to 450, the cut that costs least is "Easter, the second trouble Eusebius names, had some Christians fasting while others feasted; now it would fall on one day everywhere, as at Rome and Alexandria." → "Easter, once kept on different days, would now fall on one day everywhere, as at Rome and Alexandria." (−11 words).

4. MINOR (card housekeeping, flagged in Fixes_R50 and not on the fix list). The card no longer matches the brief's quotations and references:
   - `quotationOriginals`: remove the "in the sight of all" entry (Eustathius, npnf203 6395-6396); add "from God":
     ```json
     {
       "modern": "from God",
       "printed": "that the Son is not from nothing but ‘from God,’",
       "work": "Athanasius of Alexandria, Defence of the Nicene Definition (De decretis) 19, tr. Archibald Robertson",
       "file": "cic/texts/npnf204_athanasius-select-works-letters.xml",
       "lines": "27877-27878",
       "uncertain": "English only: the Greek of De decretis is held (athanasius_opera-omnia-pg25-grc-lat_migne1857.txt) but the passage was not found in the OCR. The same phrase recurs at 27881, \"understood the phrase ‘from God’ as belonging to us\"."
     }
     ```
   - `briefReferences[3]`: "…\"one in essence\" added; he signed with peace as his aim." → "…\"one in essence\" added."
   - `briefReferences[4]`: "\"from God\" read as true of all creatures; Arius's friends whispering and winking; the words written more distinctly." → "\"from God\" chosen from Scripture and read as true of all creatures; the words written more distinctly."
   - `briefReferences[5]` (Eustathius, torn up "in the sight of all"): remove; and remove the Eustathius item from `sources.fromThoseThere` only if nothing else on the card cites it (uncertain[0] still names him as an eyewitness, so keep it).
   - `briefReferences[7]`: "Socrates I.8 (npnf202): Constantine exiles Arius; …" → "Socrates I.8 and Sozomen (npnf202, 27956-27960): the emperor orders banishment for anyone who resists, and his edict exiles Arius; Socrates I.14: …"
   - `briefReferences[8]`: append "; Chalcedon recites the creeds of Nicaea and of Constantinople apart."

Note, not a finding: the brief and the story say flatly "Athanasius, who was there as a deacon", while the card now says "by Socrates's account" and the outline's Do not say gives "a later historian says". The claim is Widely Accepted (sheet C6), so a plain statement in the narrator's voice is allowed.

## Readability

- Main brief: 494 words, grade 9.3 (names out 8.3), reading ease 68.4, longest sentence 30: pass.
- Story: 262 words, grade 8.4, reading ease 73.3, longest 29: pass.

## Second readings

Appended to Second_Readings.md under "Release 50 fixes": 15 "from God" same; 16 Athanasius paraphrase minor; 17 exile paraphrase same; 18 story's Eusebius paraphrase same; 19 Chalcedon lead-in same; 20 letter's other business same. None changes meaning.
