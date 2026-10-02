# Doc_02 / Source Registry — Independent Adversarial Review, Round 1

**Documents reviewed:** `witt_Doc_02_Source_Ecology.md` (Revision 0) and `witt_Source_Registry.md` (Revision 0, 88 rows), reviewed together as the two co-equal Step 2 outputs.

**Reviewer:** independent adversarial reviewer, no drafting context. Every checkable claim was checked against the primary source, the governing template, the Framework/Forces `.docx` files, the census JSON, the corpus-map YAML, or the open web — not against the documents' own citations.

**Method note.** I did not sample lightly. Roughly 140 distinct quotation/line citations were re-located in the ten vendored files (by `grep -n`, not by line arithmetic, after an early pass showed `sed` offsets can mislead by ±1); the Registry's summary statistics were recomputed by script from the live table; the Framework's Part II paragraph range and the Forces Framework §4 Step 2 block were read directly from the `.docx` files; three of the Confidence-C "prior knowledge, not web-verified" items were re-verified by independent web search.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**10 SUBSTANTIAL findings, 13 COSMETIC.** The evidentiary spine of both documents is genuinely strong — stronger than Doc_01's first draft by a wide margin — but three findings are in the project's own named recurring defect classes (a spliced quotation that inverts its source, an asserted absence the vendored library refutes on its own page, and a "could not locate" that a single `grep` locates), and four more are boundary/licensing judgments that do not survive being pressed.

---

## SUBSTANTIAL FINDINGS

### S1 — A quotation spliced backwards: St. Lawrence made the patron against pestilence (Doc_02 §6; Registry R25)

**Doc_02 §6** writes:

> saints' cults named by Luther as they functioned ("if he dreaded pestilence, he… chose St. Lawrence as his helper in need," LC line 454)

**What the Large Catechism actually says at that line** (`luther_large-catechism_bente-dau1921.txt`, 452–456):

> "If any one had toothache, he fasted and honored St. Apollonia…; **if he was afraid of fire, he chose St. Lawrence as his helper in need; if he dreaded pestilence, he made a vow to St. Sebastian or Rochio**, and a countless number of such abominations"

Line 454 reads, in full: `chose St. Lawrence as his helper in need; if he dreaded pestilence, he`. The drafting has taken a single OCR-clean line, cut it at the semicolon, and rejoined the two halves in reverse order behind an ellipsis — producing a sentence Luther did not write and a fact he did not state. Lawrence is the helper against **fire**; Sebastian and Rochus against **pestilence**. The same sentence in Doc_02 then correctly quotes the Apology's "Sebastian keeps off pestilence" (Apology 7595, verified), so the document contradicts itself inside one parenthesis.

**The Registry carries the same defect.** R25's Verification Note records `"St. Lawrence… pestilence" (454) verified` — the elided form is what was "verified," so the row certifies the error rather than catching it.

This is the exact failure class CLAUDE.md names ("misattributed and mis-transcribed quotes have been a real, recurring defect here") and that Doc_01 Round 1 caught at S4. Fix both the sentence and R25's note; the underlying point (saints named by their functional specialisms) survives intact and is better made with the correct pairing.

### S2 — "Could not locate" the Cole appendix heading: it is at line 15209, in clean OCR, inside the range searched (Doc_02 §0 and §16 item 6; Registry R35)

**Doc_02 §0** states the Cole *Bondage* volume appends a letter to Amsdorf "whose own heading this pass could not locate in the OCR noise between lines 15185 and 16060." **§16 item 6** carries this forward as a new open item ("identify the appended Amsdorf letter's heading and date"), and **R35** records it as unlocated.

**What is actually at those lines:**

```
15199  FINIS.
15201  - •■ -'■ '' " ' 1525!
15209  MARTIN LUTHER'S JUDGMENT
15214  OF
15219  ERASMUS OF ROTTERDAM.
15223  TP A CERTAIN FRIEND.,
```

The heading is inside the stated search range, is not OCR-degraded beyond a single transposed character (`TP` for `TO`), and is findable by `grep -n "ERASMUS OF ROTTERDAM"`. The date of the preceding work (1525) is printed at 15201. So: an open item was created, and a claimed inability to find something was asserted, where a one-line search resolves it. R35's Confidence (B) and its "Heading and date not located" note both need correcting; §16 item 6 should be struck, not narrowed.

This matters beyond the single row: the document's own credibility rests on the header claim that every asserted absence "was tested by search across all ten files." One that plainly was not weakens the rest.

### S3 — An asserted absence the vendored Apology refutes on its own page (Doc_02 §1.3)

**Doc_02 §1.3** states:

> The Confutation itself was never handed to the Lutheran party in writing — a **[Widely Accepted]** point from the secondary literature, **not from the vendored text, which does not say so.**

**The vendored Apology says so.** `melanchthon_apology-augsburg-confession_bente-dau1921.txt`, lines 8441–8449:

> "In such passages we can see what design the adversaries had in writing the *Confutation*. They judged that the ignorant would be thus most easily excited… Thus they frequently cite falsely the judgment of the Church. **Because they are not ignorant of this, they were unwilling to exhibit to us a copy of their Apology, lest this falsehood and these reproaches might be exposed.**"

("their Apology" here is the adversaries' own defence — the paragraph is about the Confutation by name, two sentences earlier.) This is the only such statement in the file, and it is directly on point.

Two consequences. First, this is the same defect class Doc_01 Round 1 found twice (S10, S11: "two asserted absences that the vendored library itself directly refutes"), recurring in a document whose opening discipline note promises it was built against that record. Second, the confidence tag is wrong in the conservative direction: the claim can be made from the movement's own primary text in hand — **[Documented]** as Melanchthon's own complaint — rather than borrowed from secondary literature at **[Widely Accepted]**. R39's Verification Note should carry the 8448 locus.

### S4 — Registry Template Checkpoint violated: sources named in support of specific claims with no Registry row (Doc_02 §15 item 10, §12.3, §9)

The Template's one hard gate reads: *"Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row… if a claim in Doc_02 cannot be traced to a Registry entry, Step 2 is not finished."*

Three violations, one of them load-bearing:

1. **§15 item 10 (Karlstadt).** "now sourced from secondary literature located this session (**Britannica, GAMEO, the Karlstadt-Edition biography**): Orlamünde 1523, expulsion from Saxony 1524, shelter in Luther's house 1525, Switzerland from 1529, Basel professorship 1534–1541, death of plague 1541 **[Widely Accepted]**." Three named sources, six dated claims, and an explicit **raising of an approved document's confidence tag** from Inferential/Thin to Widely Accepted — and `grep -i "britannica\|gameo\|karlstadt-edition"` over the Registry returns nothing. (The underlying chronology is, for what it is worth, historically correct. That is not the point; the point is that the Registry is supposed to be the thing that makes it checkable.)
2. **§12.3.** "Wallmann's view that it was largely ignored in the eighteenth and nineteenth centuries" — a named scholar's named position, supporting a **[Contested]** determination, with no row. It is reported *via* R83, but the row does not name him and a reader cannot trace it.
3. **§9.** "Melanchthon's 1546 funeral oration and preface-biography are not vendored" — named in support of the claim that no in-window *Vita* of Luther exists. Four comparable named absences (*Formula Missae* R59, the German NT R60, *Monastic Vows* R61, Philadelphia vols. IV–VI R62) each got a row; this one did not. The inconsistency, not the omission alone, is the defect.

### S5 — §3.4 claims five-dimension Narrative Source Author Gravity entries; four of six entries have none

**Doc_02 §3.4** opens: "the following are given their own five-dimension entries because they *narrate* this world from outside or after it."

Framework para 275 (read directly) requires exactly that: *"These figures require their own Author Gravity entries applying all five dimensions (including transmission history)."*

What §3.4 actually delivers:

| Entry | Five dimensions applied? |
|---|---|
| Philadelphia introducers [R63] | Yes — Visibility / Representativeness / Influence / Limitations / Transmission all labelled |
| Aurifaber & Lauterbach [R32] | Yes — all five labelled |
| Captain Henry Bell [R33] | No — a narrative summary plus a boundary ruling |
| Leonard Woolsey Bacon [R66] | No — "narrates through quotation" plus a comparandum warning |
| Henry Morley [R67] and Henry Cole [R68] | No — "see §2 items 5–6" |

Bacon and Morley are not marginal: Bacon supplies the entire hymn chronology, the Walter and Spangenberg testimonies, and the Speratus anecdote §10 tiers; Morley's selection rule is the basis on which §12.3 argues that the Table Talk's mildness about Jews is "a selection effect." Both need real entries. The framing sentence is a claim of compliance the section does not meet.

### S6 — Wikipedia-derived content tagged [Documented], and quoted phrases from texts the project cannot see (Doc_02 §12.3, §12.4; Registry R83)

The tertiary labelling is *partly* well handled — R83 names Wikipedia explicitly, §17's log discloses "two encyclopedia articles… labeled as tertiary," and the "smite, slay and stab" formula is correctly quarantined as unverified. Three things still fail:

1. **Doc_02's body never names Wikipedia.** §12.3 and §12.4 say "the reference article" five times. A reader of Doc_02 alone — which is what a later step or a Level-3 disclosure will read — cannot tell that the seven-measures list and the tract's content summary come from a tertiary encyclopedia. "The reference article" reads like a designated scholarly reference work.
2. **The confidence tag does not match the evidentiary situation.** §12.3: "**[Documented]** in the secondary literature as to the treatise's content." §12.4: "**[Documented]** in the secondary literature as to content." Article 17's *Documented* is "multiple independent sources with no serious scholarly dispute." The actual basis is one tertiary article per text, with Kaufmann and Blickle named but explicitly unread. **[Widely Accepted]** is the honest tier here, and the phrase "in the secondary literature" is doing work the sourcing does not support.
3. **Quotation marks around unverified phrases.** §12.4 puts quotation marks on "three terrible sins" and "may be a true martyr" — phrases from a primary text the project cannot open, reaching the document through the same tertiary article that supplied "smite, slay and stab," which the same paragraph correctly refuses to quote. Either all three carry the caveat or none is quoted.

### S7 — The Zell exclusion is argued from a census that lists her as one of this world's own named voices, and applies a test Grumbach is never put to (Doc_02 §15 item 4; Registry R54, R55)

The *facts* of the Zell argument check out. Strasbourg did present the Tetrapolitan Confession at Augsburg in 1530, did subscribe the AC only in 1532 for Schmalkaldic League purposes under Bucer, and did reach the Wittenberg Concord in 1536; Zell's corpus does run 1524–1558; her defence of Schwenckfeld is real. The *argument built on them* has two holes.

**(a) The census says the opposite, and Doc_02 does not disclose that it is overriding it.** Doc_02 and R55 both cite the census's "wider evangelical orbit" placement note as support for exclusion. That note is real. But the same census entry (`lutheran-wittenberg-and-its-congregations`, read directly) lists among **this world's five `voices`**:

> "Katharina Schütz Zell — Strasbourg pastor's wife who published devotional writing, hymn collections and open letters in her own name"

and its `statusDescription` calls the world "rich in both directions… **including women's voices in verified modern editions (Argula von Grumbach, Katharina Zell)**." Excluding her may still be right, but Doc_02 quotes the one census sentence that helps and is silent about the two that do not. R88 claims the census entry was "read directly this session," so this is selective use of a source the Registry certifies as fully read.

**(b) Two different boundary tests, one per woman.** Grumbach is Native because *her 1523 subject matter* is the Wittenberg cause, with geography (Bavaria) explicitly set aside as "outside Saxony but inside the movement's own reach." Zell is Excluded because of *where Strasbourg ended up confessionally in 1530–36* and *whose theology she later defended*. Apply Grumbach's test to Zell's 1524 Kentzingen letter and the answer flips; apply Zell's test to Grumbach and it is never run. The Registry half-concedes this ("The one item with a plausible Native claim… would need its own argued row"), which is the right instinct — but a comparandum note that identifies the strongest counter-case and then declines to argue it is not a settled determination. The two rows need to be decided against **one** stated test, and the test needs to be named.

Related and smaller: R54's Native determination rests on content the row itself marks "prior knowledge," unverified — yet R54 is not in the summary's list of rows flagged for second-opinion review, while R50 (a far lighter claim) is.

### S8 — No Named Comparandum row for the wider Luther corpus — the exact failure the Template exists to prevent, and which the Gallic precedent this document cites does cover

The Template's own account of why the Registry exists is the Alexandria/Theon defect: vivid imagery "traced to Gregory of Nyssa, a different world's own source, borrowed unmarked into the Representative's generated content," and the mechanism is a Named Comparandum row that says *never reach for this*.

The Gallic Registry — which Doc_02 §1.3 correctly cites as its precedent for the "(context)" handling (verified: Gallic rows 14–16 do exactly that) — also carries **row 35, "The rest of Augustine's corpus… Excluded / Named Comparandum,"** with the note: *"A Representative for a world whose defining argument is grace and human effort, generated from a model trained on Augustine's own famous corpus, is at direct risk of reaching, unconstrained, for Augustine's own vivid language elsewhere."*

This world has a far larger version of that problem — the most quoted Christian author in the training distribution, with the library holding a small, early, heavily-selected slice of him — and the Registry has no equivalent row. Doc_02 §16 item 7 correctly identifies two specific instances ("Here I stand," "smite, slay and stab") and R69 de-licenses one of them *inside a Native row*. Neither is a Boundary-Status-level bar, and neither generalises. The 1543 treatise, the 1525 tract, "sin boldly," the tower experience, *Freedom of a Christian*'s famous paradox in its non-vendored renderings, the Genesis lectures — all sit outside the library and inside the model. One Excluded / Named Comparandum row covering "Luther material beyond rows R1–R35" would close this; nothing currently does.

### S9 — The Marburg Articles (R56) are marked "(context)" under a definition that does not fit them

The Registry's Conventions paragraph defines the marker precisely: *"**(context)** rows — opponent texts this world's own writings directly answered."* Seven rows carry it (verified by script: R36, R39, R40, R41, R42, R43, R56).

Six fit. **R56 does not.** The Marburg Articles of 3 October 1529 were **signed by Luther and Melanchthon** — the row's own Licensed For says so: "the Eucharistic break stated in a document **this world's own leaders signed**." That is a partly-native primary text of this world, not an opponent text this world answered. Marking it "(context)" licenses it only for "the opponent's position as this world's own texts represent it," which is the wrong licence for a document whose Lutheran signatures are the point. Meanwhile Zwingli's own report (R57) is correctly Excluded as the Reformed side's account. The effect is that this world's single best unvendored lead on its own most-disclosed silence (Doc_01 open item 1) is pre-emptively down-licensed by a category error.

### S10 — The Registry silently redefines the Template's Confidence tiers, then does not follow its own redefinition

Template (read directly): **B** = "Specific work/locus named, not independently re-checked this session." **C** = "Tied to a real author/work, no specific locus pinpointed."

Registry Conventions: "**'B' means the specific work and edition are named and their existence was verified this session by search**, but the text was not read; **'C' means tied to a real author/work from prior knowledge with no locus and no independent check this session**."

That is a different B (it adds a this-session verification requirement the Template does not impose) and a different C. The Registry then applies the Template's B, not its own: R3–R6 and R10–R13 are B on the basis of a corpus-map locus and a contents page, with no "existence verified this session by search" anywhere near them. R35 is B although its Verification Note records four line ranges read directly — the treatment R34 gets as "A (for the three passages read)."

Two problems. A methodology restatement that departs from the governing template without flagging the departure is the kind of quiet change this project escalates rather than absorbs; and a Confidence letter that means one thing in the header and another in the table is not a filter a downstream step can use. Either adopt the Template's definitions verbatim or state the departure as a departure.

---

## COSMETIC FINDINGS

**C1 — "Nine of ten files are Luther; the tenth pair (AC/Apology)…" (§3.1).** Eight of ten are Luther; two are Melanchthon. "Nine… the tenth pair" also does not add up to ten. The word-count figures in the same paragraph are all correct (v1–v3 = 471,515 ≈ "~470,000"; *Bondage* 116,624; LC+SC 52,785; hymns+TT 58,055; AC+Apology 125,737) — only the file count is wrong.

**C2 — "190 hits" for Jewish references across the ten files (§12.3).** Case-sensitive `grep -o "Jew"` returns **198** occurrences across 209 lines. A stated count that does not reproduce.

**C3 — A scatter of ±1–2 line offsets.** Most citations are exact; these are not: §12.1's "lay aside false chastity and take upon them the true chastity of wedlock" is cited v3 20634–20635, actual 20632–20633; §8 item 2's "mid-day" is cited v1 473, actual 474 (473 ends "It was not night,"); R20's AC-XVI footnote is cited 11776, actual 11775; R20's dedication heading 11804, actual 11803; R25's "ma-servants" range starts a line early. None changes a meaning; the pattern is worth a sweep because the documents rest their credibility on locus precision.

**C4 — "the secularization of the Teutonic Order into ducal Prussia (1525), narrated by Lambert (v3 lines 20784–20790)" (§4; R24 "secularization and marriage 1525–26").** The cited passage gives no 1525 date: it narrates the conversion to a duchy without a year and dates the marriage to "July 1, 1526." The 1525 is the builder's, not Lambert's, and is presented as the editor's.

**C5 — R65 cites the wrong region of the Small Catechism.** "SC 19–24 ('under continuous revision')" — lines 19–24 are *this project's own intake header* (the Rights and Source Collection block). The translator's note is at SC 38–40. A row whose Confidence is "A — read directly this session at the cited line" citing the project's own front matter for a translator's words.

**C6 — The LW 47 Bertram/Sherman "discrepancy" is not one (R49).** G1 records "trans. Bertram, ed. Sherman"; R49 says "the reference article credits Sherman — minor discrepancy, not resolved." Franklin Sherman edited *Luther's Works* vol. 47; Martin H. Bertram translated the treatise within it. The two facts are complementary and G1 already states both. Nothing asserted anywhere in Doc_02 or the Registry depends on it. It is inert, as suspected — but it should be closed as a non-discrepancy rather than left standing as an unresolved item, because an open item that cannot be resolved (there being nothing to resolve) is noise in `Open_Gaps_Tracking.md`.

**C7 — "almost certainly… stated here from prior knowledge [Inferential/Thin]" (§6, woodcuts; R86).** The rhetoric and the tag point opposite ways. On check, the tag is the one that is wrong: the 1523 joint pamphlet *Deutung der zwo grewlichen Figuren, Bapstesel zu Rom und Munchkalbs zu Freyberg*, with Cranach woodcuts, has Melanchthon on the Papal Ass and **Luther on the Monk Calf** — which is precisely Cole's "That by Luther, of Monkery." The identification is solid, not thin; the one loose end is that Cole calls Melanchthon's figure "the Whore of Babylon" rather than the Papal Ass, which is a nineteenth-century gloss, not a different image. Raise to **[Widely Accepted]** with the Cranach/1523 details, or drop "almost certainly."

**C8 — A two-fragment splice in §2 item 1.** "prepared 'with especial reference to' the 'approaching jubilee of the Reformation in 1917'". The text (v1 168–175) says the volumes were prepared with especial reference to *the discussions which the jubilee will occasion*, not to the jubilee. Both fragments are accurate; their join is not what the source says. Minor, but it is the same operation as S1 at a harmless scale — worth noting because it suggests a habit rather than a slip.

**C9 — "Sacramentarians… twice in the Philadelphia editors' commentary" (§13).** There is a third occurrence in v1, at line 15611, in the volume index. The substantive claim ("in Luther's own voice exactly once") is correct and verified. A document that stakes §13 on exhaustive search should account for all hits.

**C10 — The Large Catechism's own naming of the opponent is not recorded (§13, §12.5).** §13 says the 1529 catechisms "state the Lutheran position without naming the opponent," and §3.3 lists the Anabaptists as visible only through the AC's five condemnations. The Large Catechism, in Luther's own voice, attacks "enthusiasts" (LC 3277), "new spirits" twice in the baptism section (3841, 3916), and "the prating of nearly all the fanatical spirits" and "all fanatics" in the Sacrament section (4069, 4095). This does not overturn §13's finding — the silence really is generic rather than suppressive, and these are generic labels — it *supports* it with in-library, in-Luther's-voice evidence the section does not use. §12.5's "never heard" for the Anabaptists should note them.

**C11 — R87 is a Native row that licenses nothing.** The Template: "A Native source with nothing named here is not yet usable downstream." R87 is "Period lexicon — **none vendored**," Type L, Confidence D, Native, Licensed For = "Doc_03's German-term work, **once a real lexicon row exists**." A placeholder for a non-source, occupying a Native row. Recording the gap is right; doing it as a Native row with a conditional licence is not what the field is for.

**C12 — Four of the seven "flagged for second-opinion review" rows carry no flag.** The summary lists R48, R49, R50, R52, R72, R82, R86. Only R72, R82 and R86 carry "**Flagged for second-opinion review**" in their own Verification Notes. A reviewer reading the table row by row — which is how a Level-3 disclosure would be read — sees no flag on four of them.

**C13 — "their introductions… are the library's *only* connected narrative of events" (§2 item 1)** sits against §3.4, which treats Bacon's and Morley's introductions as narrative sources in their own right, and against Bacon's Introduction, which narrates the hymnals' publication history from 1524 to 1545 and the Worms scene. "the library's fullest connected narrative" would be defensible; "only" is not.

---

## WHAT HELD UP

I went looking hard for the standard failure classes and found the ones above. A great deal more did not break, and this should be on the record with the same specificity as the findings.

**Arithmetic and statistics, exactly.** The recount of 824,716 words reproduces to the word across all ten files, including every per-file figure. The Registry's summary statistics reproduce **exactly** when recomputed by script from the live table: 88 rows, 84 Native / 4 Excluded, the seven "(context)" rows are exactly R36/R39/R40/R41/R42/R43/R56 as listed, Confidence A 47 / B 27 / C 13 / D 1 / E 0, and the Type tallies. The claim that they were "computed from the live table by script, not tallied by hand" is true.

**Registry schema discipline is clean.** Script-checked across all 88 rows: every Native row has a non-empty Licensed For; every Excluded row has an Exclusion Reason and a blank Licensed For; both Named Comparanda carry Comparandum Notes; no Native row carries an Exclusion Reason; and the Boundary column contains *only* Native or Excluded. That last point is not trivial — it is precisely the defect the Gallic Registry's own Round 2 (finding S11) caught in ten rows after a first fix claimed otherwise, and this Registry avoids it and says it ran the check.

**The Gallic precedent is real, not invented.** Doc_02 §1.3 cites the Gallic Registry's handling of Augustine's anti-Massilian treatises. Gallic rows 14, 15 and 16 are Boundary = Native with **(context)** at the head of Licensed For, exactly as described. Given this project's history of invented cross-references to sibling worlds, I checked this expecting to find nothing. It is there.

**The negative searches are true.** "Zwingli" and "Marburg": zero hits across all ten files (checked individually). "Oecolampadius": one hit, v3 14540, in an editorial bibliographic note. "Sacramentarians" in Luther's own voice: once, Cole 16090. The tower-experience absence is exactly as stated — "tower" returns 4721, 7873, 8564 (Siloam, Prov. 18:10, church-towers) and "righteousness of God" returns **zero** in v1. The Small Catechism genuinely has no preface: "preface" and "visitor" both return nothing.

**All four corpus-map findings are correct**, checked against the YAML and the files: the map carries 26 entries; the v1 1539/1545 Prefaces (heading at 250) have none; *That Doctrines of Men Are to Be Rejected* (heading 15816) has none and is swallowed by the Sermons' "~14403-end" locus; the Magnificat (heading 6281) has none and is the work the v3 intake header flagged as unidentifiable; and the map's single Emser entry names only the second and third writings, omitting *To the Leipzig Goat* (14693) — which the volume's own editor confirms at 14466–14469 ("the three writings of Luther herewith given").

**Quotation fidelity is high.** Setting aside S1 and C8, roughly 130 quotations were re-located and re-read at their cited lines and found accurate, including every difficult case: the 1539/1545 prefaces (v1 260–261, 356–357, 365, 390–391, 396–397, 408–409 with the ellipsis correctly standing for footnote marker [5]); Jacobs on the Theses (473–474, 488–491, 498–499); Alveld's seven swords and the "jackanapes" (12283–12300); the *Kurze Form* preface (13182–13183); both Wittenberg Sermons quotations (14677, 14681); von Berlepsch (15834–15841); the Magnificat's household-tasks sentence, correctly attributed to the editor quoting Luther (6396–6397); the Emser "brotherly warning" (14553–14557) and "faithful portrait" (14640–14642); *Karsthans* and the flail (10556–10558, 10586); the 1522 *Exhortation*'s "common man" passage (10666–10671, and it is OCR-clean there as claimed); the Polentz and Spalatin letters (20802–20803, 10525); the LC preface's "louts and scrimps" (92–93) and short preface (241–243, 245–247, 333–336); the SC confession scripts (445–446, 454) and Home Chart (649); all four hymnal prefaces, correctly dated 1525/1542/1543/1545 and correctly located; the Brussels martyrs ballad with Bacon's bracketed date correction (1744–1745, 1759–1760, 1799–1800); *Ein feste Burg* in both languages (3667–3668, 3708) with Bacon's footnote correctly read as *separating* the hymn from the Worms "tiles" saying (856–866); the Table Talk passages (3013–3015, 3100–3102, 3147–3148, 3508–3509, and the household-catechism heading at 2394–2395); Cole's preface, quoting rule, and "Melkncthon's Edition" (186–189, 200–202, 218–227); the three *Bondage* passages with their raw OCR shown honestly in the Registry (759–762, 15139–15142, 16090–16092); the AC preface's Turk clause and council appeal (49–51, 149), the nine signatories (1559–1567, and Doc_02's list of them is correct), and the five Anabaptist condemnations — which I checked fall in Articles **V, IX, XII, XVI, XVII** exactly as §12.5 says; and the Apology's greeting, Campegius address, Article XXIV practice statements and "Sebastian keeps off pestilence" (97, 5915–5916, 8490–8496, 8512–8514, 8531, 7595).

**Framework and Forces compliance is real.** The Forces Framework §4 Step 2 block quoted at §13 is **verbatim exact** against the `.docx` (para 169). Framework Part II is paras 141–275 (Part III opens at 276), as the header states. Every Framework paragraph citation checks: para 184's "not a backstage construction note — it becomes a participant-facing obligation in the encounter" is exact; paras 170–174 are the four asymmetry duties §11 lists; paras 215–221 are the story-tier cross-walk; para 231's "carry formation ecology from the inside of individual lives and teacher-disciple relationships" is exact; para 246's "The ecology existed in material conditions whether or not those conditions are recoverable" is exact. All required Part II subsections are present and substantive — primary/secondary/institutional/liturgical/material/ordinary-participant voices, Author Gravity with transmission history, Source Asymmetry with all five categories and the evidential-versus-ecological distinction, Missing Voices with the Affirmative Duty, Confidence Calibration answering paras 211–213's three questions, Secondary Scholarship with all four identify-items including the synthesis-versus-specialist relationship, Formation Narrative Sources with the per-source evaluation schema, Material Culture with all four assessment categories, the four-tier story table, and an explicit **No Tier 5** statement with a "not tellable from this library" row to prove it is load-bearing.

**Doc_01's three §7 search directions are honoured, and honoured honestly.** The Catholic-responses direction produced §1.3's finding that they exist only in adversarial quotation, with a located English lead. The Marburg direction produced verified zero-hit searches, an explanation of *why* the silence is chronological rather than suppressive, and a named unvendored lead. The congregational-register weighting direction produced the single most creditable sentence in the document: the finding that **G1's weighting went the other way** — all four newly vendored files are founder corpus — stated plainly against the drafting thread's own interest. That is the behaviour this review process exists to produce.

**Three of the four flagged Confidence-C "prior knowledge" items re-verify as correct.** I checked them independently rather than take the flag as sufficient:
- **Kittelson (R72):** "Successes and Failures in the German Reformation: The Report from Strasbourg," *Archiv für Reformationsgeschichte* **73 (1982), pp. 153–175**, DOI 10.14315/arg-1982-jg07 — the Registry's citation is exactly right.
- **Oberman (R82):** *Luther: Man between God and the Devil*, Yale UP **1989**, trans. Eileen Walliser-Schwarzbart, German *Luther: Mensch zwischen Gott und Teufel* **1982** — exactly right.
- **The woodcut identification (R86):** correct, and stronger than its tag (see C7).
- **Bacon 1883 (R27):** the two catalogues Doc_02 names are the right two — Valparaiso University ArchivesSpace and HathiTrust both give *The hymns of Martin Luther, set to their original melodies, with an English version*, ed. Bacon, assisted by Allen, Scribner's, **1883**, issued for the quatercentenary of Luther's birth. The internal evidence ("this Birth-day Edition," hymns 819–820; "the commemorative character of the present edition," 711) is correctly quoted and the inference is sound. The rights-basis upgrade is justified.

**Doc_01 cross-references are sound.** I spot-checked every Doc_01 reference in Doc_02 — §1 and §4 on the 1519–20 treatises, §2.3 on the 1522 unrest, §5 on the worship gap, §7's three pointers, §8.0 on VI.27 and the parish-continuity hypothesis, §8.2 on the Anabaptists, §9 items 1–2, §10's rights flags and word count, and all ten §11 open items against §15's dispositions. None is inverted, none is invented, and §15's ten-item disposition maps one-to-one onto Doc_01 §11. The four sibling census ids cited (VI.2 `the-reformed-cities-zurich-and-geneva`, VI.3 `the-anabaptist-movements`, VI.11 `the-society-of-jesus`, VI.22 `the-tridentine-church`) all resolve correctly in `world-census.json`.

**The escalation check is correctly reasoned** and the refusal to self-dispose is correct. The Zell decision is flagged as the judgment call most deserving review, which is where I found the most to say — the flag was warranted, and the document was right not to treat it as settled.

---

## Recommended disposition

Revise and re-review, with the second round scoped to: S1–S10 and the cosmetic sweep, plus a targeted re-verification of any citation the fix round itself touches. Doc_01's own history is the warning here — five of its Round 2 substantial findings sat inside sentences written to close Round 1 findings.

S1, S2 and S3 should be fixed first and independently confirmed, since each is a claim the documents make *about their own verification discipline* rather than about Wittenberg.
