# Church in Conversation - the serving image for the clean tree.
#
# Build context is the REPO ROOT, not cic/ - the image needs cic/ and the
# participant-facing frontend, which lives outside it. See /.dockerignore,
# which allowlists exactly those two trees out of a 572MB repo.
#
#     docker build -f cic/Dockerfile -t cic .
#
# THE POINT OF THIS FILE is that nothing expensive happens on a live
# instance. Two things used to happen inside the first participant's
# first request, on a box with a recorded OOM history:
#
#   1. Two transformer models downloaded from huggingface.co
#      (all-MiniLM-L6-v2 for embeddings, ms-marco-MiniLM-L-6-v2 for
#      cross-encoder reranking). requirements.txt says so in its own
#      comment: "that host must be reachable, or every turn fails in
#      retrieval."
#   2. That world's FAISS index built from its chunk files, because
#      LexiconRetriever.__init__ falls through to index-and-save when a
#      saved index is absent (app/rag/retriever.py:71-77).
#
# Both are moved into the build below, and then ASSERTED - the build
# fails if either did not actually land. A green build is therefore
# evidence, not intent.

# --- stage 1: the participant-facing UI --------------------------------
# cic/ has no frontend of its own. The one that exists is cic-poc/frontend
# - live, CI-built (the "Frontend build (tsc + vite build)" job), and
# already compatible: every endpoint it calls (/api/worlds, /api/session/
# start, /api/session/{id}/message/stream, /api/lexicon, /api/resources,
# /api/repository/record/{id}) is served by cic/runtime/app/main.py, and
# it addresses them relative to its own origin. Served from this same
# container that means no CORS configuration is involved at all.
#
# NOTE ON THE OLD TREE: cic-poc/BACKEND is retired and is never read,
# copied or referenced. The frontend is a different thing and was never
# retired with it.
#
# Node 20 to match the CI job, so a build that passes there builds here.
FROM node:20-slim AS frontend
WORKDIR /build
COPY cic-poc/frontend/package.json cic-poc/frontend/package-lock.json ./
RUN npm ci
COPY cic-poc/frontend/ ./
# `npm run build` is tsc && vite build - a type error fails the image,
# which is the same bar CI holds it to.
RUN npm run build


# --- stage 2: the serving image ----------------------------------------
FROM python:3.11-slim

# curl is for HEALTHCHECK only; build-essential is dropped again after
# pip finishes so it does not ride along in the shipped layer.
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    # One cache location for both transformer models, written during the
    # build and read at runtime. Must be set BEFORE anything imports
    # sentence-transformers, or the models land in /root/.cache and the
    # non-root runtime user cannot see them.
    HF_HOME=/opt/hf-cache \
    # Retrieval is CPU-only by design (app/rag/embeddings.py pins
    # device="cpu", cross_encoder.py is a ~90MB CPU model). Threads left
    # at 1: a 512MB shared-CPU instance gains nothing from torch's
    # default thread pool and pays for it in memory.
    OMP_NUM_THREADS=1 \
    TOKENIZERS_PARALLELISM=false

WORKDIR /srv/cic

# --- dependencies ---------------------------------------------------
# torch first, from the CPU-only wheel index. sentence-transformers pulls
# torch transitively, and the plain PyPI resolve drags in the whole CUDA
# stack - nvidia-cublas, nvidia-cudnn, nvidia-nccl, triton, the lot - for
# a service whose two models are both pinned to device="cpu". Measured,
# not estimated: installing requirements.txt as written produces a 5.4GB
# environment. Installing the CPU build explicitly FIRST means the
# transitive resolve finds torch already satisfied and never reaches for
# the CUDA wheel.
#
# The pin is the version requirements.txt's own resolve selects
# (sentence-transformers==5.7.0 -> torch 2.13.0, observed 2026-08-17), so
# this changes which BUILD of torch is installed, never which version.
RUN pip install --no-cache-dir \
        --index-url https://download.pytorch.org/whl/cpu \
        torch==2.13.0

COPY cic/runtime/requirements.txt ./runtime/requirements.txt
RUN pip install --no-cache-dir -r runtime/requirements.txt
# NOTE: requirements.txt's last block (textstat, nltk) is labelled "engine
# gate suite only", and that is exactly true of the serving path - nothing
# under runtime/app/ imports textstat, and engine/gates.py imports only
# `re` at module level, so the bridge (app/engine_bridge.py, which pulls
# _alias_freq_table and post_history_guard_for) never reaches the
# readability code. Both verified by grep before relying on it. So this
# image deliberately does NOT download nltk's cmudict corpus - CI does
# that for the gate job, and the container has no use for it.

# --- application ----------------------------------------------------
# The four roots the serving app reads, and nothing else. engine/ and
# records/ are here because runtime/app/engine_bridge.py resolves guards,
# parameters and glosses out of them at import time, and nodes.py /
# repair_classifier.py / modern_term_bridge.py read records directly.
COPY cic/engine/  ./engine/
COPY cic/records/ ./records/
COPY cic/deploy/  ./deploy/
COPY cic/runtime/ ./runtime/

# main.py serves this directory if it exists and runs API-only if it does
# not (app/main.py:2263, _FRONTEND_DIST = <cic>/frontend/dist), so the
# path is fixed by the app rather than chosen here.
COPY --from=frontend /build/dist ./frontend/dist

# --- bake the indices and the models --------------------------------
# This is the step whose absence caused the OOM. One shared embedding
# model, six worlds sequentially, two FAISS stores each; the cross-encoder
# is warmed in the same run so its weights are in HF_HOME too. Non-zero
# exit on any world's failure, so a partial index set fails the build
# instead of reaching production as a silent per-world runtime rebuild.
RUN cd runtime && python scripts/build_indices.py

# Independent verification, in fresh processes, with the network refused.
# HF_HUB_OFFLINE is what makes these real tests rather than hopes: a
# missing weight or a missing index fails the build HERE, instead of
# failing inside a participant's first turn.
#
#   --check       loads every world's index rather than stat-ing it (a
#                 truncated store passes an existence check and dies on
#                 the first query)
#   verify_image  disables index rebuilding entirely, then retrieves from
#                 all six worlds - see that script's docstring for why
#                 the retriever's silent fallback makes this the only
#                 assertion that actually proves the baking worked
RUN cd runtime \
 && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python scripts/build_indices.py --check \
 && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python scripts/verify_image.py \
 && chmod -R a+rX /opt/hf-cache

# Keep the guarantee at runtime. If some future change introduces a third
# model, this turns a silent mid-request download into an immediate, loud
# failure - which is the version of that bug anyone can actually find.
ENV HF_HUB_OFFLINE=1 \
    TRANSFORMERS_OFFLINE=1

# --- runtime user ---------------------------------------------------
# events.py writes JSONL under runtime/transcripts/events/ (its
# CIC_EVENTS_DIR default). Created and owned here so the unprivileged
# user can write it. NOTE: this is container-local and dies with the
# container - durability is Supabase's job (SUPABASE_URL /
# SUPABASE_SERVICE_KEY), not this directory's.
RUN mkdir -p runtime/transcripts/events \
 && useradd --system --uid 10001 cic \
 && chown -R cic:cic runtime/transcripts
USER cic

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
    CMD curl -fsS "http://127.0.0.1:${PORT:-8000}/health" || exit 1

WORKDIR /srv/cic/runtime
# Shell form on purpose: Render assigns the port through $PORT, and exec
# form would pass the literal string. One worker - the two transformer
# models are per-process, so a second worker doubles the resident set on
# an instance that has already been OOM-killed once at 512MB.
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1
