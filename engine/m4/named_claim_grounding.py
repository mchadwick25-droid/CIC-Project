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

Numbers are grounded against composed VALUES pulled straight from the
same two texts (content_words() strips digits entirely, since
engine.prose._WORD only matches letters - a locus like "Philadelphians
4" would otherwise never ground a "4" a sentence names), kept as a
separate check from proper nouns because "does this exact number
appear" and "does this exact name appear" are different lookups over
the same ground, not the same lookup twice. `_numbers_in_text` parses
each contiguous run of digit or spelled-cardinal words into its own
integer value ("137" or "one hundred thirty-seven" both parse to 137)
and every comparison is by that exact value - never by whether the
individual WORDS composing a number happen to overlap with the ground,
which is how an earlier version of this check let "seven" ground itself
off an unrelated "twenty-seven" somewhere else in the same ground. The
same fact stated in a different surface form is one grounded value on
either side of the check; a genuinely different number is not, no
matter how many of its own component words happen to already be common
ground vocabulary.

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

from engine.prose import all_text, claim_markers, content_words, short_head

_WORD = re.compile(r"[a-zA-Z']+")
_DIGIT = re.compile(r"\b\d+\b")


_ONES_VALUES = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
_TEENS_VALUES = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
}
_TENS_VALUES = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}


def _parse_below_hundred(tokens: list[str], i: int) -> tuple[int, int | None]:
    """(new_i, value 1-99) or (i, None): a tens word with an optional
    trailing ones word ("twenty" -> 20, "twenty seven" -> 27), or a bare
    teens/ones word alone ("fifteen" -> 15, "seven" -> 7). Never sums two
    values that do not compose one number this way: "twenty" followed by
    "fifteen" stops after "twenty" (20) - a tens word may only be
    followed by a ONES word, never a teens word, so "fifteen" is left
    for the next, separate number to claim."""
    if i >= len(tokens):
        return i, None
    w = tokens[i]
    if w in _TENS_VALUES:
        j = i + 1
        if j < len(tokens) and tokens[j] in _ONES_VALUES:
            return j + 1, _TENS_VALUES[w] + _ONES_VALUES[tokens[j]]
        return j, _TENS_VALUES[w]
    if w in _ONES_VALUES:
        return i + 1, _ONES_VALUES[w]
    if w in _TEENS_VALUES:
        return i + 1, _TEENS_VALUES[w]
    return i, None


def _parse_below_thousand(tokens: list[str], i: int) -> tuple[int, int | None]:
    """(new_i, value 1-999) or (i, None): an "<ones> hundred [and]?
    [below-hundred]?" block, or - with no "hundred" - a bare below-100
    value. "and" is consumed only directly between "hundred" and what
    follows it ("one hundred and thirty seven" -> 137); it never joins
    two otherwise-separate numbers."""
    n = len(tokens)
    if i >= n:
        return i, None
    w = tokens[i]
    if w in _ONES_VALUES:
        j = i + 1
        if j < n and tokens[j] == "hundred":
            hundred_value = _ONES_VALUES[w] * 100
            k = j + 1
            if k < n and tokens[k] == "and":
                k += 1
            rest_end, rest_val = _parse_below_hundred(tokens, k)
            if rest_val is not None:
                return rest_end, hundred_value + rest_val
            return j + 1, hundred_value
    return _parse_below_hundred(tokens, i)


def _parse_cardinal(tokens: list[str], i: int) -> tuple[int, int | None]:
    """(new_i, value) or (i, None): the longest well-formed cardinal
    starting at tokens[i] - an optional "<below-1000> thousand"
    multiplier, plus an optional "[and]? <below-1000>" remainder. Two
    complete numbers sitting next to each other with nothing joining
    them (no "hundred"/"thousand" continuation, no "and") are each their
    own value, never summed: "fifteen twenty-seven" parses "fifteen"
    (15) here and leaves "twenty-seven" (27) for the next call."""
    n = len(tokens)
    end, val = _parse_below_thousand(tokens, i)
    if val is None:
        return i, None
    if end < n and tokens[end] == "thousand":
        total = val * 1000
        j = end + 1
        if j < n and tokens[j] == "and":
            j += 1
        rem_end, rem_val = _parse_below_thousand(tokens, j)
        if rem_val is not None:
            return rem_end, total + rem_val
        return end + 1, total
    return end, val


def _numbers_in_text(text: str) -> list[tuple[str, int]]:
    """Every checkable number in `text`, as (surface, value) pairs: a
    literal digit run ("137" -> ("137", 137)) or the longest well-formed
    spelled-cardinal phrase starting at each position
    (`_parse_cardinal` - "one hundred and thirty seven" -> ("one hundred
    and thirty seven", 137)). The single source both directions of
    missing_markers' own number check read from, so a composed value is
    compared against ground as the one number it actually is, never
    decomposed into individual words checked against an unordered bag -
    the root cause of a real measured bug in an earlier version of this
    check: "seven" counted as grounded because some UNRELATED number in
    the ground happened to be spelled with "seven" as one of its own
    components ("twenty-seven"). A bag of words cannot tell "seven" and
    "twenty-seven" apart; a parsed value can, and does. A later version
    of this same check summed every contiguous number word into one
    total regardless of whether they composed a real cardinal together -
    "fifteen twenty-seven" read as 15+20+7=42, a value neither number in
    the text. `_parse_cardinal`'s own grammar (below-hundred, below-
    thousand, the full cardinal) only ever extends a value when the next
    word can grammatically continue it; two complete numbers sitting
    next to each other with nothing joining them are parsed as two
    separate values, never one summed value.

    A phrase never STARTS on a bare "one" (the same reading SPELLED_
    NUMBERS' own comment already names as the single largest false-
    positive source measured for detection: "one" read as a pronoun or
    article, not a quantity) - but "one" already inside an in-progress
    phrase ("twenty-one", or the "one" that opens "one hundred") is still
    counted, since `_parse_cardinal` only ever reaches it as the second
    token of a run some OTHER word already started."""
    results: list[tuple[str, int]] = [(m.group(), int(m.group())) for m in _DIGIT.finditer(text)]
    words = _WORD.findall(text)
    lowered = [w.lower() for w in words]
    n = len(lowered)
    i = 0
    while i < n:
        if lowered[i] == "one" and (i + 1 >= n or lowered[i + 1] not in ("hundred", "thousand")):
            i += 1
            continue
        end, value = _parse_cardinal(lowered, i)
        if value is None:
            i += 1
            continue
        results.append((" ".join(words[i:end]).lower(), value))
        i = end
    return results


def _source_ground(record: dict, repository_records: dict[str, dict]) -> tuple[set[str], set[int]]:
    """(word ground, number-value ground) contributed by a record's own
    sources[], resolved through source_id to each source record's `work`
    field - see this module's own docstring, GROUND SCOPE, for why
    short_head() runs first. A source_id that doesn't resolve, or a
    source record with no `work`, contributes nothing (an unresolvable
    tag is a different, already-checked defect - grounding_net.
    verdict_for_sentence withholds on an unresolvable citation TAG; a
    dangling source_id inside a record that DID resolve is not this
    module's job to report a second time)."""
    words: set[str] = set()
    numbers: set[int] = set()
    for src in record.get("sources") or []:
        source_id = src.get("source_id") if isinstance(src, dict) else None
        source_rec = repository_records.get(source_id) if source_id else None
        work = source_rec.get("work") if source_rec else None
        if not work:
            continue
        head = short_head(work)
        words |= content_words(head)
        numbers |= {value for _, value in _numbers_in_text(head)}
    return words, numbers


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


def record_ground(rec: dict, repository_records: dict[str, dict]) -> tuple[set[str], set[int]]:
    """(word ground, number-value ground) one record contributes on its
    own: its own `all_text`, plus its `sources[]`' resolved `work` fields
    (see `_source_ground`). Factored out of `ungrounded_markers` so the
    same per-record computation can be summed either over just a
    sentence's own tags (below) or over an entire repository
    (`repository_ground`, `engine.m4.sentence_fact_check`'s own ground) -
    one implementation of "what does this record ground," not two."""
    rec_text = all_text(rec)
    words = content_words(rec_text)
    numbers = {value for _, value in _numbers_in_text(rec_text)}
    src_words, src_numbers = _source_ground(rec, repository_records)
    return words | src_words, numbers | src_numbers


def repository_ground(repository_records: dict[str, dict]) -> tuple[set[str], set[int]]:
    """(word ground, number-value ground) the world's ENTIRE compiled
    repository supplies - every record's own `record_ground`, unioned,
    regardless of which record (if any) a given sentence happens to tag.
    This is the wider scope `engine.m4.sentence_fact_check` needs (a
    claim can be genuinely supported by the world's own records without
    the speaking sentence tagging the right one, or tagging anything at
    all) - not a substitute for `ungrounded_markers`'s own narrower,
    tag-scoped ground, which stays exactly as calibrated (OG-9) for the
    already-tagged, already-passing sentences it exists to double-check."""
    words: set[str] = set()
    numbers: set[int] = set()
    for rec in repository_records.values():
        rec_words, rec_numbers = record_ground(rec, repository_records)
        words |= rec_words
        numbers |= rec_numbers
    return {_strip_possessive(w) for w in words}, numbers


def missing_markers(
    text: str,
    ground_words: set[str],
    ground_numbers: set[int],
    *,
    include_sentence_initial_proper_nouns: bool = False,
) -> list[str]:
    """Every proper-noun word and number `claim_markers()` finds in `text`
    that is not itself present in the given ground - the shared
    comparison both `ungrounded_markers` (tag-scoped) and
    `engine.m4.sentence_fact_check` (whole-repository-scoped) run, so the
    two checks can never silently diverge on what counts as "grounded."
    Empty for a sentence naming no checkable marker at all.

    A proper noun is compared by its own exact surface form only (see
    module docstring's own known-limit note on derivational form - tried
    as a bridge once, removed for cross-grounding real people, not
    reintroduced here). A number grounds against its own composed VALUE
    (`_numbers_in_text`) found anywhere in `ground_numbers`, digit or
    spelled-out - "137" and "one hundred thirty-seven" are one grounded
    value, compared exactly, never a bag of components that could belong
    to a different number entirely.

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
            for surface, value in _numbers_in_text(text):
                if value not in ground_numbers:
                    missing.add(surface)
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
    ground_numbers: set[int] = set()
    for rec in tagged_records:
        rec_words, rec_numbers = record_ground(rec, repository_records)
        ground_words |= rec_words
        ground_numbers |= rec_numbers
    ground_words = {_strip_possessive(w) for w in ground_words}

    return missing_markers(text, ground_words, ground_numbers)


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
