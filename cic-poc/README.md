# Church in Conversation - Proof of Concept

A proof-of-concept for "The Church in Conversation" project, demonstrating "The Table" - a space for engaging conversation with voices from Christian history.

---

## Quick Start for Claude Agents

**If you are a Claude agent helping someone set up this project, follow these steps exactly:**

### Step 1: Check Prerequisites

Run these commands to verify the user has the required tools:

```bash
# Check Python version (needs 3.11 or higher)
python3 --version

# Check Node.js version (needs 18 or higher)
node --version

# Check npm
npm --version
```

If any command fails or shows a version lower than required:
- **Python**: Direct user to https://www.python.org/downloads/
- **Node.js**: Direct user to https://nodejs.org/ (recommend LTS version)

### Step 2: Navigate to Project Directory

```bash
cd /path/to/cic-poc
```

### Step 3: Set Up the Backend

```bash
# Navigate to backend
cd backend

# Create Python virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies (this may take a few minutes)
pip install -r requirements.txt
```

### Step 4: Configure API Key

The user needs an Anthropic API key. Ask them:
> "Do you have an Anthropic API key? You can get one from https://console.anthropic.com/settings/keys"

Once they have it:

```bash
# Copy the example environment file
cp .env.example .env
```

Then edit `.env` and replace `sk-ant-...` with their actual API key:
```
ANTHROPIC_API_KEY=sk-ant-their-actual-key-here
```

**Important**: The `.env` file is gitignored and will never be committed.

### Step 5: Index the Lexicon (One-Time Setup)

```bash
# Make sure you're in the backend directory with venv activated
python scripts/index_documents.py
```

This creates vector stores for the RAG system (one per world). You should see output like:
```
CiC POC - Lexicon Indexer (Multi-World)
--- Syriac Christianity (syriac-edessa-nisibis) ---
  Found 9 lexicon files...
  Index saved to: vector_store/syriac
--- Post-Apostolic House-Church (post-apostolic-house-church) ---
  Found 13 lexicon files...
  Index saved to: vector_store/pahc
Indexing complete!
  Worlds indexed: 2
```

### Step 6: Start the Backend Server

```bash
# Still in backend directory with venv activated
uvicorn app.main:app --reload
```

The server should start and show:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**Leave this terminal running.**

### Step 7: Set Up the Frontend (New Terminal)

Open a new terminal window/tab:

```bash
# Navigate to frontend directory
cd /path/to/cic-poc/frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

You should see:
```
VITE ready in XXX ms
➜  Local:   http://localhost:5173/
```

### Step 8: Open the Application

Open a web browser and go to: **http://localhost:5173**

You should see "The Table" with a world selection screen showing available traditions:
- **Syriac Christianity** (200-410 CE) with Mar Yausep
- **Post-Apostolic House-Church** (70-200 CE) with Chloe

You can select a single representative or toggle to "Multiple Representatives" mode to invite up to 3 representatives to the same table for a multi-voice conversation.

---

## Troubleshooting

### "Model not found" error (404)

The API key may not have access to the required models. Run this to check available models:

```bash
curl https://api.anthropic.com/v1/models \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: YOUR_API_KEY_HERE"
```

Then update `backend/.env` with a model from the list. Look for models like:
- `claude-sonnet-5`
- `claude-sonnet-4-5-20250929`

### "Module not found" errors

Make sure the virtual environment is activated:
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### Port already in use

If port 8000 or 5173 is busy:

```bash
# Find and kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or start on a different port
uvicorn app.main:app --reload --port 8001
```

### Frontend can't connect to backend

Check that:
1. Backend is running (you should see logs in the backend terminal)
2. Backend is on port 8000
3. No firewall is blocking localhost connections

### Vector store errors

Re-run the indexer:
```bash
cd backend
source venv/bin/activate
rm -rf vector_store
python scripts/index_documents.py
```

---

## Stopping the Application

1. In the **frontend terminal**: Press `Ctrl+C`
2. In the **backend terminal**: Press `Ctrl+C`

## Restarting the Application

After initial setup, you only need:

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

---

## Project Overview

### What This Does

"The Table" allows participants to have conversations with historical Christian voices:

- **Mar Yausep** - A teacher from the Syriac Christian tradition (200-410 CE)
- **Chloe** - A household leader from Post-Apostolic house-church communities (70-200 CE)

The system:

- Uses AI to embody historical voices authentically, each speaking from their own formation
- Supports multi-world tables where multiple representatives engage together
- Retrieves relevant theological terms from per-world lexicons (raza, qyama, ekklesia, etc.)
- Intelligently routes questions to the appropriate representative in multi-world sessions
- Monitors for "drift" - ensuring representatives stay true to their tradition
- Highlights lexicon terms with hover tooltips and click-for-details

### Architecture

```
Frontend (React)          Backend (Python/FastAPI)
     │                           │
     │  HTTP API                 │
     ├──────────────────────────►│
     │                           │
     │                    ┌──────┴──────┐
     │                    │  LangGraph  │
     │                    │  Pipeline   │
     │                    └──────┬──────┘
     │                           │
     │                    ┌──────┴──────┐
     │                    │ RAG System  │
     │                    │ (FAISS)     │
     │                    └──────┬──────┘
     │                           │
     │                    ┌──────┴──────┐
     │                    │  Anthropic  │
     │                    │  Claude API │
     │                    └─────────────┘
```

### Key Files

| File | Purpose |
|------|---------|
| `backend/app/main.py` | FastAPI server, API endpoints |
| `backend/app/graph/nodes.py` | LangGraph conversation nodes |
| `backend/app/rag/retriever.py` | Lexicon retrieval logic |
| `frontend/src/components/TheTable.tsx` | Main UI component |
| `frontend/src/components/WorldSelector.tsx` | World selection screen |
| `frontend/src/hooks/useConversation.ts` | API communication |

### Adding More Worlds

To add another tradition/representative, edit `backend/app/main.py` and add to `AVAILABLE_WORLDS`:

```python
World(
    id="your-world-id",
    name="Tradition Name",
    period="Time Period",
    region="Geographic Region",
    description="Description of this tradition...",
    representative=Representative(
        id="representative-id",
        name="Representative Name",
        title="Their Title",
        description="Description of this voice...",
    ),
    color="#hexcolor",
),
```

You'll also need to add corresponding world content files in `backend/data/`.

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `LLM_PROVIDER` | No | `anthropic` (default) or `openai` |
| `LLM_MODEL` | No | Model ID (default: `claude-sonnet-5`) |
| `ANTHROPIC_API_KEY` | Yes* | Your Anthropic API key |
| `OPENAI_API_KEY` | If using OpenAI | Your OpenAI API key |

*Required if using Anthropic (default)

---

## Development

### Running Tests

```bash
cd backend
source venv/bin/activate
pytest
```

### Building for Production

```bash
cd frontend
npm run build
```

The built files will be in `frontend/dist/`.
