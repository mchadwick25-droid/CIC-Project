Review round 1, don record audit fixes, 2026-10-13, reviewer: independent Opus subagents (two parts)

Verdict: DOES NOT CLEAR. 12 blocking items; all fixed before round 2.

Scope: all changed files under records/don in the working tree before the first commit (doctrinal_witness, demonstration, story; figure, term, honest_limit, quote, ambient, force, gravity, contested_claim, voice_craft, world_core, and the 76 added source citation lines).

# Part A: doctrinal_witness, demonstration, story


Scope: every changed field in the working-tree diff against HEAD for records/don/doctrinal_witness/ (27 files), records/don/demonstration/ (11), records/don/story/ (13). I compared fields after parsing them (old vs new YAML, sentence diffs), graded every touched spoken field with engine.m1.gates.grade_text, and checked the claims against cic/texts/. I edited nothing in the repo.

Verdict: NOT CLEAR. 10 blocking findings. Most are one of two kinds. (a) A correction was made in one record, but a sibling record's touched field still carries the old error, so the world now contradicts itself. (b) An edit was based on an incomplete reading of the source.

---

## BLOCKING

### B1. don.dw.the-books-they-came-for - `text` - broken sentence
- Exact text: `read the account of each death aloud again every year, . That is an answer of a kind.`
- Why: The deletion of "as though the ending were not the end" left a stray ", ." in a spoken field.
- Fix: `read the account of each death aloud again every year. That is an answer of a kind.`

### B2. don.dw.not-a-death-wish - `text` (and `sources[*].locus` for the Macrobius letter); don.demo.death-wish - `sources` locus for don.story.macrobius-letter - misreport of Macrobius's closing
- Exact text (dw text): `And the letter one of our bishops wrote to the church at Carthage does not say: go and seek this. It says the opposite kind of thing, and harder. It says that what was done to these two may yet be asked of any of you. That is a man preparing people who did not choose the situation for something they cannot avoid.`
- dw locus: `Macrobius closing by telling his congregation the same may yet be asked of any of them`. Demo locus: `the closing turn to the congregation - the same may yet be asked of any of you`.
- Why: The vendored letter (monumenta-vetera-donatistarum_migne-pl8.txt, closing paragraph, ~l.1918) says `Tendunt ad vos e caelo jam brachia, opperientes tempus quo vobis occurrant. Properate graviter, concurrite pertinaciter... accelerate quantocius`. That is an exhortation to hurry after the martyrs, not "it may be asked of you". This pass corrected the same misreading in don.dw.what-belonging-cost, don.dw.who-jesus-was-among-us, don.demo.death-wish (turn) and both Macrobius story records. This dw's touched paragraph keeps it, and now contradicts them. It also contradicts don.demo.death-wish's new line, "We will not pretend that sounds like a man talking anyone out of dying."
- Fix (text): `And the letter one of our bishops wrote to the church at Carthage ends by calling the living to follow the two. It says they are waiting with their arms stretched out from heaven, and it tells the readers to hurry. We will not pretend that sounds like a man talking anyone out of dying.` Locus (both records): `Macrobius's closing: the two wait with arms stretched out from heaven, and the readers are urged to hurry after them`. Re-grade the text after the change.

### B3. don.dw.hypocrites-and-those-who-left - `text` - same misreport
- Exact text: `What he does instead, at the end, is turn to the people reading and tell them that what happened to those two may yet be asked of any of them.`
- Why: Same source and the same contradiction as B2. This paragraph was touched in this pass ("to the church at Carthage", "weighting them with sand").
- Fix: `What he does instead, at the end, is turn to the people reading and tell them the two are waiting for them, and that they should hurry after them.` (The sentences after it, "That is the whole of the answer he gave... to readers who were likely to be next", still read correctly.)

### B4. don.dw.what-we-did-with-the-power-we-had - `text` - two errors already corrected in its near-twin demo
- Exact text: `In the year 320 an official put our own people on oath about where four hundred pieces of silver had gone` ... `Every one of those letters ends the same way.`
- Why: The Gesta letters (optatus_against-the-donatists.txt ~l.6202-6226) do not all end with "let no one know". Fortis's letter to the clergy and seniors does not. This pass changed the same sentence to "Several" in don.dw.hypocrites, don.demo.never-settled, don.demo.power-against-dissenters and don.story.gesta-apud-zenophilum. The hearing was on Nundinarius's charge against Silvanus, not an inquiry "about where the silver had gone". don.demo.power-against-dissenters was corrected to say so, and this record carries the identical paragraph in a touched field.
- Fix: `In the year 320 an official heard sworn witnesses on a charge against one of our bishops, a charge that named four hundred pieces of silver, and read our bishops' letters into the record.` and `Several of those letters end the same way.`

### B5. don.dw.what-we-never-settled - `text` - same
- Exact text: `Every one of those letters ends the same way.`
- Why: Same as B4. The parallel demo (don.demo.never-settled) was corrected and this touched field was not.
- Fix: `Several of those letters end the same way.`

### B6. don.dw.who-jesus-was-among-us - `text` and `sources[6].locus`; don.dw.what-belonging-cost - `text` - Marculus timing and the deaths of Isaac and Maximianus
- Exact text (who-jesus): `Our own martyr was shown a cup, a crown and a palm four days before he was thrown from a cliff` and `about two of their number tortured to death`. Locus: `the cup, the crown and the palm shown four days before the cliff`.
- Exact text (what-belonging-cost): `two of their number who had been tortured to death and whose bodies the proconsul had weighted and sunk`.
- Why (Marculus): Passio Marculi (pl8 ~l.1049-1060) gives the vision at the end of the last night (`ubi majora noctis spatia exacta sunt... ante passionem`). The four days are his wait at Novapetra. don.story.passio-marculi's tellable_as was corrected away from "four days before" in this pass.
- Why (deaths): Macrobius (pl8 ~l.1627-1628, 1742) says both were imprisoned, Isaac died there, and Maximianus was sunk alive with the dead (`vivum pariter cum defuncto, marinis fluctibus mergi`). Both Macrobius story records were corrected on this point in this pass. "Tortured to death" for both now contradicts them. Both fields were touched.
- Fix (who-jesus): `Our own martyr was shown a cup, a crown and a palm on the last night before he was thrown from a cliff - shown, in advance, what finishing looked like. And a bishop writing to the people of Carthage about two of their number put to death closed by urging them to hurry after the two, who were waiting for them.` Locus: `the cup, the crown and the palm shown on the last night before the cliff`.
- Fix (what-belonging-cost): `about two of their number who had been tortured and put to death, one in prison and one drowned alive, and whose bodies the proconsul had weighted and sunk in the sea so that nobody could venerate them.` Re-grade both fields.

### B7. don.story.passio-marculi - `tellable_as` - "four days' fasting"
- Exact text: `On the last night of four days' fasting, Marculus is shown a cup, a crown and a palm.`
- Why: `ultimum quatridui illius diem jejunio terminavit` (pl8 ~l.1049) says he closed the last of the four days with a fast. The four days are his custody at Novapetra (`quatriduum illud, quo illic a corona impendente dilatus est`), not four days of fasting. don.dw.becoming-one-of-us was corrected for exactly this overclaim in this pass, and this newly written field brings it back.
- Fix: `On the last night of his four days at Novapetra, after a day of fasting, Marculus is shown a cup, a crown and a palm. Before dawn he is thrown from a cliff. The tradition says his body came down gently, and a bright cloud showed the brethren where he lay.`

### B8. Ingentius was a decurion, not a notary - don.story.acta-purgationis-felicis `text` and `tellable_as`; don.demo.mostly-legend `exchange[1].text`
- Exact text: story text `and a notary named Ingentius`. tellable_as `A notary admits, under threat of torture, that he added false lines to a letter against him.` Demo `a notary, under threat of torture, admits that he added false lines to the letter used against a bishop.`
- Why: In the Acta (optatus_against-the-donatists.txt ~l.5744) Ingentius answers `I am a decurion of the Ziquenses.` The notary from 303 had died (~l.5489: `the notary of that time has departed this life`). All three spans were rewritten or touched in this pass and repeat the error. (don.contested.ministerial-purity has the same error but is outside this batch.)
- Fix: story text `and a town councillor named Ingentius`. tellable_as `A town councillor admits, under threat of torture, that he added false lines to a letter against him.` Demo `a town councillor, under threat of torture, admits that he added false lines to the letter used against a bishop.`

### B9. don.dw.silver-and-the-goods-of-the-poor - `text` and `positions[0]` - a "correction" that made the record less accurate, and an unjustified build-field edit
- Exact text (new): `Lucilla of Carthage was said to have given four hundred pieces of money.` ... `The sum appears in a complaint read into a court record before a consular official, years afterward.` positions[0]: `charged in a complaint read into a consular hearing`.
- Why: The editor's evidence stopped at Nundinarius's libellus. Later in the same Gesta, Saturninus and Victor are `brought in and sworn` (~l.6286). Asked `Do you know that the money was received from Lucilla?`, they answer `We do know it` (~l.6576-6581). Zenophilus then rules that `all the statements of Nundinarius are true` (~l.6590). The original "testified to under oath, in front of a consular official" was correct. The new "was said to have given" understates a Documented fact. The positions[0] change is a build-field edit with no real factual error behind it, so it is outside the brief. ("Silver" is not wrong either: the vendored translation itself says "four hundred pieces of silver" at ~l.6566. The Latin `folles` is neutral.)
- Fix: revert positions[0] to HEAD. Text: `Lucilla of Carthage gave four hundred pieces of money, and the bishop consecrated against Caecilian belonged to her own household. That was not an inference. Sworn witnesses confirmed the gift in front of a consular official, years afterward, and an opponent of ours recalled the same fact again decades later still.` (Optional: keep "That was not an inference" out if it is treated as a tell. The facts are what matter.) Re-grade.

### B10. Grade gate on touched story `text` fields - needs a ruling, not self-certification
- The brief says every touched spoken field must pass FK<=10 and FRE>=60. These touched story `text` fields fail after the edit:
  - acta-purgationis-felicis: 11.4 / 42.4
  - bagai-reconciliation: 14.9 / 41.0
  - conference-of-carthage-411: 11.2 / 62.8
  - lucilla-affair: 9.2 / 59.6
  - lucilla-consecration-dispute: 8.8 / 59.4
  - macrobius-letter-isaac-maximianus: 10.9 / 60.2
  - macrobius-letter: 13.3 / 53.8
  - passio-marculi: 12.0 / 58.0
  - tyconius-condemnation: 11.8 / 53.8 (slightly worse than HEAD's 11.7 / 55.5)
- All failed before this pass too. Most improved, and the edits were limited to factual corrections, as this review's rule 7 requires. The two rules conflict for long story texts. The lead should rule on one of two options. (a) Rewrite these story texts for readability, keeping every fact. (b) Log them as a known gap in Open_Gaps_Tracking.md with an ACCEPTED_OPEN entry. Either way, this should not be passed silently.

---

## NON-BLOCKING

1. don.story.gesta-apud-zenophilum `confidence.divergence_note` still says the record is "independently corroborated ... by a second primary source ... with no evident coordination". This pass's corrected text says Augustine drew on the same Acts and "is not a second, independent source". This is a factual error in a build field, and the brief allows a fix. Change the note to match the text.
2. don.dw.what-we-did-with-the-power-we-had `confidence.divergence_note` still says "the general who enforced it". The text now (correctly) says it was a bishop, Optatus Gildonianus.
3. don.dw.washed-for-the-first-time `divergence_note` and its Tyconius locus still say "the man our own council condemned" with no `perhibent` hedge. The text now carries the hedge.
4. Loci that still leak build vocabulary in records this pass touched: came-to-believe ("thin_topics:"), mostly-legend ("thinness and cautions 1: Author Gravity"), someone-like-me and woman-authority ("thin_topics:"), one-formation-aim ("G1's / G3's / G5's own ..."). These are inside brief item 3 and were missed.
5. don.demo.undiscovered-traditor `exchange[3]`: the claim that "the men who consecrated Majorinus... had admitted at Cirta" is Optatus's argument (I.14, I.19-20; line ~229) and is given without attribution. don.contested.cirta-reserved-to-the-lord concedes only that "several admitted responsibility". The record's `sources` still list only the Petilian quote and the gravity, so the new Silvanus and Cirta facts have no source card. Suggested wording: `Optatus, writing against us, says the men who consecrated Majorinus at Carthage had admitted at Cirta that they handed over the scriptures.` Add the Optatus and Gesta source rows.
6. don.demo.woman-authority `exchange[1]` keeps "She had a habit of kissing a martyr's bone" with no "it was said". Optatus I.16: `It was said that she kissed` / `libare dicebatur`. don.dw.becoming-one-of-us was hedged in this pass, so this is inconsistent across the world.
7. "Silver" or "money" for Lucilla's 400 `folles`. The dw silver record now says "money". don.dw.washed-for-the-first-time ("a wealthy woman's silver"), don.demo.power-against-dissenters and the gesta tellable_as say "silver". Both have support in the vendored translation, so pick one for consistency.
8. "A modern editor reports..." in don.witness.boundary-is-doctrine and don.dw.the-word-catholic-and-no-door-today. The editor is Mabillon, 17th century; don.contested.parallel-hierarchy says "seventeenth-century editor". "A seventeenth-century editor" would be more precise.
9. don.dw.what-belonging-cost: "Our sermon says that every year on the twelfth of March..." The sermon body says only that the anniversary is kept (`anniversalis dies ... celebratur`, pl8 ~l.546). The date "4 Idus Martii" is in the heading and Mabillon's note (~l.124, 229). Suggested: `Our sermon was preached on the yearly day of the Carthage dead, the twelfth of March.` The same record also keeps "his own congregation at Carthage", which the story records dropped. And "We never wrote down what held us together" states an absence too strongly; "No text of ours says what held us together" is safer. "Two hundred and seventy-nine of our bishops" is stated as settled, but don.story.conference-of-carthage-411 holds the counts open.
10. don.dw.older-than-the-schism `text`: "an earlier council at Carthage under Bishop Agrippinus". Cyprian (Ep. 71.4 / 73.3, cyprian_epistulae-lat_hartel1871 ~l.14273, 14548) names Agrippinus and the bishops of Africa and Numidia but does not say "at Carthage". Drop "at Carthage". The Agrippinus correction itself, and the build-field change that goes with it, are justified: Cyprian is in the record's cited sources, and Benson ~l.20140-20172 shows the date is uncertain.
11. don.demo.baptism-threshold `exchange[3]`: the tense pass went too far for the speaker's own present act. "What we gave you was what everyone... had crossed through" and "That was the day we could show you" should be "What we can give you is..." and "That is the day we can show you". The community's own past can stay in the past tense.
12. don.dw.who-decides-a-disputed-case: "We have no record of our own councils on its own terms" has a number mismatch ("its"). Suggested: `No record of our own councils survives in our own keeping.`
13. Consistency, low priority. don.dw.two-churches-in-one-town keeps "simply the church of the village" in a touched sentence; silver-and-goods replaced the same phrase with "the dominant church" as Frend-leaning. don.dw.the-emperor-and-the-church keeps "two of every office in every town"; the-creed-we-shared moved to "many". don.dw.walking-to-one-font (untouched text) and forgiving `positions` still say "a council of ours took back / restored" the two bishops; the demos now say "afterwards our party".
14. Leftover "not X, Y" pivots in touched fields: don.dw.who-decides "That was not an advisory board. That was a church governing itself." and not-a-death-wish "not that dying was the goal". These only went through a tense change, not a rewrite. Low priority.
15. Outside this batch (for the figure/contested reviewer). don.figure.macrobius and don.figure.maximianus-martyr still say the letter closes with "the same may be asked of any of them". don.contested.ministerial-purity calls Ingentius "the notary" and says he "forged the letter".

---

## Verified

Readability: every touched dw `text`, demo representative turn, and story `tellable_as` passes. The dw maximum is FK 9.47 and the minimum FRE 61.4. All demo turns pass, and all tellable_as pass with a minimum FRE of 61.3. Story `text` failures are listed at B10. Build fields (positions, tensions, divergence_note) were not graded.

Facts I checked myself in cic/texts (28):
1. Passio Donati VI: hands stretched out to the Lord, clubs not swords (`manus contra innocuas ad Dominum extensas armantur fustibus`). Correct in becoming-one-of-us, emperor-and-the-church and the passio-donati story.
2. Passio Donati VIII: eyes closed, and "many bodies" buried within the basilica walls (`corpora numerosa`). The story fix is correct.
3. Passio Donati II: `Caeciliano ... tunc instante, assentiente Leontio comite, duce Ursatio; Marcellino tunc tribuno`. The story fix ("the sermon says the bishop Caecilian pressed them on") is correct.
4. 12 March: found in the heading and Mabillon's note, not in the sermon body (see non-blocking 9).
5. Passio Marculi: ten bishops sent to Macarius "to recall him from his crime, or (as happened) to go first into the fight". The story fix is correct.
6. Passio Marculi: four days at Novapetra, with a fast closing the last day. The becoming-one-of-us and room-for-dissent fixes are correct; B7 is not.
7. Passio Marculi: `splendida nubes ... fulgore promicante` (bright cloud, flashes). The story fix is correct.
8. Macrobius: `corona` (crown), not ring, in the cup. Correct in both story records.
9. Macrobius: Maximianus himself strikes out the emperor's eye in the dream (`oculum violenter eliciens`), then is crowned by the youth. The story fix is correct.
10. Macrobius: Isaac cries `venite, salvate vestram unitatis insaniam`. Correct.
11. Macrobius: both men exiled and imprisoned, and Isaac dies in prison. Correct.
12. Macrobius: Maximianus sunk alive with the dead man; jars filled with sand; given back after six days (`post bis ternos dies`). Correct.
13. Macrobius closing: arms stretched out from heaven, "Properate". Correct where applied (B2, B3 and B6 are where it was not).
14. Optatus I.16: "It was said that she kissed a bone", and the martyr "if he was a martyr". Correct in becoming-one-of-us and the Lucilla stories.
15. Optatus I.17: Mensurius summoned to the court; "very many gold and silver ornaments"; some seniors; old woman given the inventory, to be handed on "if he did not return". Both Lucilla stories are correct.
16. Gesta: `quadringentis follibus` ("pieces of money" at ~l.6198, "pieces of silver" at ~l.6566).
17. Gesta: sworn witnesses confirm the money came from Lucilla (B9).
18. Gesta letters: not all end with "let no one know", so "several" is correct.
19. Gesta: Zenophilus says it is clear Silvanus was a betrayer, and Victor confirms. The undiscovered-traditor turn 1 is supported.
20. Augustine Ep. 43 (npnf101 ~l.28060) refers to the proceedings before Zenophilus. The gesta "not independent" fix is correct.
21. Acta Purgationis: Caecilianus's letter to Felix and the disowned closing lines; Ingentius's grief over Maurus his guest; Apronianus's Numidia charge and Ingentius's denial; Aelianus clears Felix. All correct. "Finally and triumphantly vindicated" is the translator's introduction (~l.5479), so its removal is correct. The "notary" label is wrong (B8).
22. Optatus III.3: Paul and Macarius sent as Constans's almoners; Donatus's retort. The refusal-and-recourse text and locus are correct.
23. Optatus III.3: the petition signed "of the party of Donatus" and turned into an accusation. The boundary-is-doctrine text is correct.
24. Augustine c. ep. Parm. I.1 (Petschenig ~l.2182-2184): Parmenian's letter, then `concilio eorum perhibent esse damnatum`. The Tyconius hedges are correct, and deleting Monceaux's "head of a schismatic church" inference is correct.
25. Cyprian Epp. 71/73: Agrippinus council, and Benson on its disputed date. older-than-the-schism is correct apart from non-blocking 10.
26. Augustine On Baptism II.11.16 (npnf104 ~l.11527): Felicianus and Praetextatus "whom they afterwards received". The bagai locus and "afterwards" are correct.
27. 411 acts (pl11 ~l.130306): Emeritus cites 1 John 4:5, "de mundo sunt, et mundus [eos] audit". The who-jesus "belonged to the world" line is supported.
28. Optatus Gildonianus as a Donatist bishop: supported by don.source.augustine-answer-to-petilian, don.contested.rigor-against-reception and don.figure.optatus-of-milevis. The general-to-bishop change in the demos, dw records and bagai story is correct.

Other checks:
- Tyconius hedges are now applied consistently across becoming-one-of-us, how-we-read, hypocrites, room-for-dissent, the-word-catholic, washed, what-we-argued and written-by-opponents. "Layman" became "man", which matches the story's open standing.
- Locus cleanup: file paths, line numbers, "vendored", "thin_topics:", "horizon:" and "SS" were removed in all the loci that were changed (B6 and B2 aside). The remaining leaks are listed in non-blocking 4.
- Story `text` edits are factual corrections only, each traced to a passage (log_story_demo.md), with no style rewrites.
- Build-field edits: the older-than-the-schism divergence_note and tensions[1] (justified), refusal-and-recourse positions[1] (justified: "that same emperor" pointed at Julian), and silver positions[0] (not justified, B9). No hedges were dropped in the justified ones.
- New tells: none serious. "Their line stayed our line" (undiscovered-traditor) is close to a coined closer but carries a claim; acceptable once attributed (non-blocking 5).

# Part B: figure, term, honest_limit, quote, ambient and build records, citations


Scope read: `git diff` of every changed record in those folders against HEAD, the four editor logs, citations.json/citations_notes.md, BRIEF.md. Read-only; nothing in the repo was edited.

## BLOCKING

### B1. don.figure.purpurius, `bridge_line`. The letter has the wrong addressee (the edit added this error)
- Text: "He wrote to his colleague Silvanus that the accusation was true and must be kept quiet."
- Why: In the Gesta apud Zenophilum (optatus_against-the-donatists.txt, Appendix, around l.6194-6300), Purpurius's letter *to Silvanus* only asks for peace "in order that no one may know what is going on between us". The words "What is contained in the bill of accusation is true" and "Be careful that no one knows the story of this conspiracy" come from his *other* letter, "Purpurius the Bishop to the Clerics and Elders of Cirta". The old text ("to a colleague") was vague. The new text names the wrong man.
- Fix: "He wrote to the clergy and elders of Cirta that the accusation was true and must be kept quiet." (Re-grade after the change. The current field is FK 5.5 / FRE 78.7, so it has room.)

### B2. don.figure.axido-and-fasir, `sources[0]`. The new locus does not match the source it is filed under
- Text: source_id `don.source.optatus-appendix-of-documents`, locus "Optatus, Against the Donatists III.4 - the passage naming Axido and Fasir, the killings at Octavum and the priest Clarius"
- Why: The locus itself is right. Optatus III.4 at l.2002 and l.2010 has Axido and Fasir, Octavum, and "the priest Clarus" (Latin "Clarius"). But III.4 is in Optatus's own Book III, not in the Appendix of Documents. The source card would therefore name the appendix ("Appendix of Documents (the anti-Donatist dossier) ...") with a Book III locus. That is a wrong citation on a participant-facing card.
- Fix: change source_id to `don.source.optatus-against-the-donatists` and keep the locus. Two build fields still describe the passage as "a Donatist petition ... reproduced in Optatus's appendix": `dates.display` and `confidence.divergence_note`. They now contradict the corrected locus and the new bridge_line ("The hostile writer who names them"). Log them in Open_Gaps (see Out of scope below). `dates.display` should probably be fixed in the same edit if it shows to participants.

### B3. don.ambient.doubled-towns, `detail`. The edit puts back a physical claim it was meant to remove, and makes it stronger
- Text: "In many towns of Roman North Africa, two churches stood side by side."
- Why: log_build.md says the original was rewritten because "within sight of one another ... the same street" was invented. The cited source (Optatus: rival chairs and altars, town for town) has no physical layout. "Stood side by side" says the buildings were next to each other in every such town, which is stronger than the original "sometimes within sight". It also clashes with don.limit.the-room-we-cannot-show-you ("No one has dug it ... no site, no plan, no floor").
- Fix: "In many towns of Roman North Africa, there were two churches where there should have been one." Alternative: "In many towns of Roman North Africa, there were two rival churches." Re-grade after the change.

## NON-BLOCKING

1. **don.figure.isaac `bridge_line`, "come and heal their madness of unity".** The PL8 text (l.1640-1642) reads "Traditores, venite, salvate vestram unitatis insaniam", with the Corbie manuscript reading "satiate vestram crudelitatis insaniam". "Salvate" can be heard ironically ("come, save your mad unity"), and "heal" softens that. But don.story.macrobius-letter and don.story.macrobius-letter-isaac-maximianus already render it "heal" / "be cured", so the field is consistent with the world. Leave it, or align all three in a later pass. The figure body still says "the people holding the whips were the traditores" (out of scope; body prose).
2. **don.term.agonistici `quick_meaning`, "This is what Augustine says the country folk called themselves".** In Enarr. in Ps. 132.6 (augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt l.123418-123424) the Donatist speakers say "Agonisticos eos vocant ... Sic eos appellamus". So it is the party naming the group, not the group naming itself. The we-voice `plain_meaning` ("some of us ... called ourselves") is acceptable. The third-person quick_meaning is slightly loose. Suggested fix: "Contestants. Augustine says our side called the country folk this; their foes had another name."
3. **don.term.episcopus `sources[3].locus`, "...the physical evidence for a doubled church order in Numidia is undone".** "Evidence ... is undone" does not make sense. Suggested fix: "no excavation or site report is named for a doubled church order in Numidia".
4. **don.term.purity-ministerial `plain_meaning`.** The quotation "'What we look for is the conscience of the giver, to cleanse that of the recipient.'" no longer matches don.quote.petilian-conscience-of-the-giver `modern_rendering` (now "...to cleanse the conscience of the one who receives"). It does match the NPNF English, but drops "(him who gives in holiness)" with no ellipsis. It is acceptable as a quotation of the translation. Matching the rendering would be tidier.
5. **don.figure.constantine `bridge_line`, "For a century after that, we refused to accept him as a judge".** "Him" now points to Constantine, who died in 337. Suggested fix: "...we refused to accept the emperor as a judge of the church at all."
6. **don.core.donatism horizon, "Four of his letters ... They name Donatist rebaptism in Africa".** Of the four, only II.46 (Turchi l.11740 "a Donatistis denuo baptizari") and IV.32 (l.11908 "rebaptizare") name rebaptism. IV.35 speaks of "Donatistarum stimulos". Suggested fix: "Two of them name Donatist rebaptism ...". This is a build record, so the edit should be the minimal factual one.
7. **Mild tells, not worth a round on their own.** don.term.pars-donati `senses.personal` closes with "our enemies held the pen", which echoes don.term.deo-laudes "no enemy holding the pen" and works as a coined closer. don.term.liber-regularum `senses.personal` opens with an aphorism ("A movement shows what it is by how it treats a thinker it produced and did not accept."). don.term.concilium `senses.personal` mixes tense ("They are also where our sharpest inconsistency played out").
8. **Citations: style only, nothing wrong.**
   - Duplicate source pairs carry differently formatted citations, for example "Series I, vol. IV" against "1st series, vol. 4 ... ed. Schaff", and "R. Cagnat" against "Rene Cagnat".
   - don.source.gregory-the-great-register-of-letters reads "via the Turchi themed selection (1907)", which is slightly build-flavoured but taken from the fields.
   - don.source.numidian-basilica-archaeology ("Numidian basilica archaeology, general") and don.source.ebbeler-augustine-epistolography ("Jennifer Ebbeler, work on Augustine's epistolography") are honest but name no work.
9. **log_term_limit.md is wrong about three fields.** It reports them still below the gate: agonistici plain_meaning and quick_meaning, and liber-regularum quick_meaning. On the current text all three pass (FK 6.8/FRE 60.1, 6.5/63.8, 4.7/76.6). Correct the log; no record change is needed.

### Out of scope: log, don't fix in this pass
- don.figure.axido-and-fasir `dates.display` and `divergence_note` still say "Donatist petition ... in Optatus's appendix". That contradicts the corrected locus (see B2).
- don.figure.isaac body: "the people holding the whips were the traditores". The Latin has Isaac crying out to the traditores, with the proconsul then hunting for who shouted. It does not say the floggers were the traditores.

## Verified

**Mechanical checks**
- All 236 don records parse with engine.m1.loader.parse_record_file. No failures.
- I graded every changed spoken field in my folders with grade_text: figure bridge_line, term plain/quick/personal/translational, limit statement, quote modern_rendering, ambient detail. All pass FK<=10 / FRE>=60. Only two scholarly `names[1].name` labels fall short (donatus FRE 59.6, optatus-of-milevis FRE 26.7), and those are labels, not prose.
- Every non-locus change in force, gravity, contested_claim, voice_craft and world_core is a factual correction backed by a named passage. None is a style rewrite, and none drops a hedge. The changes: Gregory Numidia/Africa; Mabillon admonitio vs sermon IX; Honoratus / "on Monceaux's reading"; Liber genealogus "assumed"; Gildonianus as bishop; Marculus vision "in the night before"; Tyconius survival mechanism "not resolved". Where hedges changed, they got stronger, for example "as one reading has it" in fidelis-voice and "Mabillon dates the persecution to about 340".
- The source/ diff contains only the 76 added `citation:` lines.
- The forbidden-pattern regex finds 0 hits in all 76.
- A word-provenance script checked all 76 against author/work/edition. The only words not found in those fields are connectives (ed., trans., in, on) and possessive forms of names that are in the fields (Lucilla, Augustine, Burkitt). No first name, initial, date or publisher was added beyond the record's own fields. I read 30+ closely.
- Quote `text` is unchanged in all four quote records.
- Renderings: Petilian (every clause, "For" restored, FK 8.1/FRE 72.1) and Emeritus ("trick" for argumentum = device/ploy, "so that" for ut, FK 4.2/FRE 89.9) are both accepted.

**Vendored-text spot checks (24)**
1. Isaac's cry, PL8 l.1640.
2. Marculus vision on the last night before Sunday, PL8 l.1049-1121 ("shortly before" is correct).
3. Mensurius "seniors", "is said to have", Optatus I.17 l.203.
4. Axido/Fasir, Octavum, Clarus, Optatus III.4 l.2002-2010.
5. Purpurius's letters to Silvanus and to the Cirta clergy (this check found B1).
6. Purpurius's taunt "set free by them", l.7308.
7. Secundus's "Sit down", l.7324.
8. Lucilla's bone, "it was said", archdeacon Caecilian, I.16 l.199.
9. "some other woman", Letter 43, npnf101 l.28385.
10. Mandate list "Primiano, Petiliano, Emerito...", Collatio l.122190-122196.
11. Collatio ch. 265/267/272: Augustine speaks.
12. Collatio ch. 144: Marcellinus offers seats.
13. CIL 17732/17368/18669/20482, with 20482 as "fragmentum epistylii".
14. Petilian's proposition in Prolegomena ch. II, npnf104 l.10280, div title confirmed.
15. Shores decree in Contra litteras Petiliani I.10, npnf104 l.15512.
16. Gregory II.46: bribed bishop, heresy "cotidie dilatari", rebaptism.
17. Gregory IV.32 to Pantaleon: Africa, "rebaptizare".
18. Gildonianus as Donatist bishop, npnf104 note l.11513.
19. Honoratus of Sicilibba, sermon VII, PL8 l.526.
20. "anniversalis dies religiosa devotione", sermon IX, l.541.
21. Mabillon "circa annum 340, aut paulo post", l.185.
22. Monceaux T5 "12 mars 317".
23. Enarr. Ps. 132.6 agonistici.
24. Optatus III.3 "party of Donatus" in court proceedings and in the petition, l.1954.

**Contradiction checks**
- "Casae Nigrae" appears in no other don record, so the donatus name change contradicts nothing.
- The "heal" rendering matches both Macrobius story records.
- The deo-laudes count of four matches the-room-we-cannot-show-you.

## Resolution of part A item B10

Story `text` is excluded from readability grading by the gate itself (`_READABILITY_EXCLUDED_FIELDS` in `engine/m1/gates.py`). Story `text` fields were changed only where the vendored source contradicts them, so item B10 needs no ruling and no waiver. The blocking items B1 to B9 of part A and B1 to B3 of part B were fixed before round 2.
