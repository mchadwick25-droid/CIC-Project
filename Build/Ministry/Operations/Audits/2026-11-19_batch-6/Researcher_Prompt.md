# Batch 6 researcher prompt

You are the researcher for one Church Family Tree story about **{NAME}** (census id `{SLUG}`). Your folder is `Build/Ministry/Operations/Audits/2026-11-19_batch-6/{SLUG}/`. Write only there, and use no shared or scratch file. You write no story prose.

This person is already on the tree, with a story written before the current kit. You build the research fresh, on the kit, for the job below. Batch 5 (`Build/Ministry/Operations/Audits/2026-11-18_batch-5/`) is the working model: look at one of its `Source_Sheet.md` and `Outline.md` pairs for the form only.

**The job (Mark's, 2026-11-19).** {JOB}

**Siblings and links.** {SIBLINGS}

## Read
- `CLAUDE.md`, the "Trust and source fidelity" section.
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/researcher.md`, and follow it in full. It points you to Parts 1 to 3 of `Brief-Kit/Kit.md`. The kit now has an "Outside witness" shape and a "Words to explain" field; use them where they apply.
- `Build/Ministry/Operations/Audits/2026-11-19_batch-6/README.md`, for the batch's jobs and the quotes barred.
- The census entry `{SLUG}` in `cic-website/data/world-census.json`, but not its `longDescription`. Its card, where it has one, is `Card.existing.json` in your folder.
- Each sibling or link named above. A live story is the `longDescription` of its census entry. Polycarp's story is the approved text `Build/Ministry/Operations/Audits/2026-11-19_batch-6/polycarp-of-smyrna/polycarp-of-smyrna.brief.txt`, not his census text. A sibling earlier in this batch is its `Outline.md` in its batch 6 folder. Read each before research, keep to this story's own job, and reuse none of its quotes.

Do not read any existing brief or audio text for this subject: no `{SLUG}.brief.*` or `{SLUG}.audio.*` file anywhere, and not this entry's `longDescription`. Do not run `tools/validate-census.mjs`.

## What to do
1. `Source_Sheet.md`, ending with the Library sweep, as the role says.
2. `Outline.md` to Part 3 of the kit. Set **the essence** and **also told** to the job above, then the beats, in time order, told once. Fill the **Words to explain**, **Names** and **Sibling** fields. The **Connection** says what passed on and what the listener must be told to understand it.
3. Before you finish, search every census `longDescription` (other than this entry's, which you do not read) and the approved Polycarp text for each quote you chose, and drop any already used on the tree.
4. The four-fault self-check, as the role says.

## Reply (under 250 words)
- **The essence** and **also told**, in plain sentences, each part with its confidence. This goes to Mark on one page.
- The shape, the length and its reason, and the opening you chose.
- The connection, in one line.
- The quotes (renderings only).
- Any gap: a source not held, a thin record, or a sibling question for Mark.
- That you ran the four-fault check, and what it caught.
