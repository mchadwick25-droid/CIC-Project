# Brief: read constructed gold-set candidates

Someone else wrote candidate sentences, each meant to carry exactly one known defect of one class against its bound record. You decide, for each, whether it may enter the gold set. Be strict: a gold item that is not what it claims corrupts every measurement made with it.

Each line of the list file is a JSON object: id, type, world, bindings (record ids), sentence, record_words (the record's words that make the defect certain), construction (the author's note), problems (automatic checks; should be empty).

Read each bound record at its commit in /home/user/CIC-Project with `git show <commit>:<path>`; find the path with `git ls-tree -r --name-only <commit> records/<world> | grep <last part of the id>`. Commits: worlds alx, desert, don, gallic, hal, ijc, pahc, rzg, syr at fdfcf33dad0c7d0097fef62a3269ee8146c9a91a; witt at 1a716fe86fc084a46b5241dfac5952be65a0c30d; lpc at fcd5768412b60ae64e58c639a5624979679bce6f. Read the whole record, not only record_words. Do not read anything under Build/Ministry/Features/Answering-From-Sources/. Do not use the web or call any model API.

Accept only if all hold:
1. The defect is real, of the stated class, and certain from the record's own words (not from outside knowledge). Class meanings:
   - dropped_negation: drops, adds or reverses a negation, or shifts a modal or quantifier (may to must, some to all, often to always, could to did).
   - attribution_inflation: states as the tradition's own position what the record gives as one author's view, one text, one occasion or one group; or turns one instance into a habit. Reject if the record itself states the position as the tradition's.
   - false_friend: the sentence's claim depends on reading a word in a modern sense the source does not carry, and so asserts something false.
   - embedded_voice: gives as the tradition's own view words that in the record belong to someone else (opponent, interlocutor, quoted correspondent, hostile witness, outsider, editor). Reject if the record shows the tradition also shared that view.
2. There is no second defect: everything else in the sentence is supported by the record (no added names, dates, causes, details, no other shift).
3. It reads like a sentence a Representative could say, in plain English, first person plural; no broken grammar or giveaway wording. A repair may fix grammar or capitals only, never meaning.
4. The record is fit to judge against (it has real text; it is not itself garbled).

Write your readings to OUTFILE (given below) as YAML, one entry per id, in list order:

```yaml
cx-xxxxxxxxxxxx: {verdict: accepted, reason: "one plain sentence"}
cx-yyyyyyyyyyyy: {verdict: rejected, reason: "one plain sentence: which rule fails and why"}
cx-zzzzzzzzzzzz: {verdict: accepted, repair: "the repaired sentence", reason: "..."}
```

Report only the file path and the counts accepted, repaired and rejected, with the main reasons for rejection in a few lines.
