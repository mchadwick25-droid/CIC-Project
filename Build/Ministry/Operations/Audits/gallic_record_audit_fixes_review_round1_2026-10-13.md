Review round 1, gallic record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: FAIL (3 blocking findings, each a short fix)

Scope: commit 1f884b1, 76 files under records/gallic. I checked these fields against the vendored sources (npnf211, the Salvian Sanford edition, Hilary's Sermo in PL50):
- quote modern_rendering (10)
- demonstration representative turns (9)
- doctrinal_witness text and the positions/tensions lines this commit touched (4)
- figure bridge_line (3)
- honest_limit statement (2)
- story tellable_as (12)
- term plain_meaning and quick_meaning (37)
- the six edited notes

I read every changed field in full, not only the diff hunk. Story `text`, voice_craft, gravity, force and world_core fall outside this commit (see finding 9).

## Findings

1. **gallic.quote.the-fathers-and-the-angels-twelve, modern_rendering** - Old: whole joined sentences with the cuts removed. - New: the "..." marks are back, but three clauses are left as fragments: "... send out a poisonous root of error, or jealousy, or division, among those who came after ..."; "... in keeping with his own zeal, and with no thought for the weakness of others ..."; "... such a holy difference of opinion in their devout debate on the rule of their religion." - Source: npnf211:17195-17203, "it might send forth a poisonous root ... And when each man in proportion to his own fervour—and unmindful of the weakness of others—thought that that should be appointed ... there was such a holy difference of opinion". Method V2.0, around l.862: "A source sentence cut short mid-thought is finished with the verb its structure implies, and is not carried over as a fragment." - BLOCKING. The fix swapped one breach for another. The cuts should keep their "..." and be finished in the edition's own words. Replacement for the three pieces: "... They feared that some dispute might send out a poisonous root of error, or jealousy, or division, among those who came after ... Each man, in keeping with his own zeal and with no thought for the weakness of others, thought that what was easy for him should be fixed ... There was such a holy difference of opinion in their devout debate on the rule of their religion. So the hour of their evening office came before the sacred question was settled ..." The ending "...they added ... simply as extras" has no object. That part is non-blocking, but better: "... the two lessons they added, they added simply as extras, and by their own appointment." This also serves the record's not_for on the lessons.

2. **gallic.demo.someone-like-me, exchange[1].text** - Old: "said in the same book that no one who joined our monasteries had kept it unbroken even a year". - New: "Cassian wrote out Egypt's order and said no one who joined our monasteries kept it even a year." - Source: npnf211:18557-18560, "we cannot recollect any one who joined our monasteries keeping it up unbroken even for a year". - BLOCKING. The fix dropped "unbroken" and Cassian's "cannot recollect". That turns "nobody kept it up without a break" into "nobody kept it at all", which is a new overstatement. It also clashes with gallic.term.customs-of-the-monasteries, whose not_for says "unbroken even for a year". Replacement: "Cassian wrote out Egypt's order. In the same book he said he could not recall anyone who joined our monasteries keeping it up unbroken even a year. He never wrote what a house in Gaul did instead." The same gap appears in three other fields, which are non-blocking:
   - gallic.limit.only-on-paper statement (rewritten in this commit): "no one in Gaul kept that way even a year". Change it to "kept it up unbroken even a year".
   - gallic.demo.want-to-leave ("none of us kept the fathers' perseverance a year") and gallic.demo.record-thinnest ("kept the fathers' perseverance a year"). These are older wording in fields this commit edited. Add "unbroken" to both.

3. **gallic.term.customs-of-the-monasteries, plain_meaning** - Old: "We keep them where Gaul's cold and our weak bodies allow. Where they do not, we balance them from Pontus and Mesopotamia." - New: "We kept them as far as Gaul's cold and our weak bodies allowed. Where they did not, Cassian balanced them with the customs of Pontus and Mesopotamia." - Source: the record's own not_for, "documented Gallic practice, when Cassian admits no one in our monasteries kept Egypt's perseverance unbroken even for a year". npnf211:16526-16534 is a stated plan ("I shall ... balance it"), not a report of practice. - BLOCKING. The tense fix kept the claim the not_for forbids, and now states it as past fact. Replacement: "Cassian wrote them out for a new house in Gaul. Where Egypt's rule was too hard for Gaul's climate or habits, he said he would balance it with the customs of Pontus and Mesopotamia."

4. **gallic.quote.apostolic-authority-in-martin-alone, modern_rendering** - New: "The dignity of the priests ... had taken second place to the king's court." - Source: npnf211:1559-1565. The "priestly dignity" here belongs to the "bishops from various parts" at the court of Maximus, who was emperor, not king. - NON-BLOCKING. Two words mislead in their modern sense. Today "priests" means presbyters, and "king" is the wrong rank. The adjudicated fix had "priesthood" and "royal court". Replacement: "The dignity of the priesthood, in debased submission, had taken second place to the royal court. Yet in Martin alone, the authority of the apostles still held its ground."

5. **gallic.quote.vincent-awful-expectation-of-judgment, modern_rendering** - New: "urgently asks for more earnestness". - Source: npnf211:12090, "importunately demands increased earnestness". - NON-BLOCKING. "Asks for" softens "demands". Use "urgently demands more earnestness in our faith".

6. **gallic.dw.christ-in-the-beggar-and-the-guest, positions[3]** - Unchanged: "otherwise we answer as houses, in what we did". - The adjudicated list confirmed this one (text; positions[3], Tier B, present-tense "we answer"). The commit fixed the text but missed this position. - NON-BLOCKING. It is a tense tell, not an error of fact. Replacement: "otherwise the houses left only what they did".

7. **gallic.story.the-three-lentil-beans, tellable_as** - New: "The abbot judges the cook careless with sacred things". - Source: npnf211:19232-19233, "adjudged a pilferer and careless about sacred property". - NON-BLOCKING. The rewrite drops "pilferer". That harsh verdict is the point of the story. Use "The abbot judges him a pilferer, careless with sacred things, and bars him from prayer until he does public penance."

8. **Small wording points (all NON-BLOCKING)**
   - gallic.term.virgin-virginity, quick_meaning. "We say little of the south's own teaching on chastity" now reads as if the south had little to say. Conf. XII is about chastity. A true fact the field needs was dropped. Better: "Of the south's own teaching on chastity we can say little. A later translator left it out of our English books."
   - gallic.term.sarabaite, quick_meaning. "He was his own master" follows three present-tense verbs in the same third-person description. Use "He is his own master."
   - gallic.term.apostolic-see-pope, quick_meaning. "Its bishop ... Vincent praised him" generalises one bishop into the office. Name him: "Pope Stephen, its bishop, was first in authority of place, and Vincent praised him for being first in refusing anything new."
   - gallic.demo.never-settled. The new line "Word of the question was carried to Augustine in Africa" is now backed by no `sources` locus, because the beginning-of-a-good-will locus was trimmed. Add a locus, for example gallic.contested.beginning-of-good-will, "Augustine reports the brethren as claiming".
   - gallic.limit.no-one-who-saw-him. "After the psalms they read two lessons" leaves out that the lessons were extras "only for those who liked" (npnf211:17225-17228). Add "for those who wished".

9. **Out of scope, but not yet logged (NON-BLOCKING here; must be logged)** The adjudicated lists contain confirmed Tier A items that this commit's stated scope leaves out:
   - **Story text:** discharge "the scene the whole of Tours's memory of him turns on"; election "against his own wish, by a trick"; germanus "for the brothers at Lerins" and the "three stages" error; archebius "Their example, not their words"; the honoratus Latin strings and "the sentence the tradition of Lerins is remembered by"; the paesius closer; the id strings and over-long sentences.
   - **voice_craft:** guard and flavor_notes.
   - **The rest:** all gravity, force and world_core items; "heard only one side" in gallic.term.beginning-of-a-good-will; and "the fillet that took him off" in the honoratus absent_detail.

   These need entries in gallic's Open_Gaps_Tracking.md so they don't go quiet.

## Changes checked and found sound

- **Quote renderings, checked clause by clause:**
  - believed-everywhere-always-by-all, chaeremon-grace-requires-our-effort and chaeremon-three-stages-of-grace: the restrictive "who taught" is kept, and the note is corrected to match.
  - germanus-and-chaeremon-on-the-husbandman: "Just so, toil all night long ... prospers it" uses the edition's own words at npnf211:37547-37548, so the method allows it. A trailing "..." after "drawing us" would be tidier, but this is optional.
  - receiving-christ-in-you: the quotation marks match the source's.
  - salvian-present-judgment-clearly-shown (Sanford l.9010) and vincent-tempests-of-secular-warfare.
- **Demos:**
  - faith-alone matches XIII.3, and "later ... the other way" is fair.
  - never-settled: the Institutes preface (16503) and Conf. XV (39884, 39913) back the Cassian lines.
  - power-against-dissent: "persuasion failed ... grew angry" matches npnf211:5160-5177.
  - quiet-the-mind, and record-thinnest: "made a presbyter on the island" matches Hilary's "Apparuit illic presbyter" (PL50 l.716), and the Sulpitius line matches Life XXV.
  - want-to-leave: "Speedily" (5326), and the steward's cupboard set in Egypt (18671).
  - who-chose-bishops and women-own-words. No new tells.
- **Doctrinal witness:**
  - one-person-two-substances and the-christ-who-bears-the-wounds put Christ in the present and the community's practice in the past.
  - The catechumen raising (npnf211:999-1000) and Gallus's "Christ also working in him" (5058) are quoted correctly.
  - laughed-at-and-reported matches Institutes I.10 (16917).
  - christ-in-the-beggar-and-the-guest: the text and tensions[0] are sound.
- **Figures:** cassian, sulpitius and vincent: "harbour of religion" and "worldly warfare" match npnf211:12114.
- **Honest limits:** only-on-paper (Institutes for Castor, plus the elders' talks, with "historians" removed) and no-one-who-saw-him (Egypt's appointment named, tense fixed).
- **Story tellable_as:**
  - archebius, brictio (5337 Judas line), circuses-amid-the-ruins ("wealthiest" or "most excellent" city, Sanford l.8126, would be closer than "greatest", but this is optional), death-of-martin ("said ... nearly two thousand ... gather"), discharge (853), election, germanus (37488-37495)
  - honoratus: per claim_guard, with no English quoted as Hilary's.
  - paphnutius (43014-43080) and trier-and-the-ithacian-communion.
- **Terms:**
  - Facts: angels (1330, 4572-4581), antichrist (Gallus's eighth year, 4607), bagaudae, bloodless-martyrdom (42697), church-or-circus, conference (42316-42318), disciple-master, heathen-rustics, trial (13370), merit ("no antecedent merits").
  - Past-tense conversions: combat-athlete, conversion, example-imitation, fear-hope-love, free-will, gaul, grace, humility, illusion, lukewarmness, monk-bishop, novelty-antiquity, obedience, pelagians-as-foil, penance-satisfaction (now Egypt's discipline as Cassian set it out), perfection, renunciation, sign-of-the-cross, soldier-of-christ, the-devil-demons, the-fathers-elders, the-world-secular, tradition. Each keeps God and Christ in the present, and none adds a coined closer, an effect pivot or a build word.
- **The six notes** now match the new text.
