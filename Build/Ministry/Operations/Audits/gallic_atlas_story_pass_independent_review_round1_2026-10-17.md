# Independent review: Gallic Atlas story pass (PR #932, `site/atlas-story-gallic`)

Reviewer: Opus 5.5, independent, adversarial. Read-only.
Scope: `orientation.story` (8 units), `orientation.documented_stories` (10), `orientation.highlights` (25) in `Build/worlds/gallic/surface/world_front/gallic.front.gallic-monastic-ascetic-christianity.md`, and the `telling:` field of the 10 story records in `records/gallic/story/`.
Checked against: every `grounded_in` record, the story records' `text` / `tellable_as` / `absent_detail` / `use_note.not_for` / `divergence_note`, `gallic.core.gallic` (horizon, cautions), the five figure records, the ten gravities, the contested claims, the terms, the vendored source `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` where a record quotes it, and Pleiades JSON for all ten place IDs (fetched 2026-10-17).

---

## A. Rigor: BLOCKING

### B1. Faustus as bishop of Riez is past the horizon
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 3; `highlights` "Riez"
- **Quote:** "Faustus, another monk trained on the island, became bishop of Riez." / "Faustus of Lérins became its bishop."
- **What's wrong:** `gallic.core.gallic` `horizon`: "What came after it is not ours: the synods of the 470s ... **Faustus belongs to us only as a monk and abbot.** His later book is not ours." `gallic.gravity.grace-and-effort` not_for: "Faustus's synodal commission, which falls after the window". His episcopate at Riez is only attested by Gennadius ch. LXXXVI (c. 495) and falls after 450. The main story then says "The record closes around 450", so it contradicts itself. Also, the PR's own OG-40 entry says Faustus of Riez was cut ("Cut details with no story record stay in the records only: ... and Faustus of Riez"). He was not cut, so the gaps log is wrong too.
- **Proposed fix:** Delete the Faustus sentence from unit 3. Delete the "Riez" highlight, or change its note to: "A Roman town of the Reii, now Riez in France." Then correct OG-40.

### B2. Honoratus did not go "alone", and snakes had not "driven everyone away"
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 3
- **Quote:** "a man named Honoratus went alone to a small island off the coast. Snakes had driven everyone else away."
- **What's wrong:** This contradicts the story record. `gallic.story.honoratus-and-the-island` `text` says: "he goes in unafraid, Hilary says, and **scatters the fear of his own** by his own security", and "In heart and mouth he carried a psalm, now to himself, **now to his own**". The PR's own telling says: "his own calm scattered **his companions'** fear." The record also gives two reasons the island was empty, and does not say anyone lived there before: "stood empty because of the excess of its squalor. No one could approach it for fear of venomous creatures." So the main story and the telling on the same page disagree.
- **Proposed fix:** "Two generations later, a man named Honoratus led a few companions to a small island off the coast. It was filthy, and no one went there for fear of snakes."

### B3. Honoratus's offices: the capture is moved to Arles, the hedge is lost, and the three texts disagree
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 3; `highlights` "Arles"; consistency with the Honoratus teaser and telling
- **Quote:** "and the record says the snakes gave way. He wanted only to stay a monk there. Even so, he later became bishop of the nearby city of Arles." / "Honoratus became its bishop. Hilary came after him."
- **What's wrong:**
  1. The only reluctance in the evidence concerns the **presbyterate on the island**. The record has "Here the priestly fillet fastens on its fugitive", and `thinness` says "his being taken into the clergy there". Unit 3 leaves the presbyterate out and uses "Even so" to tie his reluctance to **Arles**. The story's not_for forbids this: "Honoratus's later episcopate at Arles as history, when the sermon is a disciple's eulogy that stops at the island". `gallic.figure.honoratus` says: "Nothing about his episcopate at Arles ... is in this world's evidence," and "that his see was Arles from 426, is the editorial apparatus's identification ... carried as such."
  2. As a result, the main story says Arles and implies reluctance, the teaser says "the priest's headband", and the telling says "made a presbyter". A reader is told about two different offices.
  3. "the record says" is the wrong attribution. The source is Hilary's funeral sermon, a Tier 3 eulogy whose wording is Inferential-Thin, and the unit never says so.
  4. "the nearby city of Arles" is not supported. Pleiades puts Lerina/Planasia at 7.045E 43.508N and Arles at 4.631E 43.678N, about 195 km apart.
  - On the "Arles" highlight: "Hilary came after him" is ambiguous on a page that also names Hilary of Poitiers (`relations_summary`).
- **Proposed fix (unit 3, after B1/B2):** "His disciple Hilary later preached that the snakes gave way before him. Honoratus wanted to stay a monk, but the priesthood found him on the island. Later, he became a bishop himself." For the Arles highlight: "A city of Roman Gaul, now Arles in France. Hilary, Honoratus's disciple, preached his life here. Editors identify Honoratus's own see as Arles."

### B4. Tier 3 wonders stated as fact
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 5
- **Quote:** "Martin once brought a dead catechumen, a new believer not yet baptized, back to life. Another night the devil came to him dressed as Christ. Martin refused him."
- **What's wrong:** The hedge is lost and a not_for is breached. `gallic.story.raising-of-the-catechumen` is Tier 3, "Inferential-Thin for the specific event", and its not_for is "evidence that the miracle really happened, which the record does not assess". `gallic.quote.martin-on-the-christ-with-wounds` calls the event "a Tier-3-shaped wonder ... told by an author who was not present". Its not_for is "an independently witnessed event". The narrator states both events flatly. ("Another night" also wrongly implies the raising happened at night.)
- **Proposed fix:** "Sulpitius tells how Martin brought a dead catechumen, a new believer not yet baptized, back to life. He also tells how the devil once came to Martin dressed as Christ, and Martin refused him."

### B5. The exorcist warning is wrongly attributed, overstated, and framed as a reply to Martin
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 5
- **Quote:** "Cassian warned that a monk who boasts of casting out demons has already failed."
- **What's wrong:**
  - The speaker is Abbot Nesteros (Conf. XV.7), reporting "our predecessors". The source (npnf211 l. 39903-39906) says: "our predecessors never reckoned those as good monks or free from the fault of vainglory, who professed themselves exorcists among men". `gallic.gravity.virtus`: "Abbot Nesteros goes further still. No one who declared himself an exorcist ... was ever counted a good monk."
  - "has already failed" is stronger than "never reckoned ... as good monks".
  - Placed right after Martin's wonders, the sentence reads as Cassian answering Martin. `gallic.figure.cassian`: "He never mentions Martin". `gallic.gravity.virtus`: "Neither names the other; whether Cassian's refusal is a veiled answer to Sulpitius is not settled." `gallic.core.gallic` cautions: "Never say one house knew, argued with, or compared itself to the other."
- **Proposed fix:** "Cassian, who never mentions Martin, wrote no stories of wonders at all. In his Conferences, an Egyptian elder says the fathers never counted a monk good if he showed off his power over demons."

### B6. Purity of heart and discretion presented as the south's own invention; "what matters most" is unsupported
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 5
- **Quote:** "The south named its goal purity of heart. Cassian taught that fasting and night prayer were only aids toward it. What matters most is discretion, which he called the mother of all virtues."
- **What's wrong:**
  - `gallic.core.gallic` cautions: "The southern teaching came from the fathers of Egypt and the East: the customs, **purity of heart**, the twelve psalms, the eight faults. **Always name it as theirs, never as Gaul's invention.**" `gallic.gravity.interior-road` not_for: "the program as documented Gallic practice ... when it is Egypt's teaching received through Cassian".
  - `gallic.term.discretion`: the title is given "by the judgment of the blessed Antony" in a council reported by Abbot Moses, so "he called" is a wrong attribution.
  - "What matters most is discretion" is a ranking no record makes. The record calls discretion "mother ... guardian and regulator". Conf. XV.7 (in `gallic.gravity.virtus`) calls humility "the mistress of all virtues".
- **Proposed fix:** "From the fathers of Egypt, the south received a goal: purity of heart. Fasting and night prayer were only aids toward it. Their guide was discretion, which the Egyptian fathers called the mother of all virtues."

### B7. "Changing only what the colder climate required" contradicts Cassian's own method
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 4
- **Quote:** "brought their customs home to Gaul, changing only what the colder climate required."
- **What's wrong:** `gallic.quote.cassian-adapts-egypt-to-gaul` (verbatim, Inst. Pref.) says: "either because of the severity of the climate, **or owing to some difficulty or diversity of habits**, is impossible in these countries ... I shall to some extent balance it by the customs of the monasteries which are found throughout Pontus and Mesopotamia." `gallic.gravity.egypt-as-measure`: "Gaul's climate **or circumstances**". The word "only" is false.
- **Proposed fix:** "brought their customs home to Gaul. He changed them only where Gaul's cold climate or its different habits made them impossible."

### B8. The grace argument's "beginning" loses its attribution and is stretched to Rome
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 6
- **Quote:** "The south's best-known argument began as a worry at prayer. ... That answer grew into a long argument over how much of a monk's progress is God's gift and how much is his own. It later reached Rome."
- **What's wrong:**
  - The old text said "began, **by its own account**". `gallic.gravity.grace-and-effort` says "the moment **the tradition's own text says** the argument began". The pass dropped the attribution, so a literary framing in Cassian now reads as a historical origin.
  - The story record says "That morning's answer grew into **the whole Conference**", meaning a book, not "a long argument".
  - The story's `claim_guards` say: "participant is asking about Prosper, Celestine's letter ... no Native voice narrates that, and **this story must not be stretched to cover it**." Unit 6 builds a causal chain from Chaeremon's answer to Rome.
- **Proposed fix:** "By Cassian's own account, the south's best-known argument began as a worry at prayer. ... That morning's answer grew into a whole Conference on how much of a monk's progress is God's gift and how much is his own. That book was later attacked as far away as Rome. No one in these houses wrote down what happened there."

### B9. Unit 7 breaches two not_for lines and the no-contact caution
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 7
- **Quote:** "On bishops and councils, the two households disagreed. At Tours, Martin kept his distance from other bishops. ... In the south, church councils were trusted as guardians of the truth."
- **What's wrong:**
  - "Martin kept his distance from other bishops" is given as a standing trait before Trier. `gallic.story.trier-and-the-ithacian-communion` not_for: "Martin's rejection of synods as a general principle, **when it follows one forced act**". No record says he avoided bishops before Trier.
  - "In the south, church councils were trusted" applies Vincent's view to the whole south. `gallic.gravity.authority-ambivalence` not_for: "Martin's distrust of bishops or **Vincent's reverence for councils as every voice's view, when each rests on one house**". That record also shows that at Marseilles "the office is a temptation" and the Massilians "clung to their views in spite of the authority of the Pope". Vincent's object was "**an ancient General Council**", not "church councils" in general.
  - "the two households disagreed" suggests a dispute between them. `gallic.core.gallic` cautions: "Never say one house knew, argued with, or compared itself to the other."
- **Proposed fix:** "The two households held opposite views of bishops and councils, though neither ever wrote about the other. At Tours, bishops had opposed Martin's election. At the emperor's court in Trier, Martin once took communion with bishops he had refused, to save lives. He regretted it for the rest of his life and never attended a synod again. On Lérins, Vincent trusted the decrees of an ancient general council to guard the faith."

### B10. Unit 8 pronoun makes Sulpitius the dying traveller
- **Severity:** BLOCKING (it misleads, especially read aloud)
- **Where:** `orientation.story` unit 8
- **Quote:** "He was never present for the events he describes, and he says so himself. When Martin's death drew near, he traveled to make peace among quarreling clergy. His monks wanted to lay him on straw."
- **What's wrong:** The subject of the three sentences before it is Sulpitius, so "he traveled" and "His monks" read as Sulpitius. The record (`gallic.story.death-of-martin-at-condate`) is about Martin.
- **Proposed fix:** "Knowing his death was near, Martin went to make peace among quarreling clergy. As he lay dying, his monks wanted to put straw under him. He kept to sackcloth and ashes, so as not to leave them a different example."

### B11. Unsupported and overstated portrait of Sulpitius
- **Severity:** BLOCKING
- **Where:** `orientation.story` unit 8
- **Quote:** "Sulpitius Severus was a layman who gave up his career to follow Martin. He was never present for the events he describes"
- **What's wrong:**
  - "layman", "gave up his career" and "to follow Martin" are in no record. A grep of `records/gallic/` finds no such claim. `gallic.figure.sulpitius` gives only "an Aquitanian 'of an illustrious family' who visited Martin at Tours". "To follow Martin" also suggests he joined Martin's community, which no record says.
  - The same figure record says he "visited Martin at Tours" and had his facts "partly from himself", so "never present for the events he describes" goes too far. He disclaims presence at the specific events (the death, Letter III; the youth, Vita XXV).
- **Proposed fix:** "Almost everything known about Tours comes from one writer, Sulpitius Severus, a wealthy Aquitanian who visited Martin at Tours. He saw none of the events in these stories himself. He says he learned them from Martin and from the people who lived with him."

### B12. Discharge card date "c. 360" is not in the evidence
- **Severity:** BLOCKING
- **Where:** `documented_stories` gallic.story.discharge-before-caesar, `when`
- **Quote:** "c. 360, before a battle in Gaul, on the eve of Martin's discharge from the Roman army"
- **What's wrong:** `gallic.figure.martin` says: "The year of his birth, of the cloak, **of the discharge**, and of the election are not given in the text". The story's absent_detail says: "The text gives no year". Any date depends on identifying "Julian Caesar" as Julian the Apostate, which the not_for bars: "the editors' identification of Julian and Worms as the text's own". OG-40 also calls it "360s", which disagrees with "c. 360". (This field predates the pass but was re-shipped.)
- **Proposed fix:** "Before a battle in Gaul, when Martin left the army; the text gives no year"

### B13. Trier card date contradicts the telling on the same page, and "companions" is unsupported
- **Severity:** BLOCKING
- **Where:** `documented_stories` gallic.story.trier-and-the-ithacian-communion, `when`
- **Quote:** "385/386, after the execution of Priscillian and his companions at Trier"
- **What's wrong:** No record gives 385/386. A grep of `records/gallic/` finds nothing. The story record says: "The text gives no year; Gallus says only that Martin 'lived sixteen years after this'", and adds "carried as given, not converted to a year". The PR's telling says "He lived sixteen more years". With Martin's death in 397, which the next card states, that puts Trier in 381, not 385/386, so the page contradicts itself. "and his companions" is also unsupported. The absent_detail says "The Priscillianists themselves are not narrated here", and the record mentions only Priscillian.
- **Proposed fix:** "After Priscillian was put to death, while Maximus ruled at Trier; the text gives no year"

### B14. Discharge teaser: "Before morning" contradicts the record
- **Severity:** BLOCKING
- **Where:** `documented_stories` discharge-before-caesar, `teaser`
- **Quote:** "Before morning, the enemy asks for peace."
- **What's wrong:** The record `text` says "On the following day the enemy sent envoys to ask for peace". `tellable_as` says "The next day the enemy asks for peace". The PR's telling says "On the following day". (Also: "walk at the enemy" is awkward.)
- **Proposed fix:** "Called a coward for refusing to fight, a soldier offers to face the enemy unarmed. The next day, the enemy asks for peace."

### B15. Brictio teaser: "within the hour" is invented
- **Severity:** BLOCKING
- **Where:** `documented_stories` brictio-in-the-courtyard, `teaser`
- **Quote:** "then begs pardon within the hour."
- **What's wrong:** The source (npnf211 l. 5323-5327) says only "with rapid steps he rushed back ... Speedily, then, he returns". The record says "quickly turned back", and `tellable_as` says "soon comes back". No hour is given. The phrase was carried over from the old main story.
- **Proposed fix:** "A presbyter, a priest Martin raised from boyhood, rages at him, then soon comes back to beg pardon. Martin will not remove him. If Christ bore with Judas, why not Brictio?"

### B16. Angel telling misstates what "the East never heard"
- **Severity:** BLOCKING
- **Where:** gallic.story.the-angel-and-the-twelve-psalms, `telling`, final paragraph
- **Quote:** "In Gaul the twelve were kept, together with a hymn of praise called the Gloria, which Cassian says was never heard in the East."
- **What's wrong:** The source, Inst. II.8 (npnf211 l. 17312-17316), says: "That practice too which we have observed in this country—viz., that while one sings to the end of the Psalm, **all standing up sing together with a loud voice**, 'Glory be to the Father...'—we have never heard anywhere throughout the East". The new thing is the practice of everyone singing the doxology aloud, not the doxology itself. `gallic.core.gallic` says "the loud Gloria the East never heard". "A hymn of praise called the Gloria" also suggests to a modern reader the Gloria in excelsis, which is a different text.
- **Proposed fix:** "In Gaul the twelve were kept. Cassian adds one custom of our own, which he says the East never had: at the end of each psalm, everyone stood and sang 'Glory be to the Father' aloud together."

### B17. Angel telling breaches its own not_for
- **Severity:** BLOCKING
- **Where:** gallic.story.the-angel-and-the-twelve-psalms, `telling`, final paragraph
- **Quote:** "Cassian names no witness who saw the angel, and nothing in our record says what the brothers at Tours sang."
- **What's wrong:** The story's not_for includes "Martin's angels or **the singing at Tours**" and "**a remark about this record's own coverage, sources or scholarly attribution**". The coda does both. The story's `claim_guards` already keep Tours singing out of this story.
- **Proposed fix:** "Cassian names no one who saw the angel himself."

### B18. Honoratus telling misstates the source limit
- **Severity:** BLOCKING
- **Where:** gallic.story.honoratus-and-the-island, `telling`, paragraphs 1 and 4
- **Quote:** "as far as the rough copy of that sermon can be read." / "This is the closest our record comes to Lerins itself."
- **What's wrong:** The story record's absent_detail says "Hilary's sermon **exists in full, unread here beyond these lines**". Its divergence_note says the limit is "rough OCR of the Latin ... its sense not verified". The roughness is in this build's digitized text, not in the sermon's ancient transmission. "The rough copy of that sermon" tells participants the sermon survives only in a bad copy, which is false. (`gallic.gravity.monk-bishop` carries the same wrong phrase, "His Latin survives only in a rough copy". Fix that record separately.) "Our record" is build language in an emic voice.
- **Proposed fix:** Paragraph 1: "...preached his life at his death. This is how our community at Lérins remembers its founder, though only part of that sermon is told here, and its Latin is hard to read." Paragraph 4: "This is the nearest we come to Lérins itself. We can tell how the founder arrived and was made a priest there. What anyone did on the island in between, no one wrote down for us."

### B19. Germanus telling: "first arose" overclaims, and two separate teachings are merged
- **Severity:** BLOCKING
- **Where:** gallic.story.germanus-scruple-at-morning-service, `telling`, paragraphs 1 and 4
- **Quote:** "Cassian describes how the question of grace and effort first arose." / "Later Chaeremon says that grace works together with the human will, and that the human mind cannot fully understand how both are true."
- **What's wrong:**
  - The record says "how the question of grace and effort **came up** in Egypt". "First arose" turns one occasion into the origin of the whole question, on a matter the record set treats as contested (`gallic.contested.beginning-of-good-will`).
  - The record's body note says XIII.13 and XIII.18 are "two separate teachings from two non-adjacent chapters ... **each carried as its own record rather than joined**." The telling joins them and drops the three stages, so "how both are true" now points at the wrong pair. In the record the paradox is "all three stages of the good ... are God's gift, **yet none of them takes away free will**."
  - "missing from our edition" is build language in participant text.
- **Proposed fix:** Paragraph 1: "...Cassian describes how the question of grace and effort came up for him and Germanus." Paragraph 4: "That morning's answer grew into the whole Conference. Later, Chaeremon says that grace works together with the human will. Elsewhere he says that wanting the good, doing it and holding on to it are all God's gifts, yet none of them takes away free will. How both are true, he says, the human mind cannot fully grasp. What he taught about chastity the night before is lost to us in English."

---

## B. Rigor: SHOULD-FIX

### S1. Funeral number loses its "it is said"
- **Where:** `orientation.story` unit 8
- **Quote:** "Sulpitius says almost two thousand monks gathered for his funeral."
- **What's wrong:** The record says "The monks alone **are said to** have gathered", and the divergence_note says "The funeral's numbers are given as report". `tellable_as` says "it is said". The telling keeps the hedge ("are said to have gathered"); the main story drops it.
- **Proposed fix:** "Sulpitius reports that almost two thousand monks were said to have gathered for his funeral."

### S2. Postumianus's line is merged with a different quote
- **Where:** `orientation.story` unit 4
- **Quote:** "Sulpitius has a traveler from Egypt say that Martin alone was worth all its hermits put together."
- **What's wrong:** `gallic.quote.postumianus-you-have-conquered-all-the-eremites` has "you have conquered all the eremites and anchorites". Its not_for is "the claim that Europe needs only Martin, which sits in gallic.quote.europe-will-not-yield-having-only-martin". "Martin alone" comes from that other quote.
- **Proposed fix:** "Sulpitius has a traveler just back from Egypt admit that Martin had outdone all its hermits."

### S3. "Both called themselves keepers" / "Both households also agreed" go beyond the evidence
- **Where:** `orientation.story` units 1 and 4
- **Quote:** "Both called themselves keepers of what came before them." / "Both households also agreed that nothing true could be new."
- **What's wrong:** "Keeper" is Vincent's word (Comm. ch. 22). For Tours, `gallic.gravity.received-not-invented` has one episode, Martin refusing an unattested tomb (Vita XI), and says "none cites another". Its not_for is "the test as consistently applied, when that is contested in gallic.contested.who-holds-antiquity". "Agreed" also suggests contact, which the core caution forbids.
- **Proposed fix:** Unit 1: "Both looked back to what came before them, not to anything new." Unit 4: "Each house, in its own way, distrusted anything new."

### S4. Election title overstates the trick
- **Where:** `documented_stories` election-at-tours, `title`
- **Quote:** "The Monk Tricked Into the Bishop's Chair"
- **What's wrong:** The trick only drew Martin out of the monastery. The crowd's vote and the consecration made him bishop. The not_for bars "Martin's reluctance as proven fact, a claim contested in gallic.contested.election-as-capture".
- **Proposed fix:** "The Monk Lured Out to Be Made Bishop"

### S5. Trier telling joins the Sacred History and the Dialogues without saying they tell different moments
- **Where:** trier-and-the-ithacian-communion, `telling`, paragraph 1
- **Quote:** "Martin begged at court that none be sent ... In his Sacred History, Sulpitius states Martin's view that a worldly ruler judging a church case was a shocking wrong."
- **What's wrong:** The not_for bars "the earlier phase told in Sulpitius's own voice as one account with the Dialogues, when the two accounts remain distinct". The record says the Sacred History "narrates an earlier phase", before the execution. The telling drops "earlier".
- **Proposed fix:** "In his Sacred History, telling of an earlier visit before Priscillian's death, Sulpitius states Martin's view..."

### S6. Trier teaser: motive and "troops"
- **Where:** `documented_stories` trier, `teaser`
- **Quote:** "so that troops will not be sent to hunt heretics in Spain."
- **What's wrong:** Tribunes were officers with power over life and death, not "troops". The immediate price was also lives: Maximus "ordered executioners for the very people Martin had pleaded for", and Martin promised communion "if these people's lives were spared and the tribunes recalled".
- **Proposed fix:** "A bishop shares communion with men he had refused, to save lives and stop officers being sent to hunt heretics in Spain. He never fully forgives himself."

### S7. Honoratus teaser: lost hedge and "singing"
- **Where:** `documented_stories` honoratus, `teaser`; also unit 3
- **Quote:** "A founder walks unafraid onto an island shunned for its snakes, singing a psalm. ... Then the priest's headband catches the man who ran from it."
- **What's wrong:** `tellable_as` keeps "as far as his sermon can be read"; the teaser drops it. The record has "In heart and mouth he carried a psalm"; "singing" is not in it. "The priest's headband ... it" is unclear: a reader cannot tell what "it" refers to, and the image is never explained.
- **Proposed fix:** "A founder walks unafraid onto an island shunned for its filth and snakes, a psalm on his lips. The snakes give way. Then, his disciple says, the priesthood he had run from caught up with him there."

### S8. Chaeremon highlight: made-up causal link, and the source is flattened
- **Where:** `highlights` "an elder" / Chaeremon
- **Quote:** "Cassian wrote down his answer much later in Gaul, so the speeches are Cassian's own composition."
- **What's wrong:** The record says the speeches are "Cassian's composition **of what he heard**". "Own composition" with "so" implies invention, and the cause is the reviewer's inference, not the record's.
- **Proposed fix:** "Chaeremon, an old man whose cell stood near Panephysis in Egypt. Cassian wrote down his words decades later in Gaul, so they are Cassian's retelling, not a transcript."

### S9. Discretion and purity-of-heart highlights credit Cassian with Egypt's teaching
- **Where:** `highlights` "discretion", "purity of heart"
- **Quote:** "Cassian's word for the judgment that keeps each virtue from going wrong." / "Cassian ranked fasting and night prayer as aids to it"
- **What's wrong:** This is the same reception breach as B6. `gallic.term.discretion` gives the title "by the judgment of the blessed Antony"; `gallic.term.purity-of-heart` has the teaching arrive "as Abbot Moses's", framed by Cassian as received from Egypt.
- **Proposed fix:** "The Egyptian fathers' word, passed on by Cassian, for the judgment that keeps each virtue from going wrong..." / "The Egyptian fathers, as Cassian reports them, ranked fasting and night prayer as aids to it, never as the point."

### S10. Priscillian and Maximus highlights: unclear sources and meta-language
- **Where:** `highlights` "Priscillian"; "the emperor's court" (Maximus)
- **Quote:** "A hostile writer sums up the charges." / "The record calls him a usurper."
- **What's wrong:** The "hostile writer" is Sulpitius himself (Sacred History; story absent_detail), not some other writer. "Usurper" is not Sulpitius's word in the vendored text; it is the build's own framing in `gallic.force.court-at-trier`. "The record calls" offers a build artifact as if it were a source.
- **Proposed fix:** "Sulpitius, who was hostile to him, sums up the charges in his Sacred History." / "The emperor was Maximus, who had seized power. At Trier he shielded Ithacius, who had accused Priscillian."

### S11. Cloak telling repeats a "first" claim the source does not make
- **Where:** the-cloak-at-amiens, `telling`, sentence 1
- **Quote:** "Sulpitius tells us how Martin began, before any monastery existed in Gaul."
- **What's wrong:** The words come from the record's framing, but the sourced locus (Vita II-III) does not say it, and "Sulpitius tells us" attributes it to him. The pass's own body note rejected "the West's first monastery" as unsupported.
- **Proposed fix:** "Sulpitius tells us how Martin began, while he was still a soldier."

---

## C. Craft: SHOULD-FIX

### C1. "Record" used as meta-language in participant text, with formulaic endings
- **Where:** unit 3 "the record says"; unit 5 "Tours built its record on power"; unit 6 "The record never settles it."; unit 7 "The record leaves that disagreement standing."; unit 8 "The record closes around 450"; highlights "synod" ("The record leaves both views standing."), "virgins" ("The record names none of them"), Maximus; tellings: angel and Honoratus "our record", Germanus "our edition".
- **What's wrong:** This is build language the brief bans. Units 6, 7 and 8 also all end on the same unresolved-argument summary, which is an AI tell.
- **Proposed fix:** Unit 6: end at "...as far away as Rome." Unit 7: end at the Vincent sentence (B9 fix). Unit 8: "The story closes around 450, with the argument over grace and effort still open." Synod: "...ancient councils were trusted to guard the faith." Virgins: "No woman among them is named, and none speaks." Unit 5: "Tours told its story through power instead."

### C2. Ten tellings follow one template
- **Where:** all ten `telling` fields
- **Quote:** Openings: "Sulpitius tells us how Martin left the army" / "Sulpitius tells us how Martin began" / "Sulpitius tells us about the first of Martin's works" / "Sulpitius tells us how Martin, a monk, became bishop". Endings: every telling ends with a source-limits paragraph ("the text gives no year" in four; "He was not present", "never names him", "never heard", "missing from our edition").
- **What's wrong:** All ten are 239-250 words and four paragraphs long, and all end the same way. This is the uniform "generic AI voice" polish the project names as a fabrication risk. Read in sequence, it sounds produced, not remembered.
- **Proposed fix:** Vary the way in. For example, discharge: "Martin left the army at a pay parade, on the eve of a battle." Election: "Tours wanted Martin, but he would not leave his monastery." Fold the limits into the telling where they belong, instead of a closing coda in every one. Example for the cloak: "...Sulpitius had this from Martin and his companions, years later." Keep a separate coda only where the limit is the point (Brictio, Honoratus).

### C3. Register slips in the emic tellings
- **Where:** the death telling (no emic marker at all); "the text", "the account says", "the text provides no year" throughout; Trier "Treves, now Trier"; Honoratus "the rough copy"
- **What's wrong:** Tellings are meant to be the tradition speaking of itself ("we", "our"). Several read as an outside narrator, or as a scholar describing a document, especially in their codas.
- **Proposed fix:** Death, final paragraph: "Sulpitius does not name the city where they carried him, and the numbers came to him by report. The choir of virgins is the only trace of the women who took up this life with us, and none of them speaks." Use "Sulpitius gives no year" instead of "the text gives no year".

### C4. Choppy main-story cadence and template parallelism
- **Where:** units 2, 3, 5, 7, 8 (average 10.6-11.9 words per sentence); unit 4 "In the south, that meant reception. ... In the north, it meant comparison."
- **Quote:** "Martin refused him. The only Christ he would accept..."; "It later reached Rome. The record never settles it."
- **What's wrong:** The writing standard asks for roughly 12-20 words on average. These units run below that in clipped bursts. Unit 4 rests on two nominalizations set in a matched pair.
- **Proposed fix:** Join the clipped pairs, as in the B4, B8 and B10 fixes. Unit 4: "The south took Egypt's customs as a rule to keep. The north set Martin beside Egypt's hermits and claimed he outdid them."

### C5. Unit 1 never says what the "one idea" is
- **Where:** `orientation.story` unit 1
- **Quote:** "two households of monks lived out one idea."
- **What's wrong:** The unit never names the idea. The tile does ("a monk does not stop being a monk just because the Church makes him a bishop"), but the spoken story is heard on its own.
- **Proposed fix:** "...two households of monks lived out one idea: a monk made bishop must stay a monk."

### C6. Unit 2: "Julian, then Caesar" sounds like two commanders
- **Where:** `orientation.story` unit 2
- **Quote:** "While he served under Julian, then Caesar, he asked for his discharge before a battle."
- **What's wrong:** Heard aloud, it sounds like he served Julian and then Caesar. The text's own name is "Julian Caesar".
- **Proposed fix:** "Before a battle, he asked his commander, Julian Caesar, for his discharge."

### C7. Pronouns and references with nothing to point back to
- **Where:** Trier telling "Yet the bishops could never get him to sign it."; angel telling "through the angel's own act"; Honoratus telling "Near the city lay an island"; Germanus teaser "The old man cuts the service short"
- **What's wrong:** "It" has no document to refer to. The angel is never identified as an angel. No city has been named. "The old man" has not been introduced.
- **Proposed fix:** "...but they could never get him to sign their decision." / "The fathers understood that the singer had been an angel, sent by Providence to fix the rule." / "Near Leontius's city lay an island..." or simply "There was an island off the coast..." / "Two friends come to morning prayer troubled by something an old monk said the night before. He cuts the service short..."

### C8. Cloak telling: translationese and hard sentences
- **Where:** the-cloak-at-amiens, `telling`
- **Quote:** "The son of a military tribune, an army officer, Martin was seized at fifteen on his father's information" / "One unusually harsh winter was proving fatal to many from the cold."
- **What's wrong:** "On his father's information" is archaic and opaque. "An army officer" could be glossing Martin or the tribune. The winter sentence is stiff translation English.
- **Proposed fix:** "Martin's father was a tribune, an army officer. When Martin was fifteen, his father reported him, and he was seized and made to swear the soldier's oath." / "One winter was so harsh that many people were dying of cold."

---

## D. NITs

- **N1.** Spelling is inconsistent: "Lérins" (main story) vs "Lerins" (tellings); US "quarreling/traveled/plow" (main story, death teaser) vs UK "quarrelling/travelled/ploughs" (tellings). Pick one.
- **N2.** Angel title "The Angel Who Fixed the Psalms": "fixed" also means "repaired". Use "The Angel Who Set the Number of Psalms".
- **N3.** Election teaser "feigns a sick wife" is above B2 level. Use "pretends his wife is sick".
- **N4.** Brictio teaser "presbyter" is not glossed (the telling glosses it). Covered by the B15 fix.
- **N5.** "Condate" highlight: "The church where Martin went" should be "The village where Martin went to settle a quarrel among the clergy of its church". Pleiades: "An ancient settlement located in the modern French commune of Candes-St-Martin".
- **N6.** The "Sulpitius" highlight states "of an illustrious family" flatly. `gallic.figure.sulpitius` says it is "by the vendored volume's own introduction". Use "said by his editors to come from a leading family".
- **N7.** Unit 1: "the nearby city of Marseilles" is about 136 km from Lérins (Pleiades). Use "the city of Marseilles, further west along the coast".
- **N8.** OG-40 says `documented_stories` are "in date order". They are not consistent by either event date (the angel story is set earliest) or writing date (Honoratus's founding, c. 400-410, comes before the Institutes). Fix the claim or the order.
- **N9.** Germanus telling "for the brothers Honoratus and Eucherius" can be heard as siblings. Use "for two monks, Honoratus and Eucherius".

**Place checks that passed (Pleiades):** Tours/Caesarodunum 138255, Massalia 148127 (founded c. 600 BC by Phocaean Greeks), Lerina = Île Saint-Honorat 157906, Samarobriva = Amiens 109321, Augusta Treverorum = Trier 108894, Arles 148217, Reii = Riez 157805, Condate = Candes-Saint-Martin 138305 (hedged as "probably"; acceptable), Andethanna = Niederanven 108743 (hedged; acceptable), Panephysis / el-Manzala 727184. The URLs and identifications are correct. The defects are in the notes (B1, B3, N5).

---

## E. Outside the requested fields, but material

- **The world_front body note is stale and false.** It is process commentary inside a canonical file (`Build/worlds/`), lines 445-713. It says Brictio "is voiced directly in `orientation.story`'s tenth paragraph" (the story now has 8 units and no Brictio), says "`narrative.questions` is left EMPTY" (it has four entries), and says "no repeated first name" (Hilary of Poitiers and Hilary of Arles both appear). CLAUDE.md requires a PR that edits a canonical file to remove the commentary in it. `tools/check_live_commentary.py --base origin/main` does not flag it, so the tool will not catch it.
- **OG-40 contains false statements.** It says Faustus of Riez was cut (B1) and that the stories are in date order (N8). It also records a round-1 review "PASS" over a text with the defects above.
- **`gallic.gravity.monk-bishop`** says "His Latin survives only in a rough copy". This is the source of B18 and contradicts the Honoratus story's own absent_detail.
- **`orientation.voices`** (Honoratus): "went alone to an island" repeats the contradiction in B2.

---

## Verdict

**NOT APPROVED TO PROCEED.** The pass is shorter and easier to read than the text it replaced. But the cutting removed hedges that the old text had ("by its own account", the Tier 3 framing, "it is said"). It also introduced new unsupported facts: Sulpitius as a "layman who gave up his career", "within the hour", "before morning", "only what the colder climate required". It kept a post-horizon claim the gaps log says was removed (Faustus), and shipped two dates that conflict with the records and with each other (c. 360; 385/386 against "sixteen years"). The Honoratus material now gives three different offices across the main story, teaser and telling. Four main-story units (4, 5, 7 and 8) carry more than one BLOCKING defect each. The angel telling misreports its own vendored source on the Gloria.

**Counts:** BLOCKING 19 · SHOULD-FIX 19 (rigor 11, craft 8) · NIT 9

Per CLAUDE.md, these blocking findings need independent re-confirmation after the fix. The author cannot self-certify them closed.
