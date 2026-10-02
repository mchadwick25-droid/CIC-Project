# Doc_10 — Representative Emergence (Renatus): Bounded Round 2 Spot-Check

**Reviewer:** independent fresh-context subagent (model opus). No drafting involvement, no involvement in Round 1.
**Date:** 2026-09-10.
**Scope:** BOUNDED spot-check of the Round 1 fix round only — the 23 findings recorded in `gallic_Doc10_Review_Round1.md` (H1, H2, M1–M11, L1–L10), plus four cross-cutting checks (full propagation, new-defect, word-count/structural claims, standing-instruction re-check). This is **not** a fresh full review; nothing outside those items was re-reviewed.
**Documents checked:** `gallic_Representative_Permanent_Prompt_Renatus.txt` (59 lines / 5,257 words) and `gallic_Representative_Construction_Notes_Renatus.md` (460 lines), both at their current on-disk state (commit `b40ab18`).

**Method.** Read `gallic_Doc10_Review_Round1.md` in full, then the Document Log (Notes lines 431–459), then both deliverables in full. Independent machine checks run this pass:

- RCF V3.2 re-extracted directly from `word/document.xml` (unzip + XML strip, 65,939 chars — identical length to Round 1's extraction) and grepped for every H1 term.
- Full `git diff 9f29f4e..b40ab18` of the Permanent Prompt, giving the complete, exhaustive list of the twelve prompt-side edits the fix round made.
- Byte-diff of the Construction Notes' Section 2A blockquote against the deployed Section 2A paragraph (Python string equality, not eyeballing).
- Independent word count of the prompt (pre-fix and post-fix), token estimate, and boilerplate/world-specific segmentation against `L3B-World-Build-Methodology/Representative_Permanent_Prompt_Template.txt`.
- Independent recount of sentences over 35 words, mean sentence length, Flesch Reading Ease and Flesch-Kincaid, over world-specific prose and boilerplate separately, both pre-fix and post-fix.
- Standing-instruction sweep: regex sweep for `I` / `my` / `mine` / `me` / `myself` over the world-specific prose only, plus a name-and-place sweep (Ligugé / Marmoutier / Saint-Victor / Saint-Sauveur / Trier / Treves / Condate / Amiens / Poitiers / Augustine / Benedict / semi-Pelagian / Massilian / Chalcedon / Antony / Athanasius) and an analytical-distance-marker sweep against check 5's own word list.
- Direct re-reads at source loci: Doc_07 §7 (Notes template M6), Doc_05 §1.1 and §1.3(a)/(b) item 1 (M8), Doc_08 Force 2A-5 (M5), Doc_04 §6 and Doc_07 §5 (M7), Source Registry rows 7, 8, 9, 10, 13, 26, 27, 43 (L4, L5, L8, M4), `L4-Templates/Representative_Construction_Notes_Template.md` §1 lines 130–139 and its Builder Confirmation Note lines 794–803 (H1, L9).
- Grep sweep of the Construction Notes for every other instance of each corrected claim ("as the texts do," "corroborat*," "RCF default," "all nine," "ten Registry rows," "we do not invent it," "at every point where they diverge").

---

## Finding-by-finding verification

### H1 — RESIDUAL ISSUE (High)

**The four named loci are fixed; a fifth locus, never visited, still carries both halves of the original misattribution.**

Source check first, independently reproduced. Grep counts over the freshly extracted RCF V3.2 text: `strand` = 0, `register-range` = 0, `register range` = 0, `communion` = 0, `refused each other` = 0, `single voice` = 0, `one voice` = 0, `multiple-named-voices` = 0, `V7.2` = 0, `Voice Grounding` = 0. RCF Part Four's only register language remains the different concept Round 1 identified: "What guards against genericism is no longer a single chosen biography but **unity of register**: the voice must speak, always and only, in this world's own distinctive manner." Every element is instead at `L4-Templates/Representative_Construction_Notes_Template.md` lines 130–139: "the default is that this Representative holds all documented strands together as one register-range … e.g., communions that refused each other's 'we.' … may require the multiple-named-voices construction (Construction Framework V7.2, Representative Voice Grounding)." Round 1's diagnosis is fully confirmed.

The four loci the Document Log claims were fixed **are** fixed, and correctly:

- Notes line 11 (top structural note): "per the Representative Construction Notes Template's own default (v2.2 §1) — RCF V3.2 Part Four supports this in substance … without itself stating a strand-attribution framework." ✔
- Notes line 25 (Section 1, Strand attribution): "**The Construction Notes Template's own stated exception to the single-voice default** (v2.2 §1, corrected, Round 1 review finding H1 — the prior draft attributed this default and this quoted exception to RCF V3.2 Part Four, which contains no strand-attribution framework at all …)." ✔
- Notes line 394 (Judgment 1): "Decided per the Construction Notes Template's own default (v2.2 §1, corrected, Round 1 review finding H1 — see Section 1)." ✔
- Notes line 418 (Conditions That Would Trigger Revision): "reconsidering the multiple-named-voices construction (**Construction Framework V7.2**, Representative Voice Grounding, via Construction Notes Template v2.2 §1's own cross-reference)." ✔

**But Notes line 380 (Section 8, Scholarly Questions, Question 1 — "One world or two") was not visited and still reads:**

> "This construction holds both nodes in one "we" on the **RCF default** and the identity decision's instruction … it names the consequence if Step 0 resolves it toward two lineages: the single-voice construction would need re-examination against **the RCF's multiple-named-voices allowance**."

Both halves of H1 survive verbatim at this locus: the default is attributed to the RCF (it is the Template's) and the multiple-named-voices allowance is attributed to the RCF (it belongs to Construction Framework V7.2). This is the same defect at a fifth locus, in the section a reviewer reads *for* the disclosed uncertainty on this exact decision — and it now sits four lines above the corrected Judgment 1 that says the opposite, so the document also contradicts itself internally.

The Document Log's "Naming/term propagation check" (line 456) asserts: "the H1 attribution correction … [was] checked against every other place in the Construction Notes those exact phrases or claims appear; **no further stale instance was found**." That assertion is false. Line 380 was not caught. This is precisely the build's established Round-2 failure pattern — the same defect surviving in a place the fix round did not visit, under a propagation-check claim reused without re-verification.

### H2 — RESIDUAL ISSUE (Medium)

**All three loci Round 1 named are fixed; a fourth locus in the prompt, which Round 1 miscounted, is still unmarked, and the Notes' corrected claim asserts the wrong count.**

The three named loci now mark origin:

- Prompt line 27: "Among those who read Cassian, it is purity of heart, which is charity — **the fathers' own mark**, the definite thing the archer fixes his gaze on …" ✔
- Prompt line 35: "What he aims at, in the south, is purity of heart, **the fathers' own mark**." ✔
- Prompt line 47: "the aim the practice serves: purity of heart **received from the fathers**, the example that draws others, the faith kept whole." ✔

The Notes' claim (line 67) now quotes accurately — I verified the quoted string is present byte-for-byte in the deployed prompt: "the prompt says 'Among those who read Cassian, it is purity of heart, which is charity — the fathers' own mark.'" The Round 1 falsification (a claim disproved by the very text it quoted) is repaired: "the fathers' own mark" does discharge Doc_06 §4(a)'s "as *received*" rule.

**Residual (a) — a fourth deployment locus, unmarked.** `grep -c "purity of heart"` on the prompt returns **4**, not 3, and returned 4 in the pre-fix file as well (verified by `git show 9f29f4e:…`). Round 1's "three times" was a miscount, and the fix round fixed exactly the three Round 1 named. The fourth is prompt line 57, inside the Christ-Ward Telos paragraph:

> "What we aim at is purity of heart, which is charity, and the kingdom which is its end."

No origin marking, and no node marking either, on a term the Notes themselves classify as "single-voice, Cassian's" and a gravity (G7) they classify as "Supporting, node-bound southern." The paragraph's opening ("Everything we became was handed to us … The customs were the fathers'") supplies a general reception frame, which is why this is Medium and not High — but the specific clause reads as the whole "we"'s own aim, which is the (i) half of Doc_06 §4(a)'s risk, and it is also the one point where Section 1's "at every point where they diverge" certification (M10's own standard) is unmet for a node-bound southern gravity.

**Residual (b) — the count claim.** Notes line 67 states the origin-marking was "added at **all three** deployment loci." There are four deployment loci. The Notes certify completeness against a number that is wrong.

**Residual (c) — a smaller carry-over.** The same parenthesis still reads "framed as Abbot Moses's received teaching." Abbot Moses is named nowhere in the prompt; "the fathers' own mark" marks the fathers generally. The claim is now defensible as a description of the term (per chunk 006) rather than of the prompt, but the sentence still reads as though the prompt carries the Abbot Moses framing.

### M1 — CONFIRMED FIXED

Prompt line 31 now reads: "A coerced communion with bishops who had shed blood left the saint at Tours **feeling a diminution of his power, and he lived sixteen years after, but never again went to a synod.**" The duration now attaches to his remaining life and the synod-avoidance, exactly as *Dial.* III.13 / gallicstory005 has it ("He lived sixteen years after this, but never again did he attend a synod"), and the diminution is stated as felt, matching Doc_08 2A-3's own rendering ("he felt a diminution of his power on account of the evil of that communion"). No duration is now attached to a Reported-Experience-Status claim. Notes line 438 describes the fix accurately.

### M2 — CONFIRMED FIXED (both loci)

Prompt line 49 now reads: "But not one of them left us her own word." The clause "and we do not invent it" is gone from the prompt (grep over the whole build directory returns it only inside the Notes' and Round 1 review's *descriptions* of the removed text). Notes line 128 quotes the corrected sentence and states the removal. Both loci touched.

### M3 — RESIDUAL ISSUE (Medium)

**Two loci fixed, a third left standing with the exact defective claim, producing a new internal contradiction.**

Fixed:

- Notes line 69 (Terms considered and rejected): now "the prompt describes the places without them, in wording drawn partly from this build's own analytical layer rather than the ancient text's own words at every point (corrected, Round 1 review finding M3 … the *Vita*'s own words at its cited locus, *Vita* X, `ii.ii.xi`, are 'about two miles outside the city' …)." ✔
- Notes line 398 (Judgment 3): now "describing the places instead in wording drawn from this build's own analytical layer and the ancient texts together, not from the ancient texts alone (corrected, Round 1 review finding M3 …)." ✔

**Not fixed — Notes line 160, in Section 3's "What Was Excluded and Why" list:**

> "- **The editorial place-names** Ligugé, Marmoutier, Saint-Victor, Saint-Sauveur: not in the ancient texts as this build reads them (Doc_09 H2; Doc_05 §1.3 trace 1); **the prompt describes the places as the texts do.**"

That is verbatim the claim M3 falsified, at the third locus in the same document, and it is now in direct contradiction with the two corrected loci. `grep -n "as the texts do"` returns exactly this one hit. The Document Log (line 440) claims M3 was "fixed at both loci"; there were three.

### M4 — CONFIRMED FIXED

Notes line 88, Approved Source List grouping 2, now reads: "**Seven of these eight items** are Egyptian or Eastern content Cassian frames as received, and the prompt says so ('always as theirs'); **the eighth, the Gallic Gloria, is the one item in this grouping Cassian expressly marks as *not* Eastern** ('we have never heard anywhere throughout the East,' *Inst.* II.8) and Doc_06 §4(a) names among the things that are Gaul's own." I counted the grouping's own list independently: girdle, angel's twelve psalms, Gallic Gloria, three lentils, Pæsius and John, fast broken for a guest, vainglory's wish for holy orders, "Not I" + the two-sided teaching = eight items, of which the Gloria is one. Arithmetic and characterization both correct.

### M5 — CONFIRMED FIXED

Doc_08 Force 2A-5 re-read directly (`gallic_Doc08_Forces_Document.md` line 216): "finds, in Sulpitius, **six textual occurrences across four distinct episodes**" — the discharge at the garrison of the Vaugiones (two occurrences, *Vita* IV); the demons' false rumour of an inroad (two occurrences, *Vita* XVIII); Avitianus's "too barbarous" ferocity (*Dial.* III.4); and Brictio and the barbarian captives (*Dial.* III.15).

Notes line 132 now reads: "Doc_08 2A-5's fuller, Round-2-corrected tally — one book, four Sulpitian episodes across six textual occurrences, one Egyptian-set occurrence). The prompt gives them a **proportionately thin but narrower selection than that fuller tally** — 'one indignant voice,' and two of the four Sulpitian episodes (the discharge scene, the demon's lie) — **rather than all four**." The prompt (line 49) gives exactly two: "once as the occasion of his discharge and once as a demon's lie." The false "exactly that proportion" certification is gone and the replacement is accurate.

### M6 — CONFIRMED FIXED (both loci)

Doc_07 §7 re-read directly at its own locus (`gallic_Doc07_Integrated_Ecology_Analysis.md` line 220). Its own text is exactly what Round 1 quoted:

> "That thinness is what a person formed in this world, from what has survived of it, would themselves be able to speak to — **with one qualification the Representative must carry**: the silence on the body and on women's formation is partly an edition's and partly the sources', and the two must not be blurred (Doc_02 §10; Doc_05 §1.3(a)'s Facilitator hand-off)."

Doc_05 §1.3(a) re-read directly (line 93): its hand-off is scoped as the fix now claims — "whoever builds this world's Facilitator apparatus should receive this paragraph directly. **A participant asking this world's Representative about women's formation** must be told …" — i.e. to women's formation, not to the edition-level chastity excisions.

Both loci corrected and both now accurate:

- Notes line 136 (thin domain 7): "**Doc_07 §7 itself is on Doc_09's side of this conflict, not the Framework's** (corrected, Round 1 review finding M6 — the prior draft claimed Doc_07 §7 'routes to the Facilitator hand-off'; at its own locus §7 states the opposite …). So the resolution below is one Approved document (Doc_09, and Doc_07 §7 alongside it) overruled by the governing Framework, not two Approved documents agreeing against a third." ✔
- Notes line 402 (Judgment 5), title and body: "against Doc_09's **and Doc_07 §7's** own usage guidance … **overruling Doc_07 §7's own hand-off assignment rather than agreeing with it**." ✔

A third locus (the Final Assembly Confirmation's escalation note, line 427) was also correctly updated to "Doc_09's usage guidance, **and Doc_07 §7's own hand-off assignment**" — a propagation the fix round made beyond what was asked. The substantive resolution (follow the RCF; route disclosure to the Facilitator) is unchanged, correctly.

### M7 — CONFIRMED FIXED

Notes line 25 now carries both halves of both loci, with both source quotations verified at their own loci this pass:

- Doc_07 §5 (`gallic_Doc07…` §5): "a finding about mechanism, offered here as one additional, specific fact for Step 0 to weigh, **not as a resolution, partial or otherwise** …" and "the seen/read axis is a real, consistent pattern in *how* they differ where they do, **not evidence that they do not**." Both strings verified verbatim. ✔
- Doc_04 §6 (`gallic_Doc04…`): "the gravity evidence is consistent with *one world in two modes* … and **equally consistent** with *two lineages that share a Latin-monastic inheritance*"; "the fact that G3 and G6, the two gravities that give each node its *particular* character, **never meet in any text is the strongest** for two." Both verified verbatim. ✔

The Notes' rendering of each is faithful, and the corrected passage now says the two loci state both halves rather than presenting only the pro-unity half.

### M8 — RESIDUAL ISSUE (Low)

**The named locus is fixed; a second locus carrying the same overstatement was not visited.**

Fixed at Notes line 94: "the Representative is built on in-window facts Gennadius **attests** … '**Corroborates**' overstates Gennadius's role for one of these three: for the two houses at Marseilles, Gennadius is not a corroborating second witness but the ***only*** one — Doc_05 §1.1 and §1.3 item 1 rate the women's house Documented on that single c. 495 source alone, with no in-window Native text attesting it."

Verified at source. Doc_05 §1.1 (line 67): "Cassian's own house is two: **Gennadius's** 'two monasteries, that is to say one for men and one for women, which are still standing' (ch. LXII, ancient text, Doc_02 §1.2)." Doc_05 §1.3(b) item 1: "**A women's house at Marseilles** — 'one for men and one for women, which are still standing' (Gennadius ch. LXII, ancient text, c. 495). **Documented.**" — a single source, with no second witness listed. Round 1's finding is confirmed, and the correction is accurate.

**Not fixed — Notes line 158, in Section 3's exclusion list:**

> "- **Gennadius's own words and Richardson's dates** (rows 30, 42): post-window and editorial respectively; only the in-window facts Gennadius **corroborates** are used."

The exact word M8 identified as the overstatement, at a second locus in the same document, uncorrected. `grep -n "corroborat"` returns four hits: line 21 (correct usage — G1/monk-bishop, where Gennadius genuinely does corroborate Sulpitius and Cassian), line 94 (fixed), line 158 (residual), line 445 (Document Log). Low, because line 158 is a summary line rather than the evidential-discipline claim M8 targeted — but it is the same defect and it was missed by the same propagation check.

### M9 — RESIDUAL ISSUE (Medium) — a new defect introduced by the fix round itself

The correction itself was applied. Notes line 338 now reads: "the boilerplate itself (untouchable per 5d) contains **thirteen** sentences over 35 words, and the world-specific prose contains **one** — Section 2A's 'What Sulpitius wrote of Martin…' sentence, 36 words (corrected, Round 1 review finding M9 …)."

I reproduced Round 1's count exactly on the current file (sentence split on terminal `.!?`, punctuation-only tokens excluded, template Section 1 boilerplate = prompt paragraphs 2–8 segmented separately): **boilerplate = 13 sentences over 35 words**, at 84, 52, 51, 50, 48, 46, 42, 42, 40, 39, 39, 37, 36 — matching Round 1's stated series (84; then 52, 51, 50, 48, 46, 42, 42, …) exactly. The boilerplate figure is correct and the boilerplate is untouched (the diff confirms zero edits inside paragraphs 2–8).

**But the world-specific figure is no longer one. It is four, and three of the four were created by the fix round's own edits.** Verified by running the identical count against the pre-fix file (`git show 9f29f4e:…`), which returns exactly one — Round 1's finding is exactly reproducible pre-fix:

| Sentence | pre-fix | post-fix | created by |
|---|---|---|---|
| "And one thing that is ours in this country and not Egypt's … loud — a thing we have never heard done anywhere throughout the East." (prompt line 29) | 34 | **40** | the L1 fix |
| "The last of these, **and the island beside it**, received the customs …" (prompt line 1) | 32 | **37** | the L6 fix |
| "Among those who read Cassian, it is purity of heart, which is charity — **the fathers' own mark**, the definite thing …" (prompt line 27) | 33 | **37** | the H2 fix |
| "What Sulpitius wrote of Martin: the cloak halved at the gate …" (prompt line 37) | 36 | 36 | pre-existing (Round 1's one) |

So the Register-Fidelity entry's corrected claim is stale as written, and two disclosure sentences are falsified by it:

- Notes line 71: "these figures predate the Round 1 fix round; that round's edits … were not re-measured, though they are small enough in aggregate … that **no material change to these figures is expected**." For mean sentence length, FRE and FK that prediction holds (my recount: mean 16.55 vs. the stated 16.7; FRE 73.7 vs. 73.9; FK 7.1 vs. 7.1 — all immaterial). For the >35-word count it is wrong by a factor of four.
- Notes line 338: "These figures predate the Round 1 fix round and were not re-measured after it" — an honest disclosure, and the reason this is Medium rather than High, but the sentence immediately above it states "**one**" as a fact without hedge, and a reader of Section 7 takes it as the corrected count.

This is the fix round breaking something the correction had just made right, at the one metric M9 was about.

### M10 — CONFIRMED FIXED

Prompt line 31 now reads: "… and he lived sixteen years after, but never again went to a synod. **On the island,** councils and the Apostolic See guard antiquity; the bishops at Ephesus innovated nothing, presumed nothing." The southern half now carries its node, matching the northern half ("at Tours") in the preceding clause. The valences meet at a marked seam, and lexicon 059's own two-ended divergence is now reported at both ends. Section 1's "at every point where they diverge" certification is met at this sentence. (One further unmarked southern locus is noted under H2 residual (a) — prompt line 57 — but that is the H2 defect, not this one.)

### M11 — CONFIRMED FIXED

Prompt line 23 now reads: "The number of the psalms, **as the fathers of Egypt received it**, was no appointment of man's invention; an angel sang eleven, and the twelfth with Alleluia, and vanished." gallicstory008's Usage Guidance — "the Representative **must name the origin** … it is Egypt's story, received at Marseilles" — is now satisfied at this locus, and the sentence no longer reads as the world's own founding memory of its own office. The two loci where the discipline was already present (prompt lines 29 and 37) are unchanged.

### L1 — CONFIRMED FIXED

Prompt line 29: "… we all stand and sing Glory be to the Father, loud — **a thing we have never heard done anywhere throughout the East**." *Inst.* II.8's first-person frame ("we have never heard anywhere throughout the East") is restored; the objective claim about the East is gone.

### L2 — CONFIRMED FIXED

Prompt line 23: "He would not lend the multitude his authority." The false conditional "until they answered" is deleted. *Vita* XI stages no conditional, and the prompt no longer implies one.

### L3 — CONFIRMED FIXED

Prompt line 37: "the death on ashes and **the almost two thousand monks said to have walked behind him**." Both of *Ep.* III's hedges — the report-frame ("are said to have") and "almost" — are restored.

### L4 — CONFIRMED FIXED

Notes line 85: "in six groupings (within the RCF's 5–10 *entry* band) covering **twelve** Registry rows (corrected, Round 1 review finding L4 — the prior draft said 'ten'; the six groupings below cite rows 1, 2, 3, 6, 7, 8, 9, 10, 13, 27, 26, 43)." I counted the groupings independently: grouping 1 cites rows 1, 2, 3, 6; grouping 2 cites row 7; grouping 3 cites rows 8, 9, 10; grouping 4 cites row 13; grouping 5 cites row 27; grouping 6 cites rows 26 and 43 = **twelve**. Header, enumeration and groupings all agree.

### L5 — CONFIRMED FIXED, with one small new inaccuracy (Low)

Registry row 9's Confidence cell re-read directly (`gallic_Source_Registry.md` line 25): "**A (dedication text) / B (editorial identification of Lérins/abbot) / C (content, except Conf. XIII)**." Notes line 89 now quotes that cell verbatim and states: "**B covers only the editorial Lérins/abbot identification, not content generally**." The misstatement L5 identified is corrected and the quotation is exact.

**Small new inaccuracy introduced.** The grouping-level summary was rewritten from "A for the dedication texts, **B/C for content**" to "A for the dedication texts, **C for content** (except *Conf.* XIII, C's own stated exception) per the Registry's own tiers." Grouping 3 covers rows 8, 9 **and 10**. Row 8's cell is "A (dedication/dating) / C (content)" ✔, row 9's is as quoted ✔, but **row 10's cell is a flat "B"** with no A/C split at all. The new summary is therefore accurate for two of the grouping's three rows and inaccurate for the third — the old wording at least gestured at a B. Low, and a one-clause fix.

### L6 — CONFIRMED FIXED

Prompt line 1: "The last of these, **and the island beside it**, received the customs of the fathers of Egypt and the East from the man who had lived among those fathers …" This now agrees with prompt line 25 ("Among the brethren at Marseilles **and on the island**, the fathers of Egypt are the standard we received") and with *Conf.* Pref. III's rule of anchorites addressed to the Lérins dedicatees. The internal inconsistency is gone.

### L7 — CONFIRMED FIXED

Notes line 408 (Judgment 8): "runs to roughly **5,250 words** … the template's target is 1,500–3,000 tokens, and **5,250 words is roughly 7,000–7,500 tokens — better than double the ceiling, not the ~1.7× a word-to-word comparison alone would suggest**." Independent verification: `wc -w` on the current prompt returns **5,257** ("roughly 5,250" ✔); the pre-fix file returns 5,223, so growth is 34 words, matching Notes line 71's "grew by roughly 30 words" ✔. The token estimate is sound at the usual ~1.3–1.4 tokens/word ratio. The unit mismatch is corrected and the overage remains disclosed rather than hidden.

### L8 — CONFIRMED FIXED

Prompt line 27 now reads: "That was a presbyter at Marseilles, **one of Honoratus's own household**, who wrote of the ruin itself as judgment falling now, **not for the cell**." Both unsupported flat statements are gone: the Lérins-teaching claim resting on Sanford's 1930 Introduction (editorial, no Registry row) is removed, and "for the lapsed Roman" as an addressee characterization is replaced with a content description grounded in Doc_08 2A-5 Layer 2 ("the present judgment of God was clearly shown," *Gov.* VII.10) and Doc_05 §1.4. The replacement tie to Honoratus's circle rests on Registry row 27's own verification note, which I read directly: Hilary of Arles's funeral sermon "names him '*charorum suorum unus*' — one of Honoratus's own dear associates," verified there against the vendored Latin. Minor note, not a finding: "household" is a slightly stronger rendering than "dear associates," and this is a row-27 (Inferential/Thin wording) source that the prompt marks "as far as those words can be read" only at its *other* row-27 deployment (line 37). Defensible as it stands.

### L9 — CONFIRMED FIXED

Notes line 425 now reads: "Section 7 records **all eight Part Eight probe categories** (Source-Awareness, Anachronism, Confidence-Under-Thinness, Self-Referential, Scholarly-Framework, Relational Safety, Claim-Laundering/Decontextualization, Sustained Engagement) … **plus the Register-Fidelity entry — a Part Five build-time construction check, not a ninth Part Eight probe category, per the template's own Builder Confirmation Note**." Eight named, count correct. Verified against the template's own Builder Confirmation Note (`L4-Templates/Representative_Construction_Notes_Template.md` lines 794–803), which lists exactly those eight and states parenthetically: "(Register-Fidelity is a Part Five construction check, run at build time — recorded in Section 7 where conducted, but not a Part Eight probe category.)" `grep "all nine"` over the Notes now returns only the Document Log's own description of the fix. Section 7's own Register-Fidelity entry still self-labels correctly ("Build-time assembly check only (not a probe result)").

### L10 — CONFIRMED FIXED

Notes line 156 (Section 3 exclusion list, row 36) now carries the reconciliation: "**Reconciled with Section 6, which does cite row 36 and Doc_01 §8.3 (RB 73, RB 42) as the evidential ground for the prompt's own afterlife sentence** … (added, Round 1 review finding L10 …): that sentence sits in the prompt's final, explicitly outside-the-horizon paragraph … **An Excluded row may ground what the Representative's own afterlife is said to include without becoming content he draws on inside his own horizon; row 36 is used only in the former way.**" Section 6 (line 265) is unchanged and still cites row 36 + Doc_01 §8.3 for RB 73 / RB 42. The two sections are now explicitly reconciled and the distinction drawn is the right one.

---

## Cross-cutting check 1 — full propagation

Findings whose fix touched more than one locus, checked exhaustively rather than at the first hit:

| Finding | Loci required | Loci touched | Result |
|---|---|---|---|
| H1 | 5 (Notes 11, 25, 380, 394, 418) | 4 | **line 380 missed** |
| H2 | 4 prompt loci + 1 Notes claim | 3 prompt + 1 Notes | **prompt line 57 missed; Notes count claim wrong** |
| M2 | prompt + Notes 128 | both | ✔ |
| M3 | 3 (Notes 69, 160, 398) | 2 | **line 160 missed** |
| M6 | 2 named (Notes 136, 402) + 427 | all 3 | ✔ (over-delivered) |
| M8 | 2 (Notes 94, 158) | 1 | **line 158 missed** |
| L1 / L2 / L3 / L6 / L8 | prompt | all present in diff | ✔ |
| L3 propagation | prompt + Notes blockquote | both | ✔ (see check 2) |

The `git diff` of the prompt confirms the fix round made exactly twelve prompt-side edits, one for each prompt-touching finding (H2 ×3, M1, M2, M10, M11, L1, L2, L3, L6, L8), with no unrecorded edits and no boilerplate touched.

## Cross-cutting check 2 — new-defect check

- **Section 2A re-sync: verified byte-identical by machine.** Python string equality between the deployed Section 2A paragraph and the Notes' blockquote at line 98 returns `True`, both **1,854 characters**. Round 1 measured 1,838 pre-fix; the +16 delta is exactly the L3 hedge restoration ("the two thousand monks who walked behind him" → "the almost two thousand monks said to have walked behind him"). The fix round's self-caught propagation catch (Document Log line 449, 455) is real and correctly executed. The Notes' framing at line 96 ("re-synced at Round 1 fix round … so this blockquote stays byte-identical with the deployed text") is accurate.
- **Every other Notes quotation of the prompt verified present verbatim** in the deployed text: the H2 quote at line 67; "not one of them left us her own word" (line 128); "Vincent, on the island, read the letter that came from the Apostolic See as written for the side of antiquity, which he held to be his own" (Test Exchange 1's recorded revision, line 203); "the almost two thousand monks said to have walked behind him". No stale quotation found.
- **New factual errors:** none in the prompt. Every fix-round edit was checked back to a source locus this pass (M1 → *Dial.* III.13/gallicstory005; M11 → gallicstory008; L1 → *Inst.* II.8; L2 → *Vita* XI; L3 → *Ep.* III; L8 → Registry row 27's verification note; M10 → lexicon 059/*Comm.* 31). No new unverified quotation is introduced.
- **New internal inconsistencies:** two, both in the Notes and both from incomplete propagation — line 160 vs. lines 69/398 (M3), and line 380 vs. lines 11/25/394/418 (H1). One small new inaccuracy at line 89 (L5, row 10).
- **Something previously correct broken:** yes, one — the world-specific >35-word sentence count (M9, above), raised from 1 to 4 by the H2/L1/L6 edits, at the exact metric M9 had just corrected.
- **Analytical-distance markers:** sweep of the world-specific prose for `sources`, `evidence`, `documentation`, `scholars`, `reconstruction`, `project`, `AI`, `language model`, `limitation`, `scope`, `historical context`, `formation world`, `architecture`, `this prompt`, `construction`, `documented` returns **zero**. Check 5 still satisfied after the edits.

## Cross-cutting check 3 — word-count and structural claims

- Prompt word count: **5,257** (Notes claim "roughly 5,250" ✔). Pre-fix 5,223; growth 34 words (Notes claim "roughly 30" ✔).
- Boilerplate ≈ 1,019 words, untouched by the diff (Judgment 8's "roughly 1,000" ✔).
- Token estimate 7,000–7,500 ✔ plausible for 5,257 words.
- Readability, world-specific prose, independently recomputed post-fix: 256 sentences, 4,238 words, **mean 16.55 w/s, FRE 73.7, FK 7.1** against the Notes' stated 16.7 / 73.9 / 7.1. Immaterial drift; Section 2's prediction holds for these three.
- Sentences over 35 words: boilerplate **13** ✔ (claim correct, series reproduced exactly); world-specific **4**, not one ✘ (see M9 residual).
- Final Assembly Confirmation's section-completeness claims re-checked against the edited documents: "All eight sections present" ✔ (Notes Sections 1–8 all present); Section 5's provisional open-flag blockquote verbatim ✔; Section 6 PENDING with outstanding items stated ✔; Section 7's eight categories all OUTSTANDING with "Prompts used: none yet / Finding: none / Revisions made: none" throughout ✔; Section 4's three exchanges present and labelled single-turn, same-hand, construction-time ✔; no brackets, no markdown labels and no builder notes in the prompt ✔. All nine Permanent Prompt sections remain present in substance — none of the twelve prompt edits removed a section element; the only deletions were the M2 clause and the L2 conditional, both intra-sentence.

## Cross-cutting check 4 — standing-instruction re-check (fresh and independent)

Clean. Nothing the fix round did touches it.

- Regex sweep of the world-specific prose for first-person-singular: `my` = 0, `mine` = 0, `myself` = 0. `I` = 3 and `me` = 3, and **every one is inside quoted world material**, not a Renatus claim: "Not I, but the grace of God with me" ×2 (*Inst.* XII.9, prompt lines 35 and 57), "Not I" ×1 (line 41), and "Abraham's bosom is about to receive me" (*Ep.* III, line 27). No first-person-singular claim of any kind is attached to Renatus.
- No invented biography, anecdote or personal memory is introduced by any of the twelve edits. The only edit that adds a biographical particular — "one of Honoratus's own household" (prompt line 27) — attaches it to **Salvian**, a documented figure, on Registry row 27's own directly-verified Latin, and it *removes* a weaker editorial claim rather than adding one.
- No node-specific anchoring for Renatus is introduced. The L6 edit ("The last of these, and the island beside it") *widens* the reception across two houses rather than locating the voice; the M10 edit ("On the island") attaches a valence to a house, not the speaker. The prompt still names all three houses in its first sentence, holds the "we" across them, and states the non-contact in voice ("Those at Tours and those at Marseilles never wrote of each other").
- Editorial place-name sweep of the prompt returns **zero** occurrences of Ligugé, Marmoutier, Saint-Victor, Saint-Sauveur, Trier, Treves, Condate, Amiens, Poitiers, Augustine, Benedict, "semi-Pelagian," "Massilian," Chalcedon, Antony, Athanasius. "Renatus" appears once, in the opening sentence.

**No High finding on the standing instruction. It survives the fix round intact.**

---

## Verdict

**Residual issues found.** The fix round did real, checkable work: all twelve prompt-side edits are present and correct at their loci, every one traces to a source locus that holds under direct re-reading, the Section 2A blockquote is genuinely byte-identical (1,854 chars both sides), the word-count and token claims are accurate to my own count, the standing instruction is untouched, and eight of the twenty-three findings that required multi-locus work were propagated completely. Fifteen of the twenty-three findings are confirmed fixed with no residue.

But the build's established failure pattern recurred in three of its three recognised forms — a fix asserted at every locus it touches but applied at fewer; a defect surviving where the fix round did not go; and a propagation-check claim ("no further stale instance was found," Document Log line 456) reused without re-verification and now falsified twice over. The Document Log's closing disposition — "both High findings and all eleven Medium and ten Low findings fixed" — is not accurate as written.

**What needs further fixing, in severity order:**

1. **[High] H1, fifth locus — Notes line 380 (Section 8, Question 1).** Replace "on the **RCF default** and the identity decision's instruction" with the Construction Notes Template v2.2 §1 attribution used at lines 11/25/394, and replace "re-examination against **the RCF's multiple-named-voices allowance**" with the Construction Framework V7.2 attribution used at line 418. As it stands the section that discloses the uncertainty on this construction's most consequential decision states the misattribution H1 was raised to remove, and contradicts Judgment 1 fourteen lines below it.

2. **[Medium] H2, fourth prompt locus — prompt line 57.** "What we aim at is purity of heart, which is charity, and the kingdom which is its end." Add the origin-marking used at the other three loci (and, if Section 1's "at every point where they diverge" is to hold, the southern node marker), or state explicitly in the Notes why the telos paragraph's own reception frame is held sufficient here.

3. **[Medium] H2, count claim — Notes line 67.** "with the origin-marking added at **all three** deployment loci" — there are four. Correct the count when item 2 is resolved. Consider also whether "framed as Abbot Moses's received teaching" should stand, since the prompt names no Abbot Moses at any locus.

4. **[Medium] M3, third locus — Notes line 160.** "the prompt describes the places **as the texts do**" is the exact claim M3 falsified, still standing in the exclusion list, and now in direct contradiction with the corrected lines 69 and 398. Rewrite it to match them.

5. **[Medium] M9, broken by the fix round — Notes line 338 (and the prediction at line 71).** The world-specific prose now contains **four** sentences over 35 words, not one: prompt line 29 (40 words, from the L1 fix), prompt line 1 (37, from the L6 fix), prompt line 27 (37, from the H2 fix) and prompt line 37 (36, pre-existing). Either re-measure and restate the Register-Fidelity entry, or remove the flat "contains one" and let the disclosure carry the whole claim. Line 71's "no material change to these figures is expected" should be narrowed to the mean/FRE/FK figures, for which it is true (my recount: 16.55 / 73.7 / 7.1).

6. **[Low] M8, second locus — Notes line 158.** "only the in-window facts Gennadius **corroborates** are used" repeats the overstatement corrected at line 94. Change to "attests," matching line 94.

7. **[Low] L5, small new inaccuracy — Notes line 89.** Grouping 3's summary "A for the dedication texts, C for content" does not cover **row 10**, whose Registry Confidence cell is a flat **B**. A one-clause qualification fixes it.

8. **[Low] Document Log accuracy — Notes lines 436, 440, 445, 456, 459.** "fixed at all four loci" (H1), "fixed at both loci" (M3), "fixed" (M8, H2), "no further stale instance was found" and "all eleven Medium and ten Low findings fixed" each overstate what was applied. These lines should be updated to match what a second pass actually leaves standing, so the next reviewer is not sent to a locus the log says is clean.

None of these requires rebuilding a section, revisiting the identity decision, or re-deriving any gravity, story or lexicon linkage. Items 1, 3, 4, 6, 7 and 8 are single-sentence edits in the Construction Notes. Item 2 is one clause in the prompt (plus a one-word check that it does not push a fifth sentence past 35 words). Item 5 is a re-measurement the build thread can run in a minute and record.
