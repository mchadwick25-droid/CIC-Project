# staging/ — which files are LIVE and which are SUPERSEDED

Per world directory:

| file | status |
|---|---|
| `*_Representative_Permanent_Prompt_S52.txt` | **LIVE** — the §5.1 assembly, written by `s62_<world>_permanent_prompt.py` (Desert: `permanent_prompt.py`); the file `assembly_identity.py` reasons about |
| `*_prompt_segment_manifest.json` | **LIVE** — the assembly's manifest |
| `*_World_Capsule_Core_generated.md` | **LIVE** — the capsule render (the capsule half of `s62_<world>_capsule_prompt_views.py` is still current) |
| `lexicon_chunks/`, `story_chunks/` | **LIVE** — the rebuilt chunk serializations |
| `*_Representative_Permanent_Prompt_generated.txt` | **SUPERSEDED** — the prompt half of the deliberately-temporary `capsule_prompt_views` scripts, replaced by the S52 assembly. Kept only because the committed `probe_parity` instruments read them; graded once in error (Chloe's void checkpoint-1 runs, 2026-08-09 — see the `_VOID-wrong-prompt` artifacts). **Never build a candidate from these.** Candidate trees are built by `scripts/checkpoint_candidate.py`, which calls the assembler directly and never reads staging prompts at all. |

Flagged for Phase 3 (S6.5 capsule fold-in): retiring the `_generated.txt`
prompt halves and re-pointing or retiring the parity scripts that read
them.
