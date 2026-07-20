# Front-End Brand Alignment Review — V0.1

**Date:** 2026-07-17 · **From:** the branding workstream (Brand Foundations now
govern all public-facing language and presentation, per Mark) · **To:** the
front-end workstream and Front-End Graphics thread, which own the changes · **For:**
Mark's review with his front-end hat on.

**What this is:** a full inventory of the prototype app, the front-end documents,
and the three HTML demos, checked item-by-item against the Brand Foundations
(`Ministry/Communication/CiC_Brand_Brief_V0_1_DRAFT.md` +
`CiC_Messaging_Branding_Kit_V0_1_DRAFT.md`). Sorted: what already aligns, what
conflicts (by participant-visibility), and what genuinely needs Mark's decision.
Judgment is applied — mechanical word-matches that are actually correct usage are
cleared, not flagged.

---

## 1. Already aligned — worth knowing before fixing anything

The prototype's instincts were right long before the kit existed:

- **"Participants," never "users," everywhere in product code.** The app UI and all
  Facilitator prompts use "participant" without exception. (The word "users"
  appears only in internal design prose — see §3.)
- **The we-voice discipline** is strong and participant-facing:
  "each one represents a whole tradition's documented life… a discipline against
  fabricating a person" (facilitator_prompts.py:265) — that's relational-but-not-
  human and no-single-figure, already operating.
- **AI is never the headline.** Zero "AI-powered" labels anywhere. The only
  participant-facing AI self-description is *reactive* — surfaced when a
  participant asks "Are you an AI?" (facilitator_prompts.py:264) — which is exactly
  the kit's rule: experience first, disclosure inside, never the banner.
- **No engagement mechanics, no urgency, no promised answers** anywhere in the
  product surface. The Facilitator's closing prompt ("the last word is always a
  comma, not a period") is doorway-not-home embodied.
- **Onboarding line 38 is nearly the model sentence:** "…talk with a
  Representative — a voice built from the historical record" is the *anchored*
  voice form the kit requires (same as the 5-minute speech). Only its "The" is
  wrong.
- **The current visual identity is accidentally close to the approved direction.**
  The app's one committed system (`cic-poc/frontend/src/styles/table.css`) is a
  warm parchment ground (#f9f7f4), warm near-black text, an amber/burnt-orange
  Representative family, and Georgia serif over a system sans — which is most of
  the way to the manuscript-pigment direction (parchment · iron-gall ink ·
  gold-leaf/madder warmth) and the humanist serif + sans pairing. The Graphics
  thread's job is convergence and refinement, not replacement. All theming runs
  through ~20 CSS variables in one file, so the palette swap is centralized.

## 2. Conflicts — Priority 1: participant-visible today

| # | Where | Current | Change to | Rule |
|---|---|---|---|---|
| 1 | `cic-poc/frontend/src/components/OnboardingScreen.tsx:38` | "**The** Church in Conversation lets you talk with a Representative…" | drop "The" | Naming decision |
| 2 | `Ministry/Technology/World-Orientation-Map/CiC_World_Map_Interactive_Demo.html:170` | `<h1>The Church in Conversation</h1>` | drop "The" | Naming decision |
| 3 | `OnboardingScreen.tsx:41` | "You're talking to a voice shaped by the whole documented life of that community" | "a **representative** voice shaped by…" | anchored voice ("it's not a ghost") |
| 4 | `OnboardingScreen.tsx:68` | "It will tell you **honestly** what its world held to be true" | "It will tell you **plainly**…" | honesty-word retirement |
| 5 | `OnboardingScreen.tsx:82` | heading "The one **honest** distinction that matters most" | "The one distinction that matters most" | same |
| 6 | `OnboardingScreen.tsx:97–98` | "whether it felt **honestly** itself — a **real voice** with real edges" | "whether it felt **genuinely** itself — a voice with **real edges**" | same + "real" flatness |
| 7 | `TheTable.tsx:197` | "conversation with **voices** from Christian history" | "…with **representative voices** from Christian history" | anchored voice |
| 8 | `main.py:64` (API metadata, low stakes) | same phrase | same fix | consistency |
| 9 | World-Map demo `:259/262/263, :486/497` | "this lane's own **living voice**"; "Deep Interview — one **voice**…" | "living **representative** voice" / "one **Representative**, room to go deep" | anchored voice |
| 10 | World-Map demo `:173/176/199/214` | "…real history, **honestly** labeled"; "Legend, **honesty** marks…" | see Decision D2 below — the caption system needs one considered rework, not word-swaps | honesty-word retirement |

**Cleared, deliberately (do not "fix"):** `OnboardingScreen.tsx:88` — "that
community has its own voice, and it isn't this one" — that "voice" belongs to the
*living tradition*, which is precisely correct usage. The onboarding consent button
("I understand — let's begin") also stays: it's consent, not invitation; the
approved CTA governs invitations (see D5).

## 3. Conflicts — Priority 2: documents and titles (not participant-visible today)

- **Doc titles carrying "The"** (drop it at next touch): `cic-poc/README.md:3` ·
  `CiC_Full_System_Feature_Analysis_V0_1.md:1` ·
  `CiC_Guided_Questions_Curriculum_V1_0.md:1` ·
  `CiC_Guided_Questions_Design_Study_V0_1.md:1` ·
  `CiC_Guided_Questions_Sets_V0_1.md:1`.
- **The three .docx** the 2026-07-07 correction was applied to (Engineering Spec
  V1.0–V1.2, Experience Vision, Vision & Phased Plan) still carry "The" per the
  front-end log — the front-end thread reverts them at next revision (handoff
  already issued; also check `CiC_FrontEnd_Design_Brief_V1_0.docx`).
- **Decision-log history is NOT edited.** The log entries recording the old "The"
  decision (`CiC_FrontEnd_Decision_Log.md:823–833` etc.) are dated records; the
  reversal is itself logged. Rewriting history would violate the project's own
  log discipline.
- **"users" in design prose** (~14 spots across the FrontEnd Decision Log, Guided
  Questions docs, Feature Analysis — some quoting external research): fix at next
  touch, not as a dedicated pass; the lexicon rule is "participants."
- **Series title standing alone** (`CiC_FrontEnd_Decision_Log.md:831`): the log
  record stays, but wherever "Conversations with the Early Church" surfaces to
  participants (world catalog, curricula), the pairing rule applies — never
  without "Church in Conversation" (see D4).
- **"chatbot" ×3** (Guided Questions docs): all contrastive ("distinguishes this
  from a chatbot") — acceptable; the lexicon bans calling the product one, not
  naming the category it exits.
- **`CiC_Guided_Questions_Curriculum_V1_0.json`** likely holds participant-visible
  display strings — needs a display-string pass (not machine-read in this
  inventory).

## 4. Decisions that are genuinely Mark's (the review's real payload)

**D1 — How far does the honesty-word retirement reach into the product?**
The Facilitator uses "honest/honestly" as its signature tone word across nearly
every prompt (~10+ instances), including the acute-distress turns ("say something
honest," "warm, honest, brief"). *Recommendation:* the retirement governs **written
brand surfaces** (onboarding, headings, captions, demo labels, tour copy) — but the
Facilitator's *conversational, spoken* uses are natural human speech, not brand
catch-all, and should stay. A crisis turn that says "let me be honest with you" is
warmth, not fog. Draw the line at: repeated *devices* are brand surfaces;
*sentences a person would say* are speech.

**D2 — The Chloe Tour's caption system.** "A REAL PLACE, HONESTLY LABELED" (×12+)
is the tour's core rhetorical device — and it's doing real work (it implements the
imagery-governance rule). *Recommendation:* rework once, concretely, rather than
word-swapping: captions state *what the thing is* — "A REAL PLACE — PERIOD
PHOTOGRAPH" / "A LABELED RECONSTRUCTION" — which is more informative than
"honestly labeled" and is the transparency pole shown, not claimed. "The tour ends
here — honestly" → "The tour ends where the sources end."

**D3 — "Choose a Tradition" (WorldSelector.tsx:119).** The lexicon says a *world*
is what you visit; "tradition" is a third noun doing neither job.
*Recommendation:* "Choose a World" (the cards beneath already describe the
movements). Mark's call — "tradition" has warmth, but three nouns for one thing is
how vocabularies fog.

**D4 — Series-title pairing in product.** When the world catalog/curriculum
surfaces "Conversations with the Early Church," the lockup rule applies
(masterbrand present). The Kit's §3 lockup pattern governs; Graphics executes.

**D5 — Where does "Come and join us at the Table" live in-product?**
*Recommendation:* it's the *invitation* CTA — it belongs to the landing page, the
interest list, and any future world-catalog entry point ("Choose for Table" flow).
In-app functional buttons (consent, send, end) stay functional. The demo's "Your
table is set" (World-Map `:511`) is already in the family and can stay.

**D6 — Capital-R "Representative" in Facilitator prompts.** The UI capitalizes;
the prompts don't. Low stakes, one pass, worth doing for the same reason the
Constitution capitalizes it: it's a defined role, not a generic noun.

## 5. Visual identity — state of the handoff

- The Graphics thread is on record waiting for exactly this
  (`CiC_FrontEnd_Graphics_Thread_Launch_2026-07-17.md:64–68`: palette and
  typography "should come from the Messaging & Branding Kit thread… one visual
  identity, not two"). **The approved direction now exists** (manuscript-pigment
  palette; humanist serif + humanist sans; masterbrand/series lockup; imagery
  governance) — Kit Part 3.
- **Current state:** one committed system (app `table.css` — parchment ground,
  amber Representative family, blue participant, violet lexicon, gray Facilitator,
  Georgia + system-ui) plus **two independent demo palettes** (World-Map's
  dark-chart + gold; Chloe tour's own). Three systems → one, per the Graphics
  thread's own stated concern.
- **Continuity worth preserving in convergence:** the role-color language (a
  distinct hue per speaker role) is genuinely good information design and maps
  naturally onto the pigment palette (amber→gold-leaf/madder for Representatives,
  violet→lapis for lexicon, parchment ground, iron-gall text). Recommend the
  Graphics thread treat the app's current system as the seed, not a casualty.

## 6. Count summary (from the full inventory)

"The Church in Conversation": 12 instances in scope (2 participant-visible) + 3–4
docx flagged by reference · bare "voice": ~12 across app, prompts, demos (1
cleared as correct living-tradition usage) · "honest/honestly" catch-all: the
largest surface — ~3 app, ~10+ Facilitator prompts (see D1), ~18+ across the two
demos (see D2) · "users": 0 in product, ~14 in design prose · "come sit": 0 in
scope · approved CTA: 0 in scope (see D5) · "AI" as headline: 0 · flagship
"documented Christian movements": 0 in scope — not yet propagated (landing/FAQ
carry it; the app's "whole documented life of that community" is directionally
aligned).

---

**Who does what:** P1 app/demo fixes and D6 → front-end workstream (small,
surgical). P2 titles → next-touch rule. D1–D5 → Mark. Palette/type execution →
Front-End Graphics, with Kit Part 3 and §5 above. This review is input; the
front-end thread owns the changes and logs them in its own decision log.

---

## Mark's decisions and same-day execution (2026-07-17)

- **D1 — DECIDED, further than the recommendation:** "i dont want honest as a brand
  or signiture tone, its not a facilitator word, is ok once in a while but it
  undermines the conversation." Applied: all ~15 honest-as-tone-word instances in
  the Facilitator prompts replaced (plain/clean/real/clearly, varied to avoid
  minting a new catch-all); the rule written into the prompts module's THRESHOLD
  VOICE register so future prompt authors inherit it.
- **D2 — DECIDED** ("same with D2 what is honestly adding"): the concrete-caption
  rework is approved. **Queued as the next chunk** — the World-Map (~6 instances)
  and Chloe Tour (~12+) caption sweeps ("A REAL PLACE — PERIOD PHOTOGRAPH" / "A
  LABELED RECONSTRUCTION" pattern).
- **D3 — recommendation WITHDRAWN; vocabulary question opened:** Mark: "i through
  we were moving to christian tradition as the outward facing term, and world is an
  inward definition." "Choose a Tradition" therefore STAYS. The
  tradition/movement/world architecture is an open Brand Foundations question put
  back to Mark (see the branding thread).
- **D5 — DECIDED (yes):** the "Come and join us at the Table" CTA belongs to
  landing/catalog entry points; in-app functional buttons stay functional.
- **D6 — DECIDED (yes) and applied:** capital-R "Representative" in all
  participant-facing Facilitator prompt text (handoff, multi-handoff, bridge,
  frame-breaker); internal monitoring prose left for the front-end thread's
  next-touch pass.
- **NEW — Facilitator speaks "I," first person singular (Mark):** "the facilitator
  should not be speaking in we, they are an I and should speak in first person
  singular, they are not representing anyone." Applied to the prompts module
  docstring, the reception prompt, and the frame-breaker (which now states the
  contrast explicitly: Representatives = "we" because they represent movements;
  the Facilitator = "I" because it represents no one).
- **P1 fixes executed and browser-verified:** onboarding (no "The"; "representative
  voice"; "plainly"; de-honested heading; "genuinely itself — a voice with real
  edges"), Table header ("representative voices"), API description, World-Map demo
  H1. Backend files compile; onboarding and Table verified live in the preview.
- **Sync flag:** the onboarding copy's source document
  (`Ministry/Operations/CiC_Prototype_Testing_Pilot_Plan_DRAFT_V0_1.md`, Section 3)
  now lags the component — needs the same revisions (noted in the component's
  provenance comment).

*Compiled 2026-07-17 from a full read of the cic-poc frontend components, backend
Facilitator prompts, Ministry/Technology markdown documents, and all three HTML
demos. The .docx documents and the Guided Questions .json were flagged by
reference, not read.*
