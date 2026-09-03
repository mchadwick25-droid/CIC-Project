# `_intake/` — the inbox, not the shelf

Raw, not-yet-processed source files land here — pushed directly to this
folder on GitHub, as an alternative to attaching them in a chat message
(both are real paths; see `cic/texts/INTAKE.md`'s own "Trigger" section).
Any format: DOCX, PDF, plain text, HTML saved from a page, whatever the
download actually was.

**Nothing here is vendored yet.** A file in `_intake/` has no header, no
rights determination, no `REGISTRY.yaml` row, no corpus-map assignment —
none of the verification `cic/texts/` itself requires. Treat this folder
the same way `cic/corpus-map/_staging/` is already treated: a working
queue, not a citable source. A build thread should never read from here
directly.

**Provenance travels with the file, not just in a chat message.** A file
attached mid-conversation has Mark's own words alongside it to say where
it came from; a file pushed straight to `_intake/` doesn't, unless it's
written down. Add a short note per file (or one shared `NOTES.md` covering
several) stating: the URL it came from, and what that host itself says
about rights — the same two facts `cic/texts/INTAKE.md` §1 asks for either
way. A file with no stated provenance just means the processing session
has to ask before going further, the same as an attachment with no context
would.

**What happens to a file after it's processed:** once a session works it
through `cic/texts/INTAKE.md` — rights checked, header written, named,
registered, assigned — the raw original is deleted from `_intake/`. The
properly-headered file under `cic/texts/` *is* the enduring record; its own
`Source:` line states it arrived via `_intake/<original filename>` and
when. `_intake/` stays a queue of what's still waiting, not a second copy
of everything that's already landed.

**What happens to a file that turns out not to be usable** (rights don't
clear, OCR too corrupted to verify, out of scope) — also removed from
here once that's determined, with the finding recorded in the session's
own commit history or conversation rather than left sitting in the queue
indefinitely. An empty `_intake/` is the healthy state, not a stalled one.
