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
`OTHER_WORLDS` is **empty**.

**`PENDING_RECHECKPOINT` refilled the same day, deliberately**, by the v2
pass rolling from the Chloe pilot to the other five worlds (items 4b and
5). Five worlds now have an assembly ahead of what is deployed — +53 to
+216 words — each declared with its reason, each reported loudly on every
gate run, none swapped. Chloe is not among them: her v2 material was
already checkpointed and swapped, so she stays byte-identical. **Do not
swap any of the five until its checkpoint re-runs** — that is what the
registry has meant every previous time it was filled.

Items 2, 4b, 5, 6b(Chloe), 8 are done; 3, 4, 10 settled by the
Integration Design's adoption. All four remaining checkpoints ran and passed against the post-1A block
(Theon after Mark's per-world failure-measure ruling; Papnoute after his
density fix and a second checkpoint).

**Open for Mark, the whole remaining list:** items 6 and 7;
~~the standing scorer question~~ **RULED and implemented 2026-08-09**
(matched → FAIL, unmatched → WATCH; no existing verdict changed); and the palette's instruments: the **variance probe is BUILT and RUN**
(`scripts/variance_probe.py`, first run on Chloe 2026-08-09 — she chose a
different witness every time, phrase overlap 0.000–0.007), and the **cross-world probe is BUILT and RUN** against the live fleet
(2026-08-09: all six inside the B2 floor, zero phrase overlap between any
pair of worlds, on both questions). **Every instrument the 1A design
called for now exists and has been run at least once.**

**2026-08-09, Integration Design ADOPTED by Mark** — items 3 (instruments),
4 (the read = six-dimension grid) and 10 (sequencing: fleet work first,
remaining four worlds checkpoint once post-1A) are settled by adoption.
The block rewrite (item 2) executed the same day: ten new constructive
sections added (~1450 words), every defensive section intact, verified by
mock run and gates; every checkpoint artifact now stamps the shared-block
sha256 so pre/post-1A is a recorded fact.

---

## 1. Fix the Facilitator — **DONE AND VERIFIED 2026-08-09** (FK 12.4 → **8.37**, FRE 52.5 → **61.2**, breaches none)

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

**Done 2026-08-09.** A shared `PLAIN_SPEECH` block now appends to all
**16 participant-facing** facilitator prompts — reception, both handoffs,
bridge, frame-breaker response, closing, anything-else, both resource
prompts, the modern-term and epistemology bridges, and the four
safety-path prompts (acute distress A1/A2 + continuation, harmful
dynamic + continuation). The **model-facing** prompts are deliberately
untouched and asserted so: monitoring, both adjudicators, over-settling
screen, reroot, and both classifiers — nobody reads those.

The instruction itself measures FK 6.52 / FRE 75.05 — it meets the
standard it imposes. **Safety-path content is unchanged**: the block is
appended, never edited into the reviewed crisis wording, and plain
speech in a crisis serves those prompts' own purpose. **Extended same day on Mark's correction:** "it does not have a
glossary, so it shouldn't be pulling words, stories or quotes... it just
talks in modern english and acts as a bridge... it should be much
simpler." Two things followed.

**(a) The role is now stated, not just implied.** The shared block leads
with *Who You Are*: the bridge, no world of its own — no old vocabulary,
no stories, no quotable lines, no tradition to speak from; never reach
for a world's own word, story or quotation, because those belong to the
representatives. Its work named plainly: welcome, introduce, translate a
modern question inward, explain when a question comes from a later age,
and **name it aloud when a view is being pressed on a representative
rather than asked of them**. Then step back. (Architecturally this was
already true — the Facilitator receives no retrieved context, no lexicon
or story chunks — but nothing *told* it so.)

**(b) The prompts themselves were the deeper defect.** They were written
at **FK 11.3–11.5** — the instructions modelled the exact density they
were meant to prevent, teaching the register by example. Simplified:
handoff 11.35 → **7.22**, multi-handoff 11.29 → **7.04**, with every
substantive constraint kept (name, place, period, invitation, no
limitations talk, cautions-never-voiced). Reception 8.39 → 7.77,
closing 8.71 → 7.95 via the shared block.

**VERIFIED 2026-08-09** by `pahc_phase2_checkpoint4_full_2026-08-09-facverify`:
**FK 8.37 / FRE 61.2, breaches none** — inside the floor and in the 8–10
target band. Chloe unchanged in the same run (control held: only the
shared component moved).
Three participant-facing prompts remain dense and are deliberately
untouched for now: frame-breaker response (FK 11.5), epistemology bridge
(10.29), bridge (11.45) — all carry review history or safety weight, and
they now at least carry the shared block.

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

## 4b. Palette supply-side (curator's collection) — **ROLLED TO ALL SIX 2026-08-09** (Chloe 7 story records; Desert 4, Hieronymian 1 added on rollout; IJC/SYR/ALX carry none, honestly)

**Rollout finding, recorded rather than papered over.** Of the five
remaining worlds, only **Desert** and **Hieronymian** carry genuine
quoted material in their story text. Four Desert records and one
Hieronymian record gained a `key_line`, each asserted verbatim against
its own record's `text` at write time. **IJC (6 story records) and
Alexandria (10 story records) carry zero quoted lines**, and none was
invented for either — the Article 30 rule is that a citation points at
something real. **Syriac** was the sharpest case: a `key_line` was
applied to `syrstory004` and then **backed out**, because that world's
own post-history guard holds that *no line of our teaching survives word
for word*. Supply cannot manufacture what the record does not have; item
7's remaining call is now better informed for it.

*Original scope:*

Three records/runtime pieces the palette depends on: **`key_line`** — one
pre-vetted quotable line per story/source record (quotes are rare because
anti-fabrication rightly suppresses invented ones; supply, not
permission, is the fix; schema addition, same pattern as ceiling_words);
**witness variety** — the same theme answerable from more than one
witness so evidence can vary across conversations; **session flavor
ledger** — runtime memory of stories/quotes/figures used, re-use taking
callback framing (folds item 6's option (b) in). Records-schema pieces
are Mark's license, as frozen ground truth.

## 5. Layer 2 engagement demonstrations — **ROLLED TO ALL SIX 2026-08-09** (`pahcdemo007` pilot + `ijcdemo009`, `alexdemo008`, `desertdemo010`, `syrdemo008`, `haldemo010`; every world's selector now picks three DIFFERENT shapes)

**Rollout, 2026-08-09.** One engagement demonstration authored per
remaining world, each verified selected into its assembly, each inside
its own world's `typical_words` on every turn, all thirty Representative
turns measured (not hand-counted) and readability-clean:

| record | world | shape | words/turn | FK / FRE |
|---|---|---|---|---|
| `ijcdemo009` | Marius | the vigil in the basilica; attested/not-attested drawn inside the telling | 93, 96, 82 (typ 115) | 4.80 / 83.4 |
| `alexdemo008` | Theon | Leonidas and Origen; weaker particulars weighed in the telling, answer-first | 112, 105, 76 (typ 140) | 5.19 / 85.2 |
| `desertdemo010` | Papnoute | Abba Moses and the leaking jug; key_line quoted whole, nothing added after | 45, 38, 42 (typ 55) | 3.50 / 91.9 |
| `syrdemo008` | Yausep | the Abgar–Addai founding account held as account, not history | 79, 63, 78 (typ 98) | 5.96 / 76.6 |
| `haldemo010` | Albina | the Ciceronian dream; one interested witness named in the telling | 78, 87, 77 (typ 120) | 4.21 / 89.9 |

Every one ends on a genuine question back to the visitor — the behaviour
the post-1A measurement found at **zero** across every measured run and
which prose alone did not move. Zero readability violations; zero turns
over typical, let alone over ceiling. Displacements are recorded in
`PENDING_RECHECKPOINT`: 009 displaces `ijcdemo006`, 008 `alexdemo007`,
010 `desertdemo009`, 008 `syrdemo007`, 010 `haldemo007` (that last one
deliberately carrying `haldemo007`'s caveat-in-the-telling function
forward on different material, so the Blueprint's required kind stays in
the assembled prompt).

**Two honest constraints held rather than worked around.** Yausep's demo
carries **no quoted line at all** — his guard holds that no line of his
teaching survives word for word, and a `key_line` briefly applied to
`syrstory004` was **backed out** for the same reason. Marius's and
Theon's carry none either, because their story records contain zero
quoted lines and none was invented.

*Original scope:*

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
