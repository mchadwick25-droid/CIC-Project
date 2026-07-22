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
this just adds the exact git-history explanation)._

---

## 🔴 DO NOW (all dependencies clear — priority order)

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
- [ ] **⚠ OPEN, INVESTIGATED 2026-07-20, now TRACEABLE — Content-isolation
      defect in `cic-poc/backend`, real, root cause still NOT established.**
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
- [ ] **101/401 (revised) — Stand up direct-API hosting, session caps, spending limit
      (Jonathan / System Hub).** ⚠ **HELD 2026-07-20 (Mark's direction) — hosting waits
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
- [ ] **NEW — Create Supabase + Render/host accounts (Mark only).** ⚠ **Supabase half
      no longer needed for Pilot 1 specifically as of 2026-07-20** — the simplified pilot
      runs deliberately without sign-in, so `auth.py`/`SignInScreen.tsx`/the Supabase-backed
      `session_cap.py` rework, plus the referral/invite endpoints added the same day
      (`7ea4fa6`, `/api/pilot/request`, `/api/referral/generate`, `/api/referral/redeem`,
      `refer-a-friend.html`), all stay unused rather than configured; skip creating a
      Supabase account unless a later, larger-audience phase wants identity and referral
      tracking back. **The Render/host account is still needed** — that's the real
      remaining blocker inside #101/401's "deploy-and-configure," independent of the
      sign-in question. Original context: the accounts/sign-in layer landed since the
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
      1. **603 — DONE 2026-07-21 — Filed CO Articles of Incorporation.** Faithways
         Studio, Inc. is now a real, incorporated Colorado PBC. **Entity ID
         20261874960, Transaction # 20261874960.**
      2. **624 — DONE 2026-07-21 — EIN obtained from the IRS.**
      3. **625 — DONE 2026-07-21 — Organizational Resolutions signed** by Mark and
         Susan (Bylaws adopted, officers elected, share issuance and bank account
         authorized). Saved: `Faithways_Studio_Bylaws_and_Resolutions_SIGNABLE.pdf`.
      4. **620 — NEXT: Open the corporate bank account and fund $40 founder capital**
         ($20 each from Mark and Susan, referencing "Founder Capital Stock Purchase") — reduced
         from the original $700 (Mark and Susan share only a joint personal account); the
         Organizational Resolutions were corrected and re-signed to match. Waiting on the CO SOS
         business-search record to catch up before finishing the Relay application.
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
- [ ] **TR-confirm — Two tour interpretations owed.** (1) Confirm "the Representative
      is voice-only." (2) Confirm the standing commitment that evidentiary absence is
      never a locked feature, if tiering is ever revisited. Five-minute decisions;
      (1) directly gates TR-10.
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
      treated as final. Unblocks TR-7, TR-9, TR-10.
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
      2026-07-20.
- [ ] **TR-6 — Asset-sourcing sub-pipeline.** Generalizes the Chloe demo's verified
      public-domain image sourcing and source-text audio scripts into a reusable tool.
      Cross-ref: Marketplace thread's Adopt #6 hands off here.
- [ ] **TR-8 — Confirm the recording pipeline (GIF/slideshow) generalizes per world.**
      Already built once for the map thread; confirm and document for tour use.

## 🟡 READY NEXT (starts when the item above it finishes)

- [ ] **RM-8 — Representative Modes validation run, Battery A.** ⚠ **Escalated
      2026-07-19: Mark decided P1 launches with the full feature set, not just the core
      encounter (`CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` V1.2) — this makes
      Battery A the single most schedule-critical action in the whole plan, not just the
      top validation priority.** Increment 2 (role selection) can't merge without it
      passing, Increment 3 can't start without Increment 2, and P1 itself now needs both.
      The feature's existence gate (content-invariance, five arms, blinded claim/
      confidence extraction) — a mode that fails it is a fork of the truth and fails
      outright. Costs live API calls; you schedule it. Start this now, in parallel with
      Increment 1 — not after RM-7.
- [ ] **102 — Run Prototype 1.** Dependency set expanded 2026-07-19 (full-feature-set
      decision, see V1.2 above): direct-API hosting live **and** Increment 1 **and** the
      Tier 0 four **and** RM-8/Battery A passed + Increment 2 merged **and** Increment 3
      merged **and** Hosted Tour **and** Question-First Entry **and** Guided Onboarding
      **and** the Living Table's live wiring — not just hosting alone. Protect this window
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
- [ ] **NEW: landing page copy DRAFTED 2026-07-16 (#704 at 50%)** —
      `Ministry/Communication/CiC_Landing_Page_Copy_V0_1_DRAFT.md`; quote slot waits
      for P1; page build remains.
- [ ] **218 — Weekly quality-upgrade batch** (standing rhythm from Aug 3).
- [ ] **RM-9 — Batteries B–D** (drift / general-mode overclaiming / deconstructing-mode
      adversarial pressure), after RM-8 passes.
- [ ] **TR-7 — Templated tour renderer** (after TR-4). Generalizes the Chloe HTML so a
      world supplies only manifest + assets.
- [ ] **TR-9 — Scene-narration validation probe category** (after TR-4; validation-suite
      thread). No tour ships on conversational validation alone.
- [ ] **TR-10 — House-Churches/Chloe: formalize into a reviewed Tour Manifest** (after
      TR-4 + the TR-confirm gate above). Class A, strongest case, demo already built.
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
| TR-11 | Syriac/Mar Yausep tour: manifest for `syrstory009` | TR-4, TR-6, and a 4th-century pronunciation research pass |
| TR-12 | Desert/Papnoute tour: manifest for `desertstory008` (no worship-service tour) | TR-4, TR-6, TR-11 (sequenced after) |
| TR-13 | Bethlehem Circle/Albina tour: manifest for `hal_story10` (no liturgical tour) | TR-4, TR-6, TR-12 (produce last — newest, least live-tested world) |
| TR-14 | cic-poc integration: `tour_manifest.py`, mode-overlay, invitation card, tour view | Increment 1 (budget compliance) **and** RM-10/Increment 2 (role selection); never before/during P1 |
| Incr. 4 | World Map Tier A merge — owned by front-end thread, never before/during P1 | 402/Increment 3 |
| TR-15 | World Map "Take a tour" handoff | TR-7, TR-14, **and** Increment 4 (the map itself has to be merged before it can hand off to a tour) |
| — | Cross-cutting flag: production TTS/voice + audio hosting decision | not yet scheduled — real cost decision tied to the voice-only ruling |
| — | Cross-cutting flag: image licensing at production scale + zoomable high-res artifacts | not yet scheduled — Marketplace thread's Adopt #6 hands off here |

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

---

**Standing rules carried from the Acceleration Plan:** count is the release valve
(Reformation 7 → 5 before any gate bends); if P2 and the build calendar strain, the
build calendar wins; review status is always disclosed honestly; no funder deadline
compresses a gate.
