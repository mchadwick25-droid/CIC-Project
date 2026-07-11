# Claude Agent Setup Guide

**This guide is for Claude agents helping non-technical users set up the CiC POC.**

Follow these steps exactly. After each command, verify the expected output before proceeding.

---

## Pre-Flight Checks

### 1. Verify Python 3.11+

```bash
python3 --version
```

**Expected:** `Python 3.11.x` or higher

**If missing or too old:** Tell user to download from https://www.python.org/downloads/ and install, then retry.

### 2. Verify Node.js 18+

```bash
node --version
```

**Expected:** `v18.x.x` or higher (v20+ is fine)

**If missing or too old:** Tell user to download from https://nodejs.org/ (LTS version) and install, then retry.

### 3. Verify npm

```bash
npm --version
```

**Expected:** Any version number (comes with Node.js)

---

## Backend Setup

### 4. Navigate to backend

```bash
cd /path/to/cic-poc/backend
```

Replace `/path/to/cic-poc` with the actual path where the project is located.

### 5. Create virtual environment

```bash
python3 -m venv venv
```

**Expected:** No output (silent success). A `venv` folder is created.

### 6. Activate virtual environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Expected:** Terminal prompt changes to show `(venv)` at the beginning.

### 7. Install Python dependencies

```bash
pip install -r requirements.txt
```

**Expected:** Many lines of "Collecting...", "Downloading...", "Installing..." ending with "Successfully installed..."

**This may take 2-5 minutes.** Downloading ML models (PyTorch, transformers) is the slow part.

### 8. Get Anthropic API Key

Ask the user:
> "Do you have an Anthropic API key? If not, you can create one at https://console.anthropic.com/settings/keys - you'll need to create an account first."

### 9. Create environment file

```bash
cp .env.example .env
```

**Expected:** No output (silent success).

### 10. Edit the .env file

Open `backend/.env` in a text editor and replace the placeholder API key:

```
ANTHROPIC_API_KEY=sk-ant-PASTE_REAL_KEY_HERE
```

**Important:** The key should start with `sk-ant-`

### 11. Verify API key works

```bash
curl -s https://api.anthropic.com/v1/models \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $(grep ANTHROPIC_API_KEY .env | cut -d= -f2)" \
  | head -c 200
```

**Expected:** JSON starting with `{"data":[{"type":"model"...`

**If you see `authentication_error`:** The API key is invalid. Have user check and re-enter it.

### 12. Check available models and update config

```bash
curl -s https://api.anthropic.com/v1/models \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $(grep ANTHROPIC_API_KEY .env | cut -d= -f2)" \
  | python3 -c "import sys,json; [print(m['id']) for m in json.load(sys.stdin)['data'][:5]]"
```

**Expected:** A list of model IDs like:
```
claude-sonnet-4-5-20250929
claude-opus-4-5-20251101
...
```

If the model in `.env` (`LLM_MODEL`) isn't in the list, update it to one that is.

### 13. Index the lexicon

```bash
python scripts/index_documents.py
```

**Expected:**
```
============================================================
CiC POC - Lexicon Indexer
============================================================

Found 9 lexicon files in data/syriac_world/lexicon_chunks

Indexing documents...
Parsed: syrlex001_raza-shrara.md -> raza (ܐܪܙܐ) / shrara
...
FAISS vector store created

Saving vector store...
Index saved to vector_store

============================================================
Indexing complete!
============================================================
```

### 14. Start the backend server

```bash
uvicorn app.main:app --reload
```

**Expected:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**Leave this terminal running. Open a new terminal for frontend setup.**

---

## Frontend Setup

### 15. Open new terminal and navigate to frontend

```bash
cd /path/to/cic-poc/frontend
```

### 16. Install Node dependencies

```bash
npm install
```

**Expected:** Output ending with something like:
```
added 199 packages in 35s
```

Warnings about deprecated packages are fine to ignore.

### 17. Start the frontend server

```bash
npm run dev
```

**Expected:**
```
VITE v5.x.x  ready in XXX ms

➜  Local:   http://localhost:5173/
```

**Leave this terminal running.**

---

## Verify Everything Works

### 18. Open the application

Tell the user:
> "Open your web browser and go to http://localhost:5173"

### 19. Test the application

They should see:
1. "The Table" header
2. "Choose a Tradition" section
3. A card for "Syriac Christianity" with Mar Yausep

Have them:
1. Click the Syriac Christianity card
2. Click "Begin Conversation with Mar Yausep"
3. Wait for the welcome messages
4. Try asking a question like "What is raza?"

**If they see the conversation and can send messages, setup is complete!**

---

## Common Issues

### "Model not found" (404 error)

The configured model isn't available. Check Step 12 and update `.env` with an available model.

### "Connection refused" or "Failed to fetch"

Backend isn't running. Check the backend terminal for errors.

### Blank page or JavaScript errors

Try:
```bash
# In frontend directory
rm -rf node_modules
npm install
npm run dev
```

### "No module named 'app'"

Virtual environment not activated. Run:
```bash
source venv/bin/activate  # macOS/Linux
```

### Slow first response

First message may take 10-30 seconds as models warm up. Subsequent messages are faster.

---

## Stopping and Restarting

### To stop:
Press `Ctrl+C` in both terminal windows.

### To restart later:

**Terminal 1:**
```bash
cd /path/to/cic-poc/backend
source venv/bin/activate
uvicorn app.main:app --reload
```

**Terminal 2:**
```bash
cd /path/to/cic-poc/frontend
npm run dev
```

Then open http://localhost:5173 in browser.
