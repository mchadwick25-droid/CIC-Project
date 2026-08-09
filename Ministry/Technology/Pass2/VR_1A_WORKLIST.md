# Voice Rebuild — 1A Worklist

**What this is.** The single place 1A work items live. Created 2026-08-09
on Mark's instruction ("add fixing the facilitator to the 1A worklist"),
consolidating the items that until now were scattered across the baseline
read findings, the informal category read, the 1A reassessment, and the
checkpoint watchlist. Per the standing interpretation
(`decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`): 1A is the
accessible-rigor goal everywhere it lives, and this list is its backlog.

The governing documents: the north star + B2 target (hard edge ruled) and
the Writing Standard (`decisions/VR_1A_Writing_Standard_2026-08-09.md`,
Mark's text verbatim).

Items marked **PENDING MARK** need his ruling before work starts; items
marked **READY** are decided in substance and waiting on sequencing.

**STATE AS OF 2026-08-09 END OF DAY — ALL SIX WORLDS LIVE.** **All six worlds are SWAPPED AND LIVE** — Chloe, Marius, Yausep, Theon,
Albina, Papnoute. `assembly_identity` reports byte-identical for all six;
the deployed leak gate reports **GATE PASSED fleet-wide**;
`PENDING_RECHECKPOINT` and `OTHER_WORLDS` are both **empty**, each
resolved the way its own registry said it must be. Items 2, 4b, 5, 6b(Chloe), 8 are done; 3, 4, 10 settled by the
Integration Design's adoption. All four remaining checkpoints ran and passed against the post-1A block
(Theon after Mark's per-world failure-measure ruling; Papnoute after his
density fix and a second checkpoint).

**Open for Mark, the whole remaining list:** item 1 (the **Facilitator**
— the one voice still breaching the B2 floor in every run measured, and
now the only known accessibility defect in the system); items 6 and 7;
the standing scorer question (should the sustained bar consult
`matched_contested`, now with **five** concessions fleet-wide, every one
of them `null`); and the palette's real instruments — the variance probe
and cross-world probe — which the saturated 8-question battery cannot
substitute for.

**2026-08-09, Integration Design ADOPTED by Mark** — items 3 (instruments),
4 (the read = six-dimension grid) and 10 (sequencing: fleet work first,
remaining four worlds checkpoint once post-1A) are settled by adoption.
The block rewrite (item 2) executed the same day: ten new constructive
sections added (~1450 words), every defensive section intact, verified by
mock run and gates; every checkpoint artifact now stamps the shared-block
sha256 so pre/post-1A is a recorded fact.

---

## 1. Fix the Facilitator — READY (added by Mark, 2026-08-09)

The shared Facilitator voice (`app/prompts/facilitator_prompts.py`)
**breaches the B2 floor in 3 of 3 measured runs** — FK 11.9/FRE 44.9,
FK 10.5/58.9, FK 12.4/52.5 — the least readable voice on the
participant's screen, and until 2026-08-09 the one voice every harness
deliberately skipped. Scope: rewrite the Facilitator's participant-facing
prompt text to the Writing Standard. The Facilitator speaks etically, so
it may use the standard's own phrasing directly ("historians disagree,"
"the evidence suggests") — no emic translation needed. Verify via the
facilitator-readability report now emitted by every checkpoint; the
breach never fails a world's checkpoint (shared component ≠ per-world
records defect). Note the monitoring prompts (drift signals etc.) are
model-facing, not participant-facing — only participant-visible turns
are in scope.

## 2. The shared `_HOW_YOU_ENGAGE` rewrite — **DONE 2026-08-09, verification pending**

The Blueprint's original Phase-1A task, still unexecuted (the block
predates the rebuild; none of Design §2's six additions are in it).
Content now comes from three sources: Design §2's list (bridge-first
entry, candidate-understanding offer, callback license, lead-with-insight
with both field names, three-way disagreement license, shape repertoire),
the Writing Standard (explain before naming; one idea per paragraph,
pause; define terms naturally; transparent uncertainty in the emic
register), and the **Conversation Palette + Response Composition Protocol**
(`decisions/VR_1A_Conversation_Palette_2026-08-09.md`, Mark verbatim) —
the constructive half: sixteen truthful moves available never mandatory,
intent over pattern (the gravity index IS the hidden-opportunity map),
sources as witnesses ("which witness best answers this question?"), the
curator principle as governing sentence. The block's existing defensive
sections stand. Measurement is session-level palette diversity, never
per-turn structure compliance.

Evidence the constructive half is needed (measured 2026-08-09, 16 probe
turns across two worlds): 0 turns tell a story, 1 carries a quotation,
0 end with a question back (DECLINING_INITIATIVE blind to it — fired 0),
'we believed/held' lands in only 2 of 8 turns per world, and Marius names
Leo 4x / Ambrose 5x in 8 turns with no session memory anywhere.

## 3. Engagement instruments — PENDING MARK (reassessment decision 1)

Before the block rewrite is graded: first-sentence-uptake analyzer,
bridge-first manual-read rubric with regex floor, **2 genuinely ambiguous
probes per world** (the candidate-offer mechanic currently has zero test
cases anywhere), callback-occurrence transcript check.

## 4. The blind paired read — PENDING MARK (reassessment decision 2)

1A's human bar, replacing the dangling Objective-3 clause: same 8 probes,
pre-1A vs post-1A block, scored blind. Now carries the Writing Standard's
dual-audience principle explicitly — two questions per transcript:
*could you follow it easily* (newcomer) and *do you recognize careful
scholarship* (historian/pastor/seminary reader). The second audience is
currently tested by nothing.

## 4b. Palette supply-side (curator's collection) — **LICENSED + PILOTED ON CHLOE 2026-08-09** (key_line + signature on 7 story records, rendered into chunk headers; session flavor ledger deliberately deferred until repetition exists to manage)

Three records/runtime pieces the palette depends on: **`key_line`** — one
pre-vetted quotable line per story/source record (quotes are rare because
anti-fabrication rightly suppresses invented ones; supply, not
permission, is the fix; schema addition, same pattern as ceiling_words);
**witness variety** — the same theme answerable from more than one
witness so evidence can vary across conversations; **session flavor
ledger** — runtime memory of stories/quotes/figures used, re-use taking
callback framing (folds item 6's option (b) in). Records-schema pieces
are Mark's license, as frozen ground truth.

## 5. Layer 2 engagement demonstrations — **LICENSED + PILOTED ON CHLOE 2026-08-09** (`pahcdemo007`: story-with-caveat + key_line quoted + ends on a real question; selector now picks three DIFFERENT shapes. Rolls to other worlds with their v2 passes.)

One per world: **the hardest thing this world holds, said so a newcomer
understands it, without softening** — the Writing Standard's "complex
ideas expressed simply" as a worked example, scored in an engagement
vocabulary. Currently all Phase-2 demonstrations score fidelity traits
only. Alternative: ship 1A prose+code only and let pilot readers judge.

## 6. Demonstration reuse (Paula-story finding) — PENDING MARK

His baseline read: the selector has no within-session memory; Albina
retold the Paula story twice, unaware. Options he left open: (a) track
used demonstrations and deprioritize repeats, (b) require explicit
callback framing on genuine re-use — (b) doubles as a live demo of the
callback license.

## 6b. Transparency verified visible — **CLOSED FOR CHLOE 2026-08-09** (backend two-tier gloss detection 0/8→4/8; `GlossHighlight` falls back to the original phrase for `inline:false`; citations verified wired end to end). Still REQUIRED per world before each swap.

His read of the blinded transcripts surfaced it: "we still need to make
sure the 3 level transparency and lexicon, story, quote, and general
referencing are all working well." Findings: **citations fire 4/8 turns
with full Article 30 payloads** (working — my read page had hidden them;
now shown); **glosses fire 0/8 on every Chloe arm** — her lexicon
surfacing never triggers at runtime and must be diagnosed and fixed
BEFORE her swap; quote referencing now has supply (key_line) but
coverage remains thin. No world ships until its transparency stack is
verified firing AND visible to the participant.

### 6b verification result (2026-08-09, static wiring check)

**Citations: VERIFIED wired end to end** — `MessageBubble` passes
`message.citations` to `CitationMarker`/`CitationModal`; payloads proven
rich in the artifacts. **Glosses: one frontend change needed for tier-2**
— `GlossHighlight.tsx` highlights only occurrences of each gloss's
`rendered` string (its own line 51), so an `inline: false` gloss (original
phrase spoken naturally, rendered form absent — Chloe's whole case) passes
to the frontend and renders NOTHING. Fix: in the matching loop, fall back
to `g.original` when the rendered string is absent, and add optional
`inline?: boolean` to `GlossUsed` in `types/conversation.ts`. ~5 lines,
then a live browser check as the pilot's first click. Chloe's swap waits
on this.

## 7. Quotes / citation coverage — PENDING MARK, partially moved already

His baseline read found citations firing on ~21% of turns fleet-wide.
The rebuilt worlds now fire 4–7 of 8 probe turns, so the records rebuild
moved this substantially. Remaining call: (a) wiring/visibility fix only,
(b) increase verbatim primary-source quoting in-voice (authoring cost,
six worlds), or both.

## 8. "What would people today get wrong" pattern — **DONE 2026-08-09** (via the block's new "You Do Not Know What Another Age Thinks" section)

His informal-read catch, logged fleet-wide: Representatives answer with
confident knowledge of what "modern people" think — an anachronistic
awareness. Better shape (his own): answer from uncertainty about *any*
outside era looking in. A prose-shape fix in the shared block (item 2)
plus a probe-phrasing check; this question type recurs in the batteries.

## 9. Sentence tail — watch, no bar ruled

9–17 sentences per run over the standard's 25-word guard (worst 46w)
while averages sit in-band. Reported per world by the sentence-discipline
instrument; accumulates on the watchlist. A bar, if one is ever ruled,
comes from that data — not invented mid-stream.

## 10. Sequencing — PENDING MARK (reassessment decision 4)

Recommended: run items 1–2 (facilitator + block rewrite) before the
remaining four world checkpoints, so Chloe's and Marius's completed runs
become the pre-1A arm of the paired read and the remaining worlds are
checkpointed once, against the post-1A block. Cheaper than six-then-redo.

---

*Cross-references: fleet watch items live in
`gates/voice_rebuild_checkpoint_watchlist.md`; the structural analysis
behind items 2–5 is
`Ministry/Operations/Audits/CiC_VoiceRebuild_Blueprint_2026-08-08/CiC_VoiceRebuild_1A_Design_Reassessment_2026-08-09.md`.*
