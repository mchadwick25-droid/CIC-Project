# Church in Conversation — cic-poc, as ONE deployable service.
#
# Multi-stage build: stage 1 (Node) builds the frontend static bundle;
# stage 2 (Python) is the actual runtime image — it serves both the API
# and the built frontend from one process, one port. See
# backend/app/main.py's _FRONTEND_DIST mount for how the built assets
# get served (falls back to backend-only if dist/ isn't present, so
# local backend-only dev is unaffected).
#
# Root/build-context directory for this Dockerfile is `cic-poc/` (this
# file's own parent) — NOT cic-poc/backend/. A single-stage,
# backend-only Dockerfile used to live at cic-poc/backend/Dockerfile;
# it silently produced a container with no frontend at all, since
# frontend/dist/ is gitignored and nothing ever built or copied it in.
# On Render/Railway/Fly.io, set the service's root directory to
# `cic-poc` and it'll find this file automatically — no separate
# "Dockerfile path" setting needed on platforms that don't offer one.
#
# Required at runtime (see backend/.env.example for the full list):
#   ANTHROPIC_API_KEY   - required
#   CORS_ORIGINS        - required for any real deployment; defaults to
#                         localhost-only otherwise and every browser
#                         request will be blocked
#   LLM_PROVIDER, LLM_MODEL - optional, default to Anthropic/claude-sonnet-5
# Everything else (Supabase, pilot logging, mock mode) is optional and
# no-ops safely when unset.

FROM node:20-slim AS frontend-build
WORKDIR /frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app

# System deps for faiss-cpu / sentence-transformers' compiled wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app/ ./app/
COPY backend/data/ ./data/
COPY backend/supabase_schema.sql .
COPY backend/build_indices.py .

# app/prompts/confirmed_glosses.py loads this file at import time (module-
# level, not lazy) - since the S6.2 tail's SS4.3 data move (2026-08-01),
# the gloss data's authoritative home is wrs/glosses/, not an in-code dict.
COPY backend/wrs/glosses/ ./wrs/glosses/

# main.py's _multi_world_turn_floor() reads this at runtime for
# turn_floor_multi_world. It used to be dev/build-time only, like the rest
# of wrs/ (migration scripts, per-world records, gate code, still
# deliberately not copied below) - but that stopped being true at S4.4a and
# this line was never added, so production silently ran on the function's
# hardcoded except-path fallback instead of the canonical value (2026-08-05
# full-system review, Engineering P1-2). Two runtime dependencies under
# wrs/ now; both copied explicitly rather than the whole tree.
COPY backend/wrs/parameters.yaml ./wrs/parameters.yaml

# Pre-compute every world's FAISS indices now, on Render's (or whichever
# host's) build machine, instead of leaving app/main.py's own startup
# lifespan to rebuild them from scratch inside the much more
# memory-constrained runtime instance on every single boot - that
# runtime rebuild (loading sentence-transformers + embedding the full
# lexicon/story corpus for all 6 worlds at once) is what was actually
# causing the OOM kill (status 137) on Render's smaller instance types.
# vector_store/ is gitignored/dockerignored on purpose (generated,
# large) - this bakes a fresh copy directly into the image layer instead
# of ever committing it.
RUN python build_indices.py

# Lands at /frontend/dist — app/main.py resolves this path as two
# parents above app/main.py itself, matching the local dev layout
# (cic-poc/backend/app/main.py -> cic-poc/frontend/dist) one level for
# one level: /app/app/main.py -> parents[2] -> /frontend/dist.
COPY --from=frontend-build /frontend/dist /frontend/dist

# Most hosts (Render, Railway, Fly.io) inject $PORT; default to 8000 for
# anything that doesn't.
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
