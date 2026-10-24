# lpc sermon quote batch 1: review, round 1

- Reviewer: Opus 5.5 (`claude-opus-5-5`), independent reviewer. I did not draft or render any of these records.
- Date: 2026-10-24
- Subject: 12 new `lpc.quote.*` records on branch `claude/lpc-sermon-batch1-2026-10-24`, commit `b01ea289`. Also reviewed: the four gravity records' new relations, and the generator changes in `Build/worlds/lpc/scripts/wb_lpc_s24.py`, `wb_lpc_s25.py` and `wb_lpc_s2y_canon_cells.py`.
- Sources checked: English at `cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml`. Latin at `cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt` (PL 38, OCR).
- Severity scale: P0 and P1 block. P2 does not block; it is a recommended correction with exact text.

## Method

1. **Quote text, two independent methods.** (A) Python: read each record's `text` with a YAML parser, read the cited file lines, strip tags, fold whitespace, and test for a substring match. (B) `sed` tag strip, `tr` whitespace fold, and a `grep -F` fixed-string match against the record text. Both methods gave the same result.
2. **Latin.** I printed every cited PL 38 range with two lines of margin on each side. I checked each range's first and last line against the start and end of the Latin that matches the passage.
3. **Renderings.** I compared each `modern_rendering` clause by clause with the NPNF English and the PL 38 Latin. I also measured sentence lengths.
4. **Context claims.** I checked every line-number and context claim in the claim guards and body text against the file: the notes, the Isaiah sentence, the "not repeated" sentence, the Cyprian mentions, the sermon headings and the household illustration.
5. **Graph and canon.** I confirmed that every `prefer_instead` target exists. I read the canon-cell questions in `wb_lpc_s2y_canon_cells.py` and `engine/canon/seed_appendix_a.py`. I diffed the four gravity records against `origin/main`.
6. **Gates.** Run in a detached scratch worktree at `b01ea289`, never in the main tree: `python -m engine.m10.cli records lpc` and `python -m engine.m10.cli regate lpc`.

## Results that hold for the whole batch

- **Quote text: all 12 pass.** Every `text` field matches the file word for word at its stated NPNF lines under both methods. Each passage starts on the first cited line and ends on the last one.
- **NPNF loci: all 12 resolve.** The note-line claims also hold: 20610/20613, 20847 (the Carthage-conference note), 15141, 13011, 19723-19725, 12932 ("the washing of the flesh is not repeated in their case") and 15205 ("according to each one's grade and condition"). Cyprian is named in running text only at 20827 and 20848, as the records say. NPNF 79 is headed "Against the Donatists", which supports the Donatist framing in record 12.
- **PL 38 loci: every start line is right, but six end lines are short.** See finding B-1.
- **Rendering length:** every sentence is 20 words or fewer. The longest are 20 words (record 7) and 19 words (records 6 and 11).
- **Gravity records:** the diff adds only three `associated-with` relations to each of the four records, pointing to the three new quotes for that gravity. Nothing else in them changed. The `wb_lpc_s25.py` change matches: the quotes go into `OTHER_TYPE_EDGES_LAST`, and the docstring's "NOT DONE HERE" list no longer bars gravity-to-quote edges.
- **Canon cells:** each quote's cell matches its gravity record's cell, and each passage answers its cell's question. F3-I asks "Who held authority among you, and how did anyone come to have it?" F4-I asks "when someone wronged the community, how was it handled, and could they come back?" F3-T asks "Was your church 'Catholic'?" and about handling other communities. F6-I asks what your people never settled.
- **`prefer_instead` targets:** all seven exist in `records/lpc/`.
- **Gates:** `records lpc: PASS`. `regate lpc: PASS`. Regate checked 12 new or edited fields; it reports 11 edited fields below FK 8, which it notes but does not fail. The other notes are base failures that this branch did not change. The worktree was clean after both runs.

## Batch-level finding

### B-1 (P1): six PL 38 loci stop before the Latin passage ends

In six records the cited Latin range ends one or more lines before the passage does. Usually a hyphenated last word runs onto the next line; in record 6 a page break falls inside the sentence. A reader who checks the cited lines will not find the end of the passage. These records are marked `verified-direct`, so the locus has to cover the whole passage. The same wrong ranges appear in two places in each record, the `sources[].locus` field and the body text, and both come from `wb_lpc_s24.py`. The ranges were copied from `sermon_batch1_renderings.md`, so that working file has the same error.

| Record | Cited | Where the Latin actually ends | Correct range |
|---|---|---|---|
| `bind-him-justly` | 35544-35548 | 35549, "in coelo." | **35544-35549** |
| `reprove-and-forgive-the-surgeons-knife` | 36195-36200 | 36201, "mentum ?" (*ferramentum*) | **36195-36201** |
| `peter-the-sick-man-and-the-physician` | 52934-52943 | 52947, "gationem timoris." (52942-52945 are blank lines and the page number "7K6"; 52946 is "sed ut trina confessione amoris, deleret trinam ne-") | **52934-52947** |
| `going-out-without-violating-unity` | 38536-38540 | 38542, "plinam ; existi inde." | **38536-38542** |
| `pardon-through-a-wicked-clergyman` | 32485-32491 | 32492, "rum." (*peccatorum*) | **32485-32492** |
| `consider-who-was-there` | 50696-50700 | 50701, "quis ibi fuit." | **50696-50701** |

**Fix:** in `wb_lpc_s24.py`, change each range in both its locus string and its body string, then regenerate. Lines 1651/1669, 1703/1718, 1753/1768, 1895/1916, 2015/2035 and 2066/2085 hold the old ranges. The other six ranges are right: 53418-53424, 42457-42464, 42699-42703, 53554-53561, 38364-38370 and 32254-32262.

### B-2 (P2): single-line NPNF loci say "lines"

The `locus` fields for records 4, 5, 7, 9 and 12 say "lines 14225", "lines 14444", "lines 20848", "lines 15208" and "lines 19722". Their bodies correctly say "line". **Fix:** use "line N" in the locus whenever the range is one line.

## Per-record findings

### 1. `lpc.quote.ye-belong-to-my-care` (F3-I, tier 1)

- Text, NPNF locus and PL locus (53418-53424) are verified. *Communicatis membris Apostolorum, communicatis memoriis sanctorum martyrum, diffusorum per orbem terrarum, et pertinetis ad curam nostram...* matches.
- The Latin-based corrections are right. *Memoriis* means martyrs' shrines; in African Latin of this period *memoria* is the usual word for a martyr's memorial. "Care" for *curam* is also right. The divergence note is accurate, and the body records the bishop's plural.
- The claim guards hold. The omitted "Catholic people" sentence is guarded so it cannot be supplied as if quoted. The prayer is correctly guarded as Augustine's own words.
- The `retrieve_when` triggers match the passage, and the canon cell fits.
- **R1-1 (P2):** in the rendering, "spread over the whole world" now seems to describe the shrines. In the Latin, *diffusorum* is genitive plural and agrees with *martyrum*, and NPNF has "who are spread". **Proposed:** "You share communion with the shrines of the holy martyrs, who are spread over the whole world."

### 2. `lpc.quote.stewards-and-future-bishops` (F3-I)

- Text and both loci are verified. Every clause of the rendering is present: the stewards, the "I too was once where you are", the higher and lower place, "a few years ago", "bishop to lay people", and the future bishops. Nothing is added.
- The claim guards hold: no date or manner of ordination may be drawn from the passage, and no ordination rite is shown. The lens note's gloss of *dispensatores* is accurate.
- `retrieve_when`, canon cell and the null divergence note are all right. "Stewards" is a modernization of the word, explained in the lens note; it is not a Latin correction.
- No findings.

### 3. `lpc.quote.good-works-the-comfort-of-our-dangers` (F3-I)

- Text and both loci are verified. "Good way of life" for *bonis moribus* is the right Latin-based correction; the modern sense of "conversation" would mislead.
- **R3-1 (P2), rendering logic:** the relative clause (*qui sperni nolumus a vobis*) now stands as its own first sentence, so the next sentence's "But" reads as a contrast with it: "We do not want you to look down on us. But why do we speak to you...". The Latin *autem* only links back to the previous verse ("he that despiseth you"). It sets up no contrast. **Proposed:** "We do not want you to look down on us. Why do we speak to you, except to take joy in your good way of life? Let your good works comfort us in our dangers. Live well, so that you do not die badly."
- **R3-2 (P2), divergence note:** the note says the rendering follows the Latin "where the English misleads" and lists "despised" for *sperni*. "Despised" does not mislead; the change to "look down on" is a plain-English choice. **Proposed divergence_note:** "The text field is the NPNF English as printed. modern_rendering follows the Latin of PL 38 where the English misleads: 'good conversation' renders bonis moribus, a good way of life. 'Despised' (sperni) is rendered 'look down on' for plainness."
- The claim guards hold: no gloss is added on the dangers, and the earlier sentences are not supplied. `retrieve_when` and canon cell fit.

### 4. `lpc.quote.bind-him-justly` (F4-I)

- Text and NPNF locus are verified. PL locus: see B-1 (35544-35549).
- The rendering carries every clause. "Tax collector" for *publicanum* and "made peace with" for *concordaveris* are right. The divergence note's point about the quotation marks is accurate: the Latin is not the *reconciliari* of Matt. 5:24. "Him" after "corrected" is understood in the Latin, as the rendering file says.
- The claim guards hold. They exclude formal penance, excommunication and a bishop readmitting a penitent, and they require the Matt. 18:15-17 steps. Lines 14218-14219 do quote Matt. 18:16-17.
- `retrieve_when` and canon cell fit.

### 5. `lpc.quote.reprove-and-forgive-the-surgeons-knife` (F4-I)

- Text and NPNF locus are verified. PL locus: see B-1 (36195-36201).
- The Latin-based corrections are right. *Culpam de corde abjiciamus* asks that the fault be cast out of the heart, not forgotten, so "remembrance" is NPNF's interpretation. *Si per charitatem* is conditional and means love. The divergence note is accurate.
- **R5-1 (P2), rendering logic:** *Ideo ... subdidit ... ut ... non recedat* is a purpose clause: the Lord added "from your hearts" *so that* gentleness would not leave the heart. In the rendering, "That is why the Lord added" points back to the sentence before, and the purpose becomes a separate rule. **Proposed:** "The Lord added “from your hearts” for this reason: when discipline is given out of love, gentleness must not leave the heart."
- **R5-2 (P2), unsupported detail in the lens note:** "unruly boys and the head of the house" adds a figure the text does not have. The Latin is *pueri indisciplinati ... quando volumus dare disciplinam*: unruly boys, and "we" who want to discipline them. Nothing names a household head; *pueri* can also mean young servants. **Proposed modern_lens_note:** "A modern listener may hear 'scourges' as a church penalty. In the sermon they belong to an illustration about unruly boys who beg to be let off a beating, which Augustine then applies to brethren. His point is that correction is to be given out of love, with the sin forgiven in the heart, as a surgeon cuts out of kindness." **Proposed first claim guard:** "The blows belong to an illustration about unruly boys and must not be read as a church penalty." The selection and rendering notes also say "household". This change is only to the record.
- **R5-3 (P2), claim guard alignment:** the second guard says only that the passage does not show how discipline was carried out in the church. To match records 4 and 6, **proposed:** "The passage does not describe formal public penance, excommunication or how discipline was carried out in the church, and must not be used as evidence of any of them."
- `retrieve_when` and canon cell fit. Augustine does apply the illustration to "our brethren" just after the passage (NPNF line 14445 onward).

### 6. `lpc.quote.peter-the-sick-man-and-the-physician` (F4-I)

- Text and NPNF locus are verified. PL locus: see B-1. The cited range ends at *Christi*, and the Latin for "efface the threefold denial of fear" falls outside it. This is the most serious of the six short ranges.
- The rendering carries every clause, and the Lucan reference is correctly left out. "Sick man" for *infirmus* is right.
- **R6-1 (P2):** "not as the sick man assumed" weakens *praesumpsit*, which says Peter was overconfident; NPNF has "presumed". "Presumed" is still plain modern English. **Proposed:** "And it happened as the doctor foretold, not as the sick man presumed."
- The claim guards hold. Peter's restoration to feed the flock is correctly kept out; it comes in section 4, "Quid a Petro exigitur", at PL 38 line 52949. No penitential rite is shown.
- `retrieve_when` and canon cell fit. The fit is loose, but the cell's question ("could they come back?") covers it.

### 7. `lpc.quote.one-good-shepherd-not-many` (F3-T)

- Text, NPNF locus and PL locus (53554-53561) are verified. "Blessed Cyprian" matches *beatusque Cyprianus*.
- The rendering carries every clause. "The same holds for" turns the list attached to the double negative into its own sentence and adds no claim.
- The claim guards hold. There is no rebaptism, no dispute between bishops, and no claim that Augustine and Cyprian agreed or differed. The guard requires John 10:14, which follows at line 53561.
- `retrieve_when` and canon cell fit. No findings beyond B-2.

### 8. `lpc.quote.apart-in-heart-united-in-body` (F3-T)

- Text, NPNF locus and PL locus (38364-38370) are verified. Every clause is present, and "your care" for *ad curam vestram* is right.
- The claim guards hold: the hearers are lay people, no bishop-to-bishop dispute is shown, and the threshing-floor sentence is not supplied.
- `retrieve_when` and canon cell fit. No findings.

### 9. `lpc.quote.going-out-without-violating-unity` (F3-T)

- Text and NPNF locus are verified. PL locus: see B-1 (38536-38542).
- The rendering carries every clause. The "If" makes the condition explicit; the Latin has the same structure. "Fitting discipline ... that does not break unity" is right.
- **Rank guard: holds.** The guard ties the discipline to "each one's grade and condition" and cites NPNF line 15205. That line has the phrase, and the Latin (*pro uniuscujusque gradu atque persona*, PL 38 lines 38535-38536) supports it. The guard says plainly that the passage does not give every hearer the same power to discipline.
- The Isaiah and Donatist context is guarded, and no bishop-to-bishop dispute is shown.
- **R9-1 (P2), body accuracy:** "The sentence before the passage, at lines 15204-15207" is really several sentences. **Proposed:** "The sentences before the passage, at lines 15204-15207, quote..."
- `retrieve_when` and canon cell fit.

### 10. `lpc.quote.the-branch-cut-from-the-vine` (F6-I)

- Text, NPNF locus and PL locus (32254-32262) are verified.
- **Pairing with "the washing is not repeated": holds.** The first claim guard requires it and cites NPNF line 12932, which is correct. The body quotes it word for word, and the lens note states it. The guard against "validity" also holds.
- **R10-1 (P2), rendering:** the comparison *ita ... quemadmodum* ("just as") is dropped. The last sentence now stands alone, and the reader has to supply the analogy. **Proposed last sentence:** "In the same way, feeling does not stay with a person's limb when it is cut off from the body."
- **R10-2 (P2), retrieve_when:** the trigger "participant asks why a person baptized among schismatics was not baptized again" sends exactly that question to a passage that does not answer it. Only the paired sentence does; on its own, the passage leans the other way. The guard covers the risk, but the trigger should match what the passage says. **Proposed:** "participant asks what a baptism given outside the Church lacked, if it was not given again".
- **R10-3 (P2), body:** "That sentence ends:" introduces two sentences. **Proposed:** "That sentence and the next read:".
- Canon cell fits, and the divergence note (null) is right.

### 11. `lpc.quote.pardon-through-a-wicked-clergyman` (R2, F6-I)

- Text and NPNF locus are verified. PL locus: see B-1 (32485-32492).
- The Latin-based corrections are right. "Ministry" is NPNF's addition; the Latin is *per malum clericum*. *Sed tamen catholicum ministrum* is concessive. The divergence note is accurate.
- **"Catholic" gloss: holds.** A claim guard rules out "Roman Catholic" and requires a gloss when the word is shown, and the lens note gives the gloss.
- **R11-1 (P2), rendering:** the *etiamsi* ("even if") on the wicked cleric is the load-bearing concession, and the rendering softens it: "He may come through a wicked cleric...". **Proposed:** "He may even come through a wicked cleric, a worthless man and a hypocrite, who is still a Catholic minister."
- **R11-2 (P2), typo in a claim guard:** "The passage is the near end of a long argument". **Proposed:** "The passage comes near the end of a long argument on the sin against the Holy Spirit (Matthew 12:32); it needs that frame and must not be told without it."
- The ordination and Donatist guards hold. `retrieve_when` and canon cell fit.

### 12. `lpc.quote.consider-who-was-there` (F6-I)

- Text and NPNF locus are verified. PL locus: see B-1 (50696-50701).
- The rendering carries every clause. "The One" before "in whose name" adds no claim, and "properly" for *recte* is right.
- The claim guards hold: the speaker is a baptized believer voiced by Augustine ("We answer him", NPNF line 19717), and the Donatist's words are not Augustine's position. No ordination or dispute between bishops is shown. The trigger "how Augustine answered the Donatists on baptism" is supported by the sermon heading, "Against the Donatists".
- `retrieve_when` and canon cell fit. No findings beyond B-1 and B-2.

## Readability note (not a finding)

Regate reports 11 edited fields below FK 8. CLAUDE.md treats grade 8 as a floor worth staying above, not a hard limit. These renderings are short preaching sentences, and raising the grade would mean adding words, which the rendering bar forbids. I do not count this as a defect. Mark should decide whether the grade-8 floor applies to quote renderings at all; the rendering file raises the same question.

## Counts

- P0: 0
- P1: 1 (B-1, six records: 4, 5, 6, 9, 11, 12)
- P2: 14 (B-2, R1-1, R3-1, R3-2, R5-1, R5-2, R5-3, R6-1, R9-1, R10-1, R10-2, R10-3, R11-1, R11-2); B-2 covers five records.
- Records with no finding of their own: 2, 7, 8, 12 (7 and 12 are touched only by the batch-level findings B-1 and B-2)
- Gates: records PASS, regate PASS

B-1 is a mechanical correction: six line numbers, each in two places, in `wb_lpc_s24.py`. It is still blocking, because a `verified-direct` record must not cite a range that leaves out the end of its own passage. Round 2 should be a targeted recheck of the corrected ranges, plus any P2 items taken up.

VERDICT: Substantial revision required
