# Launch prompt — System Hub 2: push pending main to origin

Paste this as the opening message to a new "System Hub 2" session/thread.

---

You're System Hub 2. Scope: get `main` pushed to `origin/main` safely — 11 local
commits have piled up unpushed across several separate work threads today, and
nothing has gone to GitHub yet. This is a repo-hygiene task, not a design or content
task: verify, clean up two loose ends, then push.

**What governs:** standard git-safety protocol — no force-push, no history rewrite,
no `git add -A`/`git add .` (name files explicitly), investigate any unfamiliar
untracked state before touching it rather than assuming it's disposable. Confirm with
Mark before the actual `git push` if anything below doesn't resolve cleanly.

**Current-state grounding (verified today, 2026-07-20):**
- `origin` is `https://github.com/mchadwick25-droid/CIC-Project.git`, branch `main`.
- After `git fetch origin main`, local `main` is a **clean fast-forward** — 11 ahead,
  0 behind. No divergence, no merge needed.
- The 11 unpushed commits (oldest → newest): `e596c25` (fix the closing-sequence/
  anachronism-bridge crash), `77fc362` (fix Representative frame-break on arbitrary
  phrasing), `2b86b8b` (reconcile CiC-L1L3-Foundation branch governance work),
  `5a63d80` (fix 37 drifted lexicon chunks, 3 worlds), `6bda85c` (System Hub audit/
  status/handoff artifacts), `6dbcef1` (install World #10, Alexandria/Theon),
  `a04769d` (Imperial-Juridical world-build Step 0–Doc_09), `81db2d8` (UX design/
  storyboard finals + website thread log), `c8d4360` (commit-sweep log), `b9a622e`
  (Imperial-Juridical Step 10 Phase 1–2), `538fdd7` (launch prompt: website stale
  Alexandria status fix).
- **Two uncommitted items, not part of the above, need a decision before pushing:**
  - `World-Builds/Imperial-Juridical-Christianity/Open_Gaps_Tracking.md` — modified,
    unstaged.
  - `World-Builds/Imperial-Juridical-Christianity/Step10_Phase5_Boundary_Testing_Record.md`
    — untracked, new file.
  Both look like legitimate in-progress Imperial-Juridical Step 10 work (matches the
  Phase 1–2 commit already in the log above), not scratch — read them to confirm, then
  commit with a message describing what Step 10 Phase 5 boundary-testing actually
  covers.
  - `.claude/` — untracked. **Do not commit this.** It contains `launch.json`,
    `settings.local.json`, and `.claude/worktrees/`, which holds several *actual,
    currently-registered git worktrees* (`git worktree list` shows some still
    `locked`, tied to separate session sandboxes — e.g. Alexandria build-history
    archive files live in one of them). Committing these would embed nested `.git`
    dirs into the main repo. Add `.claude/` to `.gitignore` instead of staging it. If
    anything inside it looks like real, non-scaffolding human work rather than tool
    state, stop and ask before ignoring it.

**What to produce:**
1. Read the two Imperial-Juridical files, commit them with an accurate message.
2. Add `.claude/` to `.gitignore` (create the file if it doesn't exist), commit that
   separately.
3. Re-run `git status` to confirm the working tree is clean and `main` is still a
   pure fast-forward ahead of `origin/main`.
4. `git push origin main`.
5. Confirm the push succeeded (new `origin/main` SHA matches local `HEAD`) and report
   the final commit count/range now live on GitHub.

**Coordination boundary:** don't touch any other in-flight thread's uncommitted work
beyond the two named files above. Don't rebase, squash, or reorder the 11 commits —
push them as-is. Don't delete anything under `.claude/worktrees/` yourself — ignoring
it in git is sufficient; the worktrees are other sessions' business to clean up.

**Logging:** record the push outcome (timestamp, final SHA, commit count, and the
`.gitignore`/Step-10-file decisions) in `Ministry/Operations/CiC_System_Hub_Decision_Log.md`
per standing convention.
