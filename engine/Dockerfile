# Church in Conversation — engine/api as a deployable service.
# PHASE-1-LAUNCH.md Stage 3: "the engine needs a container. There is no
# engine/Dockerfile. render.yaml builds cic-poc/Dockerfile and nothing
# else." This is that container.
#
# Build context MUST be the repository root, not engine/ — the image needs
# engine/, records/, and records/worlds.yaml together, the same layout
# every COPY below and .github/workflows/ci.yml's own recipe already
# assume. On Render (or any host that lets you set a Dockerfile path
# separately from the build context), point dockerfilePath at
# engine/Dockerfile and leave dockerContext as the repo root — unlike
# cic-poc/Dockerfile, which sets dockerContext to cic-poc/ because its own
# needs (frontend/, backend/) are both under that one directory.
#
# No frontend stage: engine/api is HTTP-only (four endpoints, no UI —
# CiC-Program-Spec.md M6). The participant-facing surface is a separate,
# not-yet-built piece (PHASE-1-LAUNCH.md Stage 4), explicitly gated on
# Mark's own design pass (Stage 7.5) before any surface code is written.
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

# Most hosts (Render, Railway, Fly.io) inject $PORT; default to 8000 for
# anything that doesn't — same convention cic-poc/Dockerfile already
# uses.
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn engine.api.app:app --host 0.0.0.0 --port ${PORT}"]
