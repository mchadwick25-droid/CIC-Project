# Adversarial review round 2: `CiC_System_Redesign_Pass1_Design_2026-07-26.md` — did the fix pass land?

*Opus review, dispatched 2026-07-26 — checking whether the fix pass applied after doc 20's review actually landed correctly, per the same discipline this project has used every time a fix pass follows a review: that is exactly where a corrector introduces a new error while removing an old one, and it has happened before in this same arc (`19_Opus_Adversarial_Review_Round4_of_Brief.md`, on a different document, caught two new errors introduced by the immediately-prior fix pass).*

*Process note, acted on below: doc 20 was edited in place to mark its own findings "fixed," rather than left as a verbatim, closed record with a separate append-only fix-list update — the pattern used successfully on the brief's reviews (docs 18, 19). That meant no pre-fix version of doc 20 survived to check the fix pass against. This review is saved as its own new document for exactly that reason, verbatim below, with closure notes added only to its own prioritized fix list at the end — not to the findings themselves.*

**Findings below are preserved exactly as the reviewing agent returned them.** Closure annotations, added 2026-07-26 after fixes were applied, appear only in the "Prioritized fix list" section at the end.

---

## Bottom line

**One more short round before Fable reads it — 2 P0s, 5 P1s, all localized text edits, none needing Fable or a redesign.**

Of the 15 findings from doc 20, **12 landed cleanly and verifiably, 3 landed partially, and 1 did not land at all** despite doc 20 and the Decision Log both certifying it fixed. The fix pass was genuinely careful — the two P0 corrections that mattered most (Desert's Quick Meanings exist; the leak is the chunk's own `## Key Sources`, not registry rows) are substantively correct against the actual files, the actual parser, and the actual transcript, and the twelve clean fixes are clean. But it produced exactly the failure mode this project has caught before: **a new wrong mechanism claim inside the sentence that was rewritten to fix the old wrong claim.**

I re-derived every fix against the same primary sources doc 20 used — ran the indexer's split logic over all 104 chunk files, read `retriever.py`/`indexer.py`/`nodes.py`/`modern_term_bridge.py`, parsed the real two-world session's citation payloads, extracted FG V3.6 and RCF V3.2 from the .docx files, and re-read doc 14, doc 15, and the brief's §8 objective 1.

---

## P0 — real errors, fix before Fable reads this

**1. The Desert correction gets the *mechanism* backwards, in the paragraph that exists to fix a mechanism error.** (§0 item 1, line 15; repeated in Appendix A, line 588)

The substantive correction is right and I confirmed it directly: 104 chunk files total (45/9/15/12/13/10), all 104 carry authored Quick Meaning content, Desert's 9 use `**Quick Meaning:**` bold inline labels with real content, and the 80/24 drop split is exact (three files matched "quick meaning" only as a back-reference — "See Quick Meaning above" — so 24 is correct, not 27).

But the text says Desert's 9 survive *because of* the bold inline label "rather than the `## Quick Meaning` heading the other worlds use." That is false. `indexer.py:117` computes `main_content = content.split("---", 2)[2]`. Desert files open with `---`-delimited front matter, so `parts[2]` begins immediately after it and carries the whole body. **Desert survives for the identical reason Hieronymian does — `---`-delimited front matter — and Hieronymian uses the `## Quick Meaning` heading in all 15 files.** The label style has zero causal role in the parser drop; it is why the *original audit's search* missed Desert, which is a different fact.

Why this matters for Pass 2: the sentence as written invites a build step like "normalize Quick Meaning labels to Desert's format," which would not fix the drop. The real fix is the front-matter delimiter/parser.

**Status: fixed 2026-07-26.** §0 item 1 and Appendix A both rewritten to state the correct mechanism (both survive because their front matter is `---`-delimited; label format only explains why the original audit's search missed Desert).

**2. P1 #1 (the fabricated FG rule number) was not applied — and §0 now asserts it was.**

Doc 20: *"'Facilitator Governance §8 Rule 1' is a citation label that doesn't exist… Fixed to cite the actual sentence, not an invented rule number."* It wasn't. I extracted `L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx`: §8 "Turn Management" is four unnumbered prose paragraphs. The design still carries:

- line 403 — heading: "Turn selection: enforce Rule 1 first, then judge"
- line 405 — "This enforces Facilitator Governance §8 Rule 1"
- line 406 — "which is what governance Rule 4 already describes"
- line 509 — "under the redesign it is **Rule 1a**, guaranteed" (the exact site doc 20 singled out, because "Rule 1a" in the cited literature means Sacks/Schegloff/Jefferson 1974)
- line 595 — Appendix A: "§8 Rule 1 mandates immediate direct-address routing," stated as a *verification result*

What the fix pass actually did was add §0 item 4 (line 18), which quotes the real sentence correctly — I confirmed it verbatim — and then claims: *"FG §8 is four prose paragraphs, not numbered rules — cited here and throughout by its actual text, not an invented rule number."* That claim is false in five places, so the document now contradicts itself and self-certifies the contradiction away. This is the letter-of-the-finding-not-its-point failure.

**Status: fixed 2026-07-26.** All five sites corrected — invented rule numbers removed, replaced with citations to FG §8's actual text or plain description.

---

## P1 — materially improves it

**3. `modern_term`'s new §3.11 table drops the field the whole mechanism runs on.** The real `definitions.json` carries `term_id`, `display_terms`, `modern_sense`, `period_originated`, `origin_year`, `contested_today`, `underlying_subject`. §3.11 specifies four fields: `term`, `display_phrases[]`, `distinguishing_claim` ▲, `native_subject_map` ▲. Missing are `origin_year` — which is the *only* thing that decides whether the bridge fires (`_is_anachronistic` compares it against the world's parsed end year) — plus `modern_sense` (the Facilitator's beat-2 speech) and `underlying_subject` (the term-free handback). §6.6's headline correction ("anachronism evaluated against **every seated world**") is not computable from the fields §3.11 specifies, even though §3.10 correctly supplies the world side (`time_window`). §3.1 handles this problem with an explicit *(carried forward unchanged)* row; §3.11 has none, and its `display_phrases[]` note ("Kept as today") implies the table is complete for what's kept.

**Status: fixed 2026-07-26.** `origin_year`, `modern_sense`, and `underlying_subject` added as explicit *(carried forward unchanged)* rows; `display_phrases[]` corrected to `display_terms[]` to match the real field name.

**4. The generation-context correction missed a fourth site.** §9.5 (line 518) still says Chloe's *"Justin's First Apology registry row [is] one click away **instead of inlined**."* I checked the actual session (`6bdbe5cb-…json`): the Justin registry row P06 resolves into the **citations payload only**. It was never inlined — which is precisely what P0 #2 corrected. §5.1, §8, and §9.3 are all now correct and mutually consistent (and §7's table carries no stale version), but this one clause preserves the retracted claim.

**Status: fixed 2026-07-26.**

**5. The new record types were added but never wired in.** `world_core` and `modern_term` appear nowhere in the document outside their own subsections and the §3.0 enum. Consequences: §11's world-freeze table (which §4, §5, and §10 all point at as the single reference) enumerates 11 record types and **does not require a `world_core` record at freeze** — so a world could freeze without the record §5.1's always-present assembly and §6.6's per-world anachronism check both depend on. §5.1, §6.6, and §9.4 also don't name the new sections, so nothing routes a reader to them.

**Status: fixed 2026-07-26.** `world_core` row added to §11's world-freeze table; §5.1, §6.6, and §9.4 now cross-reference §3.10/§3.11 by name.

**6. The §4.2 field-completion gate's only surviving example isn't gateable under the schema as written.** With Desert's 0/9 correctly removed, the row rests entirely on the 7%–100% Author-Gravity variance (real — Desert 22%, Hieronymian 7%, Alexandria 100%, from `03_WorldBuilds_Validation_Sweep.md`). But no record type in §3 defines an Author-Gravity field. §3.2 says Author Gravity risk notes "ride on the source link," yet §3.0 specifies `sources[]` as `{source_id, locus, licensed_for}` — no slot. §11's `term` freeze row doesn't require one either. So §4.2, §10's Organization row, and §11 all claim field completion would have caught a defect the schema gives it no field to check. (Not introduced by the fix pass, but the fix pass made it load-bearing by removing the other example.)

**Status: fixed 2026-07-26.** `sources[]` envelope extended to `{source_id, locus, licensed_for, author_gravity_note}`.

**7. Doc 20 was overwritten in place, so no as-reviewed artifact survives.** Commit `3c08f23` introduced the design document (606 lines) and doc 20 (54 lines) together, both already in post-fix form — there is no pre-fix version in git and no diff is possible. Doc 20's own P2 section points to "the Decision Log's 2026-07-26 entry" for the full list; that entry points back to "doc 20 and this entry's source material." The original 15-item prioritized fix list and the 12 P2 items exist in neither. For a design whose §4.2 requires "every round saved as an artifact; no self-certified dismissals," a review artifact rewritten to certify its own closure is the wrong shape.

**Status: addressed 2026-07-26 by this document's own existence** — saved as a new file (doc 21) rather than another in-place edit to doc 20, with findings preserved verbatim above and closure notes confined to this fix list.

---

## P2 — polish

- **§3.11's gloss-list paragraph is findable only by reading to the end of a subsection titled `modern_term`.** The specification itself is good and correctly scoped (keyed list, not a record type). But §2 job 6 and §7's table still say "record data" for a thing §3.11 explicitly says is *not* a record, and neither points at §3.11; nor does §5.6's Level 1 row. Add the cross-reference at all three rather than relying on §3.11's retro-definition. **Fixed 2026-07-26** — all three now cross-reference §3.11 directly.
- **`display_phrases[]` (§3.11) vs `display_terms` (the actual field name in `definitions.json`)** — the note says "Kept as today," so it should use today's name. **Fixed 2026-07-26** (folded into P1 #3's fix).
- **§4.3's preamble and its item 1 duplicate the same clause** two lines apart ("adopted from doc 14, as specified there… the best-worked-out piece of the corpus"), an edit artifact from the §3.12 consolidation. **Fixed 2026-07-26** — the duplicated clause removed from item 1.
- **§3.12's "(adopted from doc 14, §4.3)"** reads as doc 14's §4.3, which doesn't exist (doc 14 uses §1c/§4a–4c/Tier 1–3). Otherwise §3.12 is an accurate, complete rendering of doc 14's Tier-2 STARLITE table — all eight elements map correctly, including Limits→`languages_searched` and Approaches-as-derived-view. **Fixed 2026-07-26** — corrected to "doc 14's Tier-2 recommendations."
- **§10's objective-1 list omits §3.12**, the section that now holds the search-strategy record the objective explicitly asks for. **Fixed 2026-07-26.**
- **§11 calls the Quick Meaning defect "a rendering bug"** — it's an indexing/parse-time drop; §0 calls it a parser drop. **Fixed 2026-07-26** — unified on "parser drop."

---

## What I verified as correct

Worth stating, because it's most of what I found. **P1 #2** — RCF Part Eight has exactly eight test categories (Source-Awareness, Anachronism, Confidence-Under-Thinness, Self-Referential, Scholarly-Framework, Relational Safety, Claim-Laundering, Sustained Engagement); §5.5 now says eight and Appendix B's separate nine-vs-eight note is consistent. **#3** — `must_not_retrieve` is fully gone. **#4** — all three `Jobs (§6)` sites now read §2, and no residual §6/§2 ambiguity survives (line 44's `(§6)` correctly points at Facilitator governance). **#5** — now reads "brief §9," unambiguous. **#6** — quotes claim `text_translation` + `license`, matching §3.4's actual table. **#8** — the four-field relation taxonomy is clean: §3.0 states the envelope relationship, §4.2's reciprocity gate names all four, §11's gravity/force row correctly names its own two and defers to §4.2, and nothing implies they're unrelated. **#9** — the new objective-1 mapping genuinely covers the brief's actual "generalizing… to every document type that currently fans out" ask, which the narrower one did not. **#10** — R7 sits between R6 and R8, exactly doc 15's position, and doc 15's parroting contingency is preserved verbatim in both §5.3 item 4 and §5.4. **#11** — §7's reconciliation is accurate: a Representative does gain visibility into Facilitator crisis-intercept turns under §6.6, and §6.6/§7/§9.1 now say the same thing. **#12** — both judgment calls are in §12 (items 7, 8) and cross-referenced from §6.2 and §4.1.

**P0 #2's substance holds against code and transcript.** `resolve_references(...)` output reaches only `Citation.registry` → `citations_payload` → `message_kwargs["citations"]`; `retrieved_context` (which is `doc.page_content`, the full indexed body) is what reaches `build_representative_prompt`. In session `d1ec86a7-…`, `syrlex002_qyama.md`'s indexed body does carry its `## Key Sources` section — "rests on later hagiographic attribution," raw `(Source Registry #10, #13)` — and it went out in both of Mar Yausep's turns (messages 4 and 6), with the P → MY → P → MY order §9.3 describes. The section is 971 chars / ~140 words, so "~275 tokens" is a touch generous but within estimate tolerance. The `"confirmed directly against publisher page"` quote is now verbatim-correct against `source_registry.json` row 33.

**P0 #3's other two sections are sound.** §3.10 `world_core` matches §5.1's "world's own ground" segment field-for-field and supplies the `time_window` §6.6 needs. §3.12 is faithful to doc 14. §3.4, §3.8 tables are consistent with the §3.0 envelope and the eight jobs. The §3.0 `record_type` enum lists 13 types and all 13 now have field tables.

---

## Prioritized fix list — all items closed 2026-07-26

1. ~~§0 item 1 and Appendix A: replace the Desert survival mechanism.~~ **Closed.** Correct version now states: Desert's 9 and Hieronymian's 15 both survive because their front matter is `---`-delimited, so `split("---", 2)[2]` begins at the body; the four fenced worlds' bodies begin after the Quick Meaning section. Desert's bold inline label is why the original audit's search missed it, not why the parser keeps it.
2. ~~Lines 403, 405, 406, 509, 595: remove the invented rule numbers.~~ **Closed.** All five sites now cite FG §8's actual sentence or describe the mechanism in plain language.
3. ~~§3.11: add `origin_year`, `modern_sense`, `underlying_subject`, or an explicit *(carried forward unchanged)* row.~~ **Closed.**
4. ~~§9.5: drop "instead of inlined."~~ **Closed.**
5. ~~§11 section A: add a `world_core` row; add forward pointers from §5.1, §6.6, §9.4.~~ **Closed.**
6. ~~§3.0/§3.1 and §4.2: give Author Gravity a named field.~~ **Closed** — `sources[]` extended with `author_gravity_note`.
7. ~~Process: restore or reconstruct doc 20's original findings as a separate as-reviewed artifact.~~ **Closed** — this document.
8. ~~P2 sweep.~~ **Closed** — all six items applied.

Items 1–4 were the ones held for before Pass 2. Items 5–8 were done in the same pass since the document was already open.
