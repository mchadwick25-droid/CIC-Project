"""The question links the shared orientation renderer writes carry their own question into the conversation."""
import json
import shutil
import subprocess
from pathlib import Path
from urllib.parse import unquote

import pytest

RENDERER = Path(__file__).resolve().parents[2] / "cic-website" / "assets" / "orientation-render.mjs"

RUNNER = r"""
const [renderer, compiled] = JSON.parse(process.argv[1]);
const { renderQuestions } = await import(renderer);
process.stdout.write(renderQuestions(compiled, { slug: 'desert-monasticism', representativeName: 'Papnoute' }));
"""

pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")


def _render(questions: list[str]) -> str:
    compiled = {"narrative": {"questions": [
        {"demonstration": {"exchange": [{"speaker": "participant", "text": q}]}, "cite": []} for q in questions
    ]}}
    out = subprocess.run(
        ["node", "--input-type=module", "-e", RUNNER, json.dumps([RENDERER.as_uri(), compiled])],
        capture_output=True, text=True, check=True, timeout=30,
    )
    return out.stdout


def test_each_question_link_carries_its_own_question():
    question = "I can't quiet my own head. Does your way of life have anything for someone like me?"
    html = _render([question])
    href = html.split('href="', 1)[1].split('"', 1)[0].replace("&amp;", "&").replace("&#39;", "'")
    assert href.startswith("../talk.html?worlds=desert-monasticism&mode=interview&from=traditions%2Fdesert-monasticism.html#q=")
    assert unquote(href.split("#q=", 1)[1]) == question


def test_question_links_are_not_rewritten_by_the_held_question_script():
    html = _render(["Who was Jesus, to you and your people?"])
    assert " data-question>" in html
    assert "data-ask" not in html
