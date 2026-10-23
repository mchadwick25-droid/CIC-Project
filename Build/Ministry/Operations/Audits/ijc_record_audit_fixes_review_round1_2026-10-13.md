Review round 1, ijc record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: BLOCKING

Scope: branch records/ijc-audit-fixes, `git diff origin/main HEAD -- records/ijc` (commits dc5e3fb, 4a1734d, a6b33de; 130 files). Every changed field was pulled out by script, comparing origin/main with HEAD per record: 214 field changes. The intent logs (changes_dw_hl.md, changes_story_demo.md, changes_fig_term.md, changes_quote.md) were read, but every claim was checked by grep against the vendored text in cic/texts/: npnf101, npnf104, npnf111, npnf201, npnf202, npnf203, npnf209, npnf210, npnf212, npnf214, the Ammianus/Yonge text, optatus_against-the-donatists.txt and the Paulinus/Kaniecka text.

Mechanical checks, all clean:
- All records load. `load_world_records('ijc')` returns 186 records.
- No quote `text:` line changed.
- In demonstrations, only representative turns changed (exchange indices 1 and 3). No participant turn changed, and no exchange changed length.
- Readability: every touched spoken field passes grade_text, with FK <= 10 and FRE >= 60. The lowest is ijc.quote.sozomen-thessalonica-law (FK 9.79, FRE 60.5).
- Source citation lines: all 30 records/ijc/source/*.md have one plain line. None matches the forbidden pattern. Every word in each line is already in that record's author/work/edition fields. The only exceptions are abbreviation normalisations ("ser." to "series", "revised" to "rev.") and "trans." added before Yonge (Ammianus), which is accurate. This is not a finding.

## Findings

1. **ijc.quote.no-power-but-of-god, modern_rendering** - BLOCKING
   - Old: `That there should be rulers, that some should rule and others be ruled, and that everything should not simply run on in one confusion ... — this, I say, is the work of God's wisdom.`
   - New: `For there are rulers, and some rule while others are ruled. All things are not just carried on in one confusion, with the people swaying like waves this way and that. This, I say, is the work of God's wisdom.`
   - Source: npnf111 l.53987-53990: "For that there should be rulers, and some rule and others be ruled, and that all things should not just be carried on in one confusion ... this, I say, is the work of God's wisdom."
   - Chrysostom's noun clause ("that there should be rulers ...") is the subject of "is the work of God's wisdom". The new rendering turns it into two flat statements of fact ("there are rulers"; "all things are not ... carried on in one confusion"). That changes what he says: he speaks of the ordering principle, not a report on how things are. The old rendering had this right.
   - Suggested: `There should be rulers, with some ruling and others ruled. All things should not just be carried on in one confusion, with the people swaying like waves this way and that. This, I say, is the work of God's wisdom.` (The whole field then grades FK 4.8, FRE 81.3.)

2. **ijc.quote.chalcedon-definition, modern_rendering** - BLOCKING
   - Old: `...both are united in one Person and one subsistence.`
   - New: `Both are united in one Person and one single being.`
   - Source: quote text and npnf214: "united in one Person and subsistence".
   - "Subsistence" here is hypostasis. In this world's own English, "of one being" is how homoousios (ousia) is rendered (ijc.dw.jesus: "of one being with the Father"). "One single being" therefore reads as one essence, which is the doctrine Chalcedon was excluding. This is a word whose modern sense misleads, at the most doctrinally load-bearing point in the world.
   - Suggested: `Both are united in one Person and one subsistence.`

3. **ijc.quote.nicene-creed, modern_rendering** - BLOCKING
   - Old: `...he came down [from heaven] ... And [we believe] in the Holy Spirit.`
   - New: `...he came down from heaven, and took flesh ... And we believe in the Holy Spirit.`
   - Source: quote text: "came down [from heaven]" and "And [we believe] in the Holy Ghost". Percival brackets the editorial supply.
   - Dropping the brackets presents "from heaven" as words of the 325 creed. They are the editor's supply (the phrase belongs to the 381 form). A rendering must add nothing, and the old rendering kept the brackets.
   - Suggested: restore `he came down [from heaven]` and `And [we believe] in the Holy Spirit.`

4. **ijc.demo.reading-confusion, exchange[1] (representative) and exchange[2] (participant, unchanged)** - BLOCKING
   - Old turn 1: the Augustine narrative ("Augustine, our most famous reader of Scripture ... 'I scorned to be a little one' ...").
   - New turn 1: `...What we do have is one night, when soldiers surrounded our basilica. Our people sang the psalms together all through it, and the singing made the fear bearable. Can we tell you how our people met this book?`
   - Source: Conf. IX.7, npnf101 l.13766-13773: "kept guard in the church ... hymns and psalms should be sung, lest the people should pine away in the tediousness of sorrow."
   - There are two problems.
     - (a) "the singing made the fear bearable" and "the psalms ... all through it" are the very wordings that the same pass removed from ijc.limit.reading-alone as unsourced. That limit now reads "They sang hymns and psalms together, so that sorrow would not wear them down." This demo cites that limit as "statement used directly", so the demo now contradicts its own source record.
     - (b) The unchanged participant turn 2 answers a rep turn that no longer exists: "So even your most famous bishop struggled with it. But he was a trained scholar." The demonstration is now incoherent as an exemplar. Removing Augustine's Confessions III/VIII was correct, because ijc.source.augustine-confessions licenses Book 9 only. But participant turns cannot be edited.
   - Suggested turn 1: `You are not missing something everyone else had. We do not have an ordinary believer's own account of struggling with the Bible. What we do have is one night, when soldiers surrounded our basilica. Our people kept watch in the church and sang hymns and psalms together, so that sorrow would not wear them down. Can we tell you how our people met this book?` (FK 5.6, FRE 77.8.)
   - The dangling participant turn needs a project-lead ruling: rebuild the demo with a new participant turn 2, or retire it. Log this in Open_Gaps_Tracking.

5. **ijc.dw.ancient-custom, text and new sources[4]** - BLOCKING
   - Old: `Damasus built pilgrim roads of verse to make his see's apostolic memory visible.`
   - New: `Damasus used verse to make his see's apostolic memory visible.` A new source entry was added: ijc.source.jerome-de-viris, `De Viris Illustribus 103`.
   - Source: npnf203, Jerome ch. CIII: "had a fine talent for making verses and published many brief works in heroic metre." Nothing about apostolic memory, martyrs or inscriptions.
   - In the same pass, the claim was demoted to a modern reading in three other records:
     - ijc.figure.damasus: "Trout reads ... Jerome does not say so."
     - ijc.term.martyrium: "Modern scholars read ..."; locus: "the notice names no martyr, shrine, grave or inscription".
     - ijc.term.primatus: locus "names no inscription".
   - Here it stays a flat Documented claim, and is now cited to the one notice those loci say does not carry it. The claim is stronger than its cited source, and it contradicts sibling records.
   - Suggested: `Damasus wrote verse. Modern scholars read it as a way to make his see's apostolic memory visible.` Keep the Jerome entry, which supports "wrote verse".

6. **ijc.term.homoios, sources[0].locus** - BLOCKING
   - Old: `the quoted creed formulae ("like the Father", from npnf209 line 8067)`
   - New: `De Synodis, the Ancyra anathema of 358 (likeness in essence, npnf209 line 8067) and Hilary's own reading (sec. 73, line 9397), both pro-Nicene witnesses`
   - Source: npnf209 l.8065-8068 is the Ancyra anathema. The volume's own introduction (l.1876-1885) says the Ancyra party "maintained the homoiousion". Hilary (sec. 73, l.9396) is pro-Nicene.
   - The Ancyra synod of 358 was homoiousian (Basil of Ancyra), not pro-Nicene. The source card would show participants a factual error. The trailing comment is also commentary rather than a place.
   - Suggested: `De Synodis: the Ancyra anathemas of 358 and Hilary's comment on "like" (sec. 73)`

7. **ijc.demo.reading-confusion, exchange[3] / ijc.dw.how-we-read, text** - NON-BLOCKING
   - dw new: `What it shows is the channels: confessing the creed and singing hymns and psalms together.` The read-aloud channel was dropped as uncited.
   - demo new: `The record shows three ways. Scripture was read out loud whenever the assembly gathered. People said the creed together. And they sang the psalms...`
   - The demo cites ijc.dw.how-we-read for "the reception channels, used directly", but now names a channel the dw no longer states, and says "the psalms" where the dw says "hymns and psalms". Public reading is in fact attested in ijc's vendored material: Ambrose Ep. XX, npnf210 l.41575, "whilst the lessons were being read", and l.41786. So one of two fixes:
     - (a) restore the channel in ijc.dw.how-we-read, citing ijc.source.ambrose-epistles Ep. XX; or
     - (b) change the demo to `The record shows two ways. People said the creed together. And they sang hymns and psalms, as they did that night under siege.` (Full turn: FK 2.9, FRE 92.5.)

8. **ijc.demo.bread-and-cup, exchange[1]** - NON-BLOCKING
   - New: `'This is not what nature made, but what the blessing made holy. ... blessing itself changes nature... The Lord Jesus himself declares ... Before the blessing of those heavenly words, one nature is named...'`
   - Source: npnf210 l.33203-33205 and the quote text: "by blessing nature itself is changed ... proclaims ... another nature is spoken of".
   - The words in quotation marks, attributed to Ambrose, are the quote record's old rendering, which this pass corrected in ijc.quote.ambrose-blessing-changes-nature. "One nature is named" also reverses "another nature".
   - Suggested: quote the current modern_rendering, from `This is not what nature made, but what the blessing made holy. The power of blessing is greater than the power of nature, because by blessing, nature itself is changed... The Lord Jesus himself proclaims: "This is my Body." Before the blessing of the heavenly words, another nature is named...` through `After it, it is called Blood.`

9. **ijc.figure.damasus, bridge_line** - NON-BLOCKING
   - New: `The bishop of Rome who wrote verse. Jerome says he made many short poems in heroic meter. Trout reads his verse program as Rome's claim to guard the martyrs' memory. Jerome does not say so.`
   - Source: Trout (2015) is not a source record. It is in copyright and not vendored, and appears only in the record's body note and Build/worlds/ijc/build/SOURCE-REQUEST-MANIFEST.md. A participant hears a bare surname with no card behind it.
   - Suggested: `The bishop of Rome who wrote verse. Jerome says he made many short poems in heroic meter. Modern scholars link that verse to Rome's care for the martyrs' graves. Jerome himself does not.` (FK 3.7, FRE 83.1.)

10. **ijc.dw.marriage-ranked, text** - NON-BLOCKING
    - New: `Virginity is high and steep. Widowhood is rocky and rough. Marriage is smooth and even, but it reaches the camp of the saints by a longer circuit, and most people take it.`
    - Source: npnf210 l.45071-45076: "The path of virginity is good ... Good also is that of widowhood ... Good too is that of marriage; being smooth and even it reaches the camp of the saints by a longer circuit."
    - The paraphrase drops Ambrose's "good" for each path, and adds a "but" that turns his neutral "longer circuit" into a drawback. This tilts the ranking slightly beyond the text. The quote's own not_for forbids "a claim that Ambrose condemns marriage".
    - Suggested: `In a letter to the church at Vercellae, Ambrose sets out the paths, and calls each one good. Virginity is high and steep. Widowhood is rocky and rough. Marriage is smooth and even. It reaches the camp of the saints by a longer circuit, and most people take it.`

11. **Ep. LXIII cited outside the source record's scope: ijc.quote.the-rewards-of-virginity-the-merits-of-widowhood (sources, speaker_or_author) and ijc.dw.marriage-ranked (sources[1])** - NON-BLOCKING
    - The move from Concerning Widows to Letter LXIII.40 is correct. The excerpt occurs once in npnf210, at l.45069-45076, in Ep. LXIII.
    - However, ijc.source.ambrose-epistles `work` lists only Ep. 17-18, 20-22, 40-41, 51 and 61-62, so it does not license Ep. LXIII.
    - The quote's build fields are now stale:
      - use_note.years {377, 380}: Ep. LXIII is 396.
      - not_for: "the argument of a treatise commending widowhood".
      - The body note still says "ch. IV.40-41".
    - Suggested: add Ep. 63 (to the Church at Vercellae) to ijc.source.ambrose-epistles `work`, and update the quote's years, not_for and body note to match. Mechanical.

12. **ijc.demo.want-to-believe, exchange[1]** - NON-BLOCKING (pre-existing words in a touched turn)
    - Current: `'Let the saint rejoice: he draws near to victory. Let the sinner be glad: he is invited to pardon. Let the gentile take courage: he is called to life.'`
    - Source: npnf212 l.14505-14507: "Let the saint exult in that he draws near to victory. Let the sinner be glad in that he is invited to pardon. Let the gentile take courage in that he is called to life."
    - The quotation marks enclose a paraphrase. The new framing ("At Christmas, Leo, our bishop of Rome, preached:") is correct.
    - Suggested: use the verbatim lines inside the marks.

13. **ijc.limit.f5-ordinary-day, statement vs ijc.demo.ordinary-day, exchange[1]** - NON-BLOCKING
    - Limit new: `During one siege they enter the record singing ... The women our record shows acting are mostly two empresses...`
    - Demo new: still `On one besieged night ... The only women our record shows acting are two empresses...`
    - The demo is adapted from the limit, and the two now disagree on "only" versus "mostly". The limit's body note also still says "two empresses".
    - Suggested: carry the limit's two sentences into the demo word for word.

14. **ijc.limit.marriage-money, statement** - NON-BLOCKING
    - New: `It also shows men fighting, sometimes to the death, over our offices. Our preachers also demanded a fair share of it for the poor.`
    - After the split, "it" no longer has "wealth" as its antecedent. "Sometimes to the death" is world-derivable (ijc.quote.ammianus-sicininus-massacre) but is not in this record's only source (Eusebius HE X.5-7).
    - Suggested: `...a fair share of that wealth for the poor.` Optionally, add ijc.source.socrates-he IV.29 to sources.

15. **Locus convention, participant source cards** - NON-BLOCKING
    - The dw/limit edits stripped file and line references from loci (e.g. `IV.61-64 (..., npnf201 from line 67742)` became `Life of Constantine IV.61-64`). The quote, term and figure edits added them. Examples:
      - ijc.figure.theodosius `npnf202 line 40625 ... npnf202 line 42146`
      - ijc.term.homoios `npnf202 line 8557`
      - ijc.term.haeresis `npnf202 line 40625`
      - ijc.quote.no-power-but-of-god `npnf111 lines 53973-53991`
      - ijc.quote.secular-ruler-ecclesiastical-cause, ijc.quote.compelled-to-come-in, ijc.quote.the-reading-of-all-the-documents, ijc.quote.augustine-vigil-hymns, ijc.quote.the-rewards-of-virginity-...
    - Every line number checked points to the right passage. But "npnf202 line 40625" is a vendored-file reference shown to participants, the same kind of thing the citation-line rule forbids.
    - Suggested: one rule for the world. Strip the file/line references from loci and keep them in body notes. Example: `VII.4 (the 380 law issued at Thessalonica); VII.25 (the massacre and the penance)`.

## Checked and clean

All other changed fields were checked against the vendored text and found correct. The new facts that were verified include:
- Callinicum (Ep. XL.6 "at the instigation of the Bishop"; XL.16 Valentinian "temple ... of heathen"; XLI.28 "amend the edict ... end the whole investigation").
- Leo Ep. CIV.3 ("royal ... cannot make it an Apostolic See").
- VC IV.62 Jordan and the Bagster/Gibbon note.
- Leo Serm. on collections ("purged from wicked superstitions", "needier than all the needy").
- Tome ("could both die with the one and not die with the other").
- Hilary introduction ("no ... wide or permanent success").
- Socrates I.8 ("impugn his motives").
- Ep. LI.4/14 (private over public).
- Altar of Victory note (Constantius/Julian/Gratian).
- Paulinus 3 and 9 (governor's residence; eighth day).
- Optatus App. X summary (curial exemptions).
- Anatolius's letter in Percival ("most pious and in all respects faithful", martyry of Euphemia).
- Theodoret II.17 and V.10-11 (Damasus letters).

Build-field edits are consistent with Lactantius ("directed in a dream", no night named): ijc.contested.constantine-conversion, ijc.story.vision-and-alliance absent_detail and ijc.story.dream-before-battle use_note.

Clean records: ijc.demo.argued-about, ijc.demo.hypocrisy, ijc.demo.never-settled, ijc.demo.someone-like-me, ijc.demo.who-was-jesus, ijc.dw.baptism-threshold, ijc.dw.bread-made-body, ijc.dw.collections-discipline, ijc.dw.jesus, ijc.dw.original-sin-transmitted, ijc.dw.received-not-seen, ijc.dw.record-under-question, ijc.dw.room-for-hesitation, ijc.dw.women-authority-cost, ijc.limit.earlier-windows, ijc.limit.inner-life, ijc.limit.jesus-to-you, ijc.limit.later-questions, ijc.limit.reading-alone, all 11 changed stories, ijc.figure.ambrose, ijc.figure.constantine, ijc.figure.constantius, ijc.figure.eusebius-caesarea, ijc.figure.julius, ijc.figure.justina, ijc.figure.leo, ijc.figure.marcian, ijc.figure.pulcheria, ijc.figure.theodosius (bridge_line), all term spoken fields except the homoios locus, the other 33 changed quote renderings, and all 30 source citation lines.
