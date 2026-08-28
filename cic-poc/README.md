# cic-poc — frontend only (the backend is retired)

What remains here is `frontend/`: the participant-facing surface, built
into the engine's own image (engine/Dockerfile's frontend stage) and
served same-origin by engine/api/app.py's static mount. It is the only
participant-facing surface in this repository, kept on purpose when the
rest of the proof-of-concept was retired — exactly the salvage
.github/workflows/ci.yml's 2026-08-24 note called for.

The proof-of-concept backend (LangGraph app, its own record store, the
direct Anthropic Console API path), its Dockerfile, and its setup guides
were removed 2026-08-28 on Mark's decision ("yes we can retire the old
systems"), completing the retirement PHASE-1-LAUNCH.md Stage 6 began:
the churchinconversation.com links moved to cic-engine on 2026-08-25
(PR #54) and the old Render service was suspended the same day. All of
it remains in git history; the Supabase project holding the old pilot's
transcripts is a separate service and is untouched by this removal.

To work on the frontend: `cd frontend && npm install && npm run dev`.
It talks to engine/api (see engine/api/README.md for running that
locally).
