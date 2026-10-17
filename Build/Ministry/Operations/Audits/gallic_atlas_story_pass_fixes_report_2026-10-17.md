# Gallic Atlas story pass: fixes after independent review

- Worktree: `/home/user/CIC-Project/.claude/worktrees/agent-a792408e07913bea8`
- Branch: `site/atlas-story-gallic-fixes` (from `origin/site/atlas-story-gallic`, PR #932). Not pushed.
- Files changed: `Build/worlds/gallic/surface/world_front/gallic.front.gallic-monastic-ascetic-christianity.md` (orientation.story, documented_stories, highlights, stale body note deleted) and the `telling:` line of all ten card stories in `records/gallic/story/`.
- Not done, per brief: no package rebuild, no site JSON or page rebuild, no audio. The site JSON, page and audio on this branch are now stale against the source and need regenerating before merge.

Every finding was checked against the records and, where the reviewer cited it, the vendored file `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`. **None was rejected.** All 19 BLOCKING, 19 SHOULD-FIX and 9 NIT findings were confirmed. Where Mark's ruling on add-on tails applied, a finding was settled by cutting the closing paragraph, not by rewriting it. Those cases are marked "resolved by cut".

## A. BLOCKING

**B1 ACCEPTED.** Faustus as bishop of Riez is after the horizon. `gallic.core.gallic` horizon: "Faustus belongs to us only as a monk and abbot." His see rests only on Gennadius ch. LXXXVI.
- Before: "Faustus, another monk trained on the island, became bishop of Riez." Riez highlight: "Faustus of Lérins became its bishop."
- After: the sentence is deleted. The Riez highlight is deleted, because Riez no longer appears in any text.

**B2 ACCEPTED.** The record has Honoratus "scatters the fear of his own", so he did not go alone. It gives filth and venomous creatures as the reasons the island was empty, and does not say anyone lived there before.
- Before: "a man named Honoratus went alone to a small island off the coast. Snakes had driven everyone else away."
- After: "a man named Honoratus took his followers to Lérins. The island stood empty, because it was filthy and no one went near it for fear of snakes."

**B3 ACCEPTED.** The reluctance in the record concerns the clergy and priesthood on the island (`thinness`; "Hic primum illigatur"). The story's not_for bars "Honoratus's later episcopate at Arles as history". Pleiades places Arles about 195 km from Lérins.
- Before: "the record says the snakes gave way. He wanted only to stay a monk there. Even so, he later became bishop of the nearby city of Arles." Arles highlight: "Honoratus became its bishop. Hilary came after him."
- After: "His disciple Hilary preached that Honoratus went in unafraid, with a psalm on his lips, and the snakes gave way. Honoratus had run from church office, but on the island the priesthood caught up with him. In time he became a bishop himself." The last sentence rests on Cassian's Preface III, "Honoratus, a Bishop", in `gallic.figure.honoratus`, and names no see. The Arles highlight is deleted, because Arles no longer appears in the story or any telling. The main story, teaser and telling now all name the same office, the priesthood on the island.

**B4 ACCEPTED.** Both wonders are Tier 3 or "Tier-3-shaped".
- Before: "Martin once brought a dead catechumen ... back to life. Another night the devil came to him dressed as Christ."
- After: "Sulpitius tells how Martin brought a dead catechumen, a new believer not yet baptized, back to life. He also tells how the devil once came to Martin dressed as Christ."

**B5 ACCEPTED.** The source (npnf211 l. 39903-06) says "our predecessors never reckoned those as good monks ... who professed themselves exorcists". The speaker is Abbot Nesteros, not Cassian. In the old text the sentence also read as a reply to Martin.
- Before: "Cassian warned that a monk who boasts of casting out demons has already failed." (after Martin's wonders)
- After: placed before Tours is mentioned: "Cassian refused to tell stories of wonders. In Cassian's Conferences, an Egyptian elder says the fathers never counted a monk good if he showed off his power over demons. Tours told its story through power instead."

**B6 ACCEPTED.** Core caution: purity of heart is Egypt's teaching, "never ... Gaul's invention". Discretion's title comes "by the judgment of the blessed Antony" (Conf. II.4, l. 27340-46). No record ranks discretion "most".
- Before: "The south named its goal purity of heart. Cassian taught ... What matters most is discretion, which he called the mother of all virtues."
- After: "From the fathers of Egypt, the south received a goal called purity of heart, and fasting and night prayer were only aids toward it. The monk was kept on course by discretion, the judgment that tells when a practice goes too far. The Egyptian fathers called it the mother of all virtues."

**B7 ACCEPTED.** `gallic.quote.cassian-adapts-egypt-to-gaul` reads "severity of the climate, or owing to some difficulty or diversity of habits ... impossible ... or hard and difficult".
- Before: "changing only what the colder climate required."
- After: "He changed them only where Gaul's harsh climate or different habits made them impossible or too hard."

**B8 ACCEPTED.** "By its own account" had been dropped. The story's claim_guards forbid stretching it to Prosper, Celestine or Rome.
- Before: "The south's best-known argument began as a worry at prayer. ... That answer grew into a long argument ... It later reached Rome. The record never settles it."
- After: "By Cassian's own account, the south's best-known argument began as a worry at prayer. ... That answer grew into a whole Conference on grace and effort." Rome is removed rather than hedged. The guard bars this story from carrying it, and under Mark's ruling the unit ends on its last event. This departs from the reviewer's wording, which kept a closing "No one in these houses wrote down" tail.

**B9 ACCEPTED.** The not_for lines in trier-and-the-ithacian-communion and authority-ambivalence, and the core no-contact caution, all apply.
- Before: "On bishops and councils, the two households disagreed. At Tours, Martin kept his distance from other bishops. ... In the south, church councils were trusted as guardians of the truth. The record leaves that disagreement standing."
- After: "At Tours, some bishops had opposed Martin's election. Later, at the emperor's court in Trier, Martin once took communion with bishops he had refused, to save lives. He felt it cost him some of his power, and he never attended a synod again. Vincent, by contrast, wrote that the decrees of an ancient general council should be preferred to the rashness and ignorance of a few." The views are tied to one man each, and nothing says the houses disagreed with each other. The Vincent clause quotes `gallic.quote.council-over-rashness-and-ignorance`.

**B10 ACCEPTED.** The pronoun made Sulpitius the dying traveler.
- After: "Knowing his end was near, Martin went to make peace among the quarreling clergy at Condate. As he lay dying, his monks asked to put straw under him. He kept to sackcloth and ashes, so as not to leave them a different example."

**B11 ACCEPTED.** Grep finds no "layman", "career" or "follow Martin" in `records/gallic/`. The figure record says he "visited Martin at Tours".
- Before: "Sulpitius Severus was a layman who gave up his career to follow Martin. He was never present for the events he describes"
- After: "Almost everything known about Tours comes from Sulpitius Severus, an Aquitanian who visited Martin there. He was not present for most of what he tells, and says he learned it from Martin and those who lived with him."

**B12 ACCEPTED.** `gallic.figure.martin`: the year of the discharge is "not given in the text".
- Before (when): "c. 360, before a battle in Gaul, on the eve of Martin's discharge from the Roman army"
- After: "Before a battle in Gaul, when Martin left the army; the text gives no year"

**B13 ACCEPTED.** No record gives 385/386. The record says "carried as given, not converted to a year", and "companions" is unsupported.
- Before (when): "385/386, after the execution of Priscillian and his companions at Trier"
- After: "After Priscillian was put to death, while Maximus ruled at Trier; the text gives no year"

**B14 ACCEPTED.** The record says "On the following day".
- Before: "Called a coward for refusing to fight, a soldier offers to walk at the enemy with no weapons. Before morning, the enemy asks for peace."
- After: "Called a coward for refusing to fight, a soldier offers to face the enemy unarmed. The next day, the enemy asks for peace."

**B15 ACCEPTED.** The source (l. 5323-27) gives no hour, only "with rapid steps ... Speedily".
- Before: "A presbyter Martin raised from boyhood rages at him, then begs pardon within the hour."
- After: "A priest Martin raised from boyhood rages at him, then soon comes back to beg pardon." "Priest" replaces the unglossed "presbyter", which also settles N4.

**B16 ACCEPTED, resolved by cut.** Inst. II.8 (l. 17306-16) says the custom new to the East is that "all standing up sing together with a loud voice" the doxology. The PR text misstated this. That sentence sat in the closing paragraph, which Mark's ruling removes. It also reaches outside the story's own locus (Inst. II.5-6), so the whole paragraph was cut. The telling now ends on the fathers adding "two readings of their own choosing".

**B17 ACCEPTED, resolved by cut.** The sentence about the coverage note and the singing at Tours breached the story's not_for. It was removed with the closing paragraph.

**B18 ACCEPTED.** The absent_detail says the sermon "exists in full, unread here". The roughness is in this build's OCR, not in the sermon's survival.
- Before (paragraph 1): "...as far as the rough copy of that sermon can be read." Paragraph 4: "This is the closest our record comes to Lerins itself..."
- After: paragraph 1 opens "When our founder Honoratus died, his disciple and successor Hilary preached his life." The claims are carried by in-line "Hilary says" and "Hilary adds". Paragraph 4 is cut under Mark's ruling. The reviewer's replacement for paragraph 4 was itself a source-limits tail, so it was not used.

**B19 ACCEPTED.** The record says "came up", not "first arose". The body note says XIII.13 and XIII.18 are "two separate teachings ... not joined".
- Before: "Cassian describes how the question of grace and effort first arose." / "Later Chaeremon says that grace works together with the human will, and that the human mind cannot fully understand how both are true. What he taught about chastity the night before is missing from our edition."
- After: the opening "first arose" sentence is gone. The telling now opens "Cassian wrote this down years later, in Gaul." It ends: "Later in the same Conference, Chaeremon says that grace works together with our will, and sometimes waits for some effort from it. Elsewhere he says that wanting the good, doing it and holding on to it are all God's gifts. Yet none of them takes away free will, and how both are true, he says, the human mind cannot fully grasp." The tail about the missing chastity teaching is cut.

## B. Rigor: SHOULD-FIX

**S1 ACCEPTED.** Before: "Sulpitius says almost two thousand monks gathered for his funeral." After: "Almost two thousand monks, it is said, came to his funeral." The telling uses the same wording.

**S2 ACCEPTED.** "Martin alone" belongs to a different quote. Before: "Sulpitius has a traveler from Egypt say that Martin alone was worth all its hermits put together." After: "The Tours writer Sulpitius has a traveler just back from Egypt admit that Martin had outdone them all." The highlight phrase is updated to match.

**S3 ACCEPTED.** Before (unit 1): "Both called themselves keepers of what came before them." (unit 4): "Both households also agreed that nothing true could be new." After: both sentences are removed. Unit 1 now states the shared idea instead (see C5). Vincent's rule stays, tied to him alone: "On Lérins, Vincent wrote that the true faith is what has been believed everywhere, always, by everyone." `gallic.quote.believed-everywhere-always-by-all` is added to grounded_in. No "both agreed" claim remains.

**S4 ACCEPTED.** Before: "The Monk Tricked Into the Bishop's Chair". After: "The Monk Lured Out to Be Made Bishop".

**S5 ACCEPTED.** After: "In his Sacred History, Sulpitius tells of an earlier stage, before Priscillian's death. There he says Martin held it a shocking wrong for a worldly ruler to judge a church case."

**S6 ACCEPTED.** Before: "...so that troops will not be sent to hunt heretics in Spain." After: "To save lives, a bishop takes communion with men he had refused. He also stops officers from being sent to hunt heretics in Spain. He never fully forgives himself." The reviewer's single sentence was reworded because its reading ease scored 52.

**S7 ACCEPTED.** Before: "...shunned for its snakes, singing a psalm. ... Then the priest's headband catches the man who ran from it." After: "A founder walks unafraid onto an island shunned for its filth and snakes, a psalm on his lips. The snakes give way. Then, his disciple says, the priesthood he had run from catches up with him there."

**S8 ACCEPTED.** Before: "...so the speeches are Cassian's own composition." After: the phrase is now "Chaeremon", because the main story names him. The note reads "An old man whose cell stood near Panephysis in Egypt. Cassian wrote down his words decades later in Gaul, setting out in his own composition what he had heard." This follows the record's "Cassian's composition of what he heard". The reviewer's "not a transcript" was not used, to avoid a "not X but Y" construction.

**S9 ACCEPTED.** Discretion: "The Egyptian fathers' word, passed on by Cassian, for the judgment...". Purity of heart: "The Egyptian fathers, as Cassian reports them, ranked fasting and night prayer as aids to it, never as the point."

**S10 ACCEPTED.** Priscillian: "Sulpitius, who was hostile to him, sums up the charges in his Sacred History." Maximus: "The emperor was Maximus. At Trier he took the side of Ithacius, the man who had accused Priscillian." "Usurper" and "the record calls" are removed.

**S11 ACCEPTED.** "Before any monastery existed in Gaul" is gone. The cloak telling now opens "Martin's father was a tribune, an army officer."

## C. Craft: SHOULD-FIX

**C1 ACCEPTED.** All meta uses of "record" and "edition" are removed: units 3, 5, 6, 7 and 8; the synod, virgins and Maximus highlights; the angel, Honoratus and Germanus tellings. The repeated unresolved-argument endings of units 6, 7 and 8 are cut under Mark's ruling. The reviewer's replacement for unit 8, "The story closes around 450, with the argument ... still open", is itself such a tail and was not used. The 450 cut-off stays in unit 1. Virgins now reads "No woman among them is named, and none speaks." Synod now reads "Vincent, a monk of Lérins, trusted the decrees of an ancient general council to guard the faith."

**C2 ACCEPTED.** The template is broken up.
- Openings now differ:
  - cloak: Martin's father
  - discharge: barbarians at the frontier
  - catechumen: the monastery
  - election: what Tours wanted
  - Trier: "We have this story from Gallus"
  - Brictio: the wooden seat
  - death: Martin's foreknowledge
  - angel: "Cassian brought us this story"
  - Germanus: "Cassian wrote this down years later"
  - Honoratus: "When our founder Honoratus died"
- Lengths run from 169 to 249 words.
- Seven tellings have three paragraphs and three have four, including the two-sentence opening paragraph in Trier.
- No telling ends on a source-limits paragraph.
- Each telling keeps its source hedges in place ("Sulpitius tells us", "Gallus says", "Hilary says", "it is said", "they say").

**C3 ACCEPTED.** Each telling now has an emic marker: "tells us", "told us", "the one we all knew", "Martin became our bishop", "Cassian brought us", "our founder", "Our part". "The text" and "Treves, now Trier" are gone from the tellings. The death telling has "Sulpitius writes" and "Those who were there told us".

**C4 ACCEPTED.** Main-story sentences now average 14.8 words, up from 11.8, and none is over 24 words. The paired nominalizations are gone ("The south took Egypt's customs as a rule to keep. ... The north set Martin beside Egypt's hermits.").

**C5 ACCEPTED, different wording.** The reviewer's version uses a colon reveal. After: "two households of monks lived out the same idea. In both, a monk who was made a bishop went on living as a monk."

**C6 ACCEPTED.** After: "Before a battle, he asked his commander, Julian Caesar, for his discharge, to serve Christ instead."

**C7 ACCEPTED.**
- Trier: "yet he would never put his name to it in writing" ("it" is now the communion just named).
- Angel: "through an angel, they believed, a rule had been fixed".
- Honoratus: "There was an island that stood empty" (no unnamed city).
- Germanus teaser: "troubled by something an old monk said the night before. He cuts the service short".

**C8 ACCEPTED.** "When Martin was fifteen, his father informed on him, and he was seized, put in chains and made to swear the soldier's oath." "One winter was so harsh that many people were dying of the cold."

## D. NITs

- **N1 ACCEPTED.** "Lérins" with the accent and US spelling throughout: quarreling, plows, traveler, labor. The duplicate "Lerins" highlight is deleted.
- **N2 ACCEPTED.** "The Angel Who Set the Number of Psalms".
- **N3 ACCEPTED.** "A citizen pretends his wife is sick".
- **N4 ACCEPTED** through B15.
- **N5 ACCEPTED.** "The settlement where Martin went to make peace among the clergy of its church, and where he died." "Settlement" follows Pleiades. "Village" is not in the record.
- **N6 ACCEPTED.** "An Aquitanian, from a leading family by his editors' account, who wrote the Life of Martin."
- **N7 ACCEPTED.** "the nearby city of Marseilles" becomes "the city of Marseilles". The same phrase is still in `skim.tile`, which is outside this brief.
- **N8 ACCEPTED as a log defect, order unchanged.** The cards run through Martin's life in order and then the three southern stories. That is a sensible order. The false "in date order" claim is in OG-40, which is append-only and outside this brief.

## E. Body note

The stale process note (old lines 445-713) is deleted. It was commentary in a canonical file and contradicted the current text: "tenth paragraph", "narrative.questions is left EMPTY", "no repeated first name". The file now ends at the closing `---` of the frontmatter.

## Main story changed: yes

It has nine units, up from eight. Received tradition (Vincent) moved into the purity-of-heart unit, and virtus became its own unit. grounded_in was extended where claims needed it. Ids added: `gallic.gravity.monk-bishop` (unit 1); `gallic.quote.cassian-adapts-egypt-to-gaul` and `gallic.quote.postumianus-you-have-conquered-all-the-eremites` (unit 4); `gallic.term.purity-of-heart`, `gallic.term.discretion` and `gallic.quote.believed-everywhere-always-by-all` (unit 5); `gallic.quote.cassian-refuses-to-weave-a-tale-of-miracles` and `gallic.quote.humility-mistress-of-virtues-not-exorcism` (unit 6); `gallic.quote.council-over-rashness-and-ignorance` (unit 8); `gallic.figure.martin` (unit 3). One id was dropped where its claim was cut: `gallic.core.gallic` from the last unit (the 450 closing line).

## Tellings changed: all ten

| Telling | Words before | Words after | Paragraphs | Avg sentence | Max | FK | FRE |
|---|---|---|---|---|---|---|---|
| the-cloak-at-amiens | 248 | 225 | 3 | 17.3 | 25 | 7.26 | 73.8 |
| discharge-before-caesar | 239 | 169 | 3 | 13.0 | 19 | 5.61 | 78.0 |
| raising-of-the-catechumen | 239 | 208 | 3 | 16.0 | 23 | 6.36 | 77.9 |
| election-at-tours | 240 | 203 | 3 | 16.9 | 22 | 8.10 | 67.1 |
| trier-and-the-ithacian-communion | 250 | 249 | 4 | 15.6 | 25 | 8.49 | 61.9 |
| brictio-in-the-courtyard | 249 | 217 | 3 | 15.5 | 24 | 7.37 | 69.9 |
| death-of-martin-at-condate | 244 | 221 | 4 | 15.8 | 21 | 5.94 | 80.6 |
| the-angel-and-the-twelve-psalms | 243 | 185 | 3 | 16.8 | 23 | 7.11 | 74.1 |
| germanus-scruple-at-morning-service | 246 | 246 | 4 | 15.4 | 25 | 6.14 | 78.4 |
| honoratus-and-the-island | 247 | 220 | 3 | 15.7 | 25 | 6.84 | 74.0 |

The main story is 692 words by whitespace count (659 before). The scorer's tokenizer counts 694, because it splits "Lérins". Over the whole story: 47 sentences, average 14.8 words, maximum 24, FK 7.21, FRE 69.7. Before: average 11.8, FK 6.37, FRE 70.4. Each unit's FRE is at least 61.9, and each unit's FK is at most 8.72.

Scores are from `engine.m1.fk` (fk_grade, fre_score). Every field is at or under FK 10 and at or above FRE 60. Most are below FK 8. regate reports "47 edited field(s) below FK 8 (reported, not failed)". Sentences were lengthened toward the 12-20 average without padding. The low FK comes from plain, short words rather than short sentences.

## Tails removed

- Unit 6 (grace): "It later reached Rome. The record never settles it."
- Unit 7 (councils): "The record leaves that disagreement standing."
- Unit 8 (Sulpitius): "The record closes around 450, with the argument over grace and effort still open."
- Cloak: "Sulpitius witnessed none of this, and learned it partly from Martin and partly from those who had lived with him. The text provides no year and never names the beggar."
- Discharge: "That interpretation belongs to Sulpitius himself. He was not present, the text gives no year, and no independent witness survives."
- Catechumen: "Sulpitius presents the man as a living witness, yet never names him. He identifies the monastery only as a place not far from the town."
- Election: "Sulpitius gives no year for the election. He is openly hostile to the objecting bishops, whose own side is never heard."
- Trier: "The text gives no year, and we hear Ithacius only through the writer who called him worthless."
- Brictio: "Brictio's own side is never heard, since every word of his reaches us through men hostile to him."
- Death: "The letter never names the city where the body was taken, and the numbers are report. The choir of virgins is the only trace of the women who embraced this life at Tours, and none of them speaks."
- Angel: "Cassian names no witness who saw the angel, and nothing in our record says what the brothers at Tours sang. In Gaul the twelve were kept, together with a hymn of praise called the Gloria, which Cassian says was never heard in the East."
- Germanus: "What he taught about chastity the night before is missing from our edition."
- Honoratus: "This is the closest our record comes to Lerins itself. It tells how the founder arrived and was made a priest there. What anyone did on the island in between, it does not say."

Hedges kept in place because they qualify a specific claim: "Sulpitius tells us" (the cloak vision, the discharge reading), "As Sulpitius tells it" (the raising), "Sulpitius says" (Martin's reluctance), "Gallus says" (demons, angel), "Those who were there told us" and "they said" (deathbed), "it is said" (funeral numbers), "they believed" (the angel), "Hilary says" and "Hilary adds" (Honoratus), "By Cassian's own account" (grace).

## Checks

- `python -m engine.m10.cli records gallic`: PASS.
- `python -m engine.m10.cli regate gallic --base origin/main`: PASS. Every remaining note is "not a regression, already failed at the base and unchanged" and concerns fields outside this brief.
- `python -m engine.m9.cli check`: see the result line below.
- Highlight kinds are all person, term or place. Every highlight phrase appears case-sensitively in the story or a telling. "Discretion" was reworded to lowercase in unit 5 so the term marks.
- AI-tell scan of all edited fields found no em or en dashes, no colons, no parentheses, no "not ... but", no "this world" and no meta "record". The only "the text" hits are in the `when` date labels ("the text gives no year").

- `python -m engine.m9.cli check` exited 0 with "library access gate: clean - every finding is waived, every waiver is live and current". No unwaived gallic findings, so the world_front validates. Full output: `/tmp/claude-0/-home-user-CIC-Project/0b1f54c8-3ed3-54d3-9dab-f497b0e870d6/scratchpad/m9.txt`.
- Commit: `c1d79d3c2` on `site/atlas-story-gallic-fixes`.

## Record defects to log (outside this brief, not edited)

1. **OG-40** in `Build/worlds/gallic/Open_Gaps_Tracking.md` says Faustus of Riez was cut, but he was in the shipped text until this fix. It also says documented_stories are "in date order", which is false, and it records a round-1 PASS over the defects above. OG entries are append-only, so this needs a new entry that cites OG-40 by subject and date.
2. **`gallic.gravity.monk-bishop`** description says "His Latin survives only in a rough copy". That contradicts `gallic.story.honoratus-and-the-island`'s absent_detail, "exists in full, unread here". The roughness is this build's OCR. This was the source of B18.
3. **`orientation.voices` (Honoratus)** in the same world_front: "went alone to an island so overrun with snakes that no one else would live there", and "ended his life leading the church at Arles". This repeats B2 and goes against the story's not_for on the Arles episcopate. The Honoratus hedge also has a dash aside and "rough, hard-to-read Latin" (B18). The Sulpitius voice says "He gave up his own career to follow Martin", which is the B11 claim with no record behind it. The Martin voice hedge says "never present for any of it" (B11).
4. **`skim.tile`** says "the nearby city of Marseilles" (N7), "never fully settled", and "this world".
5. **`orientation.sourcing`, `legacy`, `floor_note`, `relations_summary`** use "this world's own record" meta-language throughout (C1). These fields are outside this pass.
6. **`records/worlds/gallic.yaml`** may still carry "360s" for the discharge story (OG-40 cites it). Not checked; outside this brief.
7. **Rebuild owed.** The site JSON, the page `cic-website/.../gallic-monastic-ascetic-christianity.html`, the package pin and the narration audio (story.mp3 and the docstory MP3s) on this branch reflect the pre-fix text. Recording audio of the new text is a paid run and needs Mark's sample approval first.
8. Per CLAUDE.md, the BLOCKING findings need independent re-confirmation. This report is not self-certification.

---

# Second commit: `4a890e172`

This commit widens the scope as the coordinator asked. It uses the same worktree and branch and sits on top of `c1d79d3c2`. Nothing is pushed. Two kinds of file changed: the rest of the Gallic world_front, and the bodies of the ten card-story records. No other record type was edited.

## 1. The rest of the world_front

For each field: the defect, then the fix. All new claims are grounded in the ids listed in each field's `grounded_in`.

- **skim.tile**
  - Before: "lived out one shared idea in different ways: a monk does not stop being a monk..." (colon reveal). "He gathered followers in the woods near Tours" (no record has woods). "the townspeople later seized him". "Two generations later". "the nearby city of Marseilles" (N7). "adapted it for a colder land and a different church" (B7 and S3 problem). "Running through both households was one argument, never fully settled" (false: Tours has no grace doctrine, `gallic.gravity.grace-and-effort`). "The story closes around 450, before that argument hardened into fixed camps" (unsupported tail).
  - After: the shared idea is stated without a colon. Martin's election is told by the trick, as the record has it. The southern houses are dated "In the years after his death". The tile says "the city of Marseilles". The no-contact sentence moved into the middle. Cassian's adaptation now reads "only where Gaul's climate or habits made it too hard". The grace question is tied to Cassian and the prayer scene only. The tile ends on Vincent's rule. grounded_in went from `[gallic.core.gallic]` to eight ids.
- **voices: Martin**
  - Before: "gathered followers in the woods". "made bishop against his own will" (stated as fact; `gallic.contested.election-as-capture`). "He healed the sick and raised the dead, by his own account" (wrong: it is Sulpitius's account). "to save two men's lives" (the number is not in the story record).
  - After: "Sulpitius says he could not easily be drawn out of his monastery, so the people of Tours made him their bishop by a trick." "Sulpitius tells of him healing the sick and raising the dead." The communion was taken "to save lives". The hedge is rewritten in the tradition's voice and drops "never present for any of it" and the "single-author risk ... this world tells" tail. It now reads: "Almost everything we tell of Martin comes from one writer, Sulpitius Severus, who admired him. Sulpitius visited Martin, but he was not there for most of what he tells. He says he learned it from Martin and from those who lived with him."
- **voices: Cassian**
  - Before: "lived for years" (the length of his stay is "not stated"). Two colon reveals. "no one in his own monasteries kept it even for a year" (overstated: Inst. IV.2 concerns the Egyptian perseverance, `gallic.term.junior-novice`).
  - After: "as a young man". The two houses are named, one for men and one for women. The program is credited to "the Egyptian fathers". The hedge reads "he could recall no one in our monasteries who kept up the Egyptian perseverance unbroken even for a year". This hedge failed FRE at the base and now passes (64.4).
- **voices: Honoratus**
  - Before: "went alone", "no one else would live there" (B2). "ended his life leading the church at Arles" (breaches the story's not_for). The hedge had "read today only in rough, hard-to-read Latin" (B18) and a dash aside. It failed FK and FRE at the base.
  - After: the island description matches the story text. "In time he became a bishop" rests on Cassian's Preface III and names no see. The hedge now reads "All we can tell of our founder comes from the funeral sermon his disciple Hilary preached..." and scores FK 5.6, FRE 79.5.
- **voices: Sulpitius**
  - Before: "rich and well-educated", "gave up his own career to follow Martin", "wrote Martin's Life while Martin was still alive", "never there for any of the events". None is in the records. The hedge had a dash aside and "this world".
  - After: he is an Aquitanian, "from a leading family by his editors' account", who visited Martin at Tours. The Life was written so readers "would be stirred to follow him". The text names the letter on Martin's death and the Dialogues, with Gallus as the friend he talks to. His sources come from Vita XXV. The hedge reads "Nearly everything we know of Tours passes through this one writer. He admired Martin and wrote to make his readers follow him, so he was never a neutral reporter."
- **floor_note**
  - Before: "This world confessed...", "not a live debate", "He wrote it to defend a different point" (the record calls it a proof-case for his rule), and an ending tail, "this world's own record never reaches a settled answer".
  - After: the two households, the formula, Vincent's use of it "as an example of his rule", and the Ephesus refusal. It ends on Ephesus. `gallic.contested.beginning-of-good-will` was swapped for `gallic.quote.believed-everywhere-always-by-all`, because the grace sentence is gone.
- **legacy**
  - Before: "This world's own record stops ... It says so itself ... ends at the edge of that change, not inside it." All meta language and tails. "A bishop trained on the same island" (he was abbot there).
  - After: "After 450 the argument over grace and effort went on, but it was no longer one monk writing to another. In the 470s Faustus, once abbot of Lérins and by then a bishop, took it up. He says he wrote at the request of church councils at Arles and Lyons, as a bishop writing for other bishops." "He says" keeps the prologue's attribution. The force record notes that the prologue survives only in a poor copy.
- **relations_summary**
  - Before: "This world grew up on ground another community had already fought to hold" (vague). Hilary "had refused to accept a creed backed by the emperor" (not in any record). Two closing tails: "does not say what happened ... says nothing about monasticism elsewhere".
  - After: the four events in `gallic.force.arian-scattering` and the raising story. These are Hilary's exile by heretics, Auxentius driving Martin from Milan, the island, and Martin following Hilary home to found his monastery. "Poitiers" is left out, since the raising record calls that identification editorial.
- **sourcing**
  - Before: "This world's record...". A colon reveal. "a later editor cut three whole sections ... from the one edition of Cassian that survives" (false: `gallic.core.gallic` says "missing from the English we have ... A later translator left them out"). A "not in what this world itself said" tail.
  - After: "Cassian's English translator also left out three of his texts on the body and its discipline." The rest is restated without meta language.
- **read_first**
  - Vita: "The whole of Martin's own story ... never present for any of it" (overclaim) becomes "Martin's life from soldier to bishop, by a man who knew him and heard the stories from Martin and his brothers."
  - Institutes: "adapted for a colder climate" (B7) becomes "changed only where its climate or habits made them too hard."
  - Commonitory: unchanged.
- **narrative.who_speaks**
  - Before: "this world's own voice". "made a bishop against his own will" (contested). "never present for it himself". "Like Martin, he was overtaken" (a cross-house comparison).
  - After: "Four figures carry the voice of the two households..." Martin "was drawn out of his monastery to be made a bishop". Sulpitius wrote "much of it from what Martin and his brothers told him". The Honoratus clause no longer compares him to Martin.

Readability of the edited fields, scored with `engine.m1.fk`: every field is at FK 10.0 or below and FRE 60 or above. The two highest are the Vita note (FK 7.8, FRE 76.7) and who_speaks (FK 9.3, FRE 61.0). No sentence is over 25 words. A scan found no dash asides, colon reveals, "this world", meta "record", "not X but Y" or "never settled" in any of these fields. One field was left alone: `confidence.divergence_note` at the top of the file still says "this world's own already-rated records". It is internal envelope metadata, not page text, and outside the listed fields.

## 2. Story-record bodies

All ten bodies were build commentary, so all ten were deleted. Each file now ends at the closing `---`. The bodies were:
- cloak: the translation note on Amiens
- discharge: the Julian/Worms editorial note
- catechumen: the Ligugé/Poitiers note
- election: the cross-node pairing "finding of the construction"
- Trier: the slug and spelling note
- Brictio: "No separate figure record exists"
- death: "Sourced from Letter III ... This record paraphrases"
- angel: "The origin ... is disclosed"
- Germanus: the ligature note and "never Germanus of Auxerre"
- Honoratus: the OCR grounding and relation notes

The engine never reads a body. `engine/m1/loader.py` says the body is "provenance/build notes only - never read by any builder". Every guard that mattered is already in the frontmatter. The divergence notes cover the editorial place names and the OCR limit. The Germanus of Auxerre guard also stands in `gallic.figure.cassian`.

## Checks after the second commit

- `python -m engine.m10.cli records gallic`: PASS.
- `python -m engine.m10.cli regate gallic --base origin/main`: PASS. 67 fields are new or edited, and 59 are below FK 8 (reported, not failed). The two front-file voice hedges that failed at the base (`voices[1].hedge`, `voices[2].hedge`) no longer appear.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0. Records show 1 hit, KEEP (a "reviewer" word inside the Brictio tier justification in the frontmatter). Worlds show KEEP 8 (the highlight `verified_on` dates) and PROTECTED 235 (Open_Gaps_Tracking). There are 0 REWRITE and 0 ROUTE.
- `python -m engine.m9.cli check`: exit 0, "library access gate: clean". No unwaived gallic findings.

## Defects in other record types (listed only, not edited)

1. `gallic.gravity.monk-bishop` description says "His Latin survives only in a rough copy, so the exact wording is uncertain." This contradicts the Honoratus story's "exists in full, unread here". The roughness is this build's OCR.
2. `gallic.force.army-and-rank-before` (line 63) says the same thing, "only in a rough copy", about the Lérins source.
3. `gallic.force.synodal-commission` says "The prologue survives here only in a poor copy". "Here" makes it accurate, but it reads as a claim about the text's survival. Also, "The world's real change came in the 470s" is a build verdict voiced as fact.
4. `gallic.force.arian-scattering` uses "Ligugé" three times (divergence_note, description, manifestations). `gallic.core.gallic` bars that name as editorial.
5. 163 gallic record files contain "this world". Many of these are in participant-retrievable fields such as `use_note.means`, gravity descriptions and `modern_contrast`, for example `gallic.limit.only-on-paper`'s means ("The record attests that ... this world's places"). This needs a fleet-wide sweep, not a story-pass fix.
6. The story records' own `text` fields (not edited) still carry claims the tellings dropped. These are "before any monastery existed in Gaul" (cloak, S11) and "succeeded him at Arles" (Honoratus). The Honoratus `text` also says "as far as these lines can be read".
7. OG-40 is still owed its corrective append-only entry (see the first-commit list).

---

# Round 2 fixes: `9ee272fdd`

This commit answers the round 2 recheck (`recheck-gallic.md`: 4 BLOCKING, 7 SHOULD-FIX, 3 NIT). It is on the same worktree and branch, on top of `4a890e172`, and is not pushed. Every finding was checked against the records and the vendored text, and all 14 were confirmed and fixed. None was rejected.

## BLOCKING

**R1 ACCEPTED.** The Honoratus wording is Inferential-Thin. `use_note.means` hedges this exact claim with "as far as the sermon can be read", and `tellable_as` carries the same hedge. My round 1 cut removed it with the tail. It qualifies one specific claim, so Mark's ruling keeps it. It is now restored on every priesthood claim:
- Telling: "And there, as far as Hilary's sermon can be read, the priesthood caught up with the man who had run from it."
- Teaser: "Then, as far as his disciple's sermon can be read, the priesthood he had run from catches up with him there."
- Unit 3: "As far as Hilary's sermon can be read, the priesthood he had run from caught up with him on the island." The claim no longer sits outside the attribution.
- Voice: "...but on the island, as far as the sermon can be read, the priesthood caught up with him."
- who_speaks: "There, as far as his disciple's sermon can be read, the priesthood he had fled caught up with him."

**R2 ACCEPTED.** The absent_detail says the sermon "exists in full, unread here beyond these lines". "All we can tell ... comes from the sermon" also contradicted the voice's own "became a bishop", which comes from Cassian's Preface III.
- Hedge, before: "All we can tell of our founder comes from the funeral sermon ... Of our days on the island in between, it says nothing."
- Hedge, after: "Almost all we can tell of our founder comes from part of Hilary's funeral sermon. Its Latin is hard to read. It tells how he came to the island and was made a priest there. What he or anyone did on the island in between, we cannot tell you."
- Sourcing, before: "Nothing survives of the island's daily life".
- Sourcing, after: "The island's daily life is known least of all". This follows `gallic.core.gallic` thinness: "the house we know least from inside".

**R3 ACCEPTED.** I verified that Conf. XV.3 (npnf211 l. 39759, "a most ancient corpse") narrates a wonder. The refusal in `gallic.quote.cassian-refuses-to-weave-a-tale-of-miracles` sits at the Institutes Preface only.
- Unit 6, before: "Cassian refused to tell stories of wonders."
- Unit 6, after: "In his Institutes, Cassian chose not to write up the wonders he had seen, since they teach nothing about how to live."
- Voice: "in his Institutes he chose not to write up the wonders he had seen."
- who_speaks: "In his Institutes he chose not to write of wonders."

**R4 ACCEPTED.**
- Before: "Both households left much writing on virtue and on the saint's power, and little on daily life."
- After: "Both households wrote much about virtue. Tours also wrote of Martin's power, while Cassian set down Egypt's customs more than the days of his own houses." The second half follows the Cassian bridge_line: "He told no tales of his own houses".

## SHOULD-FIX

- **S-1 ACCEPTED.** Dial. III.13 (l. 5187) reads "the tribunes, who had already been sent". The teaser is now: "To save lives, a bishop takes communion with men he had refused. In return, the officers sent to hunt heretics in Spain are called back. He never fully forgives himself."
- **S-2 ACCEPTED.** The tile is now: "In the Loire valley, the first household grew around Martin, a soldier who had left the army to serve Christ. The people of Tours drew him out of his monastery by a trick and made him their bishop." The redundant "He gathered monks around him" is gone.
- **S-3 ACCEPTED.** The Martin voice is now: "Sulpitius says he could not easily be drawn out of his monastery. The people of Tours drew him out by a trick and made him their bishop."
- **S-4 ACCEPTED.** Vita III (l. 809-813): the tribune is his "tent-companion", and the period of "his office" is the tribune's. The cloak telling is now: "His commander, a tribune who shared his tent, promised to leave the world with him once his own command ended. So Martin stayed nearly two more years, a soldier in name only."
- **S-5 ACCEPTED.** The highlight is now: "This is Postumianus, a speaker in the Dialogues. Sulpitius wrote the words of praise he says about Martin." I didn't use the reviewer's wording, because it scored FRE 54.7 and failed regate. This version scores FRE 66.1.
- **S-6 ACCEPTED.** "decades later" became "years later", matching `gallic.figure.cassian`, which says the interval is "not computed".
- **S-7 ACCEPTED.** Unit 5 is now "discretion, the judgment that keeps him between too much and too little". This follows `gallic.term.discretion`: "the royal road between excess and slackness".

## NITs

- **N-1 ACCEPTED.** Death telling: "The whole city his body was brought to poured out to meet it, with people from the villages and towns around."
- **N-2 ACCEPTED.** Institutes note: "where Gaul's climate or habits made them too hard."
- **N-3 ACCEPTED.** Unit 6 now reads "Tours told its story through power." The "instead" is gone.

## Length trims

Restoring the hedges took the main story over 700 words, so I trimmed it:
- "In the years after Martin's death, a man named Honoratus" became "After Martin's death, Honoratus".
- "Sulpitius Severus, an Aquitanian who visited Martin there" became "Sulpitius Severus, who visited Martin there". His origin is still in the Sulpitius highlight and voice.
- "against the monks of Egypt" became "against Egypt's monks".
- "Cassian and his friend Germanus" became "Cassian and Germanus".
- "One grew up in the Loire valley, around the town of Tours" became "One grew up around Tours, in the Loire valley".

## Counts and checks after round 2

- **Main story:** 697 words by whitespace count. The longest sentence is 24 words. Each unit is at FK ≤ 8.72 and FRE ≥ 61.9.
- **Changed tellings:**
  - Honoratus: 228 words, FK 7.06, FRE 73.4.
  - Cloak: 232 words, FK 7.00, FRE 74.4.
  - Death: 225 words, FK 5.99, FRE 80.7.
- **Changed front fields:** Martin voice FK 6.74 / FRE 72.2. Honoratus hedge FK 4.36 / FRE 85.6. who_speaks FK 7.68 / FRE 66.0. No edited field has a sentence over 25 words.
- **Scan:** no dashes, colon reveals, "this world", meta "record", "says nothing", "Nothing survives", "refused to tell" or "decades".
- **Highlights:** every phrase still appears in the story or a telling.
- **Gates:** `records gallic` PASS. `regate gallic --base origin/main` PASS. `engine.m9.cli check` exits 0 with no unwaived gallic findings. `check_live_commentary --base origin/main --enforce` exits 0.

## Record defects for the gaps log (added in round 2; not edited)

1. **Cassian's refusal of wonders is overgeneralized at the record level.** This is the root of R3. Conf. XV.3 narrates Macarius raising a corpse, so the refusal belongs to the Institutes Preface only.
   - `gallic.gravity.virtus`: the description says "Cassian refuses this on principle" and "refuses the whole approach outright". `use_note.means` says "Cassian refuses wonder-tales on principle". The divergence_note cites "Conf. XV.1, XV.6-7" as if those were refusals too.
   - `gallic.force.power-displayed-disowned`: the divergence_note says "Cassian refuses".
   - `gallic.gravity.egypt-as-measure` not_for: "when he refuses wonders".
   - `gallic.story.raising-of-the-catechumen`: the not_for says "where Cassian declines such stories on principle", and the `modern_contrast` says "the south did not tell stories like this".
   - `gallic.contested.egypt-two-measures` (l. 98): "refuses wo[nders]".
2. **`gallic.figure.honoratus` understates Gennadius.** Its divergence_note calls the Arles see "the editorial apparatus's identification". But Gennadius ch. LXX, in ancient text (npnf203 l. 43389-43401, which I verified), reads "Hilary, bishop of the church at Arles ... his Life of Saint Honoratus, his predecessor". Only the year 426 is editorial.
3. **`gallic.story.honoratus-and-the-island` `text`** (not edited) opens "as far as these lines can be read". That keeps the wording hedge, but it is build meta-language inside a participant-retrievable field.
4. The defects listed after the first and second commits still stand: monk-bishop and army-and-rank-before "rough copy"; arian-scattering "Ligugé"; the "this world" sweep across 163 files; the cloak `text` saying "before any monastery existed in Gaul"; OG-40.
