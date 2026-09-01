# Source Registry — Independent Review, Round 2

**Reviewed document:** `cappadocian_Source_Registry.md`, second pass (112 rows, revised from Round 1's 99), 2026-08-31.
**Reviewer:** independent Opus-tier agent, fresh context, no prior involvement in drafting.
**Method:** read the Registry in full, the governing template, `cappadocian_Doc_02_Source_Ecology.md`, `cappadocian_Doc_01_World_Identification.md`, `cic/texts/README.md`, and `CAPPADOCIAN_BUILD_LEDGER.md` §9. Checked Round 1's specific fixes rather than trusting the revision's own claim that they landed.

This file is the review's verbatim output, preserved as the actual review artifact per this project's build-cycle discipline. Row numbers below refer to the 112-row numbering in effect at the time of this review (before Round 3's further renumbering to 116 rows).

---

## Verdict

**The revision landed most of round 1's substantive fixes, but its central claim about itself is false.** The living-document log (line 222) asserts: *"every 'row N' cross-reference in the document checked against its actual target's content."* It was not. I found **eight wrong row-number targets** the post-edit audit missed, four of them stacked in a single row, plus three wrong section pointers, two table-breaking formatting defects, a residual confidence-tier miscalibration that contradicts the Registry's own newly-written rule, and three more Doc_02-named sources with no row. This is not ready for disposition.

The good news: the specific things you asked me to verify as fixed **are** fixed, and the renumbering did **not** corrupt any historical number.

---

## Confirmed fixed (verified, not trusted)

- **Numbering integrity is clean.** 112 rows, IDs 1–112, no gaps, no duplicates (mechanically checked).
- **No renumbering corruption of historical numbers.** Every `Ep./Epp.`, canon, CTh, and HE citation in the Registry matches Doc_02 verbatim. Specifically, **Epp. 101, 102, 202** appear twice (rows 31 and 39) and are correct and consistent in both places; the claimed "102, 103" artifact is gone. I swept every integer in the 81–111 range: the only historical ones are 101 and 102, both correct. Everything else in that range is a row ID.
- **Philocalia (row 81):** exists; **Confidence B, not A** — correct, `cic/texts/README.md` shows `origen_philocalia_lewis1911.txt` added 2026-08-21 for the Alexandria world. The Boundary reasoning (Native on the *compiling act*, not Origen's underlying content) is coherent under the template and is independently supported by the template's "was this source actually used/inherited by this world" test plus Doc_01 §2's Origen-via-Caesarea-Maritima channel.
- **Eupsychius (row 83):** the fabricated-adjacent homily claim is gone; the row title now reads "no homily attested" and the note explains the correction. Clean.
- **Basil Ep. 8 (row 26):** now Native, with the correct template reasoning.
- **Homoian imperial acts (row 64):** Exclusion Reason now Named Comparandum, with a real Comparandum Note.
- **Part F:** all ten schema columns restored on every row.
- **Rows 27, 56, 73** all now carry a Licensed For target.
- **Confidence-A discipline holds.** All nine A rows map to files vendored 2026-08-30/31 per `CAPPADOCIAN_BUILD_LEDGER.md` §9; every A row's verification detail (footnote counts, chapter ranges, TOC contents, Loeb pagination, Araxius, the Padelford translator caveat) matches `cic/texts/README.md` exactly. No fabrication anywhere in the A rows.
- Round 1's nine missing sources all have rows (Armenian literature with a qualification — see below).

---

## Must-fix

**1. Row 41 — four wrong cross-reference targets in one cell.** The note reads: *"Does NOT include Ad Graecos (row 51), the Life of Macrina (row 47), or the Song of Songs/Ecclesiastes/Beatitudes/Lord's Prayer homilies (row 48) or the Theodore the Recruit homily (row 50)."* Actual targets: row 51 = *Life of Gregory Thaumaturgus*; row 47 = *On the Making of Man*; row 48 = *Life of Macrina*; row 50 = *On Virginity*. Correct numbers: **Ad Graecos = 54, Life of Macrina = 48, the four homily sets = 52, Theodore the Recruit = 53.** The offsets are mixed (−3, −1, −4, −3), i.e. stale pre-insertion numbers. Row 41 is not on the log's list of eight rows the post-edit audit says it corrected — it was simply missed.

**2. Row 16 — "the martyr-homily row (22)"** → row 22 is **Morison's 1912 study**. Should be **row 20** (Basil's martyr homilies on the Forty, Gordius, Julitta, Mamas). Note this reference uses the form `row (22)` rather than `row 22`, which is presumably why the revision's own grep-based audit didn't see it — it is the document's only parenthesized row reference.

**3. Row 79 — "independently well attested via Van Dam (row 93)"** → row 93 is **Susanna Elm**. Van Dam is **row 95**. (Row 95's reciprocal pointer back to row 79 is correct, so this is one-directional.)

**4. Row 32 — "matching the treatment already given those other named orations (rows 34–37)."** The sentence's own list is the Theological Orations, the funeral orations, and Oration 2. Row 36 is *De vita sua* and the poems; row 37 is Nazianzen's **will** — neither is an oration — while **row 38, the funeral orations**, is excluded from the range. Correct target: **rows 34, 35, and 38**.

**5. Row 82 — wrong Doc_02 subsection.** Licensed For cites *"§6.3's against-the-grain evidence of a woman's formation-agency."* §6.3 is **The enslaved**; Emmelia's relic acquisition is named in **§6.1 (Women)**. Every other §6.x pointer in the Registry (rows 7, 8, 9, 11, 18, 19, 37, 38, 39, 52, 60, 70) checks out; this is the only one wrong.

**6. Row 28 — wrong Doc_01 section.** Licensed For cites *"Basil's death year 377 (Doc_01 §4a's chronology…)."* Doc_01 §4a is the six-question separation test and says nothing about Basil's death date. The dependent chronology (Macrina's death computed from Basil's) is in **Doc_01 §1**'s ending-boundary paragraph — which the row's own Verification Note cites correctly. Fix the Licensed For to §1.

**7. Row 81 — wrong Doc_02 section.** *"Doc_02 §1.1/§5 carries the live Contested status."* The Philocalia appears in Doc_02 only at **§5 debate (5)** and **§9**; it is not in §1.1. Fix to §5/§9 (Doc_01 §2 is already cited correctly).

**8. Row 24 — a scholar's first name is wrong and hedged.** *"Bronwen/Mark DelCogliano &amp; Andrew Radde-Gallwitz."* The translator is **Mark DelCogliano**; there is no Bronwen DelCogliano (Bronwen Neil is a different patristics scholar). Doc_02 §1.1 gives surnames only, so the first name was supplied from model knowledge and then hedged with a slash — in a document whose entire discipline is attribution accuracy. Delete "Bronwen/".

**9. Row 71 breaks the markdown table.** The Verification Note contains unescaped pipes: `(|245–|293)`. This splits the row into **12 columns instead of 10**, so the rendered row's Verification Note truncates at "pagination (" and the Comparandum Note and Added values land in the wrong columns. Fix: `\|245–\|293` or "pp. 245–293".

**10. Row 81 is orphaned from the Part C table.** Line 147 is a blank line between the Part C table (ending at row 80) and row 81. A single `| 81 | … |` line with no header/delimiter above it does not render as a table row in GFM — it renders as literal text with visible pipes. Delete the blank line.

**11. Residual Confidence-tier miscalibration — the exact error the revision says it corrected.** The preamble commits to: *"a source with a specific work, letter number, or locus named is at least B, whether or not it has been acquired… acquisition status and attribution doubt belong in the Verification Note, not in a downgraded letter grade."* Four rows violate this:
- **Row 24** (DelCogliano &amp; Radde-Gallwitz, *Against Eunomius*, FotC 122, 2011) — **D**, justified as "named work, no accessible locus." Named authors, named title, named series, named year. Should be **B**.
- **Row 80** (Pharr, *The Theodosian Code*, 1952) — **D**, same invented basis. Should be **B**.
- **Row 52** (Nyssa's homilies on the Song of Songs, Ecclesiastes incl. *the fourth homily*, Beatitudes, Lord's Prayer) — **C**, downgraded because unacquired. Named works plus a named locus. Should be **B**.
- **Row 53** (Nyssa on the Forty and on Theodore the Recruit) — **C**, "no specific locus *in an accessible edition*." Two named works. Should be **B**.

These are directly inconsistent with **row 19** (Small Asketikon: "hence B, not the E… a real, identifiable recension awaiting acquisition") and **row 54** (*Ad Graecos*: "A specific, identifiable named work, hence B rather than E: real and traceable, simply unacquired"). Three different treatments of the same situation inside one revision.

Separately, a systematic misreading of the C/D boundary: **rows 29, 30, 61, 101, 107, 110, 111** are rated D on the stated ground that "no single specific work title" is given. But the template's D is *"Tradition/genre-level attribution, **no specific text/author named**"* and its C is *"Tied to a real author/work"* — the slash is a disjunction. Cavallin/Hübner/Zachhuber, Rudberg, Epiphanius, Drecoll, Barnes, Beeley, and Ludlow are all named authors, so all seven are **C** by the template's literal text. (Rows 86 and 88 are correctly D — genuinely no author or text.)

**12. Part F: seven rows have no Verification Note.** Rows **92, 93, 95, 96, 97, 100, 103** carry "—" in a field the template defines without an optional marker and which it explicitly requires even for Excluded rows. Part F's own preamble claims "Full schema columns restored here to match every other Part" — the columns are there, but seven cells are empty, and rows 89, 91, 94, 98, 99, 101, 102, 104–109, 112 all show what such a note should say.

**13. Completeness — three sources Doc_02 names that still have no row.** Round 1's nine are in; these three are not, and two are in Doc_02 §4, which you flagged for re-scrutiny:
- **The family estate-shrine at Annisa.** Doc_02 §4's "what this build can honestly use" list has four items; three have Part E rows (84, 85, 86) and this one does not. Worse, **row 82's Licensed For points at "the Annisa estate-shrine material-culture entry (§4)"** — a dangling reference to a row that does not exist. Needs a Part E row (attested via row 48, the *Vita*; Doc_02's own "text-attested archaeology, not excavated certainty" caveat carried).
- **"Gregory Nazianzen's oration on baptism"** (Doc_02 §2, baptismal exhortations). Row 17 covers only Basil's half of that same parenthesis; Nazianzen's oration appears nowhere in the Registry.
- **"Nazianzen on the Mamas festival at work level"** (Doc_02 §4). Row 20's Mamas homily is **Basil's**; Nazianzen's is a separate named source with no row, and row 84 doesn't cite row 31 either.

**14. Row 84's attestation list is wrong for its own claim.** *"Attested via the homilies themselves (rows 16, 20, 51)"* — row 51 is the *Life of Gregory Thaumaturgus*, a hagiography, not a homily. (Its festival-institution narrative may well be genuine evidence for the panegyris pattern, so the target may be substantively defensible — but it cannot be described as a homily.) Nyssen's own martyr homilies (**row 53**) are the obvious missing member, as is the Nazianzen Mamas source above.

**15. Part G says "Three items" and lists four.** The Armenian-literature bullet was added in this revision without updating the count.

**16. The living-document log overclaims.** Line 222's "every 'row N' cross-reference in the document checked against its actual target's content" must be corrected, not just the references. Given this project's own discipline about self-reported verification, an inaccurate verification claim in the record is a finding in its own right.

---

## Worth noting

- **Armenian Christian literature is a half-measure.** Round 1 asked for it as an Excluded entry. It sits in **Part G** as a bullet that assigns a full disposition ("**Excluded, Out-of-Boundary**") — which is precisely what a row is, and which contradicts Part G's own heading ("no current disposition beyond what Parts B–D already record"). Outside the numbered table it is invisible to any row-based downstream process. Append it as row 113 (append-only permits appending).
- **Row 22 (Morison) is Native with no real Licensed-For target.** The cell offers "supplementary reading," an appendix, and a chapter "not yet drawn on," and the note concedes "it is not currently cited by Doc_02 at all." The template: "A Native source with nothing named here is not yet usable downstream." Honest, but flag it as such rather than presenting three non-targets as a target.
- **Doc_01 §2 names van den Broek, van den Hoek, and Scholten** in support of a specific Contested claim. No row, no Part G mention. The preamble's "every source Doc_02 §§1–6 and Doc_01 name has a row below" is therefore not literally true. Cleanest fix is a Part G bullet noting their subject is Alexandria's world, not this one.
- **Row 6's "Epp. 188, 199, 217"** appears in neither Doc_01 nor Doc_02 (Doc_02 names only Ep. 199 among the canonical letters). The numbers are historically correct, but they are specificity supplied from model knowledge, unflagged — while **row 17** flags exactly this situation ("specific letters named by Doc_02 §2 but not independently isolated by exact number this session"). Same for the first names/initials in rows 29 and 30.
- **Row 10's Verification Note claims a licensing the Licensed For column doesn't contain** — the note says "this Registry instead licenses it primarily to debate (4)," but debate (4) appears nowhere in row 10's Licensed For. Add it (the divergence-flagging itself is good practice and should stay).
- **Row 26 is the only Native row carrying a Comparandum Note.** The content is useful (it explains why this is *not* a Named Comparandum), but every other Native row uses "—".
- **Section-filing artifacts.** The header "Macrina the Younger and the opponents (§1.4, §1.5)" covers rows 57–64, none of which concerns Macrina (she is at rows 11 and 48), and rows 62–63 (church historians, Philostorgius) are assessed at Doc_02 **§1.6**, not §1.5. Row 81 (Philocalia) sits inside **Part C — "Doc_02 §2"**, but the Philocalia is a §5/§9 + Doc_01 §2 source, not institutional/legal/liturgical evidence. Row 88 sits in Part E ("Doc_02 §4") but its basis is Doc_01 §4.
- **Row 81 could also license Doc_02 §5 debate (9)** — "how much Origenism the circle transmitted and how deliberately (**the anthology question**)" is the Philocalia by another name; only debate (5) is currently named.
- **Rows 74 and 84 at C where D fits** (neither names an author or text), inconsistent with row 86's D for the same situation. **Row 3** is D on the stated ground that no site is pinpointed, while its own Source cell names Göreme.
- **Row 56's Type S** doesn't meet the template's S definition ("modern scholarship"); it is a biographical fact from the general record. The Part G treatment given to the Pneumatomachians' positions would fit it better.
- The preamble's "the ten files Mark supplied 2026-08-30/31" is defensible as "the ten files carrying A rows," but ledger §9 records **eleven** files vendored (ten download-list files plus the Morison bonus, plus the superseded Macrina introduction-only).

---

## Recommendation

Send it back for a third, narrow pass. The findings are almost entirely mechanical — eight row-number corrections, three section-pointer corrections, one name, two formatting fixes, eleven tier re-scores, seven Verification Notes, three new rows plus one moved from Part G, and one honest correction to the log's own verification claim. None of it touches the design, which continues to hold up: the A/B discipline, the Part F Native-despite-copyright reasoning, the Philocalia boundary argument, and the Eupsychius correction are all genuinely right.

But the pattern from `CAPPADOCIAN_BUILD_LEDGER.md` §7 is repeating exactly as that section predicted: **each fixing round introduces a smaller set of errors than it removes, and the round's own self-audit misses some of them.** The renumbering did not corrupt historical content — that specific worry is cleared — but it did leave eight stale row pointers behind, and the document's claim to have checked them all is the single most misleading line in it. Whoever does the third pass should verify cross-references by resolving each target's content mechanically rather than by grep, and should specifically re-check that `row (N)`-style parenthesized references and `rows N–M` ranges are covered, since both slipped through last time.
