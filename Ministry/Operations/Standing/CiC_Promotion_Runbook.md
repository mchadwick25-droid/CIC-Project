# Promotion Runbook — `main` → `live`

D3's promotion model (`CiC_Repo_Structure_Tracking.md`, Decisions 2026-09-14; executed
phase 3, 2026-09-15): `main` is the integration sandbox — every merge deploys to
`cic-engine-staging`. `live` is the protected branch production actually deploys from.
Nothing reaches participants without a deliberate, logged promotion through this file's
own procedure. `render.yaml` carries the two services; this file carries the process
around them.

## What this replaces

Before phase 3, `main` deployed straight to the one production service. Every PR merge
this project has run so far — code, records, docs — went live the moment it merged.
**That stops here.** From this point on, merging to `main` only reaches staging. Reaching
participants requires the promotion step below, every time.

## One-time setup (Mark's own dashboard actions — not executable from a build thread)

None of the four steps below can be done from this sandbox: Render and GitHub's branch-
protection settings are both dashboard-only, and Render's own API is unreachable from
here (egress-blocked, confirmed 2026-09-15).

1. **GitHub — protect `live`.** Settings → Branches → Add rule → branch name pattern
   `live`. Require a pull request before merging (0 required approvals is fine — a
   solo-operator promotion is still logged and reviewable, just not blocked on a second
   person). Disallow force pushes. Disallow deletions. The `live` branch already exists,
   created at `main`'s tip the same day this file was written — zero drift at creation.
2. **Render — sync the Blueprint.** Dashboard → the `cic-engine` Blueprint → Sync. This
   is what actually creates `cic-engine-staging` from `render.yaml`'s new second service
   entry, and picks up `cic-engine`'s new `branch: live` pin.
3. **Render — set `cic-engine-staging`'s secrets.** Same three `sync: false` keys as
   prod (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `CIC_API_ADMIN_TOKEN`), but their
   own values — never prod's. A scoped, separate AWS identity is worth setting up here
   rather than reusing prod's; nothing about staging needs prod's own blast radius.
4. **Confirm the real cost.** `cic-engine-staging` is pinned to Render's `starter` plan
   in `render.yaml` (cheaper than prod's `standard`) precisely because it never carries
   real participant load — reduce further or pause it between verification passes if the
   monthly cost isn't worth carrying continuously.

Until these four are done, `render.yaml`'s new service and `branch:` pins describe the
intended state, not the live one — `cic-engine` keeps deploying from whatever branch
Render's dashboard already has it connected to (almost certainly still `main`) until
step 2 actually flips it.

## The promotion procedure itself (every time, once set up)

1. Verify on staging first. `cic-engine-staging` already has `main`'s latest — read it,
   run whatever check the change calls for, on the real running service, not just CI.
2. Open a PR from `main` into `live`. Title it plainly ("Promote: <one-line summary of
   what's shipping>"). The diff is the promotion's own record — no separate log entry
   needed, the PR itself is the deliberate, logged act D3 asks for.
3. Mark reviews and merges it himself. This is the verification step D3 names — not a
   formality, the actual gate between staging and participants.
4. Render deploys `cic-engine` from the new `live` tip automatically on merge, the same
   way `main` always deployed to prod before this file existed.
5. Rollback, if ever needed: revert the promotion PR (a normal `git revert` PR into
   `live`, reviewed the same way) rather than force-pushing or hand-editing `live`
   directly — `live`'s branch protection (setup step 1) blocks a direct push regardless.

## What does not go through this

`cic-website` (the public site, Atlas) deploys via Cloudflare Workers Build, a separate
pipeline this runbook does not touch. Cloudflare already builds a preview per branch
(D3's own text notes this). Its *production* deployment stays on `main`, not `live` —
settled, not an open question: Mark tracks `live` as the deliberate, reviewed signal for
what has actually shipped; Cloudflare tracking `main` directly is how the public site
stays current in the background without needing its own promotion step (Mark, 2026-09-20).
