# CiC Task Board — Acceleration Jul–Dec 2026

**How this works:** This board is the day-to-day view of
`Ministry/Operations/CiC_Acceleration_Gantt_2026.gan` (open that in GanttProject —
free, ganttproject.biz). Task IDs match the Gantt file. **DO NOW** = every
predecessor is done (or it never had one) — you can work on these today, in priority
order. When something finishes: move it to DONE here, set it complete in
GanttProject, and promote anything it unblocks. When something new arrives: add it to
both files with a new ID and its dependencies. Ask Claude to resync both files any
time — say what's done and what's new.

**Funding gates (fixed):** $7.5K by Sept 1 · ~$25K by Nov 1 · $35–45K by Dec 31.
**Hard calendar gates:** reviewers engaged Sept 1 · entity filed ~Sept 15 · CCSA ~Nov 15 · Lane B go/no-go Dec 15.

_Last synced: 2026-07-19, later still (⚠ CORRECTION: this board previously carried
"re-engage Bedrock" as the live infra item — stale. `CiC_System_Hub_Decision_Log.md`
(2026-07-19) records **Bedrock dropped entirely; direct Anthropic API hosting decided**,
alongside the website's own infra. System Hub has already built the pilot-invitation
website pages (`cic-website/pilot.html`, `pilot-thank-you.html`) and the per-tester
session-cap code (`cic-poc/backend/app/session_cap.py`) — see the corrected DO NOW entry
below, moved out of DELAYED since it's active now, not paused. ⚠ SCOPE DECISION: Mark also
says P1 launches with the full feature set, not the minimum-viable path — see
`CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` V1.2. Battery A (RM-8) is now the single
most schedule-critical action in the plan; #102 Run Prototype 1's dependency set expanded
accordingly — see READY NEXT.) Earlier 2026-07-19: UX design CLOSED OUT — the two
remaining graphics DRAFTs decided (reading surface = warm cream; Era-2 ground = no
variation, seating/object only); §G/§R approved; two Living-Table layout bugs found and
fixed (desktop + phone scene-lock); a content-integrity issue found and fixed (invented
Representative dialogue stripped from all mockups); a first-page greeting/CTA screen
(with per-world briefs) added to the Living Table mockups on both desktop and phone;
Alexandria/Theon installed as the fifth live world. Prior: 2026-07-18 late, Complete
Experience Storyboard shipped (SB-1..4); icon set 5/5 locked + era palette approved
(IC-1..8).) Later still (2026-07-19, System Hub thread restarted): this file,
`CiC_Dashboard.html`, `CiC_Gantt_Visual.html`/`.gan`, and `CiC_System_Hub_Decision_Log.md`
had gone missing from disk (an untracked-file loss during today's earlier merge to
`main`) — recovered intact, zero content lost, from an orphan git safety-snapshot commit
(`09f1de5`, see the decision log's 2026-07-19 recovery entry for how). Delta added since
that snapshot: the accounts/sign-in layer (`cic-poc/backend/app/auth.py`, a Supabase-backed
rework of `session_cap.py`/`transcript_logging.py`, `SignInScreen.tsx`) is built and
smoke-tested, uncommitted — new DO NOW item above.) Later still (2026-07-19, systematic
L1-L5 audit): a 10-agent audit found real cross-document drift (full findings in
`CiC_L1-L5_Systematic_Audit_2026-07-19.md`) — one item flagged as urgent (House-Church's
crisis/distress handoff mechanism) was **checked directly in code and confirmed already
built, wired into both message endpoints** — removed from DO NOW, was a documentation-lag
false alarm, not an open safety gap. Remaining audit follow-through (registry reconciliation,
prompt-drift decision, citation fixes, lexicon compliance script) handed to a new disciplined
successor thread — `CiC_System_Hub_Thread_Launch_V2_2026-07-19.md`.)_ **⚠ CORRECTION
2026-07-21: this note's own "live-tested 2026-07-13" claim was wrong** — the actual
2026-07-13 implementation notes disclose the opposite (no live testing run). Code/architecture
confirmed real and platform-wide; live-adversarial-testing status corrected to NOT DONE — see
the 2026-07-21 Decision Log entry and the new DO NOW item below. Same entry also: **Path B
(full feature set) reconfirmed**, **Article 31 external review reworded to aspirational, no
longer a go-live dependency** (financial reality, per Mark — see #301 below), and **Albina's
Bethlehem Circle drift traced and confirmed closed** (already marked DONE 2026-07-19 below;
this just adds the exact git-history explanation)._ **Later, 2026-07-22 (In-App Icons &
Graphics thread):** Marius/Church and Empire's icon LOCKED and IC-9 re-run across all six
(IC-13); the Living Table scene redesigned live with Mark and its first real slice built
into `cic-poc` — `LivingTableScene.tsx`, `worldIcons.tsx`, `table.css` (LT-1); a real
world-selector tile-ordering bug found and fixed (LT-2). Full reasoning:
`Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`. **Still open:** a live visual
check of the real Living Table build in a running conversation — see LT-1.

---

## 🔴 DO NOW (all dependencies clear — priority order)

- [ ] **SH-1..SH-12 — Mark's full to-do list, logged 2026-07-30 (25 min before the Fable
      reset), sequenced Fable-track vs Sonnet/System-Hub-track.** One step at a time from
      here; this entry is the queue, not a commitment to parallel everything.

      **Fable-track (needs Fable's weekly budget):**
      - **SH-1 — Brief Fable on tonight's VG-1a/1b/1c fixes before Step 3 starts**, so the
        new world (Hieronymian/PAHC/Imperial-Juridical) builds clean against the corrected
        parser/gate/schema instead of needing a VG-2-style retrofit after. Briefing sent
        this session, ahead of the reset — see System Hub Decision Log.
      - **SH-2 — Rebuild the 3 remaining worlds** (Step 3 proper) once SH-1 lands. ~30-35%
        of a weekly budget per Mark's own earlier estimate.

      **Sonnet/System-Hub-track (no Fable budget needed):**
      - **SH-3 — Go live on the current pilot site**, run real tests to verify both cost
        (against tonight's cost-investigation baselines, `Ministry/Technology/Pass2/`,
        `Pass3/`) and quality. Blocked on the live/pre-launch status question already open
        with Mark (see auth-fix thread, System Hub Decision Log).
      - **CORRECTED 2026-07-30 (later):** SH-4/SH-5/SH-6 below were first logged as if new
        — they're not. All three continue the existing **World Orientation & Selection
        Map thread** (`Ministry/Features/Atlas-World-Map/`), which already has a full
        V0.1 spec, a 178-entry census, three built redesign prototypes (A/B/C), a
        Usability Redesign Study, and its own `CiC_World_Atlas_PreStep0_Survey_V0_1.md`
        — near enough to SH-5's ask that it's very likely the same document, not a new
        one to write. That thread's own Decision Log ends on **five open questions
        blocking V0.2**, explicitly gated ("No construction, no code, no census expansion
        until the open questions above are answered"): the census review (what's
        missing), Lane 4's grouping/label, whether floor-excluded movements show
        dimmed-with-copy at V1 or wait, whether "Notify me when this changes" is real or
        an over-promise, and whether the map ships standalone before front-end
        integration. **SH-4/5/6 aren't build tasks yet — they're blocked on Mark
        answering those five, same as the thread already said.** Corrects the two
        entries below rather than replacing them, so the original log stays visible.
      - **SH-4/SH-6 — Rebuild the vertically-scrolling map to v3 spec.** Mark named this
        twice in the same list (items 4 and 6) — flagged, not silently merged: item 4 says
        "fully rebuild... may have more design work to complete v3," item 6 says "rebuild...
        to the v3 specifications with further input... last two versions were still messy."
        Read as one task with two notes attached (more design work may be needed; the core
        complaint is visual clarity/engagement, not features) unless Mark says otherwise.
        **Superseded by the correction above** — this is the World-Map thread's own V0.2,
        not a fresh build.
      - **SH-5 — Pre-Step-0 update: full Christian Movement analysis, 10-era Atlas.**
        Recognizes the worlds already built, free to go deeper on the rest; per-era small
        box (title + dates), hover for short description, click for full description +
        key influencers + sources + cross-tradition connections. Real scope — likely its
        own design pass before build. **Superseded by the correction above** — check
        `CiC_World_Atlas_PreStep0_Survey_V0_1.md` against this ask before writing anything
        new; it may already exist.
      - **SH-7 — Identify the ~150 most probable interview questions.** Multi-step process,
        not yet designed — needs its own scoping conversation before work starts.
      - **SH-8 — Org/finance: bank account finalized (1st deposit through, 2nd pending),
        then the Letter to Shareholders.** Tracking only — Mark's own process, not a build
        task for either Fable or Sonnet.
      - **SH-9 — Set up Stripe for contributions**: wording, strategy, and logistics.
        Connects to tonight's contribution/tier economics work
        (`Ministry/Features/Funding-Strategy/`) — should ground its wording/asks in the
        real market research already done there (the "keep it open" $10/$8 figures, the
        PBC no-tax-deduction framing). **BUILT 2026-07-31** — code and copy done, real
        Stripe account/webhook setup still Mark's own step; the 2026-07-22 funding hold
        this depended on was explicitly lifted by Mark first. Full account:
        `Ministry/Features/Funding-Strategy/CiC_Stripe_Setup_Wording_Strategy_Logistics_V0_1.md`.
      - **SH-10 — Keep testing real costs once real questions get asked.** Standing,
        ongoing — not a one-time task. Feeds the B-COST re-baseline already blocked open
        (see Pass2/Pass3 baselines).
      - **SH-11 — Design a system that pulls prepared answers seamlessly into interview
        mode.** This is the precomputed answer-bank lever from tonight's cost investigation
        — real, but sized at ~5% of cost (not the 30-50% first assumed), see
        `Ministry/Technology/Pass3/cost_floor_model.py` (restored to `main` 2026-07-31 -
        it existed only on an orphaned branch until now). **BUILT 2026-07-31** — the
        mechanism (storage, lookup, live-shaped serving, hit/miss logging), fully verified
        offline (`scripts/answer_bank_check.py`, 14/14), zero real content. Full account:
        `Ministry/Features/Guided-Questions/CiC_Answer_Bank_SH11_V0_1.md`. **Not live**:
        needs a real content-generation run (live API key) plus human review before any
        bank file is trusted, and the curriculum-picker UI is explicitly the front-end
        thread's job, not built here. Worth doing for the quality/
        consistency win on curriculum-path traffic; go in with the real cost expectation,
        not the inflated one.
      - **SH-12 — Set up the tier system.** Direct build-out of tonight's tier/breakeven
        work (`Ministry/Features/Funding-Strategy/`) — free tier (2hr interview), $15/mo
        paid tier, blended contribution/patron/subscription mix. Real numbers already
        modeled; this is implementation. **Scope addition, Mark's decision 2026-07-31
        (Table-mode product shape):** Table-mode (up to 3 representatives) stays
        available to everyone through the pilot; at public launch it becomes a paid-tier
        feature — free tier is solo conversations only from that point on. This needs
        the same subscription-status infrastructure SH-12 already requires (Stripe
        subscription state reaching a real check at session-start), so it belongs in
        this build, not a separate ad-hoc gate. Not yet built — SH-12 itself hasn't
        started. **DEFERRED, Mark's decision 2026-07-31:** wait until piloting is far
        enough along to know real costs from real traffic and to keep the pilot
        experience simple — don't build the paywall before there's a real number to
        build it around. Revisit once real B-COST/pilot data exists.


- [x] **DONE 2026-08-01 — Table size permanently capped at 3 (down from the original
      5-world design ceiling), cost-driven.** Live cost proved too high at 5 (see SH-2's
      PAHC entry above — TRR partner-count compounds every world frozen). **App already
      enforced 3 functionally** (`WorldSelector.tsx` `MAX_WORLDS = 3`,
      `main.py` `world_ids[:3]`) — no code-behavior gap. Fixed the stale framing that
      called 3 a temporary "Phase 1" placeholder awaiting a raise to 5: both code
      comments and `wrs/parameters.yaml`'s `table_size_ceiling` entry (`design_value: 5`
      marked RETIRED, kept not deleted, per that file's own citation discipline).
      **Not touched, flagged instead:** the master design doc
      (`L3D-Encounter-Methodology/CiC_L3D_The_Table_Design_Document_V2.3.docx`, a
      binary `.docx`), and several other threads' own specs still describing a 5-world
      table (Front-End-Integration-Strategy, In-App-Icons-Graphics, Full-UX-Design, the
      original World-Build construction docs) — owned elsewhere, not edited here. A
      `CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md` already exists alongside the
      master doc — unchecked, worth Mark confirming whether it already covers this.
      Full account: Decision Log, 2026-08-01.
- [x] **DONE 2026-08-01 (later) — Table-size cap wider cleanup executed: master design
      doc + 8 other live specs corrected, 1 FLAGS.md entry filed, ~55 files checked and
      confirmed clean.** `CiC_L3D_The_Table_Design_Document_V2.3.docx` (the actual source
      everything else cited) fixed directly, including the "five worlds at any one Table"
      passage. `CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md` turned out not to be
      the reconciliation — it was the original Phase-1 framing doc, corrected the same
      way. `Syriac-Build/`'s copy confirmed a frozen clean-build sandbox (2026-07-20
      Filing System Audit), not a duplicate — left alone. FLAG-038 filed against Pass 1's
      now-stale audit finding, no in-place edit. Surgical fixes landed in Full-UX-Design
      (3 files), Brand-Assets' Table Template Spec (found by citation chase, not keyword
      grep), and all 4 current Front-End-Integration-Strategy specs (Design Brief,
      Engineering Spec V1.2, Experience Vision, Vision and Phased Plan) — the Drafts-Archive
      superseded versions and In-App-Icons-Graphics/World-Build construction docs checked
      and confirmed clean. Full account, every file and bucket: Decision Log, 2026-08-01
      (later).
- [x] **DONE 2026-07-21 — Live adversarial testing of the Acute-Distress/Harmful-Dynamic
      mechanism run: 19/20 clean, real API calls, all 5 worlds, both endpoints.** Closes
      the one real gap under the "crisis handoff" cluster. Covered: A1/A2/continuation on
      House-Church specifically, the historical-otherness-vs-real-crisis boundary (zero
      coverage before this — passed, including the hardest edge case), both Harmful
      Dynamic paths (zero coverage before this — both correct), a false-positive control
      (6 turns, zero false fires), the frame-breaker/relational-safety overlap (correct
      priority), a 3-world table (correct), and the non-streaming endpoint (correct). Full
      transcripts and scoring: `CiC_Live_Safety_Testing_Script_2026-07-21.docx` (repo
      root). Same bar Self-Narration/frame-breaking cleared (12/12 live) before being
      trusted — now cleared here too, with one exception below.
- [x] **DONE 2026-07-21 (later) — De-escalation follow-up run: real, reproducible, and
      safe-direction, not a bug that blocks launch.** Re-tested twice more with
      unambiguously neutral turns (no crisis language at all) — de-escalation
      consistently takes ~3–4 clean turns to clear, not the code's documented 2, but it
      does clear reliably and stays cleared once it does (no flickering back). Direction
      of the miss is the safe one: the system holds its cautious posture slightly longer
      than coded, not shorter. No participant-facing problem — the "still here"
      continuation turns read as attentive, not broken or alarming. **No urgent code
      change needed before launch.** Low-priority cleanup for later: either correct the
      `_DEESCALATION_TURNS_REQUIRED = 2` comment to match observed behavior, or (optional)
      tighten the classifier prompt for exact 2-turn precision if that specificity ever
      matters. Full account: Decision Log, 2026-07-21 (later still).
- [x] **⚠ INVESTIGATED 2026-07-20, LEADING CAUSE FOUND + GUARDED 2026-07-22 — Content-isolation
      defect in `cic-poc/backend`, real, root cause still not proven but a strong environmental
      explanation reproduced.** **2026-07-22 addition:** a separate finding the same day as the
      original incident (2026-07-20, mobile-popover thread) had already spotted a real
      shared-port hazard on this machine and flagged the connection but didn't chase it. Chased
      it now and reproduced it directly: uvicorn sets `SO_REUSEADDR` unconditionally
      (`venv/.../uvicorn/config.py:583`), and on Windows (unlike Linux) that flag lets a
      **second** process bind and LISTEN on an already-occupied port with zero error — its
      startup banner looks completely normal. Verified live on this machine: two test listeners
      both bound port 18453 successfully; **all 8 requests silently went to whichever process
      bound first**; killing that first process did NOT fail traffic over to the second, already-
      listening one — new connections just timed out. **This is not proof the 2026-07-20 incident
      was this exact mechanism** (the stale process's own identity is gone, unrecoverable), but
      it's a real, reproduced, silent failure mode on this exact machine that fits the symptom
      shape well: a fresh-looking server that is actually answering zero requests while something
      stale (possibly a leftover process from a completely different task) answers instead —
      which would explain why the leaked content read as content from an unrelated context rather
      than anything `cic-poc`'s own prompts would generate. **Guarded, not just diagnosed:**
      `cic-poc/backend/run_dev.cmd` now runs a pre-flight check
      (`check_port_free.ps1`) before starting uvicorn — if port 8000 is already listening, it
      prints which process owns it and aborts instead of silently binding alongside it. Verified
      both directions (blocks with a stale listener present; passes silently when the port is
      genuinely free). Does not touch production (Render/Fly.io containers don't have this
      hazard — one process per container). Full account: System Hub Decision Log, 2026-07-22.
      **Original 2026-07-20 investigation, preserved below:**
      A live API response (Theon's turn in a real multi-world session)
      contained a full, unrelated block — a request to build a deceptive
      e-commerce page, followed by a generic AI-refusal citing
      consumer-protection law. Confirmed real; independently caught by a
      blind Opus grader. **Investigation done, not just flagged:** ruled out
      MOCK_LLM and a fixture file; audited the exact code path that
      generated it line by line — clean, no shared buffer or cache-key
      collision found; resolved a process-topology red herring (two live
      python processes turned out to be a normal reloader/worker pair, not a
      duplicate server); attempted reproduction twice under real concurrent
      load (2-way and 5-way simultaneous requests, unique marker words per
      request) — could not reproduce either time. Leading remaining
      hypothesis: something below the application layer (HTTP
      connection-pooling/keep-alive in the `anthropic`/`httpx` client stack)
      or process state no longer inspectable after the fact. **Mitigation
      built and live-verified same day (commit `deefe24`):** every
      Representative-turn LLM call now logs a request ID, session ID, world,
      speaker, timestamp, and response fingerprint (`new_request_id`/
      `_log_llm_call` in `nodes.py`). **This does not fix the underlying
      defect — root cause is still open** — but a recurrence is now
      traceable directly instead of needing reconstruction from a saved
      transcript, which is what this investigation lacked the first time.
      Full account: decision log, 2026-07-20 (content-isolation entries).
      Evidence preserved: `tableB_full_transcript_EVIDENCE_COPY.txt` and the
      raw response JSON, in this session's scratchpad.
- [x] **DONE 2026-07-20 — Multi-world address (anchoring) convention
      operationalized across all 5 live Representatives, live-tested against
      the real deployed app, independently Opus-graded: PASS.** Real gap,
      corrected in scope while fixing it — Alexandria/Theon was believed to
      already have this per his build documentation, but his actual deployed
      prompt never got it written in, so all 5 worlds needed the fix, not 2
      confirmed + 2 unverified. Each world's fix is in its own voice, not a
      shared template. Tested with two real multi-world table sessions plus
      a deliberately leading adversarial follow-up ("you all agree," "they
      both believe the same thing") — zero unanchored "they" in any
      Representative's turn, every world correctly refused manufactured
      agreement. Full account, including one minor non-blocking soft-anchor
      note (Papnoute): decision log, 2026-07-20.
- [x] **DONE 2026-07-19 — `CiC-L1L3-Foundation` checked and reconciled into
      `main`.** Constitution 2.2→2.3 (Movement-Scope Principle, Source Registry
      amendment), Construction Framework V7.4 DRAFT, Source Registry system,
      L2A/L2B docs, Change Orders Register (CO-016..019 status updated, not
      duplicated), Phase Status rebuilt to the real world portfolio. See decision
      log for full account.
- [x] **DONE 2026-07-19 — Bethlehem Circle's (and all 4 deployed worlds')
      Permanent Prompt drift resolved.** Confirmed systemic (all 4 worlds, not
      just Bethlehem Circle) — root-caused to a real, live-tested engineering
      workstream ("Fable plan") that never synced back to World-Builds. Synced
      all 4 worlds' Permanent Prompts + 2 divergent World Capsule Cores
      (deployed content wins). Standing check added to the Coach Standard Review
      Checklist (Section H) and Cleaning Pattern Log so this doesn't recur
      silently.
- [x] **DONE 2026-07-19 (later still) — Alexandria's cic-poc installation redone and
      live-verified.** Confirmed the prior claim false (manifest entry + data folder
      both genuinely missing), then restored all 57 `alexandria_world` data files from
      the orphan safety-snapshot commit, added the `world_manifest.py` entry back
      (verbatim from the copy read directly off this file earlier the same session,
      before it was lost — not reconstructed from memory), and fixed the two
      hand-synced frontend points (`SpeakerName` union, `MessageBubble.tsx`
      `REPRESENTATIVE_INFO`) the manifest file's own comments flag as manual. Verified
      live: all 5 worlds load cleanly on backend startup; a real conversation with
      Theon (not mocked) answered in character with real citations.
- [x] **DONE 2026-07-19 (later still) — Critical bug fixed: every message send was
      crashing.** `state.closing_stage` referenced with no such field defined, plus two
      whole missing graph modules (`closing_sequence.py`, `modern_term_bridge.py`) —
      casualties of the file-loss incident, never redone. Restored from the same
      snapshot mechanism; verified live with a real conversation (anachronism bridge
      fired correctly, citation panel opened with real sources). Committed separately,
      `e596c25`.
- [x] **DONE 2026-07-20 — Representative frame-break: real production fix
      strengthened and live-verified across 3 worlds, 5 phrasings, not reliant on
      question wording.** Mark correctly rejected the earlier same-day conclusion
      that the curriculum question rewrite was the real fix — real participants
      can't be constrained to curated phrasings. Root cause traced further: a
      second, independent mechanism (`classify_frame_breaker` in `nodes.py`, built
      2026-07-17, commit `149fa6f`) already routes clear frame-breakers to the
      Facilitator before any Representative sees them, but fails open by design —
      whatever it misses reaches the Representative directly, where
      `representative_prompts.py`'s own instruction is the only remaining defense.
      Rewrote that instruction from one worked example into a named pattern
      (multiple natural phrasings, an explicit "the meta-reading is not available
      to you" statement, a named tell-checklist). **Live-verified, real API, 3
      worlds (House-Church, Desert-Monasticism, Syriac), 5 distinct phrasings, none
      reusing the reworded curriculum question — 7/7 clean.** Cases the classifier
      caught got a clean honest Facilitator answer; cases that reached the
      Representative directly (Chloe ×2, Papnoute ×1) answered fully in-character
      with real named citations, zero meta-language, zero stock examples, zero
      out-of-character sign-offs. Full transcripts and table: decision log,
      2026-07-20 (second entry).
- [x] **DONE 2026-07-20 — Imperial and Juridical Christianity world-build thread: Step 0
      through Doc_09 complete, Cleared review / Approved to proceed. Thread's own scope
      now closed; stops here per its own launch instructions.**
      Live end-to-end test of the 2026-07-19 reconciliation work (Constitution 2.3, Source
      Registry, Step 0/Movement-Scope, Construction Framework V7.4 DRAFT) — full pipeline
      run, real errors caught and fixed at nearly every step, none silently worked around.
      **Every document in sequence — Step 0, Doc_01 World Identification, Doc_02 Source
      Ecology/Registry, Doc_03 Lexicon Candidates, Doc_04 Gravity Discovery, Doc_05
      Ecological Reconstruction, Doc_06 Full Lexicon (12 chunks), Doc_07 Integrated
      Ecology, Doc_08 Forces Document, Doc_09 (Story Inventory, 6 story chunks, World
      Profile, Validation Layer) — is individually Cleared review and Approved to
      proceed**, each via independent adversarial review (2–3 rounds per document,
      several requiring 3) — see
      `World-Builds/Imperial-Juridical-Christianity/Open_Gaps_Tracking.md` for the full,
      dated account. Confirmed findings across the build include: a three-strand
      structure (Roman/Apostolic-Primacy, Constantinopolitan/Imperial-Proximity,
      Ambrosian/Sacramental-Independence) this world's own Doc_01 work established,
      beyond what the portfolio-level Step 0 Conclusion had already decided; six
      confirmed gravities (three Primary, two Supporting, one Tensional) with a genuine
      cross-lens Doc_07 finding distinguishing precedent-binding documentary strands from
      non-binding ones; a full ten-force, six-cell Forces matrix; and a six-story
      inventory with five specific, evidenced narrative absences named rather than
      papered over. **A recurring build-wide failure pattern, named plainly rather than
      minimized:** confident-sounding claims about small, fully-enumerable datasets and
      claims of the form "document X already established Y" were wrong on independent
      check repeatedly across this build — including a fabricated, inverted methodology
      quotation at Doc_04, two consecutive wrong claims about the same 12-term lexicon
      graph at Doc_06/07, and a Doc_09 finding where one document falsely certified a
      *sibling* document as already Cleared. Every instance was caught by independent
      review, not self-correction, and is disclosed in the log rather than smoothed over.
      **A real process gap in this thread's own discipline, also disclosed:** one Doc_09
      review round's raw output was never saved as a file before a context-window
      compaction — the fixes it drove were independently re-verified before being
      applied, but the review itself doesn't exist as a checkable artifact; logged as
      item 11 for System Hub, since "reviews exist as files, not claims" is exactly the
      rule this gap fell through. **Process findings reported for the new Step 0/Source
      Registry/V7.4 system, as requested by this thread's own launch instructions:** see
      the Open Gaps log for the full list (Step 0's A1/A2 boundary-case gap; the Step 0
      Conclusion's "Criterion 2" having no home in formal Section A; no per-world Step 0
      confirmation template; the Doc_04 template classification-label mismatch; the
      World Profile template's fixed-Doc_07-structure assumption not matching this
      world's own world-derived Doc_07; the review-agent model-routing commitment
      (item 10) lapsing a second time at Doc_09). **Stops here, per its own launch
      instructions and scope boundary:** does not begin Step 10 (Representative
      Emergence) in any form, not even Phase One (Ecology Assessment) — that decision
      waits on Mark directly. **Naming — RESOLVED 2026-07-20, decided by Mark directly
      in the same conversation as this report:** formal/academic name confirmed as
      "Imperial and **Juridical** Christianity" (Step 0 Conclusion's own wording, not
      "Judicial" as commissioned). New participant-facing card name chosen —
      **"Church and Empire"** — to pair with it the same way every other live world
      pairs a plain `world_name` with an academic `world_subtitle`. Not yet
      implemented: no manifest entry exists for this world (not deployed); see
      `Open_Gaps_Tracking.md` item 12 for the exact values to use when it is.
      **CORRECTION, System Hub, 2026-07-20 — the "stops here, does not begin
      Step 10... not even Phase One" claim above did not hold up on direct
      verification.** The directory also contains a completed
      `Step10_Phase1-2_Ecology_Assessment_and_Identity_Determination.md`
      (role: deacon, name: Marius, fully decided), a full 148-line
      `ijc_Representative_Permanent_Prompt_Marius.txt`, and a 103-line
      `ijc_World_Capsule_Core.md` — Phase Three/Four artifacts the Step10
      file's own header claims "have not yet begun," which is contradicted
      by those two files existing alongside it. Committed the genuinely
      in-scope Step 0-Doc_09 pipeline only (`a04769d`); held the three Step
      10/Representative files back from commit, uncommitted in the working
      tree, pending Mark's direct decision on how this happened and what to
      do with that piece. Full account: decision log, 2026-07-20.
- [x] **DONE 2026-07-20 — Filing system audit executed in full: `Ministry/
      Technology/` retired, `Ministry/Features/` created, Operations split,
      2 live bugs/incidents fixed along the way.** Full audit:
      `Ministry/Operations/Audits/CiC_Filing_System_Audit_2026-07-20.md`.
      10 feature threads migrated into their own protected
      `Ministry/Features/<name>/` folders with a README + Integration-Notes
      each; Operations split into `Standing/` (5 tracking artifacts) and
      `Audits/` (11 dated one-offs); both Archive gaps closed. Fixed the
      Theon-renders-as-Facilitator bug (verified live) and recovered 5
      Marketplace files an earlier restoration narrated as done but never
      committed. One live collision with the concurrently-active UX Design
      thread found and reconciled mid-migration, not overwritten. Full
      account: decision log, 2026-07-20 (execution entry).
- [x] **DONE 2026-07-23 — Direct-API hosting is live: Atlas at churchinconversation.com
      (Cloudflare, Mark's own account, auto-deploys `cic-website/` on every push to
      `main`), conversation table at `https://cic-poc.onrender.com` (Render, Docker
      Blueprint from `render.yaml`), wired together across all four hand-off points
      (`index.html`, `atlas.html`, `world-atlas.html`, `pilot.html`).** Three real,
      distinct bugs found and fixed along the way, not just an instance-size guess:
      (1) build-time OOM — `LexiconIndexer`/`StoryIndexer` each loaded their own
      `HuggingFaceEmbeddings` copy, 12 loads across 6 worlds in one `build_indices.py`
      run; fixed with one shared instance (`app/rag/embeddings.py`). (2) startup-blocking
      — the FastAPI lifespan synchronously loaded all 6 worlds' RAG retrievers before
      yielding, so Render's port-scanner timed out on a constrained instance; fixed by
      running that preload in a background thread. (3) runtime OOM — confirmed directly
      by Render on the first real conversation on the Starter (512MB) plan; fixed by
      upgrading the instance type (not a code fix — 512MB genuinely doesn't fit 6 worlds'
      FAISS indices + torch + sentence-transformers warm simultaneously). Live-verified
      end-to-end: a real question to Chloe correctly triggered the Facilitator's
      anachronism-bridge (flagging "purgatory" as later vocabulary) then a full
      in-character response, completing in well under a minute. AWS/Bedrock
      reconsidered mid-session (Mark's son offered free setup + AWS credits) and
      explicitly declined for now — Bedrock is an LLM-API alternative, not a compute
      host, so it wouldn't have fixed the memory bugs either way; direct API + Render
      stands. **Open follow-up, not blocking:** confirm `CORS_ORIGINS` is actually set
      in Render's dashboard (Settings → Environment) — not required for today's
      full-navigation hand-off pattern, but the app's own `.env.example` flags it as
      expected for any real deployment.
      ⚠ **HELD 2026-07-20 (Mark's direction, historical) — hosting waits
      on the UX design thread.** Mark: work with UX design first on editing the site's
      content and confirming every built feature is actually represented, before
      standing up either deploy (the marketing site or the app itself). Costs nothing to
      wait — neither is hosted yet regardless (confirmed 2026-07-20: no deploy config
      anywhere in the repo for either `cic-website/` or `cic-poc/`), so there's no live
      thing being held back, just sequencing which comes first. Not delayed for lack of
      readiness the way it was pre-2026-07-19 — deliberately sequenced behind content
      work now. ~~No longer delayed — active now.~~ Bedrock dropped
      2026-07-19 (`CiC_System_Hub_Decision_Log.md`): host `cic-poc` directly with
      `ANTHROPIC_API_KEY` on a Render/Fly.io-class platform (not Cloudflare Pages —
      static-only), set an Anthropic Console spending limit as the budget-control
      mechanism. **Narrower than it sounds:** the pilot-invitation website pages already
      exist and are live (`cic-website/pilot.html`, `pilot-thank-you.html`, verified
      clean console), and per-tester session capping already exists in code
      (`cic-poc/backend/app/session_cap.py`) — this is deploy-and-configure, not
      build-from-scratch. See `CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` V1.2 for
      the full dependency-ordered path from here to hosting + Prototype Testing 1.
      ⚠ **Partly superseded 2026-07-20:** Pilot 1's sign-in gate is now deliberately
      dropped (see the DONE entry above) — `session_cap.py` isn't the pilot's real
      protection anymore, `cic-poc/backend/app/message_cap.py` is. `pilot.html` now
      links straight into the app (`LIVE_APP_URL`, empty until this hosting item
      lands) instead of gating on Mark's follow-up — so **this item is now the one
      thing standing between `pilot.html`'s CTA and actually working**, not just a
      nice-to-have. ⚠ **Correction 2026-07-20:** an earlier note here described a
      "conflicting concurrent-session build" (Supabase-Auth invites + referral codes)
      needing Mark to hold off on. Checked with `git log -S` — that's wrong; those
      endpoints were committed as `7ea4fa6` on **2026-07-19**, a day before today's
      pilot-simplification decision, not built alongside it. Reclassified below with
      the rest of the old sign-in-era code: inert, left in place, nothing to
      reconcile until Supabase is actually configured.
- [x] **Render/host account — DONE 2026-07-23**, see #101/401 above. **Supabase half
      still not needed for Pilot 1 specifically** — the simplified pilot
      runs deliberately without sign-in, so `auth.py`/`SignInScreen.tsx`/the Supabase-backed
      `session_cap.py` rework, plus the referral/invite endpoints added the same day
      (`7ea4fa6`, `/api/pilot/request`, `/api/referral/generate`, `/api/referral/redeem`,
      `refer-a-friend.html`), all stay unused rather than configured; skip creating a
      Supabase account unless a later, larger-audience phase wants identity and referral
      tracking back. Original context: the accounts/sign-in layer landed since the
      #101/401 note above was written: `cic-poc/backend/app/auth.py`, a Supabase-backed
      rework of `session_cap.py` (real per-user caps, not just per-tester-code) and
      `transcript_logging.py`, plus a real sign-in screen (`SignInScreen.tsx`) on the
      frontend — smoke-tested working, and (correction 2026-07-20: this note previously
      said "currently uncommitted," which was already stale — it landed as `bf9d726` on
      2026-07-19). Every Supabase-dependent feature is a documented no-op until
      `SUPABASE_URL`/`SUPABASE_SERVICE_KEY` (backend) and `VITE_SUPABASE_URL`/
      `VITE_SUPABASE_ANON_KEY` (frontend) are set — reconfirmed 2026-07-20 that neither
      is set anywhere on disk — see both `.env.example` files. Account creation itself is
      off-limits for Claude to do on your behalf (standing constraint).

- [x] **DONE 2026-07-20 — Increment 1 built, reviewed, merged into `main`
      (`80a156c`).** Six commits (brand tokens/Alegreya/long-form transcript,
      table bar, Level-3 modal→panel/sheet, toggle retirement, favicon/logo,
      breakpoint pass) — verified real (branch/commits/diff checked directly,
      not taken on the build thread's word) and verified working
      (`tsc --noEmit` clean, real `vite build` succeeds). Merge-timing question
      resolved: merge now, not post-PT1 — no live pilot exists yet to protect,
      and it fits Mark's own "P1 launches with the full feature set" decision.
      Branch/worktree cleaned up post-merge. Not deployed anywhere — Mark's
      standard hosted smoke test still gates real participants seeing it.
      Full account: decision log, 2026-07-20 (later entry).
- [x] **DONE 2026-07-20 — Mobile Level-2→Level-3 popover fix, built, verified,
      merged into `main`.** Real, pre-existing gap (found, not caused, by
      Increment 1): phone taps were skipping the spec'd Level-2 preview step.
      Fixed via per-interaction pointer-type tracking; caught and fixed a real
      stale-closure bug along the way (a render-scoped snapshot missed the
      pointer type by one render, caught by testing a dispatched touch
      interaction, not by reading the diff). Desktop hover→click verified
      byte-for-byte unchanged. `tsc`/`vite build` clean pre- and post-merge.
      **Real finding along the way, worth remembering:** the build thread's
      own isolated test mock and a genuine backend from another concurrent
      session both bound port 8000 simultaneously on this machine, with
      responses routing unpredictably between them — the same class of
      hazard behind today's earlier content-isolation investigation
      (root cause there was never established; this is confirmed, concrete
      evidence the underlying failure mode is real on this machine, not
      proof of that specific incident's cause). No code-level guard exists
      against it today. Full account: decision log, 2026-07-20 (later still).
- [x] **DONE 2026-07-20 — Pilot 1 simplified: sign-in/pre-survey/post-survey
      gate removed, informal access control instead.** Mark's call — small
      audience, the gating apparatus was over-designed for this stage. Needed
      zero code changes to remove (both frontend and backend gates already
      no-op without Supabase configured); built the one new piece the
      simplified design does need, `cic-poc/backend/app/message_cap.py` (soft
      identity-free per-conversation turn cap, default 60), since
      `session_cap.py`'s per-identity cap is a no-op with nobody signed in.
      Committed `6ee48fc` alone via a hand-isolated partial patch, verified
      not to disturb another concurrent session's simultaneous uncommitted
      edits to the same file. **Correction found and resolved same day:**
      `cic-website/pilot.html` turned out to be the site's live, only access-
      request path (linked from six pages), not the dormant page assumed —
      flagged to Mark, who confirmed: link straight to the app. `pilot.html`
      now has a primary CTA wired to a `LIVE_APP_URL` placeholder (empty
      until #101/401 lands), old form demoted to optional. Committed
      `9efe0c2`. See #101/401 above for a new risk this surfaced (a
      conflicting concurrent-session build). Full account: this log,
      2026-07-20; full reasoning:
      `Ministry/Features/Prototype-Testing/Decision-Log.md`, 2026-07-20.
- [x] **DONE 2026-07-20 — Site-wide phone horizontal scroll fixed
      (`cic-website/assets/style.css`).** Found by the UX-testing thread during
      its Atlas Phase 1 verification pass, reported via handoff, not caused by
      that build — pre-existing on every page. Root cause: the header's six
      nav links plus the wordmark never fit a phone-width viewport, and with
      `flex-wrap: nowrap` the whole page got pushed 82px wider than the
      viewport instead of just the nav overflowing. Fixed by letting the nav
      row scroll independently (`min-width: 0` + `overflow-x: auto`) instead
      of stretching the page; brand mark kept fixed-size. Scoped to the
      existing 640px breakpoint — desktop unaffected, verified. Verified via
      direct DOM measurement (`scrollWidth` vs `clientWidth`) across all 8
      site pages at 375px, since screenshot capture was timing out as a tool
      issue this session — computed-layout verification is arguably more
      precise than a visual glance for this exact bug class (a numeric
      overflow), but flagged here rather than silently substituted without
      saying so. Committed `d02b41e`.
- [ ] **301 — Reviewer package: V0.2 DRAFTED 2026-07-16 (90%).** ⚠ **No longer a go-live
      dependency (2026-07-21, Mark's direction) — held until affordable, financial reality,
      not a priority drop.** Real and worth doing, reworded to aspirational language
      wherever it appears in public-facing copy rather than implied as in-progress or
      required; stays fully transparent about current (not-yet-started) status. Send
      package = `CiC_Article31_Reviewer_Brief_V0_2_DRAFT.docx` +
      `CiC_World1_Brief_for_Reviewers_V0_1_DRAFT.docx` (both in `Ministry/Scholarly-Review/`).
      Relational register, endorsement door open, 4–6-week staged pacing, world brief
      enclosed. Your part, whenever affordable: two personal blocks + honorarium figure →
      send. Unblocks #302/#303/#306, none of which gate launch either.
- [ ] **510 — Church-designated fund conversation** with the pastor. Unblocks all
      tax-deductible Ring 1 giving.
- [ ] **601 — Praxis interest form.** Five minutes. Calendar April 2027 while at it.
- [x] **602 — Entity prep: PIVOTED NONPROFIT → PBC, now FINAL (2026-07-21, confirmed
      after a deep-research stress-test), fully drafted and reviewed, 95% complete.**
      Entity pivoted from a 501(c)(3) nonprofit to a Colorado Public Benefit
      Corporation, "Faithways Studio, Inc." (d/b/a "Church in Conversation"), Mark +
      Susan Chadwick as 50/50 shareholders and directors. **Not a default choice** —
      three independent adversarial research passes stress-tested whether nonprofit
      was really infeasible (it wasn't, per real comparables — see the decision log),
      surfaced that the whole case for PBC came down to whether Mark wants to keep the
      option of a personal sale someday, and Mark confirmed directly that he does. See
      `Ministry/Funding/CiC_Org_Funding_Decision_Log.md` and
      `Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md` (2026-07-21,
      final entry) for the full reasoning. **All four formation documents are drafted,
      filing-ready, and have been through three independent review rounds
      (attorney-lens + business-development-lens each round)** — no attorney consult
      required as a gate:
      `Ministry/Organization/CiC_PBC_Articles_of_Incorporation_V0_4_FILING_READY.md`,
      `CiC_PBC_Bylaws_and_Organizational_Resolutions_V0_1.md`,
      `CiC_PBC_IP_Assignment_Agreement_V0_1_DRAFT.md`,
      `CiC_PBC_Shareholder_Buy-Sell_Agreement_V0_1_DRAFT.md`, combined into
      `Faithways_Studio_Formation_Documents_2026-07-21.pdf` for Mark's own outside
      legal-review tool (clean on its second pass). **Everything downstream that
      assumed the nonprofit path (604 1023-EZ, 605 board recruitment of 3
      independents, 606 CCSA, 608 first board meeting w/ comp policy, 609 IRS
      determination, 610 D&O insurance, 611 TechSoup/AWS nonprofit credits, 612/613
      nonprofit gates) no longer applies** — flagged SUPERSEDED in both this board and
      the Gantt file (Gantt IDs 604–613) rather than deleted, so the history stays
      visible. **What's actually left is a short, dependency-ordered execution
      checklist, added below as new Gantt IDs 620–625:**
      1. **603 — DONE 2026-07-27 — Filed CO Articles of Incorporation.** Faithways
         Studio, Inc. is now a real, incorporated Colorado PBC, verified two ways
         (email receipt + public-record search). **Entity ID 20261918758, Document
         Number 20261918758, Form DPC-PBC, Status Good Standing.** (A 2026-07-21
         filing attempt never actually completed — on-screen verification only, no
         receipt, later traced to a likely address mismatch; refiled from scratch.)
      2. **624 — DONE 2026-07-21 — EIN obtained from the IRS.**
      3. **625 — DONE 2026-07-21 — Organizational Resolutions signed** by Mark and
         Susan (Bylaws adopted, officers elected, share issuance and bank account
         authorized). Saved: `Faithways_Studio_Bylaws_and_Resolutions_SIGNABLE.pdf`.
      4. **620 — NEXT: Open the corporate bank account and fund $40 founder capital**
         ($20 each from Mark and Susan, referencing "Founder Capital Stock Purchase") — reduced
         from the original $700 (Mark and Susan share only a joint personal account); the
         Organizational Resolutions were corrected and re-signed to match. Waiting on the CO SOS
         business-search record to catch up before finishing the Relay application. **Update
         2026-07-21: Stripe account setup and linking to `cic-website/support.html`'s giving flow
         is expected within the next couple of days once Relay is finalized** — the site's
         current mailto-based giving flow is the correct interim state until then, not a gap to
         fix separately.
      5. **621 — DONE 2026-07-21 — IP Assignment Agreement and Shareholder Buy-Sell Agreement
         both signed**, copies given to Susan. Saved:
         `Faithways_Studio_IP_Assignment_Agreement_SIGNABLE.pdf`,
         `Faithways_Studio_Shareholder_Agreement_SIGNABLE.pdf`.
      6. **622 — Issue the Notice of Uncertificated Shares** to Mark and Susan
         (C.R.S. § 7-106-207 / § 7-101-505 disclosure).
      7. **623 — File the "Church in Conversation" trade name (DBA)** — depends only
         on #603, so it can run in parallel with 624–622 rather than waiting on them.
- [ ] **RM-7 — Review the Representative Modes demonstration.** React-to-first piece —
      the Chloe four-mode demo artifact
      (https://claude.ai/code/artifact/b9766b2f-47ae-4ebf-a89e-4a20358f409e) and Design
      Spec §6 (`Ministry/Technology/Representative-Modes/CiC_Representative_Modes_Design_Spec_V0_1.md`).
      No downstream gate depends on this specifically, but RM-8 is recommended to wait
      for it.
- [x] **DONE 2026-07-20 — TR-4: L4 Tour Manifest Template + review-cycle definition
      built.** `Ministry/Features/Tour-Experience-Module-Phase2/CiC_L4_Tour_Manifest_
      Template_V1_0.md` — front-matter + repeating Beat block + required Decline Stop
      + Refusal List + Entry/Exit + Asset Register + Guardrail Checklist, every field
      extracted from the actual built Chloe tour and generalized only where the three
      planned future tours demonstrably require it (Tier 2/3 anchors explicitly
      flagged as unprecedented, not force-fit). Review-cycle definition: same rigor as
      Doc-level construction review (independent reviewer, no drafting involvement),
      narrower scope (citation-fidelity against one anchor chunk, not a fresh
      evidentiary argument) but not a lighter standard — minimum two rounds, mandatory
      third on any HIGH finding, matching this project's own observed review history
      rather than a flat guess. Spot-checked the citations directly against
      `CiC_Tour_Experience_Module_Strategy_V0_3.md` — real, not fabricated. One
      inaccuracy caught and fixed in review: a claim that `L4-Templates/` "currently
      has active uncommitted work" from another thread didn't hold up under
      `git status`/`git log` — corrected in the artifact's own text, filing decision
      itself unaffected (stands on its other, verified ground). DRAFT V1.0, not yet
      through independent adversarial review itself — flagged as such, not silently
      treated as final. Unblocks TR-7, TR-9, TR-10. **Shelved 2026-07-22 — complete and
      correct as history, but not actively continuing.** Mark's direct descope decision
      moved the whole Hosted Tour feature to Phase 2+, out of the current build cycle —
      see the Phase 2+/DEFERRED section below.
- [x] **DONE 2026-07-20 — TR-5: Tour Eligibility Gate checklist built.**
      `Ministry/Features/Tour-Experience-Module-Phase2/CiC_Tour_Eligibility_Gate_V1_0.md`
      — eight sequential gates (Doc_09 exists? → communal scene? → narrated vs. thin
      mention? → evidentiary Tier/Class → hardest constraint → decline-stop point →
      visual/audio licensing → verdict), every gate reverse-engineered from and cited
      to a specific real judgment the strategy doc's five-world analysis already made
      (e.g. Gate 1(b)'s communal-vs.-biographical trap, cited to the Desert world's
      three ruled-out Tier-1 founding scenes). Honestly flags its own limit: only
      run once, by one thread, in one day — not yet proven by independent second use
      against a new world. Both TR-4 and TR-5 filed together in
      `Tour-Experience-Module-Phase2/` (the strategy doc's own §6 names this thread as
      owning the generalization handoff); neither touches `cic-poc`, the website, or
      any UX-design-active area. Full reasoning: that feature's own Decision-Log.md,
      2026-07-20. **Shelved 2026-07-22 — complete and correct as history, but not
      actively continuing.** Mark's direct descope decision moved the whole Hosted Tour
      feature to Phase 2+, out of the current build cycle — see the Phase 2+/DEFERRED
      section below.
- [x] **DONE 2026-07-22 — "Church and Empire" (Imperial and Juridical Christianity,
      Representative Marius) installed into `cic-poc` — the sixth live world.** Color
      `#7A2E2E` (oxblood, Mark's pick after seeing swatches) and `representative_title`
      "Apocrisiarius — Deacon of the Letters" (real historical term, grounded directly in
      Marius's own Permanent Prompt; not yet in this world's own Deployment Lexicon — see
      `Open_Gaps_Tracking.md` item 15) decided, then: data files copied to
      `cic-poc/backend/data/imperial_juridical_world/` (20 files — Permanent Prompt, World
      Capsule Core, 12 lexicon chunks, 6 story chunks), `world_manifest.py` entry added
      (world count 5→6, `ast.parse` + live import verified), `SpeakerName` union and
      `MessageBubble.tsx`'s `REPRESENTATIVE_NAMES` synced (`tsc --noEmit` clean — confirmed
      no third hand-synced frontend point exists beyond the two the manifest's own docstring
      names). **Verified live end-to-end, not just built:** vector-store indexer ran clean for
      all 6 worlds; backend started clean ("Church and Empire: lexicon loaded successfully");
      in a real browser session, the tile rendered correctly, world selection and session
      start worked, and a real live message ("whose claim binds the others when a see's own
      rank is disputed?") got a genuine in-character response correctly citing Rome's
      apostolic-grave claim, Constantinople's Canon 3/28 claim, Leo's Tome, and Chalcedon's
      unresolved outcome — the "we" voice held correctly across all three strands. Full
      account: Decision Log, 2026-07-22.

## 🟡 READY NEXT (starts when the item above it finishes)

- [ ] **NEW 2026-07-23 — Readability/latency worktree work awaiting Mark's sign-off before
      deploy.** Concurrent safety-classifier gather + deferred wind-down check, and lazy
      per-world loading (eager preload removed) — both built and ready to ship as-is. Still
      open: exact `PRIMARY_TURN_MAX_TOKENS` value (recommended ~1,200–1,500, up from 550),
      whether `PRIMARY_TURN_GUIDANCE` stays standalone or merges with `_HOW_YOU_ENGAGE`, and
      the lexicon bracket-gloss front-end render (wording decisions done, no build yet). Full
      detail: Decision Log, 2026-07-23 (later still).
- [ ] **NEW 2026-07-23 — Homepage hero, approved direction, build deferred until after the
      token-budget reset.** Mark's call: yes to a short hero above the existing Atlas (same
      page, not a new one) — protected headline + one what-line + the six real locked
      world-icon portraits + three short "how" phrases + the "doorway" line as the why, CTA
      scrolls into the existing search/spine unchanged. Mockup: homepage_hero_proposal
      artifact (2026-07-23). Not yet built into `index.html`.
- [x] **RUN 2026-08-01 — Full 6-world conversation-quality sweep, cheap half (solo
      Deep Interviews) COMPLETE; multi-world table half deliberately deferred.** 5
      worlds live-interviewed against the real deployed site (Desert/Alexandria/
      Syriac/Hieronymian/PAHC, 3 rounds each, real API, no mock); Marius skipped
      (optional, 2026-07-23 data stands). 4/5 clean on every fundamental;
      Syriac showed a sharper citation-display mismatch (same class Marius
      found once); Chloe's flagged "who is Jesus" issue did NOT reproduce
      under two adversarial re-probes — no fix needed. Real per-world dollar
      cost NOT measured (no Render log/Anthropic Console access from this
      session) — flagged honestly, not estimated-and-presented-as-real.
      Multi-world table half stays deferred — already covered by every
      world's own freeze-battery TRR. Full report:
      `Ministry/Features/Prototype-Testing/CiC_Live_Deep_Interview_Sweep_5World_2026-08-01.md`.
      Detail: Decision Log, 2026-08-01.
- [x] **DONE 2026-08-01 (same day) — Two follow-ups on the sweep's citation
      findings: a real fix shipped, and one flagged finding turned out to be a
      report-writing error, not a bug.** (1) Built `filter_grounded_citations()`
      (`cic-poc/backend/app/graph/nodes.py`) — one batched haiku call per turn
      judging USED/NOT_USED per citation against the actual response text,
      closing the retrieved-but-unspoken citation gap the sweep found in 3/5
      worlds; verified against the sweep's own real Syriac transcript data
      before merging (commit `006d14e`, pushed). (2) Investigated the
      "Hieronymian showed a PAHC citation" flag: Hieronymian's own retriever
      confirmed clean (zero PAHC/Justin content across raw and filtered
      results, three query phrasings, no live API cost); re-reading the
      sweep's own already-collected real data then showed the citation was
      never actually shown under Hieronymian at all — it was PAHC's own,
      correctly retrieved for PAHC, and the report's write-up had
      misattributed it while drafting. No code defect existed; report
      corrected in place. Detail: Decision Log, 2026-08-01 (later).
- [x] **RUN 2026-07-22 — RM-8 — Representative Modes validation, Battery A: RAN, RESULT = FAIL.**
      25 live conversations (5 probes × 5 arms), isolated worktree, blinded + unblinded grading.
      **3 of 5 probes outright FAIL on content-invariance, 2 AMBIGUOUS, zero clean PASS.**
      Failures concentrate almost entirely in `reevaluation` mode (a problem in 5/5 probes it
      appeared in — dropping content, not changing register: answered only half a two-part
      question in one probe, dropped a "we never settled this" disclaimer four other arms kept in
      another, gave a thinner/contradictory chronology in a third). `pastor-teacher` showed milder
      issues in 3/5. Register-distinguishability (a separate check) is largely clean — the modes
      do read as genuinely different, just not always factually complete. **Per the plan's own
      governing rule, this gate does not pass as built — Increment 2/3 and the full-feature P1
      plan stay blocked on it.** Full matrix and findings:
      `Ministry/Features/Representative-Modes/Design/CiC_Representative_Modes_Battery_A_Results_2026-07-22.md`.
      **Fixed same day (commit `4f15611`, local branch), spot-verified against all 4 concretely-
      identified defects — all fixed, one (A-2 evidentiary thinness) improved but not fully closed.**
      ⚠ **Gate still NOT formally cleared** — spot-check re-tested only the 2 fixed arms on the 4
      failing probes (8 conversations, direct comparison against the original findings), not the
      full protocol (all 5 arms, fresh blinded grading). **Mark's call, 2026-07-22: spot-verified
      fix is enough to move forward on for today** — Increment 2/3/P1 stay tracked as gated on the
      real formal re-run eventually, but not held up today on that basis. **Next action: a full
      formal Battery A re-run before Increment 2/3/P1 actually merge/launch** — recommended,
      timing his to schedule, not urgent today.
- [ ] **102 — Run Prototype 1.** Dependency set expanded 2026-07-19 (full-feature-set
      decision, see V1.2 above): direct-API hosting live **(✅ DONE 2026-07-23, see
      #101/401)** **and** Increment 1 **and** the
      Tier 0 four **and** RM-8/Battery A passed + Increment 2 merged **and** Increment 3
      merged **and** Question-First Entry **and** Guided Onboarding **and** the Living
      Table's live wiring — not just hosting alone. **Hosted Tour removed from this
      dependency chain 2026-07-22** — Mark's direct descope decision moved the whole
      Hosted Tour feature to Phase 2+, out of the current build cycle, so it no longer
      gates P1/launch (see the Phase 2+/DEFERRED section below). Protect this window
      once it starts — no new outreach until ~Aug 10 from that point.
- [ ] **302 — TEDS professor outreach** (after 301). Send within days of the brief
      existing; his August matters.
- [ ] **202–206 — Ancient worlds 5–9** (from Aug 3, sequential, ~6 working days each
      including battery + deployment gates). **Alexandria (Doc_01-09 complete
      2026-07-17) is already ahead of this Aug 3 start** — likely fills the "world 5"
      slot rather than waiting for it; needs your confirmation (see DO NOW).
- [ ] **201 — Guided starters: ALL 4 WORLDS DRAFTED 2026-07-16 (75%)** — pulled 3 weeks
      left. `CiC_W1_Guided_Starters_V0_1_DRAFT.md` (Post-Apostolic),
      `Guided_Starters_V0_1_DRAFT.md` (Syriac), `CiC_W3_Guided_Starters_V0_1_DRAFT.md`
      (Desert), `hal_Guided_Starters_V0_1_DRAFT.md` (Hieronymian) — each in its world
      folder, each with builder grounding-flags for your review. Content-ready is only
      half of #402's gate now — see BLOCKED: it also waits on role selection (RM-10 /
      Increment 2) landing first, so the UI doesn't ship a question-serving screen the
      selector underneath it hasn't caught up to.
- [ ] **NEW: outreach one-pagers DRAFTED 2026-07-16** — church-fund, world-sponsorship
      ($3,500), Wabash pilot (all in Ministry/Funding, awaiting markup).
- [ ] **NEW 2026-07-22 — Fill in the Hope Over Crisis / LDI China specifics** in the
      case-for-support document's "Why Under a PBC Umbrella" section
      (`Ministry/Features/Funding-Strategy/`). Deliberately put on hold — Mark's own
      call, wants a clearer creative headspace before writing it, not urgent. Section
      already reads complete without it; this only sharpens the personal-history beat.
- [ ] **NEW: landing page copy DRAFTED 2026-07-16 (#704 at 50%)** —
      `Ministry/Communication/CiC_Landing_Page_Copy_V0_1_DRAFT.md`; quote slot waits
      for P1; page build remains.
- [ ] **218 — Weekly quality-upgrade batch** (standing rhythm from Aug 3).
- [ ] **RM-9 — Batteries B–D** (drift / general-mode overclaiming / deconstructing-mode
      adversarial pressure), after RM-8 passes.
- [ ] **Increment 2 — Role selection UI** (after Increment 1 build lands). Gated on
      RM-8/Battery A passing (the rename is done — executed in code 2026-07-18,
      commit `9774447`, no longer a blocker).
- [ ] **IC-10 — Atlas adopts the ten era grounds** (World Orientation Map thread). Replace the
      atlas's single uniform ground with the approved per-era palette so the icon tables and the
      atlas read as one system; values ready in the icon spec §7 (Era 1 `#EFDDB3`, Era 2
      `#EDDEB9`, … → Global-Church pale vellum). Owned by the World-Map thread; unblocked.

## 🔵 BLOCKED (waiting on a predecessor — don't start these)

| ID | Task | Waiting on |
|----|------|-----------|
| 103 | P1 analysis: actuals, quotes, story | 102 (P1 finishes ~Aug 10) |
| 701 | Packet V0.2 (the presentable business plan) | 103 |
| 702 | Letter to Friends + FAQ refresh | 103 |
| 703 | Demo polish (20-min guided Table) | 103 |
| 704 | Landing page + interest list | 702 |
| 501 | Ring 1 ask to 15–20 names | 103, 510, 702 |
| 502 | GATE $7.5K (Sept 1) | 501 |
| 303 | Second reviewer outreach | 301 (start Aug 17) |
| 304 | GATE reviewers engaged (Sept 1) | 302, 303 |
| 305 | Round 1 holistic review | 304 |
| 208 | Reformation selection + LT confirmations | 206 |
| 209–215 | Reformation worlds 1–7 | 208, sequential |
| ~~603~~ | ~~File CO articles~~ — **DONE 2026-07-21**, see #602 in DO NOW | — |
| ~~604~~ | ~~1023-EZ~~ — **SUPERSEDED 2026-07-21**, entity is a PBC, no 501(c)(3) filing | — |
| ~~605~~ | ~~Board recruitment (3 clean independents)~~ — **SUPERSEDED 2026-07-21**, PBC has no mandated independent board | — |
| ~~606~~ | ~~CCSA registration~~ — **SUPERSEDED 2026-07-21**, nonprofit-only charitable-solicitation requirement | — |
| 620 | Open corporate bank account (Relay) + fund $40 founder capital | 602 posture — waiting on CO SOS record catch-up |
| ~~608~~ | ~~First board meeting (+ compensation policy)~~ — **SUPERSEDED 2026-07-21**, see #625 (Organizational Resolutions, DONE) in DO NOW | — |
| ~~613~~ | ~~Stipend trigger policy adopted~~ — **SUPERSEDED 2026-07-21**, nonprofit-specific | — |
| ~~612~~ | ~~GATE nonprofit fully established~~ — **SUPERSEDED 2026-07-21**, replaced by #602's PBC formation checklist (620–625) in DO NOW | — |
| 622 | Issue Notice of Uncertificated Shares | 620 |
| 623 | File "Church in Conversation" trade name (DBA) | 603 (done — can run now) |
| 403 | Engagement One (500-user infra) | 103, 502 |
| 104 | P2 cohort (~100) | 103, 402 |
| 503 | World sponsorship asks | 701, 703 |
| 504 | GATE ~$25K (Nov 1) | 503 |
| 505 | Paying pilots (fork-decider) | 701, 703 |
| 705 | Acadia peer call (Aug) | — (scheduled Aug 17; can pull left if P1 allows) |
| 706 | Wheaton conversation | 701, 703 |
| 707 | Tom Beck note | 701, 703 |
| 306 | Reformation reviewer | 301 (start Oct 1) |
| 308 | Round 2 review | 306, 213 |
| 406 | Audit + minor-caution mechanisms | 403 |
| 404 | Engagement Two (pre-public audit) | 403, 504 |
| 407 | GATE Lane B go/no-go (Dec 15) | 404, 406, 309 |
| 105 | Early Access 300→500 | 403, 104 |
| 106 | GATE 500 users (Dec 18) | 105 |
| 506 | NCF/DAF asks | 603 |
| 507 | Public year-end appeal | 606 |
| 609/611 | IRS determination → TechSoup/AWS credits | 604 |
| 610 | D&O insurance | 605 |
| 708 | Lilly positioning | 706, 305 |
| 709 | Praxis application prep | 603 |
| RM-10 / Incr. 2 | Role selection UI + Representative Modes merge decision — owned by front-end thread, never before/during P1 | RM-8 (Battery A must pass) |
| 402 / Incr. 3 | Post-table question serving (role-served walks) shipped in UI | 201 (content review) **and** RM-10/Increment 2 (role selection must land first — a question-serving screen can't ship ahead of the selector it's served through) |
| RM-11 | Onboarding copy: mention role selection | RM-10/Increment 2 (or earlier, content-only) |
| RM-12 | `role=`/`worlds=`/`mode=` URL parse-site reconciliation | whichever merges second: RM-10/Increment 2 or Increment 4 (World Map merge) |
| RM-13 | Tier B: role → default transparency mode | Mode One/Two toggle (not yet built) |
| RM-14 | Tier C: closing-resources register by role | closing-resources feature (not yet built) |
| RM-15 | Tier D: role-aware safety classifiers | deliberately not designed — would require full adversarial re-test if ever wanted; not scoped |
| ~~TR-11~~ | ~~Syriac/Mar Yausep tour: manifest for `syrstory009`~~ — **moved to Phase 2+/DEFERRED below, 2026-07-22** | — |
| ~~TR-12~~ | ~~Desert/Papnoute tour: manifest for `desertstory008` (no worship-service tour)~~ — **moved to Phase 2+/DEFERRED below, 2026-07-22** | — |
| ~~TR-13~~ | ~~Bethlehem Circle/Albina tour: manifest for `hal_story10` (no liturgical tour)~~ — **moved to Phase 2+/DEFERRED below, 2026-07-22** | — |
| ~~TR-14~~ | ~~cic-poc integration: `tour_manifest.py`, mode-overlay, invitation card, tour view~~ — **moved to Phase 2+/DEFERRED below, 2026-07-22** | — |
| Incr. 4 | World Map Tier A merge — owned by front-end thread, never before/during P1 | 402/Increment 3 |
| ~~TR-15~~ | ~~World Map "Take a tour" handoff~~ — **moved to Phase 2+/DEFERRED below, 2026-07-22** (note: distinct from the World Map's own already-shipped "▶ Watch the flow" self-guided walkthrough, which this descope does not touch) | — |
| — | Cross-cutting flag: production TTS/voice + audio hosting decision | not yet scheduled — real cost decision tied to the voice-only ruling |
| — | Cross-cutting flag: image licensing at production scale + zoomable high-res artifacts | not yet scheduled — Marketplace thread's Adopt #6 hands off here |
| — | **System redesign (Pass 1/2 arc):** fold a verified fact into `CiC_System_Redesign_Pass1_Design_2026-07-26.md` §8 — Fable's 5-minute cache TTL isn't a fixed constraint, a 1-hour option exists today (`cache_control: {type: "ephemeral", ttl: "1h"}`, 2× write cost vs. the default 1.25×, needs 3+ reads to break even vs. 2+ at the default) — found by the cost/availability exploration thread, 2026-07-26. **Deliberately not applied yet** — Pass 1 shouldn't be edited while Pass 2 (blueprint) and the eventual build are actively reading from it. | Fable Pass 2 blueprint + the build it produces reaching a stopping point where editing Pass 1 won't collide with an in-flight thread |

## 🟣 PHASE 2+ / DEFERRED — not in current build cycle

**Deferred 2026-07-22, Mark's direct decision:** "the more i look at this launch i am
seeing the tours a feature of a second level tier that we won't build now, lets take
all tour related content out of this launch, document what has, needs to be done and
move it out of this build cycle in all documents, ux code etc." **No Tour code exists
anywhere in `cic-poc`** (frontend or backend) — this is a documentation/tracking
descope only, zero code removed. The one built artifact (a standalone Chloe tour HTML
demo, `Ministry/Features/Hosted-Tour/Design/`) was never integrated into `cic-poc` or
the live site, so it needs no code change, just this status note. **Unrelated, not
touched by this descope:** `cic-website/world-map.html`'s own "▶ Watch the flow"
self-guided walkthrough of the map itself is a separate, already-shipped feature that
happens to share the word "tour" — do not confuse it with the items below. TR-1
through TR-5 are complete and shelved (see their DONE entries above/below, unchanged);
everything below was not yet started when the descope landed.

- [ ] **TR-confirm — Two tour interpretations owed.** (1) Confirm "the Representative
      is voice-only." (2) Confirm the standing commitment that evidentiary absence is
      never a locked feature, if tiering is ever revisited. Five-minute decisions;
      (1) directly gated TR-10 before the descope. Not urgent while Tour is Phase 2+.
- [ ] **TR-6 — Asset-sourcing sub-pipeline.** Generalizes the Chloe demo's verified
      public-domain image sourcing and source-text audio scripts into a reusable tool.
      Cross-ref: Marketplace thread's Adopt #6 hands off here.
- [ ] **TR-8 — Confirm the recording pipeline (GIF/slideshow) generalizes per world.**
      Already built once for the map thread; confirm and document for tour use.
- [ ] **TR-7 — Templated tour renderer** (after TR-4). Generalizes the Chloe HTML so a
      world supplies only manifest + assets.
- [ ] **TR-9 — Scene-narration validation probe category** (after TR-4; validation-suite
      thread). No tour ships on conversational validation alone.
- [ ] **TR-10 — House-Churches/Chloe: formalize into a reviewed Tour Manifest** (after
      TR-4 + the TR-confirm gate above). Class A, strongest case, demo already built.
- [ ] **TR-11 — Syriac/Mar Yausep tour: manifest for `syrstory009`** — needs TR-4, TR-6,
      and a 4th-century pronunciation research pass.
- [ ] **TR-12 — Desert/Papnoute tour: manifest for `desertstory008`** (no
      worship-service tour) — needs TR-4, TR-6, TR-11 (sequenced after).
- [ ] **TR-13 — Bethlehem Circle/Albina tour: manifest for `hal_story10`** (no
      liturgical tour) — needs TR-4, TR-6, TR-12 (produce last — newest, least
      live-tested world).
- [ ] **TR-14 — cic-poc integration: `tour_manifest.py`, mode-overlay, invitation card,
      tour view** — needs Increment 1 (budget compliance) and RM-10/Increment 2 (role
      selection); was already scoped never-before/during-P1 pre-descope, now moot since
      Tour isn't part of this build cycle at all.
- [ ] **TR-15 — World Map "Take a tour" handoff** — needs TR-7, TR-14, and Increment 4
      (the map itself has to be merged before it can hand off to a tour). Distinct from
      the World Map's own already-shipped "▶ Watch the flow" self-guided walkthrough,
      which is unaffected by this descope and continues as normal, in-cycle work.

## ✅ DONE

- [x] **UX design CLOSED OUT — zero open decisions remain (2026-07-19).** The two
      standing graphics DRAFTs decided: reading surface = brand warm cream
      (`--gold-wash #FBF2E2`), Era-2 ground = no separate background (one reading surface
      for both eras; the Era-1/Era-2 template distinction is seating/object only). §G
      (Guided onboarding) and §R (question-routing UI) — the storyboard's two never-
      designed screens — approved by Mark. Two Living-Table layout bugs found and fixed
      this session (desktop, then independently on phone): figures and the table line
      were positioned in separate, un-linked coordinate boxes tuned by eye; fixed by
      scene-locking both platforms to one shared coordinate system. A content-integrity
      issue was also found and fixed: invented first-person Representative dialogue in
      the graphics mockups, replaced everywhere with explicitly-labeled placeholder text
      (a standing rule now on record against this recurring). **Produced:**
      `Ministry/Operations/CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` — the
      dependency-ordered path from here to real hosting and Prototype Testing 1,
      separating what's Mark's to decide (stand up hosting — since revised from Bedrock
      to direct-API, per System Hub's own same-day decision — Battery A go-ahead, the 2
      Guided-Questions content calls, the Chloe tour voice read, Section 10, Gantt IDs)
      from what's build-thread execution once those clear.

- [x] **IC-13 — Marius (Church and Empire, sixth live world) icon LOCKED; IC-9 re-run
      across all six (2026-07-22).** Object source-verified against his own Permanent
      Prompt: a leather-strapped scroll-case, not a single letter — his own title is
      "Deacon of the Letters." Dress: plain tunic + orarion (DOCUMENTED for his exact
      312–451 window, Council of Laodicea canon 22); dalmatic considered, held in reserve
      as Rome-specific. Robe: oxblood `#7A2E2E`, the world's own manifest colour. IC-9
      re-run found one real question — his skin/hair reading close to two other icons —
      **resolved on regional grounds (Mark's correction: accuracy to the world's actual
      population, not an engineered spread) rather than nudged for difference's sake.**
      Built: `Brand-Assets/World-Icons/empire.svg`; spec §7e added. Full reasoning:
      `Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`.
- [x] **LT-1 — The Living Table scene redesigned live (mockup phase closed) and its
      first slice built into `cic-poc` (2026-07-22).** Table redesigned to a filled
      roundish table with a thick rim (Mark's call, supersedes spec's old thin-arc
      model); two real bugs found only via built verification tooling (table drawing
      behind the figures instead of over them; the nameplate speaking-state was
      hand-painted per instance, not one real toggleable class). **Real, flagged
      departure from icon spec §7a:** every held object moved off the body onto the
      table surface in front of each figure, per Mark's direct call — not yet
      reconciled in the spec document itself. Phone corner-chip + load-greeting built
      as first passes. Built into the real app: `LivingTableScene.tsx`,
      `worldIcons.tsx`, `BrandMark.tsx`, wired into `TheTable.tsx` + `table.css`;
      `tsc --noEmit` clean, geometry formulas hand-verified against the mockup's own
      tuned values. **Not yet done:** a live visual check inside a real running
      conversation (backend was slow to start, wrongly reported unresponsive
      mid-session — confirmed serving real data on a later check, live check itself
      not yet re-run). Full reasoning, every round:
      `Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`.
      **⚠ Paused 2026-07-23 — see LT-3: the scene's graphics are pulled from the live
      view for now, pending new assets.** This entry's own build work is not undone.
- [x] **LT-2 — World-selector tiles: real ordering bug found and fixed (2026-07-22).**
      Tiles had no sort at all (whatever order the backend happened to return); now
      sorted by each world's own documented start year, extracted from its `period`
      string. Verified against the real six worlds' own manifest data: House-Churches
      (70) → Alexandria (150) → Syriac (200) → Church and Empire (312) → Desert (320)
      → Bethlehem Circle (382) — corrects two dates assumed earlier the same session.
- [x] **LT-3 — Living Table graphics pulled from the live conversation view, pending
      new realistic-portrait assets (2026-07-23).** Mark's direct call: the old flat
      icons "detract from the conversation" — both `<LivingTableScene>` renders
      removed from `TheTable.tsx` (active + closing views); component/data files
      (`LivingTableScene.tsx`, `worldIcons.tsx`, `table.css`) untouched, not deleted.
      `BrandMark`/`ArrivingLockup` (the approved brand mark, separate from the
      Representative icons) left in place — not part of Mark's complaint. Frontend
      compiles clean; a live in-conversation check wasn't possible this round (local
      backend launch config broken, pre-existing/unrelated). **✅ Committed and
      pushed as `bd2a69a` shortly after this entry — confirmed live** (`origin/main`
      matches local HEAD). Full account: System Hub Decision Log, 2026-07-23 (later).
- [x] **LT-4 — Real tile photos + all six Representative portraits wired into the
      live World Selector (2026-07-24).** Six real, license-verified architectural/
      artifact photos (Wikimedia Commons, one per world) sourced to
      `Brand-Assets/World-Media/`; a real catch along the way — two of the first
      six files pulled were correctly-licensed from the right sites but showed the
      wrong content (a marble-fragment close-up, a portrait bust), swapped for
      recognizable views from the same verified categories after actually looking
      at the downloaded images, not just trusting filenames. All six approved
      Representative portraits copied to `public/images/portraits/`. New
      `worldMedia.ts` maps both by real `world_id`; `WorldSelector.tsx`/`table.css`
      render the world photo top-right of the world description and the portrait
      top-right of the representative box, per Mark's design. Verified on a real
      local build at desktop (1400px) and phone (375px) widths — no overlap, no
      overflow. **⚠ Superseded same day — see LT-5: the world photos were pulled
      entirely on a rights question.** Portraits stand; world photos do not.
      Full account: In-App-Icons-Graphics Decision-Log; System Hub Decision Log,
      2026-07-24 (even later).
- [x] **LT-5 — World-media tile photos withdrawn from production on a rights
      question (2026-07-24).** Mark was told 5 of the 6 world photos need
      permission and payment to use — pulled immediately, discrepancy with this
      thread's own CC BY-SA license verification left genuinely unresolved. Real
      production incident, not just cleanup: the photos had already reached
      `main` and were live. Fixed directly on `main` (commit `1caf85e`) — six
      files removed, code un-wired cleanly, portraits untouched, sourcing
      research kept but flagged "do not use." Full account:
      In-App-Icons-Graphics Decision-Log; System Hub Decision Log, 2026-07-24
      (still even later).
- [x] **LT-6 — Homepage's static representative grid upgraded to a real
      interactive carousel; live (2026-07-24).** The pilot-invitation homepage's
      static six-portrait grid (built by a separate thread) is now a
      chronological, era-tinted carousel reading `data/world-census.json` live —
      click any Representative for their tile info, then **"Launch an
      Interview"**, a real link into a free single conversation. Required an
      actual `cic-poc` fix, not just a website change: `WorldSelector.tsx`'s
      documented-but-unused `mode=interview` param now skips the multi-select
      picker entirely for a single-world request, keeping the planned free
      (interview) / paid (multi-table) boundary real rather than just labeled.
      Two bugs caught pre-ship: a census/app world_id mismatch that would have
      404'd one interview link, and a dark-mode contrast bug on card/panel text.
      **Committed, pushed, and confirmed live by direct check** (`cic-poc`:
      `83d058f`; `cic-website`: `3566031`) — deliberately scoped past a large
      amount of unrelated uncommitted work (signed legal/entity documents
      among it) sitting in the shared repo at push time. Full account:
      Website Decision-Log; System Hub Decision Log, 2026-07-24
      (later, cross-thread).
- [x] **IC-9 — Icon full-family review RUN: FAMILY PASSES, the five locks stand
      (2026-07-18, overnight).** Frame/silhouette/objects/flags/skin-spread/template checks
      all green, measured from the masters; two findings fixed in-pass (three in-file lock
      headers aligned; desert's INFERENCE keyword added); three watch items for daylight
      (W1 Chloe cup tone — observation only · W2 Era-2 figures on the live table render ·
      W3 Theon's manifest colour unassigned → World-Map thread).
      `Brand-Assets/CiC_World_Icon_Family_Review_V1_0.md`; spec §7d updated.

- [x] **SB-1..SB-4 — Complete Experience Storyboard shipped + spec-text bug fixed
      (2026-07-18, overnight).** Every path S0→S5 storyboarded (descriptive spine, every
      decided piece cited; five visual frames with build-status flags); the two
      never-designed screens designed — **Guided onboarding** (three Facilitator-hosted
      beats → a prepared table) and the **Question-First Tier-3 routing UI** (held question
      → honest considering → proposal / clarify-once / honest null); **SB-4 fixed same
      night** — `CiC_Full_UX_Design_V1_0.md` swept of stale camera/chip text (V1.0.2), §G/§R
      integrated as states, the Increment-1 handoff bumped to V1.1 (long-form transcript
      §1.3), the icon spec §1b synced. Storyboard:
      `Ministry/Technology/CiC_Full_UX_Storyboard_V1_0.md`; hub hand-off:
      `CiC_UX_Storyboard_System_Hub_Update_2026-07-18.md`. **Mark's morning rulings:
      §G + §R APPROVED; side "other choices" DROPPED** — the journey now has zero
      undesigned and zero unapproved screens. **Still open from it:** SB-5 stale "four
      live worlds" (World-Map thread) · SB-6 Theon tour-eligibility (TR-5) · SB-7 tour
      stop-numbering line · SB-8 "house church" naming gap (world threads) · the
      warm-cream reading surface (DRAFT, graphics pass).

- [x] **IC-1..IC-8 — World Representative icon set: all five built & LOCKED + era-ground
      palette APPROVED (2026-07-18).** One governed connected-bust template (Era-1 style;
      Era-2 = same figure on a different ground). Each object/appearance verified against its
      world's OWN construction record, flagged DOCUMENTED/INFERENCE; anti-anachronism enforced.
      The five: **Chloe** (House-Churches, cup — V1.8, skin warmed to a Greek-East olive) ·
      **Papnoute** (Desert, cracked jug) · **Theon** (Alexandria, open scroll; this world also
      promoted from "example" to live) · **Mar Yausep** (Syriac, one Gospel book; first Era-2) ·
      **Albina** (Bethlehem Circle, wax tablet). Two women, three men, five distinct objects, a
      skin spread by setting. **Era-ground palette APPROVED & canonical:** one warm→cool flow
      across ten eras, light+dark (Era 1 `#EFDDB3`/`#241A0C`, Era 2 `#EDDEB9`/`#221A0E`, …).
      Masters in `Brand-Assets/World-Icons/`; locked bases in `_working-base/`. Spec §7c/§7d +
      §7 palette. Hand-off: `Brand-Assets/CiC_World_Icons_System_Hub_Update_2026-07-18.md`.
      Open follow-ons: IC-9 (family review, DO NOW) and IC-10 (atlas hand-off, READY NEXT).

- [x] **464 — Transcript-logging gap fixed and VERIFIED live (2026-07-17).** Frame-breaker
      and relational-safety branches in both endpoints now call `write_transcript`;
      confirmed live on an isolated backend with a real frame-breaker exchange
      captured correctly.

- [x] **Full UX Design V0.1 — APPROVED by Mark (2026-07-17).** Whole journey drawn,
      desktop+phone, every screen five-count-checked. Visual identity (exact
      palette, Alegreya + Alegreya Sans, madder action accent, typographic
      wordmark), the Level-3 modal→panel fix, and the reflection-beat timing all
      converted from RECOMMENDED to DECIDED. Next: build Increment 1 (see DO NOW).

- [x] **Alexandria — Doc_01 through Doc_09 + full Representative build (Theon) +
      Phase 5 boundary testing, all complete and Mark-approved for integration
      (2026-07-17).** Representative Emergence (Mark's own naming decision),
      Construction Framework Phases 1-4, Permanent Prompt + World Capsule Core, all
      45 Tier-1 lexicon chunks, and boundary testing (RETEST CLEARS, zero hard
      Violation Indicators) all reviewed and cleared. Next: install into `cic-poc`
      (see DO NOW).

- [x] **RM-1..RM-6 — Representative Modes: design + build, self-verified (2026-07-16).**
      Design spec + Chloe four-mode demo, prompt architecture, exploration branch build
      (`claude/representative-modes-exploration`, commit `1127c09`, local-only), live +
      assertion verification in mock-LLM mode (byte-identical no-role baseline), 5-battery
      validation plan authored, integration assessment + decision log. Inert until RM-7
      (Mark's review) and RM-8 (Battery A, the real gate) — see DO NOW / READY NEXT.
- [x] **TR-1..TR-3 — Hosted Tour: strategy, evidentiary analysis, Chloe demo build,
      decision log (2026-07-16).** Self-contained immersive demo of Justin's Sunday
      gathering (`pahcstory006`, Tier 1) — four verified public-domain images, two
      source-text audio readings with transcripts, an honest four-part decline stop.
      Not integrated into `cic-poc`; nothing merged. Demo:
      https://claude.ai/code/artifact/74a8c750-b828-443d-8d8a-e83f038a6eb7
      **Shelved 2026-07-22 — complete and correct as history, but not actively
      continuing.** Mark's direct descope decision moved the whole Hosted Tour feature
      to Phase 2+, out of the current build cycle — see the Phase 2+/DEFERRED section
      above.

---

**Standing rules carried from the Acceleration Plan:** count is the release valve
(Reformation 7 → 5 before any gate bends); if P2 and the build calendar strain, the
build calendar wins; review status is always disclosed honestly; no funder deadline
compresses a gate.
