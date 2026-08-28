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
COPY packages/ packages/

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
CMD ["sh", "-c", "uvicorn engine.api.app:app --host 0.0.0.0 --port ${PORT} --proxy-headers --forwarded-allow-ips='*'"]
