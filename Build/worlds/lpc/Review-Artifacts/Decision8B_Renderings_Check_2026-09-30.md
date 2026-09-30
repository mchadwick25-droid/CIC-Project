Simulated review — informational only, not an Article 31 substitute.

# lpc Decision 8B: independent check of the 30 new quote renderings and the host sentences

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-opus-5-5
- **Reviewer agent:** separate Decision 8B renderings-check pass (fresh context; read none of the drafting session's reasoning; read only the committed records, the vendored sources and the stage-1 SUMMARY.md)
- **Drafter agent:** Decision 8B extraction session (commit d950380b4: Opus renderings and lens notes; Sonnet host sentences and relations)
- **Round:** 1 (the separate Opus check Decision 8B requires; not a document revision round)
- **Truncation check, method 1:** line count and closing marker: `grep -cE '^\| [0-9]+ \| lpc\.quote\.' ` on this file returns 30 record rows, and `tail -n 1` returns "End of review.", both run after the last edit.
- **Truncation check, method 2:** set comparison in Python: the record ids named in the per-record table equal, as a set, the 30 ids that `git show --name-status d950380b4 -- records/lpc/quote` lists as added; none is missing on either side. Each finding id in the summary list also appears as a `###` finding heading.
- **Scope:** the 30 quote records added in d950380b4; the host-sentence replacements, relations and apparatus deletions in the 24 host records of the same commit (`git diff d950380b4^ d950380b4 -- records/lpc`). Records only; nothing was edited.
- **Standards read:** Record-Native Build Process V2.0 section 6 (Decision 8B; renderings at birth; the fragment rule; the register rule; the source-spoken forms rule); CLAUDE.md (source fidelity, accessible and rigorous); `lpc` Open_Gaps_Tracking entry "Decision 8B extraction for lpc, 2026-09-30".
- **Verdict:** 10 records clear, 20 need a fix. 1 blocking finding (a wrong book and chapter in one quote's locus), 5 substantial findings, the rest optional. The renderings as a set are faithful translations: no clause dropped, no claim added, no fragment. The substantial findings are one softened word ("rescued" for "redeemed"), one phrase whose modern sense misleads ("fell asleep"), one false body sentence, one false lens-note sentence, and the Celerinus "began" defect that the pass documented in the wrong place instead of fixing in the sentence it rewrote.

## Gates and tools run directly

| Check | Result |
|---|---|
| All 22 registered gates (`engine.m1.gates.GATES`) on lpc | 0 findings in every gate except `readability` (61, none on a quote record; host and other fields, the separate readability task named in OG "Decision 8B extraction for lpc, 2026-09-30") |
| `quote-verbatim` | 0 findings |
| `quote-mark-fidelity`, `quote-recording`, `reciprocity`, `referential`, `schema-validation` | 0 findings each |
| `gate_readability_floor` (report-only) | 26 quote renderings score below FK grade 8 (reported, not failed). Not a finding: the renderings follow the source's own sentence breaks, and the fragment rule forbids reopening them to raise the score |
| `python -m engine.m10.cli records lpc` | PASS |
| `engine/m1/sentence_completeness.py` (functions called directly with both parsers; calibration clean) | 3 flags, each read by hand: "All the same, know that..." (imperative, whole); "But why?" (the source's own "But wherefore?", a source-spoken question, stays); "But the space beyond stretched so far..." (parser misread, whole). No fragment in any rendering |
| Independent verbatim re-check (own script: endnotes stripped, tags stripped, letters and digits compared) | All 30 texts found in the vendored file within a few lines of the cited locus. 19 fall inside the stated line range; 11 have their first or last word one or two lines outside it (finding O1). One structural locus is wrong (finding B1) |
| Sentence length (renderings) | Two sentences past 25 words: grace-sufficient (24 words inside a lead-in of 4, acceptable) and no-donatist (27, finding O2) |

Note: the working tree carries another session's uncommitted edits to 12 non-quote lpc records (ambient, contested_claim, figure). The gates above ran on that tree. None of those files is a quote record, and the host checks below were read from the commit diff, not the working tree.

## Findings summary

| Id | Record | Severity |
|---|---|---|
| B1 | lpc.quote.custom-handed-down-from-the-apostles | blocking |
| S1 | lpc.quote.christ-in-our-captive-brethren | substantial |
| S2 | lpc.quote.slept-with-his-fathers | substantial |
| S3 | lpc.quote.celerinus-tribulation-and-sister + lpc.story.celerinus-writes-to-lucian | substantial |
| S4 | lpc.quote.judgment-of-god-and-favour-of-people | substantial |
| S5 | lpc.quote.weeping-in-hymns-and-canticles | substantial |
| O1 | 11 records (locus line ranges) | optional |
| O2 | lpc.quote.no-donatist-bishop-in-the-succession | optional |
| O3 | lpc.quote.no-donatist-bishop-in-the-succession | optional |
| O4 | lpc.quote.lucian-already-weary | optional |
| O5 | lpc.quote.thirteen-letters-transmitted | optional |
| O6 | lpc.quote.to-answer-to-our-birth | optional |
| O7 | lpc.quote.wealthy-and-rich-matron | optional |
| O8 | lpc.quote.lucian-hunger-thirst-brightness | optional |
| O9 | lpc.quote.not-cruelty-but-righteous-retribution | optional |
| O10 | lpc.quote.grant-me-chastity-but-not-yet | optional |
| O11 | lpc.quote.judgment-of-god-and-favour-of-people | optional |
| H1 | lpc.witness.baptism-traced-to-the-apostles (host locus, outside 8B scope) | substantial (flag only) |
| H2 | lpc.story.election-of-cyprian | optional |
| H3 | lpc.force.congregational-acclamation-overriding-preference | optional |
| H4 | lpc.witness.apostolic-succession-of-bishops | optional |
| H5 | lpc.story.celerinus-writes-to-lucian (Lucian sentence) | optional |
| H6 | lpc.story.the-psalms-on-the-wall | optional |
| H7 | lpc.force.augustine-engagement-cyprian-conciliar-acts | optional |

## Per-record table

Columns: R = modern_rendering read clause by clause against `text`; L = modern_lens_note; V = verbatim text, speaker and locus against `cic/texts`; W = retrieve_when. "ok" means checked and nothing wrong.

| # | Record | R | L | V | W | Verdict | Severity |
|---|---|---|---|---|---|---|---|
| 1 | lpc.quote.all-our-power-is-of-god | ok | ok | text and speaker ok (Ep. I §4); lines 28426-28429, not 28425-28428 | ok | fix | optional (O1) |
| 2 | lpc.quote.celerinus-tribulation-and-sister | ok ("God only knows" rendered to its sense, "Only God knows it") | ok | ok (Ep. XX §2; Celerinus) | ok | fix | substantial (S3) |
| 3 | lpc.quote.christ-in-our-captive-brethren | "redeemed" softened to "rescued" | ok | ok (Ep. LIX §2; Gal 3:27 endnote) | ok | fix | substantial (S1) |
| 4 | lpc.quote.custom-handed-down-from-the-apostles | ok | ok | text ok at line 12167; structure marker wrong: Book IV, Chapter 6, §9, not Book II, Chapter 7, §10 | ok | fix | blocking (B1) |
| 5 | lpc.quote.grace-sufficient-heard-for-salvation | ok ("heard" rendered "answered", the right modern sense) | ok | ok (Homily VI §6) | ok | clear | — |
| 6 | lpc.quote.grant-me-chastity-but-not-yet | ok ("hear me" rendered "answer me") | ok | text ok (Conf. VIII.vii.17); lines 12744-12750, not 12745-12749 | first line a stretch | fix | optional (O1, O10) |
| 7 | lpc.quote.grief-of-mind-and-tears | ok | ok | text ok (Ep. LIX §1); lines 36009-36012, not 36008-36010 | ok | fix | optional (O1) |
| 8 | lpc.quote.infant-baptism-apostolical-authority | ok | ok | ok (On Baptism IV.24.32) | ok | clear | — |
| 9 | lpc.quote.judging-no-man-from-communion | ok | ok | text ok (Council of 256, preface); lines 56868-56871, not 56869-56871 | ok | fix | optional (O1) |
| 10 | lpc.quote.judgment-of-god-and-favour-of-people | ok | one interpretive clause | text ok (Pontius §5); lines 27817-27825, not 27817-27824; body sentence false | ok | fix | substantial (S4); optional (O1, O11) |
| 11 | lpc.quote.later-councils-correct-earlier | ok ("charity" to "love" and "experiment" to "experience" are the right modern senses; rhetorical question stated as assertions, faithful) | ok | ok (On Baptism II.3.4); body honest about the mid-question start | ok | clear | — |
| 12 | lpc.quote.letter-sent-back-altered | ok | ok | text ok (Ep. III §2); lines 28926-28935, not 28927-28934 | ok | fix | optional (O1) |
| 13 | lpc.quote.lucian-already-weary | awkward "too" placement | ok | ok (Ep. XXI §3; Lucian) | ok | fix | optional (O4) |
| 14 | lpc.quote.lucian-hunger-thirst-brightness | ok ("That was when..." gives the mid-sentence opening a subject and verb) | ok | ok (Ep. XXI §2; endnote at "so intolerable" correctly noted); body silent on the mid-sentence start | ok | fix | optional (O8) |
| 15 | lpc.quote.no-donatist-bishop-in-the-succession | opening sentence 27 words; "is what counts" slightly hardens "is to be taken into account" | ok | ok (Letter LIII §2, A.D. 400); the 33 elided names (Evaristus to Damasus) counted against the source, 37 in all from Linus to Siricius; body exact | ok | fix | optional (O2, O3) |
| 16 | lpc.quote.not-cruelty-but-righteous-retribution | ok | ok | ok (Reply to Faustus XXII.74); body silent on the elided "if" clause | ok | fix | optional (O9) |
| 17 | lpc.quote.numidicus-left-for-dead | ok | ok (restates the host's own modern_contrast) | ok (Ep. XXXIV; endnote 'Otherwise, "unconquered."' verified at "unwillingly"; divergence_note honest) | ok | clear | — |
| 18 | lpc.quote.penitential-psalms-and-seclusion | ok | ok | ok (Vita XXXI, lines 4924-4935; printed "them ;" kept) | ok | clear | — |
| 19 | lpc.quote.plague-and-the-city | ok ("demanded the pity of the passers-by for themselves" read correctly as the dead asking pity) | ok | text ok (Pontius §9); lines 27939-27949, not 27939-27948 | ok | fix | optional (O1) |
| 20 | lpc.quote.restless-till-they-find-rest | ok | ok | ok (Conf. I.i.1) | ok | clear | — |
| 21 | lpc.quote.slept-with-his-fathers | "fell asleep with his ancestors" misleads | ok | ok (starts at "with sight and hearing unimpaired", page 143, lines 4979-4981; "With all the members of his body intact" confirmed at line 4938, page 141; body honest) | ok | fix | substantial (S2) |
| 22 | lpc.quote.sum-sent-fruitful-fields | ok | ok | ok (Ep. LIX §3; endnote "The text (sestertia) dubious. Ed. Paris." verified) | ok | clear | — |
| 23 | lpc.quote.thirteen-letters-transmitted | last sentence's "They" is unclear | ok | text ok (Ep. XIV §2); lines 30188-30195, not 30187-30194 | ok | fix | optional (O1, O5) |
| 24 | lpc.quote.thousands-of-certificates-daily | ok | ok (two kinds of certificate, correctly named) | text ok (Ep. XIV §2); lines 30198-30207, not 30199-30206 | ok | fix | optional (O1) |
| 25 | lpc.quote.to-all-men-not-the-household-of-faith | ok | ok | ok (Pontius §10) | ok | clear | — |
| 26 | lpc.quote.to-answer-to-our-birth | ok ("degenerate" rendered "unworthy of their birth", the right sense); "admonishes" rendered "warns" | ok | ok (Pontius §9; speaker Pontius as reporter, body says so); text drops the source's closing quotation mark | ok | fix | optional (O6) |
| 27 | lpc.quote.trees-eyes-and-executioner | ok (the Zacchaeus parenthesis is not inverted) | ok | ok (Pontius §18) | ok | clear | — |
| 28 | lpc.quote.water-extinguishes-fire-almsgiving-sin | ok ("almsgiving" to "giving to the poor"; "sanctification" to "His making us holy") | ok | ok (On Works and Alms §2; Prov 16:6 and Ecclus 3:30 endnotes) | ok | clear | — |
| 29 | lpc.quote.wealthy-and-rich-matron | ok ("matron" to "married woman" is right); "collyrium" to "eye paint" is a judgement call | ok | text ok (§14; endnote on "in Christ's Church" verified); lines 47709-47717, not 47709-47716 | ok | fix | optional (O1, O7) |
| 30 | lpc.quote.weeping-in-hymns-and-canticles | ok | "the one first-person line" is false | text ok (Conf. IX.vi.14); lines 13731-13733, not 13731-13732 | ok | fix | substantial (S5); optional (O1) |

## Findings on the quote records

### B1 custom-handed-down-from-the-apostles: the structure marker points to the wrong book and chapter

The text is at line 12167, as cited. That line sits inside `<div3 ... title="Book IV">` (opened at line 11995) and `<div4 ... n="6">` (opened at line 12150, "Chapter 6.—9."). Chapter 7 opens at line 12173, after the quote. Book II, Chapter 7, §10 (line 11394) is a different passage ("Wherefore, then, have ye severed yourselves?"). A reader who follows the locus does not find the quote. Blocking, because the locus is the quote's address and the record claims citation_specificity A.

Proposed `sources[0].locus`: `On Baptism, Against the Donatists, Book IV, Chapter 6, section 9; cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, line 12167`

The host `lpc.witness.baptism-traced-to-the-apostles` carries the same wrong marker in its own `sources[].locus` ("Book II, Chapter 7, SS10"). See H1.

### S1 christ-in-our-captive-brethren: "redeemed" softened to "rescued"

The letter is about paying a ransom. "Redeem" survives plainly in modern English and keeps the buy-back sense on both sides of Cyprian's parallel. "Rescued" drops the payment, which is the point of the letter. The host sentence in `lpc.story.hundred-thousand-sesterces` already keeps "redeemed".

Proposed `modern_rendering`: `For, as the Apostle Paul says, "All of you who were baptized into Christ have clothed yourselves with Christ." So we must see Christ in our captive brothers. And He who ransomed us from the danger of death must be ransomed from the danger of captivity...`

("redeemed ... redeemed" is equally acceptable.)

### S2 slept-with-his-fathers: "fell asleep with his ancestors" misleads

The rendering never says Augustine died. At a bedside where people are "watching and praying", a listener can hear "he fell asleep" as a doze. The lens note already gives the modern sense ("Scripture's way of saying that a man died and joined those who went before him"). The rendering should carry that sense.

Proposed `modern_rendering`: `His sight and hearing were unimpaired. While we stood by, watching and praying, "he died and joined his ancestors," as it is written, "well nourished, at a good old age."`

### S3 celerinus-tribulation-and-sister: the "began" defect is recorded in the wrong place and left unfixed

The host `lpc.story.celerinus-writes-to-lucian` says Celerinus "began" with these words. Verified: they open §2 of Epistle XX, after a greeting paragraph. The pass rewrote exactly that sentence and kept the false "began". It then recorded the host's error in the quote record's `confidence.divergence_note`. That field is for this quote's own divergence from its source; this quote has none. A note about another record's error is tracking material, not record content. The fix belongs in the sentence Decision 8B already allows the pass to change.

Proposed host sentence (`lpc.story.celerinus-writes-to-lucian` `text`): `He told Lucian that he was in the midst of a great tribulation, and the tribulation was not his own captivity.`

Proposed quote record: `divergence_note: null`. Log the correction in OG "Decision 8B extraction for lpc, 2026-09-30".

### S4 judgment-of-god-and-favour-of-people: a false body sentence

The body says "The second sentence runs on past the span held here; the span ends at the end of its main clause." Verified at line 27825: Pontius's sentence ends at "the priesthood that was coming upon him." and the next sentence opens "Moreover, I will not pass over...". The span holds the whole sentence.

Proposed body: `Pontius, Cyprian's deacon, writes in praise of his bishop. That Cyprian was a neophyte when elected rests on Pontius alone.`

### S5 weeping-in-hymns-and-canticles: the lens note's "one first-person line" is false

The passage goes on in the first person past this sentence ("The voices flowed into mine ears, and the truth was poured forth into my heart ... my tears ran over"). It is one account, not one line.

Proposed `modern_lens_note`: `A modern listener may expect a detailed account of what baptism felt like. This passage is the one first-person account we have, written years later by a man who was by then a bishop.`

### O1 eleven loci: line ranges miss a first or last line

Each quote verifies, but its first or last word sits one or two lines outside the stated range. Mechanical fix, suited to a Haiku pass.

| Record | Stated | Correct |
|---|---|---|
| all-our-power-is-of-god | 28425-28428 | 28426-28429 |
| grant-me-chastity-but-not-yet | 12745-12749 | 12744-12750 |
| grief-of-mind-and-tears | 36008-36010 | 36009-36012 |
| judging-no-man-from-communion | 56869-56871 | 56868-56871 |
| judgment-of-god-and-favour-of-people | 27817-27824 | 27817-27825 |
| letter-sent-back-altered | 28927-28934 | 28926-28935 |
| plague-and-the-city | 27939-27948 | 27939-27949 |
| thirteen-letters-transmitted | 30187-30194 | 30188-30195 |
| thousands-of-certificates-daily | 30199-30206 | 30198-30207 |
| wealthy-and-rich-matron | 47709-47716 | 47709-47717 |
| weeping-in-hymns-and-canticles | 13731-13732 | 13731-13733 |

### O2 no-donatist-bishop-in-the-succession: opening sentence at 27 words

"If the lineal succession of bishops is to be taken into account" is a concession. "Is what counts" makes it the deciding test. Splitting fixes both points.

Proposed opening, replacing the first sentence: `Suppose the line of bishops is to be taken into account. Then how much more surely, and how much more to the Church's good, we count back to Peter himself!`

### O3 no-donatist-bishop-in-the-succession: the spoken ellipsis

The record is honest. The text marks the elision, the body names the 33 omitted names, and the rendering follows the text. Spoken aloud, though, "Clement, Anacletus, ... and Siricius" can sound like three successors. This is the project lead's call already open in OG "Decision 8B extraction for lpc, 2026-09-30" (full list plus a readability waiver, or the elision). No wording change is proposed while that call is open.

### O4 lucian-already-weary: "too" at the end of a long clause

Proposed second sentence: `We also greet all those whose names I have not written, because I am already worn out.`

### O5 thirteen-letters-transmitted: "They worked" has no clear subject

Proposed, replacing the last two sentences: `With the Lord's help, my poor abilities gave all of it as fully as they could, by the law of faith and the fear of God.`

### O6 to-answer-to-our-birth: "warns" for "admonishes"; closing quotation mark

"Admonishes and exhorts" are two words for urging. "Warns" adds a threat. Proposed: `as the Lord counsels and urges`. The source closes Cyprian's direct speech with a quotation mark after "goodness." (line 27975). The record `text` drops it, so the text opens a quotation it never closes. Proposed: end `text` with `His goodness."`

### O7 wealthy-and-rich-matron: "collyrium" as "eye paint"

The English says "the collyrium of the devil" against "Christ's eye-salve". A collyrium is an eye ointment. "Eye paint" turns it into a cosmetic. That may match Cyprian's Latin, which is not vendored and was not checked. If the Latin was not checked, follow the English: `Do it not with the devil's eye ointment, but with Christ's eye-salve.` The lens note's "eye paint" would change to match.

### O8 lucian-hunger-thirst-brightness: body silent on the mid-sentence start

The other two mid-sentence records say so in their bodies. Proposed addition to the body: `The quotation begins mid-sentence. The words run on from 'as what we in all cases decreed', so the rendering's opening 'That' is the confessors' decision to give peace to all.`

### O9 not-cruelty-but-righteous-retribution: body silent on the elided condition

The span is the main clause of a sentence that opens "Now, if this explanation suffices to satisfy human obstinacy...". The rendering states it without the condition, which is faithful to the span. Proposed addition to the body: `The quotation begins at the main clause of a sentence that opens 'Now, if this explanation suffices'.`

### O10 grant-me-chastity-but-not-yet: first retrieve_when line

This prayer is about delaying chastity, not about wanting to believe. The line was copied from the host, which makes that bridge itself. Proposed first line: `participant describes putting off a change they know they should make, or being persuaded yet still unable to act on it`

### O11 judgment-of-god-and-favour-of-people: one interpretive clause in the lens note

"For him the people's favour was how God's choice became visible" goes a step past the quote. The host story makes that reading, but the quote only names the two side by side. Proposed: `A modern listener may hear 'the favour of the people' as a popular vote. Pontius names it together with the judgment of God, as one event, not as a count of votes.`

## Special cases

| Case | Check | Result |
|---|---|---|
| no-donatist (33 of 37 names elided) | The source list counted name by name, lines 29696-29710. Linus, Clement, Anacletus, 33 names from Evaristus to Damasus, then Siricius: 37. The body is exact, the ellipsis is marked, and the rendering keeps the ellipsis and every clause. | honest and faithful; O2, O3 optional |
| later-councils (starts inside a rhetorical question) | The source question opens "But who can fail to be aware that the sacred canon..." (line 11300). The body names this. The rendering states the "that" clauses as assertions, which is what a rhetorical question of this kind asserts. Nothing added. | clear |
| lucian-hunger (opening sentence) | "That was when we were in this distress." has its own subject and verb, and finishes a clause the source runs on from "decreed". | clear; O8 optional |
| celerinus (divergence_note on "he began") | The fact is verified, but it is in the wrong field and the host is not corrected. | S3 |
| numidicus ("unconquered" endnote) | Endnote verified at "unwillingly". The divergence_note and body are accurate. The rendering follows the main text ("against his will"). | clear |
| Possidius ch. XXXI (starts at "with sight and hearing unimpaired") | Verified as one continuous segment on page 143 (lines 4979-4981). The opening clause is confirmed at line 4938 on page 141, before the facing Latin page 142. The body is accurate. | verbatim clear; rendering S2 |

## Host records (24)

Each changed sentence was read against the quote it replaces. Apparatus changes were checked for deletion only. The 7 figure records gained `relations[]` back-links only, and those are correct.

| Host record | Replacement sentences | Apparatus | Verdict |
|---|---|---|---|
| lpc.contested.cyprian-death-genre | (not a quotation; unchanged) | body paragraph deleted, deletion only | clear |
| lpc.witness.almsgiving-quenches-sin | faithful; all facts kept | none | clear |
| lpc.witness.apostolic-succession-of-bishops | `text` adds "anywhere" | none | fix, optional (H4) |
| lpc.witness.baptism-traced-to-the-apostles | faithful; 24-word sentence is within the bound | none | clear (H1 is outside 8B scope) |
| lpc.witness.grant-me-chastity-but-not-yet | faithful | none | clear |
| lpc.witness.heard-for-salvation-not-for-wish | faithful | none | clear |
| lpc.witness.restless-heart-and-the-unrepentant-enemy | faithful | none | clear |
| lpc.witness.violence-commanded-not-cruel | faithful | none | clear |
| lpc.figure.augustine / celerinus / cyprian / lucian / numidicus / pontius / possidius (7) | relations only | none | clear |
| lpc.force.augustine-engagement-cyprian-conciliar-acts | faithful; unattributed | trailer deleted, deletion only | fix, optional (H7) |
| lpc.force.confessors-claim-to-grant-peace | faithful | trailer deleted | clear |
| lpc.force.congregational-acclamation-overriding-preference | 28 words | trailer deleted | fix, optional (H3) |
| lpc.force.decian-persecution-libelli-system | faithful | trailer deleted | clear |
| lpc.force.transmission-institutionally-dominant-side | faithful; 25 words | trailer deleted | clear |
| lpc.gravity.collegial-communion-preserved | faithful | trailer deleted | clear |
| lpc.gravity.grace-and-human-incapacity | faithful ("says it twice for emphasis" matches "I say, of God") | trailer deleted | clear |
| lpc.limit.ordinary-interior-life | faithful | two body sentences deleted, deletion only (the "No relations[] edge" sentence was stale once the edge was added) | clear |
| lpc.story.celerinus-writes-to-lucian | "began" kept (S3); "asking them to pardon him" softens "they must pardon me" (H5) | locus clause deleted, deletion only | fix, substantial (S3) |
| lpc.story.election-of-cyprian | faithful; one sentence at 29 words | trailer deleted | fix, optional (H2) |
| lpc.story.hundred-thousand-sesterces | faithful | trailer sentence deleted | clear |
| lpc.story.numidicus | faithful ("preserved" correction kept as its own sentence) | trailer deleted | clear |
| lpc.story.the-death-of-cyprian | faithful (Zacchaeus not inverted) | trailer sentence deleted | clear |
| lpc.story.the-plague-and-the-enemies | faithful; 26-word sentence is within the bound | trailer deleted | clear |
| lpc.story.the-psalms-on-the-wall | faithful; "fell asleep" put as "the words of Scripture" | trailer deleted | fix, optional (H6) |
| lpc.core.latin-pastoral-congregational-christianity | faithful | ", read in full" deleted from a locus, deletion only | clear |

### H1 baptism-traced-to-the-apostles: the host locus carries the same wrong marker as B1

`sources[].locus` reads "Book II, Chapter 7, SS10" for the passage at lines 12163-12169, which is Book IV, Chapter 6, §9. This field is not a sentence that held a quote, so it is outside Decision 8B's edit scope. Flagged for the record's owner: `Book IV, Chapter 6, SS9`.

### H2 election-of-cyprian: 29-word sentence

Proposed: `Pontius did not soften this; he pressed it. Cyprian, he noted, was still in the early days of his faith, at an untaught stage of his spiritual life.`

### H3 congregational-acclamation: 28-word sentence

Proposed: `By the judgment of God and the favour of the people, he wrote, Cyprian was chosen for the priesthood and the rank of bishop. He was still newly baptised.`

### H4 apostolic-succession `text`: "anywhere" hardens the source

Proposed: `Then they added that no Donatist bishop is found in this line of succession.`

### H5 celerinus story, Lucian's sign-off: "asking" softens "must"

Proposed: `He signed off exhausted, greeting others whose names he had not written because he was already weary, and saying they must pardon him.`

### H6 psalms-on-the-wall: "the words of Scripture" then altered words

The preceding sentence already says "while he died", so Scripture's own verb does not mislead here. Proposed: `Possidius put it in the words of Scripture: he slept with his fathers, well nourished in a good old age.`

### H7 augustine-engagement force: the principle is stated unattributed and drops "the earlier"

Proposed: `Even among full councils of the whole church, he wrote, the earlier ones are often put right by those that come after.`

## Checks with no finding

- Speakers: Celerinus (Ep. XX), Lucian (Ep. XXI), Pontius (Life §§5, 9, 10, 18, including as reporter of Cyprian's address), Possidius (Vita XXXI), and Augustine for the joint Letter LIII (the body names Fortunatus and Alypius) are all right against the vendored headings.
- Every retrieve_when line other than O10 is true of its quote.
- No rendering adds a claim, drops a clause, or leaves a fragment. The register calls checked are right: "charity" to "love", "heard" to "answered", "degenerate" to "unworthy of their birth", "matron" to "married woman", "almsgiving" to "giving to the poor", "experiment" to "experience", "aliens" to "strangers".
- Every apparatus change in the 24 hosts is a deletion only. No wording was added outside the replacement sentences and `relations[]`.

End of review.
