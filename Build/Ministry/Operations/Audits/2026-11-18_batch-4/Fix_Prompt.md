# Batch 4 outline fix prompt

You apply one outline check's findings for **{NAME}** in `{FOLDER}/`. Read `Outline_Check.md`, then `Outline.md` and `Source_Sheet.md`.

1. Apply every BLOCKING and MINOR finding. Where the check gives exact wording, apply it **word for word**. Where it doesn't (it says "move", "state a reason or restore", "replace with a sourced line or cut"), make the smallest change that meets it. Check what you write in the cited file at its lines. Never invent, and change nothing the check did not ask for.
2. Write `{FOLDER}/Fixes.md` with two lists:
   - **Applied verbatim:** finding, then where it went.
   - **Worded by me:** finding, your exact new text, and the file lines that hold it. These get an independent check.
   If you judge a finding wrong, don't apply it. List it under **Not applied**, with the lines that show why.
3. Write only in your folder, and use no shared or scratch file. Don't read any `.brief.*` file or `longDescription`, and don't commit.

Reply in under 100 words: counts for each list, and any finding you did not apply.
