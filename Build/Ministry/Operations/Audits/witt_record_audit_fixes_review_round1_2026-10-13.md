Review round 1, witt record audit fixes, 2026-10-13, reviewers: two independent Opus subagents (part A: doctrinal witnesses, stories, demonstrations, figures, honest limits, quotes, force and gravity; part B: terms)

Verdict: BLOCKING (both parts). Every blocking finding was fixed in the working tree before the rebuild; the non-blocking ones were fixed where the fix was plain and the rest are listed in the log entry. Round 2 rechecks only what changed.

# Part A

Verdict: BLOCKING

Scope: uncommitted working-tree changes under records/witt/{doctrinal_witness,story,demonstration,figure,honest_limit,quote,force,gravity}/ (55 files). I read them with `git diff -U2`. I checked every changed spoken field and every changed locus against the cited witt records and the vendored texts in cic/texts/: luther_works-v1/v2/v3, luther_table-talk_bell1886, luther_hymns_bacon-allen, luther_small-catechism_smith1994, luther_large-catechism_bente-dau1921, melanchthon_augsburg-confession_anon-pg275 and melanchthon_apology-augsburg-confession_bente-dau1921. Readability was run with engine.m1.gates.grade_text on every touched spoken field. All of them pass FK<=10 and FRE>=60. The `positions` lists in the doctrinal witnesses fail the gate, but this pass did not change them. Citation lines on records/witt/source are out of scope. No unrelated text changed: the other edits are YAML re-wraps and quote-escaping only.

## Findings

1. **witt.gravity.promise-and-sign, sources[1].locus**: BLOCKING (wrong locus)
   - Old: `source_id: witt.source.luther-treatise-on-the-holy-sacrament`, locus `'v1 2271-2272: the 1519 sacrament treatise''s own three-part reduction'`
   - New: same source_id, locus `v2 6695-6701; 10362-10364: the 1520 reduction of the seven sacraments to three, then to two`
   - Source: witt.source.luther-treatise-on-the-holy-sacrament is *A Treatise on the Holy Sacrament of Baptism* (1519, vol. I). v2 6695-6701 and 10362-10364 are in the Babylonian Captivity (v2 6470 onward), which sources[0] of this same record already cites.
   - The new locus pins a passage of one work under another work's source_id. Fix it one of two ways. Either restore a locus the Baptism treatise supports, `v1 2269-2272: baptism's three things - the sign, the significance, and the faith`, or remove this entry, because sources[0] already carries the reduction. In this record the same locus was also fixed in description and manifestations, and those fixes are correct.

2. **witt.dw.true-priests-of-gods-own-making, sources[0].locus**: BLOCKING (locus now quotes text that is not in the cited record)
   - Current: `... 'the only martyr-song this library holds'; 'true priests of God's own making'`
   - The pass rewrote witt.story.brussels-martyrs, and its text now says "the only martyr-song we have from his hand". The quoted phrase no longer appears in the cited record. It is also build vocabulary on a card that participants see.
   - Fix: `the whole story: two named monks burned at Brussels on 1 July 1523 for refusing to recant; the only martyr-song we have from Luther's hand; 'true priests of God's own making'`. sources[2] in the same record ("this library holds ... never independently vendored") was not changed by this pass, but it carries the same build vocabulary. Clean it while the record is open.

3. **witt.demo.someone-like-me and witt.demo.the-way-in, sources (household-catechism-lesson-typical-practice).locus**: BLOCKING (same cause as 2)
   - Current: `'no single household's own record survives... what survives is the program'` and `'no single household's own record survives'`
   - The story's text now reads "No record survives from inside any single household ... What survives is the program every household was told to follow." The quoted phrase is gone from the cited record.
   - Fix: requote the new wording, e.g. `'No record survives from inside any single household'; 'What survives is the program every household was told to follow'`. The exchange_note prose in both demos (lines ~49 and ~55) quotes the old line too. That prose is a build field, but it should follow.

4. **witt.quote.the-poor-man-who-comes-to-you, modern_rendering**: NON-BLOCKING, but needs an Opus re-render before approval
   - New: `When the poor man comes to you -- and there are so many of them now -- he must buy with the penny of his daily wages and live on it. And you are harsh to him, as though everyone lived by your favor.`
   - Text: `When the poor man comes to you ... who must buy with the penny of his daily wages ..., and you are harsh to him, ... he will go away wretched`
   - Problems: (a) The text is one conditional: when he comes and you are harsh, he will go away wretched. The rendering breaks that conditional into flat statements. "And you are harsh to him" now reads as an accusation of the reader, not a case Luther is supposing. The old rendering ("Say you are harsh...") kept the conditional. (b) The "when" clause now attaches to "he must buy". In the text, "must buy" is a relative clause about the poor man. (c) The first sentence is 31 words, over the ~25 limit. Every other clause is rendered faithfully.

5. **witt.demo.who-held-authority, exchange[1].text**: NON-BLOCKING (misleading word)
   - New: `Our founder said he had been regularly called by the Council to preach in his place.`
   - Source: v2 14778-14779, "regularly called by the Council to preach in this place".
   - "In his place" reads as "instead of someone else". Use `to preach in Wittenberg` or `to preach there`. Also, "God ruled in two ways, we said" and "Through the Word he made Christians" put God's own action in the past tense. The rule keeps present tense for who God is: `God rules in two ways, we said. Through the Word he makes Christians...`.

6. **witt.dw.cold-and-careless-among-us, text para 1**: NON-BLOCKING
   - New: `...those who taught the faith among us were failing at it... He spoke of pastors and preachers of our own. In 1522 he told his own Wittenberg congregation that an ass can almost intone the lessons...`
   - Source: v2 14681-14688. The "ass" line rebukes the congregation, the hearers who repeat doctrine ("why should you not be able to repeat the doctrines"), not its pastors. The date and the 1522 Eight Sermons attribution are now correct and verified.
   - The paragraph's framing sentence points the 1522 example at teachers. Suggest `Our own founder said, more than once, that the faith was failing among us, among those who taught it and those who heard it.` Keep the rest. The new closing hedge on the Table Talk answer ("though the exact words are not certain") correctly matches the story's Contested rating.

7. **witt.dw.scripture-judges-every-other-voice, text para 2**: NON-BLOCKING (redundancy)
   - New: `Our confession states the same rule more gently, alongside the wider Church. ... Our founder spoke sharply. Our confession spoke more gently, alongside the wider Church. We hold to both and do not blur them into one.`
   - The paragraph repeats its own first sentence almost word for word. Paragraph 1 already says "We hold both, rather than smoothing them into one tone." Cut the last three sentences of paragraph 2 so that it ends at "...nor Rome's own writers."

8. **witt.dw.one-holy-church-forever, text para 3**: NON-BLOCKING
   - (a) `We can tell you that we drew a line against those who taught otherwise on the Supper.` This restates the sentence before it. Suggest `We can tell you that the break was real and that we held our ground.`, which is the old sense without the repeat.
   - (b) `is not something our own library lets us narrate from the inside` keeps "library", which is build vocabulary, in a paragraph the pass rewrote. Suggest `is not something our own texts let us tell from the inside.`
   - (c) The new `Our texts name none of those we broke with` matches witt.force.reformed-rival-by-absence (zero hits). But witt.limit.record-thinnest and witt.demo.record-thinnest still say the names "barely appear". The two forms are compatible but uneven. Align them if convenient.

9. **witt.dw.what-we-have-never-settled, text para 4**: NON-BLOCKING
   - New: `In our founder's own words, these are not plainly one doctrine under one name.`
   - This reads as if Luther said so himself. Suggest `Read in our founder's own words, these are not plainly one doctrine under one name.`
   - Separately, paragraph 3 was re-wrapped only, but it calls the "accounted righteous / made righteous" wording "a point in our own confession". The demo fix (finding-level change in witt.demo.faith-alone) correctly places that wording in the Apology (Apology l.1426). Consider `a point in the Apology that defended our confession` so the two records agree.

10. **witt.dw.truly-god-and-truly-man, text para 2 and sources[1].locus**: NON-BLOCKING
    - `-- no saint and no scholar in his place.` "Scholar" is new and has no source behind it. The old wording was "no saint, no teacher, no priest of our own". witt.term.christ-alone is about the saints' intercession. Suggest `-- no saint and no priest of ours beside him.`
    - Locus `'on account of the righteousness of another, namely, of Christ' (Apology)` is verbatim in the Apology (l.3223). The cited record witt.term.justification, however, still carries the non-verbatim `'the merits of another, namely, of Christ alone'`; the vendored text has "of Christ", without "alone". That belongs to the terms reviewer, and I flag it for cross-reference.

11. **witt.story.first-german-mass-sung, text para 3**: NON-BLOCKING
    - New: `Walter added his own view: "The most profitable songs for the common multitude are the plain psalms and hymns,"`
    - Source: hymns l.773-778. After an ellipsis, the letter does not make clear whether this is Walter's view or his report of Luther's. The old wording took the other reading. Neutral wording is safer: `Walter's letter goes on: "The most profitable songs..."`. The quote also drops "both Luther's and the earlier ones" without an ellipsis; add `...` after "hymns".

## Quote renderings, clause by clause

- **article-ii-of-original-sin**: Every clause is rendered. "Concupiscence" becomes "evil desire", "vice of origin" becomes "inborn fault" and "original depravity" becomes "inborn corruption". All three are accurate and none misleads. Nothing is added except a repeated "They teach that" to carry the subject. The longest sentence is 26 words, which is acceptable. Sound.
- **article-ix-of-baptism**: Complete and faithful. Sound.
- **christs-return-to-judgment**: Complete. "Consummation of the World" becomes "end of the world". "Jewish opinions" is kept as the text has it. The longest sentence is 25 words. Sound.
- **congregation-of-saints**: Complete and faithful. "Gospel" now replaces "good news", matching the text. Sound.
- **nothing-that-varies**: Complete. "Received" becomes "accepted", which fits. The locus fix (Conclusion following Article XXVIII, not XXI) is correct: CONCLUSION is at AC l.1531, after Article XXVIII at l.1271, and the quoted words are at l.1547. Sound.
- **second-article-of-the-creed**: Complete. It keeps the text's own "And in Jesus Christ" opening and adds no "I believe". Sound.
- **the-poor-man-who-comes-to-you**: See finding 4.

## Changes checked and found sound

- witt.dw.a-death-begun-that-a-child-receives: "our founder wrote" for "a death begun" is correct. It is the 1519 Baptism treatise ("the beginning of a blessed death", v1), not the catechism. The drowned old Adam now goes to the Small Catechism (l.398), which is correct. The tithes sentence now matches AC XXVIII l.1354 ("as of matrimony or of tithes ... they have it by human right"), which fixes the old "civil courts" drift.
- witt.dw.how-the-promise-reached-us: "I did nothing; the Word did it all" is verbatim at v2 14931, and "preached, taught, and written down" matches v2 14928.
- witt.dw.born-in-sin-fed-at-the-table: the past-tense recast is good. The faith-alone breadth claim is backed by witt.gravity.justified-by-faith-alone ("every kind of writing") and witt.term.faith. "Though they earned nothing" replaces the coined fruit-tree closer cleanly.
- witt.dw.true-priests-of-gods-own-making: "by the power of grace ... true priests of God's own making" and "a refusal to deny God's Word" are both checked against the hymn, stanzas 3 and 6 (hymns l.1764-1797). The term.martyr locus phrases are verbatim at hymns l.1744 and l.1756.
- witt.dw.one-holy-church-forever: the new locus for the AC Art. X quote is correct (AC l.324).
- witt.dw.a-confession-answered-not-a-vote, a-narrow-word-plainly-spoken, nothing-against-scripture-or-the-church-catholic, the-household-we-can-describe: these are cuts to the closers and the tense. The new household scene matches LC l.242.
- witt.story.augsburg-before-cajetan: the kneeling, lying "all along upon the ground" and "three times bade me arise" are verbatim at TT l.3450-3453. The Cardinal's speech is now verbatim.
- witt.story.brussels-martyrs: "Satan's mock and masquerade" is verbatim (stanza 5), and "one line ... says what the stripping meant" fits stanzas 5-6. The coined closer is gone.
- witt.story.composing-the-magnificat: "30 October 1520", the copy of the letter to his uncle, the quires and the dedication letter all check out against v3 l.6303-6336.
- witt.story.diet-of-augsburg-1530: the signatories and "ready, God willing, to present ampler information according to the Scriptures" check out against AC l.1551-1567. "Two city councils" corrects the overcount, and the locus is fixed to match.
- witt.story.first-german-mass-sung: the sequence ("kept me three weeks ... to write out the notes"), Vespers, the charity-scholars and "no satisfaction ... nothing but German songs" all check out against hymns l.752-776.
- witt.story.household-and-kate-on-prayer, household-catechism-lesson-typical-practice: the Home Chart headings (SC l.610-665), the TT chapter title (TT l.2394) and the LC preface quotes are all correct.
- witt.story.letter-to-albrecht-and-theses-circulation: "Primate of the Church" (v1 l.996) and "money-box" (v1 l.1021) are now true to the letter, and the overlong locus note was trimmed.
- witt.story.prayer-for-rain-1532: the invented "not let the whole town suffer" is replaced by the prayer's actual "thou hast still means whereby to maintain those that are thine" (TT l.3171-3173). "Changed and refreshed in a most miraculous manner" is verbatim.
- witt.story.return-and-the-eight-sermons: "against the Elector's instruction to stay", "Karlstadt and others" and the Kessler quote are verbatim or supported at v2 l.14440-14510.
- witt.story.speratus-hymn-under-the-window and witt.figure.speratus: the eight-hymn book, four of them Luther's and "not less than three" by Speratus, and the "Eight Songs" tune trace are correct (hymns l.106-110, l.686-690). The divergence_note four-to-eight fix is a verified factual correction.
- witt.story.worms-1521: "books of doctrine; the same I neither can nor will revoke" and the young Landgrave who "desired that I might be heard" are verbatim at TT l.3543-3566. The Carlyle wording is now quoted as the hymn editor gives it.
- witt.demo.bread-and-cup: "rejoiced that the simple faith of this sacrament was still found among common people ... as they do not understand, neither do they dispute" is checked against v2 (Babylonian Captivity). The demo.faith-alone move from "confession" to the Apology is correct (Apology l.1426). demo.record-thinnest, scripture-alone, the-way-in and true-priests-by-no-ordination keep their content, with tense fixed and the coined lines cut.
- witt.figure.* bridge_lines and names: all supported. Removing the out-of-text "Hendrik Vos and Johann van Esschen" label is correct.
- witt.limit.no-outsider-witness and record-thinnest: the content is unchanged, with build vocabulary and closers removed.
- Force records: "Christian Nobility of the German Nation" matches the title at v2 l.1787. Duke George's complaint of March 1523 is checked against v3 l.11744. inheritance-refused gets the corrected Babylonian Captivity lines (v2 l.6695-6701, l.10362-10364). In gravity.bodily-presence, re-pointing v2 7143-7224 to the Babylonian Captivity source is correct.

# Part B

Verdict: BLOCKING

Scope: uncommitted working-tree changes under records/witt/term/ (66 files). I parsed each file at HEAD and in the working tree and compared every field. The changed fields are plain_meaning (16), quick_meaning (13), senses.personal (13), senses.translational (5) and sources[].locus (148). No other field and no record body changed, so the YAML re-wrap is the only other difference. Facts were checked by grep against cic/texts/: luther_works-v1/v2/v3 (Jacobs-Spaeth), luther_large-catechism_bente-dau1921, luther_small-catechism_smith1994, luther_table-talk_bell1886, luther_hymns_bacon-allen, luther_bondage-of-the-will_cole1823, melanchthon_augsburg-confession_anon-pg275. Grades come from engine.m1.gates.grade_text. For term, engine/m1/spoken_fields.py and the gate list only plain_meaning and quick_meaning as spoken fields.

Root cause of B1 to B5: in five records the applied text does not match the audit's `fix`. In each case the whole fix sentence replaced only part of the `old` span, or was added beside it. Some of the fix's own instruction text was also pasted in literally. The edits for parts A and C came from the same apply step (apply_edits.py, story_apply*.py), so those parts should get the same repeated-text check.

## Findings

1. **witt.term.household, plain_meaning** (spoken)
   - Old: `The household is where our catechism is taught. A father questions his family and servants every week. ...`
   - New: `The household is where our catechism is taught. The household is where our catechism was taught. Our books told a father ...`
   - Source: the audit fix (findings_terms1) starts "The household is where our catechism was taught." The old first sentence was left in place.
   - BLOCKING. The same sentence now appears twice, once in present tense and once in past. Delete the first sentence. The rest is sound (LC l.241-242 "at least once a week"; SC Appendix I l.538-539, 579 morning, evening, meals). With the sentence removed it grades FK 4.8 / FRE 82.

2. **witt.term.fear-and-love-god, plain_meaning** (spoken)
   - New: `...So every commandment ties back to trust, the First Commandment's own lesson. This ties each commandment back to trust, the First Commandment's own lesson.`
   - BLOCKING. The old second sentence was kept after the fix sentence, so the closing claim is said twice. Delete the final sentence. It then grades FK 6.1 / FRE 72. The new claim that only commandments 2 to 10 open with "fear and love" is correct.

3. **witt.term.satisfaction, senses.translational** (reaches the glossary via engine/m4/term_glosses.py)
   - New: `A participant who hears 'satisfaction' in the sense we refuse (our own) inside a sentence about the sense we rest on (Christ's) A participant who hears 'satisfaction' ... has mixed the two meanings.`
   - BLOCKING. The fix was added next to the old span, which doubled the subject and left the sentence ungrammatical. It should read once: `A participant who hears 'satisfaction' in the sense we refuse (our own) inside a sentence about the sense we rest on (Christ's) has mixed the two meanings.`

4. **witt.term.the-two-governments, senses.personal**
   - New: `...and the sword from being the Church's instrument -- We prayed for the prince in the petition for daily bread.`
   - BLOCKING. A capitalised sentence was spliced in after a dash, so the text is broken. Change the dash to a full stop: `...the Church's instrument. We prayed for the prince in the petition for daily bread.` That grades FK 5.6 / FRE 82. The content is supported by LC l.3500-3504, the Fourth Petition.

5. **witt.term.pope-and-antichrist, sources[1].locus and sources[3].locus** (participant source card)
   - Old [1]: `Papacy at Rome -- 'the papacy is the mighty hunting of the Roman bishop'`
   - New [1]: `the Papacy at Rome (1520), the pope and the Roman Church. Move the quotation 'the papacy is the mighty hunting of the Roman bishop' to the Babylonian Captivity locus.`
   - New [3]: `Babylonian Captivity`
   - Source: v2 l.6512, Babylonian Captivity, "THE PAPACY IS THE MIGHTY HUNTING OF ..."
   - BLOCKING. The audit's editing instruction was published as the locus, and the move it asked for was never made. Set [1] to `the Papacy at Rome -- the pope and the Roman Church` and [3] to `Babylonian Captivity -- 'the papacy is the mighty hunting of the Roman bishop'`.

6. **witt.term.pastor, plain_meaning** (spoken)
   - Old: `Our own catechism openly rebukes lazy pastors.`
   - New: `Our catechism rebukes lazy pastors by name.`
   - Source: LC preface l.51 "many pastors and preachers are very negligent", l.115 and l.200 "lazy paunches". No pastor is named anywhere.
   - BLOCKING. "By name" says the catechism names individual pastors, and the source does not support that. Use `Our catechism rebukes lazy pastors.` The full field then grades FK 6.2 / FRE 65. "Openly" would fail the gate at FRE 59.6. The clause "The people owe him honor and a living" is supported by LC l.1407-1417.

7. **witt.term.christendom, plain_meaning**
   - New: `It took in believers whom Rome had never confirmed.`
   - Source: v1 l.12796-12799, Papacy at Rome: they "do not have their priests and bishops confirmed by Rome".
   - NON-BLOCKING. Rome confirmed bishops, not believers, and "confirmed" also suggests the sacrament. Suggested wording: `It took in peoples whose bishops Rome had never confirmed.` The full field grades FK 5.0 / FRE 76.

8. **witt.term.pope-and-antichrist, plain_meaning**
   - New: `...we spoke courteously of the Church of Rome and claimed our teaching did not differ from it.`
   - Source: the AC Conclusion of Part I, "nothing that varies from ... the Church of Rome as known from its writers".
   - NON-BLOCKING. The fix itself is right: the confession does not name an adversary. But it drops the confession's own limit, "as known from its writers". Suggested wording: `...We claimed our teaching did not differ from that Church as its own writers showed it.`

9. **witt.term.the-turk, plain_meaning / senses.personal / senses.translational**
   - New: `we prayed against him along with the pope`; `named with the pope`
   - Source: Table Talk l.3134, "will pray against the Pope and the Turk as long as I live". That is the founder speaking in the first person, and the record's own locus marks it "Contested as verbatim". The LC pairs the Turk with heathen, Jews and false Christians (l.2960), not with the pope.
   - NON-BLOCKING. Removing the unsourced "devil's instruments" is right. But the pope pairing now rests on one contested table remark, which "we prayed" turns into the community's practice. Suggested wording: `We named the Turk as an outside enemy. Our founder said he would pray against the pope and the Turk as long as he lived. Our household prayer asked that rulers vanquish him. We give no other account of him.` This grades FK 4.2 / FRE 82.

10. **witt.term.christ-alone, senses.personal and senses.translational**
    - New: `we put no saint or scholar in his place`
    - Source: v2 l.16021-16027, That Doctrines of Men: "St. Bernard, St. Gregory, St. Francis and other saints ... He did not say, Hear ye St. Bernard, St. Gregory, etc., but, Hear ye Him".
    - NON-BLOCKING. Moving the line from the uncited Walter remark to this cited passage is a real fix. But "scholar" is not in the passage. Use `no saint` or `no saint or teacher of ours`, or drop the word.

11. **witt.term.the-two-governments, sources[3].locus**
    - Old: `Bondage of the Will (OCR-degraded) -- the other 'two kingdoms,' Christ against Satan`
    - New: `Bondage of the Will -- the other 'two kingdoms,' Christ against Satan`
    - NON-BLOCKING. A reliability disclosure on a quoted phrase is dropped. witt.term.free-will sources[2], which quotes the same file, keeps "(OCR-degraded)". The two should match, and keeping the disclosure is the safer choice.

12. **senses fields over the readability target** (not on the engine's gate for term)
    - calling.personal FK 9.2 / FRE 50; conscience.personal 10.8 / 49; fear-and-love-god.personal 11.7 / 45; prayer.personal 11.5 / 56; sects-and-new-spirits.personal 11.5 / 56 and .translational 17.9 / 35; the-turk.translational 14.0 / 46; justification.translational 21.8 / 26.
    - NON-BLOCKING. Most of these improved on the old text (calling went from 15.0 / 27, conscience from 15.5 / 39). fear-and-love-god.personal (old 11.1 / 50) and the-turk.translational (old 13.3 / 48) got slightly worse. senses.translational reaches participants through the glossary, so the CLAUDE.md target still applies there. Split the longest sentences in a later pass.

Observed but not introduced by this change (pre-existing, outside the changed fields):
- witt.term.the-turk use_note.means still says "one of the devil's instruments", the claim this pass removed from three fields as unsourced.
- witt.term.christendom senses.informational carries the same Nobility/Papacy misattribution that this pass fixed in the loci. The audit noted this.
- witt.term.pope-and-antichrist confidence.divergence_note still frames "the Church of Rome" as the adversary's second name, which the corrected plain_meaning no longer says.
- A few we-voice fields are still in present tense for the community's past: spiritual-temporal-estate "We call this a pure invention", the-turk "We give no other account of him", the-devil quick_meaning "We fight him daily".

## Changes checked and found sound

- **Build vocabulary stripped from loci** in about 130 loci: "cited among this entry's Registry rows (Doc_06 ...)", "read this pass", "read entire this pass", "whole file", "unread", "(layer)", line numbers, and the insurrection note about "this library". In each, the remaining locus still names the right work. The three "per Doc_06 §5 entry N's own Key Sources line" loci (comfort, fear-and-love-god x2, letter-and-spirit, what-does-this-mean) now name the source's own work. The what-does-this-mean "father's staged question" matches LC l.2606. The prayer and catechism Kurze Form loci are true to v2: its Lord's Prayer section exists at l.13027 onward.
- **Locus corrections verified**:
  - christendom swap: "Muscovites ... 'perhaps better Christians than we are'" is v1 l.12795-12818, Papacy at Rome; "to one man" is v2 l.2410, Nobility.
  - promise-and-testament: "only a last irrevocable will of one who is about to die" is v1 l.11102-11103, Treatise on the New Testament. The old wording came from Babylonian Captivity, v2 l.7307.
  - merit: AC l.233-235, verbatim.
  - free-will: 'delight in assertions' is in Cole l.601. The old 'we delight' was a misquote.
  - martyr: the hymn title is verbatim at bacon-allen l.1744-1745.
  - vows: the note is at v3 l.20822-20824, inside the Philadelphia source's own per-work introductions.
  - purgatory: neutral wording.
- **plain_meaning / quick_meaning, source drift and confidence**:
  - assurance: "prayed conditionally" matches TT l.3063.
  - catechism: "Our books told every household" now reads as prescription, matching the record's Documented-as-prescription tag. "singing at work" is supported by SC l.557.
  - household and quick_meaning: prescription framing (aside from finding 1).
  - patience: "our founder was said to remark" properly hedges the table saying, and the quoted words are verbatim (TT l.3014-3015).
  - given-for-you, office, indulgence, justification ("In the same breath" removed), neighbor, obedience (AC XVI limit), sects-and-new-spirits (the unsourced "helped suppress" claim removed from all three fields), spiritual-and-temporal-estate, the-devil, the-mass, we-are-all-priests, confession-and-absolution, prayer (past tense, "honestly" tell removed).
  - gospel: "the true treasure of the Church, set against the pope's treasury of pardons" matches Theses 56 and 62, v1 l.1365 and l.1387.
  - conscience: the G1 build code is replaced with "Justification by faith".
  - grace, scripture-against-tradition, promise-and-testament: coined closers and "not X but Y" tails removed with no new claim.
  - calling: "the pulpit included" is supported by the record's own ministry-as-calling content.
- **Readability**: every changed plain_meaning and quick_meaning passes FK <= 10 and FRE >= 60. The lowest is given-for-you quick_meaning at FK 7.8 / FRE 61. the-turk quick_meaning is too short to grade. Once B1, B2 and B6 are applied they still pass, with grades as given above.
