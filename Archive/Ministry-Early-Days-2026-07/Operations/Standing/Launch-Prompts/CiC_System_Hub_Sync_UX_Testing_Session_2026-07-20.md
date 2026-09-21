# Launch prompt — sync System Hub on today's parallel UX-testing session

Paste this into the running System Hub thread to bring it up to speed on a separate
session that ran in parallel with the filing-system reorg.

---

You're System Hub, mid filing-system reorg. A separate session ran alongside yours
today — fixed two live bugs, ran real live testing against all five worlds, and built a
feature-status checklist now sitting in your own `Audits/` folder (you already
reconciled one collision with it during the migration, correctly keeping its newer
content). This isn't new work to do — it's context to fold in before you act on
anything that touches the same ground.

**What governs:** standard git-safety protocol — no force-push, no history rewrite,
confirm before anything destructive. Nothing here overrides your reorg's own standing
rules.

**What that session actually did, in order:**
1. **Fixed a crash that broke every message send** (`e596c25`) — `state.closing_stage`
   referenced but never defined, plus two entire missing backend modules
   (`closing_sequence.py`, `modern_term_bridge.py`) lost to the earlier file-loss
   incident. Verified working with real conversations afterward.
2. **Installed and verified Alexandria/Theon live** (`6dbcef1`) — was completely absent
   from the running app despite being reported everywhere as live; all 57 world-data
   files and the manifest entry restored, a real conversation run successfully. (Your
   own later commit `920cc87` — the missing `'theon'` case in `MessageBubble.tsx` — is a
   related follow-up gap in the same area; worth a quick live re-check that Theon's
   nameplate/speaker-info actually renders correctly now, not just that the world loads.)
3. **Found and diagnosed a 100%-reproducible Representative frame-break** — one specific
   curriculum question broke character identically across all 4 tested worlds (0
   citations instead of the usual 3–5, third-person platform-description leaking
   through). Full repro steps and root-cause analysis in
   `Audits/CiC_System_Hub_Handoff_RepresentativeSelfReference_2026-07-19.md`. **Your
   commit `77fc362` ("Fix Representative frame-break: robust to arbitrary question
   phrasing") looks like the fix landing — but nobody has re-run the original repro
   steps against it live yet.** Worth doing before calling this closed.
4. **Ran extensive live testing** — 20 real academic-tier curriculum questions, real API
   calls, across 4 worlds. 19/20 were excellent (honest, well-cited, genuine historical
   nuance volunteered unprompted). Full results in
   `Audits/CiC_UX_Implementation_Status_2026-07-19.md`.
5. **Built the feature-status checklist** now in
   `Audits/CiC_Full_UX_Feature_Checklist_2026-07-20.md` — 89 Program features from the
   Full UX Design spec, each tagged with status (Implemented / Ready for implementation /
   Still needs testing / Still needs design work / No record) **and** two axes Mark asked
   for after seeing the first draft: **Track** (Program vs. Business & Organizational
   Development — Marketplace/Funding/Organization, out of UX-testing scope entirely) and
   **Surface** (Website / App / Both / System). An interactive filterable version is
   published as a Claude Artifact for Mark's own feature-by-feature testing pass, which
   is starting now — expect this file to keep changing as he works through it live.
6. **Wrote a push handoff** (`Standing/Launch-Prompts/CiC_System_Hub2_Push_Thread_Launch_2026-07-20.md`)
   for a "System Hub 2" thread to push local `main` to `origin/main`. **This never ran —
   the repo is now 26 commits ahead of origin, not the 11 that prompt described,** since
   your reorg added 15 more on top. That prompt's specific commit list and the two
   uncommitted-file callouts are now stale; if you're the one pushing, re-verify current
   state rather than trusting that file's snapshot.

**What to do with this:**
- Fold the frame-break re-verification (item 3) and the Theon nameplate check (item 2)
  into your own tracking if they're not already there — don't re-diagnose either, just
  confirm live.
- Treat the checklist (item 5) as the current authoritative Program feature-status
  source, superseding any older status claims in your Task Board for the same features —
  but expect it to be a moving target this session as Mark tests through it.
- Before pushing anything, re-run `git fetch` + `git log origin/main..HEAD --oneline`
  yourself rather than trusting either push prompt's commit count — both are already
  stale relative to each other.
- If your reorg's own Website/App workstream boundaries (the new `Features/Website`,
  `Features/Backend` folders) suggest a correction to the checklist's Surface tags,
  that's worth a note back rather than a silent edit — Mark's actively using that file
  right now.

**Logging:** record whatever you do with this in
`Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, same as the reorg's own
entries.
