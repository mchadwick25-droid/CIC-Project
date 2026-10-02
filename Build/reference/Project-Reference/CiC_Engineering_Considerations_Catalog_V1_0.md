# Church in Conversation — Engineering Considerations Catalog

*Running catalog of durable engineering/architecture considerations that apply across build threads — not tied to one world, one document level, or one workstream. Purpose: the same "will this need a rebuild to grow" judgment shouldn't have to be rediscovered independently in a later thread. Not a governance document — a working reference, alongside the Cleaning Pattern Log, for any thread doing system, front-end, or deployment design work.*

*Format per entry: the risk, framed as cheap-to-build-in-now vs. expensive-to-retrofit-later; what to actually do about it at the current lean/prototype scale; what it protects when the project grows. Status marks whether this is still open, decided, or partially addressed. Entries are appended as they surface — no reordering required.*

---

## Consideration: World data schema should carry more than Phase 1 displays

**Category:** Data model / World Map readiness

**Status:** Open — no runtime data model exists yet to apply this to (see Layer 7/10 gaps, Engineering Spec §5.2–5.4)

**The risk:** Phase 1's world-browsing UI is a flat list of nine worlds. If each world's underlying record only stores what that flat list needs (name, description), then when the future World Map (abstract timeline, cross-era Table combinations, "shaped-by" relationships between worlds) gets built, every world record — eventually 50 to 100 of them — has to be retrofitted with temporal range, region, and relationship data after the fact, one world at a time.

**What to do now (lean):** No UI work required at Phase 1. Just make sure each world's record/schema includes fields for temporal start/end, region or geography, and an explicit (even if empty at first) "influenced-by / shaped" relationship, sourced from that world's own Forces Document (Doc_08). The data can sit unused; only the timeline visualization itself is future work.

**What it protects later:** The World Map becomes a visualization layer over data that already exists, not a data-collection project across every already-deployed world.

---

## Consideration: Retrieval should sit behind a clean interface, not be hardwired to one method

**Category:** Runtime architecture / Layer 7 retrieval

**Status:** Open — Layer 7 retrieval systems (Three-Level Transparency, Deployment Lexicon, Story Repository, World Context Layer) are not yet built at all (Engineering Spec §5.2)

**The risk:** Rule-based matching against a chunk's Retrieve-When conditions is the right, lean choice for now. But if application code calls that matching logic directly everywhere it's needed, swapping to semantic/embedding-based search later means touching every call site instead of one implementation.

**What to do now (lean):** Build retrieval behind one clean function/interface — something like "get relevant chunks for this message" — so callers never know or care whether the implementation underneath is literal condition-matching or embedding search.

**What it protects later:** Upgrading retrieval quality becomes a swap behind an existing seam, not a rewrite of every place retrieval is called.

---

## Consideration: The funding-model direction forces the accounts/identity question sooner than "later"

**Category:** Identity & access / Funding model

**Status:** Decided (direction) — Bible-Project-style free access for general users, with a possible paid tier gating pastor/academic tooling (Tours, sermon-prep, Academic Documents), never gating in-conversation Three-Level Transparency (Article 30 boundary — see below). Accounts mechanism itself: still open.

**The risk:** You can't gate a future pastor/academic tier without some notion of identity and entitlement — even if nothing is charged at Phase 1. If the data model has no concept of a user or a role until the day a paywall is actually built, that paywall requires an identity system built from scratch under time pressure, on top of whatever session model already exists.

**What to do now (lean):** At minimum, a role/entitlement field in the data model from day one — even just "sign in to save a role preference," non-monetized. Doesn't need real accounts infrastructure yet, just a place for identity/entitlement to live once it's needed.

**What it protects later:** Phase 2's paywall becomes turning on a feature against an existing field, not retrofitting identity onto every session record that came before it.

---

## Consideration: Build the real voice pipeline now, with a cheap voice selected — not a throwaway version

**Category:** Voice / TTS pipeline

**Status:** Open — voice is envisioned from Prototype Alpha (per phase table in Vision and Phased Plan) but not yet architected

**The risk:** It's tempting to stand up a simple, cheap voice system at Alpha and plan to "really build it properly" later once richer, culturally-matched, multi-language voice is affordable. That plan usually means throwing the first version away.

**What to do now (lean):** Build the actual pipeline shape now — how text becomes audio, how pronunciation/voice config per Representative is loaded and applied — just pointed at a cheap voice model. Richer casting later becomes a configuration change (swap the voice model ID), not new plumbing.

**What it protects later:** Voice quality upgrades don't require re-architecting how voice is invoked or configured per Representative.

---

## Consideration: Conversation logging for internal QA is in direct tension with participant privacy — needs one coherent policy, not two separate defaults

**Category:** Privacy / observability — flagged as time-sensitive, not a someday item

**Status:** Open — actively unresolved tension between two already-established requirements

**The risk:** The project's own review cycle (Engineering Spec §6) requires reviewing real conversation logs for drift, retrieval failures, and latency after prototype testing — meaning some conversation logging has to exist. Separately, the privacy/disclosure question (what's ever retained, what a participant is told before their first conversation) has been flagged as open multiple times without a decision. Left as two independent defaults, they'll likely collide in exactly the place that matters most: what an Alpha tester is actually told before they start talking.

**What to do now (lean):** One explicit, written answer — before Alpha testing begins — covering what's logged for internal review, how long it's kept, who can see it, and what the participant is told about that up front. Doesn't need to be elaborate; needs to exist and be consistent.

**What it protects later:** Avoids a retroactive disclosure problem once real participants have already had conversations under an undefined policy, and avoids the review cycle itself being blocked or improvised later.

---

## Consideration: Plan for world-content versioning separately from app-code versioning

**Category:** Deployment / content lifecycle

**Status:** Open — no Runtime State Model or deployment pipeline exists yet (Engineering Spec §5.1, §5.3)

**The risk:** World construction documents already iterate in practice (Source Ecology FINAL, FINAL_v2, Lexicon chunks FINAL_v3, etc.). Once a world is live, an update to its content needs a path that doesn't require a full app redeploy and doesn't break a session already in progress mid-conversation.

**What to do now (lean):** No infrastructure needs building yet — just don't let the Runtime State Model (§5.3) get designed without a concept of "which version of this world's deployment package is this session running," even if the only mechanism at Alpha is "don't update a world while anyone's mid-conversation."

**What it protects later:** Content updates become routine operations instead of each one being a small, risky redeploy.

---

## Related considerations already logged elsewhere (not duplicated here)

- **Article 30 boundary** (in-conversation Three-Level Transparency can never be gated; standalone tools like Academic Documents, Tours, and sermon-prep can be) — logged in the Front-End Decision Log, `Build/Ministry/Technology/CiC_FrontEnd_Decision_Log.md`.
- **Five-Representative ceiling has no system-level guard**, enforced by Facilitator judgment only — Engineering Spec §3.4, flagged directly as a callout for engineering.
- **World-click-menu architecture** (Description / Tour / Choose for Table / Academic Documents) should be built as a real four-option menu at Phase 1, with only Choose for Table functional and the rest visible-but-disabled placeholders — avoids a menu-concept rebuild when Phase 2 unlocks the rest. Logged in the Front-End Decision Log.
- **Three distinct transparency concepts get conflated easily**: Three-Level Transparency (Article 30), Transparency Mode (Simple Conversation vs. Transparent Sourcing), and the five-level confidence vocabulary (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin) are three separate mechanisms. Worth a standing check in any thread writing about "transparency" that it's naming which of the three it means.
