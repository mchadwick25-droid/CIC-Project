"""cic-website/talk.html passes ?ours= on to the framed app and drops it from its own address."""
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

TALK = Path(__file__).resolve().parents[2] / "cic-website" / "talk.html"

RUNNER = r"""
const [script, search, hash] = JSON.parse(process.argv[1]);
const frame = { src: null, contentWindow: {} };
const replaced = [];
const location = { search, hash, pathname: '/talk.html', hostname: 'churchinconversation.com', href: '' };
global.window = {
  location,
  history: { state: null, replaceState: (_s, _t, url) => replaced.push(url) },
  addEventListener: () => {},
};
global.document = {
  getElementById: (id) => (id === 'talk-frame' ? frame : { setAttribute: () => {}, getAttribute: () => '/' }),
};
new Function(script)();
process.stdout.write(JSON.stringify({ src: frame.src, replaced }));
"""


def _page_script() -> str:
    scripts = re.findall(r"<script>(.*?)</script>", TALK.read_text(encoding="utf-8"), re.S)
    return next(s for s in scripts if "talk-frame" in s)


def _run(search: str, hash_: str = "") -> dict:
    out = subprocess.run(
        ["node", "-e", RUNNER, json.dumps([_page_script(), search, hash_])],
        capture_output=True, text=True, check=True, timeout=30,
    )
    return json.loads(out.stdout)


pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")


@pytest.mark.parametrize("value", ["1", "0"])
def test_ours_is_forwarded_and_removed_from_the_page_address(value):
    result = _run(f"?worlds=desert&ours={value}&mode=table", "#q=hello")
    assert result["src"] == f"https://cic-engine.onrender.com/?worlds=desert&mode=table&ours={value}#q=hello"
    assert result["replaced"] == ["/talk.html?worlds=desert&mode=table#q=hello"]


def test_other_ours_values_are_dropped_not_forwarded():
    result = _run("?ours=yes")
    assert result["src"] == "https://cic-engine.onrender.com/?mode=interview"
    assert result["replaced"] == ["/talk.html"]


def test_without_ours_the_target_and_address_are_unchanged():
    result = _run("?worlds=desert")
    assert result["src"] == "https://cic-engine.onrender.com/?worlds=desert&mode=interview"
    assert result["replaced"] == []
