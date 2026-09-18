# Built-World Voice Alignment — Decision Log

Dated entries: what was decided (or is still open), the reasoning, and
the next action.

## 2026-09-17 — Workstream opened

Mark's charter: one consistent, human, participant-facing voice across
every touchpoint between browsing the site and a conversation with a
Representative. First concrete task: locate where each of the 8 built
worlds' conversation-opening introduction actually lives — the launch
prompt guessed it was authored per world somewhere under `worlds/<code>/`.

**Finding, not the guess:** there is no per-world opening line. Every
world's literal first conversation line is one shared, hardcoded
Facilitator template (`DOOR` in `engine/m4/facilitator_turns.py`),
deliberately not world-voice ("the Facilitator speaks for the system,
not for a world... a fixed table, never a prompt") and already
Mark-approved (2026-08-25). The real per-world, threshold-facing text
sits one screen earlier: the **Arrival screen**
(`cic-poc/frontend/src/components/Arrival.tsx`), rendering
`doorway_description` and `thinness_statement` straight from each
world's `records/worlds/<code>.yaml`. Touchpoint 4 revised to this.

Full findings and the touchpoint map: artifact `The Fourth Touchpoint`
(https://claude.ai/artifact/7N2wpobk9VbUhLG1VLzJ5u).

## 2026-09-17 (same day) — DOOR's own words didn't align; fixed

Mark's ruling on the DOOR mechanism itself: "it is fine to come from the
facilitator, but the words of the facilitator should align with the text
the world has." Concrete defect found: DOOR's world-name slot was fed
each world's scholarly `display_name` (e.g. "Imperial and Juridical
Christianity"), never the plain `card_name` every other participant-
facing surface uses ("Church and Empire") — a mismatch across 7 of the 8
built worlds. Mark picked the data-source swap (registry `card_name`
over compiled `display_name`, falling back only for the non-participant-
facing `fix` fixture). Shipped same day: `engine/m4/facilitator_turns.py`,
`engine/api/wiring.py`, `engine/api/table_wiring.py`, new regression
coverage in `engine/m4/tests/test_facilitator_turns.py`. Full detail
logged in `Ministry/Technology/CiC_FrontEnd_Decision_Log.md` alongside
DOOR's original approval (git commit on
`claude/amazing-lovelace-coy644`).

## 2026-09-17 (later) — Doctrine field: Atlas-owned, not in scope yet

PR #246 (Atlas/Church Family Tree thread) adds a structured `doctrine`
field (belief-statement objects, not prose) to 6 of the 8 built worlds'
Atlas entries. Asked Mark whether this thread shares ownership of it or
leaves it entirely to the Atlas thread.

**Mark's ruling:** it's an Atlas entry this thread *can* draw on "if
there is a place that it helps the participant in knowing what to ask" —
but "maybe not yet." Reading: `doctrine` stays Atlas-owned data; this
thread doesn't edit or take responsibility for it. A future touchpoint
that helps a participant formulate questions (most plausibly the
Arrival screen's `starters`, or the "More information" page) could draw
on it, but that's not scoped into current work — tracked here as an open
possibility, not a task.

## 2026-09-18 — Touchpoints 1–3 audited; mechanical batch fixed

Audit findings: artifact `The Drift Report`
(https://claude.ai/artifact/WUFC7PeNmncENMKMo1U6Gs). Before trusting the
subagent's headline finding, verified it directly and had to correct the
severity: `atlas-v3.html` has no `fetch()` call anywhere in the file — it
never reads `world-census.json` at runtime, so the raw Ministry
build-process text the audit found in that JSON's `gallic` `why` field
("Not a Step 0 verdict... Doc_01 found the southern pair... admitted
2026-09-13") was never actually shown to a participant. The real live
defect was smaller: gallic's *embedded* `why` in `atlas-v3.html` never
invited the participant to talk to Renatus, unlike every other built
world's template ("...you can have a conversation with X, right now").

Mark said "go" on the mechanical batch (restorative/templated fixes,
nothing newly invented):

- **6 of 8 worlds' `longDescription`** synced in `atlas-v3.html`'s
  embedded data from the richer, more complete `world-census.json`
  copy — pahc (Ignatius's own words, the Pliny/deaconesses paragraph),
  alx (the Eusebius source-critical sentence, the Nepos/Dionysius
  paragraph), syr (named sources restored - Chronicle of Edessa,
  Theodoret, Yazdegerd I - in place of "tradition"/"another source"),
  desert (the Kellia commercial-center sentence), ijc (the full 386
  Ambrose basilica standoff and the origin of antiphonal hymn-singing),
  hal (the Jonah-translation riot and Augustine's letter to Jerome).
  cappadocian and gallic already matched — untouched.
- **gallic's `why`** fixed in both `world-census.json` (source hygiene —
  cic-website/ is a named live/canonical surface, and raw build-process
  narration in it is exactly the corruption CLAUDE.md's "keep live/
  canonical surfaces clean" rule warns against) and `atlas-v3.html`
  (the live fix) to the same template every other built world uses:
  "This Christian tradition is fully built, and you can have a
  conversation with Renatus, a bishop, right now."
- **gallic's `tile`** — the tradition page had one extra, accurate
  closing sentence ("The story closes around the year 450...") the
  JSON/homepage copy lacked. Added it to `world-census.json` and
  `index.html` so all three surfaces now match.
- **Dead `informalName` field** — confirmed zero call sites anywhere in
  `cic-website/` (real, unused data). Deleted it from `cappadocian` and
  `gallic`'s records, the two whose value actually disagreed with their
  own `card_name` (the other 6 built worlds' values were redundant but
  correct, so left alone — not this pass's problem to fix).

Verified: exact post-edit text match against the JSON source for all 7
sync targets; `atlas-v3.html`'s embedded `DATA` object still parses as
valid JSON (292 movements) after the surgical edits; `world-census.json`
still valid JSON; `engine/m6/tests/test_census_sync.py` (11 tests) still
passes.

### Next action

Held back, not yet touched: the three tiles running 2–2.5x the craft
doc's own sentence-length target (cappadocian, ijc, hal) — that's a real
rewrite, not a sync, and needs drafts put to Mark before anything
changes. Going through them one at a time, each as a readable
before/after artifact, per Mark's request.

## 2026-09-18 (later) — Tile 1 of 3 (ijc, "Church and Empire") redrafted

Original: 3 sentences, 132 words, every sentence 35–50 words. First
draft put to Mark as an artifact (current vs. proposed, full text,
word counts, no invented content). Mark's one note: "the first
sentence is too complex, make it two thoughts" — it was doing three
jobs at once (where, when, what changed). Split into a where/when
sentence and a what-changed sentence; everything after was already
approved as drafted. Mark: "yes much better."

Final tile (7 sentences, 126 words, 26/27/31/5/8/10/19, no two 30+
adjacent): "Bishops in Rome, Constantinople, and Milan lived through a
real change between Constantine's toleration of the church in 312 and
the Council of Chalcedon in 451. They stopped being outlaws beneath
the sword and became office-holders beside a throne — hearing
lawsuits, managing imperial funds, summoned to councils at the
emperor's own expense. Three claims to final authority over the
church rose in this window: Rome's from Peter, Constantinople's from
nearness to the throne, a bishop's claim to stand in judgment over
any ruler. The question was never settled. This world's worst hours
were caused, not suffered. One was a bloody contest over the
bishopric of Rome. The other was a massacre an emperor ordered — then,
at his own bishop's insistence, did public penance for."

Applied to all three surfaces that carry this field (confirmed
identical before editing, so no drift to reconcile): `world-census.json`
(`entry.tile`), `index.html`'s homepage card, and
`traditions/imperial-juridical-christianity.html`. Every fact preserved
— three places, two dates, all three rival claims and who each rests
on, both worst-hour events, the penance. Nothing added, nothing cut.

## 2026-09-18 (later) — Tile 2 of 3 (hal, "The Bethlehem Circle"); principle generalized

Densest of the three: 3 sentences, 134 words, 52/46/36 words each.
Same split-by-claim approach put to Mark as an artifact. No specific
objection raised; instead Mark generalized directly: **"now use this
same principle in all writing."** Recorded as its own craft-doc
section (`CiC_Prose_Craft_Analysis.md` §10, "One claim per sentence")
so it governs future writing project-wide, not just these three
tiles — flagged honestly in that doc as a separate source from the
original pahc-corpus sections 1–9, per this project's own citation
discipline.

Final tile (9 sentences, 135 words, 26/11/16/20/8/19/4/18/13, longest
26 words): "In Rome and then Bethlehem, from 382 to 420 CE, a circle
of wealthy women and one scholar-priest practiced renunciation and
scholarship as a single discipline. Fortunes were converted into
text, hospitality, and care for the sick. A Latin Bible was built
word by word against the Hebrew it was first written in. The women
funded it, founded it, and — by Jerome's own account — pressed him
with scriptural questions for decades. But Jerome wrote nearly every
surviving page himself. How much independent authority his account of
them actually reflects is a question this world's own record cannot
settle. The cost was concrete. In 384 a daughter of the household died
within four months of taking up Jerome's own fasting regime. Rome's
outrage over it helped drive the whole circle out of the city."

Applied to all three surfaces (confirmed identical before editing):
`world-census.json`, `index.html`, `traditions/
hieronymian-ascetic-literary.html`. Every fact preserved, including
the world's own honest hedge about how much of the record is really
the women's own voice versus Jerome's.

### Next action

Tile 3 of 3: cappadocian, applying §10 directly.

## 2026-09-18 (later) — "Entire ecology" pass: naming erasure, then a real factual error

Mark's note on the cappadocian draft ("carried by one family and one
friendship... I feel like they were core but not everything of the
world") generalized into a full-corpus check: does any tile let a
small named core, or an anonymous collective, stand in for the whole
movement's real ecology? Checked all 8 against their own
`longDescription`.

**Clean:** `pahc`, `syr`, `desert` already describe the movement's real
structural plurality rather than centering a small named core. `alx`
is a soft, lower-priority case — already hedged honestly, just stops
on an early anecdote.

**Needed the pass:**
- `cappadocian` — "carried by" fixed to "had... at their center";
  added Macrina's own action (not just "his sister"), the pastoral
  dimension (famine response, hospital — literally in this world's own
  registry name), and named the martyr Eupsychius.
- `ijc` — Ambrose, Theodosius, and Damasus restored by name (two of the
  tile's three "worst hours" claims belonged to specific documented
  people, reduced to "a bishop" and "an emperor"). Then Mark's follow-up
  ("there was more to the movement than the political inclusion") caught
  that even with names restored, every claim was still about power —
  added the Chalcedon doctrinal content (Leo of Rome's letter on Christ's
  two natures), currently used only as an end-date. Two further
  dimensions found but held for Mark's call rather than added unasked:
  the origin of Western hymn-singing, and the Callinicum synagogue-
  burning episode ("the hardest evidence against this world... not what
  was done to it, but what it did").
- `gallic` — the most anonymized tile of all 8: zero proper names
  anywhere despite Martin, Honoratus, Cassian, and (per this world's own
  sourcing record) Vincent of Lérins all being specifically documented.
  Also missing entirely: the Augustine/predestination controversy that
  provoked three of Augustine's own treatises against these monks.

**Then Mark asked a harder question: "let's not overstate the
persecution, be honest to the sources and context" — followed by his
own doubt, "maybe i'm wrong... am I applying the pahc situation against
this one."** Checked case by case against each figure's own record
(one tier more careful than longDescription) rather than assuming
either way:

- `ijc`'s Damasus/Theodosius/Ambrose material: **not an overstatement.**
  All three figure records are `verification_state: verified-direct`,
  `citation_specificity: A` — this project's top confidence tier.
  Damasus's own record states directly: "This world tells that fact
  rather than hiding it." Applying the caution here would have been
  the wrong call.
- `cappadocian`'s Eupsychius line ("Julian's brief pagan revival cost
  them a martyr") **did overstate it** — his figure record is an
  explicit "NO-STORY BOUNDARY FIGURE": only "martyred under Julian in
  362" is Widely Accepted; any causal narrative beyond that is flagged
  out of bounds for this world's own sources. Fixed to "This world
  buried a martyr, Eupsychius of Caesarea, executed under Julian in
  362."
- `cappadocian`'s Gregory of Nyssa line ("The Homoian church... drove
  [him] into exile") **also overstated it** — his own story record
  says the charges were nominally financial mismanagement, and the
  "trumped up, packed synod" characterization is explicitly Basil's
  own partisan defense of his brother, "carried here as exactly that,
  not as an adjudicated verdict." Fixed to name that attribution
  directly.
- `hal`'s already-shipped line ("Rome's outrage... helped drive the
  whole circle out of the city") turned out to be **a real factual
  error, not just an overstatement.** Marcella's own figure record: she
  founded the circle before Jerome ever arrived and stayed in Rome
  until her death in 410. Only Jerome left in 385, followed later by
  Paula and Eustochium. Fixed immediately (already live): "Rome's
  outrage over it helped drive Jerome from the city — though not the
  whole circle: its founder, Marcella, stayed in Rome for the rest of
  her life." Applied to all three surfaces.

### Next action

cappadocian's revised tile (ecology additions plus the two
source-honesty fixes above) is with Mark for review, not yet shipped.
`ijc`'s Chalcedon addition and the two held-back dimensions
(hymn-singing, Callinicum) are also awaiting his call. `gallic`'s
naming pass is drafted and awaiting review.

## 2026-09-18 (later still) — Stop patching; rebuild all 8 tiles from the records

**Mark's ruling:** "i feel like we need to start over and build these
from scratch from the records in this new voice simplicity. we are
finding too may mistakes and mis-focused statements." This is "no fix
on a fix" (CLAUDE.md) applied at the workstream level: three rounds of
patching (readability, ecology, source-honesty) kept surfacing new
defects in the same tiles, which means the tiles were never soundly
built to begin with — patching them further just stacks a fourth
layer on an unsound base.

**New method, all 8 built worlds' `entry.tile`:** draft fresh from each
world's own primary records (`world_core`, `figure`, `story` — not the
existing tile text, and not `longDescription` either, since it's one
step removed from the primary records and has its own inherited
compressions) rather than editing the existing tile. Every draft
applies, from the start rather than patched in after the fact:

- **§10, one claim per sentence** (`CiC_Prose_Craft_Analysis.md`).
- **Full ecology** — the movement's real range (doctrinal, pastoral,
  social, monastic, as each world actually has them), not a small named
  core or a single dimension standing in for the whole.
- **Source-honesty against each figure/story record's own confidence
  tier** — a "Widely Accepted" bare fact stays a bare fact; a claim
  carried as one side's own partisan framing (per a record's own
  `divergence_note`) gets attributed as such, not presented as settled;
  a "NO-STORY BOUNDARY" figure gets no narrative causation invented for
  them.

Scope: `longDescription` is not being rebuilt — its content held up
well under the same scrutiny (only mechanical JSON-vs-live drift was
found there, already fixed; no source-fidelity defects). This pass is
`entry.tile` only, across all 8 worlds, including `pahc`/`alx`/`syr`/
`desert`, which only had a lighter longDescription-comparison check
before, not the full records-based pass now being applied everywhere
else.

### Next action

Research each world's primary records (world_core, figure, story) to
build a fresh tile per world, one at a time as before, starting with
the four worlds already deep in revision (cappadocian, ijc, gallic,
hal) so the source-honesty work already done there isn't lost, then
the four checked only at the lighter longDescription level
(pahc, alx, syr, desert).
