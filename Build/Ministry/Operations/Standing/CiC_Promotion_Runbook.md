# Promotion Runbook — `main` → `live`

**Reviewed 2026-09-21 (Tech-Readiness Package 2, Operations):** checked
against today's `render.yaml` and `README.md` — still current, no drift
found. The one-time setup section below (GitHub branch protection, Blueprint
sync, staging secrets) could not be re-verified as *done* from this sandbox
(Render/GitHub dashboard state isn't readable here, same egress restriction
this file already names); it is left exactly as this runbook already stated
it rather than asserted complete without evidence.

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
2. Run the admission gate on a named, capped run. Admission conformance is a
   promotion gate, not a merge gate (decision 58): in CI it only reports. Before
   the promotion PR opens, Mark approves one named, capped admission run under
   decision 56 (started as described under "A named, capped run" below), for the whole fleet or for the worlds
   the report lists as stale; its reports are committed on `main`; then
   `python -m engine.m3.admission_conform --enforce` must exit 0.
3. Confirm the hand-set secrets. Run `python -m engine.api.required_secrets --service cic-engine`
   on the branch being promoted. It prints every `sync: false` value in `render.yaml` for
   production, with the ones the engine cannot start without listed first. Tick each one off
   in Render → `cic-engine` → Environment. A value declared in `render.yaml` is not thereby
   set. The command exits 1 if `render.yaml` itself turns a switch on without declaring
   what that switch needs.
4. Open a PR from `main` into `live`. Title it plainly ("Promote: <one-line summary of
   what's shipping>"). The diff is the promotion's own record — no separate log entry
   needed, the PR itself is the deliberate, logged act D3 asks for.
5. Mark reviews and merges it himself. This is the verification step D3 names — not a
   formality, the actual gate between staging and participants.
6. Render deploys `cic-engine` from the new `live` tip automatically on merge, the same
   way `main` always deployed to prod before this file existed. Confirm it went live:
   `https://cic-engine.onrender.com/health` reports the commit it runs, and it should be
   the new `live` tip. The Live watch workflow (`.github/workflows/live-watch.yml`) checks
   the same thing every 15 minutes and fails, emailing you, if an older build is still
   serving 30 minutes after the merge.
7. Rollback, if ever needed: revert the promotion PR (a normal `git revert` PR into
   `live`, reviewed the same way) rather than force-pushing or hand-editing `live`
   directly — `live`'s branch protection (setup step 1) blocks a direct push regardless.

## A named, capped run (decision 56)

The engine refuses any model call outside a conversation unless the command carries
both `--live-test "<name>"` and `--cap-usd <dollars>`; without them it prints the rule
and exits before a client exists. To get one:

1. The thread that needs a run stops and asks Mark in the conversation, giving the
   command, what it will measure, the models and the route (Bedrock regional or global
   profile, or the Anthropic API), and a proposed cap. With the ask, the thread writes
   three things it has checked in this session, not recalled from memory or a log:
   what the harness keeps if the run stops early, shown by running its tests or a dry
   run here (the admission run keeps every completed world and writes its report
   after each one since pull request 998; the live-turn run keeps the turns already
   paid for); the cap's margin over the run's real cost, read from the latest ledger
   or report for the same worlds and model, since the preflight estimate ran a third
   under the real cost on 20 October; and that the output goes to a file and the
   ledger path is set. A run started without that record is a breach, logged in the
   System Hub Decision Log and named to the thread, whatever it cost.
2. Mark approves it by name with a dollar cap, once. The approval is logged in the
   System Hub Decision Log before the run starts, so the monthly reconciliation can
   match each charge to it.
3. The run starts from the live-tests environment, for example
   `python -m engine.m3.live_admission_run --live-test "<name>" --cap-usd <n> ...` plus
   the command's own arguments. Before its first call it prints the name, the cap,
   every model id and the route. Check that print against the approval.
4. It stops before any call that could carry the priced total past the cap, and writes
   the name into every usage record. Every call is also appended to a ledger file
   (`CIC_LIVE_TEST_LEDGER`, else `cic-live-test-ledger.jsonl` in the temp directory; the
   header prints its path): a `hold` line before the call and a `settle` line with the
   priced usage after it. A call is refused if the ledger cannot be written. Run the
   command with its output going to a file, never into a pipe that can close, and keep
   the ledger when the session ends. A live-turn report carries the name, cap, route,
   priced total and per-call usage, and the admin dashboard lists it under named live
   tests as internal.

Test conversations on the live engine are conversations and need no flags.

## What does not go through this

`cic-website` (the public site, Atlas) deploys via Cloudflare Workers Build, a separate
pipeline this runbook does not touch. Cloudflare already builds a preview per branch
(D3's own text notes this). Its *production* deployment stays on `main`, not `live` —
settled, not an open question: Mark tracks `live` as the deliberate, reviewed signal for
what has actually shipped; Cloudflare tracking `main` directly is how the public site
stays current in the background without needing its own promotion step (Mark, 2026-09-20).
