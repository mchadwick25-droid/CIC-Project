Review round 1, pahc record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: FAIL (2 BLOCKING, 16 NON-BLOCKING)

Scope: uncommitted working-tree changes under records/pahc, compared with HEAD (`git diff -- records/pahc`): 84 files, 109 field edits. The intended edits, with the audit's reasons and source checks, are listed in the session scratchpad's `all_findings_applied.json`. The standard is the pass's own brief together with CLAUDE.md.

How the edits were checked:
- **Edit list.** Each file was parsed at HEAD and in the working tree, and the YAML values were compared leaf by leaf. Exactly 109 values changed, one for each listed edit, and each new value matches its listed fix. No quote `text` changed.
- **Participant turns.** In demonstrations, only `exchange[1]` and `exchange[3]` changed. Both are representative turns. No participant turn changed.
- **Gates.** `python -m engine.m10.cli records pahc` gives PASS.
- **Readability.** Every touched spoken field was graded with `engine.m1.gates.grade_text`.
- **Facts.** Facts were checked by grep against the vendored files:
  - cic/texts/anf01 (Ignatius, 1 Clement, Justin, Martyrdom of Polycarp)
  - anf02 (Hermas)
  - anf03 (Tertullian)
  - anf07 (Didache, anti-Montanist fragment)
  - anf08 (Melito, Hegesippus)
  - npnf201 (Eusebius, Pliny)
  - npnf204 (Athanasius)
  - the Tacitus file
  - the Lucian file

## Findings

1. **pahc.story.martyrdom-of-polycarp, tellable_as**
   - Old: `...and honored afterward with a yearly gathering at the place his bones were kept.`
   - New: `Afterward the church met each year at the place where his bones were laid.`
   - Source: anf01, Martyrdom of Polycarp 18: "whither, being gathered together, as opportunity is allowed us, with joy and rejoicing, the Lord shall grant us to celebrate the anniversary of his martyrdom". This is a hope written within the year, not a report of a yearly practice. pahc.gravity.martyrdom-meaning also says the yearly remembrance "is not yet part of this world's own worship". The same pass corrected this exact claim in pahc.demo.lament-suffering (now "They hoped to gather each year"). The record is Contested.
   - BLOCKING. The rewritten sentence states as fact, in the past tense, a practice the source only hopes for. Suggested fix: "Afterward the church hoped to gather each year at the place where his bones were laid."

2. **pahc.demo.identity-collision-someone-like-me, exchange[1] (representative)**
   - Old: `...laid open before every person as a real choice - kept daily after the water as much as before it. What that teaching asked of anyone, it asked of everyone.`
   - New: `We put both before every person, and we kept to the way of life daily after the water as much as before it. What that teaching asked of one person, it asked of all.`
   - Source: the audit's source check for this edit cites pahc.term.two-ways ("kept, daily, after the water as before it"). That wording was removed in this same pass (edits to two-ways plain_meaning, quick_meaning and senses.personal), on the ground that "a choice kept daily" is not in the Didache. The Didache prescribes. It gives only 4:2, "seek out day by day the faces of the saints", and 16:2 on being made perfect at the last time.
   - BLOCKING. The new sentence now rests on wording this pass ruled unsupported. It also changes a teaching into a claim about conduct: "we kept to the way of life daily". No source reports how members actually lived.
   - Second problem: the audit's B finding on the coined chiasmus is not fixed. "What that teaching asked of one person, it asked of all" is the same line reworded.
   - Suggested fix: "The way of life did not end at the water. It asked a person to seek out the faces of the saints day by day." Then drop or recast the chiasmus.

3. **pahc.source.anti-montanist-fragments, body**
   - New: `contested by gatherings of the faithful across Asia Minor`
   - Source: npnf201 l.29721-29722 (HE V.16.10): "the faithful in Asia met often in many places throughout Asia". This means the province of Asia. The gravity edit in the same pass says "the faithful of Asia".
   - NON-BLOCKING. "Asia Minor" is carried over from the old wording and widens the province into the whole peninsula. Use "across Asia".

4. **pahc.demo.center-how-we-know, exchange[1]**
   - New: `In Rome, on the day we gather, someone reads aloud for as long as there is time. It may be the memoirs...`
   - NON-BLOCKING. The tense is not fixed. This is the community's own past, in the present tense. The parallel sentence in pahc.witness.how-we-know was changed to "gathered ... read" in this pass. The Papias addition is sound. It paraphrases npnf201 l.20495ff closely and marks the inference as "our reading".

5. **pahc.demo.center-jesus-as-god, exchange[1]**
   - New: `It was a phrase of worship, not an argument worked out. ... We did call him God. We cannot tell you we had settled how.`
   - NON-BLOCKING. The audit named two tells, the "not an argument worked out" pivot and the balanced closing pair. Both are still there. The tense fix and the shorter text are good. Adding "Trinity" is correct, since the participant's turn uses that word.

6. **pahc.demo.identity-collision-womens-authority, exchange[1]**
   - New: `What it cost the women who held that authority, our record does not say.`
   - Source: anf02 l.1024, "Grapte will admonish the widows and the orphans". No source mentions a cost.
   - NON-BLOCKING. Removing the invented cost is correct, but the new sentence still assumes a cost existed. Use "Whether it cost the women who held it anything, our record does not say", or cut the sentence.

7. **pahc.figure.hermas, bridge_line**
   - Old: `A freedman in Rome...`
   - New: `A former slave in Rome...`
   - Source: anf02 Vision 1.1, "sold me to one Rhode in Rome".
   - NON-BLOCKING. "Former" carries the same inference of freed status that the audit objected to in "freedman". The story edits in this pass word it more carefully: "who says he was once sold as a slave" (pahc.story.hermas-visions, tellable_as and text). Align this line with them.

8. **pahc.figure.tacitus, bridge_line**
   - New: `He despised Christians, yet he thought their deaths served one man's cruelty.`
   - Source: tacitus_annals-15-44 l.68: "there arose a feeling of compassion; for it was not, as it seemed, for the public good, but to glut one man's cruelty". The reason Tacitus gives explains the crowd's pity, and it is qualified by "as it seemed".
   - NON-BLOCKING. The line gives Tacitus a personal judgment that the passage reports as public feeling. Suggested: "He despised Christians, yet he wrote that people came to pity them, since they seemed to die for one man's cruelty."

9. **pahc.witness.how-we-know (text) and pahc.witness.reading-scripture (text)**
   - New: `...alongside the words of the prophets before them.` (how-we-know) and `They read the writings of the prophets and the memoirs the apostles left.` (reading-scripture)
   - Source: anf01 l.16504 (1 Apol. 67): "the memoirs of the apostles or the writings of the prophets are read".
   - NON-BLOCKING. In pahc.demo.center-how-we-know the audit corrected "alongside" to Justin's "or" ("It may be the memoirs ... or the writings"). These two sibling fields were touched in the same pass but keep "alongside" and "and". This is a small inconsistency against the source.

10. **pahc.witness.who-was-jesus, text**
    - New: `He was truly brought before Pilate, truly crucified... So Jesus was a real man, really killed, really raised, and the one through whom we gave thanks.`
    - Source: anf01 Trallians 9: "He was truly persecuted under Pontius Pilate". The audit's own source check for pahc.demo.center-who-was-jesus says "brought before Pilate" is not in Trallians 9, and that demo now reads "persecuted under Pilate".
    - NON-BLOCKING. This field is now framed as Ignatius's words but keeps "brought before". It also keeps the three-beat summary closer that the audit removed from the matching demo as a coined line. "Others among us said the same thing more quietly" is supported by the record's divergence_note (Strand B states the same substance).

11. **pahc.quote.those-who-lived-reasonably-are-christians, modern_rendering**
    - New: `...are Christians, even if they were thought to be atheists.`
    - Text: "even though they have been thought atheists".
    - NON-BLOCKING. "Even if" turns a stated fact into a hypothetical. The sibling quote pahc.quote.justin-reasonable-livers correctly keeps "even though". "Lived by reason" is a good fix.

12. **pahc.story.first-clement-corinthian-dispute, text**
    - New: `And it calls on the Corinthians to submit to their presbyters.`
    - Source: anf01 l.2336 (1 Clem. 57): "Ye therefore, who laid the foundation of this sedition, submit yourselves to the presbyters".
    - NON-BLOCKING. The call is addressed to the people who started the revolt, not to the Corinthians as a whole. Use "calls on those who started the revolt to submit to the presbyters".

13. **pahc.story.hermas-visions, text**
    - New: `That shows a Rome led by several presbyters, with named roles for Clement and Grapte, and no single bishop.`
    - Source: anf02 l.1025-1026: "along with the presbyters who preside over the Church".
    - NON-BLOCKING. Plural presiding presbyters are shown. "No single bishop" is an argument from silence stated as something the passage shows. Use "and names no single bishop". The removal of the invented "his own household" is correct.

14. **pahc.story.one-eucharist-under-bishop, tellable_as**
    - New: `Ignatius told his people to treat only the eucharist that the bishop led, or allowed, as valid.`
    - Source: Smyrnaeans 8 is addressed to the church at Smyrna. Ignatius's own see was Antioch.
    - NON-BLOCKING. "His people" misnames who was addressed. Use "Ignatius told the churches he wrote to...". The correction on the eucharist itself ("or one to whom he has entrusted it") is right.

15. **pahc.term.ministrae, senses.personal**
    - New: `...The record keeps no name and no word of theirs, and nothing may be invented for them.`
    - NON-BLOCKING. "Nothing may be invented for them" is the build's own rule, spoken in a participant-facing field. It reads as process voice or a disclaimer. Use "...and keeps no name and no word of theirs." The removal of "seized" and of the coined closer is correct.

16. **pahc.term.two-ways, senses.personal**
    - New: `The teaching's heart was a choice, and it asked for more than one yes. The way of life included seeking out the faces of the saints day by day.`
    - NON-BLOCKING. The second sentence is sourced (Didache 4:2). "It asked for more than one yes" is a coined phrase, and it brings back in softer form the claim of repeated choosing that the audit removed as unsupported. The second sentence alone carries the sourced point.

17. **Story `text` readability (pahc.story.didache-eucharist, pahc.story.polycarp-forwards-letters, and four others)**
    - didache-eucharist: FK 9.90 to 10.41.
    - polycarp-forwards-letters: FK 10.13 / FRE 59.1 to FK 10.95 / FRE 56.9.
    - These four touched story texts were already under target and are still under it:
      - day-under-bishop-and-presbyters: FK 10.40 / FRE 51.6
      - first-clement-corinthian-dispute: FRE 55.2
      - mutual-aid-prisoner: FRE 59.6
      - nero-scapegoating: FRE 57.2
    - NON-BLOCKING. The engine does not gate story `text` (`_READABILITY_EXCLUDED_FIELDS`, because these texts quote archaic translations). The brief's rule for touched spoken fields is still not met, and two of the edits made the grade worse. Every gated field that was touched passes FK<=10 and FRE>=60. pahc.quote.jesus-christ-our-god has one 26-word sentence, which is within "~25".

18. **Whole-block YAML re-serialization (all 84 files)**
    - NON-BLOCKING. The apply script re-dumped each touched top-level key with `yaml.safe_dump(width=100)`. That changed quoting style and reflowed unchanged paragraphs and sibling list items, for example every `sources[].locus` in pahc.force.selective-canonization. A parse comparison confirms that no value other than the 109 listed ones changed. However, the textual diff (741+/923-) is far larger than the edit, which makes line review and blame harder. Consider re-applying as in-place string edits before commit.

## Changes checked and found sound

- **Build records (13 edits).** Only the wrong words changed, and every confidence and caveat clause is kept.
  - Athanasius 367 placed Hermas and the Didache among books "appointed ... to be read by those who newly join us" (npnf204 Festal XXXIX.7).
  - The Didache's eclipse now ends at its 1873 rediscovery (pahc.source.didache: "found 1873").
  - Trallians 2 now reads "as to the apostle of Jesus Christ" (anf01 l.6314). Magnesians 13 is checked.
  - "The faithful in Asia met often in many places" (npnf201 l.29721) replaces "bishops" and "synods".
  - Adv. Marc. I.19 is now described correctly: Antonine reign, about 115 years and 6½ months after Tiberius (anf03 l.23723).
  - Justin 1 Apol. 26 now reads "many of every nation" (anf01 l.14946).
- **Quote renderings (15).** Each was checked clause by clause against its `text`: appointed-to-be-read, asia-rejected-new-prophecy, first-clement-apostolic-chain, ignatius-marriage-bishop, jesus-christ-our-god, justin-reasonable-livers, lucian-all-brothers, lucian-orphans-and-widows, melito-no-phantom, moses-is-more-ancient, tacitus-hatred-against-mankind, the-memoirs-of-the-apostles-are-read, they-appointed-those-already-mentioned, two-female-slaves-who-were-called-deaconesses. Each renders every clause and adds nothing beyond a supplied referent: "those who held them" follows Eusebius's "these persons", and "them" is the implied object in 1 Apol. 67. Except for item 11, none uses a misleading word, and the "former/latter", "exquisite", "suggestions", "lived reasonably" and "president" fixes are all correct.
- **Demonstrations.**
  - becoming-one-of-us (both turns): "other water" and the fasting are as in Didache 7. The invented "not a rush / room for a scared person" is gone.
  - center-coming-to-belief: "straightway a flame" and "whilst revolving his words" (anf01 l.17853ff). The conditions are correctly addressed to Trypho.
  - center-who-was-jesus: Trallians 9 wording; Didache 9 "Thy servant" now goes to the Father. The unsupported "more than one household" is removed.
  - honest-limit-material-remains: Pliny's sequence is now correct, and the "only outside description" claim matches pahc.limit.material-remains' own locus.
  - lament-suffering: the yearly gathering is now a hope, and Quintus "when he saw the wild beasts, became afraid".
- **Doctrinal witnesses.** apostolic-practice, coming-to-belief, doubt-and-asking (Hermas Mandate 9 checked at anf02 l.2398-2430: "wicked and senseless", "has no power", "with difficulty be saved", "gain the mastery over it ... clothing yourself with faith"), hard-texts, jesus-as-god, marriage-and-wealth, our-own-failures, outside-our-community, outsider-view, prayer-and-struggle (Didache 15.3 rendered faithfully), scholarly-standing, scripture-and-testimony, what-we-never-settled. Tense, pivots and coined closers are fixed, and the facts are kept.
- **Figures.** pliny, ministrae, justin, network, ignatius (the authenticity dispute is now carried), polycarp.
- **Honest limits.** enslaved-voices (the Philippians 2 import and "suffered for us" are removed) and ordinary-majority.
- **Stories.**
  - day-under-bishop-and-presbyters: Smyrnaeans 8.
  - didache-eucharist.
  - first-clement-corinthian-dispute tellable_as: "consulted us" makes "unrequested" wrong, and that is fixed.
  - grandsons-before-domitian: "dreaded the advent of Christ, as Herod had", "brought ... before Domitian", "When they were released".
  - ignatius-guarded-journey: Smyrnaeans 10, Philo and Rheus Agathopus.
  - justin-sunday-gathering, martyrdom-of-polycarp text, mutual-aid-prisoner ("Their officials bribed the gaolers to let them sleep inside with him"), nero-scapegoating ("called Christians by the populace"), pliny-interrogation, polycarp-forwards-letters.
  - quintus-recantation: the quotation now matches Martyrdom 4 verbatim, including "[to suffering]", and "lately come from Phrygia" is correct.
  - two-ways-catechumen.
- **Terms.** diakonos (deacons carry the elements to the absent, 1 Apol. 65; succour of widows and prisoners is the president's, ch. 67), agape-label, ekklesia, episkopos, hetaeria, ministrae plain_meaning, pertinacia, presbyteros, prophetes ("Christ-monger", Didache 12), two-ways plain_meaning and quick_meaning (Didache 1:1), baptisma.
