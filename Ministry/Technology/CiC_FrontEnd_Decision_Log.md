# CiC Front-End / Product Strategy — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning — including the "heart" reasoning, not just the operational one — and the specific next action. A decision that only lives in conversation history is a decision that gets re-litigated by accident later.

---

## 2026-07-07 — Voice at Prototype Alpha: Table Design Document governs

**Decided:** The engineering spec follows the Table Design Document (V2.3, Section 11) as written: Prototype Alpha ships text conversation *and* audio voice together, with a static picture background — not text-only. Mark's own framing for this thread ("text first, then pictures and voice") does not override this; it was reconciled rather than treated as a silent scope change.

**Reasoning:** The Table Design Document is a construction-complete, already-worked-out design document — Section 11's phase ladder is a considered position, not a placeholder. Flattening it to "text-only, voice later" would have quietly revised a governing document without that revision being named as a revision, which cuts against this project's own discipline (deferrals are documented, not hidden — Constitution Article 36). Reconciling before drafting, rather than guessing which framing was authoritative, kept the spec from being wrong on its very first structural section.

**Open question closed:** What did "text first" mean, if not a feature cut? Left unresolved in this pass — Mark accepted the Table Design Document's framing without specifying what he meant by his own phrase. If it resurfaces (e.g., as a build-sequencing preference for the engineer — stand up text before wiring voice — rather than a participant-facing cut), that's a distinct, compatible decision and can be layered in without contradicting this one.

**Next action:** Spec Section 1 ("What it looks like") states the phase-by-phase modality plainly, sourced to Table Design Document Section 11, with the static-picture-not-text-only distinction called out explicitly so a reader doesn't default to assuming a text-only Alpha.

---
