# Doc_08 Review — Round 1 (independent adversarial review, cold)

**Document under review:** `witt_Doc_08_Forces_Document.md` (DRAFT, Revision 0 — first draft, no prior review rounds), Lutheran Wittenberg & Its Congregations (Atlas VI.1, era 7, `witt`).
**Reviewer:** independent. No drafting involvement, no prior context on this document, this world, or any decision taken in building it, beyond what is written in the files read this pass.
**Date:** 2026-09-16.
**Scope:** the whole document, cold, against (a) the Forces Framework V1.1, extracted from the `.docx` and read directly in full — §2 (the two axes, the six cells in detail, Transmission as a named dimension), §3 (the three-layer requirement, all three layer descriptions), §4 (Steps 1, 2, 4, 5, 7, 8), §5 (Principles 1–5), §6; (b) the L4 `[world-code]_Forces_Document.md` template v1.1 in full, including its Version History, Section 1 field list, Section 3 builder note, Section 4 note, the Section 9 twelve-item checklist, the Final Assembly Instruction and the Builder Confirmation Note; (c) `witt_Doc_01`, `witt_Doc_02` (§12.3–§12.4 and §13 in full), `witt_Doc_04` (§1, §3 all thirteen entries, §4, §5, §6, §7, §10 in full), `witt_Doc_05` (§1.4, §2.5, §9B, §13), `witt_Doc_07` (§6 and §12 in full), `witt_Source_Registry.md` (R48, R49, R69, R93, R94 in full plus the Conventions and tally paragraphs), `Open_Gaps_Tracking.md` OG-8 and OG-11 in full, and `witt_Doc07_Review_Round1.md` for the ruling cited at S7 below; (d) the ten vendored primary texts in `cic/texts/`. **Doc_01–Doc_07's settled findings — Doc_04's thirteen classifications, Doc_02's confidence tags, Doc_07's lens work — were not re-litigated; only Doc_08's use of them was checked.**

**Method.** Nothing in the document was accepted as proof of itself, and the draft's own verification paragraph (§12, "Verification result, Revision 0": 164 pairs, five defects fixed, 149/164, 38/38 short phrases) was treated as a claim to test, not a fact to inherit.

Three checkers were built from scratch for this pass.

1. **Vendored-quotation checker.** The file uses only straight double quotes (496 `§`, 479 em-dashes, zero curly quotation marks — counted, because the first draft of my parser silently mis-paired on that assumption and had to be rebuilt). It pairs every quoted span with the first `PREFIX nnn–nnn` locus appearing within 40 characters of the closing mark and before any further quotation mark, splits on ellipsis, normalizes Unicode, drops bracketed editorial insertions, optionally de-hyphenates across line breaks, and tests each fragment against the cited line range at three widths (0, ±3, ±25). **173 quotation/locus pairs extracted; 156 verbatim inside the cited range exactly; 8 more verbatim but spilling one line past the cited range (ordinary line-wrap — each opened and read); 9 not matched — every one of the nine adjudicated by hand at the vendored file.**
2. **Prior-document checker.** Every quoted span followed within 60 characters by a `Doc_0n` attribution was tested against that document's own normalized text (125 pairs). Its flags were then hand-adjudicated, since the heuristic frequently grabs the *next* `Doc_0n` in the sentence rather than the attribution.
3. **Notation re-derivation.** Doc_04 §3's thirteen `**Forces-connection notation.**` paragraphs were extracted programmatically and inverted code-by-code, producing an independent force→gravity map, which was then compared against Doc_08 §3.0's table, §5's thirteen gravity entries, §5's by-gravity index view, and §3.7's Force Index. §4's thirteen connections were re-derived by hand and compared against §3.7's cross-cell column and §4's own map.

In addition: the Forces Framework and the L4 template were read directly rather than through the document's quotations of them, and every governing-question and principle quotation was compared word by word. Eighteen vendored loci were **opened and read in context for sense**, not only string-matched — LC 3443–3452, LC 3466–3490, LC 3500–3506, LC 3530–3545, v1 258–262, v1 327–332, v1 402–412, v2 6684–6689, v2 14725–14731, v2 15323–15328, v3 12185–12193, Ap 10000–10008, Co 16088–16094, Co 198–204, TT 3061–3066, TT 3132–3137, TT 106–114, TT 154–158. Registry row R94 was read in full and the document tested against each item it bars. Layer 2 was scanned independently of §8's own list, and every Layer 3 paragraph was scanned for household/parish assertions.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**8 substantial findings, 8 cosmetic, 5 observations.**

**The label overstates the size of the repair.** Seven of the eight substantial findings are repairable by rewriting one clause, one table cell, or one checklist line, and none overturns the matrix, the gravity synthesis, the transmission work, or any Doc_01–Doc_07 finding. What this review could not break, it tried hard to break:

- **Source fidelity against the vendored files is excellent.** Of 173 quotation/locus pairs, **164 verify at or within one line of the cited locus, and the nine residuals are all explained**: five are my parser's own pairing artefacts, one is my bracket-stripping removing the very text being quoted (Ap 10002–10006 — opened and verified verbatim inside Bente/Dau's bracketed German text, which the document itself discloses), one is the declared OCR-exempt Cole file (Co 16090–16092 — opened and verified, with the document itself disclosing the "sprjing" OCR), one is a dual citation the parser could only see half of (v1 "260–261, 329–330" — verified at 329–330), and one is a short phrase quoted from Doc_04 rather than from a vendored file. **I found zero genuine mis-quotations of a vendored text.** That is a better result than the draft's own report claims for itself.
- **The thirteen-of-thirteen gravity connection claim holds, re-derived from Doc_04's own text.** I extracted all thirteen forces-connection notations mechanically and inverted them independently. Every one of G1–G13 is connected to at least one force in §5, no row is empty, and G10's three connections ([F-ref], [F-rad], [F-sel]) are exactly the three forces Doc_04 §3 G10's own notation names — the thinnest row in both documents, for the same reason (R56).
- **Two of the three claimed corrections to Doc_07 §6 are right, and I verified both at source.** Doc_07 §6 does place [F-pop] in no cell at all (it appears there only in the absent-inputs list), while Doc_04's G6 notation carries "Intensified under [F-pop] in 1521–22" and G8's carries "Under [F-pop] (the *Exhortation*, 1522) it is the same restraint applied to the 'common man'" — both documented, both in-window, so Cell 2A is the right home and Doc_08's correction (a) is a real catch in an approved document. Correction (c) is also right, and more precisely right than the document claims: I read the vendored Large Catechism at LC 3443–3545 and the Fourth Petition runs from its own heading at LC 3445 to LC 3541, so LC 3535–3541 (the economic datum) and LC 3471–3484 (the prince's loaf) genuinely sit inside one petition — which is the exact ground Doc_05 §13 item 13's "under an existing cell; no new force code" instruction needed.
- **R94's bar is observed.** I read R94 in full and tested the document against every item it names. No "Here I stand" in any rendering; no "smite, slay and stab," no "three terrible sins," no "true martyr" sentence; no tower-experience narrative; no *pecca fortiter*; nothing from the *Deutsche Messe*; nothing from any Excluded row. The single quoted phrase inside the 1525 entry ("appearing as the princes' armies were already winning") is Doc_02 §12.4's own characterizing words, not the tract's, which R94 does not bar and §12.4's tags support exactly.
- **Living Tradition discipline holds, and Representative scope is respected.** Nothing in the document characterizes how anything is held in any Lutheran church or community today; the only occurrence of that register is Discipline 2's own bar. No Representative name, voice, biography or first-person content appears anywhere; every "Representative" sentence describes a construction consequence for a figure not yet chosen, exactly as §0 declares.

**The eight substantial findings are:** one unsourced general-knowledge clause inside a Layer 1 entry, in a document whose front matter declares no general knowledge is used anywhere (S1); two errors in §3.0's re-derivation table — the document's own headline methodological claim — both of which the cross-check it says it ran would have caught (S2); six disagreements between §3.7's Force Index and §5's by-gravity view, under a log entry certifying the two were reconciled entry by entry (S3); two mis-cited cross-cell connection numbers in the same index (S4); a Section 9 checkbox resting on a Proportionality provision that the Framework, the template, and this document's own Discipline 7 all say does not cover the case (S5); one misquotation of Doc_04 (S6); one clause reproducing, unqualified, the exact sentence-shape Doc_07's own Round 1 ruled must carry a qualifier (S7); and one Layer 2 sentence that converts a vendored text's recommendation into a description of practice (S8).

---

# SUBSTANTIAL FINDINGS

## S1 — Cell 1A-1's Layer 1 carries an unsourced general-knowledge clause, and it is garbled

§3, Cell 1A, Force 1A-1, Layer 1 (line 109):

> The frame is present at the origin: the 1517 letter goes to **an archbishop who is also an imperial elector's brother-in-arms in that frame**, and the 1520 *Christian Nobility* is addressed to "the German estates" (Doc_02 §1.1).

The second half of that sentence is cited and verifies. The first half is not cited, and it is not in this build's evidence base. I searched Doc_01, Doc_02, Doc_03, Doc_05 and the Source Registry for any characterization of Albrecht beyond his offices. What the build actually holds is Doc_01 §1: "**Albrecht, Archbishop of Magdeburg and Mainz** (1517)," and Doc_02 §1.1's "the covering letter to Albrecht of Mainz." Neither says anything about electors, and the phrase "brother-in-arms" appears nowhere in any file in `World-Builds/Lutheran-Wittenberg/` except this sentence.

The clause is also wrong on its own terms in a way that marks its origin: the Archbishop of Mainz *was himself* one of the seven imperial electors, so "an imperial elector's brother-in-arms" is neither a description of Albrecht's own standing nor a recognizable relationship — it reads as a half-remembered fact from outside the library, imprecisely rendered.

This matters more than its length. The document's front matter states, in bold: "**No live research; no general knowledge of Luther, Lutheranism or the Reformation is used anywhere** — where a true thing about this world could not be traced to Doc_01–Doc_07 or a vendored locus they cite, it is absent or named as a gap." One clause breaks that declaration, and it breaks it in the Layer 1 of the document's first force entry, in the sentence that establishes the entry's load-bearing claim ("The frame is present at the origin").

**Fix:** delete the clause. The sentence still carries its claim on its second half, and can be strengthened from what the build does hold — Doc_01 §1's list of named addressees (an archbishop, a pope, named territorial princes) is itself evidence that the imperial frame was the address-space of the founding act.

---

## S2 — §3.0's re-derivation table, the document's headline methodological claim, contains two errors against Doc_04 §3

Discipline 4 (line 25) and §3.0 (lines 75–95) present the cell-placement table as re-derived from Doc_04 §3's thirteen notations directly — "each notation was re-read this pass at Doc_04 §3 and cross-checked against the §7 Index's summary column" — and the table's own column header reads "Doc_04 notations in which it appears (gravity: role)." I extracted all thirteen notations mechanically and inverted them. Eleven of the thirteen code rows reproduce exactly. Two do not.

**(a) The [F-imp] row omits G11.** Line 86 reads:

> | [F-imp] | G1, G5: intensified into confessional definition; G2: stated additively; G3: shifted ("retained"); G6: settlement 1555 unvendored; G7: reworded "calling"; G8: occasion (the Edict, 1521) and settlement (adiaphora); G12: naming shift | … |

Doc_04 §3 G11's own notation reads: "**Shifted under [F-imp]** into the Apology's explicit two-tier rule (Latin for learners, German for the people) — a balance the 1520 *Kurze Form* did not need to state." [F-imp] appears in nine notations (G1, G2, G3, G5, G6, G7, G8, G11, G12); the table lists eight.

**(b) The [F-turk] row adds G6, which is not in G6's notation.** Line 91 reads:

> | [F-turk] | G5: not touched; **G6: "the Turk as the Diet's own agenda"**; G12: the world's own reading | … |

G6's forces-connection notation (Doc_04 line 271) names [F-emb], [F-ter], [F-pop], [F-rad] and [F-imp], and does not mention the Turk at all. The quoted phrase "the Turk as the Diet's own agenda (AC 49–53)" is the **G6 × G12 cell of Doc_04 §5's Interaction Matrix** (Doc_04 line 455) — a gravity-to-gravity relationship, not a forces notation. [F-turk] appears in two notations (G5, G12), not three.

Neither error changes a cell assignment, and §5 G11 does carry the [F-imp] connection correctly, so nothing downstream is wrong. What is wrong is the certification: the table claims a specific derivation from a specific source, and in two rows it did not perform it. Both would have been caught by the cross-check the same sentence claims to have run — Doc_04 §7's Index summary for G11 reads "shifted to a two-tier rule **[F-imp]**," and its summary for G6 names no [F-turk]. This is the OG-8 class exactly: "a claim that a check was run, made before it actually was, or made about a narrower scope than the sentence itself claims."

**Fix:** add G11 to the [F-imp] row; remove G6 from the [F-turk] row, or re-label it "(Doc_04 §5 interaction cell, not a forces notation)" so the table's own column header stays true.

---

## S3 — §3.7's Force Index disagrees with §5's by-gravity view in six of twenty rows, under a log entry certifying they were reconciled entry by entry

§12 (line 753) certifies: "(2) the by-gravity view built by inverting §5's connection lists by hand and **checked against the Force Index's 'Connected gravities' column, entry by entry** — thirteen of thirteen gravities non-empty." Discipline 9 adds: "Index and prose were reconciled by hand after drafting."

I inverted §5's thirteen gravity entries independently and compared force-by-force against the Force Index. **The by-gravity view (§5) and §5's prose agree exactly — all thirteen rows and all thirteen counts reproduce.** The Force Index does not. Six of its twenty rows disagree with §5:

| Force Index row | Index says | §5's by-gravity view says |
|---|---|---|
| 1A-2 (line 352) | G1, G2, G7, **G12** | G12's row is `2A-1, 2A-5, 2B-1, 2A-2, 3A-1, 1B-3` — **1A-2 absent** |
| 2A-1 (line 357) | G1, G2, G3, G5, G9, G12 — **no G13** | G13's row includes **2A-1** ("its 1529 occasion by subtraction — the Easter compulsion lifted (C5)") |
| 2A-2 (line 358) | G1, G2, G3, G5, G7, G8, G11, G12 — **no G9** | G9's row includes **2A-2** ("*held into the confessional register* (AC XXIII, XXVII)") |
| 3A-1 (line 367) | G6, G7, G8, G12 (stated: G1–G3, G5) — **no G4** | G4's row includes **3A-1** ("*held into the confessional corpus*") |
| 3B-1 (line 369) | G2, G7, **G8** | G8's row is `2B-1, 2A-2, 2B-3, 3A-1, 2A-4` — **3B-1 absent** (it appears only in G8's Tensional note, not as a connection) |
| 3B-2 (line 370) | G3, G4, G9, G10, G13 — **no G1** | G1's row includes **3B-2** ("*carried* — visible after 1531 'in hymn and Table Talk only'") |

Four omissions and two additions. None of them changes a substantive claim — every one of the six relationships is stated somewhere in the document, and the thirteen-of-thirteen result is unaffected — but the index is the artefact this project's own forces-index bar exists for: "the index is what a reviewer checks the prose against without rereading it" (Discipline 9's own words). An index that disagrees with the prose in 30% of its rows does not do that job, and the log's "entry by entry" is a certification the document cannot support.

**Fix:** re-derive the Force Index's "Connected gravities" column mechanically from §5's by-gravity table rather than by hand, so the two are one artefact in two orientations. Note also that a hand reconciliation of a 20 × 13 relation is exactly the task OG-8's pattern says will fail silently.

---

## S4 — Two of the Force Index's cross-cell citations name connections that §4 does not carry

Same table, "Cross-cell connections" column, which §3.7's own preamble says "cite §4 by connection number with direction."

**(a) Line 351, row 1A-1:** "C1 → 2A-3; **C9 → 3A-1**." §4's Connection 9 (line 402) is "**Forces 2A-2 ([F-imp]) and 2A-3 ([F-ter])** → Force 3A-1." 1A-1 is not a party to it. The underlying relation the row is reaching for is real — [F-emb] is co-listed inside the 2A-3 entry — but as written the index asserts a membership §4 denies.

**(b) Line 352, row 1A-2:** "C1 → 2A-3; **C5 ⇒ 2A-1**." §4's Connection 5 (line 390) is "Force 2A-1 ([F-pap], **its removal**) → Force 2B-3." It is not a 1A-2→2A-1 relation, and its direction is the opposite of the one the index draws.

The second is the more interesting of the two, because it exposes a real gap rather than a slip. The document names the "same force at two phases" relation explicitly for [F-print] (C6: 1A-3 ⇒ 2B-4), for [F-rad] (C12: 2B-1 ⇒ 3B-1) and for [F-sel] (C13: 2B-2 ⇒ 3B-2) — but not for [F-pap], whose initiating form (1A-2) and ongoing form (2A-1) are the most heavily used pair in the matrix, carrying six gravities between them. The index papers over the gap by borrowing a number that belongs to something else.

**Fix:** correct row 1A-1 to show its participation as indirect (e.g. "C1 → 2A-3 (whose C9 → 3A-1)"), and add a fourteenth connection for [F-pap] initiating ⇒ ongoing rather than mis-citing C5. The §4 count and the map would then both move to fourteen.

---

## S5 — §9's second checkbox rests the Layer-1-only entry on a Proportionality provision the Framework, the template, and this document's own Discipline 7 all say does not cover it

§9, item 2 (line 694):

> - [x] Every identified force documented at all three layers — nineteen of twenty entries; 3A-2 is Layer 1 only **with the reason stated per the Proportionality Principle's provision**, and its Layer 2 and Layer 3 fields state what is not recoverable rather than being left blank.

The Forces Framework §3 is categorical: "Every force identified in every cell must be documented at three layers. **This is not optional.** All three layers are required for every force. A force documented only at Layer 1 (what happened) without Layers 2 and 3 is a force that has not been analyzed — it has only been noted."

The only carve-out is Principle 2, and Principle 2's wording is narrow: "A force that was present but **left little formative trace** warrants brief documentation at Layer 1 only, **with a note that its formation impact was minimal.**" The L4 template's own Section 3 builder note repeats it in the same terms: "Forces with **minimal formative trace** may be documented briefly at Layer 1 only."

3A-2 is not that case, and the document says so twice, in its own voice. Discipline 7 (line 31): "[F-ref], [F-pop]'s 1525 climax and [F-imp]'s 1555 settlement are thin **because the library lacks them, not because their impact was small — the inverse case, which the Principle's wording does not cover**." 3A-2's own Layer 1 (line 307): "**Why Layer 1 only, and why this is not Proportionality's case:** both events are absent from the library, not minimal in impact." §8's Proportionality section says it correctly too ("Layer 1 only: 3A-2, with the reason stated (barred and unvendored inputs, not minimal impact)").

So §9 item 2 invokes, as its warrant, the one provision three other passages of the same document correctly say does not apply. And the template's Section 9 instruction is explicit about what to do instead: "**Where any item cannot be confirmed, note it as OUTSTANDING** with what remains to be done."

This is not a quibble about a tick-box. Item 2 is one of the two checklist items that gates Validation and Deployment, and the honest report is available and is already half-written elsewhere in the document.

**Fix (two options, either acceptable):** (i) mark item 2 **OUTSTANDING**, with "3A-2 is Layer 1 only because its Layer 2 and Layer 3 are barred and unvendored, not because its impact was minimal; the Framework's only Layer-1-only provision does not cover this case; Philadelphia vol. IV [R62] and anything post-1546 are what would close it." (ii) Re-cast 3A-2 so it is not a numbered force at all but an **absent-input register** appended to Cell 3A — which is what its content actually is, and which would leave item 2 satisfiable on all *identified* forces (nineteen of nineteen). Option (ii) is cleaner, but it sharpens the question at §9 item 1, since Cell 3A would then be populated by 3A-1 alone.

**Related, and carried here rather than as its own finding:** §9 item 1 is ticked `[x]` while its own text says the item "is satisfied by 3A-2 alone **or is to be marked OUTSTANDING**." A checkbox that is ticked and simultaneously conditionally outstanding is not a certification. My ruling on the underlying question is at "Rulings requested" below; whichever way it goes, the box should state one status, not two.

---

## S6 — 3B-1's Layer 3 misquotes Doc_04 §3 G7, changing the referent, and the same phrase is quoted correctly elsewhere in the same document

§3, Cell 3B, Force 3B-1, Layer 3 (line 331):

> a criterion of legitimacy — "regularly called," the "external Word" — that is **"the world's own answer to unlicensed preaching"** (Doc_04 §3 G7)

Doc_04 §3 G7's notation (Doc_04 line 292) reads:

> an explicit requirement of regular call — **the gravity's own answer to unlicensed preaching**, stated in the founder's voice against Karlstadt's circle and in the confession against the Anabaptists.

"The gravity's" has become "the world's" inside quotation marks. The substitution is small but it moves the referent from a gravity (G7, a construction object) to the world (a historical community), which is precisely the kind of slippage this build's Discipline 6 exists to prevent elsewhere.

The document knows the right wording: §5 G7 (line 498) quotes it correctly — `"the gravity's own answer to unlicensed preaching."` One document, two renderings, one of them wrong.

**Fix:** restore "the gravity's" at line 331, or drop the quotation marks and paraphrase.

---

## S7 — 1B-3's Layer 3 reproduces, unqualified, the exact clause Doc_07's own Round 1 review ruled must carry a prescription qualifier

§3, Cell 1B, Force 1B-3, Layer 3 (line 169):

> **Made the married household the formation site** (G4's site is G9's estate).

`witt_Doc07_Review_Round1.md` finding S6 (lines 118–126) quoted Doc_07's then-draft — "a formation site **that is** the married household under a father who is a priest by baptism" — and ruled:

> "Examined weekly and fed only after the parts are said" is LC 241–243 and LC 333–334 — prescription, and prescription whose reception is the G4 divergence Doc_04 §6.3 reserves and Doc_07 says it carries "on every use of G4." **Here it is stated as constitutive fact of the site.** … **Fix:** one clause — "a formation site that *was to be* the married household…"

Doc_07 applied it. Its approved §7 now reads "a formation site that ***was to be*** the married household," with the correction noted inline. Doc_08 is drafted from that approved text and reverts to the unqualified form.

The mitigation is real and should be weighed: §7 of this document carries a blanket line — "**Every Layer 3 sentence touching the household or the parish** inherits the G4 divergence: Documented as program, I/T as anyone's fact (Discipline 6)" — and Discipline 6 declares the rule. But Doc_07's Round 1 ruled specifically that a blanket carry was *not* sufficient for this clause, on the ground that this is the sentence a downstream World Profile or Capsule writer lifts verbatim: "An unqualified reception claim propagating out of Doc_07 into the Capsule is precisely what Doc_02 §14's confidence propagation exists to prevent." The same reasoning applies with equal force to a Doc_08 Layer 3, which Doc_09 and Doc_10 will read.

**Fix:** "Made the married household the formation site **the program prescribes**" or "**was to be** the formation site." One clause.

**Checked and clean around it:** I scanned every Layer 3 paragraph for household/parish assertions. This is the only one. Every other instance either names a program, quotes a text, or reports an absence; 2B-3's Layer 3 and 3B-2's Layer 3 both hold the line exactly.

---

## S8 — 1A-1's Layer 2 converts the Large Catechism's recommendation into a description of practice

§3, Cell 1A, Force 1A-1, Layer 2 (line 111):

> so that **"a loaf" is painted on the prince's arms** (LC 3480–3484)

I opened `luther_large-catechism_bente-dau1921.txt` at LC 3480–3484:

> Therefore **it would be very proper to place** in the coat-of-arms of every pious prince **a loaf of bread instead of a lion**, or a wreath of rue, or to stamp it upon the coin, to remind both them and their subjects that by their office we have protection and peace…

The quoted words ("a loaf") are verbatim and my checker passed the pair; the failure is one of sense, which a string match cannot catch — the very limitation §12's own "checker-side lesson" names. The text proposes something that is *not* the case ("instead of a lion") and gives a reason for proposing it. Doc_08's Layer 2 states it as an existing practice, in the indicative, in the layer that is supposed to be the world's own experience of the force. On the document's own evidence the world's experience here is the *wish* — which is a better Layer 2 datum than the false description, because the wish is what the frame felt like from inside.

The compression is partly inherited (Doc_05 §1.4 writes "hence the loaf on the coat-of-arms"; Doc_07 §6 writes "the prince's loaf"), but neither prior document asserts that it *is painted*, and Doc_08 is the document that must carry the locus.

**Fix:** "so that a prince's coat-of-arms, the catechism says, would more properly carry 'a loaf of bread instead of a lion' (LC 3480–3484)."

---

# COSMETIC FINDINGS

**C1 — Cell 2B's governing question is truncated without ellipsis.** Line 241 reads: "What internal forces sustained this community from within, generated its characteristic internal tensions, and shaped how it transmitted itself?" The Forces Framework §2 reads: "…and shaped how it transmitted itself **to the next generation**?" The other five governing questions (1A, 1B, 2A, 3A, 3B) are verbatim; only 2B's is cut. The cut is not neutral for this world — "to the next generation" is the part a 1517–1545 window can least show, and silently dropping it removes a bar the document elsewhere takes seriously. Restore the four words and, if needed, note in the entry that the window bounds what can be shown of them.

**C2 — 2B-3's Layer 3 compresses a Doc_04 quotation without ellipsis.** Line 273 quotes "the founder's response shifts with it: rebuke → program → print-control" as Doc_04 §3 G13's. Doc_04 reads: "rebuke (1522) → program (1529, the catechisms; the visitation by reference) → print-control (1543, names attached to hymns)." Three parentheticals removed inside quotation marks with no ellipsis. Add ellipses or drop the marks.

**C3 — Discipline 4 mischaracterizes OG-8.** Line 25: "OG-8, OG-10 and OG-11 each record a reviewer catching an enumeration transcribed from a prior document's prose rather than re-derived from source." OG-11 records exactly that and names OG-10 as the precedent ("the identical 'enumerate rather than re-derive' failure OG-10 already recorded"). OG-8 records something adjacent but different: an inline-line/matrix-cell mismatch and three consecutive rounds of false self-certification of a sweep. The distinction is worth keeping, since OG-8's actual pattern is the one S2 and S3 above belong to.

**C4 — the [RES] marker is a shorthand for a prescribed sentence, and the substitution is not among Discipline 1's disclosed template deviations.** The L4 template's Layer 2 instruction prescribes the marker's wording: "Reported as the world's own self-understanding — not assessed for historical accuracy; confidence calibration applies to the historical-event layer only." Doc_08 substitutes "**[RES]**" plus a one-clause gloss. The substitution is sensible in a document with six of them, and §8(c) discloses the glosses — but Discipline 1 lists exactly two template discrepancies, and this is a third. Either add it to Discipline 1's list or state the template's sentence once, at Discipline 5, as what "[RES]" abbreviates.

**C5 — 1B-2's internal/external disclosure omits the strongest text against its own placement.** Line 155 argues the classification from the Framework's Cell 1B example ("inherited practices from a prior tradition that were reinterpreted under new conditions") and discloses that "a reviewer may hold that the condition of the parent church's laity is external." What it does not quote is the Framework's own definition of External, whose closing gloss is: "These are **what the world was responding to from outside itself**" — and Doc_01 §7 files [F-resp] under precisely the heading "what it was responding to at its origin." That is the counter-argument at its strongest, and a disclosure that omits it is weaker than it needs to be. (My ruling on the substance is below; the placement stands.)

**C6 — §11 item 3 omits that Doc_04 already assigns the codeless force a home.** The open item asks "whether Doc_04 §1 should carry a fourteenth code for the parish's state as reported, or record why it stays codeless." Doc_04 §3 G13's notation already brackets it: "a force Doc_02 §13 could not document at Layer 1 — the parish's actual state **[F-ter's inspecting arm, R51–R52 absent]**." A Doc_04 revision reading §11 item 3 cold could add a fourteenth code for something Doc_04 has already located inside [F-ter]. Add the bracket to the item.

**C7 — one locus for the AC preface's Turk clause is cited three ways.** 1A-1 uses AC 49–55, 2A-5 uses AC 49–51, and §5 G6 (line 492) uses AC 49–53. All three are traceable (Doc_02 §13 uses 49–55, Doc_04 §3 G12 uses 49–51, Doc_04 §5's matrix cell uses 49–53) and all three contain the quoted words, so nothing is wrong — but one document citing one clause three ways invites a false positive in the next reviewer's checker. Harmonize on AC 49–51 for the quoted phrase.

**C8 — §7's Table Talk list is one entry short of its own scope.** Line 630: "**Every Table Talk sentence quoted** (1A-1, 1B-2, 2A-1, 2A-3, 2A-5, 2B-3): Contested as verbatim." 2B-2's Layer 2 also quotes the Table Talk file — "fragments that fell from Luther's Table" (TT 156–157), which I opened and verified — though it is Aurifaber's dedication rather than a reported saying, and is separately covered by that entry's [RES]. Either add 2B-2 with the distinction, or narrow the scope line to "every reported saying."

---

# OBSERVATIONS

**O1 — §5 asserts several connections Doc_04's notations do not carry, and the document's own claim about §5 is stronger than what §5 does.** §5's preamble says the connection statements are "Doc_04's own verbs… mapped onto this document's cell IDs," and §12's review requirement (e) sharpens it: "the load-bearing claim is that **no connection is asserted that Doc_04's own text does not carry**." Tested against my mechanical inversion of the thirteen notations, at least five connections in §5 go beyond them: G1 → 3B-2 [F-sel] ("carried"; Doc_04's G1 notation states the post-1531 thinness as a Persistence result, not as a [F-sel] effect); G2 → 2B-2 [F-sel] (Doc_04's G2 says only "Under [F-print] it is the thing printed"); G4 → 1A-1 [F-emb] (the household's petition for the prince — not in G4's notation); G4 → 3A-1/3B-2 (Doc_04 says "Held," with no code); G13 → 2A-1 [F-pap] (the Easter compulsion lifted — Doc_05 §2.5(c)'s finding, not Doc_04's).

Each is separately grounded in a cited prior document or in this document's own cells, each is a defensible piece of forces analysis, and none is needed for the thirteen-of-thirteen result. The defect is in the claim, not the content: §5 is doing more than restating Doc_04, which is what a Step 8 compilation *should* do. The clean repair is to soften the preamble to something like "Doc_04's own verbs where Doc_04 states the connection, with additions from Doc_02 and Doc_05 marked as such," and to mark the five.

**O2 — length is earned by the matrix and spent unevenly outside it.** Measured by section: the twenty force entries total ≈ 10,100 words (mean 505; the longest are 2B-1 at 784 and 3B-2 at 921, which are the two the document names as its most consequential); §5 is 2,445; §4 is 1,493; §6 is 1,156. That is proportionate for a six-cell/three-layer document with twenty entries and thirteen gravities, and I would not cut the entries.

The one genuine redundancy is the one the document already names at §12: **3B-2's Layer 1 (921 words) and §6's first two subsections (≈ 620 words) list the same fourteen transmitting lineages with the same interests**, in the same order, largely in the same words. One of the two should carry the roster and the other should point at it — §6 is the better home, since the Transmission Specificity Principle is answered there.

Separately: §0 (1,905 words) plus §12 (1,558 words) is 14% of the document, in a Revision 0 with no repair history to narrate. That is the same pattern `Open_Gaps_Tracking.md` OG-11 item 5 carries as an undecided fleet-level question and OG-11 item 9(i) counts as its seventh data point; this is the eighth. Flagged as a data point, not charged as a defect, exactly as Doc_07's Round 1 O5 handled it.

**O3 — the From-Within word-list scan reproduces exactly, and §8's summary of it is broader than the scan supports.** I ran my own scan over all twenty Layer 2 entries with §8's word list plus a dozen terms it does not include. Every hit of a listed word is where §8 says it is: inside a quotation, inside a bracketed layer note, or in one of the four disclosed places ((a) 2A-6/3A-2's non-recoverability statements, (b) 3A-1's voice-change confinement, (c) the six [RES] glosses, (d) 2A-3's economic-datum marker). The false positives §8 names ("estate," "statements") are real false positives. **That claim verifies.**

What does not verify is the sentence after it: "**No other analytical term was found inside any Layer 2 entry.**" The analyst's *framing* vocabulary is present in most Layer 2 entries and is simply not on the list — "Its name shifts by register" (2A-1), "the same force is met with a measured voice" (2A-1), "this layer is confined to the voice-change the texts themselves show" (3A-1), "the world names the frame by its offices and its bread, never as a system" (1A-1). This is ordinary connective tissue, it is how a Layer 2 gets written at all, and Layer 2 passes the Framework's governing test comfortably — I read every one asking "could someone formed within this world recognize this as an honest account of how they understood what was happening to them?" and the answer is yes throughout. But the claim should be scoped to the list it actually ran: "no *listed* analytical term."

**O4 — the escalation check holds, and I tested each of its four categories.** (1) No Representative identity, title or voice is decided: the §1 field is `[TBD — PENDING]` per the template's own v1.1 provision, and no candidate, name, biography or first-person line appears anywhere. (2) Nothing portfolio-level is decided: every cross-world sentence restates Doc_01 §8, Doc_02 §12.4–12.5 or Doc_04 §8, and no sibling world's Doc_04 or Doc_02 is claimed as precedent (there are none — I confirmed the neighbours have Step 0 only, as Doc_04 §8 records). (3) No governance or methodology change is made: Discipline 3 applies the Framework's own cell wording to this world's evidence and discloses the reading; Discipline 1's two template discrepancies are flagged, not fixed; no force code is added; §11 item 3 is a recommendation to Doc_04's owner. (4) The one genuine tension — Doc_07 §6's "nothing the library attests" for 3A/3B against the template's "all six cells populated" checklist — is resolved by argument from the governing Framework's own wording with the alternative disposition stated. That is within the pipeline's own competence and does not meet the escalation bar. **No escalation category applies.**

**O5 — the document's self-reported verification is honest but understates its own result, and the disclosure about the checker is the right one.** §12 reports 149/164 after repairs with fifteen residuals. My independently built checker, run on a different pairing rule, found 164 of 173 pairs clean at or within a line, with all nine residuals explained and zero genuine defects. The five defects the draft reports finding and fixing (SC 305–306's "for"; the v1 12304–12309 compression and trailing comma; v1 396–397's "grew"; LC 71–72's inherited paraphrase; v1 299–300's "they will") all verify as fixed at the file. The §12 note that "a substring match against ±1 line confirms a quotation appears near its citation, not that it is *the* quotation the citation names" is exactly right, and S8 above is the finding that lesson predicted — it is the only sense-level defect I found in eighteen loci opened and read in context.

---

# RULINGS REQUESTED BY THE DRAFT

The draft asks for three rulings (§12, "The places this document most expects to be argued with"; §11 item 1). Each is ruled here.

**(a) Does 3A-1 belong in Cell 3A, or should it fold into 2A? — It belongs in 3A. The document's own alternative is the weaker reading.**

The cell's governing question, verified verbatim against the Forces Framework §2, is: "What external forces brought this world's **distinct form** to an end **or transformed it into something different**?" The object of the verb is the world's *form*, not its existence. What Doc_01 §2.3 documents and Doc_05 §9B adjudicates is precisely a change of form: "the *relationship* in which it is transmitted changes substantively: from a professor addressing named readers, to a preacher restraining his own congregation, to a father examining his servants under a pastor the prince inspects, to princes confessing before an emperor" — "a transition in *who is formed by whom under what force*, not in what is taught" (verified verbatim at Doc_05 §9B). A transformation in who forms whom, under which authority, is a transformation of a formation world's distinct form under the Framework's own terms. It is external (the Diet's summons, the princes' signatures), it is in-window, and it is Documented as to the documents.

The fold-into-2A alternative is worse on two counts. First, it would leave Cell 3A carrying only 3A-2 — an entry that documents nothing the library holds — which reports the world as having *no* attested transformation when the library in fact attests one. Second, it would lose the distinction the matrix exists to draw: 2A-2 and 2A-3 are the forces pressing continuously; 3A-1 is what those forces *did* to the world's form by 1530–31, which is a different claim and is the one Doc_01 §2.3 handed forward for exactly this purpose.

Two conditions on the ruling. (i) The Layer 1 disclaimers stay as written — "the world's form after it is a successor form of itself, not a different community," and "**What is not claimed:** that this transformation ended anything." They are what keeps the entry honest against Articles 28–29. (ii) The double-count with 2A-2/2A-3 must remain visible, which C9 and the Force Index already do. With those, Discipline 3's option (iv) is the right resolution and I would not disturb it.

Doc_07 §6's "Cells 3A/3B — nothing the library attests within 1517–1545" was a reasonable provisional call, and correcting it is not a fault of Doc_07: it is what §12 item 3 asked Doc_08 to do. Doc_08's handling — correcting by placement, not by editing an approved document, and logging it at §11 item 4 — is the right procedure.

**(b) Is [F-resp] correctly Internal at 1B-2? — Yes, it stands, but the disclosure needs C5's addition.**

The Framework defines Internal as "forces originating **within the world's own community**… These are what the world was doing to itself," and External as forces "originating outside the world's own community… what the world was responding to from outside itself." The decisive question is where the *force* sits, not where its cause sits, and the force Doc_01 §7 named is a need carried in the bodies of the people who became this world — its founder a friar under vows, its 1529 "we" the people who "went from mere compulsion and fear" (LC 4304–4307, verified). The apparatus that produced the need is external and is separately carried at 1A-2 and 1B-3, so nothing is lost. The Framework's 1B example the draft cites ("inherited practices from a prior tradition that were reinterpreted under new conditions") is the right one.

But the External definition's own closing gloss cuts the other way and is not quoted: "what the world was responding to from outside itself" is almost word-for-word Doc_01 §7's own heading for this force. A disclosure that does not put the strongest counter-text on the page is not yet a full disclosure. Add it (C5); the placement does not change, and the document's own "nothing in Section 5 depends on which cell it sits in" is true — I checked: every §5 entry that cites 1B-2 (G1, G4, G5, G11) states the same relation either way.

**(c) Is the codeless 2B-3 a defensible construction? — Yes, and it is not a conflation of a gravity with a force.**

The worry is that G13 is a Tensional *gravity* — a founder's complaint-register — and that entering "the force G13 documents" as a 2B force turns a gravity into a force. Doc_04's own text forecloses that reading. G13's forces-connection notation states, in Doc_04's voice: "This gravity **is Layer 2 of a force** Doc_02 §13 could not document at Layer 1 — the parish's actual state." And Doc_04 twice uses that force in the same grammatical slot as its coded forces, in *other* gravities' notations: G4 is "**Intensified under the internal force G13 documents**," and G8 is "**Reversed under the force G13 documents.**" A force named three times by the source document, twice as the agent of another gravity's change, is a force. Doc_08 is following Doc_04, not inventing.

Two refinements. First, the entry is unusually honest about its own shape — a force whose Layer 1 is an absence and whose Layer 2 is the library's fullest material is genuinely strange, and 2B-3's Layer 1 states it as such rather than filling the gap. Second, the fourteenth-code question at §11 item 3 should record that Doc_04 has already bracketed this force as "[F-ter]'s inspecting arm" (C6), so that Doc_04's owner decides between *adding* a code and *recording* the existing one, rather than between adding and nothing.

---

# WHAT WAS CHECKED AND FOUND CLEAN

- **Vendored quotation fidelity.** 173 quote/locus pairs; 156 verbatim inside the cited range, 8 verbatim spilling one line past it (TT 3063–3064, v2 6686, v2 14727–14728 twice, TT 3134–3135, v2 15325–15326, v1 404–405, LC 3433 — all eight opened and read), 9 residuals all adjudicated at the file. **Zero genuine mis-quotations of a vendored text.**
- **Prior-document quotation fidelity.** 125 pairs tested; the only genuine defects are S6 and C2. Every other flag was my parser's pairing artefact. Load-bearing quotations of Doc_01 §7, Doc_02 §13, Doc_02 §12.2, Doc_04 §2.2, Doc_04 §3 (G1, G3, G4, G6, G8, G10, G11, G12, G13), Doc_05 §1.4, §2.5(b)–(e), §9B, §13 item 13, Doc_07 §6, §7 and §12 item 3 all verify verbatim in the cited document.
- **The thirteen-of-thirteen gravity claim**, re-derived mechanically from Doc_04 §3's notations and compared row by row. No gravity has an empty row. §5's by-gravity index view and §5's prose agree on all thirteen rows and all thirteen counts.
- **The cross-cell map (§4) against §4's prose.** Thirteen connections; every participant pair, every direction glyph and every cited ground matches. (The two defects are in the Force Index, S4, not in the map.)
- **The §3.0 table's cell assignments.** Every cell assignment is right on Doc_04's own text, including the two rows whose notation lists are wrong (S2). [F-pop] → 2A is correct; [F-ref] → 2A by located absence is correct; [F-print] → 1A and 2B is correct; [F-sel] → 2B and 3B is correct.
- **The economic-datum fold.** Verified at the vendored file: the Large Catechism's Fourth Petition runs LC 3445–3541, so LC 3535–3541 and LC 3471–3484 are one petition. Doc_05 §13 item 13's instruction ("for Doc_08's Layer 2 under an existing cell; no new force code") is discharged exactly, and no code is added.
- **R94's bar,** read in full and tested item by item. Clean. Doc_02 §12.3's 1543 bar is observed — the treatise is named, dated and not characterized beyond §12.3, and its scholarly contest (Kaufmann/Wallmann) is carried at §7 item 5 with the tags Doc_02 assigns. Doc_02 §12.4's 1525 bar is observed — the content is characterized at Doc_02's own tags ([Widely Accepted], not Documented; Blickle as DMR), and no phrase of the tract is quoted.
- **Living Tradition (Constitution Articles 28–29).** No characterization of present-day Lutheranism anywhere. The 1546–1580 half of Doc_01's window enters only by bare reference ([R53]; Doc_01 §8.0), as Discipline 2 declares. 3B-2's Layer 2 explicitly refuses to characterize what successor communities understood themselves to be preserving.
- **Representative scope.** No name, no biography, no voice, no first-person content, no identity or title decision. Every "Representative" sentence is a construction consequence.
- **Reported-Experience Status.** Six Layer 2 entries carry `[RES]` — 1A-2, 1B-1, 2B-2, 2B-3, 3A-1, 3B-1 — matching §7's list and §9's count exactly, with the ten total occurrences accounted for by §0, §8, §9 and §10.
- **Discipline 6's line.** Every Layer 3 paragraph scanned; no sentence says a household or parish *did* anything, and G13 is never cited as evidence of any congregation's state. S7 is the single clause that needs a qualifier.
- **The template.** Nine sections in order; Section 1's seven fields exactly as the template lists them; the twelve checklist items reproduced in the template's own wording and order; the two disclosed header discrepancies verified at the template ("Produced at: Construction Step 7"; "Forces Framework v1"), against CF V7.4's "Step 8 — Forces Document" and the governing file's V1.1.
- **Transmission Specificity (Principle 5).** Both required entries exist as dedicated forces with their own three layers (2B-2, 3B-2), both cells carry the blockquote note, §6 synthesizes, the lineages are named individually with their stated interests and Registry rows, exclusions are named with reasons, and the Author Gravity connection to Doc_02 §3 is drawn explicitly. I verified four of the lineage claims at source: R93 (Melanchthon's oration, 22 February 1546, "the earliest *Vita* of Luther"), TT 106–114 (Aurifaber as *famulus* in 1545–46), Co 198–204 (Melanchthon's edition "published immediately after Luther's death," with the "Melkncthon's" OCR disclosed), and Doc_02 §3.1 ("the Weimar critical edition (from 1883) as base"). All four hold.
- **Word count.** `wc -w` = 24,818, against §12's "24,800 words to the nearest hundred." Accurate.
- **G12's "nine Layer 2 entries" count** (1A-2, 2A-1, 2A-2, 2A-4, 2A-5, 2B-1, 2B-3, 3B-1, 3B-2), checked entry by entry. Nine, and Doc_04 §3 G12's instruction ("Doc_08's Layer 2 should expect to lean on it heavily; that is a forces role, not a reason to raise the tier") is discharged without touching the tier.
- **§10's instruction table.** Every row spot-checked against the cited source; no false discharge found. Doc_01 §7's closing sentence, Doc_02 §13's forces sentence, Doc_04 §1's "Doc_08 will compile the full matrix," Doc_04 §10 items 1/3/4/9, Doc_05 §2.5(e) and §13 item 13, and Doc_07 §12 item 3 all verify verbatim and are all genuinely discharged where the table says. The only instruction I found addressed to Doc_08 and not listed is Doc_03 6.9 / Doc_06 4.7's "Doc_08's forces material more than the lexicon's" for the Turk — discharged in substance at 2A-5, just not rowed.
- **Proportionality in both directions.** 2A-5 (the Turk, 212 words) is the Principle's own case and is argued as such. 2A-6 and 3A-2 are brief for the inverse reason and say so at each entry. I found no force given padded three-layer treatment on thin evidence: every full entry rests on multiple named loci, and the two thinnest full entries (1A-3 at 342 words, 2B-4 at 316) are proportionate to what the library holds.

---

# DOCUMENT LOG

- **Review:** Doc_08 Forces Document, Round 1 — independent adversarial review, cold, full-document. Lutheran Wittenberg & Its Congregations (`witt`).
- **Reviewer:** independent; no drafting involvement; no prior context on this world beyond the files read this pass.
- **Date:** 2026-09-16.
- **Read this pass:** `witt_Doc_08_Forces_Document.md` in full (758 lines); the Forces Framework V1.1 extracted from the `.docx` and read in full; the L4 `[world-code]_Forces_Document.md` template v1.1 in full; `witt_Doc_04_Historical_Gravity.md` §1, §3 (all thirteen entries), §4, §5, §6, §7, §9, §10; `witt_Doc_02_Source_Ecology.md` §12 and §13 in full plus targeted reads at §1.1–§1.4, §3.1, §4, §6; `witt_Doc_05_Ecological_Reconstruction.md` §1.4, §2.5, §9B, §13; `witt_Doc_07_Integrated_Ecology_Analysis.md` §6, §7, §12; `witt_Doc_01_World_Identification_Boundaries_Orientation.md` §1, §5, §7; `witt_Source_Registry.md` Conventions, tallies, R48, R49, R69, R93, R94; `Open_Gaps_Tracking.md` OG-8 and OG-11 in full; `witt_Doc07_Review_Round1.md` (finding S6 and the observations); the ten vendored texts in `cic/texts/` at the loci named under Method.
- **Built and run this pass:** three checkers, written from scratch (a vendored-quotation checker at three padding widths; a prior-document quotation checker; a mechanical inverter of Doc_04 §3's thirteen forces-connection notations). Counts as reported under Method. The checkers are one-off review artefacts and are not retained as repository files; their method is stated so the result can be re-derived independently.
- **Not re-litigated:** Doc_04's thirteen classifications and tiers; Doc_02's confidence tags and boundary determinations; Doc_07's lens spine and synthesis; the Registry's row tiers. Only Doc_08's use of them was checked.
- **Result:** **SUBSTANTIAL REVISION REQUIRED** — 8 substantial findings (S1–S8), 8 cosmetic (C1–C8), 5 observations (O1–O5), and three rulings delivered on the questions the draft raised. No escalation category applies to anything in this review; §11 items 1–2 remain correctly flagged for the coach thread rather than escalated.
- **Recommended next round:** a targeted recheck of the eight substantial repairs only, not a full re-review — with one exception: S2 and S3 are both re-derivation failures in index artefacts, and Round 2 should re-run an *independent* inversion of Doc_04 §3 and of §5 rather than confirming the build thread's own sweep, since OG-8's recorded pattern is that a hand sweep of exactly this kind fails silently and is caught only from outside.
- **Harness note:** the shared-checkout path `/home/user/cic-project/World-Builds/Lutheran-Wittenberg/witt_Doc08_Review_Round1.md` was refused to this worktree-isolated session. This file was written at the equivalent worktree path `/home/user/cic-project/.claude/worktrees/agent-a76fb2b47425af218/World-Builds/Lutheran-Wittenberg/witt_Doc08_Review_Round1.md` and should be copied to the shared path.
