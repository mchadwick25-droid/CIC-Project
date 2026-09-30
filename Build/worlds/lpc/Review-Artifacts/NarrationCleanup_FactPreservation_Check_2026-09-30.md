Simulated review — informational only, not an Article 31 substitute.

# lpc Phase L0 item C — narration clean-up, fact-preservation check

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent verifier subagent (fresh context, no drafting involvement)
- **Drafter agent:** lpc L0-C clean-up session (commits c0b1158d9, 13b011139)
- **Round:** 1 (a fact-preservation check, not a revision round)
- **Truncation check, method 1:** line and row counts, old against new, per file (Step 0 179/179, Doc_01 206/206, Doc_02 158/158, Registry 369/369 lines and 272/272 numbered rows), plus identical heading lists
- **Truncation check, method 2:** byte-level end-of-file read of each file and of the audit file (each ends in a newline and a complete final sentence or a complete 12-pipe table row)
- **Subject:** `Step0_Movement_Scope_Confirmation.md`, `Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md`, and `Build/Ministry/Operations/Audits/lpc_Live_Surface_History_2026-09-30.md`
- **Baseline:** e9b24639d (parent of c0b1158d9), compared against HEAD 13b011139

**Verdict: not ready to call fact-neutral.** Most hunks are faithful, and the audit file holds every removed fragment verbatim. But three changes alter or drop a fact, and the earlier clean-ups' cuts remain mostly unrestored.

## Findings

**P0:** none.

**P1-1. Doc_01 line 114: the corroboration claim changed.** Old: "That is a stronger, more independently-corroborated finding than the document's earlier draft claimed for it." New: "That is a strongly, independently corroborated finding." A comparative claim became an absolute one. The basis also blurred. "Two independent adversarial review threads ... through their own separate review processes" became "Two independent lines of analysis." "The same defect this document's own review series found independently" lost the fact that a review series found it. The independence claim rested on two separate adversarial reviews, and the new text no longer says so. Fix: restore the non-comparative facts without the history. For example: "Two independent adversarial reviews, on two separate branches, reached the same reading ... That independent agreement is the evidence for this reading." Do not assert "strongly."

**P1-2. Source_Registry.md row 192, Verification Note: an evidence pointer was removed.** "has been read (`Review-Artifacts/Possidius_Full_Read_2026-09-16.md`)" became "has been read in full". The file exists. It is the record that the read-in-full claim rests on, and Doc_01 line 26, Doc_02 and `records/lpc/source/lpc.source.possidius-vita-augustini-weiskotten1919.md` all still cite it. A pointer to evidence is not narration. Restore it.

**P1-3. Earlier clean-ups (28e35b19e, 87cea0c0): binding and decision facts that are still missing.** The current pass restored only "by the project lead" on Doc_01 line 20. These are still missing, and none of them is in any Ministry audit file:
- Doc_01 line 26 (the Possidius *Vita* ch. VIII ordination sentence) lost "corrected on the project lead's ruling of 2026-09-16, `lpc_Decision_Log.md`". Now it survives only in `Review-Artifacts/Doc01_Correction_Verification_Round2_2026-09-16.md`.
- Registry row 10 lost "per Mark's 2026-08-26 split ruling" (the double placement with the Hieronymian world). Row 24 lost "(Mark's ruling)" (City of God not double-assigned). Row 204, in its Boundary Status cell, lost "Mark's own 2026-08-26 ruling, independently reconfirmed this session" and "per Mark's own prior ruling". Row 204 was later re-pointed from `tertullian-s-voice` to `latin-apologists` (75c29ccb0 / 34e2128ac). The old attribution therefore cannot simply be pasted back. See Decisions below.
- Registry front matter (87cea0c0): the original saturation basis was cut and exists now only in git history. It read: 73 works, 65 `assigned` and 8 `provisional`, at the 2026-09-02 disposition, growing to 99 (87/12) at 2026-09-08. The round-by-round recall accounting was cut and replaced by a pointer to `lpc_Decision_Log.md` and `Doc02_Round1–14_Review.md`. The 30 Doc02 round files exist. Whether the Decision Log holds every per-round instrument list and PRESS disposition was not checked here.

**P2 (wording or minor provenance; no claim changed):**
- Doc_01 line 20: the date "2026-09-16" of the confirmation was not restored. It can be recovered from the Decision Log entry title. "The freeze declaration's own Article 29 listing" became "the Article 29 listing in a freeze declaration". Pre-existing, outside this pass: the cited the V1.2 process document under Build/Ministry/Technology does not exist at that path.
- Doc_02 line 13: the census lost its date ("as of 2026-09-29", "made on 2026-09-29"). The counts were re-derived today and still hold (173 / 153 / 151). But the sentence says the census grows, so the date scopes the figure.
- Registry line 87: "Field-bibliography sweep, 2026-09-29" lost its date.
- Registry line 369: "carried forward as an open item (Doc_02 §9)" became "disclosed as a limit at Doc_02 §9". Doc_02 §9 is headed "Open items carried forward", so "carried at Doc_02 §9" is the faithful form.
- Registry rows 94 and 148, Licensed For: the wording changed ("open question ... carried unmoved" became "question ... left unanswered, unchanged"; "still-open" became "unanswered"; "open item" became "gap"). The scope is unchanged. The brief said no column changes. `records/lpc/source/*dossey*` and `*millar*` still carry the old wording, but as copied prose, not as a quotation.
- Registry Discovery cells: "direct fetch" was dropped on rows 194–212. "Field knowledge" was dropped on rows 34, 35, 41, 46 and 47. "Grep and read" was dropped on row 11. None was moved to the Verification Note. All are method detail only.
- Registry row 39: "read directly, for the base-text correction" became "read directly, supports the base-text correction", which is slightly stronger. Row 56: "Extent and rights re-verified **by WebSearch**" adds a method the old Added cell did not state. The row's own Discovery cell ("WebSearch / 2026-09-02") supports it. Row 192: "not stated when supplied" was dropped (a provenance fact).
- Doc_02 line 91: "for the first time" came out of the §5 heading. Doc_02 §9 item 9 still says "assessed for the first time at §5".
- Registry row 65: "(Doc_04 §7 Open Item 6)" became "(Doc_04 §7, item 6)". It still resolves, because Doc_04 §7 is "Open Items Carried Forward", item 6. Doc_04 itself uses "Open Item 6".
- Doc_02 line 25 still says "Doc_01's nine review rounds". 28e35b19e replaced "nine" with "history" in the Registry, so the two documents now describe the same count differently.

## What was checked

1. **Hunk by hunk, all four files.** Every changed line or cell was diffed against e9b24639d, and each removed span was searched for in the audit file. All are present verbatim (the only automated misses were punctuation at span edges, confirmed by hand). Step 0's five hunks remove or replace "open" / "not yet resolved" with no change of meaning. Doc_01 line 93 and Doc_02 lines 25, 95, 107 and 112 are faithful.
2. **Registry.** 272 rows; the same numbers in the same order (the non-sequential order is unchanged); 12 pipes on every row, old and new. Type, Confidence, Boundary Status, Exclusion Reason and Comparandum cells are byte-identical in all 272 rows. The Licensed For cells differ only in rows 94 and 148. Every shortened Discovery cell was checked, and its map path, check target and locus are in the row's Verification Note. The locus was already there for rows 11, 14, 43 and 213, and was added for the others. Rows 3, 33, 43, 44, 45, 48, 56 and 171 read faithfully. Row 3 keeps "read from Doc_01's own finding, not an independent locus check". Row 33 keeps the five-source count. Row 43 keeps its review-history locus. Row 44 keeps the Donatism Registry row 16 and Manifest G3. Row 45 keeps Doc_01 §5 plus field knowledge. Row 48 keeps the second WebSearch correcting G2's "not identified". Row 56 is as noted at P2. Row 171 turns "verified absent" plus "direct XML check" into "Verified absent from the vendored corpus by direct XML check", which is faithful.
3. **Doc_01.** Line 20 "CONFIRMED by the project lead" matches `lpc_Decision_Log.md` "2026-09-16 — Project lead's Article 29 confirmation" ("Confirmed by the project lead"). Line 114 keeps the pinned commit `9caf7bea` and branch, and the `Step0_Round2_Review.md` cite. The quotation was re-verified verbatim at `9caf7bea:World-Builds/Donatism/Review-Artifacts/Step0_Round2_Review.md`. The corroboration claim changed (P1-1).
4. **Doc_02 line 95 against Doc_01 line 35.** The quotation is now verbatim: "how deeply that substrate culture shaped ordinary congregational life specifically... is a genuine question for Doc_02's Source Asymmetry work, not resolved or assumed here." Before, it had an extra "own" and did not match.
5. **Downstream.** Searched Docs 03–09, `records/lpc`, `packages`, `canon`, the world core and the Representative files for every removed phrase. Doc_05, `lpc_World_Profile.md`, the world core and `lpc.limit.rural-punic-berber-life` carry "genuine open question", but as their own prose or as a quotation of the world core's `thin_topics`, not of Doc_01. The source records for rows 59, 94, 148 and 192 repeat old Registry wording as copied prose, not as quotations. No downstream quotation is broken.
6. **Tools.** `python tools/check_live_commentary.py --surface worlds`: no REWRITE or ROUTE lines for the four files (all PROTECTED or KEEP). `python -m engine.m10.cli citations lpc`: the same 10 pre-existing findings at HEAD and at e9b24639d (checked in a detached worktree), none new.

## Decisions for the project lead

1. Row 204's boundary attribution. Should the Registry record the ruling behind Perpetua's exclusion? The original 2026-08-26 ruling named `tertullian-s-voice`. The current `latin-apologists` assignment came from the later directed corrections (75c29ccb0). The live cell should name whichever ruling is actually in force.
2. The facts that 28e35b19e and 87cea0c0 cut without an audit file (P1-3). Restore them to the live files, or move them verbatim to the Ministry audit file? The rulings are bindings, so the recommendation is to restore them live.
