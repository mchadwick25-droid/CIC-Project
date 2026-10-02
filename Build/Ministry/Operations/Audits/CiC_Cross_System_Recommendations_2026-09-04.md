# Cross-System Recommendations — 2026-09-04

Requested by Mark: "look through the total system and make any recommendations
for improvement or growth." Produced by the Cross-System Analysis thread,
same session as the voice-perspective work logged in
`CiC_Cross_System_Analysis_Tracking.md`.

**Scope discipline, stated up front:** this thread's own mandate is
fleet-wide defects — things wrong the same way across every world — not
general system health, product strategy, or funding. What follows is sorted
into three tiers on purpose: findings this thread can act on, findings that
are real but belong to another thread's ground (surfaced, not touched), and
broader observations flagged lightly because they're outside even a generous
reading of this thread's authority. Nothing below was investigated by
guessing — each item names what was actually read or run to establish it.

---

## Tier 1 — cross-system findings, this thread's own ground

### 1. The modern-term anachronism bridge is fully built, tested, and almost entirely unpopulated

This is the strongest finding here — a real, high-leverage gap, not a defect.

`engine/m5/anachronism.py` is a complete, working mechanism: it scans a
participant's message for any fleet `modern_term` record's `display_terms`,
resolves it to the record id, and routes it to the Facilitator to bridge
("what you call X, they called Y") before the Representative ever has to
handle a term its own world's window didn't reach. It isn't a stub — its own
code comments cite two real bugs it fixed from a measured 2026-08-24 live
session (a model-invented id never matching the fleet's real id; a reader
that flagged "Trinity" twice and missed it once, now backstopped by direct
message-scanning that doesn't depend on the model noticing at all). It's
wired live into `engine/m4/turn.py` and confirmed still working today (this
session's own live re-proof run passed `anachronistic_term_ids` through it
against a real Bedrock call).

`records/_fleet/modern_term/` holds exactly **one** record: `_fleet.modern.trinity`.

Meanwhile, individual worlds are solving the identical problem
per-term, redundantly, in prose: 168 term records fleet-wide carry a
`false_friend` field, and a first-pass grep found at least ~28 of those
explicitly naming a later/modern-term distinction ("later," "modern," a
named anachronistic word) — the same kind of content the fleet mechanism
exists to centralize. This session alone touched several such cases
directly: `hal.term.vulgata` ("Vulgate"), `syr.term.catholicos`
("Catholicos"), `syr.term.memra`, `cappadocian.dw.not-later-formulas` and
`hal.dw.was-jesus-god` (both naming "transubstantiation" as the
participant's own later word) — every one of these is a `modern_term`
candidate being handled by hand, world by world, instead of once, fleet-wide,
through a mechanism that's already proven to work.

**Recommendation:** build out `records/_fleet/modern_term/` — Vulgate,
Catholicos, transubstantiation, original sin, canon, Bible (as a bound
volume), Pope, monk/monastery (for the two pre-4th-century worlds), sacrament,
excommunication are the candidates already visible from this session's own
reading, and a real per-world sweep of `false_friend` fields would find the
rest. This is populating fleet data behind an already-built, already-tested
mechanism — not new engineering, and squarely fleet-wide by nature (the
whole point of a `modern_term` record is that it's authored once and serves
every world whose window it postdates).

### 2. The self-reference defect survives in synonym form — a real, demonstrated recall gap, not fully closed

Already logged in today's earlier tracking-doc entries, restated here because
it belongs in a system-level view: `gate_voice_perspective` (added this
session) catches literal "this world" / "the world's..." / an it-its chain
following one. The Opus adversarial review of the Fable regeneration pass
found the *same* defect surviving in different words — "this community,"
"these churches," "this voice," "these people" — in records the mechanical
gate structurally cannot see, because they never contain the literal phrase
it checks for. Four such records were found and fixed by hand this session;
there was no exhaustive fleet-wide census of the synonym family the way
there was for the literal phrase.

**Recommendation:** a follow-up census specifically for this synonym
class before considering the self-reference defect closed. Not attempted
here — flagged, per this thread's own discipline of not asserting a defect
class is closed because a mechanical check went quiet.

### 3. A duplicate YAML key silently shadows content — found once, not yet checked fleet-wide

`records/syr/doctrinal_witness/syr.dw.decides.md` has two `retrieval:` keys
in its own front matter (confirmed pre-existing, not introduced by anything
this session touched). YAML resolves duplicate keys by taking the last one
silently — the first `retrieval` block (`tier: 1`, empty `retrieve_when`) is
dead, invisibly overwritten by the second. `gate_schema_validation` doesn't
catch this because both blocks are individually valid; it's the file having
two of the same key that's the problem, and nothing in the current gate
battery parses for that.

**Recommendation:** a small, cheap, high-confidence gate — read each
record file's raw YAML for a duplicate top-level key before `yaml.safe_load`
silently resolves it — plus a one-time fleet sweep to see whether this is a
single stray record or a wider pattern. Not yet run; found incidentally while
reading one file for an unrelated reason, so the true count fleet-wide is
unknown, not zero.

### 4. Mark's own FRE "hard edge" ruling isn't actually enforced anywhere — worth his direct read, not a unilateral fix

Corrects something said earlier this session: `engine/m7/readability.py`
**does** compute Flesch Reading Ease correctly (confirmed by reading the
function — same formula `VR_1A_NorthStar_Readability_Target_2026-08-09.md`
itself cites), so the claim that "nothing computes FRE" was wrong and is
corrected here. What's still true: Mark's own ruling in that same document
— *"hard edge, readability is the whole point... any single emitted turn
breaching FK ≤ 10 / FRE ≥ 60 fails the world"* — doesn't appear to be
enforced as a hard gate anywhere. M7's own docstring says its readability
instrument is "report-only per principle 10," which reads like a deliberate
architectural choice (measure before gating), not an oversight — but that
means a real, dated, "hard edge" ruling and the actual enforcement layer may
be out of sync, and this thread can't tell from the code alone whether that's
intentional-pending-more-baseline-data or a dropped thread.

**Recommendation:** not a fix — a question back to Mark (or whoever owns
the M7/register discipline) to confirm which is true before anyone builds a
gate for it.

---

## Tier 2 — real findings, belong to other threads' ground (surfaced, not touched)

- **`engine/api tests` is red on every `main` push**, root-caused by System
  Health (a regression test depends on historical package bytes deliberately
  excluded from git) and escalated to Mark as of today's tracking doc — not
  fixed yet, still red. Not this thread's to fix; noted here only because
  "total system" should include the fact that CI is currently red.
- **PR #10** — 25 days stale, real work stuck behind it (a round-cap change,
  a dormant Haiku fix with an ordering dependency), already flagged by
  System Health to Mark for a disposition call.
- **119 remote branches.** Not evaluated for which are safe to prune — that's
  a real judgment call (some may be legitimate in-flight world-thread work)
  — but worth a housekeeping pass by whoever has the standing view across
  all of them, since a repo this size makes "what's actually active" hard to
  answer by branch list alone.

## Tier 3 — broader observations, outside this thread's authority

- Cache economics (`engine/m8`) look healthy on the one live data point this
  session generated incidentally (Bedrock prompt caching engaging correctly:
  a write then three clean reads off the same prefix) — but a real cost/
  growth assessment is `engine/m8`'s and the funding-strategy thread's
  territory, not a spot-check.
- Product and participant-experience questions (more worlds, what a
  participant sees, platform choice) are explicitly owned by dedicated
  threads (`cic-frontend-strategy`, `cic-org-funding-strategy`) built for
  exactly this kind of question — not something this thread should opine on
  with any authority, even informally.

---

## What this thread would want to do next, pending Mark's word

In priority order, if asked to act: (1) populate `modern_term` records —
highest leverage, lowest risk, uses infrastructure already proven correct;
(2) the synonym-family census for self-reference; (3) the duplicate-key gate
+ fleet sweep. None of this is started; this document is the recommendation,
not the work.
