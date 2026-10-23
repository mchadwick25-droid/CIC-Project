Review round 1, desert record wording pass (spoken fields), 2026-10-13, reviewer: independent Opus subagent

Verdict: BLOCKING

Scope: commit 5d581f0 ("desert records: fix source drift, renderings and AI-tell wording in spoken fields"), 92 files under records/desert, 122 changed fields. The pass was briefed as an uncommitted diff, but it is now committed as HEAD with a clean working tree, so it was reviewed as `git diff HEAD~1 HEAD -- records/desert`. Every changed field was compared against the change list (merged.json). The YAML front matter of each file was parsed at HEAD~1 and at HEAD. Exactly the 122 listed fields changed, and every new value equals the listed `new`. No body text and no other key changed. Only demonstration, doctrinal_witness, figure, honest_limit, quote, story and term records were touched. No build record (force, gravity, source, voice_craft, world_core, contested_claim) changed. Every changed exchange turn is a representative turn. All 122 new values pass `grade_text` (FK <= 10, FRE >= 60). Facts were checked by grep against cic/texts/ (npnf204 Vita Antonii, npnf211 Cassian, palladius_lausiac-history_clarke1918, palladius_paradise-v1-syriac_budge1907, anan-isho_paradise-v2-sayings_budge1907, evagrius_praktikos_dysinger, macarius_fifty-spiritual-homilies_mason1921, pachomius_rules-ethiopic_schodde1885, origen_philocalia_lewis1911, anf04, anf09) and against the records' own use_note, divergence_note and absent_detail fields.

## Findings

1. **desert.dw.the-heart-and-the-spirit, text**
   - Old: `There was another voice among us besides our most systematic teacher's, and we will not flatten it into his. That teacher had the mind clear itself until it saw its own proper radiance.`
   - New: `Besides our most systematic teacher, we carried another current, and we will not flatten it into his. It came down in homilies under the name of Macarius, though no outside evidence shows he wrote them. That teacher had the mind clear itself until it saw its own proper radiance.`
   - Source: the record contrasts the Evagrian mind that sees its own radiance with the Macarian soul lit by Someone else.
   - BLOCKING. The inserted sentence is correct on authorship (Mason p. xviii: "rests upon no external evidence"). But it now stands between "our most systematic teacher" and "That teacher", so "That teacher" now points to Macarius, the nearest "he". A listener will hear the Evagrian teaching given to Macarius, and the contrast with "This other current" falls apart. Change "That teacher had the mind clear itself..." to "Our most systematic teacher had the mind clear itself...".

2. **desert.quote.antony-on-living-near-kin, modern_rendering**
   - Old: `...freed him from all the worry and work of daily life. This let him give himself completely to reading and prayer...`
   - New: `...freed him from all the care and worry of daily work. He gave himself only to reading and prayer, without ceasing and without any distraction of spirit.`
   - Source: npnf211 Conf. XXIV: "boasted that by their provision he was set free from all care and anxiety of daily work, and gave himself up ceaselessly and solely to reading and prayer".
   - NON-BLOCKING. Removing the added causal "This let him" was right. In Cassian, though, the devotion is still part of the man's boast. As a separate sentence it becomes the narrator's own statement of fact. Write "He boasted that ... and that he gave himself only to reading and prayer...", or start the sentence with "He said he gave himself...".

3. **desert.quote.never-held-communion-with-the-schismatics, modern_rendering**
   - Old: `...contact with such people harmed the soul, and could destroy it.`
   - New: `...contact with such people harmed the soul and destroyed it.`
   - Source: npnf204 VA 68: "intercourse with these was harmful and destructive to the soul".
   - NON-BLOCKING. "Could destroy" was too weak, but "destroyed it" is too strong. It reports destruction as something that actually happened, where the text names what such contact tends to do. Use "was harmful and destructive to the soul".

4. **desert.quote.never-kneel-saturday-to-sunday, modern_rendering**
   - New: `...the Egyptians never knelt. Nor did they kneel from Easter until Pentecost. Nor at these times did they keep a rule of fasting...`
   - Source: npnf211 Inst. II.18 l.17736: "among the Egyptians they never kneel ... nor do they at these times observe a rule of fasting".
   - NON-BLOCKING. Cassian writes in the present tense, as a witness to current custom ("This, too, we ought to know"). The rewrite fixed the other errors but kept the old past tense. The past-tense rule applies to we-voice fields, not to renderings, and here the change shifts his testimony. Use "never kneel ... Nor do they kneel ... Nor ... do they keep a rule of fasting".

5. **desert.quote.the-kingdom-is-apatheia, modern_rendering**
   - New: `The mind, the nous, takes in this knowledge as far as it is able, and the knowledge makes it incorruptible.`
   - Source: evagrius_praktikos_dysinger.txt ch. 3: "knowledge of the Holy Trinity exercised according to the capacity of the nous ... and bestowing incorruptibility upon it".
   - NON-BLOCKING. "Exercised" means knowledge the mind actively uses. "Takes in" turns it into something the mind passively receives. Use "The mind, the nous, exercises this knowledge as far as it is able...".

6. **desert.quote.the-soul-becomes-all-eye, modern_rendering**
   - New: `Then the beauty of his unspeakable glory shines on her, for he has prepared her to be a seat and a dwelling for himself.`
   - Source: Mason, Homily I: "irradiated by the beauty of the unspeakable glory of Him who has prepared her to be a seat and a dwelling for Himself".
   - NON-BLOCKING. The fix correctly restored the conditional "A soul may be privileged...". But "for" still reads as a cause: the glory shines because he prepared her. In the text, "who has prepared her" only identifies whose glory it is. The pass removed the same kind of added causal link from antony-on-living-near-kin. Write "...the beauty of the unspeakable glory of the one who prepared her as his seat and dwelling shines on her", or split it into two sentences without "for".

7. **desert.quote.twelve-psalms-by-an-angel, modern_rendering**
   - New: `Each man acted in proportion to his own fervor... So holy a difference of opinion arose in their pious discussion on the rule of their religion. The time for evening prayer came before the sacred question was decided.`
   - Source: npnf211 Inst. II.5: "there was such a holy difference of opinion ... that the time for their Vesper office came before the sacred question was decided".
   - NON-BLOCKING. When "such ... that" was split, the result link was lost. "So holy a difference of opinion arose." now stands as a fragment-like exclamation. "Acted" is also an added verb. A possible rendering: "Their pious discussion brought such a holy difference of opinion that evening prayer came before the sacred question was decided." That is 21 words. For the opening, "Each man, in proportion to his own fervor and unmindful of the weakness of others, thought..." or something close.

8. **desert.story.pachomius-founding, text**
   - New: `Each was to eat and work according to his own strength. The strong took the harder tasks, and the weak took what they could manage.`
   - Source: Clarke ch. XXXII [2]: "appoint the tasks that need strength to those who are stronger ... and to the weaker ... such as the weak can manage".
   - NON-BLOCKING. The tablet gives a rule. "Took" reports it as what actually happened. Keep it a rule, as the sentence before it does: "The strong were to be given the harder tasks, and the weak what they could manage."

9. **desert.story.sarah-answer, tellable_as**
   - New: `elder monks told Amma Sarah she was only a woman, and she said she was the man and they the women`
   - Source: the vendored Budge §525 has only "Mother Sarah used to say to her brethren, 'It is I who am a man, and ye who are women.'" The visit is in no vendored text. In this same pass, desert.demo.identity-collision-womens-authority added "The tradition tells" for exactly this reason.
   - NON-BLOCKING. The motive gloss is gone, which is right, but the tellable line now states the monks' challenge as fact with no frame. Write "in the tradition's telling, elder monks told Amma Sarah..." or something similar.

10. **desert.story.kellia-day, tellable_as**
    - New: `a typical day at Kellia, rebuilt from the evidence, since no one recorded a day like it`
    - Source: the record's absent_detail: "no surviving source narrates one specific day this way".
    - NON-BLOCKING. "No one recorded" claims that no record was ever made. The record claims only that none survives. Write "since no surviving record tells a day like it".

11. **desert.term.anachoresis, plain_meaning**
    - Old: `leaving settled village life for the desert's edge`
    - New: `leaving settled life for the desert as the whole work of formation.`
    - Source: the record's own evidential sense ("the settlements sat on marginal land with real village trade ties") and use_note not_for ("Presenting desert settlements as cut off from villages").
    - NON-BLOCKING. Dropping "edge" removes a true, sourced detail that the record makes a point of keeping, and the new line leans toward the misreading the record warns against. Restore "for the desert's edge".

12. **desert.dw.only-true-religion, text**
    - New: `We asked them which was nobler: to confess the Cross, or to tell of their own gods' adultery and the seduction of boys.`
    - Source: Vita §74. These are Antony's words to the philosophers.
    - NON-BLOCKING. Replacing the invented "excuse for the passions" with the Vita's own charge is correct. But the brief says an individual's reported words do not become "we said", and this new sentence turns them into "we asked". Use "One of us asked them which was nobler...".

13. **desert.story.antony-withdrawal, text**
    - New ending: `The Vita gives a reason only for the last one: crowds beset him, and he wanted quiet. Solitude, once found, draws people to it, and total withdrawal has to be sought again.`
    - Source: the record's use_note not_for: "Supplying Antony's reasons for each move, which the Vita does not give".
    - NON-BLOCKING. The added Vita sentence is sound. The kept closing line, though, is a present-tense maxim that applies the crowd reason to every move again, straight after saying the Vita gives that reason for only one. Cut the last sentence, or tie it to the last move only.

14. **Newly written sentences over ~25 words**
    - desert.quote.origen-on-the-sinning-brother modern_rendering: "Or take those who are carried away by passion, ... common among ordinary people." (30 words). The fix edited this sentence, and the rendering limit is firm.
    - desert.dw.grace-and-effort text: "It began when the old teacher told us plainly that a man may strive ... unless he has it as a gift." (37 words, new).
    - desert.demo.center-coming-to-belief exchange[1]: the new closing sentence (33 words).
    - desert.demo.identity-collision-someone-like-me exchange[1]: the new closing sentence (29 words).
    - desert.story.angel-hands-the-tablet text: "As he sat in his cave, ... now a waste." (32 words, lengthened by the fix).
    - NON-BLOCKING. Each field still passes grade_text, but the brief says no sentence should run past ~25 words. Split each one at its natural joint.

The fixes below are needed because the pass removed a defect from one record but left the same defect in another field it also rewrote. The text was already there before this pass. They are listed because each sits in a changed field and repeats a claim the pass itself judged unsupported elsewhere.

15. **desert.demo.identity-collision-divorce, exchange[1].text**
    - Still has: `He came home one day...` and `He went on to become one of the most honored among us.`
    - Source: Clarke ch. XXII: "came in suddenly from work"; Paul is "counted worthy of grace over demons and diseases" and "surnamed Simple by all the brotherhood". desert.dw.marriage-ending dropped "one of the most honored among us" in this pass as unsupported.
    - NON-BLOCKING. Make this match the dw: "came in from work", and "went on to be trusted even with a case the greatest of us sent on to him".

16. **desert.demo.identity-collision-someone-like-me, exchange[1].text**
    - Still has: `a man other people were afraid of`
    - Source: desert.dw.someone-like-me removed this in the same pass as invented. Clarke ch. XIX gives "renowned and far-famed robber".
    - NON-BLOCKING. Remove it, or use the dw's wording.

17. **desert.demo.center-how-we-know, exchange[1].text**
    - Still has: `Ask an elder a question, and he would answer with a line of Scripture rather than a teaching of his own`
    - Source: desert.force.scriptural-address, which is compiler-mediated. desert.dw.writings changed the same sentence in this pass to "he might answer with a verse chosen for your one situation".
    - NON-BLOCKING. Use the dw's wording.

18. **desert.demo.lament-suffering, exchange[1].text**
    - Still has: `A friend found him and carried him back, to grieve for him as dead. But he had himself carried back to the same tomb, rather than stay where people could tend him.`
    - Source: npnf204 VA 8 l.31466-31473: carried "to the church in the village", where kinsfolk "sat around Antony as round a corpse", and at midnight he "asked him to carry him again to the tombs". desert.story.antony-tomb-combat removed "rather than stay where people could tend him" in this pass as an invented motive. This demo is rated Contested.
    - NON-BLOCKING. Use the story's corrected wording: "carried him to the village church, where people sat around him as around a corpse. But at midnight he revived, and asked to be carried back to the same tomb."

19. **desert.demo.center-coming-to-belief, exchange[1].text**
    - Still has: `He did - he withdrew to Egypt.`
    - Source: Budge vol. II ch. I §§1-2 (l.54-56): "in the palace" ... "when Arsenius was living the ascetic life in the monastery". It does not mention Egypt. desert.story.arsenius-flee removed the withdrawal to Egypt in this pass because Budge does not support it.
    - NON-BLOCKING. Write "He did, and became a monk", or similar.

20. **desert.demo.quiet-head, exchange[3].text**
    - New: `Someone once asked what happens to a person who dies still fighting... The answer was: ...` and `Some among us did speak of a soul filled with light and truly at rest, felt and not only believed.`
    - Source: desert.dw.the-heart-and-the-spirit divergence_note: the Macarian current is "never voiced as 'one of us said'". In this pass, the dw itself changed "Someone was once asked" to "One homily asks", because Homily XXVI §18 is a literary Question/Answer and not a recorded event.
    - NON-BLOCKING. Removing "elder" and "hesychia" was right. Finish the job the same way: "One of the homilies we carried asks what happens..." and "Some of the homilies we carried speak of a soul filled with light...".

21. **desert.story.antony-call, text, and desert.story.antony-withdrawal, text**
    - Still have: `seeking out and copying an old man who was already living that way nearby` and `seeking out and copying an old man already living a solitary life near his village`
    - Source: Vita §3: "Antony, after he had seen this man, imitated him in piety". The seeking out in §3 is of other good men. desert.dw.apostolic changed "sought him out" to "saw him" in this pass on exactly this point.
    - NON-BLOCKING. In both stories, write "seeing and copying an old man...".

Every other changed field was checked against its source as the brief requires, and nothing in it needs changing. That includes all 31 quote renderings, read clause by clause against `text`, apart from those named above.
