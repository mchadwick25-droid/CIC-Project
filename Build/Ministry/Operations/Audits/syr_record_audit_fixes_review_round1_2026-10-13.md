Review round 1, syr record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS WITH NON-BLOCKING

Scope: commit 33750806e, 60 files under records/syr. `git diff origin/main -- records/syr` equals that commit, so there are no other uncommitted changes under records/syr. Intent was read from Build/worlds/syr/Open_Gaps_Tracking.md entry 27. Facts were checked by grep against cic/texts/ (npnf213 Aphrahat/Ephrem, aphrahat_demonstrations-2-7_hallock1932, npnf203 Theodoret, palladius_lausiac-history_clarke1918, npnf208 Basil, anf08 Book of the Laws of Countries, anf09 Hogg's Diatessaron introduction, chronicle-of-edessa_cowper, duchesne tome 3). Which fields are spoken was checked against engine/m1/spoken_fields.py.

## Findings

1. **syr.quote.a-pearl-upon-the-palm, modern_lens_note**
   - Old: `...he says the pearl 'fills me in the place of books, and the reading thereof, and the explanations thereof'...`
   - New: `Later in the same hymn he says the pearl will "fill me in the place of books, and the reading thereof, and the explanations thereof".`
   - Source: npnf213 l.21823-21825, Pearl Hymn I: "so does this pearl fill me in the place of books, and the reading thereof, and the explanations thereof."
   - NON-BLOCKING. The words inside the quotation marks are verbatim. The added "will" turns Ephrem's present ("does ... fill") into a future. "says the pearl fills me in the place of books..." keeps his tense.

2. **syr.quote.warned-before-baptism, modern_lens_note**
   - Old: `This settles the infant-baptism question by making it unaskable: nobody warned here is a baby...`
   - New: `The people warned here are adults choosing for themselves. ... The passage does not say whether infants were also baptised.`
   - Source: hallock1932 l.47 (VII.20): "those who choose for themselves virginity and holiness, young men and virgins".
   - NON-BLOCKING. The overclaim about infant baptism is fixed, and the closing hedge is right. "Adults", though, is the note's own word, not the text's. The text names "young men and virgins" who "choose for themselves". "People old enough to choose for themselves" says what the passage supports without fixing an age.

3. **syr.dw.decides, text**
   - Old: `There were bishops - Nisibis remembered its line of them with love, and one of them sat at the great council of Nicaea.`
   - New: `...Nisibis remembered its line of them with love, and remembered that one of them sat at the great council of Nicaea.`
   - Source: Jacob's presence at Nicaea comes from Theodoret (npnf203 l.11115, Greek, Antiochene). The Nisibene Hymns in npnf213 never mention Nicaea; a grep for "Nicaea"/"Nice" there finds nothing. syr.story.jacob-nicaea's tellable_as says "the tradition's memory", not Nisibis's.
   - NON-BLOCKING. The intent was to recast Nicaea as remembered tradition, and that is met. But the new grammar makes Nisibis the one remembering, which no cited source shows. syr.dw.was-jesus-god's wording, "Our tradition remembers that our own bishop of Nisibis sat at Nicaea", avoids this and could be reused here.

4. **syr.dw.unsettled and syr.demo.unsettled, text / exchange**
   - Old: `the same gift that made us sing made us scornful`
   - New: `Our poets who sang so well could also be scornful.`
   - Source: syr.dw.failures, which is unchanged on this point, puts the scorn in one man: "Our greatest teacher's gift for poetry was also a gift for scorn". The polemic records name Ephrem's Prose Refutations and the Hymns. No second poet in the syr records carries this charge.
   - NON-BLOCKING. The plural spreads a charge sourced to one poet across "our poets". "Our great poet, who sang so well, could also be scornful" keeps the coined-closer fix without the broadening.

5. **syr.demo.someone-like-me, exchange (representative turn 2)**
   - Old: `...a single word, deception, more polemic than fair portrait.`
   - New: `...a single word, deception. That was polemic, not a fair portrait.`
   - NON-BLOCKING. "More polemic than fair portrait" was a judgment of degree. The new line makes it a flat "X, not Y" verdict, which is mildly firmer and has the pivot shape the rules warn about. "That was more polemic than a fair portrait" keeps the original's degree in a short sentence.

6. **syr.force.synod-410, description**
   - Old: `...the settled order its own long ambiguity never produced from within arrives from without.`
   - New: `...The community's own leaders had not settled this order. The synod did.`
   - NON-BLOCKING. The coined closer "from within ... from without", which entry 27 names, is gone. But the new ending puts back a short contrast-and-reveal closer ("had not settled ... The synod did."). The fact is fine; only the shape is a mild tell. Something like "The order came from the synod, not from the community's own leaders" would avoid it, or the sentence could simply be cut, since syr.dw.unsettled already says it.

7. **syr.force.frontier-plural-milieu, description**
   - New value ends `...had formed yet. '`, with a trailing space inside the quoted scalar.
   - NON-BLOCKING. A whitespace defect only.

8. **syr.figure.marutha, names / dates.floruit (rationale only, not the record)**
   - Old: `Marutha of Maiperqat (Martyropolis)...`
   - New: `Marutha, bishop in Roman Mesopotamia...`
   - Source: duchesne_histoire-ancienne-de-leglise-tome3-fra_2e-ed1910.txt l.20630: "Marutas, évêque de Maïpherqat (Martyropolis dans la Mésopotamie transtigritane)". On relics, no vendored hit supports "gathering the relics". Duchesne l.20532 says only that the Acta collection is wrongly attributed to him.
   - NON-BLOCKING. The record edit is sound, because the record cites only Socrates VII.8, which does not name the see. But entry 27's stated reason, "no vendored source or record carries them", is wrong for Maiperqat: a vendored file does carry it. Correct the reason in the log, or keep the see and cite Duchesne. The relics removal stands.

Observed but not introduced by this change (pre-existing, outside the change's intent; listed so they are not lost):
- **syr.dw.death-judgment.** The Bardaisanite dialogue (anf08 l.68966) is answering fate and astrology, not "the complaint that one way is too narrow". The dialogue is also not among the record's own `sources`. The edit only fixed the attribution, which it did correctly. Its addition of "new" ("one new people") matches the source's "the new race of us Christians".
- **syr.dw.remains, positions.** These still contain the build word "in-window". This field is unchanged, but it is an evidence-head field.

## Changes checked and found sound

- **Quote renderings, each re-checked clause by clause against its own `text`.**
  - a-man-called-wise: the wise man who asks and is heard are joined back into one clause, and nothing is added.
  - Both pearl quotes: "went to look" matches "I went to look at it".
  - basil-credits-a-syrian: "he says" is restored.
  - palladius-hospitaller: "hospitaller" is rendered as taking in and caring for the needy. This fits Palladius XL.3, where Ephrem nursed the famine-stricken and "provided day by day hospitality and assistance".
  - tatian-born-assyrian: "barbarian philosophy" is kept.
  - the-blasphemy-of-madmen: "blaspheme" is kept, "for one reason" is removed, and "(this is said) in order that ... may perchance" becomes "We say this so that ... may perhaps".
  - theodoret-gnats: "no other curse" in both the rendering and the use_note.
  - warned-before-baptism: the virginity group is rendered as a second group, which matches "and to those who choose"; the 48-word sentence is split; nothing is added. The removed "~" is the transcription's non-breaking-space artefact (compare "3.~For", "~|45~"), so "i.e. in matrimony" is a faithful normalization.
- **Demonstration XXI (syr.demo.suffering, syr.dw.suffering).** "Jesus was persecuted, and the martyrs came after him" matches XXI.23 ("after Him was the faithful martyr Stephen..."). The false "Jesus at the far end" is gone.
- **Demonstration VII (syr.demo.room-for-doubt, syr.dw.penitence-prayer).** "Must not turn you away, or tell anyone what you showed him" matches VII.4 ("not withhold healing", "when he has revealed to you do not publish it"). syr.demo.physician's "hiding a wound was what kept it from healing" and "Coming to him meant turning back from wrong" match VII.3 ("confess his sin, and depart from it"; "gangrene comes to the wound of him who is ashamed to show it").
- **syr.dw.adam-grace.** "Christ was the foundation stone, and faith rested on him" matches Dem I.2 and I.4. The list fasting, prayer, love, almsgiving, meekness matches I.4. The unsourced "courtroom verdict" is gone.
- **syr.dw.doubt.** "He says the taunt troubled him" matches XXI.1-2 ("my mind was disturbed"). "Patiently" is gone.
- **The 512 manuscript.** syr.figure.aphrahat, syr.figure.jacob-of-nisibis, syr.term.mar and syr.source.aphrahat-select-demonstrations all match npnf213 l.13080-13085 ("a second, dated 512 ... 'Mar Jacob the Persian Sage'").
- **syr.force.transmission-ongoing.** "His name was soon lost" fits npnf213 l.12981 ("his proper name seems to have been for a time forgotten"). "Barely disseminated" is rightly removed: the same introduction says the work was "remembered, cited, translated, and transcribed for at least two centuries".
- **syr.force.transmission-ending.** "In time its Syriac copies were lost" is consistent with Hogg (anf09 l.1937: Syriac manuscripts still made in the ninth century).
- **syr.story.jacob-deliverance.** Ephrem begs Jacob to mount the wall, see the enemy and curse them; Jacob calls down no other curse than gnats; "The Persians left their camp and fled". All of this matches npnf203 l.11171-11182. The unsourced "watched it / put it into the hymns" is gone.
- **syr.story.edessa-flood-201.** "About 340 years" matches the Chronicle's 540s compilation against the 201/202 flood (cowper l.4, l.32, l.53).
- **syr.dw.corpus-and-its-edges.** The flood line, its dispute kept open, the Abgar legend told without "scholars", and "some of our arguments survive only from our side" (more accurate than "every argument") are all sound.
- **syr.dw.failures.** "Began decades before the persecution" fits syr.contested.papa-primacy (the synod c. 315 against the 340s). The positions line and use_note follow.
- **syr.dw.gospel-harmony.** "Later Syriac writers called it..." matches syr.contested.diatessaron-name.
- **syr.dw.was-jesus-god.** Nicaea is told as remembered tradition, and the tense moves to "we answered/guarded".
- **syr.term.raza-shrara, syr.gravity.raza-shrara-method.** "Hidden power" is gone from plain_meaning, quick_meaning and description, which are the spoken fields. senses.informational still carries it, but that field is not in SPOKEN_FIELDS, and the evidential sense labels it as scholarly synthesis.
- **syr.voice.craft.** "Adiabene" and "fleet floor line" are removed. "No one now knows whether Aphrahat held a bishop's office" fits npnf213 l.12986-12988.
- **syr.demo.authority, syr.dw.authority-lived.** Same fix as voice.craft.
- **syr.story.qyama-morning.** The reconstruction is now flagged in the opening sentences.
- **syr.dw.remains.** "The only building ... that can be dated securely" matches its own positions. "Historians" and the coined closer are gone.
- **syr.dw.apostolic.** "The historian can trace" and "Both of those things are true." are gone.
- **Tier B rewrites.** These were checked for meaning drift, and none was found: the coined closers removed, the dash-chain splits, the three-beat removals (someone-like-me, woman-authority), and the past-tense changes. The files covered are demo.jesus, marriage-ending, physician, woman-authority, someone-like-me; dw.born-again-endtimes, cost-distance, jesus, reading, outsiders-empire, physician; the two honest limits; term.ihidaya and term.anti-jewish-polemic; story.choirs-tradition; figure.bardaisan bridge_line; force.qyama-commitment and force.frontier-plural-milieu. No new build words or etic "scholars/historians" were introduced in we-voice spoken text.

## Disposition

No blocking findings. All eight non-blocking findings were applied before the package was rebuilt: the pearl lens note keeps Ephrem's present tense ("does fill me"); the baptism lens note says "old enough to choose for themselves"; syr.dw.decides says "our tradition remembers"; syr.dw.unsettled and syr.demo.unsettled name the one poet; syr.demo.someone-like-me keeps "more polemic than a fair portrait"; the synod-410 contrast closer is cut; the stray space is gone; the Marutha reason in the gaps log is corrected. The two older defects noted (the framing of the Bardaisan dialogue in syr.dw.death-judgment, and "in-window" in syr.dw.remains positions) were fixed in the same pass. Separately, the m1 quote-verbatim gate showed that Hallock's bare "~" (a space) is part of the vendored text, so syr.quote.warned-before-baptism keeps "(i.e.~in matrimony)" as printed, and its divergence_note now says so.
