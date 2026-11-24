import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from check_brief_craft import check_text  # noqa: E402


def kinds(text):
    return {item["check"] for item in check_text(text)}


def test_lists_each_named_tell():
    text = (
        "He was not a rebel, but a reformer. His legacy lives on. "
        "The sources do not say where he died. A modern historian takes him for the bishop. "
        "Socrates says he was proud. He wrote a book. Who was he? He was a monk."
    )
    found = kinds(text)
    for name in (
        "not X but Y",
        "stock word",
        "silence sentence",
        "modern-scholar word",
        "names a source",
        "possible bare statement",
        "question",
    ):
        assert name in found, name


def test_clean_narration_lists_nothing():
    text = (
        "In 399 John climbed into the pulpit while Eutropius lay under the altar. "
        "He told the crowd the church had hidden her enemy under her cloak."
    )
    assert check_text(text) == []


def test_long_sentence_is_listed():
    text = " ".join(["word"] * 31) + "."
    assert any(i["check"].startswith("over 30 words") for i in check_text(text))
