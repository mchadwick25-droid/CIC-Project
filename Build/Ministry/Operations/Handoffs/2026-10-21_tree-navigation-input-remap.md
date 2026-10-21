# Handoff — Church Family Tree navigation: input remap (option A) — 2026-10-21

From session: https://claude.ai/code/session_016TfsmpqN3i7uRXDPKQLpTz · World or workstream: Atlas / Church Family Tree front end · Branch / PR: `claude/pensive-cori-culrhf`, no PR

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Read how the Tree handles input. Findings: the stage is full screen with `touch-action:none`, so the page never scrolls; the wheel zooms (`stage.addEventListener('wheel'` near line 41767 of `cic-website/atlas-v3.html`); mouse and one-finger drag pan; two-finger pinch zooms; marker click or tap opens a panel; markers take Enter and Space. | Read the code. Nothing was run in a browser. |
| Found the only visible control is "Reset view" (`#resetBtn`, line 385). Code for pan arrow buttons (`panUp` and the rest, near line 41826) has no matching markup. No zoom buttons, no keyboard pan or zoom. | `grep` on the page for the button ids and key handlers. |
| Drafted the input plan as an Artifact: https://claude.ai/artifact/2KtmME9nUyQp6DasRbw3rj. It holds the per-device table and three build options (A remap, B scrolling page, C phone feed). | Artifact `read`. |

## 2. Not done

- No code changed. No decision logged.
- Option B (a real scrolling landing page) and option C (phone era feed) are not approved. B is gated on the week 3 pilot gate, which has no numbers yet.

## 3. Re-check before you trust it

- The line numbers above, against the current `atlas-v3.html` (the file is about 3.8 MB; line numbers drift).
- Whether the Atlas decision log already rules on map input: `Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`.
- Which thread owns `atlas-v3.html` now. Mark's 2026-10-19 entry gives `cic-website/index.html` to the chooser thread; the map file was not covered.
- No device was tested. Real phones, a real trackpad and a screen reader were not tried.
- Trackpad pinch reaches the page as a wheel event with `ctrlKey` set. This is general browser behaviour and was not tested here.

## 4. Waiting on Mark

- Direction chosen: A now, B later. Shown in the Artifact, section "Three ways to build it". Mark said "lets launch a new thread to do this". He did not use the word "converged"; if the thread doubts it, confirm before editing.
- The week 3 gate numbers for deciding on B and on the churchfamilytree.com site. Not decided.

## 5. Next step

Check the two re-checks above. Then build option A on `atlas-v3.html`:

1. The wheel and trackpad swipe move the map. Ctrl or Cmd with the wheel zooms.
2. Add + and − buttons beside "Reset view".
3. Add keys: arrows, Page Up, Page Down, Home and End to move; + and − to zoom.
4. Reword the corner hint (`#zoomHint`, line 416). Show the pinch line only on touch screens.
5. Leave one-finger pan and two-finger pinch as they are.
6. Test in the preinstalled Chromium with simulated wheel, Ctrl-wheel and key events, then log the decision in the Atlas decision log.
7. Tell Mark what could not be tested on real devices, and give him the steps to try them.

## 6. Spend

Allowance share used: not measured. Metered: none.
