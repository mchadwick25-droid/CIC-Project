# Independent Adversarial Review, Round 2 (targeted recheck) — The Methodist Revival, Steps 0–2

**For:** the same reviewer (or an equally independent one) who ran Round 1 (`Review-Artifacts/Independent_Review_Round1.md`). Per `cic-build-cycle`'s own rule, this is a **targeted recheck of what changed against the prior findings**, not a full re-review from scratch — Round 1 already did the exhaustive first pass; this round verifies the fixes and checks for anything the fix work itself introduced.

**Standard:** same as Round 1 — `reference/method/CiC_Adversarial_Review_Standard_Practice.md`, Opus tier, source-level verification for anything load-bearing.

## What changed since Round 1 — check each against Round 1's own finding, not against this brief's own description of the fix

**Step 0** (`Step0_Movement_Scope_Confirmation.md`):
- Zinzendorf/Marienborn correction (§2 A3.2) — verify the corrected sequence (banished from Saxony 1736; met at Marienborn July 1738; Herrnhut visited August 1738) against Widely Accepted historiography directly, not just against this document's own new wording.
- Census `statusWord` now quoted as "Researched — strong candidate" (no "(Era 8 Step 0)" suffix) — re-check against the live `cic-website/data/world-census.json` file yourself.
- Sermon count corrected to sixteen, Sermon III flagged as Charles Wesley's — re-verify at least the heading line (1204) and the footnote (8298–8299) yourself, independent of this build thread's own claim.
- A new A3 item 4 added, naming VII.2/VII.6/VII.20/VIII.1/VIII.2/VIII.34 as further census neighbours — check this list is itself complete and each entry's own one-line characterization is accurate.
- The essay-length "version-discrepancy" process narration was trimmed to one paragraph pointing at `Open_Gaps_Tracking.md` — confirm no equivalent process narration remains elsewhere in the document (Round 1 also flagged a "B1 correction narrative" — check whether that specific instance still exists or was addressed differently).
- `Open_Gaps_Tracking.md` cross-references corrected (Article 20 voices → item 7; review-independence → item 3) — re-verify these actually match the live file's own current numbering, not the numbering at the time Round 1 wrote its finding.

**Doc_01** (`Doc_01_World_Identification_Boundaries_Orientation.md`) — the section that matters most:
- **§4 (Whitefield) is substantially rewritten.** This is the one place Round 1's own verdict said the conclusion "partly survives but the argument does not... reached to get a clean answer." Read the new §4 fresh, as if for the first time, and answer honestly: does the corrected six-question argument (gravity yes/authority yes/interpretation arguably yes/formation partial/worship no) actually hold up, or does the rewrite just launder Round 1's own preferred tally into the document without independently re-testing it? This is the single question this recheck most needs to answer honestly, not rubber-stamp.
- **§9's escalation framing** — check the three named options (A: remove entirely; B: split by date, Whitefield's person stays, his post-1741 legacy allocated elsewhere; C: non-exclusive shared assignment) are actually distinct, actually have real stated trade-offs, and that this document does NOT quietly pick one under the guise of "recommending" B while still calling the question open. If the "recommendation" language reads as a soft decision rather than a genuine option among three, say so.
- **§5 (Strand Determination)** — the 1787 Whatcoat correction and the "shared mechanisms, different ecological pressure" formation-emphasis fix. Verify the Whatcoat episode independently if you can (Widely Accepted, not vendor-verified by this build thread either — note if you can do better).
- **§7 (Moravian account)** — now states four points of contact instead of three, adds Böhler and the Fetter Lane founding date, and states plainly that Vol. I does NOT reach the Herrnhut visit. Re-verify the "ends 8 June 1738" claim and the Böhler/Fetter-Lane citations directly against the vendored file.
- **The disposition itself:** confirm the header status line, §9, and the closing paragraph all say the same thing (cleared pending Mark's ruling on Whitefield allocation, not "Approved to proceed" outright) — check for any place that might still imply full self-disposition.

**Doc_02 / Source_Registry / Source_Acquisition_Manifest:**
- Voice/author corrections: Sermon III → Charles Wesley; the Large Minutes → institutional Conference voice, not Wesley's own; Curnock's editorial introduction → its own `curnock-nehemiah` slug. Cross-check these against the regenerated `cic/corpus-map/the-methodist-revival.yaml` (now 12 rows) directly, not only against this document's own prose.
- Author Gravity's own word-count correction (Asbury 569,170/56.6%, Wesley's own material ~299,000) — recount at least one file's own word count yourself (`wc -w`) to confirm this build thread didn't make a new counting error while fixing the old one.
- The `PAIRS.yaml` entry (`the-methodist-revival` / `the-moravian-church-at-herrnhut`, one-way) and the expanded cross-world-overlaps list in Doc_02 §7 — check these are accurate and that "one-way" is the right relation given what's actually vendored.
- The corrected Source Registry (now 24 rows) and Manifest (the withdrawn false queue-seeding claim for G2/G3/G5) — spot-check a few row locators directly (row 3's new end-line 386; row 4's new end-line 258).

## What this recheck should NOT do

Re-litigate anything Round 1 already found correct (the vendored-file existence, the rights basis, the `meth` registry code, the dates already confirmed clean in Round 1's own "What I checked and found correct" section) — recheck only what changed, plus a light independent spot-check of the highest-stakes claim (§4's own re-argued case), per the standard practice's own "read what the last review found before hunting for new problems" rule.

## What "done" looks like

A verdict per document (cleared / still substantial / now a new, different finding), and, separately, a direct answer to: **is Doc_01 §9's escalation to the project lead now genuinely well-formed** (three real options, honest trade-offs, no quiet pre-decision), such that the project lead can rule on it as presented? Save as `worlds/meth/Review-Artifacts/Independent_Review_Round2.md`.
