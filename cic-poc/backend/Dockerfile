# Church in Conversation — backend (FastAPI + LangGraph)
#
# Vector stores are generated at container startup from the checked-in
# data/*_world/ source files (vector_store/ is gitignored - see
# app/graph/nodes.py's lifespan handler, which builds each world's RAG
# index on first access). First boot takes ~20-30s while this runs; no
# separate build step needed.
#
# Required at runtime (see .env.example for the full list):
#   ANTHROPIC_API_KEY   - required
#   CORS_ORIGINS         - required for any real deployment; defaults to
#                          localhost-only otherwise and every browser
#                          request will be blocked
#   LLM_PROVIDER, LLM_MODEL - optional, default to Anthropic/claude-sonnet-5
# Everything else (Supabase, pilot logging, mock mode) is optional and
# no-ops safely when unset.

FROM python:3.11-slim

WORKDIR /app

# System deps for faiss-cpu / sentence-transformers' compiled wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY data/ ./data/
COPY supabase_schema.sql .

# Most hosts (Render, Railway, Fly.io) inject $PORT; default to 8000 for
# anything that doesn't.
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
