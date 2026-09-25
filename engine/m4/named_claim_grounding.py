"""Marker-level grounding for CITATION-TAGGED sentences that already
passed engine.m4.grounding_net's own ratio test (fabrication guard; see
worlds/pahc/Open_Gaps_Tracking.md OG-9 for the traced regression).

THE GAP THIS CLOSES: grounding_net.verdict_for_sentence's ratio test
scores a tagged sentence by the SHARE of its own content words found
anywhere in its tagged records' ground - an aggregate. A wrong proper
noun counts exactly the same as any other matched word, so a sentence
can clear the 40% floor on the strength of its OTHER words while naming
something its own records never named at all. OG-9's own traced case: a
voice turn cited pahc.story.one-eucharist-under-bishop (sources[0].locus
"Philadelphians 4; Smyrnaeans 8"; the record's own text never names a
letter) and said "Ignatius writes it to the Ephesians." "ephesians"
shares zero words with the record's own ground, but the sentence's other
two content words ("ignatius", "writes") were enough to clear the floor
at 67%. engine.m4.uncited_claims's own find_uncited_claims does not
catch this either - it only re-examines UNTAGGED sentences, and this
sentence carried a real tag. No automated check currently insists that
every specific thing a tagged sentence names is actually IN what it
cites; an aggregate share has no way to do that by construction. This
module adds the one thing it cannot: for each proper noun and number
engine.prose.claim_markers finds in a tagged, passing sentence, that
exact name or number must itself appear in the ground its own tags
supply - not just contribute to a passing average.

GROUND SCOPE - what a marker is allowed to match against:
  - the tagged record's own text, exactly what grounding_net's ratio
    test already scores against (engine.prose.all_text, which already
    walks the record's own sources[].locus string - "philadelphians"
    and "smyrnaeans" are already in there for the OG-9 record; "ephesians"
    is not)
  - PLUS, for each of the record's own sources[] entries, the resolved
    source record's own `work` field, truncated through engine.prose.
    short_head() - the same truncation engine.m2.builders' own
    retrieval_words() already applies to this exact field, and for the
    same reason: a source row's `work` can be an omnibus covering
    several works at once. pahc.source.ignatius-letters' own `work`
    field opens "The seven letters, middle recension (Ephesians,
    Magnesians, Trallians, Romans, Philadelphians, Smyrnaeans, To
    Polycarp); traditional dating..." - the full seven-letter
    enumeration sits in that field's own scholarly apparatus, in
    parentheses, exactly the shape short_head() exists to drop. Matching
    the untruncated field would let "Ephesians" ground itself off the
    very sentence this module exists to catch, since it names one of the
    seven letters the omnibus source row covers even though this
    record's own locus never cites it. Reusing short_head() (rather than
    a second, separately-tuned truncation) is why the OG-9 fixture in
    this module's own tests still gets caught.

Numbers are grounded against literal digit/spelled-cardinal tokens
pulled straight from the same two texts (content_words() strips digits
entirely, since engine.prose._WORD only matches letters - a locus like
"Philadelphians 4" would otherwise never ground a "4" a sentence names),
kept as a separate check from proper nouns because "does this exact
number appear" and "does this exact name appear" are different lookups
over the same ground, not the same lookup twice. Each side is checked
by its own exact surface form only, digit against digit and spelled
word against spelled word - never against each other. Known, accepted
limit: a claim stated as a digit ("137") is not recognized as the same
number as a record naming it spelled out ("one hundred thirty-seven"),
or the reverse; a digit/word form mismatch flags exactly the way a
genuinely absent number would.

A value-composing cross-form check (parsing both sides to one integer,
"137"/"one hundred thirty-seven" grounding as the same value) was built,
found still unsafe on review after two rounds of narrowing (an "and"
between a hundred-block and its own remainder, and two adjacent numbers
sitting next to each other with nothing joining them, both had to be
special-cased in the parser's own grammar to avoid silently composing a
value neither side of a claim actually states), and removed entirely
per the same "no fix on a fix" rule that removed the derivational
bridge above - not reintroduced here. The digit/word mismatch this
leaves is a named, accepted false-positive class, not a defect this
module is scoped to fix.

A trailing possessive ('s, or a bare trailing ' on a plural like
"disciples'") is stripped from both the marker and the ground before
comparing, since engine.prose._WORD keeps the apostrophe as part of the
word: a sentence saying "Ignatius's letter" and a record naming plain
"Ignatius" must ground each other. Known, accepted limit, NOT resolved
here: a different derivational form of the same name (a record naming
"Smyrna" does not itself ground a sentence saying "Smyrnaeans," and
naming "Alexandria" does not ground "Alexandrian," or the reverse) is a
different token this module does not equate - report-only noise, not a
false negative this module is scoped to fix.

A bridge between exactly this pattern (a place name ending in "a" and
its own bare-"n" adjective) was tried and removed: the same surface
shape covers real people too - Julian/Julia, Hadrian/Hadria,
Lucian/Lucia, Domitian/Domitia, Sebastian/Sebastia, Flavian/Flavia, and
Claudian/Claudia all fit it without being the same word at all (every
one is properly derived from a DIFFERENT root spelled with a trailing
"n" already - Julian from Julius, not Julia - and only collides on this
surface shape). Gating the bridge on a world's own figure records
(known people) still let every one of these through, because none of
them happened to be a figure record in the worlds tested - the gate
needs a POSITIVE place signal to be safe, and no world's own compiled
repository carries place records to check against yet. Rather than
carry a bridge with a known, currently-live false-grounding class,
Alexandria/Alexandrian is named here as an accepted, unfixed
false-positive class, the same status Smyrna/Smyrnaeans already has - a
real place-vs-person design, if built later, needs its own ruling and
its own PR, not a patch on this one.

Report-only: this module never withholds or edits a turn's text.
find_named_claim_flags is meant to be called the same unconditional way
find_uncited_claims/find_uncited_paragraphs already are
(engine.m4.turn._run_ordinary_voice_turn), adding its own additive
voice_event key with no change to any existing behavior. Enforcement -
what a caught sentence's own regeneration/correction should say, and
under what flag it activates - is deliberately left to a later,
separately-ruled PR: this file only makes the finding checkable and
auditable.
"""
import ast
import re

from engine.prose import SPELLED_NUMBERS, all_text, claim_markers, content_words, short_head

_WORD = re.compile(r"[a-zA-Z']+")
_DIGIT = re.compile(r"\b\d+\b")


def _number_tokens(text: str) -> tuple[set[str], set[str]]:
    """(digit tokens, spelled-cardinal words) literally present in
    `text` - claim_markers()'s own "number" marker only signals THAT a
    checkable number is present (engine.prose._has_number's own
    discourse-count exemption already decided that); this pulls the
    actual value(s) so they can be checked against ground, the same way
    _proper_noun_words pulls actual names rather than re-deciding
    whether any exist. Each side is its own exact-surface-form token set
    - never composed into one cross-form value (see module docstring's
    own known-limit note)."""
    digits = set(_DIGIT.findall(text))
    spelled = {w.lower() for w in _WORD.findall(text)} & SPELLED_NUMBERS
    return digits, spelled


def _source_ground(record: dict, repository_records: dict[str, dict]) -> tuple[set[str], set[str]]:
    """(word ground, digit ground) contributed by a record's own
    sources[], resolved through source_id to each source record's `work`
    field - see this module's own docstring, GROUND SCOPE, for why
    short_head() runs first. A source_id that doesn't resolve, or a
    source record with no `work`, contributes nothing (an unresolvable
    tag is a different, already-checked defect - grounding_net.
    verdict_for_sentence withholds on an unresolvable citation TAG; a
    dangling source_id inside a record that DID resolve is not this
    module's job to report a second time)."""
    words: set[str] = set()
    digits: set[str] = set()
    for src in record.get("sources") or []:
        source_id = src.get("source_id") if isinstance(src, dict) else None
        source_rec = repository_records.get(source_id) if source_id else None
        work = source_rec.get("work") if source_rec else None
        if not work:
            continue
        head = short_head(work)
        words |= content_words(head)
        digits |= set(_DIGIT.findall(head))
    return words, digits


def _strip_possessive(word: str) -> str:
    """Drops a trailing "'s" or a bare trailing "'" so "ignatius's" and
    "ignatius" compare equal - engine.prose._WORD keeps the apostrophe
    as part of the word, so neither a marker nor a ground word had this
    stripped before, and a real name matched only when both sides
    happened to use the same grammatical case. Does not touch a
    different derivational form of the same name (see module
    docstring's own known-limit note)."""
    if word.endswith("'s"):
        return word[:-2]
    if word.endswith("'"):
        return word[:-1]
    return word


def _proper_noun_words(marker: str) -> set[str]:
    """claim_markers() encodes a proper-noun marker as
    "proper-noun:['name', ...]" (engine.prose.claim_markers, built from
    sorted(proper_nouns)) - pull the actual lowercased words back out of
    that literal-list repr rather than re-detecting them a second,
    separately-tuned way. A name of more than one word ("John
    Chrysostom") is split into its own words, same granularity ground
    matching already uses everywhere else in this pipeline (content_words)."""
    prefix = "proper-noun:"
    if not marker.startswith(prefix):
        return set()
    try:
        names = ast.literal_eval(marker[len(prefix):])
    except (ValueError, SyntaxError):
        return set()
    return {_strip_possessive(word.lower()) for name in names for word in name.split()}


def record_ground(rec: dict, repository_records: dict[str, dict]) -> tuple[set[str], set[str]]:
    """(word ground, digit ground) one record contributes on its own: its
    own `all_text`, plus its `sources[]`' resolved `work` fields (see
    `_source_ground`). Factored out of `ungrounded_markers` so the same
    per-record computation can be summed either over just a sentence's
    own tags (below) or over an entire repository
    (`repository_ground`, `engine.m4.sentence_fact_check`'s own ground) -
    one implementation of "what does this record ground," not two."""
    rec_text = all_text(rec)
    words = content_words(rec_text)
    digits = set(_DIGIT.findall(rec_text))
    src_words, src_digits = _source_ground(rec, repository_records)
    return words | src_words, digits | src_digits


def repository_ground(repository_records: dict[str, dict]) -> tuple[set[str], set[str]]:
    """(word ground, digit ground) the world's ENTIRE compiled repository
    supplies - every record's own `record_ground`, unioned, regardless of
    which record (if any) a given sentence happens to tag. This is the
    wider scope `engine.m4.sentence_fact_check` needs (a claim can be
    genuinely supported by the world's own records without the speaking
    sentence tagging the right one, or tagging anything at all) - not a
    substitute for `ungrounded_markers`'s own narrower, tag-scoped ground,
    which stays exactly as calibrated (OG-9) for the already-tagged,
    already-passing sentences it exists to double-check."""
    words: set[str] = set()
    digits: set[str] = set()
    for rec in repository_records.values():
        rec_words, rec_digits = record_ground(rec, repository_records)
        words |= rec_words
        digits |= rec_digits
    return {_strip_possessive(w) for w in words}, digits


def missing_markers(
    text: str, ground_words: set[str], ground_digits: set[str], *, include_sentence_initial_proper_nouns: bool = False
) -> list[str]:
    """Every proper-noun word and number `claim_markers()` finds in `text`
    that is not itself present in the given (word, digit) ground - the
    shared comparison both `ungrounded_markers` (tag-scoped) and
    `engine.m4.sentence_fact_check` (whole-repository-scoped) run, so the
    two checks can never silently diverge on what counts as "grounded."
    Empty for a sentence naming no checkable marker at all.

    A proper noun is compared by its own exact surface form only (see
    module docstring's own known-limit note on derivational form - tried
    as a bridge once, removed for cross-grounding real people, not
    reintroduced here). A number is compared by its own exact surface
    form too - a digit token against `ground_digits`, a spelled-cardinal
    word against `ground_words` - never against each other (see module
    docstring's own known-limit note on digit/word form mismatch: a
    value-composing cross-form check was tried and removed).

    include_sentence_initial_proper_nouns (default False - `ungrounded_
    markers` below keeps claim_markers' own narrower, calibrated default):
    threaded straight through to `claim_markers`. `engine.m4.
    sentence_fact_check` passes True - see `engine.prose._proper_nouns`'
    own docstring for why whole-repository ground scope makes that safe
    where a 1-3-record tag scope would not be."""
    missing: set[str] = set()
    for marker in claim_markers(text, include_sentence_initial_proper_nouns=include_sentence_initial_proper_nouns):
        if marker.startswith("proper-noun:"):
            for word in _proper_noun_words(marker):
                if word not in ground_words:
                    missing.add(word)
        elif marker == "number":
            digits, spelled = _number_tokens(text)
            missing |= digits - ground_digits
            missing |= spelled - ground_words
    return sorted(missing)


def ungrounded_markers(text: str, tags: list[str], *, repository_records: dict[str, dict]) -> list[str]:
    """Every proper-noun word and number claim_markers() finds in `text`
    that does not itself appear in the ground `tags` actually supply (see
    module docstring, GROUND SCOPE). Empty for an untagged sentence, or a
    sentence naming no checkable marker at all - this narrows an already-
    passing sentence's own claim, it does not decide whether the sentence
    should have been tagged in the first place (grounding_net's own job).
    An unresolvable tag id contributes no ground and is silently skipped
    here (grounding_net.verdict_for_sentence already withholds on that
    case, before this check would ever see the sentence live)."""
    if not tags:
        return []
    tagged_records = [repository_records[t] for t in tags if t in repository_records]
    if not tagged_records:
        return []

    ground_words: set[str] = set()
    ground_digits: set[str] = set()
    for rec in tagged_records:
        rec_words, rec_digits = record_ground(rec, repository_records)
        ground_words |= rec_words
        ground_digits |= rec_digits
    ground_words = {_strip_possessive(w) for w in ground_words}

    return missing_markers(text, ground_words, ground_digits)


def verdict_for_sentence(text: str, tags: list[str], *, repository_records: dict[str, dict]) -> dict:
    """One sentence's report-only verdict - same entry shape
    (sentence/tags/verdict/why) as grounding_net.verdict_for_sentence, so
    a caller can log this alongside the ratio-test verdict without a
    second schema. "flag", never "withhold": this module never
    substitutes for the net's own pass/fail (see module docstring)."""
    missing = ungrounded_markers(text, tags, repository_records=repository_records)
    if not missing:
        return {"sentence": text, "tags": tags, "verdict": "ok", "why": None}
    return {
        "sentence": text, "tags": tags, "verdict": "flag",
        "why": f"named claim(s) not found in cited record(s)' own ground: {missing}",
        "missing": missing,
    }


def find_named_claim_flags(sentences: list[dict], *, repository_records: dict[str, dict]) -> list[dict]:
    """Report-only entry point, same calling shape as
    engine.m4.uncited_claims.find_uncited_claims: takes the same
    net_result["sentences"] list grounding_net.check_turn(_with_paragraph_
    coverage) already produced (no second sentence split), returns [] on
    a clean turn. Examines only sentences the ratio test already passed
    WITH a tag (verdict == "ok" and tags) - the sentences that actually
    reach a participant; a withheld sentence never streams, so auditing
    it a second time here adds no participant-facing signal. Each flag:
    {"sentence", "tags", "class": "named_claim_not_grounded", "missing"} -
    "missing" is this sentence's own ungrounded_markers() result, kept on
    the flag (unlike engine.m4.uncited_claims's own bare {sentence,
    class} offenses) because unlike an uncited claim's "why" - there is
    no citation at all - a named-claim flag is meaningless without
    saying WHICH name or number failed to ground."""
    flags = []
    for sent in sentences:
        if sent.get("verdict") != "ok" or not sent.get("tags"):
            continue
        missing = ungrounded_markers(sent["sentence"], sent["tags"], repository_records=repository_records)
        if missing:
            flags.append({
                "sentence": sent["sentence"], "tags": sent["tags"],
                "class": "named_claim_not_grounded", "missing": missing,
            })
    return flags
