# Object Storage Runbook — compiled packages on Cloudflare R2

**Reviewed 2026-09-21 (Tech-Readiness Package 2, Operations):** checked
against today's `render.yaml` — still current, no drift found. See the new
sibling `CiC_Backup_Restore_Runbook.md` for a **separate** R2 bucket setup
(DB backups) that this runbook's own "same bucket, both services" reasoning
deliberately does not extend to — different data sensitivity, own writeup.

WO-1 (`CiC_Repo_Structure_Tracking.md`; Artifact-2 SS5: "Packages are built by CI, uploaded
to object storage... and referenced by the registry"). Mark's provider choice, 2026-09-16:
Cloudflare R2 - same account `cic-website` already uses, S3-API-compatible, no egress fees,
and the real fleet-wide package total (13MB across 10 worlds, measured the same day) sits
entirely inside R2's free 10GB tier.

**What this buys:** installing or updating a world today means a full Docker rebuild and
redeploy, because `engine/Dockerfile` bakes every package into the image. With this set up,
a world added or repinned since the last deploy is fetched from R2 at runtime instead -
no redeploy needed. Every already-deployed world is unaffected either way: `engine/m4/
package_fetch.py` only reaches for R2 when a package isn't already sitting locally.

## One-time setup (Mark's own dashboard actions — not executable from a build thread)

Cloudflare's API is unreachable from this sandbox (egress-blocked, confirmed 2026-09-16,
same restriction already hit setting up Render's own dashboard steps in phase 3).

1. **Create the bucket.** Cloudflare dashboard → R2 → Create bucket. Name it something
   stable (`cic-packages` is assumed by nothing in code - any name works, it just has to
   match what's set in step 3).
2. **Generate an API token scoped to that bucket.** R2 → Manage API Tokens → Create API
   Token. Object Read & Write, scoped to the one bucket from step 1 - not account-wide.
   This produces an Access Key ID, a Secret Access Key, and the account's own R2 endpoint
   (`https://<account_id>.r2.cloudflarestorage.com`).
3. **Set four env vars on both Render services** (`cic-engine` and `cic-engine-staging` -
   `render.yaml` already declares all four as `sync: false` on each, so they show up in
   the dashboard ready to fill in): `CIC_API_PACKAGE_BUCKET` (the bucket name),
   `CIC_API_PACKAGE_BUCKET_ENDPOINT`, `CIC_API_PACKAGE_BUCKET_ACCESS_KEY_ID`,
   `CIC_API_PACKAGE_BUCKET_SECRET_ACCESS_KEY`. Same values on both services on purpose -
   see `render.yaml`'s own note on why one shared bucket is right here.
4. **Confirm the free tier is enough.** It should be, by a wide margin (13MB against
   10GB) - worth a glance at R2's own dashboard usage page after the first few uploads
   rather than assumed forever.

Until step 3 is done, `CIC_API_PACKAGE_BUCKET` stays unset and nothing about how packages
load changes at all - every world keeps loading exactly as it always has, straight off
the image's own baked-in `packages/`.

## Using it, once set up

1. Build the package as usual: `python -m engine.m2.cli build <world_key>`.
2. Upload it: `python -m engine.m2.cli upload <world_key>`. Requires the four env vars
   from step 3 above to be set wherever this runs (a local checkout with them exported,
   or a future CI job - see "Not done here" below).
3. Commit the registry pointer (`records/worlds/<code>.yaml`'s `package.location`/
   `manifest_hash`) as usual - "installing a world" is still a reviewed registry commit,
   same as Artifact-2 SS5 always specified, whether or not object storage is involved.
4. The next request for that world, on either running service, fetches it from R2 into
   `CIC_API_PACKAGE_CACHE_DIR` (`/data/packages-cache`, the persistent disk - survives
   restarts) the first time, then serves it locally from then on, same as any other
   resident world.

## Not done here — real follow-on work, not this pass's job

- **CI does not upload automatically yet.** `engine.m2.cli upload` is a manual step a
  human runs after `build`, the same way `build` itself is already run by hand throughout
  this project's world-build threads. Wiring a CI job to call it on every `records/`
  change (matching Artifact-2 SS5's "uploaded by CI" literally) needs its own GitHub
  Actions secrets setup - a similar one-time dashboard step to the Render one above, on
  a different platform, deliberately left for whoever actually wants that automation.
- **The Dockerfile still bakes in every package.** Nothing here removes
  `COPY packages/` or the build-time `engine.m2.cli restore` step - every already-known
  world still ships fully baked in, R2 is purely additive for what's new since. Removing
  the bake-in entirely would make every world's first load depend on R2 being up, a new
  single point of failure this pass deliberately doesn't introduce.
