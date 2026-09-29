# Proposal: `canon_cells` for Alexandria's gravity / force / contested_claim records

**Status: PROPOSAL, not applied.** Nothing in `records/alx/{gravity,force,contested_claim}/`
has been edited. This is a first pass for Doc_04-reviewer sign-off before
any record is touched, per `cic-build-cycle`'s review-gated discipline.

**Revision note (same day):** the first pass under-weighted several real
relations-graph anchors by only checking the one relation that first came
to mind per record instead of every relation. Caught on `platonic-environment`
during spot-check, then fixed properly: pulled every one of the 32 records'
*complete* `relations` list and cross-referenced every target against the
real compiled `coverage.json`, not just the target I'd already picked. That
full dump changed six rows beyond the one Mark caught (`speculative-doctrinal-tension`,
`scripture-formative`, `soul-transformation`, `logos-unity`,
`neoplatonic-challenge`, `post-nicene-authority-shift`, `didaskaleion-institution`,
`transmission-ongoing`) and strengthened the rationale on several more that
didn't change. Every row below now says plainly which signal it actually
rests on.

**Why this exists.** The M2 compiler now reads `canon_cells` on these
three record types (`build/phase-1` commit `ac07562`) so they can be
retrieved for evidence assembly (`engine/m4/LIVE-GENERATION-DESIGN.md`
§3.2 Stage B/C) — but none of alx's 32 records of these types carry the
field yet, so the new compiler code has nothing to surface. Populating it
is a records-content decision (which cell does each analytical record
actually ground?), not a mechanical one, so it goes through review here
rather than being written directly.

**Method.** Three signal sources, in order of trust — every row names
which one(s) it's actually using, not just its conclusion:

1. **Confirmed real usage** — a demonstration record already cites this
   analytical record in its `sources` field, and demonstrations already
   carry `canon_cells`. Only one record has this: `learning-community-tension`
   → `F6-P`, via `alx.demo.f6-p-someone-like-me`. Treated as settled, not
   proposed.
2. **Relations-graph anchor** — the record's own declared `relations`
   connect it *directly* to a `term`/`story`/`quote`/`doctrinal_witness`
   that already carries `canon_cells` in the compiled package. This is
   verifiable against `coverage.json` right now, independent of my
   reading of the prose.
3. **Topical match** — the record's `name`/`description`/`claim` read
   directly against the fleet's actual canon-question text for a cell,
   with no declared relation backing it. Sometimes this is a near-verbatim
   wording match (marked "topical, strong" below) and sometimes a looser
   thematic fit (marked "topical, judgment call") — those are treated
   differently even at the same confidence tier, because a reviewer
   checking a strong-topical row is confirming close paraphrase, while a
   judgment-call row is making a real decision.

Confidence: **HIGH** (a real anchor confirms the proposal, or the topical
match is close enough to be near-paraphrase), **MEDIUM** (one clear signal
but genuine judgment involved, or a real anchor stretched further than its
own direct content), or **flagged, no cell** (four records where forcing a
cell would misrepresent what the record actually is). Nothing is left at
LOW-with-a-guess this pass — the full relations check gave every proposed
row at least one real signal to stand on; where it didn't, the row is
flagged instead of guessed. Cells are not exclusive; a record can carry
more than one where the content genuinely serves more than one question.

---

## Gravity (9)

| record | proposed cell(s) | confidence | rationale |
|---|---|---|---|
| `learning-community-tension` | **F6-P** | HIGH (confirmed) | Already cited by `alx.demo.f6-p-someone-like-me` (`F6-P`) — the door-line exemplar turn itself. Signal 1. |
| `teacher-bishop-tension` | F3-I; secondary F6-I | HIGH | Signal 2: `illustrated-by → alx.story.origen-demetrius`, tagged `['F3-I', 'F6-I']` in the compiled package. F3-I's own question ("Who held authority among you, and how did anyone come to have it?") is the gravity's exact subject. |
| `martyrdom-contemplative-tension` | F6-E; secondary F3-I; minor tertiary F5-P | HIGH | Signal 2, and unusually well-anchored: `term.martys` (F3-I, F6-E), `illustrated-by story.leonides-martyrdom` (F3-I, F5-P), `illustrated-by story.potamiaena` (F3-I, F6-E) — three separate relations, all converging on F3-I, two on F6-E. F6-E kept as primary because its actual question ("wanting to die as a martyr and calling it faithfulness — isn't that a death wish?") is the *tension itself* (martyrdom vs. contemplative ascent as competing formation-pictures), where F3-I is more the general historical fact of danger. F5-P noted as a minor real anchor via leonides only, not pushed as a primary. |
| `speculative-doctrinal-tension` | **F1-E** (revised primary); secondary F2-T; tertiary F1-P (topical only) | MEDIUM (revised) | **Correction from first pass**, which proposed F1-P as primary on topical grounds alone. The record's actual relation is `associated-with → alx.term.kanon-pisteos` (Rule of Faith), compiled and tagged `['F1-E', 'F2-T']` — neither of which is F1-P. F1-E's own question ("When belief was disputed, who had the right to decide, and how do we know how that person decided?") matches the doctrinal-boundary pole directly. F1-P (the speculative-freedom pole, "was there room for doubt") stays as a tertiary — it's a fair reading of the tension's *other* pole, but it has no relations-graph support, so it shouldn't have outranked the anchored cells the way the first pass had it. |
| `scripture-formative` [PRIMARY] | F2-I (primary); secondary F2-T; tertiary F2-P | HIGH (expanded) | Signal 2: `associated-with → alx.term.allegoria`, tagged `['F2-I', 'F2-P', 'F2-T']` — all three, not just the two the first pass used. F2-I kept primary as the cluster's general "how did you read scripture" question; F2-P's confusion/difficulty framing is a real fit too (this gravity's sibling `divine-pedagogy` independently proposes F2-P for the same reason — scriptural difficulty read as intentional formation). |
| `soul-transformation` [PRIMARY] | F4-I (primary); secondary F1-T | HIGH (upgraded from MEDIUM) | Signal 2, confirmed on both cells: `term.katechesis` → `['F4-I']` exactly; `term.theosis` → `['C-T', 'F1-T']`. Considered and rejected C-T as a third cell: the gravity's own content (catechesis, purification, illumination, prayer/fasting as formation *process*) is a weak match for C-T's Christological-doctrine question set, even though `theosis` technically touches there — noting the rejection rather than silently dropping it. |
| `logos-unity` [SUPPORTING] | C-T (primary); secondary F1-I | HIGH (upgraded from MEDIUM) | Signal 2, both cells confirmed at once: `associated-with → alx.term.homoousios`, tagged `['C-T', 'F1-I']` exactly. Not a primary-plus-topical-fallback the way the first pass framed it — the anchor supports both directly. |
| `divine-pedagogy` [SUPPORTING] | F6-P (primary); secondary F2-P; weak tertiary F6-E | MEDIUM (rationale corrected, confidence unchanged) | **Signal 3 only — no relations-graph anchor at all.** The first pass implied `alx.dw.f6-p-suffering` as support, but there's no declared relation to it; that was inferred shared subject matter, not a structural link. Kept F6-P because the gravity's own third manifestation ("persecution understood as God teaching through suffering") is close paraphrase of that record's actual content even without a formal tie. F2-P (scriptural difficulty as teaching) is the same shape — topical, strong wording, no anchor. F6-E noted as a *transitive* possibility only, via the `associated-with → alx.force.persecution` relation, once `persecution`'s own F6-E secondary (below) is accepted — flagged as inherited, not independently supported. |
| `learning-formation` [SUPPORTING] | F4-I (primary); secondary F3-I | HIGH | Signal 2: `illustrated-by → alx.story.gregory-formation`, tagged `['F3-I', 'F4-I']` exactly — both cells confirmed. |

## Force (18)

| record | proposed cell(s) | confidence | rationale |
|---|---|---|---|
| `apostolic-tradition` [1B init/internal] | F4-E | HIGH | **Signal 3, strong** — no declared relation to any cell-tagged record (its relations are both `precondition-for` other ungrounded gravities). Kept HIGH anyway because the wording match is near-verbatim: the force's own description ("received as the deposit, not invented in Alexandria") and F4-E's actual question ("How do you know your practices went back to the apostles and weren't later invented?") share the specific word "invented," not just the general theme. |
| `johannine-logos` [1B init/internal] | C-T; secondary F1-I | MEDIUM | Signal 3 only — both its relations (`precondition-for scripture-formative`, `logos-unity`) point to gravities with no direct cell anchor of their own on this axis. Kept as the same subject as `logos-unity`'s C-T, on content grounds, not a confirmed chain. |
| `knowing-impulse` [1B init/internal] | F1-I (primary); secondary F1-P; tertiary F4-I | MEDIUM | Signal 3 only. Broadly connected (`precondition-for` soul-transformation, learning-formation, divine-pedagogy; `associated-with` speculative-doctrinal-tension) but none of those targets carry a direct cell tag themselves, so none of this is a real anchor — it's a diffuse foundational force touching many cells transitively. F4-I added as a tertiary given how many formation-cells it feeds into. |
| `philonic-inheritance` [1A init/external] | F2-I | HIGH | **Signal 3, strong** — no anchor (`precondition-for logos-unity` only), but F2-I's "how did you read your scriptures, what did you look for in them" is near-exact for "the allegorical habit as received practice." |
| `platonic-environment` [1A init/external] | F1-I | MEDIUM | Signal 2: `illustrated-by → alx.quote.clement-schoolmaster`, tagged `['F1-I', 'F6-T']`, carrying this force's own manifestation almost verbatim. Not HIGH because F1-I's actual questions are God-belief content, not "surrounding philosophical culture" — a real anchor, imperfectly matched cell. (Caught and corrected mid-review — see revision note above.) |
| `septuagint-inheritance` [1A init/external] | F2-I | HIGH | **Signal 3, strong** — no anchor (`precondition-for scripture-formative` only), but F2-I's "was your Bible the same as ours" is near-exact for the LXX-vs-Hebrew-canon subject this force names. |
| `gnostic-challenge` [2A ongoing/external] | F2-E (primary); secondary F1-I | HIGH | F2-E: signal 3, strong ("What about the gospels that didn't make it in — were they suppressed?" is close paraphrase of the Gnostic-rival-text subject). F1-I: signal 3 only, via `term.gnosis`'s own topic overlap — not this record's own declared relation (its only relation is `associated-with learning-community-tension`, itself F6-P, which is a different enough subject — pastoral inclusion, not doctrinal rivalry — that I did *not* propose F6-P here despite the direct link, and want that specific non-inheritance flagged for a reviewer to confirm). |
| `neoplatonic-challenge` [2A ongoing/external] | **F2-P** (revised primary); secondary F1-I | MEDIUM (revised from LOW) | **Correction from first pass**, which proposed F1-I alone at LOW. Its own manifestation text is specific and I'd under-read it: "Porphyry's attack on Christian allegory, naming Origen" — allegory is `term.allegoria`'s own territory (F2-I/F2-P/F2-T), so the *method-critique* angle is a real, specific match, not a generic rival-philosophy guess. F1-I kept as secondary via the family relation to `platonic-environment` (`enabled-by`), whose own F1-I is now signal-2-anchored. Still MEDIUM, not HIGH: neither cell comes from this record's own direct relation to a cell-tagged item. |
| `arian-controversy` [2A ongoing/external] | F1-E; secondary C-T | HIGH | **Signal 3, strong** — no anchor (its three relations are all to ungrounded gravities), but F1-E's "I've heard a council basically voted Jesus into being God — is that what happened?" is close paraphrase of this exact controversy. |
| `persecution` [2A ongoing/external] | F3-I; secondary F6-E | HIGH | **Signal 3, strong**, reinforced transitively: no direct anchor (`associated-with martyrdom-contemplative-tension`, `divine-pedagogy`, neither grounded independently), but F3-I's "was it actually dangerous to be a Christian, day to day" is near-exact for "Episodic Persecution," and F6-E is now well-supported by `martyrdom-contemplative-tension`'s own real anchors (above). |
| `scripture-ongoing` [2B ongoing/internal] | F2-I; secondary F2-T | HIGH | The ongoing-force reading of `scripture-formative` — same cells, now that `scripture-formative` itself carries both (see above). |
| `teacher-bishop-ongoing` [2B ongoing/internal] | F3-I (primary); secondary F6-P; tertiary F6-I | HIGH | Signal 2, both parent tensions confirmed: `associated-with teacher-bishop-tension` (F3-I/F6-I) and `associated-with learning-community-tension` (F6-P, confirmed real usage). This force is explicitly "both tensions... as an ongoing force," so it's proposed to carry all three the parents carry between them, not just two. |
| `transmission-ongoing` [2B ongoing/internal] | F4-E (primary); secondary F4-I | HIGH (upgraded from MEDIUM) | F4-E: signal 3, strong (same "did it stay faithful" framing as `apostolic-tradition`). F4-I: **was topical-only on the first pass, now signal-2-supported** — `associated-with → learning-formation`, itself anchored `['F3-I', 'F4-I']` via its own illustrated-by story, and this force's own description (catechumenate as one of its three transmission mechanisms) is literally learning-formation's own subject matter. |
| `origen-demetrius-conflict` [3B ending/internal] | F3-I; secondary F6-I | HIGH | Signal 2: `associated-with → alx.story.origen-demetrius`, tagged `['F3-I', 'F6-I']` directly — the only force in this set whose own relation (not a related gravity's relation) is the anchor. |
| `post-nicene-authority-shift` [3B ending/internal] | F3-I (primary); secondary F6-P; weak tertiary F6-I, F4-I | HIGH (expanded from F3-I-only) | Signal 2, broader than the first pass captured: `associated-with` **four** gravities — `teacher-bishop-tension` (F3-I/F6-I), `learning-community-tension` (F6-P, confirmed), `learning-formation` (F3-I/F4-I), `speculative-doctrinal-tension` (now F1-E/F2-T, below the addition threshold here). The force's own description explicitly says it "completes the teacher-bishop and learning-community asymmetries" — i.e. it names its relationship to *both* F3-I's and F6-P's territory directly, not just one. |
| `transmission-ending` [3B ending/internal] | *(none proposed)* | flagged, no cell | Its relations now show real connections — `associated-with scripture-formative` (F2-I family) and `speculative-doctrinal-tension` (F1-E family) — but the force's own subject (what passed *beyond* this world's horizon to later tradition) is a different temporal register than what those gravities' own cells are about *within* the horizon. Kept unproposed rather than borrowing a connected record's cell for content the record itself doesn't share. Same underlying question as the other two ending-forces below: should this class of force be cell-eligible at all? |
| `arab-conquest` [3A ending/external, distal terminal] | *(none proposed)* | flagged, no cell | Only relation is `associated-with transmission-ending`, itself unproposed for the same reason. Describes the aftermath beyond the lived horizon; no natural participant question in the current 86. |
| `chalcedonian-fracture` [3A ending/external, distal] | *(none proposed)* | flagged, no cell | No relations at all. Postdates the world's own close. F3-T ("did you have denominations") remains a weak stretch, not a real match. |

## Contested claim (5)

| record | proposed cell(s) | confidence | rationale |
|---|---|---|---|
| `allegory-from-within` | F6-I (primary); secondary F2-I | HIGH | Signal 2: `associated-with → alx.story.arsinoite-conference`, tagged `['F1-E', 'F4-T', 'F6-I']`, and `associated-with → alx.term.allegoria` (F2-I/F2-P/F2-T). F6-I kept primary — "what did your people never settle" is exactly what a *contested* claim record exists to answer, closer to this record's own nature than the story's other two tags (F1-E, F4-T), which cover different episode facets, not the dispute itself. |
| `origen-positions` | F6-T | HIGH | Signal 2: `associated-with → alx.term.apokatastasis`, tagged `['F6-T']` exactly, whose own cell question ("do you believe people like me are going to hell?") is directly the doctrine this claim contests. |
| `ecology-wide-primacy` | F5-I | MEDIUM | Signal 3 only — no `relations` field at all on this record. Kept because the claim's own shape (whose formation is and isn't attested — literate ecology vs. the whole) is structurally identical to `alx.limit.f5-women-own-words`'s already-real F5-I tag (the same stratum-bias question, applied to gender there and to class/literacy here), but that's a content parallel I'm drawing, not a declared link between the two records. |
| `didaskaleion-institution` | **F2-E** (revised primary); secondary F3-I | MEDIUM (revised) | **Correction from first pass**, which had F3-I as primary. Re-reading the claim's own `held_against` reasons: both are about *evidence quality* (Eusebius's Constantinian-apologetic bias toward tidy successions; Clement's own writings never describing a formal school he headed) — that's F2-E's territory ("isn't most of what's said about you legend, collected centuries later?"), not primarily an authority-structure question. F3-I kept as a real secondary since institutional continuity does bear on how authority passed, just not as the claim's own center of gravity. No `relations` field on this record — signal 3 throughout. |
| `desert-attribution` | *(none proposed)* | flagged, no cell | No relations. A cross-build scoping question (does desert monasticism belong to Alexandria's own ecology), not phrased as a participant's question anywhere in the 86 — build-methodology content. |

---

## Summary for the reviewer

- **28 of 32** get a proposed primary cell, all now at MEDIUM or HIGH —
  the full relations check removed every LOW-with-a-guess row: either a
  real anchor was found (`neoplatonic-challenge`, upgraded to MEDIUM) or
  the existing topical case held up on its own (nothing dropped to
  flagged).
- **8 rows changed from the first pass** on the full relations recheck,
  not just the one Mark caught: `speculative-doctrinal-tension` and
  `didaskaleion-institution` had their primary/secondary swapped when the
  actual anchor pointed elsewhere than my first guess; `scripture-formative`,
  `soul-transformation`, `logos-unity`, `teacher-bishop-ongoing`,
  `post-nicene-authority-shift`, and `transmission-ongoing` gained cells
  or moved up in confidence once every one of their relations (not just
  the first one checked) was cross-referenced against the real compiled
  package.
- **4 flagged for "possibly no cell at all"**, unchanged from the first
  pass but with fuller reasoning now: `transmission-ending`, `arab-conquest`,
  `chalcedonian-fracture` (distal/epilogue forces describing what happens
  *after* the world's own horizon — even where they now show real
  connections to anchored gravities, those gravities' cells are about
  in-horizon content the ending-force itself doesn't share), and
  `desert-attribution` (a build-scope question, not lived content).
- Every row now names its actual signal — real anchor vs. strong-wording
  topical match vs. genuine judgment call — rather than presenting a
  conclusion without showing which kind of evidence it rests on.
- The single confirmed real-usage anchor (`learning-community-tension` →
  `F6-P`) remains the only one of the 32 not actually a proposal.

Once this is dispositioned, applying it is mechanical: add the agreed
`canon_cells` values to each record, gated normally (schema validation +
`gate_reciprocity` etc. already cover the rest).
