# Proposal: `canon_cells` for Alexandria's gravity / force / contested_claim records

**Status: PROPOSAL, not applied.** Nothing in `records/alx/{gravity,force,contested_claim}/`
has been edited. This is a first pass for Doc_04-reviewer sign-off before
any record is touched, per `cic-build-cycle`'s review-gated discipline.

**Why this exists.** The M2 compiler now reads `canon_cells` on these
three record types (`build/phase-1` commit `ac07562`) so they can be
retrieved for evidence assembly (`engine/m4/LIVE-GENERATION-DESIGN.md`
§3.2 Stage B/C) — but none of alx's 32 records of these types carry the
field yet, so the new compiler code has nothing to surface. Populating it
is a records-content decision (which cell does each analytical record
actually ground?), not a mechanical one, so it goes through review here
rather than being written directly.

**Method.** Three signal sources, in order of trust:

1. **Confirmed real usage** — a demonstration record already cites this
   analytical record in its `sources` field, and demonstrations already
   carry `canon_cells`. Only one record has this: `learning-community-tension`
   → `F6-P`, via `alx.demo.f6-p-someone-like-me`. Treated as settled, not
   proposed.
2. **Relations-graph inference** — the record's `relations` connect it to
   a `term`/`story`/`quote`/`doctrinal_witness` that already carries
   `canon_cells` (per the compiled `coverage.json`). Where a connected
   record's cell also matches the analytical record's own topic, that's
   the strongest non-confirmed signal.
3. **Topical match** — the record's `name`/`description`/`claim` read
   directly against the fleet's actual canon-question text for a cell
   (`records/_fleet/canon_question/`), independent of any relation.

Every row below marks **HIGH** (multiple signals agree, or a close direct
topical match), **MEDIUM** (one clear signal, some judgment involved), or
**LOW** (genuinely uncertain — flagged for a reviewer to decide, not to
rubber-stamp). Four records are flagged as possibly **not cell-eligible at
all** — distal/epilogue forces and one build-scope contested claim that
may describe the world's own historiography rather than anything a
participant would ask a Representative. Cells are not exclusive; a record
can carry more than one where the content genuinely serves more than one
question.

---

## Gravity (9)

| record | proposed cell(s) | confidence | rationale |
|---|---|---|---|
| `learning-community-tension` | **F6-P** | HIGH (confirmed) | Already cited by `alx.demo.f6-p-someone-like-me` (`F6-P`) — the door-line exemplar turn itself. |
| `teacher-bishop-tension` | F3-I; secondary F6-I | HIGH | F3-I's own question is "Who held authority among you, and how did anyone come to have it?" — the gravity's exact subject. Illustrated-by `story.origen-demetrius`, itself tagged F3-I/F6-I. |
| `martyrdom-contemplative-tension` | F6-E; secondary F3-I | HIGH | F6-E's question ("wanting to die as a martyr… isn't that a death wish?") is the tension's own content — is martyrdom formation, or something else. Illustrated-by martyrdom stories tagged F3-I. |
| `speculative-doctrinal-tension` | F1-P; secondary F1-E | MEDIUM | F1-P ("was there room among your people for doubt") maps to the speculative-freedom pole; F1-E (council/boundary-drawing) maps to the doctrinal-boundary pole. Split across two cells because the tension itself is genuinely two-sided — reviewer should confirm both belong, or pick the stronger one. |
| `scripture-formative` [PRIMARY] | F2-I; secondary F2-T | HIGH | Directly "Scripture as deep formative reality" — the F2 cluster's own subject. `term.allegoria` (already F2-I/F2-P/F2-T) is this gravity's own vocabulary. |
| `soul-transformation` [PRIMARY] | F4-I; secondary F1-T | MEDIUM | F4-I ("how did a person actually become one of you") matches the catechesis/purification/illumination progression described. `term.katechesis` is already tagged there. `term.theosis` (secondary) is tagged F1-T/C-T. |
| `logos-unity` [SUPPORTING] | C-T; secondary F1-I | MEDIUM | Logos-Christ identity is C-T's own subject ("Was Jesus God? Did you believe in the Trinity?"); `term.homoousios` is already tagged there. F1-I as the broader "what did you believe about God" fallback. |
| `divine-pedagogy` [SUPPORTING] | F6-P; secondary F2-P | MEDIUM | Its own third manifestation is persecution read as God's teaching — matches `alx.dw.f6-p-suffering` (already F6-P). Its second manifestation (scriptural difficulty as intentional teaching) matches F2-P's confusion-about-scripture question. |
| `learning-formation` [SUPPORTING] | F4-I; secondary F3-I | HIGH | Illustrated-by `story.gregory-formation`, already tagged F3-I/F4-I. "Learning IS formation" is F4-I's own becoming-one-of-you subject. |

## Force (18)

| record | proposed cell(s) | confidence | rationale |
|---|---|---|---|
| `apostolic-tradition` [1B init/internal] | F4-E | HIGH | F4-E's question ("How do you know your practices went back to the apostles and weren't later invented?") is this force's own description almost verbatim ("received as the deposit, not invented"). `alx.dw.f4-e-apostolic` already anchors this cell. |
| `johannine-logos` [1B init/internal] | C-T; secondary F1-I | MEDIUM | Foundational Logos-Christ identification — same subject as `logos-unity`, C-T. |
| `knowing-impulse` [1B init/internal] | F1-I; secondary F1-P | MEDIUM | "Genuinely knowing God, not merely holding right beliefs" reads directly against F1-I's "what did you believe about God." Named as the speculative-freedom pole's own ground (→ F1-P). |
| `philonic-inheritance` [1A init/external] | F2-I | HIGH | The allegorical reading method's own origin — F2-I is "how did you read your scriptures? what did you look for in them." |
| `platonic-environment` [1A init/external] | F1-I | MEDIUM (upgraded from LOW on review) | Under-weighted on first pass: `illustrated-by → alx.quote.clement-schoolmaster`, already compiled and tagged `F1-I`, carries this force's own manifestation almost verbatim ("philosophy... a schoolmaster... preparation, paving the way for him who is perfected in Christ"). That's a real signal-2 anchor, not just topical guesswork. Still not HIGH: F1-I's actual question set is God-belief content ("What did you believe about God?"), not "surrounding philosophical culture" — the 28 cells have no clean slot for an ambient-environment force, so the fit is real but not tight. F3-E ("what would an outsider have found strangest about you") remains a plausible alternative a reviewer may prefer. |
| `septuagint-inheritance` [1A init/external] | F2-I | HIGH | F2-I's own question ("was your Bible the same as ours") is precisely the LXX-vs-Hebrew-canon question this force names. |
| `gnostic-challenge` [2A ongoing/external] | F2-E; secondary F1-I | HIGH | F2-E's question ("What about the gospels that didn't make it in — were they suppressed?") is the rival-scripture/Gnostic-text subject directly. `term.gnosis` already tagged F1-I. |
| `neoplatonic-challenge` [2A ongoing/external] | F1-I | LOW | Porphyry's attack on Origen's allegory is closest to the F2 cluster's method-critique, but the force's own framing (a rival ascent-without-Incarnation system) reads more like general belief-content. Genuinely uncertain — flagging rather than guessing between F1-I, F2-P, and F3-E. |
| `arian-controversy` [2A ongoing/external] | F1-E; secondary C-T | HIGH | F1-E's own question ("I've heard a council basically voted Jesus into being God — is that what happened?") is this controversy's exact popular framing. |
| `persecution` [2A ongoing/external] | F3-I; secondary F6-E | HIGH | F3-I's question ("was it actually dangerous to be a Christian, day to day") is this force's direct subject. Illustrated by martyrdom stories already tagged F3-I/F6-E. |
| `scripture-ongoing` [2B ongoing/internal] | F2-I | HIGH | The ongoing-force version of `scripture-formative` — same cell. |
| `teacher-bishop-ongoing` [2B ongoing/internal] | F3-I; secondary F6-P | HIGH | The ongoing-force version of both `teacher-bishop-tension` (F3-I) and `learning-community-tension` (F6-P) combined — carries both. |
| `transmission-ongoing` [2B ongoing/internal] | F4-E; secondary F4-I | MEDIUM | How practices passed themselves on within the horizon — same transmission-fidelity subject as `apostolic-tradition`, F4-E. |
| `origen-demetrius-conflict` [3B ending/internal] | F3-I; secondary F6-I | HIGH | Illustrated-by `story.origen-demetrius`, already tagged F3-I/F6-I — the acute institutional expression of `teacher-bishop-tension`. |
| `post-nicene-authority-shift` [3B ending/internal] | F3-I | HIGH | Directly about how authority was structured and exercised late-horizon — same cell as the tension it completes. |
| `transmission-ending` [3B ending/internal] | *(none proposed)* | LOW — **flag** | Describes what passed *beyond* the world's own horizon (to later Byzantine/Syrian tradition) — a legacy/epilogue force, not something a participant inside the horizon would be asked about. Recommend confirming with Doc_04 reviewer whether this class of force needs `canon_cells` at all, or is analytical-only by design. |
| `arab-conquest` [3A ending/external, distal terminal] | *(none proposed)* | LOW — **flag** | Same shape as `transmission-ending`: describes the aftermath beyond the lived horizon. No natural participant question in the current 86. |
| `chalcedonian-fracture` [3A ending/external, distal] | *(none proposed)* | LOW — **flag** | Same shape again — postdates the world's own close. F3-T ("did you have denominations") is a weak stretch, not a real match; recommending no cell over a forced one. |

## Contested claim (5)

| record | proposed cell(s) | confidence | rationale |
|---|---|---|---|
| `allegory-from-within` | F6-I; secondary F2-I | HIGH | F6-I ("what did your people never settle?") is exactly what a *contested* claim record is for. Already associated-with `story.arsinoite-conference`, tagged F1-E/F4-T/F6-I. |
| `origen-positions` | F6-T | HIGH | `term.apokatastasis` (universal restoration) is already tagged F6-T, whose own question is "do you believe people like me are going to hell?" — directly the doctrine this claim contests. |
| `ecology-wide-primacy` | F5-I | MEDIUM | Same shape as the already-tagged `alx.limit.f5-women-own-words` (F5-I) — whose formation is and isn't attested is the stratum-bias question F5-I already carries for gender; this is its ecology-wide/class form. |
| `didaskaleion-institution` | F3-I; secondary F2-E | MEDIUM | Whether the "School" was a formal continuous institution bears directly on F3-I's authority-structure question. F2-E (record thinness/legend) as a weaker secondary. |
| `desert-attribution` | *(none proposed)* | LOW — **flag** | This is a cross-build scoping question (does desert monasticism belong to Alexandria's ecology) — build-methodology content, not something phrased as a participant's question anywhere in the 86. Recommend treating as analytical-only, no `canon_cells`, unless a reviewer sees a real conversational angle I'm missing. |

---

## Summary for the reviewer

- **28 of 32** get a proposed primary cell at MEDIUM or HIGH confidence
  (`platonic-environment` upgraded from LOW to MEDIUM on review — see its
  row; its `illustrated-by` anchor to an already-`F1-I`-tagged quote was
  under-weighted on first pass).
- **4 flagged for "possibly no cell at all"**: `transmission-ending`,
  `arab-conquest`, `chalcedonian-fracture` (all distal/epilogue forces —
  same underlying question: should ending-forces past the world's own
  horizon be cell-eligible by design, or are they structurally
  analytical-only?), and `desert-attribution` (a build-scope contested
  claim, not lived content).
- **1 at LOW confidence with a real cell guess anyway** (`neoplatonic-challenge`)
  — a genuine judgment call between adjacent cells, not a confident
  placement.
- The single confirmed real-usage anchor (`learning-community-tension` →
  `F6-P`) is the only one of the 32 not actually a proposal.

Once this is dispositioned, applying it is mechanical: add the agreed
`canon_cells` values to each record, gated normally (schema validation +
`gate_reciprocity` etc. already cover the rest).
