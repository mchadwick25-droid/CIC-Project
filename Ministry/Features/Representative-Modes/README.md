# Representative Modes ("4-role setup")

**What this is:** the feature letting a participant pick a role/mode (RM-1..RM-15 in
this project's task tracking) before entering a conversation, so the Representative's
engagement style matches why they came. Built on the four-role framework already
established in Facilitator Governance V3.6 §§4/9 — this feature implements that
framework, doesn't invent a new one.

**This was the second-worst-scattered feature found in the 2026-07-20 filing audit**
— 6 locations before this migration, and the code has never actually reached `main`.
See `Integration-Notes.md` for exact branch/commit state.

**Current state:** design and prompt architecture complete, self-consistent, verified
in mock-LLM mode only — **never validated against a live model.** "Battery A" (live
validation) is the single highest-cost, highest-scope open item blocking everything
downstream of this feature (Guided Questions' UI depends on role selection landing
first).

**Where deliverables land once integrated:** `cic-poc/backend/` (new
`prompts/role_modes.py`) and `cic-poc/frontend/` (new `RoleSelector.tsx`).
