# Build Dispatch — Modern-Term Anachronism Bridge Buildout

**Dispatched 2026-09-04**, from the Cross-System Analysis thread's own
total-system recommendations pass
(`Ministry/Operations/Audits/CiC_Cross_System_Recommendations_2026-09-04.md`,
Tier 1 finding #1). That thread has the one view spanning every world and
every layer of the pipeline; this dispatch is the handoff to a thread that
will actually do the authoring work.

Paste this into a fresh thread to launch it.

## The finding this dispatch exists to act on

`engine/m5/anachronism.py` is a complete, live, already-proven mechanism:
it scans what a participant actually says for any fleet `modern_term`
record's `display_terms`, resolves a match to the record's own id (not a
model-invented guess — its own code comments document two real bugs this
fixed, measured on a real 2026-08-24 session), and routes it to the
Facilitator to bridge — "what you call X, they called Y" — before the
seated Representative ever has to field a word its own world's window never
reached. It's wired into `engine/m4/turn.py` and confirmed still working
today (a live Bedrock call this session).

`records/_fleet/modern_term/` holds exactly **one** populated record:
`_fleet.modern.trinity` (`origin_year: 325`). Every other later/modern term
a participant might bring to any of the 7 worlds is currently being handled
--- or not handled at all --- per-term, per-world, in each term record's own
`false_friend`/`senses.translational` prose instead of centrally through the
mechanism built for exactly this. 168 term records fleet-wide carry a
`false_friend` field; a first-pass grep on this dispatch's own session found
at least ~28 explicitly naming a later/modern-term distinction. That's a
floor, not a real count --- a real sweep is this dispatch's own first task.

## What governs

- **Schema**: Artifact-1 §4, `modern_term` record type --- `display_terms`,
  `origin_year`, `modern_sense`, `underlying_subject`, `distinguishing_claim`,
  `native_subject_map`. `engine/m1/schemas.py` has the enforced JSON Schema;
  `gate_schema_validation` already covers this record type, nothing new to
  build there.
- **The one existing exemplar**, read it before writing anything else:
  `records/_fleet/modern_term/_fleet.modern.trinity.md`. Its own body note
  names the design principle directly: *"the word is a later formalization;
  the question... is not --- the Facilitator strips the modern label and
  passes the underlying subject to the voice term-free."*
- **The live mechanism**: `engine/m5/anachronism.py`
  (`anachronistic_term_ids`, `resolve_term_ids`, `terms_in_message`,
  `mentions_term`), wired into `engine/m4/turn.py`. Read it before assuming
  how matching works --- it's whole-token, on the record's own authored
  `display_terms`, not fuzzy and not model-judged.

## What to build

1. **A real fleet-wide discovery sweep, not this dispatch's own sample
   list.** Grep every world's `term.false_friend`, `term.senses.translational`,
   `honest_limit.statement`, and `doctrinal_witness.text` for later/modern-
   term language (the census methodology in
   `CiC_Cross_System_Analysis_Tracking.md`'s 2026-09-04 forward-vantage entry
   is a reusable pattern for this kind of sweep, including how to hand-check
   candidates rather than trust a blind regex count). Candidates already
   visible from this session's own reading, as a starting list, not a
   ceiling: Vulgate (`hal.term.vulgata`), Catholicos (`syr.term.catholicos`),
   transubstantiation (referenced in `cappadocian.dw.not-later-formulas`,
   `hal.dw.was-jesus-god`, `hal.dw.sin-grace`), original sin as Augustine's
   technical doctrine (referenced in `alx.dw.original-sin`), a closed
   biblical canon as a settled category, "Pope" as a formal title (vs.
   informal usage), sacrament as a fixed sevenfold category, monk/monastery
   as an ordered rule-bound institution (relevant to `pahc` and early `syr`,
   both pre-dating organized cenobitic rule).
2. **For each real candidate, research a defensible `origin_year` with real
   sourcing** --- not estimated, the same discipline this project already
   holds source records to. `_fleet.modern.trinity`'s `325` (Nicaea) is the
   standard to match: a real historical event or text the word/category's
   own currency can be pinned to, stated plainly enough that another builder
   can check it.
3. **Write `modern_sense`, `underlying_subject`, and `distinguishing_claim`**
   matching the Trinity exemplar's register and precision --- these are
   build-facing (read by the Facilitator, not spoken by any Representative),
   so they follow the Facilitator's own etic register, not the emic we-voice
   rule that governs Representative-spoken fields.
4. **Populate `native_subject_map` only where a real record already answers
   the underlying subject in that world's own words** --- point at an
   existing `term`/`doctrinal_witness` id (the `fix: fix.term.the-three`
   pattern in the exemplar). Never invent a placeholder id or force a
   world's own thin ground to answer something it genuinely doesn't cover;
   an honest absence for a given world is a correct, complete entry, not a
   gap to fill.
5. **Do not touch any world's own existing `false_friend`/`senses.
   translational` content.** This dispatch is additive only --- a new fleet
   mechanism getting populated, not a rewrite of any world's own substantive
   content. Whether existing per-term prose becomes redundant once its
   `modern_term` sibling exists is a separate, later decision (the two serve
   different moments: the fleet record intercepts a participant's own
   anachronistic word before the Representative sees it; a term's own
   `senses.translational` is the Representative's own explanation once
   already mid-conversation about the concept) --- out of scope here.
6. **Verify against the live mechanism**, not just schema validation: the
   fixture world's own pairing pattern (`fix.term.the-three` +
   `_fleet.canon.c-t-01`, exercising the bridge routing described in
   Artifact-4 §3 step 3) is the template for proving a new `modern_term`
   record actually resolves --- `engine/m5/anachronism.py`'s own tests are
   the reference shape.

## What this dispatch does NOT include

Removing or rewriting any world's own `false_friend`/`senses.translational`
prose (see item 5 above). A live Bedrock re-proof battery confirming the
new records actually change real generated turns --- valuable, but real,
billed spend, and needs Mark's own explicit go-ahead before it runs, the
same standing rule this project holds everywhere else (not assumed just
because this dispatch authorizes the authoring work). Deciding whether
existing per-term anachronism prose should eventually be trimmed once its
fleet counterpart exists --- flagged above as a real, separate, later
question, not decided or attempted here.

## Coordination boundary

`records/_fleet/` is shared, fleet-wide ground --- every world's own
compiled prompt reads `_fleet.voice.fleet` and, per participant question,
whatever `modern_term` records match. Check for other threads' in-flight
work touching `records/_fleet/` or any world's own `false_friend`/`senses`
fields before landing a batch, same discipline the Cross-System Analysis
thread held for its own fleet-wide edits this session (base freshness
before and after, a fresh `git fetch` before pushing, coordinate rather
than silently collide).

## Completion criteria

Log real counts, not an estimate: how many candidates the sweep actually
found, how many records were authored, which `origin_year`s came with weak
sourcing (name them, don't smooth over uncertainty), and which worlds got a
real `native_subject_map` entry versus an honest gap. Log to
`Ministry/Operations/Standing/CiC_Cross_System_Analysis_Tracking.md` (this
finding's own origin) or this dispatch's own dated entry wherever the work
actually lands --- same convention as every other dispatch in this project.
