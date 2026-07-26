# Launch prompt — Fable Pass 2 blueprint thread

Paste this into a fresh Fable thread to kick off Pass 2 — the build blueprint. This is the second of your two weekly Fable passes; Pass 1 (the design itself) already spent the first one.

---

**Prompt to paste:**

> You have repo access to `https://github.com/mchadwick25-droid/CIC-Project.git`, branch `main`. Read `Ministry/Technology/CiC_System_Redesign_Pass1_Design_2026-07-26.md` in full — that is the finished Pass 1 design. It has been through two rounds of adversarial review, and every finding from both was applied directly to it (the reviews themselves are `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/20_...md` and `21_...md` — worth reading for the discipline this project holds itself to, not because anything in them is still open).
>
> This is **Pass 2**, defined in the brief's own §10 (`Ministry/Technology/CiC_System_Redesign_Fable_Brief_2026-07-25.md`): turn the finished Pass 1 design into an ordered, step-by-step build blueprint a Sonnet-driven process can execute one session at a time — with a real verification checkpoint at each step, not a self-report. That checkpoint problem is explicitly the hard part, stated in the brief itself: incremental session-by-session building is exactly the process shape that produced the fan-out/drift failure the whole redesign exists to fix, so your sequencing has to actively defend against reproducing that failure, not just list steps in order.
>
> **Pass 2 does not redesign anything.** Treat every design decision in the Pass 1 document as a settled input. If something in it looks wrong, incomplete, or hard to sequence while you're working, say so explicitly rather than silently building around it or changing it — that's a decision for Mark, not something to resolve inside the blueprint.
>
> Ground the blueprint in what Pass 1 already specifies, don't invent a parallel structure: sequence around the schema (§3), the machine gates and Table Readiness Round (§4), and use §11's world-build completion standard as the actual freeze criteria each build step checks against. §10's measurement plan — thresholds deferred to real baselines, never invented — is the standard your own checkpoints should be held to as well.
>
> Before treating any claim as settled, verify it against its cited source, the same discipline both prior reviews used and that this project documents at `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`.
