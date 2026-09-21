# Doc_03 Review — Round 9 (did the regeneration actually happen? — complement, Result-column, Registry-direction and layer-note recheck, cold)

**Document under review:** `witt_Doc_03_Lexicon_Candidate_List.md` (DRAFT, Revision 8), Lutheran Wittenberg & Its Congregations (Atlas VI.1, `witt`).
**Reviewer:** independent, no drafting involvement, no involvement in Rounds 1–8, no prior context on this document or on how its Revision 8 fixes were made.
**Date:** 2026-09-16.
**Scope:** exactly the seven-item list §13's "Review requirement (next round)" sets under the Revision 8 log entry, taken from Round 8's own "What a Round 9 check should and should not do" — (a) do not re-open OG-6; (b) re-derive nothing Rounds 5–8 re-derived; (c) **test whether §11 item 2 and §13's Result columns were actually *generated* this time or point-patched a third time** — the cheap total test, run on both; (d) check §11 item 8 in the direction Round 8 used (from every §13 declared range → to the Registry row that owns those lines → to whether item 8 has a line for it), not from the lines item 8 already has; (e) sweep every Layer note and translator/editor attribution in the document against the vendored file at the cited locus, the class R8-4 named, never swept as its own step; (f) do not re-run the 606-citation sweep, the 24-citation sample, the body-vs-Appendix cross-check, the thesis-number enumeration, the Doc_01 §8.4/§8.5 comparison, the Framework paragraph 97 check, Round 7's negative-claim greps, its per-file citation bucketing, or Round 8's §10.1/§11 item 4/§11 item 5 membership recomputation; (g) N5/OG-2 not re-litigated. Per (a), (b), (f) and (g), none of those was re-opened. **OG-5 and OG-6 are both closed and are not reopened, re-argued or re-asked anywhere below.**

**Method.** §10.3, §11, §12 and §13 read in full; entries 1.1, 1.2, 1.6, 2.8, 3.1, 3.4, 3.5, 5.5, 5.6, 5.8, 5.10, 6.1, 6.2, 6.6, 6.7, 6.8, 7.1, 7.4, 8.4, 9.1, 9.2 read in full. **All 72 entries were parsed by script and 591 citations extracted from their Evidence, Preliminary-definition and Voices lines** (three independent parsers — explicit-file-code only, semicolon-segment continuation, and a maximal-recall token walk — run against each other, with every disagreement re-read by hand), then tested against §13's own declared ranges and against each discovery row's Result cell. Every range §13 declares read was sorted and subtracted per file by script, and the complement compared clause by clause against §11 item 2. Work boundaries in `luther_works-v1-selected_jacobs-spaeth1915.txt` and `luther_works-v2-selected_jacobs-spaeth1916.txt` were re-derived independently by grep for the volumes' own all-capitals title headings, and cross-checked against **each volume's own contents page** (v1 46–71, v2 47–76). `witt_Source_Registry.md` was parsed in full (95 rows) and every row that owns lines §13 declares read was read directly for its Verification Note. All five Layer notes and every translator/editor attribution carrying a locus were opened at that locus in the vendored file.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**4 substantial findings, 4 cosmetic, 3 observations.** As at every round since Round 2, **nothing found in this round misquotes a source, miscites a locus, or misclassifies an entry**, and no evidence anywhere in the document is unwarranted on the strength of anything found here. **Revision 8's R8-4 fix landed exactly and the whole layer-note class now reproduces clean** (see "What reproduced clean").

**The primary question is answered directly, in both halves, and the two halves give opposite answers.**

---

# The primary question, answered

Round 8's item (c) asked one thing: were §11 item 2 and §13's Result column **generated** this time — sorted, subtracted, confirmed — or hand-patched a third time at exactly the entries the prior round named? §13's own Escalation check, re-run at Revision 8, set the consequence in advance: *"If Round 9 finds the same root cause producing new gaps a fourth time even after this revision's mechanical regeneration, that would be a different fact than what has been true through Round 8, and would warrant escalation on its own terms — not decided here, since it has not happened."*

## Half one: §13's Result columns were genuinely regenerated. CLEAN.

This is the first time in four rounds that a claim of mechanical regeneration has survived an independent mechanical test, and it should be recorded as plainly as the failures have been.

All 72 entries' Evidence, Preliminary-definition and Voices lines were parsed and 591 citations extracted. For every citation whose locus falls inside its row's own declared read range, the citing entry **is present in that row's Result cell — with no exceptions across all ten rows.** The one apparent exception the script raised, entry 6.7 against the Ap row at Ap 4729, is a meta-reference in 6.7's Voices line (*"…now declared rather than left implicit, as Ap 4729 now is too"*) describing how a **different** entry's locus is handled, not a citation 6.7 makes; it is correctly excluded. Every out-of-range citation that is absent from a Result cell (2.2 and 6.8 at Co; 4.9's three `Hy` loci; 6.9 at LC 3504; 9.1's *Fourteen of Consolation* pointer at v1 3994; 3.5 at v3 14586–14594) is honestly attributed to the Registry pass or to R34/R94 at the point of citation, exactly as the house convention requires.

**Revision 8's disclosed disagreement with Round 8 is independently confirmed correct.** R8-6's own table listed "5.7 (12378)" as a v1 Result-column omission; Revision 8 declined to add it. Three independent parsers agree: v1 12378 appears in 5.7 only inside its **Tags** line, as a cross-reference to entry 6.7's citation, and 5.7 itself makes no such citation. Declining it was right, and disclosing the disagreement rather than applying it silently was right.

## Half two: §11 item 2 and §11 item 8 were not. The fourth recurrence has happened.

The ten-work block Revision 8 added to §11 item 2 is real work, and much of it reproduces exactly (see "What reproduced clean" — the residual spans, the ≈18,901 arithmetic and eight of the ten work boundaries all hold to the line). But **the regeneration's scope was taken from R8-3's own finding list, not from the files.** It sorted and subtracted §13's ranges *across the ten works Round 8 named*; it did not sort and subtract them *across v1 and v2*. Two consequences follow mechanically, and both are new:

1. **It ignored §13's own grep-located loci.** Three of them — v2 5418, v2 7026, v2 10562–10566 — fall inside spans the new block declares unread, one of them under the words *"all entirely unread."* Entries 9.2 and 5.7 cite all three. This is **R8-2's defect exactly**, reintroduced by the fix written to close R8-3 (**R9-1**).
2. **It left five whole spans, ≈2,205 lines, named nowhere.** Every one of them is a titled piece or a work's own title-and-introduction block sitting in a gap between two declared read ranges — which is precisely what a sort-and-subtract over the file surfaces and what a sort-and-subtract over a list of ten works cannot (**R9-2**).

And §11 item 8, checked in the direction Round 8 prescribed, is short at **five Registry rows it does not name at all** — R2 (the Ninety-Five Theses), R8 (*The Papacy at Rome*), R14 (the *Kurze Form*), the hymnal rows, and R34 (*Bondage*) — plus omitted loci at three rows it does name (**R9-3**). Round 8 ran this direction too, but over the works its own R8-3 table had assembled; the five rows above are not in that table, so a check scoped to it could not reach them. **That is the same root cause, one location further on.**

**Stated plainly, because the brief asks for it unsoftened: the condition §13's own Escalation check named has been met.** This is the fourth consecutive round (6, 7, 8, 9) in which §11 item 2 has been found drifted from §13's own ground truth, and the third consecutive round (7, 8, 9) in which the Registry-bound list has been found short — this time *after* a revision that described itself as an actual mechanical regeneration. The pattern is not "the regeneration was faked." It is narrower and more durable than that, and worth naming precisely: **every fix in this document, including the mechanical ones, has been scoped to the extension of the last finding rather than to the domain of the claim.** Revision 8 regenerated §13's Result column over the domain (all 72 entries) and it came back clean; it regenerated §11 item 2 over the finding (ten named works) and it did not. That contrast is the strongest evidence any round has produced about what actually fixes this, and it is why the recommendation at the end of this report is one sentence long.

**Nothing evidentiary turns on any of this, as at every round since Round 3.** Every locus in every span named below is either cited by no entry at all, or cited and already declared read at §13.

---

# Substantial findings

## R9-1 — §11 item 2's new regeneration block declares unread three v2 loci §13 declares read and entries 9.2 and 5.7 cite — R8-2's defect, reintroduced by R8-3's fix

**Location:** §11 item 2, the new "Ten further works" block (the *Open Letter* and *Babylonian Captivity* items); against §13's v2 row.

§13's v2 row declares three grep-located loci read, each with its citing entry named in the same row's Result cell. All three fall inside spans the new block declares unread:

| §13 declares read | Cited at | §11 item 2 declares it unread as part of |
|---|---|---|
| **v2 5418** (*Anfechtung*, the sole occurrence across all ten files; added to §13 at Round 7 R7-11) | **9.2** (Preliminary definition, the "checked — cosmetic C10" claim) | *An Open Letter to the Christian Nobility*: *"v2 2417–5789 (≈3,373 lines…)"* |
| **v2 7026** (footnote [45]'s anchor point; added to §13 at Round 4 R4-6) | **5.7** (Evidence) | *The Babylonian Captivity*: *"v2 6800–7099 (≈300 lines, the rest of 'The Sacrament of the Bread'…)"* |
| **v2 10562–10566** (footnote [45] on transubstantiation/*Firmiter*; added to §13 at Round 3 R3-5) | **5.7** (Evidence) | *The Babylonian Captivity*: *"v2 9213–11012 (≈1,800 lines, 'Confirmation,' 'Marriage,' 'Ordination,' 'The Sacrament of Extreme Unction' and the work's own footnotes, **all entirely unread**)"* |

Re-verified directly in the file: v2 10562–10566 is footnote [45]; v2 7026 is its anchor; v2 5418 is the *Gravamina* footnote. All three are exactly where §13 says they are and all three are correctly quoted where cited.

**Why this is the finding it is.** R8-2 found §11 item 2 declaring unread two v3 spans §13 declares read, one of them created by Revision 7's own R7-1 text. Revision 8 fixed both instances — and then wrote a new block that does the same thing three more times, in a different file, because the regeneration took its input from §13's *range* list and not from §13's *row*. The third instance carries an affirmative "all entirely unread" on a span that contains a locus the same table declares read and the document quotes.

**Direction and severity.** All three are footnotes, not the works' own prose, and all three are correctly attributed and correctly quoted at their entries; 9.2's own wording ("grep-located") and 5.7's ("grep-located per §13") are both honest. Nothing false travels to the Registry from item 2. Graded substantial for the reason R8-2 was: these are contradictions between two locations about the same lines, both are cited in the document's own entries, and all three were created by the fix that was supposed to close the class.

## R9-2 — §11 item 2 is still not the arithmetic complement of §13's declared ranges: five spans, ≈2,205 lines, are named nowhere in v1 and v2 — and the block's own boundary claims fail at two of the ten works

**Location:** §11 item 2, by omission; against §13's v1 and v2 rows, and against each volume's own contents page and title headings.

Sorting §13's declared ranges per file and subtracting — the test Rounds 7 and 8 both specified and the test this block claims to have applied — leaves five spans in v1 and v2 that appear in no clause of §11 item 2, in no other list, and in no read declaration:

| Span | What is actually there (re-derived by grep) | Lines |
|---|---|---|
| **v1 434–1138** | `THE DISPUTATION OF DOCTOR MARTIN LUTHER … TOGETHER WITH THREE LETTERS EXPLANATORY OF THE THESES` (434–438), H. E. Jacobs's `INTRODUCTION` (441), `FOOTNOTES` (845), `LETTER TO THE ARCHBISHOP ALBRECHT OF MAINZ` (990) and its footnotes (1100) | **705** |
| **v1 1603–2242** | the letter to `JOHN STAUPITZ,` (1616) and its footnotes, `THESES 1518` (1798), and `A TREATISE ON THE HOLY SACRAMENT OF BAPTISM` (1957) with its `INTRODUCTION` (1961) and `FOOTNOTES` (2184) | **640** |
| **v1 12211–12693** | `THE PAPACY AT ROME / AN ANSWER TO THE CELEBRATED ROMANIST AT LEIPZIG` (12211–12213), Schmauk's `INTRODUCTION` (12218) and `FOOTNOTES` (12427) | **483** |
| **v2 13026–13171** | `A BRIEF EXPLANATION (EINE KURZE FORM) OF THE TEN COMMANDMENTS, THE / CREED, AND THE LORD'S PRAYER` (13026–13027), C. M. Jacobs's `INTRODUCTION` (13033), `LITERATURE` (13120), `FOOTNOTES` (13138) | **146** |
| **v2 14403–14633** | `THE EIGHT WITTENBERG SERMONS` (14403), Steimle's `INTRODUCTION` (14409), `FOOTNOTES` (14575), `EIGHT SERMONS BY DR. MARTIN LUTHER` (14625) | **231** |
| | | **≈2,205** |

Two of these are consequential beyond their size. **v1 434–1138 carries the letter to Albrecht of Mainz**, which Registry row R2's own Licensed-For calls a *"Tier 1 story"* and Doc_01 §2.1 records as the founding act; **v1 12211–12693 carries Schmauk's introduction to *The Papacy at Rome***, from which entry 6.7 draws its grep-located "popedom" locus at v1 12378 — so the span is not even wholly unread.

**Two of the ten boundary claims in the block fail their own stated rule.** The block states its convention explicitly: *"the Philadelphia edition prints most titles twice… the first occurrence is taken as the work's own start, matching how* The Papacy at Rome *and the* Kurze Form *are already bounded above."*

- ***A Treatise on Baptism*.** The block says *"(v1 2243–2855, R3; the work's whole extent, since **its one title occurrence** and the declared read range 2243–2422 begin at the same line)."* There are **two** title occurrences — `A TREATISE ON THE HOLY SACRAMENT OF BAPTISM` at **1957** and `A TREATISE ON BAPTISM` at **2243** — the same double-title pattern the block itself describes and applies to *Good Works* (6237/6713), *Confession* (2856/3165), *Blessed Sacrament* (80/213), *Ban* (1040/1140), *Open Letter* (1787/1997) and *Christian Liberty* (11013/11590). The claim of fact is false, and it is the claim that carries v1 1957–2242 out of the residual.
- ***The Papacy at Rome*.** The same list says its *"own title stands at v1 12694"* — the **second** occurrence, against the stated convention, and against Registry row R8's own note (*"Title-page forms at 12211 and 12694 as Doc_01 recorded"*). **§11 item 2 contradicts itself on this in the same list:** its *New Testament* clause bounds that work *"running to* The Papacy at Rome*'s own title at **12211**."* The claim that the convention "matches how *The Papacy at Rome* … is already bounded above" is therefore false of the very example it cites.

**What this is and is not.** It is **not** an overclaim in the enlarging direction and it does not reopen anything: no span above is claimed read, nothing false travels to the Registry, and the one cited locus inside any of them (v1 12378) is declared at §13 and honestly flagged at 6.7. What it is: the list Doc_06 will read as "what still needs reading" omits the Ninety-Five Theses' own editorial apparatus and the letter to Albrecht, the *Papacy at Rome*'s introduction, and the *Kurze Form*'s and the Wittenberg Sermons' own front matter — and the block's own closing sentence, *"Sorted and subtracted per file against every range §13 declares read,"* is the claim these five spans falsify. (The narrower claim in the same sentence, *"no eleventh work of this kind remains unnamed in v1 or v2,"* survives on its own terms: no eleventh work carries a §11 item 8 "now read" locus and no item-2 entry. It survives only because item 8 is itself short — see **R9-3**.)

Two smaller residuals of the same shape, recorded here rather than as their own finding: **v1 14691–14734** and **v1 14810–15008** are *The Papacy at Rome*'s own footnote block on either side of the declared 14735–14809, and item 2's explicit parenthetical (*"v1 12975–14690"*) excludes them. Nothing is cited in either.

## R9-3 — §11 item 8, the Registry-bound list, has no line at all for five Registry rows that own lines §13 declares read — including the Ninety-Five Theses and *Bondage of the Will*

**Location:** §11 item 8, *"Proposed as Verification-Note extensions for the Registry owner to apply."* This is the one list with a live route into `witt_Source_Registry.md` (APPROVED TO PROCEED) — the location and the risk R5-1 named, R6-3 re-found, R7-4 re-found again and R8-1 re-found again.

Item 8's stated purpose is *"loci the Registry records as unread that this pass has now read."* Run in the direction Round 8 prescribed — from every range §13 declares read, to the Registry row that owns those lines, to the item-8 line — **five rows have no line at all:**

| §13 declares read | Registry row | What the row's Verification Note actually records | Item 8 |
|---|---|---|---|
| **v1 1139–1602** (the Ninety-Five Theses and their footnote block) | **R2** | *"Title block 434–438, letter dated 992, Theses heading 1139–1140 … Editor's introduction 441–583 read"* — **the Theses' own text and footnotes, v1 1141–1602, are recorded nowhere** | **no R2 line** |
| **v1 12775–12974** (the treatise's own argument), **14735–14809** (its footnotes), **12378** (grep-located) | **R8** | *"Introduction 12218–12320 read"* only | **no R8 line** |
| **v2 13172–13341** (*Kurze Form* preface and Commandments summary) | **R14** | *"Heading 13172; preface 13179–13218 read"* — **13219–13341 recorded nowhere** | **no R14 line** |
| **Hy 1258–1352** (Hymn I) and **Hy 1647–1696** (Hymn IV) | **R27** (*"Contents 69–520 read"*), with R28/R29/R30 covering the prefaces, Hymn V and Hymn XXVI — **no Registry row of any number records Hymn I or Hymn IV** | nothing | **no line** |
| **Co 390–398, 730–809, 5212–5228, 14740–14775** | **R34** | *"Title 76–123, Cole's preface 135–265, Luther's introduction 269–389, Sect. CLXVII–CLXVIII 15057–15185, and 16060–16219 read"* — the four declared loci are recorded only in part (759–762) or not at all | **no R34 line** |

The affected loci are not marginal. **Entries 1.1–1.7, 2.3, 2.4, 3.2, 3.4, 8.7 and 9.3 all cite inside v1 1141–1602** — the document's whole 1517 cluster. **2.5, 2.9 and 9.3 cite Hymn I; 2.4 and 9.1 cite Hymn IV** — three of the five are Tier 1. **2.9, 3.3 and 7.1 cite the four `Co` loci** — 7.1 is Tier 1 and 2.9's *Bondage* quotations are the ones R34's own note flags as needing character-level re-check.

Three rows item 8 *does* name are also short, in the same direction:

- **R11** (*Open Letter*) gives 2117–2416 and 5790–5830; **v2 5418 is missing** (R9-1's first locus).
- **R12** (*Babylonian Captivity*) gives three ranges; **v2 7026 and 10562–10566 are missing** (R9-1's second and third).
- **R31** (Table Talk) has no line at all; the residual owed is small (TT 2440–2444, 3161–3164, 3552–3556 — 14 lines, nothing cited in them) and is recorded at **C9-3** instead.

**Direction and severity.** Every omission is an **under**statement, as R6-3, R7-4 and R8-1 all were — the Registry would record less coverage than exists, never more. No fabrication risk, nothing false to apply. Graded substantial because this is the fourth consecutive round in which this one list has been found short, in a revision whose predecessor added two rows to it specifically to reconcile it, and because the check that finds these is the same check Round 8 ran — only over the whole Registry rather than over the works the last finding named.

## R9-4 — four translator attributions inside the new regeneration block name the wrong translator, each contradicted by the volume's own contents page and three of them by this document's own Registry rows

**Location:** §11 item 2, the new "Ten further works" block. This is **R8-4's class** — an editorial layer attributed to the wrong hand — found this time as its own swept step rather than by chance.

Each volume's contents page names the introduction's and the translation's author for every work. Read directly (v1 46–71, v2 47–76):

| Work | §11 item 2's new block says | The volume's own contents page says | This document's own Registry row says |
|---|---|---|---|
| *A Treatise Concerning the Blessed Sacrament* | *"the work's own title and **Lambert's** introduction"* | Introduction (**J. J. Schindel**) | **R9**: *"intro./trans. **Schindel**, vol. II"* |
| *An Open Letter to the Christian Nobility* | *"the work's own title and **Lambert's** introduction"* | Introduction (**C. M. Jacobs**) | **R11**: *"trans. **C. M. Jacobs**, vol. II"* |
| *A Treatise on Christian Liberty* | *"the work's own first title, **Jacobs's** introduction"* | Introduction (**W. A. Lambert**) | **R13**: *"trans. **Lambert**, vol. II"* |
| *A Treatise on Good Works* | *"the work's own first title and **Jacobs's** introduction"* | Introduction (**A. T. W. Steinhaeuser**) | **R6**: *"trans. **Steinhaeuser**, vol. I"* |

The first two and the third are a straight transposition — *Blessed Sacrament* and *Open Letter* given to Lambert, who translated *Christian Liberty*; *Christian Liberty* given to Jacobs, who translated *Open Letter*. The fourth gives Steinhaeuser's introduction to Jacobs.

**Consequence, stated at its real size.** No quotation is affected and no entry cites any of these four introductions: all four sit inside spans the same block declares unread, and every locus the document does draw from an editor's introduction (Neve at v1 10661/10681/10727; Schmauk at v1 12378; Steimle at v3 14586–14594) is correctly attributed and verified below. So this is materially milder than R8-4, which misattributed a **quoted** gloss inside a Tier 1 entry's Layer note. Graded substantial rather than cosmetic for three reasons: a translator attribution is a sourcing claim, not a wording choice; three of the four contradict this document's own Registry rows, which is a contradiction between two canonical surfaces; and the block's own Method claim is that these boundaries were re-derived *from each volume's own contents page* — the same page that names each translator four lines away from the title the boundary was taken from. **The fix for all four is one look at a page the regeneration says it already opened.**

---

# Cosmetic findings

## C9-1 — §11 item 8's new R19 line re-offers 82 lines Registry row R19 already records, the defect C8-1 corrected at the R15 line in the same revision

Item 8's R19 line, added at Revision 8 per R8-1, offers *"R19 (*An Earnest Exhortation*, v3 **10641–10750**, 11228–11238 [a gloss], now read)."* Registry row R19's own Verification Note already records *"introduction 10464–10628 read; body **10649–10730** read."* Only v3 10641–10648 and 10731–10750 are new. This is exactly C8-1's finding against the R15 line — *"Sermon 1's range … re-offered 75 lines the Registry already records"* — applied at one line of item 8 and not at the line added in the same pass. Harmless in direction; the same note the line itself already carries (*"Registry row R19 itself already records the heading and body loci separately"*) shows the information was in hand.

## C9-2 — §11 item 8's R7 line omits v1 10638–10639

§13's v1 row declares Neve's introduction read from **10638**; Registry row R7 records *"Editor's introduction 10640–10740 read."* Item 8's R7 line offers 10741–10750 and 10905–11094. Two lines, nothing cited in them, no substance behind it — recorded only because it is the one residual R8-1's fix to this line still leaves.

## C9-3 — three further Registry-bound tails of five lines or fewer, nothing cited in any of them

Found by the same sweep as R9-3 and separated from it because no entry cites into any of them and each is small enough that a Verification-Note extension may not be worth the Registry owner's edit: **TT 2440–2444, 3161–3164 and 3552–3556** (14 lines past what R31 records; no item-8 R31 line); **Hy 1120–1124** (5 lines past R28's recorded 890–1119); **Hy 1868–1869** (2 lines past R30's recorded 1741–1867).

## C9-4 — the *Open Letter*/*Babylonian Captivity* boundary uses the second title occurrence, against the block's own convention, putting 147 lines of one work's front matter into the other's residual

The block bounds *An Open Letter* at v2 1787–6469 and *The Babylonian Captivity* at v2 6470–11012. The *Captivity*'s **first** title occurrence is `A PRELUDE ON THE BABYLONIAN CAPTIVITY OF THE CHURCH` at **6323**, with Steinhaeuser's `INTRODUCTION` at 6329; 6470 is the second. On the block's own first-occurrence rule the boundary is 6322/6323, and v2 6323–6469 — the *Captivity*'s own title and introduction — is currently counted inside *"v2 5831–6469 (≈639 lines, the remainder of 'III. Proposals for Reform' and the work's own footnotes)."* **No line is left uncovered**, so this is a label error and not a complement gap: R8-5's class, not R9-2's. Recorded because the block's stated boundary method is the thing under test, and this is the second of the ten works (after *Baptism*, at R9-2) where it was not applied.

---

# What reproduced clean

Offered because the finding count should not be read as a general deterioration, and because two of these are the first clean results of their kind in this document's review history.

- **§13's ten Result-column cells — the full test, over all 72 entries.** 591 citations extracted by three independent parsers; every in-range citation appears in its row's Result cell; every out-of-range absence is honestly attributed at the point of citation. **This is the half of R8-6's fix that was genuinely mechanical, and it holds completely.** See "The primary question, answered."
- **Revision 8's disclosed disagreement with R8-6** (the exclusion of "5.7 (12378)") independently re-derived and confirmed correct.
- **All five Layer notes, verified verbatim at their loci and correctly attributed** — the sweep Round 8 asked for, run as its own step for the first time. **2.8**: Steinhaeuser's *Gewissen* footnote at v3 7179–7180, inside *The Magnificat*, which Steinhaeuser translated (R18) — correct. **3.1**: the *Mein Wort* gloss at v3 11232–11233 — *"the message contained in the words. Luther does not claim for himself any form of inspiration"* — verbatim-exact, inside *An Earnest Exhortation*, translated by Lambert (R19). **R8-4's fix landed exactly, on both halves, work and translator.** **3.5**: *"the foundation principles of Protestant exegesis"* at v3 14593, inside the Emser general introduction, Steimle's (R21/R23) — correct, and correctly flagged as read at the Registry's word rather than this pass's. **5.8**: footnotes [7] (v1 14739–14746) and [18] (v1 14789–14793) to *The Papacy at Rome*, Steimle's (R8), both verbatim-exact; and `[Gemeinden]` bracketed at v1 10944 inside *A Treatise on the New Testament*, Schindel's (R7) — correct. **7.1**: the marginals `The Two Kingdoms` (v3 12123–12127) and `Spiritual and Secular Government` (v3 12276–12280) both present as running marginal glosses, correctly identified as the 1930 editor's.
- **Every other translator/editor attribution carrying a locus, opened at that locus.** Jacobs's Theses footnotes [1] (v1 1522–1524), [5] (1538–1540), [6] (1542, and it does anchor Th. 27), [9] (1553–1554) — all four verbatim-exact and correctly attributed; Steinhaeuser's sidenote at v2 6713–6714; Steimle's footnotes [4]/[5] at v2 15752/15754, [16] at v2 15789–15792, [12] at v1 14770; Jacobs's sidenote at v2 2171 (`The Priesthood of Believers`, without "all" — C6's distinction holds); Neve's "priesthood of all believers" and "Sacramentarians" at v1 10681/10661/10727; Schmauk's lowercase "popedom" at v1 12378, confirmed inside his introduction; Lambert's *Karsthans* footnote region at v3 10680–10684 and the *Geysterey* anchor at v3 20994–20995, both inside works Lambert translated; Bacon's, Bell's, Cole's and Bente/Dau's attributions throughout; Spangenberg (Hy 558–561, R47) and Walter (Hy 766–768, R45) matching their own Registry rows. **No misattribution found anywhere a locus is actually cited.**
- **The ten-work block's own arithmetic and eight of its ten boundaries.** Every one of the twenty-one residual spans reproduces to the line against the files; summed independently they give **exactly 18,901**, as stated; the *Good Works*/*New Testament* re-anchoring at 10628/10629 that produced the refinement from ≈18,900 is correct. *Baptism* and the *Open Letter*/*Captivity* junction are the two exceptions (R9-2, C9-4).
- **The complement test on the other eight files.** SC, LC, AC, Ap, Hy, TT, v3 and Co all reconcile: every gap between §13's declared ranges is named somewhere in §11 item 2 (or, for the Apology, in §11 item 1 and §12), including the four-line LC Article I close added at C8-3 and the *Earnest Exhortation* and *Magnificat* gloss exceptions added at R8-2. **The LC complement is now exact.**
- **R8-2's own fixes.** §11 item 2's *Magnificat* item and *Earnest Exhortation* item both now except their read glosses correctly, and entry 2.8's Layer note no longer claims the body unread without exception.
- **The stated word count, 37,628, reproduces exactly** (`wc -w`) — the fourth consecutive revision in which it has. **72 entries by script count**, as stated.

---

# Observations

**N9-1 — the contrast inside Revision 8 is the most useful datum any round has produced, and it should not be lost in the finding count.** The same revision, by the same method, on the same day, regenerated two lists. One (§13's Result column) was regenerated over its **domain** — all 72 entries — and comes back clean under a test three independent parsers ran. The other (§11 item 2) was regenerated over the **finding** — the ten works R8-3 named — and comes back with three contradictions and five unnamed spans. Rounds 5 through 8 have each diagnosed this as "fixes scoped to where the last finding landed." Revision 8 shows that the diagnosis is right *and* that the remedy works when it is actually applied to the domain. The remaining work is not a longer list of findings; it is one sort-and-subtract over v1 and v2 line 1 to end, and one pass over all 95 Registry rows.

**N9-2 — §13's Escalation check's own condition is met, and the determination is the build thread's to record, not this review's to apply.** §13 stated in advance that a fourth-round recurrence *after* the mechanical regeneration *"would warrant escalation on its own terms."* It has recurred, at §11 item 2 (R9-1, R9-2) and at §11 item 8 (R9-3). It has **not** recurred at §13's Result column. This report records the fact and declines to rule on the disposition: whether a partially-successful regeneration meets the escalation threshold, or whether the clean half shows the pipeline can close this without the project lead, is exactly the kind of judgment CO-022 reserves, and it is not one an adversarial review should make on its own authority. **Neither OG-5 nor OG-6 is reopened or implicated by anything above** — every finding in this round runs in the understating direction, and OG-6's own test for what would reopen OG-5 (an affirmative completeness predicate on a named unit without an exact line extent, or a stated extent wrong in the enlarging direction) is met by nothing here.

**N9-3 — OG-2 continues to accrete, as its own body predicts.** Not re-counted this round and not re-litigated, per the brief and per Rounds 4–8; Revision 8's fixes add roughly a further dozen inline finding-number markers on top of N7-1's count of ~92. It remains a disclosed, deliberate deferral and a precondition on disposition, owned at `Open_Gaps_Tracking.md` OG-2.

---

# What a Round 10 check should and should not do

Offered only so the option is costed; if no further pass is authorized, this section is moot.

1. **Re-derive nothing Rounds 5–9 have re-derived.** Add to Round 8's list: v1's and v2's full title-heading inventories and both volumes' contents pages (v1 46–71, v2 47–76); the v1 *Baptism* double title at 1957/2243; the v1 *Papacy at Rome* double title at 12211/12694; the v2 *Kurze Form* title at 13026 and Sermons title at 14403; the v2 *Captivity* first title at 6323; all five Layer notes and every translator attribution carrying a locus — **this last class is now swept and clean, and should not be swept again.**
2. **Do not re-run the §13 Result-column test.** It came back clean over all 72 entries and 591 citations, by three independent parsers. Re-running it is the one check this round can say with confidence is finished.
3. **Re-run the complement test on §11 item 2 the way this round ran it — over the whole of v1 and v2, line 1 to end of file, not over a list of works** — and, critically, **include §13's grep-located single loci in the read set before subtracting.** That one step is what R9-1 turns on. If the changes land only where R9-1 and R9-2 pointed, it was edited a fourth time.
4. **Re-run §11 item 8 against all 95 Registry rows, not against the rows a prior round named.** Parse the Registry, map every §13 declared range to its owning row, diff against that row's Verification Note. R9-3's five missing rows are unreachable from any list built out of the previous round's findings.
5. **Spot-check the four translator attributions at R9-4 against each volume's contents page** — a two-minute check, but it is the class R8-4 named and it has now been found twice in two rounds.
6. Do **not** re-run the 606-citation sweep, the 24-citation sample, the body-vs-Appendix cross-check, the thesis-number enumeration, the Doc_01 §8.4/§8.5 comparison, the Framework paragraph 97 check, Round 7's negative-claim greps, its per-file citation bucketing, Round 8's §10.1/§11 item 4/§11 item 5 membership recomputation, or this round's Layer-note and Result-column sweeps — all came back clean.
7. **Do not re-open OG-5 or OG-6.** Both are closed, neither is implicated by anything in this round, and re-asking either would be the self-certification problem in reverse.
8. N5 remains open by design, owned at OG-2, and does not need re-litigating.

---

**Disposition: none claimed by this review.** This report is a finding, not a ruling; it does not dispose the document. The escalation observation at **N9-2** is offered as a statement of fact about what this round found, not as a decision that CO-022's fourth category has been triggered — that determination is the build thread's and the project lead's, and this review deliberately does not pre-empt it. No finding above may be closed by self-certification.
