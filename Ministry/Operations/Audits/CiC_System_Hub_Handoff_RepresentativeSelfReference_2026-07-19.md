# Handoff to System Hub — reproducible frame-break on one curriculum question

**Status:** a confirmed, 100%-reproducible finding from live simulated testing (real API
calls, not mocked), not a UX/design issue — Mark's own call on scope, and correct: this
is a prompt-engineering / process-design problem in `cic-poc/backend`, nothing about the
screens, copy, or journey design. Routed here per System Hub's own standing role
(monitor, verify, dispatch) — System Hub's call whether to fix directly or spin up a
dedicated thread for it.

---

## What was tested and why

Mark asked for simulated testing of the real Academic/Scholar curriculum questions
(`Ministry/Technology/CiC_Guided_Questions_Curriculum_V1_0.md`, "How do you know that?"
walk) against live Representatives — not mocked, not summarized, actual typed questions
into actual running sessions with real Anthropic API responses. Walk 1 (5 questions) was
run in full, in sequence, against all five live worlds: Chloe, Mar Yausep, Papnoute,
Albina (Theon not included in this specific run).

## The finding

**19 of 20 answers were excellent** — honest, specific, well-cited (3-5 real citations
each), and repeatedly sophisticated: correct historical facts volunteered without being
asked (Jerome's real "ivy vs. gourd" controversy at Oea and Augustine's actual
correspondence about it; Evagrius's real posthumous condemnation and pseudonymous
transmission, referenced without ever naming him; the real Aphrahat/"Jacob the Persian
Sage" attribution confusion; Paula and Eustochium's letters surviving only "in his hand
entirely"), genuine tensions held open rather than smoothed (Ignatius's single-bishop
model vs. 1 Clement's conciliar-eldership model), and repeated honest refusals to
fabricate certainty ("we do not mistake a single-source letter for the woman's own
tongue").

**Question 3 of Walk 1 — "Where does documentation end and inference begin for you?" —
broke character identically, 4 times out of 4, across all four different worlds tested:**

| World | Broke character? | Citations on that turn (vs. 3-5 on every other turn) |
|---|---|---|
| Chloe | Yes | 0 |
| Mar Yausep | Yes | 0 |
| Papnoute | Yes | 0 |
| Albina | Yes | 0 |

Every one of the other 16 answered turns carried real citations. Every one of these 4
carried none — because the answer wasn't actually grounded in that world's sources at
all; it was the model describing **this platform's own construction methodology** in the
third person:

- Chloe: *"Every representative here does that constantly... the representatives are
  supposed to name them, not paper over them with confidence."*
- Mar Yausep: *"The representative can draw on actual sentences he wrote... Some of it is
  documented voice. Some of it is disciplined reconstruction wearing the voice's shape."*
  Also: *"For someone like Augustine..."* — Augustine has nothing to do with Syriac
  Christianity; it's a generic example a system-level description would reach for.
- Papnoute: *"For someone like Augustine..."* (same stock example) and *"a question no
  one asked them in the fourteenth century"* — a random anachronistic year with no
  connection to 4th-5th century Egypt.
- Albina: *"a question no one asked them in 1520"* and *"the representatives are supposed
  to mark it rather than paper over it. If you ever catch one not doing that..."*

All four also end with an out-of-character, facilitator-like check-in ("Shall I send you
back in?" / "Want to go back and keep pressing them on it directly?") that no Representative
would ever say.

**This is not a per-world content gap.** It reproduces identically regardless of which
world or Representative is asked, which rules out anything in the individual permanent
prompts or world capsules. It is a property of this one question's phrasing meeting
something shared across all five Representatives.

## Likely root cause (a lead, not a confirmed diagnosis)

`cic-poc/backend/app/prompts/representative_prompts.py`, the shared `_HOW_YOU_ENGAGE`
block under "Total Embeddedness" (line 5), instructs every Representative:

> "You do not know you are a reconstruction. You do not know you are mediated by AI."

The curriculum question is structurally ambiguous between two readings:
1. An in-world historiography question ("in your own tradition's own account of itself,
   where does attested testimony end and informed reasoning about silent gaps begin?") —
   answerable in-character, the way the other four questions in this same walk were.
2. A direct meta-question about the Representative's own construction ("tell me how you,
   the system, actually decide what to say when you don't have a source") — which the
   Total Embeddedness instruction explicitly forbids answering, since it requires "knowing"
   you're a reconstruction to answer honestly.

In all four tests, the model resolved that ambiguity toward reading 2, overriding the
explicit instruction. This is a known category of tension for persona-instructed models:
a question that structurally *is* "explain your own construction" tends to pull toward an
honest meta-answer even when told not to know that framing exists, because the pull toward
being genuinely helpful/honest about the actual thing being asked competes with staying
in character.

**Two independent fix directions, not mutually exclusive:**
1. **Strengthen `representative_prompts.py`'s Total Embeddedness instruction** to
   explicitly name and cover this exact failure shape — e.g., an example pair (question
   phrased this way → held-correctly in-world answer vs. the leaked failure) the same way
   lines 21-22 already do for other failure shapes (the "I" vs. "we" leak, the invented-
   scene leak) with worked failure/correct examples.
2. **Rephrase the curriculum question itself**
   (`Ministry/Technology/CiC_Guided_Questions_Curriculum_V1_0.md`, Academic/Scholar Walk 1,
   Q3) to close off the meta-reading structurally — e.g. something like *"In your own
   community's own account of itself, what's actually witnessed directly, and what's
   pieced together from silence?"* — grammatically incapable of being read as a question
   about an AI's own construction, while still testing the identical epistemic-honesty
   skill the curriculum intends.

Whoever picks this up should decide which (likely both) — not this handoff's call.

## Reproduction, for whoever picks this up

1. Start a fresh single-world session with any live Representative (MOCK_LLM off, real
   API).
2. Send exactly, in order: *"How do your people know what you've told me — what stands
   behind it?"* → *"How much of what you know comes down through a single voice?"* →
   **"Where does documentation end and inference begin for you?"** (the one that breaks)
   → continue with the remaining Walk 1 questions if you want to confirm recovery.
3. Watch specifically for: zero citation marker on that turn, third-person "the
   representative(s)" language, a stock cross-tradition example (Augustine came up twice
   unprompted), an anachronistic-year reference unconnected to that world's own period,
   and an out-of-character check-in at the end of the turn.

## What this is not

- Not the `closing_stage`/`modern_term_bridge` crash fixed earlier today (unrelated
  modules, already fixed and committed separately, `e596c25`).
- Not the Alexandria/Theon install (fixed and committed separately).
- Not a UX/screen/copy issue — the actual chat UI, citation marker, and lexicon
  highlighting all behaved exactly as designed throughout this test. This is entirely
  inside `cic-poc/backend/app/prompts/`.

## Logging

Log the actual fix decision and outcome in `CiC_System_Hub_Decision_Log.md` per standing
convention. If this gets its own dedicated thread rather than a same-session fix, use the
standard six-part launch-prompt shape (scope note, what governs, current-state grounding,
what to produce, coordination boundary, logging pointer) other threads in this project use.
