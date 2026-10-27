# Backup & Restore Runbook — events.db / usage.db

Written 2026-09-21, Tech-Readiness Package 2 (Operations). Covers the two SQLite
stores on `cic-engine`'s and `cic-engine-staging`'s Render Disks:
`CIC_API_EVENTS_DB` (`engine.m4.store.Store` — session transcripts, gate
decisions) and `CIC_API_USAGE_DB` (`engine.m8.log_store.UsageLogStore` — the
cost ledger). The mechanism is `engine/api/db_backup.py`; this file is the
procedure and the numbers around it. `render.yaml`'s own top-of-file note
carries the short version and the env var names.

## Why this exists, plainly

`render.yaml` already says the disk was scheduled "WITH persistence, not
after it," but a disk is not a backup — it is the one and only copy today.
Losing that disk (Render incident, accidental resize/detach, a bad manual
edit inside the container) loses every transcript and every cost record with
nothing to restore from. This closes that gap.

## Why in-process, not a Render Cron Job — verified, not guessed

Confirmed against Render's own documentation
(<https://render.com/docs/disks>): a Persistent Disk attaches to exactly one
running service, and neither a Cron Job nor a one-off Job can reach a disk
already attached elsewhere — both run on separate compute. `engine/m7/
scheduler.py` (the daily audit) and `engine/m4/idle_close.py` (the idle-close
sweep) already hit this exact wall and both resolved it the same way: a
daemon thread inside `cic-engine`'s own process, started in `engine/api/
app.py`'s `_build_real_app()`. `engine/api/db_backup.py`'s
`start_background_scheduler` is a third sibling of that same pattern — see
its own module docstring for the full reasoning. No new Render service is
created by this runbook; there is nothing to add in the Render dashboard for
the schedule itself.

## Why the online backup API, not `cp`/`scp` of the `.db` file

Both stores run with `PRAGMA journal_mode=WAL`. A live writer's committed
data can be sitting in the `-wal` file rather than the main `.db` file at any
given moment; copying only the main file (or copying while a write is
mid-flight) can silently produce a torn, unusable backup. `sqlite3.
Connection.backup()` — the "online backup API" — is built exactly for this:
safe against a concurrent writer, no lock that would block a participant's
turn. `engine/api/db_backup.py`'s `backup_one()` uses it exclusively; a
proof that this actually survives a live uncommitted writer is one of the
unit tests below.

## One-time setup — Mark's own dashboard actions, same as the Object Storage Runbook

Not executable from this sandbox (same egress-blocked restriction the
Object Storage and Promotion runbooks already document).

1. **Create a second R2 bucket**, separate from the packages bucket
   (`CIC_API_PACKAGE_BUCKET`). Cloudflare dashboard → R2 → Create bucket.
   Name it something stable, e.g. `cic-db-backups` — nothing in code assumes
   a name, it just has to match step 3. **Do not reuse the packages
   bucket**: these backups carry real participant transcripts and usage
   records, a different sensitivity class from compiled, public-ish world
   packages, and reusing the credential would widen its blast radius for no
   benefit.
2. **Generate an API token scoped to that bucket** — R2 → Manage API Tokens
   → Create API Token, Object Read & Write, scoped to the one bucket. This
   produces an Access Key ID, a Secret Access Key, and the account's R2
   endpoint.
3. **Set four env vars on `cic-engine`** (`render.yaml` already declares all
   four `sync: false`, so they show up in the Render dashboard ready to
   fill in): `CIC_API_BACKUP_BUCKET`, `CIC_API_BACKUP_BUCKET_ENDPOINT`,
   `CIC_API_BACKUP_BUCKET_ACCESS_KEY_ID`, `CIC_API_BACKUP_BUCKET_SECRET_ACCESS_KEY`.
4. **Repeat step 1–3 for `cic-engine-staging`, with its own second bucket**
   (e.g. `cic-db-backups-staging`) and its own token — deliberately not
   shared with prod, unlike the packages bucket. Staging's `events.db` is
   synthetic verification traffic; there is no legitimate reason for a
   staging credential to read or write into prod's backup history. See
   `render.yaml`'s own comment on this service's env vars for the same
   reasoning applied to its existing AWS credentials.
5. **Confirm the free tier is enough.** Same math as the Object Storage
   Runbook: the events/usage DBs are well under 1GB combined today, one
   daily snapshot of each, 14 days retained (`db_backup.py`'s
   `_DEFAULT_RETENTION_DAYS`) — worth a glance at R2's usage page after the
   first two weeks rather than assumed forever.

Until step 3 is done on a given service, that service's daily backup thread
still runs, still verifies each backup's integrity — it just discards the
verified copy locally instead of uploading it (`db_backup.run_backup_once`'s
`"backed_up_not_uploaded"` outcome, logged to `/data/backups-staging/
last_run.json`). **A backup that never leaves the disk it backs up protects
against nothing** — step 3 is not optional, it is the entire point.

## Normal operation, once set up

Nothing to run by hand. The daily thread (started alongside the M7 audit and
idle-close threads in `_build_real_app()`) runs once a day, backs up both
DBs, verifies each with `PRAGMA integrity_check`, uploads to
`db-backups/<service>/<events|usage>/<timestamp>.db` in the service's own
bucket, and prunes objects older than 14 days. Its last outcome is on disk at
`/data/backups-staging/last_run.json` (readable via `render ssh`, below).
The public `/health` route reports two facts from it: whether every database
the last pass found reached the bucket (`backup.uploaded`), and when that pass
ran (`backup.last_run_at`). It shows no names, keys or errors. A pass that
backs up without uploading also logs a warning. The Live watch workflow
(`.github/workflows/live-watch.yml`) reads `/health` every 15 minutes and
fails, emailing you, when the last pass did not upload or is more than 26
hours old. Until the one-time setup above is done it fails on every run: that
is the alert doing its job.

To check on it or list what's backed up, from a local checkout with the R2
credentials exported:

```
python -m engine.api.db_backup list events --service-label cic-engine
python -m engine.api.db_backup list usage --service-label cic-engine
python -m engine.api.db_backup list meter --service-label cic-engine
```

When Go Deeper is switched on, its meter file (`/data/cic_deeper_meter.db`) joins the daily pass under the `meter` label, and restores the same way (`--target /data/cic_deeper_meter.db`). Its claim file (`/data/cic_deeper_claims.db`) is never backed up: it holds plain codes for one hour.

## Restore procedure

Restoring means replacing a live DB file while the one process that opens it
(`cic-engine`) is running — `engine/api/db_backup.py`'s `restore_one()` does
an atomic file replace, but atomic-from-the-filesystem's point of view is
not the same as safe-from-a-live-writer's point of view for a WAL-mode
SQLite file. Suspend writes first.

1. **Suspend the service.** Render dashboard → `cic-engine` → Manual Deploy
   menu → Suspend (or scale to zero if the plan supports it). This is a
   real, visible outage for participants — restoring is a deliberate,
   announced action, not a background one.
2. **Connect to the service's Shell** (Render dashboard → `cic-engine` →
   Shell tab, or `ssh <service>@ssh.<region>.render.com` per
   <https://render.com/docs/ssh> — this connects into the actual running
   container, with the disk mounted, unlike a Cron/one-off Job). If the
   service is fully suspended rather than just stopped from serving traffic,
   use a one-off Shell session against the same service instead — either
   way, the goal is a shell with `/data` mounted and no `uvicorn` process
   currently writing to the DB you're restoring.
3. **Restore the DB(s) you need**, from inside that shell:
   ```
   python -m engine.api.db_backup restore \
     --from-key db-backups/cic-engine/events/<timestamp>.db \
     --target /data/cic_api_events.db
   ```
   (repeat for `usage` / `/data/cic_api_usage.db` if needed). This
   downloads the object, verifies its integrity, verifies the local copy's
   integrity again after the copy, deletes any stale `-wal`/`-shm` files
   next to the target, then atomically replaces it. It refuses (raises
   `BackupIntegrityError`, target untouched) rather than restoring a
   corrupted or partial download.
4. **Resume the service.** Render dashboard → Resume / redeploy.
5. **Verify.** Hit `/health`, then read back a known session
   (`/api/session/<id>/transcript` with its own session code, or
   `/api/admin/pilot-summary` for aggregate counts) and confirm the data
   looks like the backup's own timestamp, not older or missing.

## RPO / RTO

**RPO: up to 24 hours.** The backup runs once daily; the worst case is disk
loss one minute before the next scheduled run, which loses everything
written since the prior day's backup. This is a stated tradeoff, not an
oversight: this is a solo-operator, budget-conscious pilot (`CLAUDE.md`'s own
usage-discipline section) with a 1GB disk and no current requirement to
recover the last few minutes of conversation after a disk-loss event —
losing up to a day of pilot transcripts is a real but bounded cost, not the
kind of financial-transaction loss that would justify continuous
replication. If real participant volume or funding-readiness review later
demands a tighter RPO, the fix is a shorter backup interval (the scheduler's
`_DEFAULT_HOUR`/`_DEFAULT_MINUTE` constants, or running it more than once a
day), not a redesign.

**RTO: estimated 30–60 minutes for a practiced operator; not yet measured
against the real Render dashboard.** Breakdown: suspend the service (~2
min, dashboard), connect via Shell/SSH (~2–5 min, first time slower), run
the restore command (~1–2 min for DBs this size, per the local proof below),
resume and verify (~5–10 min including redeploy). This estimate follows
`PHASE-1-LAUNCH.md`'s own "measured, not asserted" rule as far as this
sandbox can: every step's mechanism (Shell/SSH, Suspend/Resume, the restore
command itself) is verified real and the restore command's own timing is
measured locally below, but the sandbox cannot reach the production disk
(same restriction the Promotion and Object Storage runbooks already state),
so the end-to-end dashboard sequence has not been run for real. **A live
restore drill against `cic-engine-staging` — which carries no real
participant data, so nothing is put at risk — is the natural first real
measurement**, and should replace this estimate once run.

## Restore proven locally, row-for-row

Run against the real store classes (`engine.m4.store.Store`,
`engine.m8.log_store.UsageLogStore`), not a toy schema, 2026-09-21:

```
BEFORE: 8 events across 2 sessions, 4 usage rows
BACKUP: wrote /tmp/restore-proof/backups/events-backup.db (16384B), /tmp/restore-proof/backups/usage-backup.db (12288B)
DESTROYED: live events.db deleted, live usage.db overwritten with garbage
RESTORED: both DBs replaced from their online backups
VERIFIED: 8 events row-for-row identical, 4 usage rows row-for-row identical
RESULT: PASS
```

Steps taken: wrote 8 events across two sessions and 4 usage records through
the real `Store.append`/`UsageLogStore.append` APIs; backed up both with
`db_backup.backup_one`; deleted the live events DB outright and overwrote
the live usage DB with garbage bytes (simulating disk corruption, not just a
clean restart); restored both from their backups with `db_backup.
restore_one`; re-read both through `Store.read_events`/`UsageLogStore.
read_all` and asserted equality against the pre-destruction reads. Also
covered by `engine/api/tests/test_db_backup.py` (10 tests, all passing),
including a dedicated case (`test_backup_one_survives_a_live_wal_writer`)
that holds a second connection open with an uncommitted write while the
backup runs, proving the online-backup-vs-file-copy distinction this runbook
argues for above rather than just asserting it.

## First production upload and restore drill, 2026-10-16

Run by Mark in the `cic-engine` Shell. No model calls.

- **Upload:** the first manual `backup` pass sent all three databases to `cic-db-backups` (events 6,287,360 bytes, usage 208,896, meter 45,056). `/health` then showed `"uploaded": true`.
- **Drill:** each newest object was downloaded with `restore --from-key` into a scratch folder (`/tmp/drill`), never over a live file. Every download passed `integrity_check` twice (on download and on copy).
- **Row counts, backup against live:** `session_events` 1503 / 1503; `usage_log` 535 / 535; meter `daily` 6 / 6, `free_window` 1 / 1, `state` 1 / 1, and `funds`, `meter`, `pilot_joined`, `reconcile`, `voided_payments` 0 / 0. No table missing on either side.
- **Why production, not staging:** resuming `cic-engine-staging` costs money, and a restore into a scratch path reads the bucket without touching the live databases.
- **Not yet run for real:** the full sequence above (suspend, overwrite the live files, resume). The RTO estimate stays an estimate until that runs.

## The accounts files: sealed before upload

With `CIC_ACCOUNTS_ENABLED` on, the daily pass also backs up two accounts files:
the durable file (`cic_accounts.db`: accounts, linked sign-ins, shelf, codes, the
deletion ledger) and the contact file (`cic_accounts_contact.db`: sign-in
addresses, already encrypted under the contact key). The ephemeral file
(sign-in challenges, sessions) is never backed up.

Each is sealed with AES-256-GCM before it leaves the disk, under
`CIC_ACCOUNTS_BACKUP_KEY` (its own key, at least 32 characters, different from
the address, session, contact and shelf keys, with an id from
`CIC_ACCOUNTS_BACKUP_KEY_ID`, default `b1`). A bucket copy alone reads nothing.
The object ends `.db.enc`; it lives beside the plain backups under
`db-backups/<service>/accounts/` and `.../contact/`, and is pruned at the same
14 days. With the flag on, the app refuses to start without the backup key and
without `CIC_API_BACKUP_BUCKET`. A sealed file is never uploaded without a key.

**Key custody.** Keep one offline copy of the backup key, held by two people.
Without the key a sealed backup cannot be opened by anyone, including us.

**Rotating the key.** Set the new key as `CIC_ACCOUNTS_BACKUP_KEY` with a new id
(`b2`), and move the old one to `CIC_ACCOUNTS_BACKUP_KEYS_PREVIOUS` as
`b1:<secret>`. Backups made under the old key still open. Remove the old key
only after the last backup made under it has aged out (14 days).

**Restoring a sealed file.** Stop the writer first, as for any restore. In the
container's shell:

```
python -m engine.api.db_backup list accounts
python -m engine.api.db_backup restore --sealed-label accounts \
  --from-key db-backups/cic-engine/accounts/<stamp>.db.enc --target /data/cic_accounts.db
```

Use `contact` for the contact file. The label must match the file: a backup
opens only under its own label and key, and a wrong one changes nothing. The
plain copy exists beside the target only for the length of the restore.
Restoring the durable file and the contact file from different days leaves some
accounts without a stored address; restore both from the same pass.

**Deleted accounts do not come back.** The deletion ledger sits inside the durable file,
so a backup made before a deletion has no record of it. Each ledger entry is therefore
also written to the backup bucket when the account is deleted, under
`db-backups/cic-engine/ledger/<expiry day>_<ledger hash>`. The object is empty; the
name is the hash of the account's random internal id and the day it expires (16 days
after deletion, two days past the backups). If the bucket is unreachable at that moment
the entry waits in the file and the hourly job sends it. At start-up and every hour the
app reads these entries back and removes any account they name. After a restore, check
the log for "accounts named by the deletion ledger were found again and removed".

**Closed accounts stay closed.** Deleting an account closes it for 90 days (Decision-Log
ruling 108); the account row stays and a `closures` row holds the closing day and the day
it will be erased. A backup made before the closing shows the account open, so each closing
is also written to the bucket as an empty object under
`db-backups/cic-engine/closed/<erase day>_<ledger hash>`, the same hash as the deletion
ledger. At start-up and every hour the app reads these back and closes any account they
name that the file shows open. Re-opening removes the object first, so a restore leaves a
re-opened account open; if the bucket refuses, the account stays closed and the person asks
for a new code. The object is pruned the day after its erase day, when the deletion ledger
takes over. A backup made before a re-open brings the closure back with it: the bucket object
is gone, but the restored file shows the account closed, so the account is erased on its last
day unless the person signs in again and re-opens it. This is a documented choice, not a gap.
After a restore, check the log for "closed accounts found open again in a
restored file were closed".

**Erased conversations do not come back either.** The record of an erased conversation (a
keyed hash of its id and the review tokens that find its review rows) also sits in the
durable file, so a restore of the events file and the accounts file from before an
erasure would bring the conversation back. Each erasure is therefore also written to the
bucket, sealed under the backup key, under `db-backups/cic-engine/erased/<expiry day>_<hash>`.
The name holds no conversation id. At start-up and every hour the app reads these back and
the hourly job erases again any conversation in the log that they name, with its review
rows. An entry that cannot be opened (for example, sealed under a key that is no longer
listed) is skipped and logged without detail. Keep the previous backup key listed for 16
days after a rotation, not 14, so these entries still open.

## What this does not cover

- **Point-in-time recovery finer than 24 hours.** See RPO above.
- **`packages/` or `records/`.** Those are git-tracked and rebuild
  deterministically (`engine/BASELINES.md`'s own manifest-hash discipline);
  they were never in scope for this runbook.
- **Retention/TTL of the DBs' own content** (deleting old sessions,
  `deletion_requested` handling). `render.yaml`'s own comment flags this as
  scheduled-but-not-yet-implemented; it belongs to Package 6 (Privacy), not
  this one — backing up data and deciding how long to keep it are separate
  questions, and this runbook only answers the first.
