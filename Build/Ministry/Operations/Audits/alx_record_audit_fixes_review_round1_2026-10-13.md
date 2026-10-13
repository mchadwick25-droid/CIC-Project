Review round 1, alx record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: BLOCKING

Scope: commit 6c991ef (HEAD), 100 files under records/alx plus the removal of the `m9:source-citation/alx` waiver in engine/m9/enforce.py. The 25 source `citation` lines are in the parent commit 5f3b622 and were reviewed there. Each changed field was compared old against new (`git diff HEAD~1 HEAD -- records/alx`). Every changed key is a spoken field under engine/m1/spoken_fields.py: doctrinal_witness `text`, demonstration representative turns, figure `bridge_line`, honest_limit `statement`, quote `modern_rendering` and `text`, story `tellable_as` and `text`, and term `plain_meaning`, `quick_meaning`, `senses.personal` and `senses.translational`. No participant turn, `sources`, `confidence`, `use_note` or other build field changed. Every touched graded field passes FK <= 10 and FRE >= 60 (`engine.m1.gates.grade_text`); the lowest FRE is 60.01 (alx.term.didaskalos translational) and the highest FK is 9.74 (alx.figure.athanasius). Facts were checked by grep against cic/texts/ (npnf201 Eusebius, anf02 Clement, anf04 Origen, anf09 Origen on Matthew, npnf204 Athanasius, npnf203 Rufinus, palladius_lausiac-history_clarke1918). Editor logs and audit_*.md in the session scratchpad were read for intent.

## Findings

1. **alx.demo.marriage-ending, exchange (representative turn)**
   - Old: `That book has come down in a form we cannot quote to you in your tongue, and your second question - the whether and how of marrying again - lives mostly in its pages.`
   - New: `That book has come down in a form we cannot quote to you in your tongue. So your second question, about marrying again, we cannot answer.`
   - Source: anf02 l.34981-34984, Stromateis II.23, in English in the same alx.source.clement-stromateis this record cites: "the Scripture counsels marriage, and allows no release from the union ... and it regards as fornication, the marriage of those separated while the other is alive." Also anf09 l.37713-37722, Origen, Commentary on Matthew XIV (alx.source.origen-comm-matthew): "some even of the rulers of the church have permitted a woman to marry, even when her husband was living, doing contrary to what was written ... not indeed altogether without reason".
   - BLOCKING. The new line states a flat absence ("we cannot answer") that the world's own English sources contradict. The old line was already soft on this, but this edit makes it absolute. The accepted absence (alx.limit.marriage, G1) covers Stromateis III only, not II.23. The proposed text answers from II.23 and needs `II.23` added to the record's clement-stromateis locus. If Mark prefers that the turn stay inside the limit's `not_for`, the smallest true version only says Clement wrote on remarriage elsewhere, with no "cannot answer".
   - Proposed: `Our record names no rule that closed baptism or the bread to someone whose marriage had ended. It is also silent on how we received them, so we will not claim more. What we held about marriage itself was high: lasting, honorable, a place where souls are formed. Our teacher Clement wrote a whole book defending it against those who despised the body. That book has come down in a form we cannot quote to you in your tongue. But on marrying again he wrote elsewhere, in a book we can give you. He said Scripture allows no release from the union, and counts it as fornication when people who have separated marry while the other still lives. We can give you the heart: marriage honored, the body not despised. The finer grain we must leave in the sources rather than guess at. One more thing, because you may be asking this for your own life: it is not our place to weigh you. We can tell you what we held; the telling is not a judgment on you.` (FK 6.6, FRE 76.4)

2. **alx.dw.church-failure, text**
   - Old: `At our best, we refused the two easy exits: we did not pretend the failure away, and we did not make the failed unforgivable. At our worst, we did what churches with power do.`
   - New: `We refused the two easy exits: we did not pretend the failure away, and we did not make the failed unforgivable. At our worst, we did what churches with power do.`
   - Source: the same text names "the strict party [that] demanded they stay out", which took exactly the "unforgivable" exit (HE VI.45, npnf201 l.38897, Dionysius's letter to Novatus).
   - NON-BLOCKING. Removing the coined pair also removed the qualifier. The claim is now made for the whole community, and the field's own strict party contradicts it. The paired "At our worst" now has nothing to pair with.
   - Proposed sentence: `Where the restoring side won, we refused the two easy exits: we did not pretend the failure away, and we did not make the failed unforgivable.` (whole field FK 7.1, FRE 65.8)

3. **alx.demo.who-was-jesus, exchange (representative turn)**
   - Old: `Not that we become gods - but that his own life is opened to us and shared. If you want it in one line: the maker, come inside his making, to heal it.`
   - New: `We did not mean that we become gods. We meant that his own life is opened to us and shared.`
   - Source: npnf204 De Incarnatione 54, "He was made man that we might be made God". In the same commit, alx.term.theosis plain_meaning dropped "Not becoming a god" as an editorial gloss that the cited source does not carry (term audit B).
   - NON-BLOCKING. The log says the "not X, but Y" pivot was removed, but it was only split into two sentences, and the unsourced denial stays. The world now gives two answers to the same point.
   - Proposed closing: `By that we meant that his own life is opened to us and shared.` (whole turn FK 6.0, FRE 86.9)

4. **alx.term.baptism, senses.personal**
   - Old: `No one comes up from the water already fully formed - they come up as someone who has truly crossed a threshold, with a whole life of formation now opened rather than finished.`
   - New: `Clement said that at regeneration we are illuminated, which is to know God. Yet a whole life of formation still lay ahead.`
   - Source: anf02 l.19269-19271, Paedagogus I.6: "Straightway, on our regeneration, we attained that perfection after which we aspired. For we were illuminated, which is to know God." Later in the chapter: "Nothing is wanting to faith, as it is perfect and complete in itself"; "the end is reserved till the resurrection".
   - NON-BLOCKING. The audit's defect was that this field contradicted I.6's claim that perfection comes at regeneration. The "Yet" sentence turns the quoted line against itself and puts the same tension back. I.6's own qualifier is the resurrection, not unfinished formation.
   - Proposed: `Clement said that at regeneration we are illuminated, which is to know God. He held that nothing was lacking to that faith, though its end waited for the resurrection.` (FK 8.0, FRE 63.8)

5. **alx.term.arete, quick_meaning**
   - Old: `Not a habit built by effort - the fruit of a soul truly changed.`
   - New: `The fruit of a soul truly changed, reached through training and will.`
   - Source: anf02 Stromateis VII ("Not without, but through the exercise of will, and by the force of reason"). The new plain_meaning gives training and will "a part". The record's unchanged `false_friend` ("excellence built through repeated practice, as in Aristotle") and `use_note.means` ("something a soul receives ... not a skill built by habituated practice") still say the opposite.
   - NON-BLOCKING. The quick meaning makes training and will the route. That is stronger than the plain meaning above it, and it contradicts the record's own false friend.
   - Proposed: `The fruit of a soul truly changed, with training and will playing a part.` (FK 4.2, FRE 89.9)

6. **alx.term.thanatos, plain_meaning**
   - Old: `The soul's separation from God, which sin causes. Physical death is real, but it comes second. ...`
   - New: `The ruin that follows when the soul turns from God and loses the knowledge of him. Bodily death is real, but it is where that loss ends.`
   - Source: npnf204 De Incarnatione 4-6. Death and corruption are where the loss of the knowledge of God leads; they do not end it. The record's own quick_meaning ("which bodily death completes") and personal ("sealed it") say this.
   - NON-BLOCKING. "Where that loss ends" can be read as death bringing the loss to an end, which is the reverse of the claim.
   - Proposed: `The ruin that follows when the soul turns from God and loses the knowledge of him. Bodily death is real, and it is where that loss leads.` (FK 3.7, FRE 92.9)

7. **alx.demo.women-own-words, exchange (representative turn)**
   - Old: `the household, where faith passed from mother to child`
   - New: `the household, where Origen learned Scripture from his father and was held back from the arena by his mother.`
   - Source: npnf201 l.32550-32554, HE VI.2: "carried away with his zeal for martyrdom, she hid all his clothing, and thus compelled him to remain at home". Leonides was beheaded; the passage has no arena or games.
   - NON-BLOCKING. The fix is right in substance, but "arena" adds a setting the source does not give.
   - Proposed sentence: `And we can point to the household, where Origen learned Scripture from his father and was kept from martyrdom by his mother.` (whole turn FK 5.4, FRE 77.6)

8. **alx.demo.want-to-believe, exchange (representative turn)**
   - Old: `Gregory, said belief came to him almost from the side ... He was not straining to believe. He was being befriended.`
   - New: `One of our students, Gregory, said it began for him while he studied under a teacher: 'like some spark lighting upon our inmost soul, love was kindled.'`
   - Source: anf06 l.3018, Address of Thanksgiving VI: love "kindled ... a love at once to the Holy Word ... and to this man". Gregory speaks of love, not belief (term audit B4).
   - NON-BLOCKING. Coming after "force belief" and "before ever coming to the water", "it began" still reads as belief beginning. That is the audit's B4 defect in a milder form. The quote can carry the claim without "it".
   - Proposed sentence: `One of our students, Gregory, said that while he studied under a teacher, 'like some spark lighting upon our inmost soul, love was kindled.'` (whole turn FK 5.6, FRE 82.5)

9. **alx.demo.going-to-hell, exchange (representative turn)**
   - Old: `Judgment is real: what we do matters, and God is not mocked.`
   - New: `Judgment was real: what we do mattered, and God is not mocked.`
   - NON-BLOCKING. The tense fix is half applied: "what we do mattered" mixes present and past. The audit (B5) asked for "what we did mattered".
   - Proposed: `Judgment was real: what we did mattered, and God is not mocked.`

10. **alx.term.anastasis, senses.personal**
    - Old: `The one growing in prayer, community, and the Eucharist is already living in a resurrection at work now, not only a hope held for later.`
    - New: `Anyone who grew in prayer and shared life already lived in the resurrection at work now. It was more than a hope for later.`
    - NON-BLOCKING. The tense change leaves "now" inside a past-tense sentence ("already lived ... at work now"). The Eucharist removal is correct; De Inc. 8-10 and 20-32 do not mention it.
    - Proposed: `Anyone who grew in prayer and shared life already lived in the resurrection at work in them. It was more than a hope for later.` (FK 5.3, FRE 79.1)

Observed but not introduced by this change (pre-existing, outside the change's intent; listed so they are not lost):
- **Stale `use_note.means` on fixed terms.** use_note.means reaches the model through the evidence block (engine/m4/evidence.py l.1164-1169). It still carries the claims this pass removed from the spoken fields: baptism ("Christ's death and rising"), christ ("priest, king, and prophet"), hamartia ("missing the mark ... rather than a debt owed or a law broken"), prayer ("attend to what God is already saying"), thanatos ("physical death a real but secondary outward sign"), salvation ("not a not-guilty verdict"), oikos ("where most people were formed"), fall-descent ("confessed by all"), incarnation ("not to teach or model") and arete (see finding 5). alx.term.hamartia `world_word`, a participant label, still reads "hamartia (missing the mark)". The editors logged these as out of scope. They need their own slice and an Open_Gaps_Tracking entry, because until then the evidence block can put the removed claims back into speech.
- **Build-record source gaps the editors logged.** alx.dw.record's "Origen compared manuscript readings" (anf09 Comm. John VI) and alx.dw.church-failure's deathbed point (HE VI.44) both rest on loci missing from the records' `sources`. alx.term.arete still cites athanasius-vita-antonii "(whole)" against alx.contested.desert-attribution.

## Changes checked and found sound

- **Quote `text` (three typographic fixes).** In clement-rash-martyrdom, "Creator)—" matches anf02 l.37822-37823, where the vendored footnote sits between "Creator" and ")". The two curly quotes on “a perfect man.” in the-grades-here-in-the-church match anf02 l.47899-47900.
- **Quote renderings, re-checked clause by clause against `text`.** No clause is dropped and nothing is added, no sentence runs past about 25 words, and no modern word misleads:
  - a-doctrine-they-would-not-have-taught restores "undertaking" and "human life".
  - appointed-by-the-fathers renders "those who newly join us" and "word of godliness".
  - athanasius-death-trampled-down restores the two conditionals and "displayed trophies". The dash is gone.
  - clement-instructor restores "passions".
  - clement-new-song restores "beasts" and "harmonious arrangement".
  - clement-possessions renders "the brethren", "superior to the possession" and "bind and circumscribe" faithfully.
  - clement-rash-martyrdom restores "not belonging to us, but sharing the name merely".
  - clement-schoolmaster renders "directly and primarily" and paidagogos as "guardian".
  - dionysius-nepos and dionysius-too-high drop the added "precisely" and "all the more".
  - ecclesiastical-and-apostolical-tradition keeps "differs in no respect".
  - no-sun-no-moon-no-sky restores "as it were" and "first, second and third".
  - origen-scripture-senses renders "granted by God".
  - the-grades keeps "as deacons" and "promotion in glory".
  - timothy-ordinary-questions keeps the question numbers and the ellipses of `text`. "Eucharistic offering" fairly glosses "oblation".
- **Doctrinal witness.**
  - alx.dw.councils: the new Arsinoe sentence matches HE VII.24.6-7 (npnf201 l.41344-41356: "presbyters and teachers of the brethren in the villages, such brethren as wished being also present ... from morning till evening for three successive days").
  - alx.dw.doubt: "split over Nepos's reading of the promises" matches "schisms and apostasies of entire churches".
  - alx.dw.resurrection: the danger-and-courage sentence matches Contra Celsum (alx.quote.a-doctrine-they-would-not-have-taught).
  - alx.dw.was-jesus-god: the unsupported "explicit that no new God was voted in" is gone.
  - alx.dw.original-sin: the infant-baptism sentence is removed. A grep of anf02, anf04, anf06 and anf09 finds no Alexandrian locus for it. The tense is now past.
  - alx.dw.suffering: the invented "found him most present" is gone.
  - The coined closers are removed from alx.dw.apostolic, alx.dw.record, alx.dw.empire and alx.dw.jesus, and the three-beat is removed from alx.dw.god. No hedge was lost in any of them.
- **Honest limit.** alx.limit.marriage's statement now matches its own `why_sources_cannot_answer` (ANF leaves Stromateis III in Latin). The false "survives in the Greek ... no one has given us an English rendering" is gone.
- **Stories.**
  - potamiaena: "burning pitch" and "bade him take courage" match HE VI.5.3-4 (npnf201 l.32968-32981). "Later a martyr" matches VI.5.5-7, and the process narration is gone.
  - origen-daring-deed: "Soon afterward" is Eusebius's own wording (l.33217-33218). The tellable_as now carries the Contested status, which McGiffert's note backs (l.33140ff.: "Some have even gone so far as to believe that he never committed the act").
  - didymus-meeting: "Didymus the blind author" and "four times ... ten years" match Palladius IV.1 (l.211). The seer epithet is moved to later tradition, in line with the record's absent_detail (npnf203 l.48652).
  - plague-nursing, origen-demetrius and arsinoite-conference: only unsourced glosses are removed. gregory-formation: "half" is removed.
- **Demonstrations.**
  - marriage-ending: the belonging claim is now bounded to the absence in the record. Finding 1 concerns only the remarriage sentence.
  - woman-authority: Basilides is told as in HE VI.5.5. "Recognized standing", "for generations" and the assistant aside are gone.
  - couldnt-believe: the counterfactual is replaced by "The account we have ends in agreement".
  - someone-like-me: "We called Christ the door" is supported by Protrepticus (anf02 l.15400, "For I am, He says, the door").
- **Figures.**
  - origen: the line now follows the record body and alx.contested.origen-positions.
  - pantaenus: the bee attribution follows HE V.11 and McGiffert (npnf201 l.28754, "from which it is generally concluded").
  - gregory-thaumaturgus: Caesarea.
  - athanasius: "some forty-five" matches the dates block (328-373), and "this world's Center" is removed.
  - antony: "landowner's son" matches Vita Antonii.
  - heraclas: matches HE VI.26.
  - dionysius: "argument" matches HE VII.24.7.
  - clement and didymus: tells and jargon are removed.
- **Terms (other than findings 4-6 and 10).**
  - Sound against their sources: prayer (Strom. VII.7, 12 "converse with God", anf02 l.49987, 51819); ekklesia (Strom. VII.5 "assemblage of the elect", l.50447); episkopos (re-attributed to presbyters, Strom. VI.13 l.47866); martys (Strom. IV.4, heretics who hated the Creator); eucharistia (Paed. I.6 l.19760-19777, "nourishing them up to immortality"); theosis (De Inc. 54).
  - Contested status now stated, not settled: christ, incarnation, salvation, hamartia, oikos, apokatastasis, fall-descent and logikos follow the audit's corrections.
  - homoousios is now attributed to Athanasius, writing later; allegoria to "Alexandrian teachers"; lapsi "well documented".
  - Tense and "this world" fixes in the we-voice fields keep every hedge.
- **Source citations (commit 5f3b622, 25 lines).**
  - None matches `_CITATION_BUILD_TEXT` in engine/m9/confinement.py.
  - Each line uses only words from its record's author, work and edition fields. The one exception is "Nicene and Post-Nicene Fathers", the expansion of the edition field's "NPNF".
  - Disputed authorship is not asserted. Excerpts of Theodotus names no author, and the Syriac Life of Antony carries the title's own attribution.
- **Waiver removal.** All 25 alx source records now carry a citation, so the `m9:source-citation/alx` waiver (count 25) would be stale. Removing it is correct.
