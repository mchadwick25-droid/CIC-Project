# Independent review: Donatist Atlas story pass

Scope: `Build/worlds/don/surface/world_front/don.front.donatism.md` (`orientation.story`, `orientation.documented_stories`, `orientation.highlights`) and the `telling:` field of nine records in `records/don/story/`. Commits reviewed: 01ebb968b, 09350c81f and c92c6704e.

Method: I checked each claim against the cited `grounded_in` records and the story record (`text`, `tellable_as`, `absent_detail`, `use_note.not_for`, `divergence_note`). I also checked the figure, term, force, gravity, quote, doctrinal-witness and core records. I fetched all eight Pleiades URLs as JSON.

Unit numbers for the main story run 1 to 9, in file order.

---

## BLOCKING

### B1. "Nicene faith": unsupported and anachronistic
- **Where:** `orientation.story` unit 1; highlight `Nicene faith`
- **Quote:** "From around 311 until 439 ... Both confessed the same Nicene faith, word for word." Highlight: phrase "Nicene faith".
- **What's wrong:** No Donatist record uses the word "Nicene". `don.core.donatism` says only: "On the Trinity and on Christ, it holds the standard orthodox faith of Latin North Africa." `don.dw.the-creed-we-shared` says: "no creed or doctrinal statement of ours survives as a document of its own; the shared confession is read off the shape of what our opponents did and did not accuse us of." The sentence also dates the claim from 311, but Nicaea met in 325. The "Nicene" wording comes from the pre-pass text, and this pass kept it.
- **Fix:** "Both held the same faith in the Trinity and in Christ, in the same Latin words." Change the highlight phrase to "the same faith". Note: "The shared faith in the Trinity and in Christ, held across Latin North Africa. Both churches confessed it. They split over which bishops were valid."

### B2. "until 439" contradicts the closing unit and the force record
- **Where:** story unit 1 (against unit 8)
- **Quote:** "From around 311 until 439, two rival churches stood side by side in Roman North Africa"
- **What's wrong:** `don.force.vandal-capture-of-carthage` says: "What 439 closes is precise and must not be widened ... it does NOT end the two-party contest, which persists under Vandal and then Byzantine rule for roughly a further century and a half." Unit 8 says the same: "The contest went on under the Vandals". The opening sentence states the opposite.
- **Fix:** "From around 311, two rival churches stood side by side in Roman North Africa. Their story here runs to 439."

### B3. "nothing suggests they chose that name" is contradicted by a record
- **Where:** story unit 1
- **Quote:** "History calls its members Donatists, after an early bishop, though nothing suggests they chose that name."
- **What's wrong:** `don.term.pars-donati` says: "Our clergy signed a formal petition as bishops 'of the party of Donatus' ... Optatus says they used the phrase whenever they were questioned in court. Whether they named themselves so among themselves, the record cannot say." So there is evidence that they used the name, at least in legal settings. The sentence is stronger than the record and contradicts it.
- **Fix:** "History calls its members Donatists, after an early bishop. Its bishops used 'the party of Donatus' in court. What they called themselves among themselves is not known."

### B4. "hand over the scriptures or die": unsupported
- **Where:** story unit 2
- **Quote:** "Officials demanded that clergy hand over the scriptures or die."
- **What's wrong:** None of the cited records mentions a death penalty. `don.force.diocletianic-persecution-traditio-demand` says: "Clergy had to hand over scripture and sacred vessels to the persecuting authorities, to be destroyed." The `persecution of 303 to 305` highlight says the same and does not mention death, so the main story and its own highlight disagree. (`don.dw.the-books-they-came-for` has the emic flourish "or die rather than carry", but it is not cited and it is rhetoric, not a claim about the edict.)
- **Fix:** "Officials demanded that clergy hand over the scriptures and the church's vessels to be destroyed."

### B5. Marculus: the hedge is lost and the four days of fasting are invented
- **Where:** story unit 4
- **Quote:** "Bishop Marculus, after four days of fasting, was shown a cup, a crown and a palm, then thrown from a cliff called Novapetra."
- **What's wrong:**
  - **Lost hedge.** `don.story.passio-marculi` `divergence_note` says: "Inferential-Thin for the visionary and miraculous details specifically, which are offered as the tradition's own testimony and never as verified events." Its `not_for` excludes "a claim that the vision ... is independently confirmed". The etic narrator states the vision as fact.
  - **Invented detail.** The record says he was "held for four days at a cliff called Novapetra. In that waiting, the account says, he fasted". The record's own `tellable_as` says "after a day of fasting". Neither supports "four days of fasting". (The two record fields also disagree with each other. That should be logged, not built on.)
- **Fix:** "His church's own account says that Bishop Marculus, held four days at a cliff called Novapetra, fasted and saw a vision of a cup, a crown and a palm. Then he was thrown from the cliff."

### B6. "Persecution came a second time in 347": contradicted
- **Where:** story unit 4
- **Quote:** "Persecution came a second time in 347 and 348 ... It gave this church the martyrs it remembered."
- **What's wrong:** `don.force.macarian-repression` names an earlier persecution in between: "The earlier, less well-attested persecution under Leontius and Ursacius produced the commemorative sermon." `don.gravity.martyr-cult-identity` says Monceaux dates those events to 317. Calling 347 "a second time" erases that episode and its commemorated dead.
- **Fix:** "The worst persecution came in 347 and 348. This time it came at the rival church's urging, through the emperor's commissioners. It gave this church most of the martyrs it remembered by name."

### B7. "its own texts admit exceptions": wrong attribution
- **Where:** story unit 6
- **Quote:** "Still, its own texts admit exceptions. Three times it turned to the state when that served its case."
- **What's wrong:** The three recourses come from the opponents' documents. `don.gravity.principled-refusal-vs-pragmatic-recourse` says: "Anulinus's report is part of the Appendix of Documents in Optatus's own work. Augustine's own writing confirms the legal moves of the Maximianist years ... no source shows the Donatists themselves describing the tension this way." Core caution 1 forbids treating the hostile dossier as the movement's own voice.
- **Fix:** "Still, the record shows three times it turned to the state when that served its case."

### B8. 411: "ruled", and the actual outcome left out
- **Where:** story unit 7; highlight `Conference of Carthage`; `conference-of-carthage-411` telling (last sentence)
- **Quote:**
  - Unit 7: "Then he ruled that an imperial rescript had already given the name to the other side."
  - Highlight: "The record stops before any verdict."
  - Telling: "The verdict is not in what we have, because the acts break off before any sentence is given."
- **What's wrong:**
  - **"Ruled" overstates.** The story record says Marcellinus "said that he was nevertheless bound to follow the imperial rescript". In a court setting, "ruled" reads as the verdict, which is close to the `not_for` "a claim that the transcript records the court's verdict".
  - **The outcome is documented but never told.** `don.force.conference-of-411-verdict` says: "It ruled against the Donatist party. Sustained penal legislation followed the verdict, and the record documents both." No participant-facing text says that the church lost in 411 or was outlawed in 412.
  - **The highlight misleads.** It suggests no verdict is known, when only the part of the transcript read for this build lacks it.
- **Fix:**
  - Unit 7, last sentence: "Then he said he was bound by an imperial rescript that had already given the name to the other side. He ruled against this church, and harsh laws against it followed in 412."
  - Highlight: "A court hearing in 411, ordered by the emperor to settle the quarrel. The judge Marcellinus ran it and ruled against this church. The surviving transcript breaks off before his sentence."
  - Telling: "The acts we have break off before the sentence. We know from other records that the judge ruled against us."

### B9. Marcellinus "belonged to neither church": false and unsupported
- **Where:** highlight `Flavius Marcellinus`
- **Quote:** "He belonged to neither church."
- **What's wrong:** `don.figure.marcellinus` says: "The emperor's own officer, not a churchman of either side." "Not a churchman" means he was not a cleric. It does not mean he belonged to no church. He was a Catholic layman (Augustine dedicated *City of God* to him). The highlight turns "not clergy" into "neutral".
- **Fix:** "The imperial officer sent to judge the hearing of 411. He was a layman, not a bishop of either church. He was put to death in 413 on another charge."

### B10. Donatus "until his death in exile about 347": wrong
- **Where:** highlight `Donatus`
- **Quote:** "Primate at Carthage from about 313 until his death in exile about 347."
- **What's wrong:** `don.figure.donatus` says: "primate of this communion from c. 313 ... until c. 347; exiled after the Macarian repression and dead in exile." The record dates the exile to about 347. His death came later and is undated in the record.
- **Fix:** "Primate at Carthage from about 313. He was exiled about 347 and died in exile. The movement is named for him. Not one page of his own survives."

### B11. Vandal highlight: "ended the Roman state"
- **Where:** highlight `Vandal` (and unit 8 in softer form)
- **Quote:**
  - Highlight: "That ended the Roman state that this church had defined itself against."
  - Unit 8: "That ended the Roman rule this church had defined itself against. The contest went on under the Vandals, and then under the Eastern empire."
- **What's wrong:** The Roman state did not end in 439. `don.force.vandal-capture-of-carthage` defines the close narrowly: "it removes the Roman imperial state as the Catholic-aligned adjudicating and coercing power ... must not be widened." In unit 8, "ended the Roman rule" followed by "then under the Eastern empire" (which was Roman) contradicts itself.
- **Fix:**
  - Highlight: "The Vandals invaded Roman North Africa in 429 and took Carthage in 439. That removed the Roman power that had judged and coerced this church."
  - Unit 8: "That removed the Roman power this church had defined itself against. The contest went on under the Vandals, and then again under the emperors of the East."

### B12. "Its own voice survives in four short texts": contradicts the core and unit 7
- **Where:** story unit 9
- **Quote:** "Its own voice survives in four short texts, and in two words cut into pillars near Bagai"
- **What's wrong:** Core caution 2 lists the four texts and adds: "The 411 conference transcript also records Donatist bishops' own words, without an adversary selecting them for refutation." `don.story.conference-of-carthage-411` `modern_contrast` says it records the argument "in the losing side's own voice". Unit 7 itself quotes Petilian from that transcript. Petilian's letters also survive in quotation (`don.figure.petilian`). The sentence gives a false inventory.
- **Fix:** "Its own voice survives in four short texts, in its bishops' words at the court hearing of 411, and in two words cut into pillars near Bagai: Deo laudes, praise to God."

### B13. Cirta telling: "traitors" breaches `not_for`
- **Where:** `council-of-cirta` telling, last paragraph
- **Quote:** "Optatus tells it to show our founders as traitors excusing one another"
- **What's wrong:** `don.term.traditor-traditio` `not_for` excludes "a claim that traditor means a traitor in the modern political sense". The record says Optatus's aim was to show the founders as "self-interested traditores absolving one another". Glossing *traditores* as "traitors" is exactly the distortion the term record guards against.
- **Fix:** "Optatus tells it to show our founders as men who had handed over the scriptures, excusing one another."

### B14. Bagai title: "Taken Back Without a Word"
- **Where:** `documented_stories` `bagai-reconciliation` title
- **Quote:** "Condemned as Shipwrecked, Then Taken Back Without a Word"
- **What's wrong:** The `absent_detail` says: "We do not know what was said in the room". `not_for` excludes "a claim that the exception was hidden". "Without a word" claims silence, and suggests concealment, which the record says is unknown. If it is meant to say "without a rite", it misleads.
- **Fix:** "Condemned as Shipwrecked, Then Taken Back Unbaptized and Unordained Again". Shorter: "Condemned as Shipwrecked, Then Taken Back as They Were".

---

## SHOULD-FIX

### S1. Main story drops the torture caveat on Felix's clearing
- **Where:** unit 2
- **Quote:** "The emperor later had the charge against Felix tried, and Felix was cleared."
- **What's wrong:** The `acta-purgationis-felicis` `divergence_note` says the threat of torture "is stated here rather than left implicit". `don.figure.felix-of-aptungi` keeps the same hedge. The main story is the most-heard surface, and it drops the caveat.
- **Fix:** "The emperor later had the charge against Felix tried. A witness admitted, under threat of torture, that he had forged the evidence, and Felix was cleared."

### S2. "When it ended": unclear referent and compressed chronology
- **Where:** unit 2
- **Quote:** "This church held that what a minister did in that moment decided whether his hand could be trusted afterward. When it ended, Caecilian was elected bishop of Carthage."
- **What's wrong:** "It" can be read as "that moment". If it means the 303–305 persecution, the sentence makes the election follow at once. The core dates it to 311 or 312 and says "The year turns on how we date the step from persecution to the choice of a bishop."
- **Fix:** "Some years after the persecution, in 311 or 312, Caecilian was elected bishop of Carthage."

### S3. "never called it a second baptism": overstated
- **Where:** unit 3
- **Quote:** "This church never called it a second baptism."
- **What's wrong:** `don.term.rebaptism` says: "We did not think of this as baptizing twice." "Never called" is an absolute claim about usage that no record checks.
- **Fix:** "This church did not count it as a second baptism."

### S4. "its font": ambiguous
- **Where:** unit 3
- **Quote:** "A hand from a broken line had given nothing the first time, so its font marked a person's first true entry into the church."
- **What's wrong:** The nearest antecedent for "its" is "a hand from a broken line", which reverses the meaning. At 24 words, this is the longest sentence in the story.
- **Fix:** "A hand from a broken line had given nothing the first time. So this church's font was a person's first true entry into the church."

### S5. Christ comparison voiced by the etic narrator
- **Where:** unit 7
- **Quote:** "They stood before an imperial judge, as Christ had stood before his governor, and refused the chairs he offered."
- **What's wrong:** The comparison is Petilian's own claim (story record; `don.figure.petilian`: "Christ, he said, had stood before his own governor"). The narrator adopts it as its own framing.
- **Fix:** "They refused the chairs the imperial judge offered. Christ had stood before his governor, their spokesman Petilian said, and so would they."

### S6. 279 v 286 stated as settled; 279 tied to the chair refusal
- **Where:** unit 7; `conference-of-carthage-411` teaser
- **Quote:**
  - Unit 7: "two hundred and seventy-nine of its bishops faced two hundred and eighty-six"
  - Teaser: "Two hundred and seventy-nine bishops refuse the chairs a judge offers them."
- **What's wrong:**
  - **The count is disputed.** The story `divergence_note` (3) says: "The two bishop-counts do not agree and neither is suppressed here ... the acts' own roll-call tally ... records the Catholic subscriptions at two hundred and sixty-six with twenty further". The main story drops that.
  - **The chair refusal is only tied to "our bishops".** The record places the offer at acts 144–145 and says only "offered our bishops chairs". Nothing puts all 279 in the room at that moment, and seven pleaded for each side.
- **Fix:**
  - Unit 7: "about two hundred and eighty of its bishops faced a slightly larger number from the other side."
  - Teaser: "This church's bishops refuse the chairs a judge offers them. For three days they argue that the court had already given the other side the name Catholic."

### S7. 411 title and teaser overstate the rescript
- **Where:** `documented_stories` `conference-of-carthage-411`
- **Quote:**
  - Title: "Three Days Standing Before a Judge Already Told Who Was Right"
  - Teaser: "...an order that had already named the other side the church."
- **What's wrong:** The rescript gave the other side the *name Catholic* (story text; `don.figure.marcellinus`). The judge then conceded that the name belongs to whoever holds the truth. "Told who was right" and "named ... the church" are the Donatist reading presented as fact.
- **Fix:**
  - Title: "Three Days Standing Before a Judge Bound by the Emperor's Word".
  - Teaser: use the wording in S6.

### S8. `when: "1-8 June 411"`: unsupported specificity
- **Where:** `documented_stories` `conference-of-carthage-411`
- **What's wrong:** No Donatist record gives these dates. The records say "In the summer of 411" (story) and "the Conference of June 411" (`don.figure.marcellinus`).
- **Fix:** `when: "June 411"`.

### S9. Bagai teaser: register slip and an unsupported superlative
- **Where:** `documented_stories` `bagai-reconciliation` teaser
- **Quote:** "...condemn a breakaway group in the harshest words they ever used. Later our party takes two of them back, and no rite is done again."
- **What's wrong:**
  - **Register.** The front is `register: etic`, and "our party" is emic.
  - **Superlative.** The record says "the harshest terms it had", meaning that council. "They ever used" makes an all-time claim no record supports.
- **Fix:** "Three hundred and ten bishops condemn a breakaway group as shipwrecked men. Later their church takes two of its bishops back without baptizing or ordaining them again."

### S10. Bagai `when` disagrees with the telling and the records
- **Where:** `documented_stories` `bagai-reconciliation` `when` against the telling
- **Quote:** "394 (the Bagai council and reception)" against the telling's "Within a few years our party took back two of those condemned bishops"
- **What's wrong:** `don.force.maximianist-fracture` says "Over 394-398 the party suppressed them ... Afterward the mainstream party received the Maximianist clergy back". The story record's `use_note.years` is 393–398. The reception did not happen in 394.
- **Fix:** `when: "393 (the Cebarsussi rupture); 394 (the Bagai council); the reception in the following years, by 398"`.

### S11. Gesta teaser misstates who admitted what
- **Where:** `documented_stories` `gesta-apud-zenophilum` teaser
- **Quote:** "A bishop's own letters are read into the record. They admit an accusation was true and beg that no one find out."
- **What's wrong:** The letters were written by several bishops (Purpurius, Fortis, Sabinus). Only Purpurius's letter admits the charge was true: "he knew the things written in the bill of accusation were true". Fortis asks only to stay out of a public court.
- **Fix:** "A Roman official questions witnesses under oath. Bishops' letters are read aloud. One admits the charge was true, and several beg that no one find out."

### S12. Lucilla teaser: "The only account"
- **Where:** `documented_stories` `lucilla-affair` teaser
- **Quote:** "The only account comes from the man who blames her."
- **What's wrong:** The 320 court record (`don.story.gesta-apud-zenophilum`; `don.figure.lucilla`: "money that a court six years later traced to the founding of a rival altar") is a separate witness to her role. It is not Optatus's own composition.
- **Fix:** "The story of the rebuke comes only from the man who blames her."

### S13. Tyconius title and teaser: "layman" without attribution
- **Where:** `documented_stories` `tyconius-condemnation` title and teaser
- **Quote:** "The Layman Who Argued..." / "A layman argues from Scripture..."
- **What's wrong:** The only support is `don.term.liber-regularum`: "a Donatist whom Monceaux calls a layman". `don.figure.tyconius` says "writer and preacher". The story record does not call him a layman. The title states a secondary attribution as fact.
- **Fix:**
  - Title: "The Writer Who Argued the Church Reached the Whole Earth".
  - Teaser: "A writer argues from Scripture that the church spans the whole earth. His bishop tells him to stop. He neither recants nor leaves, and a council reportedly condemns him."

### S14. Cirta telling: the question was put to Felix, not Caecilian
- **Where:** `council-of-cirta` telling, paragraph 1
- **Quote:** "There they faced the same question they would soon put to Caecilian."
- **What's wrong:** The traditor charge was against Caecilian's consecrator. `don.figure.caecilian` says "we never accepted him, because of who laid hands on him". The story record's own `retrieve_when` says "the same standard they applied to Caecilian and Felix".
- **Fix:** "There they faced the same question they would soon put to Felix, the bishop who made Caecilian."

### S15. Cirta telling: missing object
- **Where:** `council-of-cirta` telling, paragraph 3
- **Quote:** "Secundus then asked the three bishops who had not been accused, Victor of Garba, Felix of Rotarium and Nabor of Centurio."
- **What's wrong:** "Asked" has no object (asked what?). Read aloud, the sentence dangles.
- **Fix:** "Secundus then asked for the judgement of the three bishops who had not been accused: Victor of Garba, Felix of Rotarium and Nabor of Centurio."

### S16. Acta telling: "said instead" is ambiguous
- **Where:** `acta-purgationis-felicis` telling, last paragraph
- **Quote:** "Even so, the inquiry did not find in our favor. Our tradition said instead that the wider dispute took in far more people than one case could settle."
- **What's wrong:** "Instead" reads as "instead of accepting the ruling". The record means instead of resting on the torture objection: "it is not the reason our own tradition eventually gave for holding it loosely - which was, rather, that the wider traditio dispute involved far more people".
- **Fix:** "Even so, the inquiry did not find in our favor. Our own reason for holding it loosely was different. The wider dispute took in far more people than one case could settle."

### S17. Passio telling merges the two hostile witnesses
- **Where:** `passio-marculi` telling, last sentence
- **Quote:** "Our opponents say only that he was killed, and they argue about whether that killing counts."
- **What's wrong:** The record's body note says: "THE TWO HOSTILE WITNESSES DISPUTE DIFFERENT THINGS AND MUST NOT BE MERGED ... Optatus argues ... the deaths were deserved punishment ... Augustine separately argues ... whether the men threw themselves down or were thrown." So Augustine does not "say only that he was killed".
- **Fix:** "Optatus, who wrote against us, grants that he was killed but calls it a just punishment. Augustine asks whether he was thrown at all."

### S18. Passio telling: "the tradition" slips out of the emic voice
- **Where:** `passio-marculi` telling, paragraphs 3–4
- **Quote:** "the tradition holds ... the tradition says ... This is the tradition's own testimony"
- **What's wrong:** Tellings are "we" speaking. Three times this one speaks of itself from outside.
- **Fix:** "...we hold that his body did not break in the fall. It came down gently, we say..." and "This is our own testimony, and no outside witness confirms the vision, the fall or the light."

### S19. Tyconius telling: "we had cut him off" closes the question the record leaves open
- **Where:** `tyconius-condemnation` telling, last sentence
- **Quote:** "...but that happened elsewhere, after we had cut him off."
- **What's wrong:** `divergence_note` says: "Tyconius's own formal standing within this communion is deliberately left open." Core caution 9 says the same. Two sentences earlier the telling hedges the condemnation ("it is reported"), then states the exclusion as fact. It also contradicts "He went on arguing from inside the party".
- **Fix:** "His Book of Rules outlived our party and shaped a rival bishop's reading of Scripture. But that happened elsewhere, to a man we never took back."

### S20. Tyconius telling: "cut themselves off" twice
- **Where:** `tyconius-condemnation` telling, paragraph 2
- **Quote:** "Those who had cut themselves off, his own party among them, were the ones who had cut themselves off from something real."
- **What's wrong:** The repeated phrase empties the sentence. Read aloud, it sounds like a tautology.
- **Fix:** "Those who had left that communion, his own party among them, were the ones who had broken away from something real."

### S21. 411 telling: unglossed legal jargon, and the point is lost
- **Where:** `conference-of-carthage-411` telling, paragraphs 3–4
- **Quote:** "he held the court to its procedure before its substance" / "He signed the record of his words again and again with his appeal reserved."
- **What's wrong:** "Procedure before substance" and "appeal reserved" are lawyer's terms that a B2 listener cannot unpack. The record's point is dropped: "He put his name to the notary's account of his own words and refused, in the same stroke, to accept the proceeding".
- **Fix:**
  - "Emeritus of Caesarea carried our argument. He would not let the court touch the case itself until it had settled the date, the mandates and who was bringing the charge."
  - "Each time, he signed the notary's record of his words, and added that he still kept his right to appeal. He would own what he said without accepting the court."

### S22. Macrobius telling flattens Isaac's cry
- **Where:** `macrobius-letter` telling, paragraph 2
- **Quote:** "he called his floggers traditores, the name for those who had handed over the scriptures."
- **What's wrong:** The letter's most distinctive line is gone. The record keeps it as indirect speech ("come, heal your madness of 'unity'"), and `don.figure.isaac` already renders it so: "told them to come and heal their madness of unity". The `divergence_note` permits indirect speech.
- **Fix:** "...he called his floggers traditores, men who had handed over the scriptures, and told them to come and heal their madness of unity."

### S23. Lucilla telling: idiom carries reproach
- **Where:** `lucilla-affair` telling, last sentence
- **Quote:** "Lucilla left no text, and no one asked her what she thought she was doing."
- **What's wrong:** In spoken English, "what she thought she was doing" is a scolding idiom. It repeats the hostile tone the paragraph has just disowned.
- **Fix:** "Lucilla left no text, and no one wrote down her own reasons."

### S24. Template across the tellings (AI tell)
- **Where:** all nine tellings
- **Quote:**
  - Openings: "Optatus, who wrote against us, is our only source" / "Optatus wrote against us some fifty years" / "Optatus, who wrote against us, kept it" / "Optatus, who wrote against us, chose to preserve it" / "Augustine, who wrote against us, tells this story" / "Augustine, who wrote against us, quotes"
  - Closings: "No account of this inquiry from our own side survives." / "Silvanus himself is never questioned in what survives" / "No record survives from the proconsul's side" / "Nor do we know whether anyone there named the contradiction out loud."
- **What's wrong:**
  - The appositive "X, who wrote against us" appears six times.
  - Every telling is 215–249 words in four paragraphs, with a provenance line at the start and an absence line at the end. Several closings are `absent_detail` lifted almost word for word.
  - A participant opening several cards hears the same machine.
- **Fix:** Vary per story. Put provenance where it bears on the scene, for example mid-story for Acta and Gesta. Let at least three tellings end on the story's own image:
  - Cirta: "No one was found guilty, and no one was cleared."
  - Macrobius: "...he urges the living to hurry after them."
  - Conference: the appeal line.
  - Keep "who wrote against us" for the first mention of each author only.

### S25. "the record" as meta-language in the main story
- **Where:** unit 8
- **Quote:** "The record closes in 439 ... After that, the record goes silent. No line from it to any church alive today has ever been shown."
- **What's wrong:** "The record" is build language for the window. In the last sentence, the nearest antecedent of "it" is "the record", so the sentence says no line runs from the record.
- **Fix:** "This story ends in 439, when a Vandal army took Carthage ... After that, the sources fall silent. No line from this church to any church alive today has ever been shown."

### S26. "simply the ordinary church of the countryside" adopts a contested thesis
- **Where:** unit 5
- **Quote:** "In Numidia it was simply the ordinary church of the countryside."
- **What's wrong:** Core caution 3 says: "The Frends thesis ... reads this world's rural strength ... as native social protest ... flagged for priority second-opinion review before it supports any specific claim." The core's neutral statement is: "Numidia is this church's own heartland, where it has far more people than its rival." The narrator's "simply" also flattens the point.
- **Fix:** "In Numidia it had far more people than its rival. There it was the ordinary church."

### S27. Gesta telling: "since it hurts us" is clumsy and close to a reveal
- **Where:** `gesta-apud-zenophilum` telling, paragraph 1
- **Quote:** "The court record survives only because Optatus, who wrote against us, chose to preserve it, since it hurts us."
- **What's wrong:**
  - **Clumsy.** It stacks three clauses with "who", "since" and "only because".
  - **Overstated.** "Only because" claims more than the record. The record says Augustine knew the Acts independently: "his letter shows that the record was known".
- **Fix:** "The court record reaches us through Optatus, who wrote against us. He kept it because it hurts us."

### S28. "proconsul" gloss is wrong in kind
- **Where:** highlight `proconsul`
- **Quote:** "A Roman official who judged court cases in a province."
- **What's wrong:** A proconsul governed the province of Africa. Judging cases was one of his duties. A listener will picture a magistrate.
- **Fix:** "The Roman governor of the province of Africa, who also judged its major cases. One cleared Felix of the charge. Another put Isaac and Maximianus on trial."

### S29. Highlights repeat "this church" throughout
- **Where:** `orientation.highlights` (15 uses) and the main story (8 uses)
- **What's wrong:** "This church" opens or closes most notes. Across 29 short notes it reads as templated filler.
- **Fix:** Use the proper name or context where it is clear, for example "the Donatist primate", "its bishops", or nothing at all. Example rewrite for `traditores`: "Latin for those who handed over. It names clergy accused of giving the scriptures to the persecutors. Such a man, Donatists held, could no longer baptize or ordain."

### S30. Donatus's question stands alone when read aloud
- **Where:** unit 6
- **Quote:** "Its bishop Donatus is remembered for one line, kept by the man who wrote against him. What has the emperor to do with the church?"
- **What's wrong:** Spoken aloud, the bare question sounds like the narrator asking it. `don.term.refusal-of-imperial-legitimacy` keeps the hedge "so our primate is reported to have asked".
- **Fix:** "Its bishop Donatus is remembered for one question, reported by the man who wrote against him: what has the emperor to do with the church?"

### S31. Rome and Arles called "a court run on a state's terms"
- **Where:** unit 6
- **Quote:** "A court run on a state's terms, in its view, was not the church judging itself."
- **What's wrong:** Rome (313) and Arles (314) were councils of bishops. `don.term.refusal-of-imperial-legitimacy` says the objection was "not because a council cannot rule, but because a council convened and enforced by a state already favouring the rival is not the church judging itself".
- **Fix:** "A council called and enforced by a state that already favored its rival was not, in its view, the church judging itself."

---

## NIT

- **N1.** Highlight `Novapetra`: "The cliff where Marculus was held and killed." Pleiades 334604 lists "Nova Petra?" as a *settlement*, with the name "less-certain". "Probably ... Henchir Encedda" is correctly hedged. Suggested change: "The cliff, by a place of the same name, where...".
- **N2.** Highlight `Vegesela`: Pleiades gives Ksar el Kelb (Barrington Atlas Directory), but its location accuracy is about 10 km. "Identified with" is fine.
- **N3.** Highlight phrase `Rome's hearing`: the possessive is odd. Use "the hearing at Rome" in both unit 6 and the highlight.
- **N4.** Highlight `Paul and Macarius`: "who forced this church ... Their force sometimes killed." The repetition of "forced" and "force" is awkward. Suggested: "At times they killed."
- **N5.** Teasers mix serial-comma styles: "a cup, a crown, and a palm" (Passio teaser) against "a cup, a crown and a palm" (title and story).
- **N6.** Passio telling: "records the day of his death but no year". The heading gives a commemoration day, with a variant reading ("8 (al. die 5) kal. decembris"). Suggested: "records a feast day but no year".
- **N7.** Unit 9 ends on an aphorism: "No hostile hand stands between those words and a modern reader." It is accurate (`don.quote.deo-laudes`), but it is the stock summary close. Suggested: "No opponent copied or chose them."
- **N8.** Unit 1: "centered on Carthage". The core places the heartland in Numidia, and unit 5 says so. "Based at Carthage and Numidia" avoids the pull.

## Places check (Pleiades)

All eight URLs resolve. The modern locations are supported by the Barrington Atlas Directory notes in the JSON:
- Aptungi (314843): Henchir-es-Souar
- Bagai (334501): Ksar Baghai
- Cebarsussi (329199): "in Byzacena", unlocated
- Cirta (305064): Constantine
- Novapetra (334604): Henchir Encedda, with the name less-certain
- Vegesela (334661): Ksar el Kelb
- Carthage (314921): "located in modern Tunis"
- Numidia (981539): province

No place note is wrong. See N1 and N2 for minor precision points.

## Out of scope but noticed

`don.story.passio-marculi` contradicts itself: `tellable_as` says "after a day of fasting", while `text` says he fasted through the four-day wait. This should go in `Open_Gaps_Tracking.md` rather than be resolved silently.

---

## Verdict

**Does not pass review.** Fourteen findings are BLOCKING. They fall into four kinds:
- **Unsupported or false facts:** Nicene; "or die"; the four days of fasting; Donatus's death date; Marcellinus "neither church"; "ended the Roman state".
- **Contradictions of records:** "until 439"; "nothing suggests they chose that name"; "a second time"; "four short texts".
- **Lost hedges and wrong attributions:** Marculus's vision stated as fact; "its own texts admit exceptions"; the 411 "ruled" and "no verdict" framing.
- **`not_for` breaches:** traditores glossed as "traitors"; the Bagai title implying concealment.

The craft is generally readable: the main story averages 13 words a sentence, with a maximum of 24. But the nine tellings share one template, and several distinctive lines were flattened.

**Counts:** BLOCKING 14 · SHOULD-FIX 31 · NIT 8
