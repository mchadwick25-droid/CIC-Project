import math
from pathlib import Path

from .catalog import REPO_ROOT, FileEntry
from .estimate import FilePlan, ScopeEstimate
from .pricing import BATCH_DISCOUNT_SOURCE, MODEL_ID, price_table
from .prompting import CONTEXT_WORD_LIMIT
from .report import WINDOW_DEFINITION, money, render_settings
from .sample import DEFAULT_FILES
from .status import PENDING_OPTION

CAP_MULTIPLE = 5
CAP_STEP = 0.5
CAP_FLOOR = 1.0
SAMPLE_COMMAND = "python Sandbox/answering-library/index/cli.py"
SAMPLE_ROLES = {
    "xml": "XML edition with divisions (English)",
    "latin": "plain text, Latin",
    "weak_ocr": "plain text from a scan, French; the weak-OCR case",
}


def recommended_cap(high_dollars: float) -> float:
    return max(CAP_FLOOR, math.ceil(high_dollars * CAP_MULTIPLE / CAP_STEP) * CAP_STEP)


def _role_of(file_name: str) -> str:
    for role, name in DEFAULT_FILES.items():
        if name == file_name:
            return SAMPLE_ROLES[role]
    return "chosen by the selector"


def _file_rows(plans: list[FilePlan], entries: dict[str, FileEntry]) -> list[str]:
    table = price_table()
    rows = ["| Role | File | Language | Passages | Text tokens (low to high) | Cost, low to high |", "|---|---|---|---:|---|---|"]
    for plan in plans:
        entry = entries[plan.file]
        languages = ", ".join(entry.language_codes) or "see file header"
        rows.append(
            f"| {_role_of(plan.file)} | `{plan.file}` | {languages} | {round(plan.passages):,} | "
            f"{plan.body_tokens['low']:,} to {plan.body_tokens['high']:,} | "
            f"{money(plan.dollars('low', table))} to {money(plan.dollars('high', table))} |"
        )
    return rows


def render_card(
    sample: ScopeEstimate, union: ScopeEstimate, entries: dict[str, FileEntry], *, segmented: bool, out_dir: Path, live_test_name: str,
) -> str:
    s = sample.summary()
    cap = recommended_cap(s["dollars_sync"]["high"])
    u = union.summary()
    status = (
        "ready, passages are the segmenter's own, selected by the rule below."
        if segmented else
        "pending, the segmenter's output (the passages folder of the answering-library out directory) does not exist yet. "
        "The files below are the default pick and every count is modeled from word counts at about 275 words a passage. "
        "Run the selector once the segmenter lands, then regenerate this card; the counts, the file list and the cap are recomputed."
    )
    lines = [
        "# S1-05 sample card: contextual indexing, lpc sample",
        "",
        PENDING_OPTION,
        "",
        f"Segmenter: {status}",
        "",
        "Nothing has been run. No model call and no paid call was made to prepare this card. The run waits for Mark to approve this "
        "sample by name and set the cap (root CLAUDE.md, metered spend and paid bulk runs).",
        "",
        "## What Mark is asked to approve",
        "",
        f"- Model: `{MODEL_ID}` (Haiku 4.5 class, priced from `engine/m8/price_tables.py`).",
        f"- What it writes: one context line of at most {CONTEXT_WORD_LIMIT} words per passage, placed in front of the passage in the search index only.",
        f"- Window: {WINDOW_DEFINITION}.",
        f"- Sample: {s['passages']:,} passages in {s['files']} lpc files, about {s['text_tokens']['low'] / 1e6:.2f}M to {s['text_tokens']['high'] / 1e6:.2f}M text tokens.",
        f"- Estimated cost: {money(s['dollars_sync']['low'])} to {money(s['dollars_sync']['high'])} on the standard path.",
        f"- Cap recommended: {money(cap)} ({CAP_MULTIPLE} times the high estimate, rounded up, floor {money(CAP_FLOOR)}); "
        f"that is {cap / 200 * 100:.1f}% of the $200 indexing ceiling. The guard stops the run before the cap and the run resumes where it stopped.",
        f"- Suggested live-test name: `{live_test_name}`.",
        "",
        "## Files",
        "",
        *_file_rows(sample.plans, entries),
        "",
        "lpc's plain-text files hold no Greek-script characters (checked on the file contents), so this sample covers Latin script only, in "
        "three languages: Latin, English and French. A Greek check would need a file from the Cappadocian shelf; say so and the selector "
        "adds one small slice.",
        "",
        "## Settings as the run prints them",
        "",
        "```",
        render_settings(sample, live_test=live_test_name, cap_usd=cap, out_dir=out_dir).replace(
            str(out_dir.relative_to(REPO_ROOT) / "context"), "the context folder of the answering-library out directory (gitignored)"),
        "```",
        "",
        "Counts on the Input lines are token estimates from character counts (no tokenizer runs offline). The run's own usage log replaces them "
        "with measured tokens after the first calls.",
        "",
        "## Commands",
        "",
        "Select the sample from the segmenter's output (free, no network):",
        "",
        "```",
        f"{SAMPLE_COMMAND} sample-select --world lpc",
        f"{SAMPLE_COMMAND} run --sample lpc --dry-run",
        "```",
        "",
        "Run after approval (live-tests environment only; the key is never set on Render). `NAME` and `CAP` are the approved values:",
        "",
        "```",
        "CIC_MODEL_ROUTE=anthropic CIC_ANTHROPIC_API_KEY=<live-tests key> \\",
        f"{SAMPLE_COMMAND} run --sample lpc \\",
        '  --live-test "NAME" --cap-usd CAP',
        "```",
        "",
        "Without both flags the command prints the live-test rule and exits before any work. With them it prints the settings above, then the guard "
        "prints its own header (name, cap, model, route, ledger) before the first call. Every call is recorded in the guard's ledger and in "
        "the run log `_runs.jsonl` beside the context lines.",
        "",
        "Look at the result:",
        "",
        "```",
        f"{SAMPLE_COMMAND} show-sample --n 9",
        "```",
        "",
        "## How to judge it by eye",
        "",
        "`show-sample` prints a spread of context lines, each beside its passage, with the mechanical check's verdict. Read about nine pairs "
        "across the three files and ask of each context line:",
        "",
        "1. Does it name the right work, author and division, as the file header and the passage say?",
        "2. Does it say where the passage sits (after what, before what) in a way a search could use?",
        "3. Is every name, date and place in it also in the stretch the model was given? Nothing added from memory.",
        "4. Is it one plain sentence, not a summary of the passage and not a quotation of it?",
        "",
        "A bad one looks like this (illustrations written for this card, not output from a run):",
        "",
        "| Defect | Illustration | Why it fails |",
        "|---|---|---|",
        "| Adds a fact | \"Cyprian's De lapsis, written in the Decian persecution of 250, warns the lapsed.\" when neither the header nor the "
        "stretch mentions Decius or 250 | Invented context. The mechanical check flags an entity not in the window; such a line is kept in the "
        "log but left out of the index. |",
        "| Restates the passage | \"The bishop urges the brethren to keep one body in the unity of the church.\" | Copies the passage. Adds nothing a "
        "search could not already find. |",
        "| Too generic | \"A passage from a Latin text about the church.\" | Does not situate the passage; useless for retrieval. |",
        "| Wrong place | Names a different work or division from the header | Misleads retrieval; the check cannot catch this, only the eye can. |",
        "| Speaks as the source | \"Here Cyprian himself says...\" on a passage whose speaker is mixed | Context must not assign a voice the segmenter "
        "did not mark. The eye catches this one too. |",
        "",
        "Decision rule suggested for the eye pass: approve if no more than one in nine is a defect of the last two kinds and the check flags "
        "no more than a few percent of lines; otherwise change the prompt and re-sample.",
        "",
        "## What the context line is and is not",
        "",
        "The context line is retrieval-only. It is prepended to the passage inside the search index so a query can match it, and it is stored "
        "in its own column. It is never stored in the passage text, never shown as source text, and never quoted. Every indexed passage keeps "
        "its file, byte span in the vendored file, division locus, ordinal, speaker, OCR score, apparatus flag, row ids and worlds. A "
        "retrieval hit returns the passage text and those fields separately from the context line, and `verify` checks that each passage "
        "text still equals its byte span in `cic/texts`. That keeps the three levels reachable: the marked text in an answer points to a "
        "passage id, the hover reads the passage's own fields, and the click-through opens the full record with the link to the vendored file "
        "and location.",
        "",
        "## Whole-job figure this sample is a step toward",
        "",
        "| Union of the twelve shelves | Low | High |",
        "|---|---:|---:|",
        f"| Standard path | {money(u['dollars_sync']['low'])} | {money(u['dollars_sync']['high'])} |",
        f"| Batch path, half price (assumed; not reachable through the live-test guard today) | {money(u['dollars_batch_assumed']['low'])} | {money(u['dollars_batch_assumed']['high'])} |",
        f"| One call per window instead of per passage, standard path (estimate only) | {money(u['dollars_one_call_per_window_sync']['low'])} | {money(u['dollars_one_call_per_window_sync']['high'])} |",
        "",
        f"The union is {u['passages']:,} modeled passages and {u['text_tokens']['low'] / 1e6:.0f}M to {u['text_tokens']['high'] / 1e6:.0f}M text tokens, "
        "modeled from word counts until the segmenter lands. The about-$150 figure does not reproduce for per-passage calls on Haiku 4.5: "
        "it counts each text token once at the plain input rate, and per-passage calls also pay the 1.25 times cache-write premium on every "
        "token of every window, cache reads on each further passage in a window, and the output lines (the output alone is "
        f"{money(u['cost_drivers_low']['output'])} to {money(u['cost_drivers_high']['output'])}). "
        f"Batch discount, {BATCH_DISCOUNT_SOURCE}. The breakdown by file, world and cost driver is in `S1-05_Cost_Estimate.md`.",
        "",
        "## Pending",
        "",
        "- Mark: the sample's approval, the name and the cap.",
        "- Segmenter output (one `passages/<file-stem>.jsonl` per file and `manifest.json` in the answering-library out directory): replaces the modeled counts with real ones.",
        "- Embeddings are a separate metered class (proposal decision 2c) that Mark has not decided. The pipeline has only an interface for one "
        "(`index/embeddings.py`) and makes no embedder call.",
        "- Batch path: needs a guard extension (the guarded client exposes only `messages.create` and `messages.stream`), which is a change to "
        "`engine/provider/guard.py` and its own change order.",
    ]
    return "\n".join(lines) + "\n"
