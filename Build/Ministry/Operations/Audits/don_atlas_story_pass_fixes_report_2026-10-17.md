# Donatist Atlas story pass: fixes after independent review

Branch `site/atlas-story-don-fixes`, from `origin/main` at 5686bf5f9f. Not pushed.
- Commit 8afababd9 holds the review fixes: the story, cards, highlights and tellings.
- Commit bcdd55fbb holds the widened scope: the rest of the world front, plus removal of the commentary bodies. See "Second commit" at the end of this report.

Items 5 and 6 under "Record defects" were fixed in the second commit.
Worktree: /home/user/CIC-Project/.claude/worktrees/agent-a7199f86b9cdac231

Files changed:
- `Build/worlds/don/surface/world_front/don.front.donatism.md`: `orientation.story`, `documented_stories`, `highlights`
- The `telling:` line of the nine story records in `records/don/story/`

Gates: `python -m engine.m10.cli records don` PASS. `python -m engine.m10.cli regate don --base origin/main` PASS. The first regate run failed on 11 short notes and teasers (FRE below 60). I fixed them by using simpler words and kept every fact.

The project lead's mid-task ruling ("remove all the add on tails that dont say anything") is applied throughout. The tails I removed are listed in their own section below.

---

## BLOCKING

**B1. ACCEPTED.** No don record says "Nicene". `don.dw.the-creed-we-shared` supports "the same Latin words".
- Before: "Both confessed the same Nicene faith, word for word." Highlight phrase: "Nicene faith".
- After: "Both held the same faith in the Trinity and in Christ, in the same Latin words." The highlight phrase is now "the same faith", with the note "The faith in the Trinity and in Christ held across Latin North Africa. Both churches confessed it in the same Latin words. They split over which bishops were valid." Added `don.dw.the-creed-we-shared` to `grounded_in` for unit 1 and for the highlight.

**B2. ACCEPTED.** `don.force.vandal-capture-of-carthage` says 439 "does NOT end the two-party contest".
- Before: "From around 311 until 439, two rival churches stood side by side…"
- After: "From around 311, two rival churches stood side by side in Roman North Africa, centered on Carthage and Numidia. This account follows them to 439."

**B3. ACCEPTED.** `don.term.pars-donati`: "Optatus says they used the phrase whenever they were questioned in court."
- Before: "…after an early bishop, though nothing suggests they chose that name."
- After: "History calls its members Donatists, after an early bishop. In court, its bishops called themselves 'the party of Donatus'." Added `don.term.pars-donati` to `grounded_in`. I left out "what they called themselves among themselves is not known". The ruling cuts what-we-don't-know lines, and "in court" already limits the claim, so it does not breach `not_for` ("settled self-description").

**B4. ACCEPTED.** `don.force.diocletianic-persecution-traditio-demand` says the scriptures and vessels were handed over "to be destroyed". It mentions no death penalty.
- Before: "Officials demanded that clergy hand over the scriptures or die."
- After: "Officials demanded that clergy hand over the scriptures and the church's vessels to be destroyed."

**B5. ACCEPTED.** The vision was stated as fact, which `divergence_note` and `not_for` forbid. "Four days of fasting" has no support. The record's `text` says he was held four days and "in that waiting… fasted". Its `tellable_as` says "after a day of fasting".
- Before: "Bishop Marculus, after four days of fasting, was shown a cup, a crown and a palm, then thrown from a cliff called Novapetra."
- After: "The church's own account says that Bishop Marculus was held four days at a cliff called Novapetra. There he fasted and was shown a vision of a cup, a crown and a palm. Then he was thrown down." No length of fast is given, so the sentence is true to both fields. The defect is logged below.

**B6. ACCEPTED IN PART.** `don.force.macarian-repression` names an earlier persecution under Leontius and Ursacius. Note that `don.core.donatism` `formation_logic` itself calls the Macarian repression "the second" persecution, so the original wording copied the core. I did not adopt the reviewer's "worst" or "most of the martyrs it remembered by name" because no record states either superlative.
- Before: "Persecution came a second time in 347 and 348… It gave this church the martyrs it remembered."
- After: "Persecution came again in 347 and 348. This time it came at the rival church's urging, through the emperor's commissioners." The sentence claiming these were all its martyrs is gone. Added `don.force.macarian-repression` to `grounded_in`.

**B7. ACCEPTED.** The gravity record shows that the three recourses come from Optatus's appendix and from Augustine. I did not use the reviewer's "the record shows", because "record" as meta-language is banned in participant text.
- Before: "Still, its own texts admit exceptions. Three times it turned to the state…"
- After: "Still, three times they turned to the state when that served their case."

**B8. ACCEPTED, with changes.** `don.force.conference-of-411-verdict`: "It ruled against the Donatist party. Sustained penal legislation followed." The story record's own tier justification also says "the proceeding was decided against us". I did not use the reviewer's "in 412". That year appears only in a `sources.locus`, not in any narrative field.
- Unit 7, before: "Then he ruled that an imperial rescript had already given the name to the other side."
- Unit 7, after: "Then he said he was bound by an imperial rescript that had already given the name to the other side. He ruled against the Donatists, and penal laws against them followed." Added `don.figure.marcellinus` and `don.force.conference-of-411-verdict`.
- Highlight, before: "…The judge Marcellinus ran it. The record stops before any verdict."
- Highlight, after: "A court hearing in 411, held on the emperor's orders to end the quarrel. The judge Marcellinus ran it, and he ruled against the Donatists." Added the force record.
- Telling, before: "The verdict is not in what we have, because the acts break off before any sentence is given."
- Telling, after: "In the end Marcellinus ruled against us, though the acts we have break off before his sentence." The hedge stays attached to the claim, as `not_for` requires.

**B9. ACCEPTED, with different wording.** "Not a churchman of either side" means he was not a cleric. The reviewer's "Catholic layman / City of God" comes from outside the records, so I did not use it.
- Before: "He belonged to neither church."
- After: "He was the emperor's officer, not a cleric of either church."

**B10. ACCEPTED.** `don.figure.donatus`: "until c. 347; exiled after the Macarian repression and dead in exile."
- Before: "Primate at Carthage from about 313 until his death in exile about 347."
- After: "Primate at Carthage from about 313. He was exiled about 347 and died in exile."

**B11. ACCEPTED.**
- Highlight, before: "That ended the Roman state that this church had defined itself against."
- Highlight, after: "That took away the Roman power that had judged the Donatists and used force on them."
- Unit 8, before: "That ended the Roman rule this church had defined itself against. The contest went on under the Vandals, and then under the Eastern empire."
- Unit 8, after: "That removed the Roman power the Donatists had defined themselves against. The contest went on under the Vandals, and then under the emperors of the East." Added `don.force.vandal-capture-of-carthage`.

**B12. ACCEPTED.** Core caution 2 counts the 411 transcript as Donatist voice.
- Before: "Its own voice survives in four short texts, and in two words cut into pillars near Bagai…"
- After: "Their own voice survives in four short texts and in their bishops' words at the hearing of 411. It survives too in two words cut into pillars near Bagai, Deo laudes, praise to God."

**B13. ACCEPTED.** This breached the `not_for` of `don.term.traditor-traditio`. The sentence is gone. Under the tail ruling the whole closing comment was cut, and the Optatus attribution now opens the telling ("We know of the meeting only through Optatus, our opponent."). The word "traitors" no longer appears.

**B14. ACCEPTED.** "Without a word" claims a silence that `absent_detail` calls unknown.
- Before: "Condemned as Shipwrecked, Then Taken Back Without a Word"
- After: "Condemned as Shipwrecked, Then Taken Back as They Were"

## SHOULD-FIX

**S1. ACCEPTED.**
- Before: "The emperor later had the charge against Felix tried, and Felix was cleared."
- After: "The emperor later had the charge against Felix tried. Under threat of torture, a witness admitted forging part of the evidence, and Felix was cleared."

**S2. ACCEPTED.**
- Before: "When it ended, Caecilian was elected…"
- After: "In 311 or 312, Caecilian was elected bishop of Carthage." Added `don.core.donatism`.

**S3. ACCEPTED.** `don.term.rebaptism`: "We did not think of this as baptizing twice."
- Before: "never called it a second baptism"
- After: "The Donatists did not count it as a second baptism."

**S4. ACCEPTED.**
- After: "A hand from a broken line had given nothing the first time. So their font gave a convert the first real baptism of their life."

**S5. ACCEPTED.**
- After: "The imperial judge offered them chairs, and they refused. Christ had stood before his governor, said Petilian, one of their spokesmen, and so would they."

**S6. ACCEPTED.** The story `divergence_note` (3) holds 279/286 open against the roll-call tally of 266 + 20. Under both counts the other side is larger.
- Unit 7, after: "about two hundred and eighty Donatist bishops faced a slightly larger number from the other side."
- Teaser, after: "Bishops refuse the chairs a judge offers them. For three days they argue before a judge bound by an order that already calls the other side Catholic."

**S7. ACCEPTED.**
- Title, before: "Three Days Standing Before a Judge Already Told Who Was Right"
- Title, after: "Three Days Standing Before a Judge Bound by the Emperor's Word"
- Teaser: see S6. Added `don.figure.marcellinus` to the card's `grounded_in`.

**S8. ACCEPTED.** `when: "1-8 June 411"` is now `when: "June 411"` (from `don.figure.marcellinus`).

**S9. ACCEPTED.**
- After: "Three hundred and ten bishops condemn a breakaway group as shipwrecked men. Later their church takes two of its bishops back, and does not baptize or ordain them again."

**S10. ACCEPTED.** `use_note.years` is 393–398. The force record dates the reception "afterward".
- `when` after: "393 to 398 (the Cebarsussi rupture in 393, the Bagai council in 394, the return of two bishops afterward)"
- Telling: "Within a few years" is now "Later" (matching `tellable_as`).

**S11. ACCEPTED.**
- After: "A Roman official puts named witnesses under oath. Bishops' letters are read aloud. One admits the charge was true, and several beg that no one find out."

**S12. ACCEPTED.**
- After: "The story of the rebuke comes only from the man who blames her."

**S13. ACCEPTED.** Only Monceaux, via `don.term.liber-regularum`, calls him a layman.
- Title, after: "The Writer Who Argued the Church Reached the Whole Earth". The teaser now reads "A writer argues…"

**S14. ACCEPTED.**
- After: "It was the same charge we would soon bring against Felix, the bishop who made Caecilian."

**S15. ACCEPTED.**
- After: "Secundus then asked the three bishops who had not been accused for their judgement. They were Victor of Garba, Felix of Rotarium and Nabor of Centurio."

**S16. ACCEPTED, resolved by removal.** The ambiguous "said instead" sentence was part of the closing tail, which the ruling cut. The torture hedge stays inline: "Under the threat of torture, he broke."

**S17. ACCEPTED, resolved by removal.** The merged-witnesses sentence was the closing tail, and it is cut. The two hostile witnesses are no longer described, so they cannot be merged. The testimony hedges stay inline ("the account says", "we hold", "we say").

**S18. ACCEPTED.**
- After: "We hold that his body did not break in the fall. It came down gently, we say, as though something carried it."

**S19. ACCEPTED.** The sentence was the closing tail and is cut. The telling now ends on "He was never received back, and he never went over to the other side." Note that the record's own `modern_contrast` says "a man we cut off", which sits against its `divergence_note`. This is logged below.

**S20. ACCEPTED.**
- After: "Those who had left that communion, his own party among them, had broken away from something real."

**S21. ACCEPTED.**
- After: "He would not let the court touch the case itself until it had settled the day, the mandates and who was bringing the charge." Then: "Each time, he signed the notary's record of his words and added that he kept his right to appeal. So he put his name to his words while refusing the court that recorded them."

**S22. ACCEPTED.** This matches the `don.figure.isaac` bridge line, given as indirect speech per `divergence_note`.
- After: "He called his floggers traditores, men who had handed over the scriptures, and told them to come and heal their madness of unity."

**S23. ACCEPTED, resolved by removal.** The line was the closing tail and is cut. The telling ends on Majorinus's consecration.

**S24. ACCEPTED.** See "Structure" below.

**S25. ACCEPTED.**
- Before: "The record closes in 439…"
- After: "This story ends in 439…" The two closing sentences were cut under the ruling.

**S26. ACCEPTED IN PART.** The unit cites `don.dw.two-churches-in-one-town`, which does say "in Numidia we were the ordinary church of the village rather than a minority". So the claim was grounded and does not import the Frends thesis. I removed "simply" and added the core's neutral statement.
- After: "In Numidia it had far more people than its rival. There it was the ordinary church of the village." Added `don.core.donatism`.

**S27. ACCEPTED for clumsiness, REJECTED on "overstated".** Augustine drew on the Acts. That shows he knew them, not that the text reaches us through him. The transcript survives in Optatus's appendix (story `divergence_note`).
- After: "Optatus, our opponent, kept the court record among his documents. He kept it because it hurts us."

**S28. REJECTED.** No don record calls the proconsul a governor or says he governed Africa. The records give only that a proconsul ran the Felix inquiry and tried Isaac and Maximianus. The reviewer's wording would add a fact that is not in the records. The note stays as it was. If a record gains that fact, the note can follow it.

**S29. ACCEPTED.** "This church" now appears 0 times in the highlights (was 15) and 0 times in the main story (was 8). The narrator uses "the Donatists", "they" or "its bishops" instead.

**S30. ACCEPTED.** I turned the question into reported speech instead of using the reviewer's colon reveal.
- After: "Optatus, who wrote against the Donatists, reports that their bishop Donatus once asked what the emperor had to do with the church." Added `don.figure.optatus-of-milevis`.

**S31. ACCEPTED.**
- After: "A council called and enforced by a state that already favored their rival was not, in their view, the church judging itself."

## NIT

- **N1. ACCEPTED.** "Where Marculus was held four days at a cliff and thrown from it. The place is probably…"
- **N2. No change.** The reviewer says the wording is fine.
- **N3. ACCEPTED.** "the hearing at Rome" in unit 6 and in the highlight phrase.
- **N4. ACCEPTED.** "…forced the Donatists into union with their rival in 347 and 348. At times they killed."
- **N5. ACCEPTED.** No serial comma throughout ("a cup, a crown and a palm") in the title, teaser and story.
- **N6. ACCEPTED, with different wording.** The telling says "It gives a day but no year." I did not use "feast day", which would be an interpretation.
- **N7. ACCEPTED.** The aphorism is cut. Unit 9 ends on "Deo laudes, praise to God."
- **N8. ACCEPTED.** "centered on Carthage and Numidia".

---

## Tails removed under the project lead's ruling

- Cirta: "Optatus tells it to show our founders as traitors excusing one another, and we have nothing from that room to set against his reading. No one on our side wrote down what 'reserved to the Lord' meant…" The telling now ends "No one was found guilty, and no one was cleared."
- Lucilla: "Optatus blames the whole split on her wounded pride, but that explanation is his, and we do not adopt it. Lucilla left no text, and no one asked her what she thought she was doing." The motive is now attributed inline ("In his telling, the elders, the two passed-over men and Lucilla now found a common cause"). The telling ends on Majorinus's consecration "at her urging and through her bribes, Optatus writes."
- Acta: "This record survives because Optatus… kept it… Even so, the inquiry did not find in our favor. Our tradition said instead… No account of this inquiry from our own side survives." The telling ends "The proconsul ruled that nothing had been proved against Felix, and he cleared him." The provenance moved inline to the middle.
- Gesta: "Silvanus himself is never questioned in what survives, and no answer of his is on the record." The telling ends on Victor's "He was a betrayer."
- Passio: "This is the tradition's own testimony, and no outside witness confirms… Our opponents say only that he was killed…" The telling ends on the burial.
- Macrobius: "No record survives from the proconsul's side, and no independent notice of the deaths." The telling ends on "He urges the living to hurry after them."
- Tyconius: "His Book of Rules outlived our party… after we had cut him off." Also cut: "No account of them from our own side survives" and "No act of that council survives, so what followed… is less certain." The "it is reported" hedge stays on the claim.
- Bagai: "We never hid the exception, but we do not know what was said in the room. Nor do we know whether anyone there named the contradiction out loud." Also the opener "Apart from that decree, no account… survives." The telling ends on Augustine's argument.
- Conference: "The verdict is not in what we have…" This became the verdict sentence with an attached hedge (see B8).
- Main story, unit 2: "This church never accepted that one hearing could settle the whole dispute."
- Main story, unit 4: "It gave this church the martyrs it remembered."
- Main story, unit 8: "After that, the record goes silent. No line from it to any church alive today has ever been shown."
- Main story, unit 9: "No hostile hand stands between those words and a modern reader."
- Highlight `Conference of Carthage`: "The record stops before any verdict."

## Structure (S24)

- **Openings now differ.**
  - Cirta: "Before the quarrel over Caecilian began…"
  - Lucilla: "She kept the bone of a martyr with her…"
  - Acta: "At the center of the case lay a letter…"
  - Gesta: "In 320 a Roman official…"
  - Passio: "We remember Marculus…"
  - Macrobius: "Maximianus, a soldier of Christ…"
  - Tyconius: "Tyconius argued at length…"
  - Bagai: "In 393 a deacon…"
  - Conference: "The judge sat, and our bishops stood."
- **Provenance is placed where it bears on the scene.** It sits at the end of the first paragraph in Cirta and Gesta, in the middle of the story in Acta and Tyconius, and in the middle of the decree in Bagai. "Who wrote against us" now appears only twice (Lucilla, plus "writing against us" in Tyconius). The other cards use "our opponent" or "in his books against us".
- **Shapes vary** from 3 to 5 paragraphs, and lengths run from 169 to 248 words.
- **Every telling ends on its own last event.**
- **Distinctive lines restored:**
  - Purpurius's "Let his head be well beaten in penance"
  - Purpurius's flame that "could not be put out without spiritual bloodshed"
  - Victor's "He was a betrayer"
  - the crown shining "with the colors of blood and light"
  - Maximianus striking out the emperor's eye in the dream
  - Isaac's "madness of unity"
  - Petilian's "We do not blush and we do not fear"
  - Emeritus's day, mandate and persons
  - the appeal reserved

## Tellings changed

All nine: council-of-cirta, lucilla-affair, acta-purgationis-felicis, gesta-apud-zenophilum, passio-marculi, macrobius-letter, tyconius-condemnation, bagai-reconciliation, conference-of-carthage-411.

## Main story changed

Yes, all nine units. `grounded_in` was extended on units 1, 2, 4, 5, 6, 7 and 8.

## Word counts and readability

Scored with `engine.m1.fk`. Sentence length was measured by a split on terminal punctuation.

| Unit | Words | Avg sentence | Max sentence | FK | FRE |
|---|---|---|---|---|---|
| Main story | 696 (was 662) | 12.4 | 22 | 7.0 | 67.2 |
| council-of-cirta | 202 | 11.9 | 21 | 6.5 | 69.5 |
| lucilla-affair | 226 | 13.3 | 25 | 6.8 | 69.8 |
| acta-purgationis-felicis | 186 | 13.3 | 22 | 8.2 | 60.1 |
| gesta-apud-zenophilum | 215 | 11.3 | 25 | 5.9 | 72.0 |
| passio-marculi | 177 | 13.6 | 23 | 6.4 | 73.5 |
| macrobius-letter | 236 | 13.1 | 23 | 6.2 | 74.2 |
| tyconius-condemnation | 177 | 14.7 | 23 | 7.0 | 71.3 |
| bagai-reconciliation | 169 | 14.1 | 22 | 7.8 | 63.9 |
| conference-of-carthage-411 | 248 | 13.8 | 24 | 6.6 | 72.1 |

Most units score below FK 8. The regate reports this ("40 edited fields below FK 8") but does not fail on it. CLAUDE.md treats grade 8 as a floor worth staying above, so a reviewer may want to look at this. The low grade comes from short sentences, not from simplified substance. No fact was dropped to reach it.

## Record defects to log in `Build/worlds/don/Open_Gaps_Tracking.md`

These are not fixed here.

1. **`don.story.passio-marculi` contradicts itself.** `tellable_as` says "after a day of fasting". `text` says he fasted during the four-day wait at Novapetra. The figure record `don.figure.marculus` and the front's Marculus voice entry ("in the fast") follow `text`. The new telling and story give no length of fast.
2. **`don.story.tyconius-condemnation` has a tension between two fields.** `modern_contrast` says "a man we cut off and never took back". `divergence_note` and core caution 9 leave his formal standing open.
3. **`don.story.conference-of-carthage-411` states the count flat.** `use_note.means` gives "279 Donatist bishops faced 286" as settled, while its own `divergence_note` (3) holds the count open. `don.force.conference-of-411-verdict` and `don.gravity.parallel-institutional-hierarchy` also state 279/286 flatly.
4. **`don.core.donatism` `formation_logic`** calls the Macarian repression "the second" persecution. That erases the Leontius and Ursacius persecution, which `don.force.macarian-repression` names.
5. **Fields of the same front record outside this pass's scope carry the same defects the review found.** They were not touched:
   - `skim.tile`: "Between 311 and 439" (see B2), "When persecution came a second time" (B6), and "Four short texts, and two words… are what survive in its own voice" (B12).
   - `voices` (Donatus): "nothing suggests his own people chose that name" (B3).
   - `voices` (Tyconius): "A layman" (S13) and "was cut off for good" (S19).
   - `legacy`: "survived the council that condemned its own author" drops the "reported" hedge.
   - Several of these fields use "this world" in participant text.
6. **The front record's body (lines after the closing `---`) is build commentary in a canonical file.** CLAUDE.md's live-surface rule says a PR that edits such a file should also remove its commentary (`tools/check_live_commentary.py`). It is outside this task's file scope and was left in place. The PR for this branch needs to decide it.

---

## Second commit (bcdd55fbb): widened scope

Gates after this commit:
- `records don`: PASS
- `regate don --base origin/main`: PASS. The edited fields that failed at the base now pass, including `read_first[2]` and `who_speaks`.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0. It reports 0 REWRITE and 0 ROUTE. Its 8 KEEP hits are the `verified_on` ISO dates on the place highlights.

The same rules apply throughout: no fabrication, hedges kept, no "this world", no dash asides, and no add-on tails.

### Front file, by section

**`skim.tile`**
- Fixed B2. It no longer says "Between 311 and 439". It now opens "From around 311".
- Fixed B6. "When persecution came a second time" is now "Persecution came again, at the rival church's urging."
- Fixed B12. "Four short texts, and two words… are what survive" is now "Its own voice survives in four short texts, in its bishops' words at the hearing of 411, and in two words cut into stone."
- "Said so plainly in the same breath as the refusal" was cut. No record has the Donatists saying this; the gravity record says "no source shows the Donatists themselves describing the tension". The tile now says they "turned to the emperor's power" three times.
- Added to `grounded_in`: traditor and rebaptism terms, the Macarian force, the martyr-cult and refusal/recourse gravities, and `don.quote.deo-laudes`.

**`voices` Donatus**
- Fixed B3. "Nothing suggests his own people chose that name" is gone.
- His question is now reported by Optatus in the setting the quote record gives: imperial almoners at Carthage offering aid.
- "Exiled after the repression under Macarius, and he died there" matches the dates of B10.
- Hedge: Monceaux's guess about the March sermon is kept as a hedged guess, now in plain words.

**`voices` Petilian**
- "This world's fullest surviving voice" is now "More of his words survive than of any other Donatist".
- The dash aside is gone. The chair refusal is attributed to him: "Christ himself, he said…"
- Hedge kept: letters filtered for what could be answered; the 411 copy is damaged.

**`voices` Emeritus**
- S21 jargon removed. "Procedure before its substance" and "appeal reserved" became plain wording, matching the 411 telling.
- Hedge kept: about 1,900 of 144,733 lines read; the 418 debate is unread.

**`voices` Marculus**
- Fixed the B5 recurrence. "Where he was shown, in the fast, a vision" had stated the vision as fact. It is now "His church's own account says he fasted there and was shown a vision…"
- Hedge kept, with the two hostile witnesses held apart (S17): Optatus calls it a just punishment; Augustine says the word martyr does not apply.

**`voices` Tyconius**
- Fixed S13. "A layman" is gone; he is now "a Donatist writer and preacher". This follows `don.figure.tyconius`.
- "The one systematic theologian this world produced, and the one it silenced" is now "the one Donatist thinker whose own book survives entire". That wording follows the `don.figure.tyconius` bridge line, per gaps entry OG-31.
- Fixed S19. "Was cut off for good" is now "It is reported that a council of his own church then condemned him."
- Hedge kept: the 1920 study, the "it is reported" hedge and his open standing.

**`floor_note`**
- "Confessed the same faith the councils of its own century put into words" was the Nicene-adjacent claim (B1). `don.dw.who-decides-a-disputed-case` says the doctrinal councils "do not appear in our own record".
- "Heretic on none" was false. It is gaps entry OG-23 item 12: `don.dw.the-creed-we-shared` says Augustine called them heretics from about 400, and the law of 405 placed them beside the Manichaeans.
- The note now says this, plus Augustine's 417 statement that most of them held the same faith.

**`legacy` [0]**
- The condemnation now carries its hedge: "A council of his own party is reported to have condemned him."
- "Generations of readers after him" was dropped as not in the records. The note now says "shaped how Augustine read Scripture" (`don.term.liber-regularum`).
- The tail "a transmission… does not explain" was cut.

**`legacy` [1]**
- Kept as a fix of the 439-as-end claim.
- "Still legislated against" was dropped; no record says this for the Vandal and Byzantine period.
- Cut: "simply falls silent" and the "Living Tradition Status" jargon.
- Kept as content: "No line… to any church a person could visit today has ever been shown."
- Added `don.force.vandal-capture-of-carthage`.

**`relations_summary`**
- "The same Constantine this world petitioned once" contradicted the three recourses (B7). It now says "asked for help in 313, and then refused as a judge".
- The tail "Neither comparison is a claim…" was cut.

**`sourcing`**
- "Numidian basilica archaeology remains honestly undone" repeats the error in gaps entry OG-23 item 9: churches were excavated, and what is missing is a report among the sources. It now says "No report or plan of the Numidian churches… is among the sources."
- The 411 transcript is now counted as Donatist voice.
- The Circumcellion question is kept open.

**`read_first` notes (3)**
- Dash asides and "this world/this communion" removed. The OCR caution is kept.
- `read_first[2]` failed readability at the base and now passes.

**`narrative.who_speaks`**
- Removed "Tyconius, the one theologian this world produced, was silenced by his own side".
- The Marculus vision is now framed as "His church remembers…"

**Body below the frontmatter**
- Deleted: the build narrative, the judgment calls and three fleet findings, about 320 lines. The text stays in git history at 8afababd9.

### Story records

**Nine bodies deleted.** Each began "Compiled from World-Builds/…" (the 411 record began "NEW AT B-4…"). Removed sizes in characters:

| Record | Characters |
|---|---|
| cirta | 1,128 |
| lucilla | 1,534 |
| acta | 1,054 |
| gesta | 1,867 |
| passio | 1,355 |
| macrobius | 977 |
| tyconius | 1,255 |
| bagai | 1,698 |
| conference | 4,217 |

**Cirta telling, one more fix.**
- Before: "We know of the meeting only through Optatus, our opponent."
- After: "Optatus, our opponent, tells the story of that meeting."
- Reason: gaps entry OG-23 item 13 records that Augustine also preserves the Cirta acts (Contra Cresconium III.27). The original telling's "our only source" repeated an open defect of the story record. The story record's `divergence_note` still says "reaches us only through Optatus". That is added to the defects list below.

### Things the deleted bodies held that need a home

The deleted bodies are in git history. Check these against `Build/worlds/don/Open_Gaps_Tracking.md` before the content is lost from view:
- **Front body FINDING 3.** `cic-website/data/world-census.json` and `atlas-v3.html` disagree on the don status ("Built & Live" against "Selected - Not Yet Built"). I found no entry for this in the gaps log.
- **Front body Timgad note.** The site census `experienceToday` names Timgad. This interacts with OG-23 item 9.
- **Front body FINDING 1 (duplicate record pairs) and FINDING 2 (`don.figure.optatus` register).** Both are already logged (gaps log lines about 1527–1547, 1538, 1872).
- **Story bodies, homonym and retrieval notes.** These cover the three Felixes, the two Caecilians, Maximian and Maximianus, Optatus Gildonianus and Optatus of Milevis, and the two Marcellini. Most also appear in core caution 7 and the figure records. The "three Felixes" note and the "two Caecilians" note in the Acta exist only in those bodies.
- **The 411 body's account of which lines were read and of the two bishop-counts.** The counts are also in the record's `divergence_note`.

### More record defects (other record types, not touched)

7. **`don.story.council-of-cirta`.** `divergence_note` says the account "reaches us only through Optatus" and `use_note.not_for` assumes one witness. Augustine also preserves the acts (gaps entry OG-23 item 13).
8. **`don.dw.who-decides-a-disputed-case`.** It lists "the Cirta acts" among proceedings that "survive" as our own, which sits against the Cirta story's single-witness framing. One of the two needs reconciling.
9. **Envelope `confidence.divergence_note` of `don.front.donatism`.** It still says "this world's own". This is metadata and not shown to participants, so it was left.

---

## Round 2 fixes (commit 80f9007e2)

Source: /tmp/claude-0/-home-user-CIC-Project/0b1f54c8-3ed3-54d3-9dab-f497b0e870d6/scratchpad/recheck-don.md (1 BLOCKING, 11 SHOULD-FIX, 12 NIT). I checked each finding against the records before changing anything.

Gates:
- `records don`: PASS
- `regate don --base origin/main`: PASS
- `check_live_commentary --base origin/main --enforce`: exit 0. It reports 0 REWRITE and 0 ROUTE in records and worlds. The worlds hits are the 8 KEEP dates plus PROTECTED lines in the gaps log.

`engine.m10.cli gaps don` reports 130 findings. They are all in older `Review-Artifacts` files, not in anything this branch touched. It is not one of the required gates.

### BL-1. ACCEPTED.

`don.core.donatism` `thinness` says "Donatist literature survives almost entirely as quotation embedded inside its own refutations". `don.figure.augustine` says "He preserves more of our own words than anyone else".

**Unit 9**
- Before: "Their own voice survives in four short texts and in their bishops' words at the hearing of 411. It survives too in two words cut into pillars…"
- After: "Most of their own words survive only as quotations in those men's books. Four short texts speak for them directly, and so do their bishops at the hearing of 411. So do two words cut into pillars near Bagai, Deo laudes, praise to God."
- Added `don.figure.augustine` and `don.figure.petilian` to `grounded_in`.

**Tile**
- After: "…Most of their own words survive as quotations in those books. Beyond those, they speak in four short texts, in their bishops' words at the hearing of 411, and in two words cut into stone."
- This now agrees with `read_first[1]`, `who_speaks` and the Petilian voice.

### SHOULD-FIX

**SF-1. ACCEPTED.** The qualifier attaches to a specific claim, so the tails ruling does not cover it.
- Unit 1, before: "In court, its bishops called themselves 'the party of Donatus'."
- Unit 1, after: "Optatus, an opponent, says its bishops called themselves 'the party of Donatus' when questioned in court. What they called themselves among themselves is not known."
- Unit 6 now reads "Optatus also reports…", so his first mention carries the attribution.

**SF-2. ACCEPTED.** `don.gravity.rebaptism-boundary-marking` says: "The accusation against Felix of Aptungi is not its root."
- Tile, before: "So a whole rival church grew up around one demand, to be washed again…"
- Tile, after: "So a rival church grew up with its own bishops. Anyone who came over to it was washed again by a hand that had never failed."
- Added the gravity record to the tile's `grounded_in`.

**SF-3. ACCEPTED.**
- Tile: "The Donatists kept the names of their dead…" The tile's later sentences now use "they".
- Unit 4: "The Donatists' own account says…" and "…they read such accounts aloud again."
- Unit 3: "So the Donatist font gave a convert his first real baptism."

**SF-4. ACCEPTED.** The story `text` says "as he signed most of what he said there". The figure record says "at times".
- After, in the Emeritus voice and the 411 telling: "He signed the notary's record of most of what he said, and added that he kept his right to appeal."

**SF-5. ACCEPTED.**
- After: "For six days, Macrobius says, the bodies were driven back toward the shore…"

**SF-6. ACCEPTED.**
- After: "Two hostile writers confirm his death, and each disputes its meaning in a different way."

**SF-7. ACCEPTED.** `don.term.liber-regularum` says "the rival church's own way of reading".
- After: "It passed to the rival church, and it shaped how Augustine read Scripture."

**SF-8. ACCEPTED.**
- Acta: "Their words survive in the dossier Optatus attached to his books against us."
- Gesta: "Optatus, our opponent, kept the court record among his documents, because its findings tell against us." This sentence is also N7.
- Cirta: "Optatus tells the story of that meeting in his books against us."

**SF-9. ACCEPTED.**
- After: "The letter came from a magistrate, Caecilianus. He told the court he had never dictated its closing lines."

**SF-10. ACCEPTED.**
- "That is the central problem with the sources."
- "The clearest exception is two words, Deo laudes, cut into stone."
- "That question is left open." was deleted.

**SF-11. ACCEPTED.** I added **OG-41** to `Build/worlds/don/Open_Gaps_Tracking.md`. It carries:
- the nine Latin phrases, the source file, the loci and the line numbers 73363 and 124975-125010;
- a pointer that replaces OG-33's "body note" reference;
- the `pull_quotes` reason (N11);
- the homonym notes that existed only in the deleted bodies;
- a note that OG-40 closes when this branch merges.

### NIT

**N1. ACCEPTED.**
- The Tyconius telling now ends "…then condemned him. He never went over to the other side."
- "He was never received back" is cut.

**N2. ACCEPTED.**
- "Where, by his church's account, Marculus was held four days at a cliff and thrown from it."

**N3. ACCEPTED.**
- "Optatus wrote against us about fifty years later. He adds that…" (split to keep it under 25 words).
- "Around then, persecution broke over Carthage".

**N4. ACCEPTED.** "ever" is cut.

**N5. ACCEPTED.** "He was not a cleric of either church."

**N6. ACCEPTED.**
- The teaser now says "argue before a court bound by an order".
- The Bagai telling now says "in the harshest terms it had".

**N7. ACCEPTED.**
- Gesta: rewritten plainly, as above.
- 411 telling: "So he put his name to his words…" is cut.
- `who_speaks`: "and its most filtered" is cut.
- Emeritus hedge: "Even this voice has limits." is cut.

**N8. ACCEPTED.** Unit 1's "This account follows them to 439" is cut. Unit 8 keeps "This story ends in 439".

**N9. ACCEPTED.**
- The 28-word sentence is split in two.
- "They confessed Father, Son and Holy Spirit as one God."

**N10. ACCEPTED.**
- "In Numidia it far outnumbered the other church."
- Unit 5's first two sentences are merged to stay within length.

**N11. ACCEPTED.** It is routed to OG-41 item 2 instead of `Build/Ministry`, so that it sits beside the other don open items.

**N12. ACCEPTED, with different wording.** The record supports Augustine's conditional ("if the baptisms these bishops had given in schism could stand"). It does not support the flat statement that they "were allowed to stand".
- After: "These two had baptized while in schism. Augustine made this the center of his case against us. If their baptisms could stand on our own authority, he argued, then our rule did not hold even for us."

### Also noted

- The recheck says FINDING 3 is moot, because `atlas-v3.html` now says "Built & Live". It is dropped from my "needs a home" list.
- To hold the 700-word cap after BL-1 and SF-1, I made these small cuts in the main story:
  - Unit 5: two sentences merged.
  - Unit 6: "Optatus also reports".
  - Unit 7: "a slightly larger number of rivals" and "said their spokesman Petilian".

  No fact was dropped.

### Word counts and readability after round 2 (`engine.m1.fk`)

| Unit | Words | Avg sentence | Max sentence | FK | FRE |
|---|---|---|---|---|---|
| Main story | 700 | 12.5 | 25 | 7.2 | 65.7 |
| Tile | 196 | | | 6.1 | 76.1 |
| macrobius | 238 | | 23 | 6.3 | 73.6 |
| acta | 184 | | 22 | 8.1 | 60.6 |
| cirta | 204 | | 21 | 6.4 | 70.2 |
| gesta | 214 | | 25 | 6.2 | 70.5 |
| tyconius | 170 | | 23 | 6.7 | 72.0 |
| lucilla | 228 | | 25 | 6.6 | 70.0 |
| bagai | 173 | | 21 | 7.5 | 65.2 |
| conference | 234 | | 24 | 6.7 | 71.7 |
| passio | 177 | | | | |

The passio telling is unchanged since round 1.
