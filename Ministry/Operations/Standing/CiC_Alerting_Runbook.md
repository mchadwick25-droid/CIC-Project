# Alerting Runbook

Written 2026-09-21, Tech-Readiness Package 2 (Operations). Five signals, what
each one watches, the threshold, where it's configured, and the exact
dashboard steps. Configuration is Mark's own account action in every case
(Render dashboard, AWS Console, or a GitHub secret) — this file specifies
what to set, not a code change that sets it.

Two of the five (health/deploy failure) are natively supported by Render, set
up in five minutes. Three (5xx rate, disk usage, 429 rate) are **not**
natively alertable on Render's current plan — verified, not assumed, against
Render's own docs and community answers (below) — so each gets a
zero-additional-cost design that fits this project's own budget discipline
(`CLAUDE.md`'s usage-discipline section: "the goal is to get everything
possible out of the flat fee").

## 1. Health endpoint failure / deploy failure — Render native, set up now

**What it watches:** `/health` failing during a deploy's own health check,
and a deploy failing outright.

**Threshold:** Render's own default — health check unmet within 15 minutes
of a deploy cancels it and keeps routing to the prior instance
(<https://render.com/docs/health-checks>). Nothing to tune.

**Where configured:** Render Dashboard → Account/Team Settings →
Notifications (workspace-level default), or per-service under that
service's own Settings → Notifications
(<https://render.com/docs/notifications>).

**Dashboard steps:**
1. Render Dashboard → your workspace → Integrations & Notifications.
2. Under Notification Destination, confirm email is on (Slack is optional —
   Connect Slack here if wanted).
3. Under service events, enable "Deploy failed" and "Deploy started/live"
   for both `cic-engine` and `cic-engine-staging`.
4. This is a workspace default; no per-service opt-in needed beyond
   confirming both services aren't individually muted.

This covers deploy-time failures only — it does **not** continuously
uptime-check an already-deployed, healthy-looking service between deploys.
That gap is signal 2.

## 2. Ongoing uptime / health-endpoint failure between deploys

**What it watches:** `/health` responding at all, independent of any deploy.

**Threshold:** two consecutive failed checks (avoids alerting on one
transient blip).

**Why not native:** Render's own health check drives traffic routing and
deploy gating, not a standing, always-on synthetic monitor with its own
alert channel outside a deploy window.

**Where configured:** a free external uptime monitor (e.g. UptimeRobot's
free tier, or a scheduled GitHub Actions workflow reusing this repo's own
existing Actions minutes) hitting `https://cic-engine.onrender.com/health`
every 5 minutes.

**Dashboard steps (GitHub Actions option, zero new account):**
1. New workflow, e.g. `.github/workflows/health-check.yml`, `schedule: cron:
   '*/5 * * * *'`, one step: `curl -f https://cic-engine.onrender.com/health
   || exit 1`.
2. On failure, GitHub already emails the repository owner for a failed
   scheduled workflow run by default (Settings → Notifications →
   Actions) — no extra wiring needed for the alert itself.
3. Repeat with a separate workflow or a matrix entry for
   `cic-engine-staging`'s own `/health`, if staging's uptime matters enough
   to page on — a call for Mark; it's not participant-facing so a lower bar
   is reasonable.

Not built this pass — this is the spec, per the runbook's own scope (item 3
in the tech-readiness brief).

## 3. 5xx error rate

**What it watches:** the fraction of requests to `cic-engine` returning a
5xx status, over a rolling window.

**Threshold:** propose **2 options** for Mark to choose (per this package's
own instruction that Mark sets the real threshold):
- **A — sensitive:** >2% of requests over 10 minutes.
- **B — conservative:** >5% of requests over 15 minutes.
A is the pick if false alarms are cheap and participant experience is the
priority (a pilot with real testers); B if the priority is fewer pages during
a low-traffic pilot phase where a handful of 5xx's could already be >2% of a
small denominator.

**Why not native:** Render's per-service metrics show request/response data
in the dashboard, but native threshold-crossing alerts on a derived rate
(5xx ÷ total) need Render's metrics-streaming (OpenTelemetry export),
documented as a **Pro-plan-and-above** feature
(<https://render.com/docs/metrics-streams>) — not assumed to be on this
project's current plan.

**Where configured (zero-cost option):** the app already logs every request
(`engine/api/app.py`'s own logger, `cic.api`) — Render's own Logs page can be
filtered, but for an actual rate alert, the same GitHub Actions cron from
signal 2 can instead poll a lightweight ops-metrics summary once this
project chooses to expose one (see "Not built this pass" below), or Mark can
use Render's Logs → "Live tail" filtered on `5\d\d` during a known
high-traffic window as a manual check until that exists.

**Dashboard steps (once a metrics summary exists):** same GitHub Actions
pattern as signal 2, polling the new endpoint and comparing against
threshold A or B above.

**Not built this pass:** an endpoint or log-derived counter that actually
computes the 5xx rate. This needs a small addition to `engine/api/app.py`
(a request-count/5xx-count counter, exposed admin-token-gated) — flagged
here as real follow-on work, not silently assumed done, per this project's
own "deferrals documented, never hidden" standard.

## 4. Bedrock spend — AWS Budgets

**What it watches:** actual AWS spend attributable to Bedrock model
invocations (all CiC model spend flows through Bedrock alone since
2026-08-28, per `render.yaml`'s own note — one channel, nothing to
reconcile across providers).

**Threshold:** propose **2 options** for Mark to set:
- **A — early warning:** alert at 50% and 100% of a chosen monthly budget
  figure.
- **B — hard ceiling only:** alert at 100% and 120% (catches a runaway
  after the fact, fewer routine notifications).
Mark picks the dollar figure itself — this runbook proposes the alerting
*shape* (percentage checkpoints), not a number, per PHASE-1-LAUNCH.md's own
"no $/token quoted until invoice-reconciled" rule (spec principle 13):
token counts are locally measurable and already tracked in `usage.db`;
actual dollar cost is Bedrock's own invoice, and Mark is the one who sees it.

**Where configured:** AWS Console → Billing and Cost Management → Budgets
→ Create budget. This is native, real, no extra cost (AWS Budgets alerts are
free).

**Dashboard steps:**
1. AWS Console → Billing → Budgets → Create budget → Cost budget.
2. Scope: filter by Service = Amazon Bedrock (or by the `cic-bedrock-dev`/
   production IAM identity's own cost-allocation tag, if one is set — a
   scoped filter avoids the budget also catching unrelated AWS spend on the
   same account, if any exists).
3. Set the monthly amount (Mark's own figure).
4. Add an alert threshold at each checkpoint from option A or B above,
   Actual (not Forecasted) cost.
5. Notification: email to Mark's own address — SNS topic only needed if a
   Slack/webhook alert is wanted later.

## 5. Render disk usage

**What it watches:** `/data`'s used percentage on the 1GB disk (both
services).

**Threshold:** propose **2 options**:
- **A — early:** alert at 70% used (buys time to act before backups/DB
  growth becomes an outage).
- **B — late:** alert at 90% used (fewer alerts, less runway to react — a
  full disk on a single-instance SQLite service means writes start failing).

**Why not native:** Render's dashboard shows a disk-usage graph per service,
but a metrics-streaming alert on it is the same Pro-plan gate as signal 3
(<https://render.com/docs/metrics-streams>); community discussion confirms
no native email/Slack alert exists for disk usage on lower plans
(<https://community.render.com/t/alerts-on-disk-usage/3796>).

**Where configured (zero-cost option):** Render's own API exposes disk usage
directly — `GET /v1/metrics/disk-usage`
(<https://api-docs.render.com/reference/get-disk-usage>) — callable with a
Render API key. The same GitHub Actions cron as signal 2 can poll this
endpoint and compare against threshold A or B.

**Dashboard steps:**
1. Render Dashboard → Account Settings → API Keys → create a read-scoped
   key.
2. Store it as a GitHub Actions secret (`RENDER_API_KEY`) in this repo.
3. Scheduled workflow (e.g. daily, since disk fills slowly compared to a
   5xx spike) calls `GET https://api.render.com/v1/metrics/disk-usage?
   resourceId=<cic-engine's service id>` and fails the job (triggering
   GitHub's own failed-workflow email) if usage crosses threshold A or B.

**Not built this pass:** the actual workflow file. Specified here, not
implemented — this package's scope is the spec and the dashboard steps
Mark takes; wiring a new CI workflow is a small, separate, low-risk follow-on
(flagged, not hidden).

## 6. Rate-limiter 429 rate

**What it watches:** the fraction of requests `engine/api/ratelimit.py`
rejects with 429, over a rolling window — a proxy for either a real abuse
pattern or the limiter's own threshold being miscalibrated against real
pilot traffic.

**Threshold:** propose **2 options**:
- **A — sensitive:** >5% of requests 429'd over 10 minutes (catches the
  limiter biting real participants early).
- **B — conservative:** >15% over 15 minutes (only pages on a sustained
  pattern, not one bursty participant).

**Where configured / dashboard steps:** identical shape to signal 3 (5xx
rate) — same missing piece (no per-derived-rate native alert without
Pro-tier metrics streaming), same proposed fix (an admin-token-gated
counter exposed by the app, polled by the same GitHub Actions cron already
proposed for signals 2/3/5, one scheduled job checking several thresholds
rather than four separate jobs).

**Not built this pass**, same reasoning as signal 3.

## Summary table

| # | Signal | Threshold options | Config surface | Built this pass? |
|---|---|---|---|---|
| 1 | Deploy/health-check failure | Render default (15 min) | Render Notifications | Yes — dashboard steps only, no code |
| 2 | Ongoing `/health` uptime | 2 consecutive failures | External cron (GitHub Actions) | Spec only |
| 3 | 5xx rate | A: >2%/10min · B: >5%/15min | Needs a metrics endpoint + cron | Spec only, endpoint not built |
| 4 | Bedrock spend | A: 50%/100% · B: 100%/120% | AWS Budgets (native, free) | Yes — dashboard steps only |
| 5 | Render disk usage | A: 70% · B: 90% | Render API + cron | Spec only, workflow not built |
| 6 | 429 rate | A: >5%/10min · B: >15%/15min | Same metrics endpoint as #3 | Spec only |

Three of six (1, 4, and half of 2) are ready for Mark to turn on today with
no further engineering. The other three name the exact missing piece (a
small ops-metrics endpoint, and the cron workflows that poll it) as real,
scoped follow-on work — not silently assumed built.
