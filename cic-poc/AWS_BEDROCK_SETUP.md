# AWS / Bedrock Setup — for Jonathan

Scope of this document: standing up Amazon Bedrock and hosting for Prototype 1 and Prototype 2. Nothing else in this repo is relevant to that task — see "What you don't need to touch" at the bottom before you go digging.

## Where things stand today

The app runs today on the direct Anthropic API only. There is no Bedrock code path yet — `LLM_PROVIDER` is a two-value setting (`anthropic` | `openai`), not three. Adding Bedrock is real integration work, not a config flip.

Local dev works end-to-end right now (`README.md` has the walkthrough) — the gap is: (1) no Bedrock provider option, and (2) nothing is hosted anywhere a remote tester could reach. Both are yours to close.

## 1. Add the Bedrock provider

Four call sites currently branch on `settings.llm_provider == "anthropic"` and instantiate `ChatAnthropic` from `langchain_anthropic`. Each needs a parallel `"bedrock"` branch (likely `ChatBedrockConverse` from `langchain_aws` — same LangChain chat-model interface, should drop in cleanly):

- `backend/app/config.py:54` — the `Literal["anthropic", "openai"]` type needs `"bedrock"` added, plus whatever Bedrock-specific settings you need (region, at minimum).
- `backend/app/graph/nodes.py` — `get_llm()` (~line 87, the main Representative/Facilitator generation call, takes `max_tokens`) and `get_monitoring_llm()` (~line 128, the Haiku-class classifier call).
- `backend/app/rag/retriever.py` — `filter_llm` instantiation (~line 81).
- `backend/app/rag/story_retriever.py` — `filter_llm` instantiation (~line 53).

Worth factoring these four into one shared factory function while you're in there rather than duplicating the branch four times — your call on how, not prescribed here.

`backend/app/mock_llm.py` gives you a zero-cost mock mode (`MOCK_LLM=true`) for exercising session flow, streaming, and multi-world turn-taking without spending anything — useful while you're wiring this up and don't want to burn real calls testing plumbing.

## 2. AWS account setup

- Request Bedrock model access for the Claude models this project uses (`claude-sonnet-5` per `backend/.env.example`, plus whatever `get_monitoring_llm()` uses for the classifier) in the Bedrock console — **not always instant**, do this the same day the account is created, before you need it working.
- Pick a region with Bedrock + the models you need available.
- IAM: a user or role with `bedrock:InvokeModel` (and streaming equivalent) scoped narrowly — no need for broader permissions for this task.

## 3. Spending limit — required, not optional

Plain AWS Budget alerts only email you; they don't stop spending. Set up an **AWS Budget + a Budget Action** that automatically applies a deny policy blocking further Bedrock calls once a threshold is crossed. Recommended starting threshold: **~$25–30** for Prototype 1 (modeled cost is $15–23, so this gives headroom without much runaway risk). You have $200 in AWS credit, barely touched — both P1 (~$15–23) and P2 (~$38–40) fit comfortably inside it.

Separately, and already in place: `backend/app/session_cap.py` enforces a per-tester session cap via `pilot_tester_codes.json` — this bounds usage at the tester level regardless of dollar cost, so treat it as the primary control and the Budget Action as the backstop, not the only line of defense.

## 4. Hosting — still an open decision

Nothing is deployed yet; local dev only. You need a host for the FastAPI backend and a static host for the built React frontend, reachable by real testers. CORS is already built to support this — set `CORS_ORIGINS` in `backend/.env` to the actual deployed frontend URL once you have one (see `.env.example`); without it every request from a real frontend domain gets blocked.

If you're keeping everything inside the same AWS account/credit as Bedrock, EC2 or Amplify both work and draw from the same $200 credit pool. No preference recorded yet — pick what's fastest for you to stand up correctly.

## Reference

- `README.md` — local dev setup, current architecture diagram, key files.
- `docs/langgraph-architecture.md` — deeper architecture detail if you want it.
- `backend/.env.example` — every environment variable the app reads.

## What you don't need to touch

Everything outside `cic-poc/` — `Ministry/`, `World-Builds/`, `L1-Foundation/` through `L3D-Encounter-Methodology/` — is organizational strategy or theological/historical content for the worlds themselves. None of it affects Bedrock or hosting. `cic-poc/docs/engineering-notes/` holds real but unrelated engineering history (a relational-safety feature, not infrastructure) — only worth opening if you're specifically debugging that feature.
