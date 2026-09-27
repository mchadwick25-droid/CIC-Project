# Doc_09 — Round 4 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

**Deliverables under review (four, reviewed together):** `Doc_09_Story_Inventory.md`; `Story-Chunks/` (`lpcstory001`–`lpcstory007`); `lpc_Story_Index.md`; `scripts/gen_story_index.py`. All revised after Round 3 at commit `abff3618` and unreviewed.

**Date:** 2026-09-15 · **Prior rounds:** 1 (2H 8M 12L 5C), 2 (0H 11M 17L 5C), 3 (1H 10M 12L 5C) — all SUBSTANTIAL REVISION REQUIRED.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**3 HIGH · 9 MEDIUM · 16 LOW · 5 COSMETIC**

**The repository is still not composited.** Every quotation I re-verified — and I re-verified all of them, not only the ones the Round 3 pass touched — is verbatim in its cited source. No invented participant, event or outcome appears in any of the seven Story Texts. That finding now holds across four independent rounds.

**All three HIGH findings are in the Absent Story Notes**, and all three are assertions about what the sources do not contain that the sources themselves refute. Two of the three notes were written from scratch by the Round 3 fix pass; the third survived, unchanged, inside the note that pass rewrote. This is the fourth consecutive round in which the most serious defect is a negation, and the third in which the negation was produced by the immediately preceding fix pass.

**I would have said MINOR REVISION on everything else.** The stories are sound, the generator reproduces its index exactly, and the two genuinely mechanical Round 3 fixes (the AST guard count, the `.**` gravity splitter) both hold under independent re-derivation and mutation. But Article 20 makes the naming of absence a *participant-facing* obligation and requires that the *reason* for an absence be named correctly. Three absences are named with the wrong reason, and in two cases with a reason the cited source contradicts on its own page.

---

# Method

1. **Read all four deliverables in full**, plus `L4-Templates/Story_Repository_Chunk_Template.md`, CF V7.4 Part II (plain text), Constitution Articles 17/19/20/23, `Source_Registry.md` rows 1/7/28/41/99/122/159/171/191/192/194/204/212, Doc_02 §§2/6/9, Doc_08 §§2B-5/2A-2/5, and the Round 1–3 review artifacts and Decision Log entries.
2. **Built an independent source extractor.** Repaired `cyprian.xml` (truncated at the junk-after-root at line 32338, void tags closed, wrapped in a root element) and walked it with ElementTree, **marking `<note>` spans before any text was flattened**, so that editorial apparatus is separated from the world's voice by construction rather than by stripping. Body and note text are held apart for all 130 titled units. Cyprian's *Epistles*, *Treatises* and Pontius's *Life* were read from that extraction, never from the flat file.
3. **Rebuilt the Possidius text.** Weiskotten 1919 prints Latin and English on facing pages interleaved in the vendored file. I reconstructed the English-only stream by page headers, de-hyphenated across line breaks, and re-verified every `lpcstory007` quotation against it. (My first pass against the raw file produced four false negatives — see *Check confirmations*.)
4. **Re-derived the index independently.** Copied the world tree to a scratch directory, ran the committed generator, and diffed against the committed `lpc_Story_Index.md`: **byte-identical**. Then re-derived the halting-guard count, the §7 word count, and every gravity/row/tier/confidence cell with my own code rather than the script's.
5. **Mutation-tested the generator** at nine sites, each in an isolated copy of the full tree.
6. **Audited closure** against Round 3's own 28 findings, site by site, with a notice-stripping sweep that separates *use* from *mention* — then hand-checked every hit, because the sweep is known to produce false positives in this build and did so again.
7. **Confirmed every finding a second way** before recording it. Where the second way disagreed with the first, the finding was dropped.

---

# The closure claim

`lpc_Decision_Log.md`, 2026-09-15 (Doc_09 Round 3): *"All findings are addressed; the closure claim below is counted rather than asserted."*

**That is false, and by the widest margin of the three fix passes.** Round 2's pass closed 5 of 27; Round 3's reviewer found 19 of 27 closed. Against Round 3's own 28 findings (1 HIGH, 10 MEDIUM, 12 LOW, 5 COSMETIC — M1 is the meta-finding about closure itself and is excluded, leaving 27 substantive):

| | Count | Findings |
|---|---|---|
| **Closed** | **9** | HIGH; M3; M4; M5; M6 (main clause); M7; M8; L1; L4 |
| **Partial** | **3** | M2; M9; L8 |
| **Open** | **15** | M10; L2; L3; L5; L6; L7; L9; L10; L11; L12; C1; C2; C3; C4; C5 |

**Nine of twenty-seven.** The Round 3 fix pass's diff touches ten files for a net 34 lines outside the review artifact and the Decision Log — which is roughly the size of a nine-finding fix, not a twenty-seven-finding one. The shape Round 3 named ("fixing the site a reviewer quotes and not the site it names") has widened: this pass largely fixed the findings the reviewer wrote extended prose about (the HIGH, M4, M5, M6, M7, M8) and left every finding recorded as a one-line LOW or COSMETIC untouched, including four that are now open for their third consecutive round (L6, L7, C1, and Round 2's M10).

**Three of Round 3's fifteen open findings are open because the fix pass never re-read the file it had already edited.** L2 (section order), C3 (five verbatim copies of a boilerplate) and C1 (the index's unscannable Confidence cell) all sit in text the pass rewrote in the same commit.

---

# HIGH

### H1 — `lpcstory006`'s new Absent Story Note says every account of Cyprian's death comes from inside his own community, and names a hostile court record as one of them in the same sentence

**Site:** `Story-Chunks/lpcstory006_the-death-of-cyprian.md`, Absent Story Note (l. 51). Written from scratch by the Round 3 fix pass in answer to Round 3's M7.

**What I found.** The note reads:

> **What cannot be told is what the execution looked like to anyone who was not already devoted to him.** Every surviving account of Cyprian's death comes from inside his own community — Pontius, his deacon, writing in praise, and the *Acta Proconsularia*, a record kept by the court that killed him. **There is no bystander.** … **So the most public event in this world's first phase has no public witness** …

The sentence refutes itself. A record kept by the proconsular court that condemned Cyprian is not from inside Cyprian's community; it is from the side that killed him, which is precisely the perspective the note's own opening sentence says is missing. Three independent sources in this build say so:

- `Source_Registry.md` row 41 calls the *Acta* *"the official trial record of Cyprian's own martyrdom"* and *"the one strictly documentary (as opposed to hagiographic) record of Cyprian's own death, **distinct in genre from Pontius's *Life***"*;
- `Doc_09` §6 item 2 calls it *"the official trial record"* and the witness that *"would let `lpcstory006` be told at Tier 1 rather than Tier 3"*;
- Pontius himself, at *Life* §11, points past his own account to it: *"And what God's priest replied to the interrogation of the proconsul, **there are Acts which relate**."*

Compounding it: the *Acta* **has not been read by this build** — the chunk's own Source field and its own parenthetical say so. The note therefore asserts a property of the perspective of a document nobody here has opened. That is Round 1's H1 in its purest form ("reading to a chosen boundary, then asserting a negative about what lies past it"), applied to a boundary that is not a section break but an unopened file.

The note closes by instructing that *"a participant who asks what an ordinary Carthaginian made of it should be told that the question cannot be answered from this world's record."* Under Article 20 that instruction is participant-facing. It rests on two false premises.

**Why this matters.** Round 3's M7 asked for this note to be recast from a build-progress item into a genuine evidentiary absence. The recast produced a false evidentiary absence — a harder defect than the one it replaced, because a build-progress item is at least true. It also produces an internal contradiction the generator cannot see: `lpc_Story_Index.md` §4 prints `lpcstory006`'s row 41 as *"named but explicitly not used"* on the same page where the chunk's note characterises what row 41 contains.

**Fix.** Rewrite the note around the absence that is actually there and is sharper: **there is no account by anyone who was neither devoted to Cyprian nor employed to kill him.** Name the *Acta* as the non-community witness that exists, is vendored, and is unread — which is what §6 item 2 already says — and drop *"There is no bystander"* and *"no public witness."* Then say what genuinely cannot be recovered: the crowd in the trees left nothing of its own, and no source describes the execution from the position of an uncommitted onlooker.

---

### H2 — `lpcstory007`'s new Absent Story Note says this world's record stops at Augustine's death; the chapter it cites records what happened to Hippo afterwards

**Site:** `Story-Chunks/lpcstory007_the-psalms-on-the-wall.md`, Absent Story Note (l. 63). Added in full by the Round 3 fix pass in answer to Round 3's M7.

**What I found.** The note reads:

> **And the city outside is absent entirely.** Hippo was under siege while this happened. Possidius gives the bishop's bedroom in detail and the town beyond it almost nothing — **what the siege was like for the congregation Augustine had served for thirty-five years is not recorded by him or by anyone else.** A participant asking what happened to those people should be told that this world's record follows its bishop to the end and then stops.

The chunk's own Source field cites *Vita Augustini* **XXVIII–XXXI**. Chapter XXVIII, inside that span, records both things the note says are absent.

On what the invasion was like for congregations, at length: churches *"stripped of priests and ministers"*; *"holy virgins and all the monastics scattered in every direction"*; people who *"gathered in flight amid the mountain forests, in the caves and caverns of the rocks"* and *"gradually perished of hunger"*; *"the hymns and praises of God perish from the churches"*; bishops and clergy *"begging in abject poverty."*

And on Hippo specifically, after the death the note says the record stops at:

> *"These cities too still stand, protected by human and divine aid, **although after Augustine's death the city of Hippo, abandoned by its inhabitants, was burned by the enemy**."*

I verified this in both columns of the bilingual edition — the Latin *"licet post eius obitum urbs Hipponensis incolis destituta ab hostibus fuerit concremata"* on p. 114 and the English on p. 115. It is running text in both, not apparatus.

The chunk contradicts itself on the same point: its Usage Guidance states flatly **"Hippo fell"** — a fact available in this build from this passage and, so far as I can find, from nowhere else in the vendored corpus.

**Why this matters.** Article 20 requires naming *"whose voices the sources structurally omit, **why they are omitted**, and what that omission means."* Here the architecture would tell a participant that the record is silent about the people of Hippo when the record's last word on them is that they abandoned the city and it burned. That is not a calibration error; it withholds from the participant the one thing the source does say about the population the participant asked after. It is also the exact defect class of Round 1's H1 and Round 3's HIGH, produced again by the fix pass answering them.

**Fix.** Keep the first paragraph, which is sound and well-argued (Possidius is the only witness to the last weeks; no second account exists in this corpus — I confirmed no other account of Augustine's death is vendored). Replace the second: Possidius records the siege, the fourteen months, the blockade, the devastation of African congregations generally, and Hippo's abandonment and burning after Augustine's death. What he does not record is any of it **from inside the congregation** — what he gives is a bishop's summary of what he *saw*, with no congregant's account of enduring it. That is the true absence and it is a stronger one.

---

### H3 — `lpcstory005`'s Absent Story Note and Doc_09 §7 item 3 deny that the lapsed silence is source loss; the corpus records two letters the lapsed wrote and Cyprian circulated

**Site:** `Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md`, Absent Story Note (l. 57, final sentences); `Doc_09_Story_Inventory.md` §7 item 3.

**What I found.** The chunk's note ends:

> **Doc_09 §7 item 3 makes this the repository's sharpest absence** … The absence is not source loss. It is that the people whose failure organised this world's whole penitential system **were never asked, and no one thought to write down what they said.**

Doc_09 §7 item 3 states the same thing more briefly: the lapsed *"appear as a category in Cyprian's letters, as petitioners at the confessors' doors, as a problem to be adjudicated"*, and *"not one of them left an account of why."*

Every clause of that is refuted by body text in this corpus — not by ANF's editorial Arguments, which I set aside.

*Epistle* XXVI, **Cyprian to the Lapsed**, §1: *"I marvel that **some, with daring temerity, have chosen to write to me** as if they wrote in the name of the Church"* … *"it behoves them … **not to write letters in the name of the Church**, when they should rather be aware that they are writing to the Church."* §2: *"But **some who are of the lapsed have lately written to me**, and are humble and meek and trembling … **these persons beseeching have written to me** that they acknowledge their sin, and are truly repentant."* And, closing: *"**whoever you are who have sent this letter, add your names to the certificate, and transmit the certificate to me with your several names. For I must first know to whom I have to reply; then I will respond to each of the matters that you have written.**"*

*Epistle* XXVII, to the Roman clergy, in Cyprian's own narration: *"the combined temerity of certain of the lapsed … **wrote to me**, not asking that peace might be given to them, but claiming it as already given … **as you will read in their letter of which I have sent you a copy**."*

So: the lapsed wrote, collectively and unprompted, at least twice. Their bishop replied to both, asked them to sign their names so he could answer them point by point, and forwarded a copy of one letter across the Mediterranean. **Neither letter survives.** The silence is exactly and only source loss — the third of the three categories the L4 template names (*"source loss, survivorship gap, transmission thinness"*).

**Why this matters.** Three reasons, in ascending order.

First, the claim is false at the level of fact, in the section whose entire content is a claim about what the record does not contain.

Second, Article 20's primary duty is to name *why* a voice is omitted. The document names the wrong why, and the wrong why is the flattering one: "no one thought to write it down" locates the failure in the world, where "their letter was copied, circulated, and lost" locates it in transmission. Those carry different formation content and the architecture is obliged to get it right.

Third, **the true account is the better story.** A body of people who had failed under persecution wrote collectively to their bishop claiming the peace was already theirs; he was scandalised enough to reply, to copy their letter to Rome, and to demand their signatures — and their letter is the one document in the exchange that did not survive, while all three of his sides of it did. That is a sharper absence than the one asserted, and it is fully sourced.

**A second, smaller defect at the same site.** Doc_09 §7 item 3 opens *"This world's central first-phase crisis is about **people who sacrificed** under persecution"* and then offers Numeria and Candida as its named lapsed exemplars. *Ep.* XX says of Candida, in Celerinus's own words: *"she gave gifts for herself that she might not sacrifice … **I know, therefore, that she has not sacrificed**."* She is a *libellatica*, lapsed on Cyprian's taxonomy but not by the definition this item supplies four sentences earlier. Round 3's M8 pushed this document toward Numeria and Candida; it did not carry the letter's own qualification with them.

**Fix.** Replace *"The absence is not source loss…"* with the documented account: the lapsed wrote at least twice (*Ep.* XXVI §§1–2), Cyprian replied and circulated their letter (*Ep.* XXVII), and their letters do not survive. Rewrite §7 item 3's middle sentences to add "as correspondents who wrote to their bishop in their own name" to the list of ways the lapsed appear, and either widen the item's opening definition to include *libellatici* or drop Candida from the pair and carry Numeria alone.

---

# MEDIUM

### M1 — the closure claim is false for the third consecutive round, at 9 of 27

**Site:** `lpc_Decision_Log.md`, 2026-09-15 (Doc_09 Round 3) entry, opening paragraph.

**What I found.** Set out in full under *The closure claim* above: nine of Round 3's twenty-seven substantive findings are closed, three are partial, fifteen are open. The entry claims all findings from all three rounds are addressed and describes the claim as *"counted rather than asserted."* No count appears anywhere in the entry.

**Why this matters.** Round 2's entry made the same claim at 5/27 and Round 3's reviewer caught it at 19/27. A closure record that overstates is worse than an unfinished fix pass, because the next round cannot distinguish a finding considered and declined from one never read. This one is worse than its two predecessors in a specific way: it *names* the counting discipline without performing it, which is harder for a reader to detect than an unqualified assertion.

**Fix.** Publish the table. Where a finding is declined rather than fixed (L2 and C3 look like reasonable declines), record the decline and the reason; that is a legitimate outcome and it is not what "addressed" currently means here.

---

### M2 — Doc_09 §7 item 4 puts the daughter searching "the ashes"; the letter does not, and §4 of the same document certifies that it does not

**Site:** `Doc_09_Story_Inventory.md` §7 item 4.

**What I found.** §7 item 4 opens: *"Numidicus's wife burns; **his daughter searches the ashes** and finds her father alive."*

*Ep.* XXXIV reads: *"when afterwards his daughter, with the anxious consideration of affection, **sought for the corpse of her father**,—was found half dead, was drawn out and revived."* Where she searched is not stated. Cyprian's only reference to burning is that the martyrs were *"slain by stones and by the flames"* and the wife *"burned (I should rather say, preserved)."* "The ashes" is supplied.

This is Round 1's L2 at a second site. Round 1 caught *"He was in the heap"* and *"a heap of bodies"* in `lpcstory003` and the Round 1 fix pass removed both — and `lpcstory003` now carries an explicit correction reading *"Where she searched, the letter does not say."* Doc_09 §4's audit row for `lpcstory003` certifies: *"The wife's death and the daughter searching for the body are **his words, not this document's**."* The document contradicts its own certification four sections later.

I checked the four committed revisions with `git show`: the phrase is present in the original draft and unchanged through all three fix passes. No reviewer has raised it.

**Why this matters.** Article 19 prohibits free invention at every stage of construction. This is a small supplied image, and no chunk carries it — but it sits in the section a Representative's absence-naming draws on, and it is the only place in the four deliverables where a concrete physical detail is asserted that its source does not contain. It is also the single clearest demonstration of the brief's diagnosis: the fix landed at the quoted site and nowhere else, three times running.

**Fix.** *"his daughter searches for his body and finds him alive."*

---

### M3 — the CO-022 escalation's third framing is also answered by CF's own text; CF classifies stories, not sources

**Site:** `Doc_09_Story_Inventory.md` Disposition, *Governance or methodology*; §2's closing paragraph.

**What I found.** The item now reads: *"whether one source may be split across tiers story by story at all — CF defines the tiers by the character of the material and never says whether a single work can sit in two."*

CF V7.4 Part II does answer it, in three places, and the answer is that the question's premise is wrong — CF never assigns a tier to a source at all:

- *"Stories also exist on a spectrum of historical reliability. Using them responsibly requires transparent classification of **where on that spectrum each story sits**."* (l. 249)
- *"**The four-tier story classification framework**"* (l. 250) — and every tier definition is phrased about stories, material or narrative, never about works or authors.
- The Story Inventory requirement: *"a working catalog of **stories** available within the world, **classified by tier**, with source identification"* (l. 271); Step 9: *"a complete catalog of **all formation stories** with final tier classifications"* (l. 699).

CF also already contemplates finer-than-story granularity in both directions — Tier 1 *"May carry Widely Accepted or Contested confidence **for specific details within the narrative**"*, Tier 3 *"Inferential/Thin **for specific details shaped by hagiographic convention**"* — and it handles the author of a hagiography separately, through the Narrative Source Author Gravity entry at l. 275, not through the tier.

So the unit of tiering is the story. A source's being "split" across tiers is not an exception requiring licence; it is the ordinary consequence of the unit CF chose. **This build's rule "A source is not a tier" is CF's rule, restated.**

**Why this matters.** This is the third consecutive framing of the same escalation and the third to be answered by CF's own Part II. Rounds 2 and 3 each narrowed it after showing CF covered the wider version; the narrowing has now reached a question CF answers more directly than either of the two it replaced. An escalation that survives three retractions consumes project-lead attention the category exists to protect.

**Fix.** Close the item. Record in §2 that CF classifies stories rather than sources, cite l. 249–250 and l. 271, and state that the per-story assignment is a reading of CF rather than a construction on top of it. Keep the *disclosure* that Pontius is tiered differently at `lpcstory001`/`002` than at `lpcstory006` — that is worth saying — but stop escalating it. The genuinely open governance item in this document is the index-generator-as-build-artifact question inherited from Doc_08 and the polarity-blind row derivation at M4(c), both of which are correctly filed.

---

### M4 — the §3 cross-check's two new comparisons both fail open, and the source-row test excuses exactly the rows a chunk disclaims

**Site:** `scripts/gen_story_index.py` ll. 167–181.

**What I found.** Round 3 added Gravities and Source to the §3 cross-check and rewrote the row test from intersection to containment, closing Round 1's M4(b). Three mutations, each run against a full isolated copy of the tree:

| Mutation | Expected | Actual |
|---|---|---|
| **A** — blank Doc_09 §3's Gravities cell for `lpcstory001` | halt | **rc 0**, index emits `G1, G3` from the chunk; divergence invisible |
| **B** — remove every row number from §3's Source cell for `lpcstory004` | halt | **rc 0** |
| **C** — re-source `lpcstory006` in §3 to *"* Acta Proconsularia* (row 41)"* | halt | **rc 0**; §4 still prints *"named but explicitly not used: 41, 194"* |

A and B are the same defect: `if cgrav and cgrav != set(...)` and an empty `csrc_rows` both mean *no claim, no comparison*. The script's own comment on the title check says it plainly — *"a fuzzy test that fails open is worse than none"* — and the two checks written to satisfy that principle fail open in the weakest possible way, by treating a deleted claim as agreement.

**C is the more serious.** `_stray` subtracts `s["rows_excluded"]` as well as `s["rows"]`. `rows_excluded` is, by construction, the set of rows a chunk named **in order to disclaim**. So Doc_09 §3 may cite as a story's source precisely the row the chunk says it has never opened, and the guard is satisfied. The generator then emits an index in which §3's authority and §4's disclaimer point at the same row. This is Round 1's M4(c) — polarity blindness — reappearing inside the check written to enforce its remedy.

The masthead continues to assert that a run re-verifies *"the agreement between each chunk and Doc_09 §3's own table."* Under A, B or C it does not.

**Fix.** Require presence, not just consistency: a §3 Gravities cell yielding no `G[1-8]` and a §3 Source cell yielding no row are each a halt. Compare `csrc_rows` against `s["rows"]` **only** — a row a chunk disclaims is not a row §3 may cite as its source, and if §3 wants to mention it, it belongs in a footnote the parser does not read as the Source cell.

---

### M5 — Round 3's M2 half-landed: the Document Log still ends at the Round 1 fix pass, and the Disposition still recites Round 1's two HIGHs as current

**Site:** `Doc_09_Story_Inventory.md` Document Log; Disposition, second paragraph.

**What I found.** Round 3's M2 asked for three things: update the Status, **add the two missing Document Log rows**, and rewrite the Disposition against the later result. Two of three landed.

The Document Log still has exactly three rows and ends at *"Round 1 fix pass — this revision … REVISED — unreviewed."* Rounds 2 and 3, their reviews and their fix passes, appear nowhere in it — while the Status line four sections above says *"REVISED after Round 3"* and the Disposition recites all three rounds' counts.

And the Disposition's second paragraph still reads: *"**Both HIGH findings** are claims this document made *about* its sources: a silence asserted in Pontius that his §10 does not contain, and two quotations altered in transcription."* Those are Round 1's H1 and H2, both closed. Round 2 had no HIGH; Round 3 had one, and it was neither of these. A reader of the Disposition is told the current HIGH findings are two that no longer exist.

**Why this matters.** Round 3 named this as *"Round 2's own M2 with the files swapped — the remedy landing in the sibling and not in the document."* The remedy has now landed in two of the document's three stale places and not the third. `lpc_Story_Index.md` derives its review history from the artifact directory and is correct; Doc_09's hand-maintained Log is a literal and is two rounds stale. The generated file remains more current than the document that governs it.

**Fix.** Add four rows (Round 2 review, Round 2 fix pass, Round 3 review, Round 3 fix pass). Replace the *"Both HIGH findings"* paragraph with one written against Round 3.

---

### M6 — `lpcstory007`'s tier warrant says Possidius uses one scriptural phrase; the sentence the chunk quotes contains two, and one of them is a death formula

**Site:** `Story-Chunks/lpcstory007_the-psalms-on-the-wall.md`, Tier Justification (l. 49).

**What I found.** The chunk argues Tier 1 against `lpcstory006`'s Tier 3 on the ground that Possidius carries none of CF's three hagiographic markers, and concludes: *"**The one scriptural phrase he uses** — 'well-nourished in a good old age' — is flagged in his own text as a quotation and is doing the work of an epitaph, not of a pattern the events have been shaped to fit."*

Weiskotten prints the sentence the chunk itself quotes ten lines earlier as: *"while we stood by and watched and prayed, **"he slept with his fathers,"** as it is written, **"well-nourished in a good old age."**"* Two flagged scriptural phrases, not one, in one clause. Chapter XXXI carries at least six in total (*"scribe instructed unto the kingdom of heaven"*, *"the pearl of great price"*, *"So speak ye and so do"*, *"Whosoever shall so do and teach men"*). The chunk's Story Text drops the inner quotation marks from both, which is how the count came to be one.

The one it omits is the load-bearing one. *"He slept with his fathers"* is a patriarchal death-formula: it patterns the death on Scripture, which is the operation the chunk says is absent here and present in `lpcstory006`.

**Why this matters.** The distinction between `lpcstory006` (Tier 3) and `lpcstory007` (Tier 1) is one of the two most consequential judgements in this repository, and it is made on this sentence. I think the tier still holds — there is no miracle and no providential intervention, and an epitaph formula is genuinely weaker than Pontius's authorial *"what happened in the case of Zacchæus"* — but the warrant as stated is inaccurate about its own source, and the accurate version is a closer call that the chunk should be making out loud.

**Fix.** Restore the inner quotation marks in the Story Text. Rewrite the warrant to concede both phrases and argue the distinction where it actually lies: Pontius names his typology and applies it to *what physically happened in the clearing*; Possidius quotes two set phrases at the moment of death and shapes no event to them.

---

### M7 — Round 2's M10 is open for a third round, and in five chunks rather than one: build-process notices sit inside deployable Story Text

**Site:** `lpcstory002` ll. 17, 21, 29; `lpcstory003` ll. 19, 21; `lpcstory004` l. 17; `lpcstory007` l. 23 — all inside `## Story Text`.

**What I found.** Round 2's M10 named `lpcstory002`'s notice; Round 3's M10 re-raised it verbatim as untouched. It is still untouched, and the same pattern holds in four other chunks. The largest is `lpcstory002`'s closing block (~75 words) narrating Round 1's H1, the section boundary the chunk had read to, and the build's habit of asserting negatives.

`CLAUDE.md` is explicit that canonical build output carries *"no notes, commentary, change history, review discussion, or process narration"* and that such material *"belongs in `Ministry/`"* — and the chunks are the files a retrieval layer serves. Whatever the eventual assembly step strips, the Story Text as committed is not deployable as written.

**Why this matters.** Not the accuracy of the notices — they are accurate and valuable — but their location. A notice in the Tier Justification or below a rule is an audit trail; the same notice between two sentences of narrative is a passage the Representative would have to be told to skip.

**Fix.** Move every notice out of `## Story Text` into a `## Correction History` block at the foot of each chunk, keyed by the sentence it corrects. This closes M10 in one edit across five files and removes the question of what a deployment step has to strip.

---

### M8 — the halting-guard notice now describes a method the script no longer uses

**Site:** `scripts/gen_story_index.py` l. 266, rendered at `lpc_Story_Index.md` l. 11.

**What I found.** The count itself is now right — I parsed the script's AST independently and got **13**, matching; the naive `count("sys.exit(")` gives **14**, reproducing the Round 3 defect exactly. Round 3's M4 is genuinely closed.

But the notice that reports the fix still ends: *"Counted here **with a grep over the script** rather than from memory."* The count is no longer a grep; it is an AST walk, and the whole point of the Round 3 change was that a grep over a script's own source counts its own literal. The sentence that explains the method now describes the defect.

The notice also still contains the hard-coded literal *"the script has **thirteen** halting sites"* immediately beside a figure the script derives — the arrangement that produced the Round 3 contradiction in the first place. It happens to agree today.

**Why this matters.** This number has reached a brief unre-derived four rounds running across two generators. The notice is the place a reader checks the derivation; it currently misdescribes it.

**Fix.** *"Parsed from this script's own syntax tree, which cannot see its own string literals."* Delete the embedded *"thirteen."*

---

### M9 — Doc_09 §7 item 3's claim about what the lapsed left is carried into the `lpcstory005` Usage Guidance as a retrieval instruction

**Site:** `Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md`, Usage Guidance (l. 67).

**What I found.** *"Doc_09 §7 item 3 makes this the sharpest absence in the repository: the world's central first-phase crisis is documented entirely from the side of those who did not fail it."*

Narrowly, for Celerinus's sister, the guidance is correct and I would leave it: no one wrote down what she thought. But the generalisation to *"the world's central first-phase crisis is documented entirely from the side of those who did not fail it"* is the H3 claim in the field that tells the Representative what to say, and it is not true: *Ep.* XXVI is a reply to the lapsed's own collective letter, quoting its claim and rebuking its self-description, and *Ep.* XXVII reports that a copy went to Rome. The crisis is documented *with* the lapsed's side present in outline, reported by a hostile respondent — which is a different and more interesting epistemic situation than the one the Representative is instructed to describe.

**Why this matters.** Recorded separately from H3 because it is a different fix at a different site — the same second-site pattern this build keeps producing — and because Usage Guidance is closer to the participant than an Absent Story Note.

**Fix.** Keep the sister-specific sentence. Replace the generalisation with the documented one: the lapsed's own letters were written and are lost; what survives of their case is their bishop's rebuttal of it.

---

# LOW

**L1 — Round 3's L2 open: the Absent Story Note precedes Usage Guidance in all six chunks that carry one.** `L4-Templates/Story_Repository_Chunk_Template.md` orders the sections Story Text → Formation Ecology Connection → Tier Justification → Usage Guidance → Source Identification (Tier 4 only) → **Absent Story Note**. Every chunk puts it before Usage Guidance. *Fix:* move it, or record the deviation as a deliberate build convention.

**L2 — Round 3's L3 open: Doc_09 §2's Tier 2 confidence line trims CF without ellipsis.** CF l. 257: *"Widely Accepted to Dominant Modern Reconstruction. **The tradition is authentic; specific details and attributions carry Contested confidence.**"* Doc_09 prints the first sentence and stops, in a section whose masthead says the bands are *"its own [CF's] words."*

**L3 — Round 3's L5 open: *Ep.* LI was dropped from `lpcstory001` without a reason.** The correction notice explains why *Ep.* XXXIII went and says nothing about LI, which Round 1 verified as relevant. The chunk's corroboration now rests on one locus.

**L4 — Round 3's L6 open for the third round: "Tobias, who buried the dead of 'his own race only.'"** Pontius: *"Tobias **collected together those who were slain by the king and cast out**, of his own race only."* The quotation marks are placed correctly; the verb immediately outside them is not Pontius's. Confirmed live text, not inside a notice.

**L5 — Round 3's L7 open for the third round: *Ep.* LXVII is described twice as "Cyprian's own letter."** It opens *"Cyprian, Cæcilius, Primus, Polycarp … and Paulus, to Felix the presbyter"* — thirty-seven named senders. `lpcstory001`'s Source field calls it *"Cyprian's own letter on episcopal election"* and its Tier Justification says *"In *Ep.* LXVII **Cyprian argues**…"* Not the intra-corpus misattribution failure mode, but the same discipline `lpcstory005` applies scrupulously to *Epp.* XX–XXI is not applied here.

**L6 — Round 3's L9 open: the tier reversal against Doc_02 §9 item 10 is still unnamed.** Doc_02 §9 item 10: *"Pontius's *Life* is described there in terms matching the Framework's own **Tier 3** definition without being so labeled."* Doc_09 assigns Pontius Tier 1 for two of the three stories drawn from him and cites §9 item 10 twice, both times for the provisional-inventory fact only.

**L7 — Round 3's L10 open: `lpcstory006`'s Tier 3 argument never engages CF's genus clause.** CF's Tier 3 opens *"Material attributed to specific figures or moments but **resting on collected tradition rather than direct documentation**."* Pontius is direct documentation by a named eyewitness. The chunk argues the hagiographic-markers sub-clause at length and never addresses the genus it sits inside — which is the strongest available argument *against* the tier the chunk assigns, and the template asks for tier disagreement to be carried at full strength.

**L8 — Round 3's L11 open, and it will fire on this review.** The Status line and the Disposition's *"this file is the Round N fix pass"* are both derived from `ART.glob("Doc09_Round*_Review.md")`. Reproduced: I dropped a one-word `Doc09_Round4_Review.md` into a scratch copy and re-ran the generator, which emitted *"REVISED after Round 4"* and *"this file is the Round 4 fix pass and is unreviewed"* with no fix pass having occurred. *Fix:* as Round 3 proposed — derive the round count from the artifacts and the fix-pass claim from a marker the fix pass writes into Doc_09's Document Log.

**L9 — Round 3's L12 open: the confidence-band guard is substring-based.** Reproduced: a `lpcstory001` declaring **"Not Documented"** (with Doc_09 §3 matched to it) passes, and the No-Tier-5 audit prints *"**Yes** — Not Documented."*

**L10 — an all-whitespace Phase cell passes the missing-phase guard.** Reproduced: `| G1, G3 |   |` yields `phase_of["lpcstory001"] == ""`, `missing_phase` is empty, and the Master Table emits a blank Phase cell. The script's comment claims *"a missing value is reported rather than inferred."* *Fix:* treat an empty stripped value as missing.

**L11 — the generated index contains a notice that swallows another notice's opener, which the generator refuses in its inputs.** `lpc_Story_Index.md` l. 11 nests `**[Amended at Round 2:** … **]**` inside `**[CORRECTED, 2026-09-15 — Round 1's brief-correction 1:** … **]**`. Running the generator's own `assert_coverage` over its own output returns one swallowing notice — the exact condition that makes it exit FATAL on a chunk. Nothing derives from the index, so this is not a live correctness problem; it is the one-notice-grammar discipline failing in the file that exemplifies it.

**L12 — Round 2's L14 open: the guard enumeration lists eight conditions under a count of thirteen.** Unlisted: no front-matter fence; a surviving notice-like opener; no chunk files found; no transmission phase in §3. The sentence would read honestly with four clauses added.

**L13 — Doc_09 §6 item 2 quotes a phrase without naming who said it.** *"the one strictly documentary (as opposed to hagiographic)"* is `Source_Registry.md` row 41's own wording. As printed it reads as a quotation from scholarship about the *Acta*. *Fix:* attribute it to the Registry, or unquote it.

**L14 — `lpcstory007`: "Two facts close the chapter." They do not.** *"He made no will"* and the library instruction sit roughly mid-chapter; XXXI continues with the disposal of the church's possessions, Augustine's treatment of his relatives, the clergy and monasteries he left, the secular poet's epitaph, and Possidius's closing prayer. The Source field for this chunk has been corrected twice already for misplacing material within XXXI; this is a third instance, unfixed.

**L15 — duplicate story-id chunk files are not detected.** Reproduced: copying `lpcstory001_election-of-cyprian.md` to `lpcstory001_duplicate.md` yields *"Eight stories — Tier 1 (7)"* with two identical rows, no halt. Latent.

**L16 — a premise in this round's own brief is wrong, and I am recording it as the brief-correction the independence instruction asks for.** The brief states that *"a seventh Absent Story Note was added to `lpcstory007`."* It is the **sixth**: six of seven chunks carry the section, and the chunks' own boilerplate says so (*"Six now do. `lpcstory001` does not"*), as does the Round 3 Decision Log entry (*"seven files, six now carrying Absent Story Notes"*). The brief's other two checkable premises — thirteen halting sites, and Round 3's 19-of-27 — are both correct; I re-derived the first independently.

---

# COSMETIC

**C1 —** Round 3's C1 open for the third round: `lpc_Story_Index.md` §1's Confidence cell for `lpcstory006` still carries the full two-clause band, making the master table unscannable at the one row a reader most wants to scan. Round 1's C4, Round 3's C1.

**C2 —** Round 3's C2 open: Doc_09 §8 item 2's placeholder is justified *"so the list's own cross-references do not shift."* I grepped the world build: nothing cross-references Doc_09 §8's item numbers (the `§8 item` hits are all Doc_01's). `lpcstory006` cites *"Doc_09 §6 item 2 and §8"* without an item number.

**C3 —** Round 3's C3 open: the `[ADDED … Round 1's L8]` boilerplate is repeated verbatim in five chunks and has grown from 62 to ~80 words each. The sentence that was wrong about `lpcstory007` is fixed — in all five copies, which is the argument for having one.

**C4 —** Round 3's C4 open: Doc_09 §3.1 quotes CF's Tier 4 placement rule as *"is appropriate in world documents (particularly ecological reconstruction sections)."* with the period inside, dropping CF's governing continuation *"**when it is explicitly marked as reconstruction in the construction notes**."* The condition is the operative half.

**C5 —** Round 3's C5 open: `gen_story_index.py` declares `global BANDS` inside the chunk loop and rebuilds the dict on every iteration; `BANDS` is undefined if the loop body never runs and is read again at l. 315.

---

# Check confirmations, and my own defective checks

The brief asks for at least one of each. I had three defective checks and dropped one finding on re-confirmation.

**Defective check 1 — the documented Weiskotten failure mode, for the fourth round running.** My first sweep of `lpcstory007`'s quotations against the raw vendored file reported **four missing**: *"except only at the hours in which the physicians came…"*, *"He had all that time free for prayer"*, *"With all the members of his body intact, with sight and hearing unimpaired…"*, and *"He repeatedly ordered that the library of the church…"*. All four are present. Two are broken by end-of-line hyphenation (`physi-\ncians`, `re-\npeatedly`); one is split by a full Latin page inserted between *"With all the members of his body intact,"* and *"with sight and hearing unimpaired"*; one differs only in the capital of a mid-sentence quotation. Reporting any of them would have been a fabricated finding against a clean chunk. Fixed by reconstructing the English-only stream by page header and de-hyphenating before matching.

**Defective check 2 — case.** My Cyprian quotation sweep reported *"as many of you as have been baptized into Christ have put on Christ"* absent from *Ep.* LIX. It is present, capitalised, inside Cyprian's own quotation of Paul.

**Defective check 3 — mention read as use, exactly as the brief predicts.** My closure sweep flagged `lpcstory005` as still carrying *"to be killed by death by hunger and thirst"* (Round 1's H2) and *"named by no source, including her brother's letter"* (Round 3's M8). Both sit in heading-form notices — `**Second, and this one is a correction. [CORRECTED …]**` and `**Two other lapsed women … [CORRECTED, 2026-09-15 — Round 3.]**` — where the bracket closes before the bold run ends, so the correction's own narration of the error falls outside every delimiter a stripper can see. Both are mention. Hand-checking every sweep hit turned two would-be findings into none. This is now the fourth documented instance of this false positive in this build; a shared stripper that treats the heading form as a delimiter would end it.

**A finding I dropped on re-confirmation.** Doc_09 §7 item 2 cites Doc_02 §6 for the claim that this world's record lacks *"any ordinary congregant writing about ordinary congregational life as such."* Doc_02 §6's skew bullet opens by naming *Epp.* XX–XXI as **"two lay believers' own letters [that] survive in their own words,"** which looked like the opposite of the claim built on it. Reading the bullet to its end: *"What remains true: no source anywhere in this world's own vendored corpus is authored by an ordinary lay believer *writing about ordinary congregational life as such*."* Doc_09's citation is exact. No finding.

**Confirmation 1 — the index is genuinely derived and genuinely current.** Copied the world tree to a clean directory, ran the committed `gen_story_index.py`, and diffed against the committed `lpc_Story_Index.md`: **byte-identical**. Nothing in the index is hand-edited, and it is not stale.

**Confirmation 2 — the guard count is right, and the Round 3 defect is real.** Independent AST walk of the committed script: **13** `sys.exit` calls. Naive `count("sys.exit(")`: **14**. Both figures reproduced outside the script. Round 3's M4 closes.

**Confirmation 3 — the §7 word count is right.** Independent notice-stripper over Doc_09 §7: **671** words (739 unstripped), matching the index's derived figure exactly.

**Confirmation 4 — Round 3's M6 fix is real, not another accident.** M6 found the gravity derivation correct only because two chunks' `Retrieve-When` fields repeat their G-codes. I removed the codes from `lpcstory005`'s and `lpcstory007`'s `Retrieve-When` in separate isolated copies: both still yield `G2, G8` and `G1, G2` from the `**Gravities: …**` declaration alone. The `.**` splitter works.

**Confirmation 5 — for every HIGH.** H1: the *Acta*'s character confirmed from `Source_Registry.md` row 41, Doc_09 §6 item 2, and Pontius *Life* §11 independently. H2: the burning of Hippo confirmed in Weiskotten's Latin (p. 114) and English (p. 115) on facing pages. H3: the lapsed's letters confirmed at *Ep.* XXVI §§1–2 and *Ep.* XXVII, both from body text with `<note>` spans excluded before flattening, never from an ANF Argument.

**Confirmation 6 — no Registry row-number collisions.** `boundary()` matches the first line beginning `| N |`; rows 1, 7, 41, 191, 192 and 194 each match exactly one line in `Source_Registry.md`, so the lookup is sound.

**What I tested hardest.** The three Absent Story Notes, at source, sentence by sentence — they are where the brief pointed and they are where the defects are. Then the generator, by mutation at nine sites. Then the closure claim, finding by finding against Round 3's own list.

**What would change the verdict.** Fixing H1, H2 and H3 — three paragraphs, all of which become *stronger* statements of absence when corrected — plus M2's four words. With those five edits I would return MINOR REVISION on the same reading; nothing in the MEDIUM band below M2 is blocking, and the LOW and COSMETIC tails are a cleanup pass. If a fix pass disagrees with any of the three HIGHs, the thing to produce is not an argument but the source: for H1, any text saying the *Acta* is a community document; for H2, a reading of *Vita* XXVIII that does not record Hippo's burning; for H3, a reading of *Ep.* XXVI that is not a reply to a letter from the lapsed.

---

# Adequate to proceed to Doc_10?

**Not as it stands. Yes after a short, targeted fix pass.**

The evidentiary base is sound and has been re-verified four times: seven stories, every quotation verbatim, no composite, no invention in any Story Text, tiers argued rather than asserted, and a generated index that reproduces exactly from its committed script. That is the part of Doc_09 that Doc_10 consumes as *content*, and it is ready.

What is not ready is the part Doc_10 consumes as *instruction*. Step 10 is Representative Emergence; the Absent Story Notes and the Usage Guidance fields are where this document tells a Representative what it may not say and why. Three of the six Absent Story Notes currently instruct it to assert a silence the sources do not have, and Article 20 makes that a participant-facing constitutional obligation rather than a construction note. A Representative built on `lpcstory006` as committed would tell a participant that the execution of Cyprian has no record outside his own community; one built on `lpcstory007` would say the record of Hippo stops at Augustine's deathbed; one built on `lpcstory005` would say nobody thought to write down what the lapsed said. All three are wrong, and all three are the kind of wrong a participant could catch.

The fix is small and does not touch a single Story Text. Rewrite three paragraphs, amend §7 items 3 and 4, and close the Document Log. Everything else can be carried into Doc_10 as open items.

---

# CO-022 escalation assessment

**Representative identity, title, or voice:** does not apply. This document makes no identity, title or voice decision. Agreed with the Disposition.

**Portfolio-level or cross-world:** correctly filed, and the three items are real. The corpus-wide editorial-apparatus item is live and well handled — `lpcstory004` met it and avoided it, citing *Ep.* LIX §3's body where the ANF *Argument* carries the same figure; I verified the sum stands in §3 of the body and that the *Argument* does print it. The index-generator-as-build-artifact item is inherited from Doc_08 Round 5 and unresolved. The polarity-blind row derivation at M4(c) is correctly identified as something that will be written into every sibling world's story index — and M4 above shows it has already propagated once *within this script*, from the derivation into the cross-check written to guard it, which strengthens the case for escalating it.

**Governance or methodology — the "a source is not a tier" item: recommend closing rather than re-filing a fourth time.** See M3. CF V7.4 Part II classifies stories, not sources: *"transparent classification of where on that spectrum each story sits"* (l. 249), *"The four-tier **story** classification framework"* (l. 250), *"a working catalog of **stories** … classified by tier"* (l. 271). A source sitting in two tiers is not an exception CF is silent about; it is the ordinary consequence of the unit CF chose. Each of the three framings has been answered by CF's own text, and each narrowing has landed on a question CF answers more directly than the one before. The right disposition is to record in §2 that the per-story rule *is* CF's rule, keep the disclosure that Pontius is tiered differently across `lpcstory001`/`002` and `lpcstory006`, and stop sending it up.

**Unresolved tensions:** one open — the 411 *Gesta*, relied on for nothing here. Correctly filed and correctly quarantined; no story draws on it and §6 item 4 says none should until it is read.

**One item the Disposition does not file and arguably should.** The *Acta Proconsularia* is vendored (inside row 194), licensable under `cic/texts/INTAKE.md` as a Latin witness where no English rendering exists, unread, and named by this document as *"the highest-value unexploited source."* It would move `lpcstory006` from Tier 3 to Tier 1 and it bears directly on H1. That is a reading task rather than an escalation category — but it is the single largest available improvement to this deliverable, it has been carried unchanged across four rounds, and it is the reason two of this round's findings exist.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**3 HIGH · 9 MEDIUM · 16 LOW · 5 COSMETIC.** Nine of Round 3's twenty-seven substantive findings are closed against a claim that all are.

The stories hold, for the fourth round running. What does not hold is what this document says about what its sources do not contain — and for the third round running, the worst of that was written by the fix pass answering the last round's finding about exactly that.

---

*Simulated review — informational only, not an Article 31 substitute.*
