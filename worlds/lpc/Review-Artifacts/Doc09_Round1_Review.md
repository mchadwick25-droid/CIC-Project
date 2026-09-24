# Doc_09 — Round 1 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

**Date:** 2026-09-15 · **Round:** 1 · **Deliverables under review (three, together):** `Doc_09_Story_Inventory.md`; `Story-Chunks/` (`lpcstory001`–`lpcstory007`); `lpc_Story_Index.md` and its generator `scripts/gen_story_index.py`.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH · 8 MEDIUM · 12 LOW · 5 COSMETIC.**

The story *selection* is sound and the repository is not composited: every one of the seven stories rests on a real text that this build has actually opened, and I could not find a single invented participant, event or outcome. The two HIGH findings are not invention. One is a **silence asserted that the cited source does not have**, repeated three times in one chunk and written into the Representative's own speech instructions. The other is **two altered quotations inside a Story Text**, one of which changes the plain sense of what a confessor wrote about his sister. Both are the class of defect Article 19 and the No-Tier-5 rule exist to prevent, and both are fixable without re-selecting a single story.

**Adequate to proceed to Doc_10 after one fix pass** — see the dedicated section below.

---

# Method

**What I actually did, so the grading can be audited.**

1. **Rebuilt the corpus with structure intact rather than using the flattened text.** I parsed `cyprian.xml` element by element, carrying (a) the enclosing work from the `title=` attribute on `<div2>`/`<div3>`, and (b) `<note>` depth, so every character of the 1.72M-character Cyprian volume is tagged with its work and its note status *before* any stripping. I separately marked all 92 ANF *Argument* regions by locating paragraphs opening `Argument.—` and masking to the paragraph break. I then built three searchable indices from the same span table: **all** (notes inline), **body** (note spans replaced by a single space, boundaries preserved), and **notes** (the inverse).

2. **Extracted every quoted string in all seven chunks by strict alternating-delimiter split**, not by regex pairing — 74 strings in total, including the short ones a minimum-length filter would silently drop and thereby misalign every subsequent pair. Every chunk has an even number of `"` characters; the split is exact.

3. **Matched each string against the corpus punctuation-insensitively and whitespace-insensitively** (all whitespace including newlines collapsed; typographic quotes, dashes, `æ`/`œ` normalised; all non-alphanumerics reduced to a single space), with an ellipsis-aware second pass that requires each fragment in order within a bounded window. For each hit I recovered the **containing work**, the **note flag** and the **Argument flag**.

4. **Verified section numbers** by locating the paragraph-initial `N.` markers inside each work's own span and binning each hit.

5. **Read the primary passages whole, not just the matched strings** — Pontius §§5, 9–10, 15–18; Cyprian *Ep.* XXXII, XXXIII, XXXIV, LI, LIX, LXVII; *Ep.* XX, XXI, XXII in full; Possidius *Vita* XXVIII–XXXI and the epilogue — and read each chunk's Story Text against them sentence by sentence.

6. **Verified Possidius separately** against `cic/texts/possidius_vita-augustini_weiskotten1919.txt`, with a de-hyphenation pass for the edition's line-broken words and by hand across the bilingual page break where the English is interrupted by the Latin apparatus.

7. **Read CF V7.4 Part II at source** (`cf74.txt` lines 250–271, plus the Story Tier to Confidence Cross-Walk at 215–221) and checked Doc_09 §2's five block quotations word for word.

8. **Reproduced the generator.** I copied the deliverables to a scratch tree, ran `gen_story_index.py`, and diffed: **the committed `lpc_Story_Index.md` reproduces byte-for-byte.** I then forced **every** halting site by mutation and recorded each message, and separately hunted for defects the guards do not catch by mutating inputs the guards do not read.

9. **Checked the upstream citations** — Doc_02 §§1, 2, 6, 9; Doc_04 §5; Doc_05 §11; Doc_07 §2B; Doc_08 §§1, 4, 5, 7, 9 and forces 1B-2, 2A-1, 2A-2, 2B-2, 2B-5, 3A-1, 3B-1, 3B-2; Source_Registry rows 1, 7, 28, 41, 99, 122, 159, 171, 191, 192, 194, 204, 212; the L4 chunk template; Constitution Articles 17, 19, 20, 23, 31; and Doc_01–Doc_08's own Status lines.

**What I tested hardest, and what I did not.** Hardest: the quotations (all 74, every one traced to a work and a note/Argument status); the two documented failure modes; the §6 candidate-declination grounds; and the generator. Least hard: the Retrieve-When / Do-Not-Retrieve-When judgements as *pastoral* judgements — I checked them against the sources, not against encounter practice; and Doc_08's forces analysis, which I took as given per its own eight rounds.

---

# The central question: is every story sourced rather than composited?

**Yes, with the qualifications at H1 and H2.** Story by story:

| Story | Source opened | Every narrative element in the source? |
|---|---|---|
| `lpcstory001` | Pontius §5 | **Yes.** Three quotations, all §5 body. The neophyte claim, the "judgment of God and the favour of the people", the "untaught season" — all Pontius's own words, in order. |
| `lpcstory002` | Pontius §9 | **Yes for what is asserted; no for what is denied.** See H1. |
| `lpcstory003` | *Ep.* XXXIV | **Yes**, with two small narrative additions at L2. Nine quotations, all letter body, none in the Argument. |
| `lpcstory004` | *Ep.* LIX §§1–3 | **Yes.** The sum, the mechanism, the eight named recipients, the Pauline argument — all body text. |
| `lpcstory005` | *Ep.* XX §§2–4, XXI §§2–3 | **Yes as to events; no as to two quotations.** See H2. |
| `lpcstory006` | Pontius §18 | **Yes.** The crowd, the trees, the Zacchaeus aside, the bound eyes, the failing hand, "power granted from above" — every element in §18 body, in order. The cleanest chunk in the set. |
| `lpcstory007` | Possidius XXXI (+ XXVIII/XXIX, epilogue) | **Yes**, but the Source field does not cover two of the Story Text's sentences. See M5. |

**No element in any Story Text is invented.** No participant, no outcome, no detail without a text behind it. That is the thing this document exists to guarantee, and on the evidence it holds.

---

# Job 1 — the quotations, the tiers, the bands

## 1.1 Editorial apparatus read as the world's voice — the trap is AVOIDED, and `lpcstory004`'s claim is TRUE

**Of the 74 quoted strings across all seven chunks, not one resolves to a `<note>` span.** Exactly one resolves inside an ANF *Argument*, and it is the one `lpcstory004` itself labels as the Argument and quotes in order to exclude it.

`lpcstory004`'s specific claim — "This chunk cites §3 of the letter body" — is **verified**:

- `"We have then sent you a sum of one hundred thousand sesterces, which have been collected here in the Church over which by the Lord's mercy we preside…"` resolves to *Ep.* LIX, **paragraph 3, body text, Argument flag false**.
- `"Cyprian Begins by Deploring the Captivity… and Says that He is Sending Them a Hundred Thousand Sesterces"` resolves with **Argument flag true** — the 19th-century editorial matter, correctly identified as such.

The build met the trap it has fallen into eight times and did not fall in. That is worth recording as plainly as the failures have been.

## 1.2 Intra-corpus misattribution — `lpcstory005`'s claim is TRUE

Recovered from the `<div3>` `title=` attributes, not from the running text:

- *Epistle* XX — **"Celerinus to Lucian."** Opens `1. Celerinus to Lucian, greeting.`
- *Epistle* XXI — **"Lucian Replies to Celerinus."** Opens `1. Lucian to Celerinus, his lord, and (if I shall be worthy to be called so) colleague in Christ, greeting.`
- *Epistle* XXII — **"To the Clergy Abiding at Rome…"** Opens `1. Cyprian to the presbyters and deacons abiding at Rome, his brethren, greeting.`

Neither XX nor XXI is by Cyprian; XXII is. The chunk's Source field states exactly this. **Verified.** Every quotation in the chunk resolves to the correct one of the two confessor letters.

## 1.3 The tiers — the distinction is principled, and it is inconsistently applied

I tested `lpcstory006` (Pontius, Tier 3) against `lpcstory007` (Possidius, Tier 1) on CF V7.4's own Tier 3 markers — "the idealized portrait of a saint's life, the miracle sequence, the death as completion of a formed life" — by reading both chapters whole.

**The distinction survives the test.** Pontius §18 supplies an **authorial typological aside** ("that there might not even be wanting to him — *what happened in the case of Zacchæus* — that he was gazed upon from the trees"): the account tells the reader it is patterning itself on Scripture. It supplies a **providential intervention at the climax** ("until the mature hour of glorification strengthened the hand of the centurion with power granted from above"). And it closes on apostrophe — "O blessed people of the Church…". Possidius XXXI supplies none of the three: sheets of psalms pinned on a wall, a request not to be disturbed, an inventory of what the dying man did not own, and one scriptural tag ("well-nourished in a good old age") that Possidius flags in his own text as a quotation. **That is a real textual difference, not a convenience.** The two chunks' tier arguments are the strongest prose in this deliverable.

**But the same test, applied honestly, does not clear the other two Pontius stories.**

- `lpcstory002` asserts: *"The account carries none of the hagiographic conventions Delehaye catalogues… no miracle, no typological patterning, no vindication."* Within its own cited range §§9–10, Pontius calls Cyprian **"the pontiff of Christ, who excelled the pontiffs of the world"**, and §10 patterns the congregation explicitly against Scripture: **"Something more was done than is recorded of the incomparable benevolence of Tobias… Tobias collected together those who were slain by the king and cast out, of his own race only."** That is typological patterning, and it is vindicatory ("if the Gentiles could have heard these things as they stood before the rostrum, they would probably at once have believed"). The stated ground of the Tier 1 assignment is false on the text. (Folded into H1.)
- `lpcstory001` does not claim absence of convention; it substitutes a corroboration test. That is a legitimate move — but §5 itself carries proleptic martyr-foreknowledge ("with a latent foreboding of divinity they were in such wise demanding… not only a priest, but moreover a future martyr") and an apostolic typology ("Possibly that apostolic experience might then have happened to him… of being let down through a window"). So the corroboration has to carry the whole weight — and half of it is mis-cited. (M3.)

**On the principle itself.** CF V7.4 nowhere says that tier attaches to the story rather than the source. Doc_09 §2 states "**A source is not a tier**" in the register of a quoted rule; it is this build's own construction. It is *defensible*: CF's Tier 3 explicitly houses "hagiographic narrative… as a specific type within this tier." It is also *not the only route CF offers*: CF's Tier 1 confidence clause says a Tier 1 story "may carry Widely Accepted or Contested confidence for specific details within the narrative depending on the author's access and perspective" — which is precisely the alternative `lpcstory002` takes. The build therefore has two mechanisms for the same problem and uses each without saying why here and not there. (M6.)

## 1.4 The confidence bands — all seven within CF's band; one pairing is internally inconsistent

Checked each pairing against CF's Story Tier to Confidence Cross-Walk (cf74.txt 217–220) and CF's per-tier confidence paragraphs (253, 257, 261, 266):

| Story | Tier | Confidence | CF band | Within band? |
|---|---|---|---|---|
| 001, 003, 004, 005, 007 | 1 | Documented | Documented → Widely Accepted | **Yes** |
| 002 | 1 | Widely Accepted | Documented → Widely Accepted | **Yes** |
| 006 | 3 | Contested for the portrait; Inferential/Thin for details shaped by convention | Contested for portrait; Inferential/Thin for convention-shaped details | **Yes — exact** |

All seven are in band. **But the band-setting rationale is applied inconsistently** (M8): `lpcstory002` is stepped down to Widely Accepted because "a reported speech inside a biography of praise is not the same evidentiary object as a letter in the man's own hand," while `lpcstory007` — whose own Tier Justification states that "**no second account of Augustine's death exists in this corpus**" and that "the tier rests on the eyewitness claim and the absence of genre machinery, not on corroboration" — sits at Documented. An uncorroborated single witness writing in praise about a forty-year friend is, on this document's own stated logic, the weaker of the two.

Doc_09 §2's quotations of CF are **accurate** at Tier 1, Tier 2, Tier 4 and No-Tier-5 — word for word. Tier 3's confidence line is silently trimmed (C1).

---

# Job 2 — the structural requirements

## 2.1 §7 Absent Stories — substantive, and item 4 survives the test

564 words (exact — I recomputed the generator's own count independently), five enumerated absences, each with a named evidentiary ground. Not a placeholder by any reading.

**Item 4 tested against `Source_Registry.md` and Doc_02 §6, as directed.** Doc_02 §6 does record that named women appear in this corpus "in real narrative weight" — Albina at *Ep.* CXXVI and the Nuns of Hippo at *Ep.* CCXI (Registry row 11). **This does not falsify §7 item 4**, because Doc_02 §6 in the same paragraph records that "Albina's own motivations and the nuns' own grievances are known only through Augustine's own framing of them," and closes: "no specific textual trace meeting any of the three bounding conditions for a marginalized voice's own perspective has been identified and verified this session." §7 item 4's claim — that no woman in this world's horizon left a narrative of her own — is exactly the narrower claim Doc_02 supports, and §7 item 4 says so in terms ("Doc_02 §6 records that named women do appear in this corpus — the absence named here is narrower and sharper").

**The brief's premise here is therefore not a defect.** What §7 item 4 *does* do is illustrate the absence entirely from Phase One (Numidicus's wife and daughter; Numeria and Candida) and never mention Albina or the nuns — the two strongest counter-cases, and the only two in Phase Two. That weakens the item rhetorically without making it wrong. Recorded as L-grade, not as a finding against the claim.

Items 1, 2, 3 and 5 each check out against the upstream documents they cite (Doc_08 §1 and §3B-2 for the 133-year silence and the single textual crossing; Doc_02 §6 and Doc_07 §2B for the ordinary believer; the *Ep.* XX text for the lapsed sister).

## 2.2 §6 Candidates declined — one is genuinely unread, one is NOT

**The *Acta Proconsularia* (§6 item 2): VERIFIED, and the "Latin only" claim is TRUE.**
`cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` carries the *Acta* from line 41413, with the trial dialogue in Latin at 41522ff (*tu es Thascius Cyprianus? … ego sum*). A corpus-wide search for the proconsul's name returns four files, all Latin, French or German — Hartel, Monceaux, Delehaye, Harnack. **No English *Acta* exists anywhere in `cic/texts`.** Doc_02 §1's supporting statement is real and I read it. Registry row 41 records the vendoring. This candidate is **genuinely unread rather than unavailable**, and §6 item 2's characterisation is correct in every particular.

**Augustine's sermons on Perpetua and the Scillitan martyrs (§6 item 1): NOT unread. Unavailable.** See **M1** — this is the brief's own premise failing, and it fails in the document's favour and against it at once.

**The boundary reasoning: SOUND.** §6 item 1 argues that a story about *this world's use of* an inherited martyr-story would be in-boundary where the martyr-story is not. I tested this against Doc_01's c. 246–430 boundary as Doc_02 restates it, and it is not merely defensible — it is **already the Registry's own position**: row 122 reads "Augustine's own Sermons 280–281 on Perpetua and Felicitas are **native, in-boundary preaching material** (distinct from the Passion of Perpetua itself, which predates this world's own c. 246 start, the same ground row 28 is excluded on)." Doc_02 §6 says the same. Row 28's exclusion turns on the *date of the Passion*, not on the topic; a 5th-century Hippo sermon is not dated 180. **The reasoning is cleared.** What defeats the candidate is availability, not boundary.

## 2.3 The generator — twelve halting sites, all reproduced; four defects none of them catches

**Reproduction.** The committed index regenerates **byte-for-byte**. I then forced every `sys.exit` in the file by mutating its input. All twelve fired:

| # | Guard | Forced by | Fired |
|---|---|---|---|
| 1 | notice swallows another notice's opener | nested `[CORRECTED …[REVISED …]]` in a chunk | ✅ |
| 2 | notice-like opener survives stripping | unterminated `[NOTED, …` | ✅ |
| 3 | no retrieval front-matter block | removed the fence | ✅ |
| 4 | missing front-matter field | deleted `Confidence:` line | ✅ |
| 5 | **Tier 5 declared** | `Tier: 5` | ✅ |
| 6 | missing required section | renamed `## Tier Justification` | ✅ |
| 7 | Tier 4 without Source Identification | retiered 003 to 4 | ✅ |
| 8 | confidence outside CF's band | Tier 1 + `Inferential/Thin` | ✅ |
| 9 | no chunks found | emptied `Story-Chunks/` | ✅ |
| 10 | Doc_09 §3 tier ≠ chunk tier | flipped 006 to Tier 1 in §3 | ✅ |
| 11 | chunk absent from §3 (and the inverse) | deleted the 005 row | ✅ |
| 12 | Absent-Stories placeholder | replaced §7 with one stub item | ✅ |

**The advertised count is wrong either way.** The generated masthead enumerates **nine** conditions and calls them "the eight lessons." The script has **twelve** halting sites, three of them unadvertised (3, 2 and 9 above). The review brief's own "nine halting guards" matches neither number. (L11.)

**Defects no guard catches** — each reproduced by mutation, recorded at **M4**:
- the No-Tier-5 Audit table's two answer columns are string literals, not computations;
- only the **Tier** column of Doc_09 §3 is cross-checked, while the masthead claims the whole table is;
- the row-extraction regex is polarity-blind, which produces a **live false statement** in the committed index;
- transmission phase is a keyword guess on the Source string, never cross-checked against §3's own Phase column;
- §5's item renderer is unvalidated and silently emits garbage rows on a legal Markdown variant.

---

# Findings

## HIGH

### H1 — `lpcstory002` asserts a silence the cited source does not have, three times, and writes it into the Representative's mouth

**Site:** `Story-Chunks/lpcstory002_the-plague-and-the-enemies.md`, Story Text (final line), Tier Justification ("Not Tier 3"), Usage Guidance ("Additional guidance"); and `Doc_09_Story_Inventory.md` §4, `lpcstory002` row.

**What I found.** The chunk cites **Pontius §§9–10**. Three times it states that Pontius records no congregational response:

> "**Pontius does not say what the congregation did next.** He moves on."
> §4: "**Nothing is supplied about what the congregation did in response** — Pontius does not say, and the chunk says he does not say."
> Usage Guidance: "**the story has no ending** — Pontius does not record whether the congregation obeyed, and the Representative must not supply one; the honest form is *'we are not told what they did.'*"

Pontius **§10 — the second half of the chunk's own cited range — records exactly that**, and in the verbal terms of the sermon just reported:

> "But if the Gentiles could have heard these things as they stood before the rostrum, they would probably at once have believed. What, then, should a Christian people do, whose very name proceeds from faith? **Thus the ministrations are constantly distributed according to the quality of the men and their degrees. Many who, by the straitness of poverty, were unable to manifest the kindness of wealth, manifested more than wealth, making up by their own labour a service dearer than all riches.** … **Thus what is good was done in the liberality of overflowing works to all men, not to those only who are of the household of faith.**"

"To all men, not to those only who are of the household of faith" is the direct answer to the address's own demand — care beyond one's own — which the chunk correctly identifies as the story's hard edge. §10 also supplies the Tobias typology that falsifies the chunk's second load-bearing negative, "no typological patterning" (see §1.3 above). Both failures are in §10; neither is in §9. The chunk rests on §9 alone while citing §§9–10.

**Confirmed a second way.** I read the passage directly in the raw XML — `<p class="c20" id="iv.iii-p25">`, ordinary body paragraph, no `<note>` and no Argument — independently of my matching pipeline. A third check: **no upstream `lpc` document quotes or cites Pontius §10 anywhere**, consistent with its never having been opened in this build.

**Why this matters.** An asserted silence is a source claim, and a false one is as much an Article 19 failure as an invented event — with a sharper edge, because Article 20's affirmative duty makes named absences load-bearing and this document's §7 builds on exactly that discipline. The concrete harm is deployed: the Usage Guidance instructs the Representative to tell a participant "we are not told what they did" about a source that tells us.

**Fix.** Read Pontius §10. Either (a) narrow the Source field to §9 and delete all three silence claims, or (b) keep §§9–10 and rewrite the ending to report what Pontius does say — which is stronger material, not weaker. In either case delete "no typological patterning" from the Tier Justification and rebuild the not-Tier-3 argument on grounds the text supports (the absence of *miracle* and of *providential intervention*, which do hold in §§9–10). Correct the §4 audit row.

---

### H2 — `lpcstory005` prints two quotations that are not what the source says, one of them meaning-changing

**Site:** `Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md`, Story Text, paragraphs 2 and 5.

**(a) *Ep.* XX §2 — a parenthesis deleted and the verb recast.**

| | |
|---|---|
| **Source (ANF, body text, no note):** | "And therefore I ask that you will grant my desire, and that **you will grieve with me at the (spiritual) death of my sister**, who in this time of devastation has fallen from Christ; for she has sacrificed and provoked our Lord, as seems manifest to us." |
| **Chunk:** | "**Grieve with me at the death of my sister**, who in this time of devastation has fallen from Christ; for she has sacrificed and provoked our Lord, as seems manifest to us." |

Two alterations inside the quotation marks and neither marked: the parenthetical **"(spiritual)"** is deleted with no ellipsis, and "that you will grieve" is recast as the imperative "Grieve". Removing "(spiritual)" removes the one word that tells the reader the sister is alive.

**This is the exact hazard the chunk itself names two sections later** and handles correctly there: "The ANF translation renders Lucian's grant of peace with a parenthesis — 'who (shall have peace)' — and attaches an editorial note. **A parenthesis in this translation frequently marks a translator's supply.** The chunk paraphrases the grant rather than quoting that clause." The discipline is stated, applied at one parenthesis, and silently violated at another in the same chunk's Story Text.

**(b) *Ep.* XXI §2 — a word substituted.**

| | |
|---|---|
| **Source:** | "wherein by the command of the emperor we were ordered **to be put to death** by hunger and thirst, and were shut up in two cells, that so they might weaken us by hunger and thirst." |
| **Chunk:** | "**to be killed by death** by hunger and thirst, and were shut up in two cells, that so they might weaken us by hunger and thirst," |

**"killed by death" occurs nowhere in the vendored corpus** — I searched the full volume including notes. It is not a variant reading; it is a transcription error that produces a phrase Lucian did not write.

**Confirmed a second way.** Both loci printed from the raw XML with markup intact; both are ordinary body paragraphs (`iv.iv.xx-p7`, `iv.iv.xxi`), neither inside `<note>`, neither inside an Argument.

**Why this matters.** Article 19's prohibition is on content not grounded in the world's evidence. Words inside quotation marks are the strongest grounding claim a chunk makes, and the chunk's Usage Guidance tells the Representative that "the register is theirs, not the bishop's." Case (a) additionally risks a Representative telling a participant that a confessor's sister died, when the world's record says she sacrificed and lived. Neither error invents an event; both misreport a text.

**Fix.** Restore both quotations verbatim. For (a): either quote in full with "(spiritual)" retained and the parenthesis explained, or paraphrase — the same remedy the chunk already applies to "(shall have peace)". For (b): "to be put to death by hunger and thirst". Then re-check every remaining quotation in this chunk against the source; these two were not caught by the build's own pass and the pass should be re-run, not spot-repaired.

---

## MEDIUM

### M1 — Augustine's Perpetua/Scillitan sermons are described as unread when the Registry records them verified *absent* from the corpus

**Site:** Doc_09 §6 item 1; §8 item 2.

**What I found.** §6 item 1: "It is not built here because **the sermon texts have not been read at source in this build**, and building it from the secondary literature alone would be sourcing a story to scholarship rather than to the world. **Named as the strongest single candidate for the next pass.**" §8 item 2 repeats: "Augustine's sermons on Perpetua and the Scillitan martyrs are **unread at source**."

`Source_Registry.md` row 171 says otherwise, and says it twice over: "**Checked directly, Round 14: Sermon 299/D is confirmed absent from this world's vendored NPNF corpus** (`cic/texts/npnf106_…xml` contains exactly 97 sermons, I–XCVII; no '299' or 'CCXCIX' reference anywhere) **and from the corpus map** — see row 189 (Morin's 1930 critical edition) for where the primary text would have to come from if this world's construction ever needs it." Row 122 records Gillette as "Not currently vendored. In copyright; consultation-only."

**Confirmed a second way, independently of the Registry.** I checked `cic/texts` myself: `npnf106` carries exactly 97 `shorttitle="Sermon …"` entries, and **no Augustine *Sermones ad populum* collection is vendored in any language** — not in NPNF, not in the Latin CSEL/Migne set (which holds *Enarrationes*, *Epistulae*, *Confessiones*, *De civitate Dei*, *De doctrina*, *Retractationes*, *contra Donatistas*, and nothing else). Sermons 280–281 and 299/D are not in this corpus at all.

**Why this matters.** "Unread" names a reading task a builder can discharge; "unvendored, verified absent, in copyright" names an acquisition obstacle the build has already investigated twice. Calling the second the first inflates the document's own improvability and, worse, promotes to "the strongest single candidate for the next pass" a story that cannot be built at all until a text is acquired. It also loses a real, checked finding that two earlier review rounds paid for.

**Fix.** Restate §6 item 1 and §8 item 2 on the Registry's own evidence: the sermons are native and in-boundary (rows 122, 171, and Doc_02 §6 all say so), **and they are not in this corpus** — the blocker is acquisition, with row 189 named as where the text would have to come from. Then re-rank: the *Acta Proconsularia*, which **is** vendored and merely unread, is the strongest available candidate, and §6 item 2 already says so.

### M2 — Doc_09's header states that Doc_01–Doc_08 are none of them self-disposed; three of them are

**Site:** Doc_09 header, "Input documents".

**What I found.** "Doc_01–Doc_08, all complete and independently reviewed, **none self-disposed** — CO-022 forbids a build thread from self-disposing a document against which any escalation category is open, and categories are open against **Doc_04 through Doc_08**."

Read directly from the documents' own Status lines: **Doc_01 — "Approved to proceed (self-disposed by the build thread, 2026-09-01)"; Doc_02 — "Approved to proceed (self-disposed 2026-09-12, on Round 30's clearing verdict)"; Doc_03 — "Approved to proceed (self-disposed by the build thread, 2026-09-09, on the project lead's own direct instruction)."** Doc_08's own header gets this right for its own inputs: "Doc_04, Doc_05, Doc_06 and Doc_07 — all complete and independently reviewed, none self-disposed."

The sentence also contradicts Doc_09's own Disposition six pages later: "**Five** documents in this world are complete, independently reviewed, and awaiting a disposition only the project lead can give. **This is the sixth.**" Five is right (Doc_04–Doc_08); "Doc_01–Doc_08 … none self-disposed" is wrong.

**Why this matters.** The build-state paragraph is what a reader uses to know what this document is standing on. Understating the disposition state of three cleared documents misrepresents the build's own position under CO-022 in the one paragraph written to state it.

**Fix.** "Doc_01, Doc_02 and Doc_03 — Approved to proceed. Doc_04 through Doc_08 — complete and independently reviewed, none self-disposed, because escalation categories are open against each."

### M3 — `lpcstory001`'s Tier 1 rests on corroboration, and half the corroboration is mis-cited

**Site:** `lpcstory001` Source field and Tier Justification; Doc_09 §3 table.

**What I found.** The chunk assigns Tier 1 on the ground that "**what settles it for this story specifically is corroboration outside Pontius's own frame** — Cyprian's letters argue the case for popular participation in episcopal election," citing "**Ep. XXXIII and LI**."

- ***Ep.* LI — correct.** "To Antonianus About Cornelius and Novatian" carries it exactly: "Cornelius was made bishop by the judgment of God and of His Christ, by the testimony of almost all the clergy, **by the suffrage of the people who were then present**, and by the assembly of ancient priests and good men."
- ***Ep.* XXXIII — wrong.** "To the Clergy and People, About the Ordination of **Celerinus as Reader**." I read all four paragraphs. It commends Celerinus's nineteen days in irons, his martyr grandmother Celerina and his uncles, and his placement on the pulpit as reader. **It contains nothing about episcopal election and nothing about popular participation** — its stated ground is the opposite emphasis: Celerinus was added to the clergy "not by human recommendation, but by divine condescension."

The corroborating loci that do exist in this corpus are ***Ep.* XXXII**, the companion letter about Aurelius: "**In ordinations of the clergy, beloved brethren, we usually consult you beforehand**, and weigh the character and deserts of individuals, with the general advice" — and ***Ep.* LXVII**, to the clergy and people in Spain: "since they themselves have **the power either of choosing worthy priests, or of rejecting unworthy ones**… that the priest should be chosen in the presence of the people."

**Why this matters.** The chunk's own rule is that where Pontius is the only witness and the narrative carries hagiographic convention, the tier drops to 3 — and Pontius §5 *does* carry convention (proleptic martyr-foreknowledge; the apostolic "let down through a window" typology). So corroboration is the whole of what holds this story at Tier 1, and half of it points at a letter about a reader.

**Fix.** Replace "Ep. XXXIII" with **Ep. XXXII and Ep. LXVII** in the chunk's Source field, the Tier Justification and Doc_09 §3's table, quoting the two clauses above so a reviewer can see the corroboration rather than take it on the citation.

### M4 — Four defects in `gen_story_index.py` that no guard catches, one of which puts a false statement in the committed index

**Site:** `scripts/gen_story_index.py`; `lpc_Story_Index.md` §§1, 3, 4, 5.

**(a) Output without a live computation — the No-Tier-5 Audit table is typed, not derived.** The rendering line is:

```python
w(f"| `{s['id']}` | {s['tier']} | **Yes** | **Yes** — {s['conf']} |")
```

Both answer columns are **string literals**. The computation that would justify them (the tier-set test and the `BANDS` test) lives ~60 lines earlier as a fatal. The table is true today only because the run reached the renderer. Move either check, relax either, or add a tier the `BANDS` dict does not cover, and the table prints "**Yes**" anyway. This is squarely against the script's own opening rule — "**DERIVE, never type.** … A number typed here is a number that goes stale" — and against the index's own masthead claim that "the confidence-band check" is "derived, and re-checked on every run."

**(b) The masthead overclaims the Doc_09 §3 cross-check.** The masthead: "**Derived, and re-checked on every run:** … and **the agreement between each chunk and Doc_09 §3's own table**." The code checks the **Tier column only** (`r"\|\s*`(lpcstory\d+)`\s*\|[^|]*\|\s*(\d)\s*\|"`). Demonstrated: I set Doc_09 §3's Confidence for `lpcstory001` to `Inferential/Thin` — flatly contradicting the chunk and outside CF's Tier 1 band — and **the generator emitted normally**, printing `Documented` in the index beside `Inferential/Thin` in Doc_09. **There is already a live divergence in the committed files:** §3 gives `lpcstory006` the confidence "Contested", where the chunk and the L4 template's own Tier 3 pairing require "Contested for the portrait; **Inferential/Thin** for details shaped by convention". §3 also titles `lpcstory001` "The election of Cyprian, **still a neophyte**" where the chunk's canonical `Story-Title` is "The Election of Cyprian" — and the template requires the title be used "consistently across all references to this story."

**(c) Polarity-blind row extraction, producing a false statement in the committed index.** `s["rows"]` is `re.findall(r"row(?:s)?\s+((?:\d+)(?:\s*[/,]\s*\d+)*)", s["src"])` — every number after "row"/"rows" in the Source field, regardless of what the sentence does with it. `lpcstory006`'s Source field reads: "The strictly documentary witness — the *Acta Proconsularia Sancti Cypriani* (**rows 41, 194**) — is vendored in Latin only and **has not been read in this build**." The index accordingly prints `lpcstory006 | 7, 41, 194` under the heading "**Registry row(s) cited**" and then asserts "**Every cited row is Native. No story draws on an Excluded row.**" `lpcstory006` does not draw on row 41; the chunk says so in the same sentence the number is taken from. The assertion is true only because row 41 happens to be Native. I demonstrated the mirror failure: adding "This story deliberately does **NOT** draw on row 28, the excluded Scillitan Passion" to `lpcstory004`'s Source field halts the generator with "**a story sourced to an Excluded row is a boundary breach**."

**(d) Transmission phase is a keyword guess, never cross-checked.** `ph = "Two" if "Possidius" in s["src"] or "Augustin" in s["src"] else "One"`. Doc_09 §3's table has its own Phase column; it is never read. Demonstrated: adding the word "Augustine" to `lpcstory001`'s Source field flipped its phase to **Two** in the index with no guard firing.

**(e) §5's item renderer is unvalidated.** The guard counts items with `^\*\*\d\.`; the renderer captures with `^\*\*(\d)\.\s*(.+?)\*\*`. These are different patterns over the same text. I rewrote §7's headings in the legal variant `**1.** There is no story…` — the guard passed, and §5's table emitted five rows each opening with a stray `**` and running on for a whole paragraph, under the unchanged sentence "**Not a placeholder.**"

**Why this matters.** The index is the artifact a reviewer filters by, and Doc_08's Round 5 already raised the index-generator-as-build-artifact question at portfolio level. (c) is the serious one: a derived table states something the source chunk contradicts, under a heading that asserts the check is "mechanical".

**Fix.** (a) Render the two audit columns from the same expressions the guards evaluate, or delete the columns and cite the guard. (b) Extend the §3 cross-check to Title, Confidence, Gravities and Phase, or narrow the masthead sentence to "the tier agreement". (c) Read cited rows from a dedicated field (e.g. `Registry-Rows:`) rather than by scraping prose, and give `lpcstory006` a way to name the *Acta* without being credited with it. (d) Read Phase from Doc_09 §3 and cross-check, or add a `Phase:` front-matter field. (e) Assert `len(items) == len(absent_items)` before rendering.

### M5 — `lpcstory007`'s Story Text draws on three parts of Possidius while citing one

**Site:** `lpcstory007` Source field ("*Sancti Augustini Vita* **XXXI**") and Story Text.

**What I found.** Everything from "He records something Augustine had said often" to "keep the books" is Vita XXXI, verbatim and accurate — I matched all twelve quoted strings (two only after de-hyphenating the edition's line-broken words and reading across the bilingual page break; see the check-confirmation section). Two Story Text sentences are not in XXXI:

- "**Possidius had been Augustine's friend for nearly forty years**" — the "almost forty" in XXXI is Augustine's years "as a priest or bishop"; the forty-year friendship is in Possidius's **epilogue** ("I have lived with this man… for almost forty years").
- "**The city was under siege by the Vandals while this happened.**" — Vita **XXVIII** ("For almost fourteen months they shut up and besieged the city") and **XXIX** ("And lo, in the third month of the siege he succumbed to fever").

**Why this matters.** Nothing is invented — both sentences are Possidius's own, and the siege sentence is the chunk's closing beat and its bridge to Doc_08's 3A-1/3B-1 seam. But the Source field is the chunk's whole sourcing claim, and a reviewer checking XXXI will not find two of the sentences there. Under the standard this document sets for itself, the citation must cover the text.

**Fix.** "*Sancti Augustini Vita* XXVIII–XXIX and XXXI, with the epilogue," or attach the two sentences to their own chapters inline.

### M6 — "A source is not a tier" is presented as the Framework's rule; it is this build's construction, and it departs from Doc_02 §9 item 10 without saying so

**Site:** Doc_09 §2, final paragraph.

**What I found.** §2 sets out CF's four tiers as block quotations, then closes: "**The tier is therefore assigned per story, not per source** … **A source is not a tier.**" The typography does not distinguish the Framework's words from the build's. CF V7.4 Part II does not contain this rule in any form — I read lines 250–271 whole.

Separately, **Doc_02 §9 item 10 reads Pontius's *Life* the other way**: "Pontius's *Life* is described there in terms matching the Framework's own **Tier 3** definition without being so labeled." Doc_09 assigns Pontius Tier 1 at two of three stories. That is a legitimate revision — Doc_02's was explicitly provisional — but it is a revision of an upstream reading and Doc_09 nowhere names it as one.

**Why this matters.** The individual chunks handle this well: `lpcstory006` says in terms "it is a judgement rather than a finding," and `lpcstory001` says "Stated as a judgement, not a finding." §2 states it as a rule. A rule that would govern how every world in the portfolio tiers an eyewitness hagiographer should be carried at the strength it actually has, and routed (see CO-022 assessment).

**Fix.** Mark §2's closing paragraph as this build's judgement, note CF's own alternative route (Tier 1 with a stepped confidence for genre-shaped details, which is what `lpcstory002` in fact takes), and state plainly that this departs from Doc_02 §9 item 10's provisional reading.

### M7 — the Tier-2-is-zero argument cites Doc_08 §2B-5 for something Doc_08 §2B-5 does not say

**Site:** Doc_09 §3.1, Tier 2 paragraph; repeated in `lpc_Story_Index.md` §2.

**What I found.** "Cyprian's letters were **gathered as a dossier by their own author in his own lifetime (Doc_08 §2B-5)**, not remembered and compiled by a later community."

Doc_08 Force 2B-5 is about survival "on the institutionally dominant side, through a 19th-century translation apparatus." The only dossier statement anywhere in Doc_08 is a single clause elsewhere: "**Cyprian forwarding a thirteen-letter dossier of his own correspondence**, knowing his letters are read aloud to other clergy." That attests **one act of forwarding thirteen letters**, not the collection history of the 82-letter corpus this world actually inherits — which Registry row 1 describes as "82 letters, including letters TO Cyprian from Rome, Cornelius, the confessors, Firmilian of Caesarea," a body Doc_02 §2 records as reaching us under CCEL's whole-body attribution.

**Why this matters.** Tier 2 = zero is one of the two structural claims §3.1 makes, and it is argued as evidentiary rather than editorial. The conclusion may well hold on other grounds — CF's Tier 2 wants *stories* in collected form, and a correspondence is not a story-collection however it was assembled — but the warrant actually offered does not reach it, and a reader following the citation will not find it.

**Fix.** Either drop the authorial-collection claim and rest Tier 2 = zero on CF's own definition (no apophthegmata, no sayings anthology, no *Vitae Patrum*, which §3.1 already says and which is sufficient), or cite the thirteen-letter dossier for what it is and stop short of a claim about the corpus.

### M8 — the confidence bands are set inconsistently between `lpcstory002` and `lpcstory007` on this document's own stated rationale

**Site:** `lpcstory002` and `lpcstory007` Confidence fields and Tier Justifications.

**What I found.** `lpcstory002` is stepped from Documented to **Widely Accepted** because "a reported speech inside a biography of praise is not the same evidentiary object as a letter in the man's own hand." `lpcstory007` sits at **Documented** although its own Tier Justification records: "Possidius is writing in praise, and a life written by a forty-year friend is not neutral. The ordinary corrective — check the detail against another witness — is unavailable: **no second account of Augustine's death exists in this corpus.**" `lpcstory002`, by contrast, *has* a corroborating witness — Cyprian's own *De mortalitate*, written into the same epidemic, which the chunk cites.

Both remain inside CF's Tier 1 band, so this is not a classification error. It is a calibration inconsistency in the direction Article 17 warns about ("invisible movement from attested evidence into speculation… overstated historical coherence").

**Fix.** Either step `lpcstory007` to Widely Accepted on its own stated ground (single uncorroborated witness, writing in praise), or state why the eyewitness-presence claim outweighs the absence of corroboration here but reported speech does not outweigh the presence of corroboration at `lpcstory002`.

---

## LOW

**L1 — `lpcstory003`'s Do-Not-Retrieve rule misstates its own source.** "Not for questions about the lapsed, which this story deliberately does not address." *Ep.* XXXIV addresses the lapse as the letter's stated occasion: the Lord added Numidicus "that he might adorn with glorious priests the number of our presbyters **that had been desolated by the lapse of some**." *Fix:* rewrite to "this story is about a confessor, not about the lapsed, though the letter names the lapse as the vacancy's cause."

**L2 — `lpcstory003`: two details not in the letter.** "**He was in the heap**" and "a daughter searching **a heap of bodies**" — the letter says she "sought for the corpse of her father"; no heap. "Numidicus had **watched** a group of Christians die" is an inference from "beheld with joy his wife"; the letter says he "sent before himself" the martyrs by his exhortation. *Fix:* delete "heap"; recast the watching as what the letter attests.

**L3 — `lpcstory002`: two unsourced narrative touches.** "then went further **than his hearers expected**" (no audience reaction in Pontius) and "Bodies were left **in the streets**" (Pontius: "There lay about the meanwhile, **over the whole city**"). *Fix:* trim to the source.

**L4 — `lpcstory004`: a word inside the quotation marks.** Chunk: "**to be** rescued and redeemed from the hands of barbarians by a sum of money." Source: "may now Himself **be** rescued and redeemed from the hands of barbarians by a sum of money—". *Fix:* move "to" outside the quotation.

**L5 — `lpcstory007` and Doc_09 §4: "we who were present".** Quoted in both as Possidius's words; the source reads "he asked **of us** who were present". *Fix:* quote as it stands, or drop to "in our presence", which is exact.

**L6 — §6 item 4 contradicts §6 item 2 and §8 item 1.** Item 4 calls the 411 *Gesta* "**this world's one unread source**", while item 2 and §8 item 1 record the *Acta* as unread. Doc_08's own wording is narrower: "the one **unexploited** source that could bear on **G5's force-connection**." *Fix:* adopt Doc_08's scope.

**L7 — the count of declined candidates disagrees with §6.** §4 says "**Two** candidate stories were declined for precisely this reason; see §6", and the index §3 repeats "§6 records **two** candidates declined on exactly that ground." §6 enumerates **four**. *Fix:* say which two, or change to four.

**L8 — no chunk carries an Absent Story Note, and at least four should.** The L4 template provides the section "where a story that might be expected cannot be told because evidence is insufficient, or where a partial story cannot be extended." Four chunks carry exactly that material inside other sections: 002's missing ending, 003's "the wife's own view… not recoverable", 005's "the sister does not speak", 007's "no second account of Augustine's death exists in this corpus." The generator has no guard for it. *Fix:* move the material into the template's own section, and add a guard.

**L9 — §6 item 1 states the wrong operative ground for Perpetua's exclusion.** It says Perpetua is out of boundary "**on the same reasoning that excludes the Scillitan martyrs at row 28**" (date). Registry row 204's Boundary Status column gives a different operative ground: "**Out-of-Boundary for this world by prior ruling** — assigned to `tertullian-s-voice`, not `latin-pastoral-congregational-christianity` (Mark's own 2026-08-26 ruling, independently reconfirmed this session)." *Fix:* name the ruling. It bears directly on whether a "next pass" may touch the text at all.

**L10 — `lpcstory007`: "The library, per Possidius's instruction, largely survived."** Possidius records the instruction, not the outcome; Doc_08 records "the inheritance was secured by copying, not by the siege," which is not the same claim as the library's survival. *Fix:* attribute or drop.

**L11 — the advertised guard count is wrong in the index and in the brief.** The masthead enumerates nine conditions and calls them "**the eight** lessons"; the script has **twelve** halting sites, three unadvertised (no front-matter fence; a notice-like opener surviving the stripper; no chunks found). The review brief's "nine halting guards" matches neither. *Fix:* derive the count, or state the conditions without a number.

**L12 — §7 item 4 argues entirely from Phase One.** Its four examples (Numidicus's wife, his daughter, Numeria, Candida) are all Cyprianic. The two strongest counter-cases — Albina at *Ep.* CXXVI and the Nuns of Hippo at *Ep.* CCXI, both named in Doc_02 §6 — go unmentioned, and both are Phase Two. The item is **correct** (see §2.1 above); it is weaker than it needs to be. *Fix:* name them and say why they do not reach a narrative of a woman's own.

---

## COSMETIC

**C1 —** Doc_09 §2's Tier 3 confidence quotation trims CF without ellipsis at the trim points: CF reads "Contested for the general portrait **or attribution**; Inferential/Thin for specific details shaped by **hagiographic** convention **or for events whose historical occurrence cannot be verified**."

**C2 —** `lpcstory002` merges across the source's interpolation: Pontius has `"It becomes us," said he, "to answer to our birth…"`.

**C3 —** `lpcstory005` quotes Doc_02 as "Firmilian"; Doc_02 reads "Firmilian **of Caesarea**".

**C4 —** `lpc_Story_Index.md` §1's Confidence cell for `lpcstory006` carries a full clause, which makes the master table unscannable at the one row a reader most wants to scan.

**C5 —** Doc_09's header paraphrases Doc_05 §11 item 9's "Pontius's *Life* and **the Perpetua sermons**" as "**the Perpetua material**", which slides toward the out-of-boundary *Passion*.

---

# Is the deliverable adequate to proceed to Doc_10?

**Yes — after one fix pass, and I would not hold it for a second review round on the story selection.**

The reasons, stated at the strength they have:

- **The repository is not composited.** Seven stories, seven real texts, every one opened. I read every Story Text sentence against its source and found no invented participant, event or outcome. That is the thing Doc_10 has to be able to build on, and it holds.
- **The two failure modes this build has committed before are both avoided.** No quotation anywhere in the seven chunks resolves to a `<note>`; the one that resolves to an ANF *Argument* is the one the chunk quotes in order to exclude. The two confessor letters are correctly attributed away from Cyprian. Both claims were made by the document and both survive direct checking.
- **The tier work is the strongest prose here.** `lpcstory006` and `lpcstory007` are a genuinely well-made pair, and the distinction between them is textual rather than convenient.
- **The generator reproduces byte-for-byte and every one of its twelve halting sites fires.**

What holds it at SUBSTANTIAL REVISION rather than MINOR is H1 and H2 together with M1 and M2: **four claims about sources or build state that are checkable and wrong**, two of them written into the Representative's own instructions. None requires re-selecting a story. H1 needs Pontius §10 read; H2 needs two quotations retyped and the chunk re-swept; M1 needs a paragraph rewritten on the Registry's own evidence; M2 needs one sentence corrected. M4 needs a short patch to the generator.

**The one thing I would not let pass to Doc_10 unfixed is H1**, because the Usage Guidance in `lpcstory002` is a deployable instruction to say something untrue about a source, and Doc_10 will carry it forward.

---

# CO-022 escalation assessment

- **Representative identity, title, or voice — does not apply.** This document makes no identity, title or voice decision. Noted separately and not as an escalation: `lpcstory002`'s Usage Guidance prescribes a specific Representative utterance ("we are not told what they did") that is false against the source. That is a content defect inside this document's own gift to fix (H1), not an identity decision.

- **Portfolio-level or cross-world — TWO items, one new.**
  1. *Inherited, and here handled correctly:* the corpus-wide editorial-apparatus item. Doc_09 §4's record at `lpcstory004` is accurate and I verified it. Worth carrying forward as the first **positive** instance in the ledger — the trap was met and identified, with the Argument and the body distinguished at the right paragraph.
  2. **New.** The index-generator-as-build-artifact item raised at Doc_08 Round 5 now has a concrete, reproducible instance: a derivation that **cannot distinguish a source a chunk cites from a source a chunk cites in order to disclaim** (M4c), which puts a false statement into a committed index under a heading asserting the check is mechanical. Every sibling build's story index will scrape Source fields the same way. **Route to review at portfolio level.**

- **Governance or methodology — open, unchanged at five, plus ONE NEW item.** **New:** "**the tier is assigned per story, not per source**" (Doc_09 §2). CF V7.4 does not state this rule, and CF's own Tier 1 confidence clause offers a different route to the same problem which this document also uses (`lpcstory002`). The rule changes how every world in the portfolio would tier an eyewitness hagiographer — Pontius here, Possidius here, and the equivalent figure in Donatism, Syriac and Alexandria. It also revises Doc_02 §9 item 10's provisional Tier 3 reading of the same source without naming the revision. **This is a project-lead decision, not a build-thread one.** Route it. (M6.)

- **Unresolved tensions — one open, unchanged.** The 411 *Gesta*, relied on for nothing here. Doc_09's own statement of it is accurate; only its scope-word is wrong (L6).

---

# Check confirmation — my own harnesses, including the ones that were wrong

This build has had thirty-odd failing checks turn out to be defects in the check. **Three of mine were**, and each would have produced fabricated HIGH findings. I record them before the findings that survived.

## Defective checks of my own (all caught before reporting)

**D1 — exact matching with notes left inline: 14 false negatives.** My first harness normalised whitespace including newlines and typographic characters, then searched the flattened text with notes in place. It reported "NOT FOUND" for, among others, `lpcstory004`'s entire sesterces quotation and five of `lpcstory005`'s. **Cause:** ANF interleaves `<note>` content *mid-sentence*, so a quotation that spans a note anchor is not contiguous in the flat text; and chunks legitimately end a trimmed quotation with a period where the source has a comma. Had I reported these, `lpcstory004` — the chunk that most carefully documents its own sourcing discipline — would have taken a fabricated HIGH.

**D2 — notes *deleted* rather than replaced: new false negatives, including two that the broken harness in D1 had found.** Replacing a `<note>` span with nothing joins the surrounding text and destroys the boundary. `"the common joy."` (*Ep.* XXXIV) and `"no longer bodies, but the carcases of many."` (Pontius §9) both went missing — **both are present in the source**. This is the exact shape the brief warns about: a harness that normalises one thing and not another. The fix was to replace each note span with a **single space**, preserving the boundary while excluding the content, and to match punctuation-insensitively.

**D3 — Possidius without de-hyphenation and across the bilingual page break: four false negatives.** The Weiskotten edition line-breaks words ("physi- cians", "re- peatedly"), so `lpcstory007`'s quotations [2] and [7] read as missing. Quotation [5] read as missing for a different reason: the English sentence "With all the members of his body intact, … with sight and hearing unimpaired…" is **split across pages 142 and 143 with the Latin text and apparatus printed between**. I verified by hand that the two halves join exactly as the chunk prints them. **Four fabricated HIGHs against the cleanest-quoting chunk in the set, avoided.**

## Confirmations of the findings I did report

**H1 confirmed three ways.** (1) My body-text index located Pontius §10 and binned it to section 10, inside the chunk's cited range. (2) **Independently of the pipeline**, I printed the raw XML around the passage and read `<p class="c20" id="iv.iii-p25">` directly: ordinary body paragraph, no `<note>`, no Argument. (3) A corpus-wide search of every `lpc` build document for "household of faith", "Tobias", "overflowing works" and "ministrations are constantly" returns **nothing** — no upstream document in this world has ever quoted Pontius §10, consistent with its never having been opened here.

**H2 confirmed two ways.** Both loci matched by the harness in body mode, then **printed from the raw XML with markup intact** — `iv.iv.xx-p7` for "(spiritual)" and the Ep. XXI paragraph for "ordered to be put to death" — confirming both are body text, outside `<note>` and outside any Argument. Additionally, "killed by death" was searched across the **whole** volume including notes: zero occurrences.

**M1 confirmed two ways.** Registry row 171's own Round-14 verification, and my own independent check of `cic/texts`: `npnf106` carries exactly 97 sermon entries, and no Augustine *Sermones ad populum* collection is vendored in any language.

**M2 confirmed by direct read** of each of Doc_01's, Doc_02's and Doc_03's own Status lines, which state "Approved to proceed (self-disposed …)" in each case.

**M3 confirmed by reading *Ep.* XXXIII whole** (all four paragraphs), not by a keyword search — the absence of election material is an absence, and an absence cannot be confirmed by a search that returns nothing. I then located the letters that *do* carry it (XXXII, LXVII) and quoted them.

**M4 confirmed by execution.** Every claim in M4 was reproduced by mutating the deliverables in a scratch copy and running the generator: the §3 Confidence contradiction emitted normally; the "Augustine" keyword flipped the phase; the disclaimed row 28 halted the run; the legal Markdown variant produced garbage §5 rows under an unchanged "Not a placeholder."

**§6 item 2's *Acta* claim confirmed two ways:** the Latin *Acta* located at line 41413 of the Hartel Pars III file with the trial dialogue at 41522, and a corpus-wide search for the proconsul's name returning only Latin, French and German witnesses — no English *Acta* anywhere.

**Doc_09 §7's own word count (564) recomputed independently** and found exact.

## False premises in the review brief, reported as directed

1. **"Nine halting guards."** The script has **twelve** halting sites; its own generated masthead enumerates **nine** conditions and calls them "**the eight** lessons." The brief's number appears in neither the script nor the index.
2. **"Two are declined as unread-at-source."** §6 lists **four** candidates, three of them declined on unread or unopened grounds — and **one of the two the brief names is not unread at all** (M1). Doc_09's own §4 makes the same two-not-four error (L7), so the brief inherited it faithfully.
3. **"Row 204 vendors Perpetua."** True, and incomplete in a way that matters: row 204 marks it **Excluded (both portions)**, and Perpetua's operative ground is not the date but **a project-lead ruling of 2026-08-26 assigning the text to `tertullian-s-voice`** (L9).
4. **"Is that reasoning sound against Doc_01's boundary?"** — the brief poses this as open. **It is not open, and the answer is yes:** Registry row 122 already states that Augustine's Sermons 280–281 are "native, in-boundary preaching material," and Doc_02 §6 says the same. Doc_09 §6's argument is not a novel claim needing defence; it is the Registry's existing position. What defeats the candidate is availability.
5. **`lpcstory004` "claims to have avoided exactly this trap — verify that claim."** Verified, and true in every particular.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH · 8 MEDIUM · 12 LOW · 5 COSMETIC.**

**Adequate to proceed to Doc_10 after one fix pass**, with **H1 blocking** until Pontius §10 is read, because `lpcstory002`'s Usage Guidance is a deployable instruction to tell a participant something untrue about this world's own record.

**What I tested hardest:** all 74 quotations, traced to work, note-status and Argument-status; the two documented failure modes; the tier and band assignments against CF's own Part II text; the §6 declination grounds against the Registry and the vendored corpus; and the generator, reproduced and mutated. **What I tested least hard:** the Retrieve-When / Do-Not-Retrieve-When judgements as pastoral judgements, and Doc_08's forces analysis, which I took as given.

**Graded honestly in both directions.** The selection is sound, the sourcing discipline is real, and the two hardest tier calls in the set — `lpcstory006` against `lpcstory007` — are correct and well argued. The defects are in the claims made *about* the sources, not in the stories drawn *from* them.

*Simulated review — informational only, not an Article 31 substitute.*
