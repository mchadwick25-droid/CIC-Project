# Church in Conversation — engine/api as a deployable service.
# PHASE-1-LAUNCH.md Stage 3 asked for this container ("the engine needs a
# container"); the cic-poc Dockerfile that stage described beside it was
# retired and deleted with the old system, 2026-08-28.
#
# Build context MUST be the repository root, not engine/ — the image needs
# engine/, records/, and records/worlds.yaml together, the same layout
# every COPY below and .github/workflows/ci.yml's own recipe already
# assume. On Render (or any host that lets you set a Dockerfile path
# separately from the build context), point dockerfilePath at
# engine/Dockerfile and leave dockerContext as the repo root. (The retired
# cic-poc/Dockerfile this note once contrasted against is deleted - the
# old system's retirement, 2026-08-28.)
#
# Frontend stage added PHASE-1-LAUNCH.md Stage 5 (one Render service, not
# two - Mark's call): builds cic-poc/frontend's static bundle and lands it
# at cic-poc/frontend/dist, same source-tree-relative path engine/api/
# app.py's own REPO_ROOT-based lookup expects locally, so nothing about
# how the mount finds it differs between a dev checkout and this image.
# engine/api/app.py serves it same-origin (no CORS_ORIGINS needed) -
# guarded on the dist/ directory existing, so a build of this image with
# the COPY below removed still runs API-only, same as it always did.
#
# Required at runtime (engine/api/config.py):
#   CIC_API_REGION      - required, no default; refuses to guess a
#                         Bedrock region
#   AWS credentials     - via boto3's standard chain (env vars,
#                         ~/.aws/credentials, or an attached IAM role).
#                         Never baked into this image. Production wants
#                         its own IAM identity scoped to Bedrock invoke
#                         on the models actually used — cic-bedrock-dev
#                         is a dev-only identity (PHASE-1-LAUNCH.md
#                         Stage 3).
# Optional, all default sensibly (engine/api/config.py):
#   CIC_API_VOICE_MODEL_PATTERN, CIC_API_SAFETY_MODEL_PATTERN,
#   CIC_API_EVENTS_DB, CIC_API_USAGE_DB, CIC_API_WORLDS_YAML,
#   CIC_API_DEFAULT_WORLD_KEY
#   CIC_ENFORCE_ADMISSION - the doors-open switch ("1" = only
#   admitted/open worlds are listed or seated; "0" = today's declared
#   deferral, see render.yaml). It was absent from this list - the one
#   config var the 2026-08-28 audit found shipped-but-undocumented.

FROM node:20-slim AS frontend-build
WORKDIR /frontend
COPY cic-poc/frontend/package.json cic-poc/frontend/package-lock.json ./
RUN npm ci
COPY cic-poc/frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app

# engine/api/requirements.txt + engine/m1/requirements.txt is the exact
# pair .github/workflows/ci.yml's api-tests job installs before running
# the restore step below — api's own reqs (fastapi, uvicorn, anthropic
# [bedrock], boto3, ...) plus m1's (jsonschema, pyyaml), which the M2
# compiler restore needs and api's own requirements.txt has no reason to
# duplicate.
COPY engine/api/requirements.txt engine/api/requirements.txt
COPY engine/m1/requirements.txt engine/m1/requirements.txt
RUN pip install --no-cache-dir -r engine/api/requirements.txt -r engine/m1/requirements.txt

COPY engine/ engine/
COPY records/ records/
# A world's search records and its site and Facilitator records; .dockerignore
# admits only those two homes from Build/worlds/.
COPY Build/worlds/ Build/worlds/
COPY packages/ packages/
# Two engine/m1/gates.py checks (gate_edition_rights_consistency, gate_
# canonical_address) read cic/texts/<file> straight off disk to confirm a
# record's cited edition/address actually resolves - _TEXTS_DIR there is
# repo-root-relative, not records_root-relative, so restore below silently
# sees every real citation as "does not exist" without this. Missing here
# was harmless until those two gates existed (2026-09-02/09-03): nothing
# else this image builds or serves reads cic/texts/, so the restore step
# was the first thing to ever notice the absence - as a validation/gates-
# report.json mismatch on every world except fix (whose only edition
# reference is a deliberately-nonexistent fixture path, already accounted
# for in its own pinned report). cic/corpus-map/ stays out - genuinely
# staging files, nothing this image builds or serves reads it.
COPY cic/texts/ cic/texts/

# cic/engine/ was "not read by anything at runtime" until P3's item 2
# (2026-09-23): engine/m1/quote_verbatim.py's _edition_apparatus_entries
# now does `from cic.engine.texts_registry import apparatus_for` for every
# quote citing an edition with a registered apparatus form. That import
# was already live in restore's own gates.run_all() once item 3 registered
# gate_quote_verbatim - harmless while report-only, a hard
# ModuleNotFoundError on this image's own restore step the moment the gate
# actually ran here, found and fixed the same day by an actual Docker
# build (not assumed from the code alone).
COPY cic/engine/ cic/engine/

# Compiled world packages are DERIVED, not source (see .gitignore) — a
# clean checkout carries only records/, records/worlds.yaml, and each
# package's own manifest.json, nothing under compiled/. restore
# recompiles every package the registry is pinned to (using each
# manifest's own package_id/records_commit/compiler_version, never a
# fresh package_id) and verifies every file hash against that manifest
# before writing anything — "a build that does not reproduce them is not
# this system" (PHASE-1-LAUNCH.md Stage 3). Same command CI runs before
# any job that reads package bytes; fails the build loudly on a mismatch
# rather than shipping an image with silently-wrong compiled content.
RUN python -m engine.m2.cli restore

# Lands at /app/cic-poc/frontend/dist — engine/api/app.py resolves this
# same path via REPO_ROOT (parents[2] from engine/api/config.py, i.e. this
# WORKDIR) both here and in a local dev checkout.
COPY --from=frontend-build /frontend/dist cic-poc/frontend/dist

# Most hosts (Render, Railway, Fly.io) inject $PORT; default to 8000 for
# anything that doesn't.
ENV PORT=8000
EXPOSE 8000

# --proxy-headers + --forwarded-allow-ips: behind Render's proxy every
# request's socket peer is the proxy itself; without these the per-IP
# rate limiter (engine/api/ratelimit.py) would see ONE client and throttle
# everyone together. X-Forwarded-For is set by Render's edge, and the
# proxy is the only thing that can reach this container, so trusting it
# is trusting the platform we already run on.
#
# --no-access-log: uvicorn's access log writes each request's client IP
# beside its path, and the path carries the session id, so it would join
# an IP to a conversation (System Hub decisions 19 and 26). The app logs
# each handled message itself, with the session id and never an IP.
CMD ["sh", "-c", "uvicorn engine.api.app:app --host 0.0.0.0 --port ${PORT} --proxy-headers --forwarded-allow-ips='*' --no-access-log"]
