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
