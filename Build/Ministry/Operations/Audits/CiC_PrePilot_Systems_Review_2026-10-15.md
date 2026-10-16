# Pre-Pilot Systems Review — 2026-10-15

Scope: the running service's risks and stability before the pilot reopens —
anything that could make it fail, lose data, run up cost, be abused, or be hard
to recover. Out of scope: conversation quality and the safety/Facilitator
protocol. Method: read-only review of the repository (`live` and `main`), with
four parallel read-only investigations. No model calls, no calls to the live
engine. The engine's `/health` could not be reached from the review sandbox.

"Repo" means verified in the code. "Dashboard" means only Mark can check it
(Render, AWS, Cloudflare, GitHub settings, Supabase).

## Findings, most severe first

### 1. Participant data may have no off-server backup — Critical (Repo + Dashboard)
- **What can happen:** every conversation, the cost ledger and the Go Deeper meter live on one 1 GB Render disk. If the disk is lost, all of it is gone.
- **Evidence:** the daily backup uploads only when `CIC_API_BACKUP_BUCKET` is set and otherwise deletes its copy (`engine/api/db_backup.py`, `run_backup_once`). The bucket is hand-set (`render.yaml`, `sync: false`). No record shows it was set up. A "not uploaded" pass logged nothing and alerted no one. The restore was proven only on a laptop (`CiC_Backup_Restore_Runbook.md`, 2026-09-21). The backup copy is written to the same disk. Go Deeper claims and the admin login file are not backed up.
- **Fix:** Mark sets up the bucket. The last backup result is shown and alerted on. One restore drill on staging, recorded.

### 2. Failed deploys are silent — Critical (Repo)
- **What can happen:** a deploy crashes on start-up, Render keeps the old build, and no one knows. This happened three times on 14–15 Oct.
- **Evidence:** no `healthCheckPath` in `render.yaml`. `/health` returned only `{"status": "ok"}`. CI builds the image but never starts it. No post-deploy check. Alerting was mostly spec only (`CiC_Alerting_Runbook.md`).
- **Fix:** `/health` reports its commit; a scheduled check compares it with the head of `live`; Render deploy-failure emails on.

### 3. No hard stop on model spend — Critical (Repo + Dashboard)
- **What can happen:** a script or bug drives Bedrock calls all day with nothing to stop it.
- **Evidence:** the door is `observe: true` (`engine/deeper/ops/go-deeper.yaml`) and narrows nothing in observe. The AWS Budget deny action exists only as `CiC_Model_Spend_Budget_Runbook.md`. A rough worst case from the code's own limits is a few hundred dollars a day per IP address; this is an estimate, not a measurement.
- **Fix:** confirm the AWS Budget deny action is live; a daily dollar breaker in the engine; door to enforce after its observe week.

### 4. Per-visitor caps can be got around — High (Repo)
- **Evidence:** a cookie-less request mints a visitor token seeded from the IP's count at that moment (`engine/api/anon_cap.py`, `mint_seeded_token`). The code documents this as an accepted, bounded gap; a reviewer worked out a much higher bound than the docstring states (not tested). Most limiters key on the full IP, so IPv6 rotation passes them; only Go Deeper groups by /64 (`engine/api/ratelimit.py`). Counts are in memory and reset on restart.
- **Fix:** cap new tokens per IP per day; group limiters by /64. The safety check on capped messages stays as it is.

### 5. A slow Bedrock can freeze the service — High (Repo)
- **Evidence:** the client used SDK default retries (two). A voice call waits up to 90 s per attempt. One server process, no limit on concurrent voice calls; about 40 stuck calls fill the thread pool.
- **Fix:** one retry; at most 16 concurrent voice calls, failing fast through the existing error path.

### 6. Settings in git switch features on before their secrets exist — High (Repo + Dashboard)
- **Evidence:** `render.yaml` sets `CIC_DEEPER_ENABLED: "1"`, which needs `CIC_DEEPER_WEBHOOK_SECRET` and `CIC_DEEPER_FREE_KEY` (`engine/api/deeper_routes.py`, `build_runtime`). Start-up refused at the first missing secret only, so each crash named one. About a dozen settings the code reads are absent from `render.yaml` (for example `CIC_DEEPER_PRODUCTS`), so dashboard-only values cannot be seen from the repo. (`CIC_MODEL_ROUTE` is among them, but the Anthropic route refuses to build on Render, so it cannot redirect production spend.)
- **Fix:** one list of what each switch needs, checked all at once at start-up and against `render.yaml` in CI, plus a pre-promotion checklist.

### 7. Staging no longer tests what runs live — High (Repo)
- **Evidence:** `main` and `live` last shared a commit on 9 Oct (#848); most later merges into `live` came from feature branches (#890–#902). The promotion runbook says `live` moves only by PR from `main`.
- **Fix:** a decision for Mark: reconcile once, then one direction of flow.

### 8. The public site ships from `main` with no gate — High (Dashboard)
- **Evidence:** Workers Builds production branch is `main` (`Build/Ministry/Features/Website-V2/Decision-Log.md`). `npx wrangler deploy` is unpinned. Pushes to `main` do not run CI.
- **Fix:** production branch to `live`, or require green CI; pin wrangler.

### 9. No uptime check or error tracking — Medium (Repo)
Logs go only to Render; request logs are off for privacy; the uptime workflow was never built. Fix: the scheduled check (finding 2) covers uptime; count 5xx responses in-app without IPs.

### 10. The 1 GB disk can fill without warning — Medium (Repo + Dashboard)
No disk check; the usage log is never trimmed; nothing compacts the files; a disk-full write surfaces as `ConcurrentWriteExhausted` (`engine/m4/store.py`). Fix: disk use shown and alerted at 70%; usage-log retention; name disk-full errors truly.

### 11. Everything depends on Mark — Medium (Dashboard)
No account/key inventory, no emergency access. `render.yaml` still describes production as using a dev AWS identity; `IAM-Runbook.md`'s replacement has no record of being done. Admin logins cannot be revoked short of rotating the token. Fix: a private inventory outside the repo with a sealed emergency contact; a narrow production AWS identity.

### 12. Library versions float — Medium (Repo)
Python requirements are minimums only; base images use floating tags; `pytest` ships in the production image; no Dependabot. Fix: hashed lockfile, pinned images, test tools out of the image, Dependabot.

### 13. The pilot could open before it is ready — Medium (Repo)
The only guard was a test pinning every `pilot_open` to false. Fix: an audience cannot open without a questionnaire link.

### 14. Privacy page promises more than is certain — Low (Repo + Dashboard)
`cic-website/privacy.html` says backups go to private storage, true only once the bucket exists, and does not name AWS Bedrock, Render or Cloudflare. The Go Deeper funds table is deleted at 90 days; check against any payment record-keeping rule.

### 15. Smaller items — Low (Repo)
Staging is public with admission off (suspended now). The incident runbook's disk-full step says failed backups pile up locally; they do not. Changing the ops file needs a deploy. The admin password check is limited per IP, not per /64.

## Incidents traced
- **Crashed deploys (14–15 Oct):** findings 2 and 6.
- **`main`/`live` drift:** findings 7 and 8.
- **$0.46/day AWS charge:** the repo shows no RDS or Postgres use. Only the AWS console can settle it.
- **Pilot opened too early:** finding 13.

## Dashboard checks for Mark
- **Render:** `CIC_API_BACKUP_BUCKET*` set on `cic-engine`; deploy-failure email on; dashboard-only settings; disk use; log retention.
- **Cloudflare:** recent files in the R2 backup bucket; Workers production branch.
- **AWS:** Budget with deny action; identity behind the production keys; the daily charge.
- **GitHub:** what the `live` ruleset requires.
- **Supabase:** whether the old pilot project still runs and what it holds.

## Outcome

Mark chose batch A, "stop the silent failures" (findings 1, 2, 5, 6, 13), with these converged choices:
1. Alerts: a scheduled GitHub check every 15 minutes (free: the repository is public), plus Render's deploy emails, which Mark turns on.
2. The backup result is read from public `/health`: uploaded yes/no and when; no names or errors.
3. Bedrock: one retry; at most 16 concurrent voice calls; the safety check still runs first.
4. Secrets: one list per switch, all missing named at once; CI checks it against `render.yaml`; a printed pre-promotion checklist.
5. Pilot: an audience needs a `questionnaire_url` to open.
6. Built on `live` first, ported to `main`. No added cost beyond Claude Code usage.

**Change order, named during implementation:** "failed calls recorded in the usage ledger" is not built. A failed or timed-out Bedrock call returns no token counts, so a ledger row would have to invent them, and the ledger's schema and every reader assume real usage. Failed voice calls are already logged (`provider call failed`, with the reason, including the new `voice capacity full`). Recording them in the ledger needs a schema decision and goes back to Mark.

Not in batch A, still open: findings 3, 4, 7, 8, 9, 10, 11, 12, 14, 15, the backup bucket setup, the restore drill, and the AWS charge.

## Batch B — cost guards (findings 3 and 4)

Converged choices:
1. The door enforces now (`door.observe: false`), ending its observe week early, with the base lowered from $150 to $75 a week until the pilot shows what real use costs. Free voice closes at 95% of the ceiling and all voice at 100%; the safety check is never closed.
2. Visitor tokens are minted only on an allowed session create, never on a message request. One address's tokens then hold at most `limit*(limit-1)/2` sessions beyond its own daily limit (10 at the default of 5).
3. Every rate limiter and the free allowance count an IPv6 connection by its /64 (`engine/api/ratelimit.py`, `network_of`).
4. Dashboard step for Mark: an AWS Budget email alert as the outer backstop (`CiC_Model_Spend_Budget_Runbook.md`).

Still open after batch B: the door counts a week, so a burst can spend much of the week's ceiling in hours before it closes. Daily visitor counts are kept in memory and reset on restart.

## Batch C — the remaining pilot risks

Converged choices:
1. **Messages that are only safety-screened and refused** (a closed conversation, an over-long message, a visitor past the daily cap, a Table round still open) get their own limit of 10 a minute per address (`REFUSED_MESSAGE_LIMIT`). Each message inside the limit is still read by the safety call. Past it, the reply is the existing "please wait" 429, without a safety call, until the minute passes. **Safety-adjacent decision, made by Mark:** a person sending more than 10 messages a minute to a finished conversation sees "wait" for the extra ones; their first messages already brought the Facilitator's redirect. Normal conversation messages keep the 40-a-minute limit.
2. **A daily door limit:** any 24 hours may spend a third of the week's ceiling (`door.daily_share: 0.333`, about $25 at the $75 base). It grows with gifts and purchases as the weekly ceiling does. The door applies whichever of the two limits is nearer. The window is rolling, so a burst late in one day cannot be followed by a fresh allowance at midnight.
3. **Disk use** is on `/health` as a whole percent (`disk_used_percent`); the Live watch check fails at 70%.
4. **Stray whitespace** in the service's own settings (`CIC_`, `AWS_`, `VITE_`) is stripped at start-up and by the backup command, and the names changed are logged, never the values.
5. **Dashboard steps for Mark:** an AWS Budget with a deny action (`CiC_Model_Spend_Budget_Runbook.md`), a GitHub rule requiring CI before merge to `main`, and the site's deploy tool pinned to an exact version in Cloudflare.
