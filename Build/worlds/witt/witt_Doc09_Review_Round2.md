# Independent Adversarial Review — Round 2 (Targeted Recheck)
## witt_Doc_09_Story_Inventory.md (Lutheran Wittenberg & Its Congregations)

**Scope of this round, per this build's calibration:** not a full re-review. Round 1
(`witt_Doc09_Review_Round1.md`) found 4 substantial findings; this round verifies each fix
directly against primary sources or the cited template file, and scans only the edited
regions plus their cross-references for new errors. Round 1's cleared areas (witt-S02,
S04–S12, No-Tier-5 discipline, Absent Stories, Story Index arithmetic) were not re-derived
from scratch, per instruction.

---

## Overall Verdict: **CLEARED REVIEW**, with one minor residual inconsistency flagged for a one-line fix (not a fifth substantial finding)

All four Round 1 substantial findings are genuinely, accurately fixed, and two of them
(witt-S03's quotation, and the Discipline 1 sequencing claim) were independently
re-verified against the actual source files and the actual template file — not accepted on
the document's own say-so. The OG tracker renumbering (OG-13 → OG-14) is applied
consistently and does not collide with the tracker's real OG-13 (World Profile), which is a
different item. One small drafting residue survived the edit: §6's completion checklist
(line 326) still uses the pre-fix "drafted alongside this document as a structural
prerequisite" framing for the World Profile, which contradicts the corrected Discipline 1
language two sections earlier ("a disclosed sequencing deviation... not a claim that the
two documents are structural peers"). This is a one-line fix, does not touch any story
entry, tier, or source citation, and does not warrant another full round.

---

## Finding 1 — witt-S03 (Worms quotation): RESOLVED, independently re-verified against source

**What I checked:** read `luther_table-talk_bell1886.txt` directly at TT 3495–3515, and
`luther_hymns_bacon-allen.txt` at Hy 635–655, rather than trusting the document's own
quotation.

**What I found:** the vendored Table Talk text at TT 3507–3509 reads exactly: *"Although I
was somewhat astonished at the news, yet I answered the herald, and said, although in Worms
there were as many devils as there are tiles on the houses, yet, God willing, I will go
thither."* This is precisely the sentence witt-S03 (current document, lines 89–93) now
quotes and attributes to "this library's own Table Talk text," with the correct line range
(TT 3507–3509).

The document also now correctly identifies the Carlyle rendering it previously
misattributed: Hy 644 gives *"Were there as many devils in Worms as these tile roofs, I
would on"* and Hy 651 gives *"Here I stand — I cannot do otherwise"* — both inside the same
Bacon-quoted Carlyle passage (Hy 644–652), exactly as the document's usage guidance and its
new "Correction note" (lines 95) describe. The entry now explicitly discloses that its own
prior draft misquoted Carlyle's rendering as "this library's own text," names this as the
project's recurring quote-fidelity failure mode, and states the fix was caught at Round 1
review, not self-discovered.

The Registry cross-reference at the end of the entry (R31 Primary; R69 Secondary, embedded
quotation only) is accurate and consistent with the corrected usage guidance, which now
requires Bacon/Carlyle provenance disclosure for *either* Carlyle-transmitted phrase ("Here
I stand" or "these tile roofs"), not just "Here I stand" as before.

**Verdict: fix is accurate, complete, and correctly sourced. No further action needed.**

---

## Finding 2 — Discipline 2 (hymn-reading-pass completeness claim): RESOLVED

**What I checked:** the current §0 Discipline 2 text against the Round 1 finding, and cross-
checked the two disclosed footnote quotations against the vendored hymns file directly
(Hy 856–870), and their "already read" claim against the Source Registry's R66 row.

**What I found:** the document now explicitly discloses both items Round 1 named:

- The "Ein' feste Burg" composition-legend footnote. The document's quotation ("The time of
  its composition was in the year 1529, just before the Diet of Augsburg... 'Burg' or
  'Festung' of Coburg... 'during the Diet, not only at Augsburg, but in all the churches of
  Saxony'") matches the vendored footnote at Hy 856–866 verbatim (I re-read the footnote
  directly; the quoted fragments and the elision are faithful to the source).
- The Melanchthon "thunderbolt" anecdote (Hy 868–870, "reported as an expression of
  Melanchthon... from Richter") — also verified verbatim against the source.

Both are disposed of with reasoning that matches Round 1's own assessment: the composition
footnote is "the editor's own hedged 'popular impression... doubtless,' not an attested
event," and the Melanchthon anecdote is "unsourced beyond a bare surname and undated,
supports no tellable claim at any tier." Neither is entered as a 13th story; the document
states plainly that neither changes the twelve-story count. This resolution path is
Round 1's option (b) — a disclosure paragraph inside Discipline 2 rather than a formal entry
at §5 — which Round 1 explicitly said was an acceptable alternative fix.

I confirmed against `witt_Source_Registry.md` row R66 (line 82) that "the Ein feste Burg
footnote (856–866) verified" is indeed already on record there, matching the document's own
claim that this material was already Registry-read before this pass.

The document's completeness language is also now appropriately qualified: it states the
pass "has now been read in full, including the two items just disposed of, rather than the
file's length alone standing in for a completeness claim" — this is a more accurate and
defensible claim than Round 1's target sentence ("nothing beyond what was already carried").

**Verdict: fix is accurate and complete. No further action needed.**

---

## Finding 3 — Discipline 1 (World Profile scope/sequencing argument): RESOLVED, independently re-verified against the template

**What I checked:** read `World_Profile_Template.md` lines 1–15 directly, independent of
the document's own quotation of it.

**What I found:** the template's header (lines 6–9) reads exactly:

> **Produced at:** Construction Step 8
> **Required inputs:** Doc_01 through Doc_08 all complete
> **Feeds:** World Capsule Core (inhabited voice rendering), Representative emergence
> (RCF v2.0 Phase One), Doc_09 Story Inventory (ecological context)

This confirms Round 1's characterization exactly: a stated sequential dependency (World
Profile produced at Step 8, feeding Doc_09), not a parallel one.

The current document's Discipline 1 (§0, lines 19) now states this accurately: it quotes the
same three header lines, states plainly that the document's first draft overstated the
relationship as "alongside... under the same build thread" as a "structural peer," names
that as the review's correct catch, and then gives the corrected reading: "a disclosed
sequencing deviation from the template's stated dependency direction, not a claim that the
two documents are structural peers." It also states, specifically and checkably, what
actually happened (World Profile drafted concurrently by a separate agent) and confirms
Doc_09's own "Built from" list does not include the World Profile among its inputs — which
I can confirm against §0's actual "Built from" paragraph (line 9), which indeed omits the
World Profile.

This does not overclaim in the other direction either: it does not now claim the World
Profile was genuinely a prerequisite that Doc_09 waited on (which would be false), and it
does not claim the deviation is harmless in general — it states the narrow, correct
consequence (no story entry rests on unverified World Profile material) and flags the
broader question (should future worlds' Doc_09s actually wait on the World Profile per the
template's stated order) as an open item at §7 item 3, appropriately deferred rather than
resolved unilaterally.

**Verdict: fix is accurate, textually supported, and appropriately calibrated. No further
action needed on Discipline 1 itself** — but see the residual inconsistency at §6, below.

---

## Finding 4 — witt-S01 (letter to Albrecht / posting-detail evidentiary basis): RESOLVED

**What I checked:** the current witt-S01 entry against the Source Registry's actual R2 and
R76 rows.

**What I found:** `witt_Source_Registry.md` row R2 (line 18) states: *"the posting narrative
('It was not night, but mid-day,' 473–474) is the editor's, 1915, and predates Iserloh
[R76]."* Row R76 (line 92) states: type S, confidence **B**, "Existence and dates verified
by search... not read."

The current witt-S01 entry (lines 55) now states this directly: *"this library's own
vendored text for the posting narrative is not a period document at all — the Registry's own
R2 entry records it as 'the editor's, 1915' ('It was not night, but mid-day,' v1 473–474)...
The Iserloh reference this document's 'Contested' tag ultimately rests on (R76) is itself
unread by this build, verified only as existing by a web search of its title (Registry line
92, confidence B)."* This matches the Registry rows verbatim in substance, correctly sourced
to the Registry by row number, and states plainly (as Round 1 asked) that "Contested" here
means an unread secondary source disputing a modern editor's own unsourced narrative claim —
not two primary accounts in tension.

**Verdict: fix is accurate, complete, and correctly sourced to the Registry. No further
action needed.**

---

## New-error scan

- **OG tracker renumbering (OG-13 → OG-14).** The document's §7 now says "To be logged as
  OG-14 at this document's disposition" (line 335), and this is the only OG-13/OG-14
  reference in the document — no leftover "OG-13" self-reference remains. I checked
  `Open_Gaps_Tracking.md` directly: OG-13 there is already a different, existing entry
  ("World Profile: one review round, two flagged items fixed directly..."), and OG-14 is
  not yet used. The renumbering is correct and does not collide with the tracker.
- **§3 Story Index, §3D Registry cross-reference, §4 summary:** spot-checked against the
  corrected witt-S01 and witt-S03 entries; both remain consistent (the Story Index rows for
  S01 and S03 are summary-level and don't restate the fixed prose, so no drift was
  introduced there).
- **§6 Completion Status checklist (line 326) — residual inconsistency, not previously
  flagged.** This line still reads: *"World Profile — drafted alongside this document as a
  structural prerequisite (§0 Discipline 1), under independent review separately."* This is
  the pre-fix framing Round 1 objected to (the "alongside... as a [peer-like]" language),
  left unedited when Discipline 1 itself was corrected two sections earlier. It also
  internally mixes two incompatible ideas in one phrase — "alongside" (concurrent) and
  "prerequisite" (before) — where Discipline 1 now correctly says "concurrently... a
  disclosed sequencing deviation from the template's stated dependency direction, not a
  claim that the two documents are structural peers." Recommended fix (one line): replace
  "drafted alongside this document as a structural prerequisite" with wording that matches
  Discipline 1's corrected language, e.g. "drafted concurrently by a separate build thread,
  per the disclosed sequencing deviation from the template's stated dependency order (§0
  Discipline 1)." This does not affect any story entry, tier, or source citation, and does
  not rise to a substantial finding on its own — it is a checklist bullet, not part of the
  document's evidentiary argument — but it should be swept in the next small edit rather
  than left standing next to a paragraph that now says the opposite.

No other new errors were found in the edited regions or their direct cross-references.

---

## Summary

| # | Round 1 Finding | Round 2 Status |
|---|---|---|
| 1 | witt-S03 "tiles" quote misattributed to Table Talk | **RESOLVED** — re-verified verbatim against TT 3507–3509 and Hy 644–652 |
| 2 | Discipline 2 overclaimed hymn-pass completeness, missed two in-scope Registry-read items | **RESOLVED** — both items now disclosed and disposed of, verified against Hy 856–870 and Registry R66 |
| 3 | Discipline 1 omitted the World Profile Template's stated sequential dependency | **RESOLVED** — re-verified verbatim against `World_Profile_Template.md` lines 6–9; corrected to "disclosed sequencing deviation," not overclaimed either direction |
| 4 | witt-S01 under-disclosed the posting detail's 1915-editorial/unread-R76 evidentiary basis | **RESOLVED** — verified against Registry rows R2 and R76 verbatim |
| — | New: §6 checklist line 326 retains pre-fix "alongside... structural prerequisite" language, contradicting the corrected Discipline 1 | **Minor, one-line fix recommended; not a substantial finding** |
