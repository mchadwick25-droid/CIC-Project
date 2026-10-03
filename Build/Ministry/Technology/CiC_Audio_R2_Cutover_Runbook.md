# Audio storage: moving the recordings from git to Cloudflare R2

The site's narration recordings (about 632 MB, 918 files under `cic-website/audio/`) are
served by the Worker in `cic-worker/worker.mjs`. This runbook moves them from the
repository to an R2 bucket without changing any page, link or player.

## What is built

- The Worker answers `/audio/**.mp3` from the `AUDIO` bucket binding first, with native
  byte ranges, and falls back to the repository copy when the binding is absent, the
  object is missing or the bucket errors. The manifest `.json` files always come from
  the repository.
- `Build/tools/sync_audio_r2.mjs` uploads every recording and checks size and MD5.
- The generation tools decide "already narrated" from the manifests, not from files on
  disk: `audio/tree/manifest.json`, `audio/worlds/manifest.json`,
  `audio/docstories/manifest.json`, `audio/site/manifest.json`.

## Steps

1. **Account (Mark).** Turn on R2, create a bucket named `cic-audio`, and create an API
   token with Object Read & Write on that bucket. Keep the account ID, access key ID and
   secret access key where the generation tools run.
2. **Upload.** Check the plan, then upload, then verify:
   ```
   node Build/tools/sync_audio_r2.mjs --dry-run
   R2_ACCOUNT_ID=... R2_ACCESS_KEY_ID=... R2_SECRET_ACCESS_KEY=... node Build/tools/sync_audio_r2.mjs
   R2_ACCOUNT_ID=... R2_ACCESS_KEY_ID=... R2_SECRET_ACCESS_KEY=... node Build/tools/sync_audio_r2.mjs --verify
   ```
   `--verify` exits 1 unless all 918 files match. The site is unchanged at this point.
3. **Bind the bucket.** Add to `wrangler.jsonc`, only once the bucket exists (a binding to
   a missing bucket fails the deploy):
   ```
   "r2_buckets": [{ "binding": "AUDIO", "bucket_name": "cic-audio" }]
   ```
   Merge. Live behavior is the same; rolling the Worker back reverts it.
4. **Check live.** Narration plays and seeks on desktop and on an iPhone, on a tree page,
   a world page, the Unfolding Story and About.
5. **Remove from git.** A separate pull request deletes the `.mp3` files from the
   repository and ignores `cic-website/audio/**/*.mp3`. The fallback then no longer
   applies, so step 4 must have passed first.

## After the cutover

New recordings are generated into `cic-website/audio/` (ignored by git), their manifest
entry is committed, and `sync_audio_r2.mjs` uploads them. A fresh checkout has no
recordings locally, which is correct: the generators read the manifests.

## Not done here

Git history still holds every recording ever committed, so a fresh clone stays large.
Removing it means rewriting history and force-pushing main, which affects every
checkout. That needs a separate, explicit go-ahead.

The conversation's welcome clips (`cic-poc/frontend/public/audio/door/`) are served by
the app on Render, not Cloudflare, and stay where they are.
