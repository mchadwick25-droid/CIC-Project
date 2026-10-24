Simulated review — informational only, not an Article 31 substitute.

# Doc_07 full review after change order CO-LPC-1

- **Document:** `Build/worlds/lpc/Doc_07_Integrated_Ecology_Analysis.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `4e7a4bd9`; the file is unchanged since commit `949edbcf`, "lpc change order, part 2", and is the same blob at `a0209b8d`)
- **Round:** 3
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent adversarial review subagent, fresh context (drafted none of the text under review)
- **Drafter:** Sonnet 5.5 drafters for CO-LPC-1 (§1 lines 30 and 32, §2C line 74, §2D line 94, §7 line 234, §8 items 6, 8 and 9), checked by the `lpc` build thread; earlier text by the `lpc` build thread (draft 2026-09-15, Round 1 and Round 2 fix passes 2026-09-15; drafting model not recorded in the log)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** CO-LPC-1 drafters and the `lpc` build thread
- **Date:** 2026-10-23
- **Scope:** full review of Doc_07 in its current state: every substantive claim; quotations re-verified word for word against the vendored files in `cic/texts/` at their structural markers and against the governing documents (CF V7.4 Step 7, Forces Framework V1.1, Completion Standard V1.4 §F); consistency with the 2026-10-23 rulings (D1 to D5, Doc_02 §7, Doc_05 crosswalk, Article 20, lexicon discovery method, liturgical candidates), with OG-28 to OG-51, with Docs 01, 02, 04, 05 and 08, and with the sibling Donatism Doc_07 it quotes; Forces Framework integration; the CO-LPC-1 edits (diff `949edbcf^..949edbcf`). Prior review files read: `Doc07_Round1_Review.md`, `Doc07_Round2_Review.md`, and the Phase L0 checks `L0_Docs03-05-06-07_Carried_Open_Check_2026-09-29.md` and `L0_Docs03-05-06-07_Recheck_2026-10-23.md`.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-1", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md:6875`). That entry records this file as Doc_07's third review under the cap; `roundcount lpc 7 --check-new` reported 2 files on record and PASS before this file was written.
- **Truncation check, method 1:** line and byte count with an end-of-file read: `wc` gives 278 lines and 46,072 bytes; the file was read in full through line 278, which ends on the Disposition's closing sentence ("…awaiting a disposition only the project lead can give.**") followed by a newline, with all ten `## ` headings present in order (§1 to §8, Document Log, Disposition).
- **Truncation check, method 2:** hash comparison against the committed blob: `git hash-object` of the working file, `git rev-parse HEAD:<path>` and `git rev-parse a0209b8d:<path>` all give `da4f223d0e1f9585e702d2e5afe20bc683f5333e`.
- **Method limits:** no web search and no model call. Nothing edited except this file. The CF V7.4 and Forces Framework V1.1 `.docx` files were read from `word/document.xml` with tags stripped. Word counts use the regex `[A-Za-z'’]+`.

---

## What was checked and found sound

- **Quotations re-verified at their structural markers.** *De Lapsis*: "it is the shepherd that is chiefly wounded in the wound of his flock" and "I wail with the wailing, I weep with the weeping" (`anf05_hippolytus-cyprian-caius-novatian.xml` lines 43727–43730, inside `div3 title="On the Lapsed."` from line 43604). Epistle XXXIX: "ancient venom" and "your suffrage and God's judgment" (`anf05` lines 32372–32373, `div3 title="To the People, Concerning Five Schismatic Presbyters of the Faction of Felicissimus."` from line 32346). "Thousands" of certificates (`anf05` line 30204, Epistle XIV; line 29850, Epistle X endnote). The 256 preface, "judging no man, nor rejecting any one from the right of communion, if he should think differently from us" (`anf05` lines 56870–56871, `div3` "The Seventh Council of Carthage" from line 56823). *On Baptism* II.3, "are often corrected by those which follow them, when, by some actual experiment, things are brought to light which were before concealed" (`npnf104` line 11303, `div4 n="3"` from line 11297, outside every `<note>`). Letter CXXVI: "the more venerable and aged men who had come up to me in the apse" and "gathered in front of the steps" (`npnf101` lines 44497 and 44505, `div3 n="CXXVI"` from line 44459). Possidius *Vita* ch. VIII, "under compulsion and constraint" (`possidius_vita-augustini_weiskotten1919.txt` lines 2142–2143, hyphenated across the line, under "CHAPTER VIII" at line 2075). The Forces Framework sentences at §4 and §2H (`ff` text lines 176, 200, 212). The Donatism Doc_07 quotations at §2C (`Build/worlds/don/Doc_07_Integrated_Ecology_Analysis.md` lines 55, 63, 93). Doc_01's "pastoral and sacramental before it is juridical", "episodic" and "one recurring pressure among several…" (`Doc_01` lines 16 and 156).
- **The Possidius ch. VIII bracket** ("the yielding follows persuasion from transmarine and African precedent, and the *Vita* records no election") is accurate to lines 2135–2144.
- **CO-LPC-1's OG-38 edits** at §2D, §7 and §8 item 6 now match Doc_04 §7 items 6 and 8 (Doc_04 lines 212 and 214: both closed 2026-09-15 on `lpc_Gapped_Formation_Precedent.md` §4a and §4b). §2D's restatement of Round 9's argument and its unstated Tensional premise matches Doc_04 line 214.
- **§8 item 8 and item 9** are no longer false: both 2026-09-19 liturgical reads exist in `Review-Artifacts/`, and `Open_Gaps_Tracking.md` exists.
- **The lens spine.** §2A to §2G are Smart's seven, each with its yield stated as a finding; §2H and §2I are the two CiC additions, named as additions; Ethical/Legal and Material are present. This meets Completion Standard V1.4 §F.
- **Forces Framework integration (Step 7)** is present and substantive: §2H carries the three movements the Framework requires of the boundary lens (`ff` line 212), and §4 synthesizes the earlier forces threads rather than starting fresh. Two of §4's claims are wrong on the evidence (P1-1, P1-2), but the integration itself is real.
- **§2E** coercion phases, the 419 Carthage codification and the Apiarius context match Doc_01 and Doc_02; §2F's provincial structure is correct.

---

## Findings

### P1-1 — §4 says *De Mortalitate* addresses a death that "was not a test of faith". Cyprian says the plague is exactly that.

- **Site:** `Doc_07_Integrated_Ecology_Analysis.md:198`: "*De Mortalitate* exists because a bishop had to say something to people dying of something that was not a test of faith", following "the second is the one no discipline can sort."
- **Evidence:** `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`, inside `div3 title="On the Mortality."` (line 46655): §14 (line 46997) "This trial, that now the bowels, relaxed into a constant flux… is profitable as a proof of faith"; §16 (lines 47051–47053) the "pestilence and plague… searches out the righteousness of each one, and examines the minds of the human race". The treatise's central move is to read the plague as a trial of faith.
- **Why it matters:** this is the claim §4 offers as the plague's place in the forces analysis, and it states the opposite of the source. A Representative or the World Profile drawing on it would misrepresent Cyprian. No other `lpc` file carries the phrase (grep), so the fix is local.
- **Fix:** restate on the source: the plague reached believers and unbelievers alike, and Cyprian answered it by reading it as a trial ("a proof of faith", *De Mortalitate* 14, 16), not as a sorting the penitential discipline could act on. Keep "no discipline can sort" only if it is put as the document's own reading, distinct from Cyprian's.

### P1-2 — §4 says the Decian edict created both the lapsed and the confessors. Earlier evidence, at Carthage, contradicts it.

- **Site:** `Doc_07_Integrated_Ecology_Analysis.md:194`: "There were no lapsed before there was a certificate to obtain, and no confessors with a claim on anything before there was an interrogation to survive. **A single imperial administrative demand produced, in one year, two new classes of person inside one congregation**".
- **Evidence:** Tertullian, *On Modesty* XXII (`cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, `div3 title="Of Martyrs, and Their Intercession on Behalf of Scandalous Offenders."` at line 9550) already describes offenders who "seek peace at the hands of" imprisoned confessors at Carthage, decades before 250. The Tertullianic corpus is `Source_Registry.md` row 29, a Named Comparandum. The lapsed also included the *sacrificati*, who fell by sacrificing, not by obtaining a certificate (§2A itself names both the *libellus* and the confessors' certificate as distinct). The same sentence stands at `Doc_05_Ecological_Reconstruction.md:86` and in `scripts/wb_lpc_s25.py:941`.
- **Why it matters:** it is §4's lead forces claim and it is stated as unqualified history. What the evidence supports is narrower: the Decian edict produced lapse and confession on a mass scale inside one congregation in one year, and the certificate as a new way to fall.
- **Fix:** restate to that narrower claim, and name the pre-Decian precedent (Tertullian, *On Modesty* XXII, row 29, comparandum only). Carry the same correction to Doc_05 line 86 and the generator line by the propagation rule.

### P1-3 — CO-LPC-1 changed the wording inside a direct quotation of CF V7.4

- **Site:** `Doc_07_Integrated_Ecology_Analysis.md:32`: *"[A]sk all of Smart’s seven dimensions as the fixed lens spine — always asked, for every world (M4, adopted July 2026),"*.
- **Evidence:** `Build/reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`, tag-stripped text line 681: "(M4, adopted 2026-07-27)". The pre-change-order text had the source's wording (`git show 949edbcf`). Line 5 of Doc_07 still says "adoption of 2026-07-27", and the Decision Log's 2026-09-15 drafting entry (line 1076) quotes it correctly.
- **Why it matters:** a quotation must match its source verbatim. This edit made a correct quotation wrong, apparently to clear an ISO date that `check_live_commentary.py` already classifies as PROTECTED, not as commentary.
- **Fix:** restore "(M4, adopted 2026-07-27)" inside the quotation. If the date must not appear, end the quotation before the parenthesis and paraphrase the rest outside the quotation marks.

### P1-4 — CO-LPC-1 closed the 411 *Gesta* at §2D, §7 and §8 item 6, but §8 item 4 and the Disposition still count it as an open unresolved tension

- **Sites:** `Doc_07_Integrated_Ecology_Analysis.md:248` ("**one unresolved tension** (item 6)", and "**four governance/methodology items** (Doc_04's three plus the translated-corpus discovery-method finding)"); line 276 ("*Unresolved tensions:* **one open** — the 411 *Gesta*"; "*Governance or methodology:* **open, unchanged** — four items"); line 278 ("Five documents in this world are now complete, independently reviewed, and awaiting a disposition only the project lead can give").
- **Evidence:** §8 item 6 (line 250) now says Doc_04 items 6 and 8 "are both closed"; §2D (line 94) and §7 (line 234) agree. Doc_04's own escalation assessment reads "**Unresolved tensions: none open.** §7 Open Items 6 and 8 are closed" and names **two** governance items, not three (`Doc_04_Gravity_Discovery.md:262` and `:266`). The translated-corpus discovery-method finding was ruled for `lpc` on 2026-10-23 (Decision Log, "Lexicon discovery method and matching rule (project lead's ruling, OG-36)"; the fleet-wide form is a System Hub proposal). Line 278 contradicts Doc_07's own Status line (line 7) and line 272: all five documents were Approved to proceed on 2026-09-15 (Decision Log line 1758).
- **Why it matters:** the 2026-09-29 L0 check graded this exact defect P1 (its P1-8: "a reader re-deriving the escalation state from these documents gets the wrong answer"). CO-LPC-1 fixed three sites and left the two that carry the escalation count, so the document now contradicts itself.
- **Fix:** in §8 item 4 and the Disposition's escalation assessment, set unresolved tensions to none from Doc_04 (the *Gesta* is closed as a persistence question), recount governance items against Doc_04 lines 262 and 266 and the OG-36 ruling, and delete or correct line 278's "awaiting a disposition".

### P1-5 — §2F says ordinary presbyteral work is "essentially unattested". A source this document says it read in full attests it.

- **Site:** `Doc_07_Integrated_Ecology_Analysis.md:128`: "the ordinary, non-factional work of a presbyter in this world is essentially unattested, and a Representative should not be built as though the presbyterate were inherently oppositional."
- **Evidence:** Possidius, *Vita* ch. V (`possidius_vita-augustini_weiskotten1919.txt` lines 1925–1930, the close of "CHAPTER V" before "CHAPTER VI" at line 1931): Valerius had Augustine preach in his presence, and "some other presbyters by permission of their bishops began to preach to the people in their presence" (Latin at line 1895, *accepta ab episcopis potestate, presbyteri nonnulli…*). Augustine's own presbyterate (391 to 395/396) is the same kind of evidence. Doc_07 §2C (line 74) says the *Vita* "has been read in full". `lpc_World_Profile.md` already carries the correction ("Possidius chapter V is the counter-instance…").
- **Why it matters:** it is an absence claim contradicted by a vendored primary source, raised as P1-3 by the 2026-09-29 L0 check, confirmed by the 2026-10-23 recheck, and still on disk. `Doc_05` §0.8's crosswalk yield for Social/Institutional ("presbyters as faction") rests on this section.
- **Fix:** restrict the claim to Cyprian's phase and cite *Vita* ch. V for Augustine's; check Doc_05 §0.8's yield line against the corrected text.

### P2-1 — Record-state and process narration that is stale or false

- Document Log line 266, "Round 2 fix pass — All applied", is false: Round 2's NEW-L2, NEW-L4, NEW-L5 and NEW-C2 were not applied (P2-3 below; L0 check 2026-09-29, P1-4). The Log records nothing of CO-LPC-1.
- The Disposition (line 274) gives the review record twice in different words, and keeps drafting narration: "which is the pass this Disposition now records", "A build thread does not score its own work as passing", and line 278's "stated here because the trim that removed it left §1 carrying the *fact*…". §4 (line 192) still says "Doc_08 NOT YET COMPILED", and §8 items 1 to 3 hand off to a Doc_08 that now exists. §8 item 9 is a closed item, not an open one.
- §1 line 30 says item 8 is "now closed" and then "No other open finding…", which reads as if item 8 were open.
- **Fix:** correct the Log line; state the review record once; remove the narration, as CO-LPC-1 did for Docs 05, 06 and 08; mark §4's status line and §8 items 1 to 3 as consumed; drop §8 item 9; reword line 30's "other open finding".

### P2-2 — Governing citation, naming choice and length figures

- §1 (line 32) cites `CiC_World_Build_Completion_Standard_V1.3.md` §F. The current file is V1.4 (`Build/reference/method/CiC_World_Build_Completion_Standard_V1.4.md`), whose §F names Doc_07 as carrying the spine. The dimension-naming choice §F asks to be settled per document is not stated.
- §1 (line 11) says "about 6,650 prose words"; §8 item 10 (line 254) says "about 12% over" 6,000. The regex count gives 6,423 words before the Document Log and 6,932 for the whole file. 6,423 is about 7% over; 6,650 would be about 11%. OG-37 carries this.
- **Fix:** cite V1.4 §F; state the naming choice in one line; give one measured figure with its rule at both sites.

### P2-3 — Round 2's four unapplied findings remain

- NEW-L2: line 114, "the wider one holds even where the primacy question is not live", still inverts Doc_01 §7 (Round 2 review, line 162).
- NEW-L4: line 138 prints *ad nostra subsellia* from an NPNF endnote (`npnf101` line 44490, `<note n="2418">`) as if it were the letter's text. The Latin is genuine: `augustine_epistulae-124-184a-lat_goldbacher-csel44.txt` lines 467–468 (Letter CXXVI), *ad nostra subsellia relicta turba redieram*. Cite Goldbacher.
- NEW-L5: §7 lacks the template's "What external scholarly review should focus on" element. §2A's rite-generates-doctrine finding and §5's "three descriptions of one mechanism" are the obvious candidates.
- NEW-C2: line 136, "two recalled-from-field-knowledge secondary rows"; Doc_02 §9 item 3 (line 135) flags rows 34–35 and 46–47, four rows.

### P2-4 — Smaller factual and consistency points

- §2H (line 152): "A century and a third later, Augustine argues at book length…". From the 256 council to *On Baptism* (c. 400–401) is about 145 years. The force record's own split (CO-LPC-1: "a century and a third" for 258 to 391, "a century and a half" for Augustine's later work) fits "about a century and a half" here.
- §2C (line 74): "roughly 308,000 words of sermons" is the 97 NPNF sermons only (`Source_Registry.md` row 19). After D1 the world holds all of Augustine's sermons, Maurist 1 to 396 plus the later finds (Doc_02 line 13). Say "in the 97 translated sermons alone"; the ratio argument only gets stronger.
- §3A (line 176): "The 133-year documentary silence" does not carry Doc_02 §7 as restated on the project lead's ruling of 2026-10-23: the silence is of an ordinary-pastoral voice within this world; Optatus (rows 27, 64, 300) and other rows do date from the gap. Use Doc_02 §7's test.
- §2F (line 124) cites *Vita* ch. VIII twice in a row (left open in the Decision Log, line 1834).
- §8 item 8 (line 252) cites "`lpc_Decision_Log.md`, October 2026"; name the entry ("Liturgical-read lexicon candidates: folded into the sermon sweep", 2026-10-23). Its "go into the sermon sweep" compresses the ruling, which adds the candidates *with* the liturgical terms the sweep yields, in one Doc_06 change order.
- §2D (line 88) gives "1,798 raw occurrences" without a matching rule. When Doc_03's counts are restated under the OG-36 ruling, carry the stated rule and the note-free figure here.

---

## Outside this document (not counted)

- `Doc_02_Source_Ecology.md` line 122 (§7) ends mid-sentence: "…are not preaching to a congregation. The" followed by the §8 heading. This looks like a truncated CO-LPC-1 edit. It belongs to the Doc_02 review and the build thread.
- `Doc_05_Ecological_Reconstruction.md:86` carries P1-2's sentence; `Doc_08_Forces_Document.md:23` still says no Registry row dates from within the interval, which the 2026-10-23 Doc_02 §7 ruling found false.

---

## Is Doc_07 doing its stage's job?

Yes, on structure and on most of its substance. It asks the full M4 spine, states thin yields as findings, applies the optional lenses on evidence, integrates forces at §2H and §4, and hands off to Doc_08. CO-LPC-1's closure of Doc_04 items 6 and 8 is correct where it was applied. Five findings are substantial. Two are historical errors in §4 against vendored primary sources. One is a quotation CO-LPC-1 made wrong. One is an escalation count CO-LPC-1 left contradicting its own edit. One is a carried absence claim a read source refutes. Each is correctable inside the existing rulings. This is Doc_07's third review file, so these findings go to the project lead; no further review file follows without a Cap ruling.

VERDICT: Substantial revision required
