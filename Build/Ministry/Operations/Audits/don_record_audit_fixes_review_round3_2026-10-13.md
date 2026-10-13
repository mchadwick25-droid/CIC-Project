Review round 3, don record audit fixes, 2026-10-13, reviewer: independent Opus subagent (final targeted recheck of round 2 blocking items)

Verdict: PASS WITH NON-BLOCKING


Scope: R2-B1..R2-B6 and non-blocking items 2, 3 and 4 as applied in log_round2_fixes.md, checked against review2.md, `git show HEAD:` and cic/texts/. Read-only. All 16 touched records parse. I graded with engine.m1.gates.grade_text and _readability_checks.

Verdict: CLEAR. There are no blocking items.

---

## BLOCKING

None.

---

## NON-BLOCKING

1. **"A bishop's troops"** in don.dw.what-we-did-with-the-power-we-had `positions` and don.quote.the-shores-are-covered `modern_lens_note`. The swap from "general" is right: Optatus Gildonianus was a bishop. But the possessive goes a little beyond the source. The source says he came *with* a military column: `Gildonianus Optatus incedens cum agmine militari` (Petschenig l.25170; PL43 l.37185). It does not say the troops were his. The column is generally taken to be Gildo's. The story and demo records already say it exactly ("came with soldiers"). A wording such as "a bishop arriving with soldiers to enforce" would match them. These fields are not spoken, and nothing contradicts them.
2. **"bishops and generals"** in don.dw.what-we-did-with-the-power-we-had `positions` (bread-boycott line). This is figurative, unchanged from HEAD and not the Gildonianus error. Leave it, or write "bishops and soldiers".
3. **don.dw.room-for-dissent `text`: "After the beating he dreamed..."** (HEAD had "That night"). The Latin does not fix the moment of the dream (pl8 l.1652-1656, `cum quietis sopore paululum teneretur`). The new wording agrees with the story record's own reading: "Maximianus, still living, had his own vision that night", after the beatings and the prison. There is no contradiction. Noted only because it is an interpretive choice.
4. **Choppy rewrites.** don.core.donatism `horizon` ("It had its own bishops. It had its own basilicas. It had its own line of ordination.", "Which year depends on how one dates the shift. It ran from persecution to the election of bishops.") and don.gravity.martyr-cult-identity `description` (round-2 NB6) are clipped to the point of sounding flat. They are accurate and pass the gate, so this is not a defect against the bar. Smooth them when the text is next touched.
5. **don.dw.becoming-one-of-us `positions`** still has "a dissenting interpreter was cut off permanently", with no hedge for the Tyconius condemnation. That is a build field outside this pass. It is consistent with "never taken back" in room-for-dissent, but it lacks the "reported" hedge used everywhere else now.
6. **Failures that predate this pass.** The readability gate still fails on many `positions[*]` and `claim` fields, and on core `formation_logic`, `thinness` and `cautions`. All of these were already failing at HEAD (gate_after3.txt). The round-2 edits did not make any of them worse (for example, the power-we-had troops line went from 20.5/17.6 to 20.2/19.7).
7. Round-2 NB5 (log the out-of-scope items in Open_Gaps_Tracking.md) is still open. The lead skipped it on purpose. It still has to be done before closure.

---

## Verified

### R2-B1 to R2-B6 (current text read, and compared with HEAD)
- **R2-B1, who-jesus `text`:** now "a bishop writing to the people of Carthage about two of their number put to death closed by urging them to hurry after the two, who were waiting for them." This matches `ad plebem Carthaginis` and `Tendunt ad vos e caelo jam brachia ... Properate` (pl8 l.1918-1919). FK 7.73 / FRE 74.86.
- **R2-B2, written-by-our-opponents `text`:** now "a town councillor admits, under threat of torture, that he added false lines to the letter", with "working for our side" removed, and "One bishop's own letter to the church at Carthage." This matches Optatus l.5704 ("I did add to this letter") and l.5745 (decurion). FK 7.03 / FRE 73.51.
- **R2-B3, room-for-dissent:** `text` now says "shape of a crown shining with blood and light", and the `sources` locus says "the crown of blood and light in the cup". This matches pl8 l.1463-1467 (`corona descendens intra calicis oras`). The word "ring" no longer appears anywhere in records/don. FK 6.78 / FRE 74.42.
- **R2-B4, the three loci:** what-belonging-cost says "Macrobius writing to the church at Carthage". mostly-legend says "the town councillor admitting under threat of torture that he added false lines to the letter". power-against-dissenters says "the bishop who enforced it with troops". The mostly-legend body now says "lines added to the letter and councillor's admission".
- **R2-B5, martyr-cult-identity `description`:** "documented on grounds largely independent of" is restored. The sentence "Three distinct texts, each voiced or written by Donatists, point to it. So do inscriptions cut in stone, with no literary go-between at any point." has the same scope as HEAD. The caveat applies to the inscriptions only, and "So do" refers back to the texts pointing to it. I compared the field clause by clause with HEAD and found no lost hedges or attributions: "On Monceaux's reading" and "Monceaux dates" are kept, and the Mabillon c. 340 date is an accepted round-0 correction. FK 7.28 / FRE 60.78.
- **R2-B6, core `horizon`:** it now says "Numidia is this communion's own heartland", "Several of its best-known bishops" (no stray space after the hyphen), "This communion's whole pattern of refusing imperial legitimacy is defined against that power" and "Donatus succeeded Majorinus from c. 313". Attribution is restored and no antecedent is ambiguous. The change from "roughly a further century and a half" to "about a century and a half more" keeps the meaning. The Gregory sentence matches the source record (two letters name rebaptism in Africa; the 592 letter goes to Numidia). FK 6.87 / FRE 60.01.

### The four rewritten long fields compared with HEAD
I checked who-jesus `text`, written-by-our-opponents `text`, room-for-dissent `text` and the gravity description, alongside the horizon. No hedge or attribution was lost. Several hedges were added: "is reported to have condemned" for Tyconius, "We left no treatise on what his death meant", and "We held that a church was not known by...". Every change in tense or claim strength makes a claim weaker, not stronger.

### Non-blocking 2, 3 and 4 as applied
All of them are present and correct:
- Macrobius `modern_contrast`: "the two are waiting for them and that they should hurry after them".
- `use_note.means`: "tortured and put to death".
- acta `use_note.means`: "a town councillor admitting ... added false lines to the letter", with the agent claim removed.
- passio-isaac source body: "to the church at Carthage".
- liber-regularum: `senses.informational` now reads "a Donatist whom Monceaux calls a layman", `use_note.means` gives Monceaux's account with "is reported to have condemned", and `senses.personal` says "the church said to have condemned its author" (FK 8.64 / FRE 63.97). `senses.translational` grades FK 7.36 / FRE 62.75.
- ministerial-purity `held_against[0]`: "The Acta also record the charge that he acted as an agent for the accusing side, and he denied having been to Numidia." This is exact.

### Vendored-text spot checks (9)
1. Optatus l.5700-5704: the threat of torture, then "I have sinned. I did add to this letter".
2. Optatus l.5716-5735: Apronianus's charge about Mauritania and Numidia. Ingentius answers "No, my Lord" for Numidia and "on commercial business" for Mauritania.
3. Optatus l.5745: "I am a decurion of the Ziquenses."
4. Augustine, Contra litteras Petiliani, Petschenig l.25170 and PL43 l.37185: `Gildonianus Optatus incedens cum agmine militari`.
5. PL43 l.441 note: Optatus Gildonianus was bishop of Thamugadi (`Thamugadensis`).
6. pl8 l.1918-1919: `Tendunt ad vos e caelo jam brachia, opperientes ... Properate`.
7. Monceaux t.5 l.8426 (`c'était un écrivain laïque`) and l.12021 (`un laïque qui se mêlait de théologie`). This backs the Monceaux attribution.
8. pl8 l.1463-1467: `corona descendens intra calicis oras`.
9. pl8 l.1630-1692: the beatings, prison and Isaac's death, then Maximianus's dream of combat, the eye torn out and the crowning youth. This is consistent with the story record's sequence.

### Grades for every spoken field the round-2 log lists (all pass FK <= 10 and FRE >= 60)
- who-jesus `text`: 7.73 / 74.86
- written-by-our-opponents `text`: 7.03 / 73.51
- room-for-dissent `text`: 6.78 / 74.42
- what-belonging-cost `text`: 7.77 / 70.36
- mostly-legend representative turn: 6.09 / 78.38
- power-against-dissenters representative turn: 7.83 / 70.59
- martyr-cult-identity `description`: 7.28 / 60.78
- core `horizon`: 6.87 / 60.01
- power-we-had `text`: 9.55 / 65.69
- shores-are-covered `modern_rendering`: 7.17 / 70.35
- the three story `tellable_as` fields: 6.40 / 68.77, 7.49 / 73.42 and 7.11 / 62.31
- liber-regularum `plain_meaning`: 5.86 / 77.52
- liber-regularum `quick_meaning`: 4.65 / 76.55
- liber-regularum `senses.personal`: 8.64 / 63.97

The other fields the log lists are `modern_lens_note`, `modern_contrast`, `use_note.means`, `held_against` and the loci. None of these is readability-graded. They grade above 10 at HEAD as well.

### Residual grep across records/don
- **"notary":** the only hits are the 411 imperial notaries (Marcellinus, the conference acta). That is correct usage. None refers to Ingentius.
- **"ring of blood" or "ring":** no hits.
- **"any of them":** the hits are the Council of Cirta question (room-for-dissent, becoming-one-of-us, council-of-cirta) and the Bagai limit. That is correct usage. None is the Macrobius closing.
- **"a general" or "the general":** the hits are "not a general end", "general persecution", "general portrait", "general disaster" and "general apology". None refers to Gildonianus. The phrase "bishops and generals" is non-blocking item 2.
- **"tortured to death":** no hits.
- **"four days before":** the only hit is becoming-one-of-us `text`, "held four days before he was thrown from a cliff". That is a correct statement of Marculus's four days at Novapetra (pl8 l.1049); it is not the vision-timing error.
- **"his own congregation":** the hits are becoming-one-of-us `positions` (another bishop's words about fear, not Macrobius), silvanus-of-cirta and the 411 story ("no traditores in his own congregation"). None of them is the Macrobius addressee.
