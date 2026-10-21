# Handoff — conversation pages build — 2026-10-21

From session: https://claude.ai/code/session_01RnnjAQrYFWSzjZiPnWuYke · Workstream: pilot feedback item 29 · Branch / PR: claude/magical-goodall-ucv6e2, PR to main (linked in the PR list)

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| The one-voice page and the Table room rebuilt: slim bar with a ⋯ menu, token ribbon with a gold line, one card (or three), one conversation area, the box under it | `cd cic-poc/frontend && npx vitest run` (285 tests pass), `npx tsc --noEmit -p .` (clean), and the real app run in headless Chromium with a mocked API at 390 px and 1100 px |
| Replies roll out word by word in order; each Table voice's card lifts only while it speaks; no card lifts while the table waits; all rest at the end; the box stays shut until the last voice finishes | Unit tests (`useReveal.test.tsx`, `TableRoom.test.tsx`) and a streamed three-voice round in Chromium |
| Smooth growth and scroll: new blocks open from nothing; the page follows the newest line; gold bar for a mouse or trackpad; finger scroll on touch; "Latest ↓" | Frame-by-frame measure in Chromium: largest height change per frame 29 px (one wrapped line), scroll step 4 px or less, ends at the bottom. Wheel, bar drag, finger drag and Latest each moved the page |
| Decisions and change orders written down | `Build/Ministry/Operations/Pilot-Feedback/Pilot_Feedback_Decisions.md` "Item 29"; `Build/Ministry/Features/Go-Deeper/Decision-Log.md` 2026-10-21 |

## 2. Not done

- Not tested on a real phone, a tablet, a screen reader, or against the live engine's streaming. The mock fulfils a streamed reply in one piece, so only the pacing and ordering are checked, not real network timing.
- Not promoted to live. Promotion is Mark's call through `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`.
- "Go deeper" as depth in the conversation or world is not built; only the token panel was renamed.
- The About panel and the panel inside "Get more conversations" were not shown to Mark as sketches.

## 3. Re-check before you trust it

- Whether any law or platform rule needs an AI disclosure inside the conversation. I did not check. The in-room disclosure is removed on Mark's word (see change order 1 in the decisions doc).
- The card band's era comes from the world's time window, not the census era the landing page uses. Check a world whose window opens before its census era.
- Replies swap from plain text to the full marked-up text (✲ marks, general references) when they finish rolling out. A reply with many marks may reflow by a line at that moment. Not seen in the mock, which has no marks.
- Reduced-motion: replies show whole at once. Only tested in unit tests.

## 4. Waiting on Mark

- The gold line's scale: the most tokens this browser has seen (built), the 550 free window, or the last top-up. Shown in the sketches only as an example length.
- Keep the per-reply "This helped" and "Answer was not clear or accurate" links? They were not in the sketches and they open a block under each reply. Kept as they were.
- Keep or drop the suggested-question chips (dropped) and the page-level "This helped" like (dropped).
- Show "Latest ↓" on touch screens (shown).
- Promote to live, once he has seen it on staging.

## 5. Next step

Open the staging deploy, ask a one-voice question and a Table question on a phone and a laptop, and tell Mark what you see before he decides on promotion.

## 6. Spend

Allowance share used: one long session on Sonnet. Metered: none (no model calls outside conversations; the engine was not called).
