# Incident & Rollback Runbook

Written 2026-09-21, Tech-Readiness Package 2 (Operations). One page: roll
`live` back, find a session's trace, Bedrock-unreachable, disk-full. Paged:
Mark, always — this is a one-operator project (`PHASE-1-LAUNCH.md`'s own
standing rules).

## Roll back `cic-engine` to its previous deploy

Two mechanisms, verified against Render's own docs
(<https://render.com/docs/rollbacks>), in the order to reach for them:

**A — Dashboard rollback (fastest, minutes).**
1. Render Dashboard → `cic-engine` → Deploys tab.
2. Find the last known-good deploy → click Rollback → confirm on the next
   page.
3. Render redeploys from that build's own artifact — no rebuild, so this is
   fast. **This automatically disables autodeploy for `cic-engine`** — a
   real, confirmed side effect, not a guess. Until autodeploy is manually
   re-enabled (same Deploys tab), a normal merge into `live` will **not**
   redeploy automatically. Do not forget to re-enable it once the incident
   is resolved, or the next legitimate promotion PR will merge and silently
   not deploy.
4. Use this for "something about the latest deploy is actively broken and I
   need it gone right now" — a fast mitigation, not the permanent fix.

**B — Revert the promotion PR (the Promotion Runbook's own documented
method, permanent).**
1. Open a revert PR against `live` for the promotion PR that shipped the bad
   change (`git revert -m 1 <merge-commit>` if it was a merge, or a plain
   revert if not).
2. Mark reviews and merges it, same as any promotion (`live`'s branch
   protection blocks a direct push regardless — Promotion Runbook step 1).
3. This is the actual fix: `live`'s history now reflects the decision, and
   a future clone/rebuild reproduces it. Do this even after using Rollback
   A for immediate relief, so `live`'s git history and Render's active
   deploy agree again — otherwise the next ordinary merge to `live`
   silently re-introduces the bad change once autodeploy is re-enabled.

**When to use which:** A first if participants are actively affected and
minutes matter; B always, eventually, even if A already stopped the bleeding
— A alone leaves `live`'s git history saying something different from what
Render is actually serving.

## Find a session's trace by its identifier

There is no separate "request ID" — the real identifiers are `session_id`
(every event and every usage record) and `trace_id` (one per model call, in
`usage_log` only). A participant report, a log line, or an error message
carries a `session_id` (the app's own logger logs session ids, never
participant or voice text — `engine/api/app.py`'s own logging note).

From a shell with access to the disk (Render Shell/SSH, per the Backup &
Restore Runbook's own connection steps) or from a downloaded backup:

```python
from engine.m4.store import Store
from engine.m8.log_store import UsageLogStore

store = Store("/data/cic_api_events.db")
usage = UsageLogStore("/data/cic_api_usage.db")

for event in store.read_events(session_id="<the session id>"):
    print(event.seq, event.event_type, event.created_at, event.payload)

for record in usage.read_for_session("<the session id>"):
    print(record.trace_id, record.call_kind, record.model_id, record.usage)
```

`store.read_events` returns every event in order (`seq` ascending) — the
full turn-by-turn record including `gate_decision` audit entries.
`usage.read_for_session` returns every model call's `trace_id`, cost inputs,
and `world_key` for that same session, joinable to the event log by
`session_id` if a specific turn's own model call needs isolating (match on
timestamp proximity — `trace_id` and `event_uuid` are independent
identifiers, not a shared key, since M4 and M8 are deliberately separate
stores, per `engine/m8/log_store.py`'s own module docstring).

`/api/admin/pilot-summary` (admin-token-gated) gives aggregate counts without
a shell session, if the question is "how many sessions" rather than "what
happened in this one."

## Bedrock unreachable

**Symptom:** `/health` still answers (it doesn't call Bedrock), but
`create_session`/`message` calls fail or time out; `engine.provider.
bedrock.make_client()`/`resolve_model_id()` raising at import time would
instead crash the whole process on boot (a different, louder failure —
this section is for Bedrock going down *after* a successful boot).

1. **Confirm it's Bedrock, not this service.** Check AWS's own Service
   Health Dashboard for `us-east-1` Bedrock (`render.yaml`'s pinned
   region). A regional Bedrock outage is outside this project's control —
   there is no failover provider wired in (`render.yaml`'s own note: "ALL
   CiC model spend now flows through AWS Bedrock alone").
2. **Check credentials before assuming an outage.** `AWS_ACCESS_KEY_ID`/
   `AWS_SECRET_ACCESS_KEY` are `sync: false` — a credential rotated or
   revoked outside this render.yaml's own tracking (e.g. IAM key rotation,
   an expired session token if the identity ever moves to STS) looks
   identical to an outage from the participant's side. Render Dashboard →
   `cic-engine` → Logs, filter for the Bedrock client's own error — a 403/
   `AccessDenied` is a credential problem, not an outage.
3. **If it's a genuine regional outage:** nothing to do but wait it out and
   communicate — there is no cross-region or cross-provider fallback built.
   Recording this as a real gap, not a task for this pass: **cross-region
   Bedrock failover is out of scope for Package 2** and belongs to a future
   reliability pass if pilot volume ever justifies the added complexity
   (AWS Well-Architected's own reliability tradeoff: redundancy costs real
   engineering and real dollars, and a single-region pilot may reasonably
   accept this risk rather than build for it prematurely).
4. **If it's the safety-model call specifically failing** (not the voice
   model): `engine/m4/turn.py`'s `run_gate()` has its own existing timeout/
   failure semantics (Decision-Log Entry 2's fixed reader-timeout defect) —
   confirm the fix from PR #306 is still in place on `live` (it predates
   this workstream and should never have been reverted) rather than
   assuming a new defect.

## Disk full

**Symptom:** writes to `events.db`/`usage.db` start failing
(`sqlite3.OperationalError`), participants see `invalid session` or a raw
500 on what should be an ordinary turn.

1. **Confirm via Render's disk usage graph** (Dashboard → `cic-engine` →
   Metrics → Disk) before doing anything destructive — a 500 has other
   causes too (see Bedrock section above).
2. **Do not delete `events.db` or `usage.db` directly to free space.** That
   is the exact data this whole tech-readiness package exists to protect.
   If a restore is needed after this incident, the Backup & Restore Runbook
   covers it — but freeing space by deleting the live DB is not a recovery
   step, it's a second incident.
3. **Check `/data/packages-cache`** (`CIC_API_PACKAGE_CACHE_DIR`) first —
   this is the one thing on the disk that is safe to clear: every cached
   package re-fetches from R2 on next request (`engine/m4/package_fetch.py`'s
   own fallback-only design, Object Storage Runbook). Clearing it via Render
   Shell (`rm -rf /data/packages-cache/*`) is reversible and low-risk.
4. **Check `/data/backups-staging`** (this package's own new local staging
   directory, `engine/api/db_backup.py`) — should already be near-empty by
   design (`run_backup_once` deletes its local copy after each upload), so a
   large size here means uploads have been failing silently (check
   `last_run.json`'s own `outcome` field) and the local copies are piling up
   without ever reaching R2. Clearing it is safe (the DBs it copied from are
   still live); fixing the upload failure is the real task.
5. **If neither of those recovers enough space:** the disk itself needs
   resizing. Render Dashboard → `cic-engine` → Disk → Resize — this is a
   dashboard-only, billed action Mark takes; not automatable from here, same
   category as the Object Storage and Promotion runbooks' own one-time
   dashboard steps.
6. **Root-cause afterward, not just relieved:** disk growth with no
   retention/TTL policy (render.yaml's own flagged, not-yet-implemented gap,
   scoped to Package 6/Privacy) will recur. A full disk today is a symptom
   this runbook can only relieve, not fix at the root — that fix is Package
   6's job, named here so it isn't lost.

## Accounts incidents

The accounts feature has one switch, `CIC_ACCOUNTS_ENABLED`. Off, the product is the
codes product exactly, and no account file is touched or deleted. Turning it off is the
first move for any incident below that is not a plain mail outage. Render redeploys on a
settings change.

**A key may have leaked.** Treat a leaked key as an incident even without proof of use.
Switch accounts off first, then rotate that key, then switch on.

| Key | What a holder can do | Rotation |
|---|---|---|
| `CIC_ACCOUNTS_KEY` (address key) | With the account file, test whether a given address has an account | New key as `CIC_ACCOUNTS_KEY` with a new `CIC_ACCOUNTS_KEY_ID`; the old one into `CIC_ACCOUNTS_KEYS_PREVIOUS` as `id:secret`. An account moves to the new key the next time its owner signs in. The log counts accounts still on the old one |
| `CIC_ACCOUNTS_SESSION_KEY` | Forge a session cookie or a sign-in challenge | Replace it. Everyone is signed out. No account is orphaned |
| `CIC_ACCOUNTS_CONTACT_KEY` | With the contact file, read sign-in addresses | New key and id; the old one into `CIC_ACCOUNTS_CONTACT_KEYS_PREVIOUS`. Each address is sealed again at its owner's next sign-in. If the contact file itself also leaked, the addresses in it are exposed whatever the key, and the breach-notice question applies |
| `CIC_ACCOUNTS_SHELF_KEY` | With the account file, open the session codes of saved conversations | New key and id, old one into `CIC_ACCOUNTS_SHELF_KEYS_PREVIOUS` |
| `CIC_ACCOUNTS_BACKUP_KEY` | With a bucket copy, open a sealed accounts backup | New key and id, old one into `CIC_ACCOUNTS_BACKUP_KEYS_PREVIOUS` until the last backup made under it is 14 days old. Backups already in the bucket stay readable by whoever holds the old key until then |
| `CIC_ACCOUNTS_SES_SECRET_ACCESS_KEY` | Send mail as us | Make a new access key for the `cic-accounts-mailer` user in IAM, put it in Render, delete the old one |

Keep the two ids distinct and the secrets different from each other: start-up refuses
a reused one.

**Sign-in mail is down, or SES has suspended sending.** Nobody can sign in who is not
already signed in; the codes product is unaffected. Check the SES account page for a
suspension notice and the reputation dashboard for bounce and complaint rates. Do not
switch accounts off for a mail outage alone.

**Many accounts look farmed, or sign-in is being hammered.** The per-address, per-network
and global send limits answer first; a full global cap pauses sign-in with a plain notice
and ends by itself. If it persists, switch accounts off.

**A restore is needed.** Follow the Backup & Restore Runbook, "The accounts files: sealed
before upload". Restore the durable and contact files from the same pass. At start-up the
app reads the outside copy of the deletion ledger from the backup bucket and removes any
account deleted since the backup. If the bucket cannot be read at that moment the log says
so, and the hourly job tries again; do not switch accounts on for visitors until it has.

**Telling people.** We hold an encrypted address for each account and nothing else that
names anyone. Whether a loss of the contact file needs a breach notice, and to whom, is an
open question for a professional (question 17 of the Go Deeper Decision-Log). Until it is
answered, a suspected loss of the contact file goes to the project lead the same day.

## Who is paged

Mark, always — every path above. This is a one-operator project; there is no
on-call rotation to define.
