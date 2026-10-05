"""The app's Go Deeper switches reach the Docker build, so a Render service's environment can turn the panel on."""
import re
from pathlib import Path

DOCKERFILE = (Path(__file__).resolve().parents[2] / "Dockerfile").read_text()


def test_both_build_switches_are_declared_and_exported_before_the_frontend_build():
    build = DOCKERFILE.index("RUN npm run build")
    for name in ("VITE_DEEPER_ENABLED", "VITE_DEEPER_SITE_ORIGIN"):
        arg = re.search(rf'^ARG {name}=""$', DOCKERFILE, re.M)
        assert arg and arg.start() < build, name
        env = re.search(rf"^ENV .*\b{name}=\${name}\b", DOCKERFILE, re.M)
        assert env and env.start() < build, name


def test_the_switches_default_to_off_so_an_unset_service_builds_the_module_dark():
    assert 'ARG VITE_DEEPER_ENABLED=""' in DOCKERFILE


def test_the_build_log_prints_whether_the_switch_arrived_before_the_frontend_build():
    echo = DOCKERFILE.index("RUN echo \"Go Deeper app build: VITE_DEEPER_ENABLED=")
    assert DOCKERFILE.index('ARG VITE_DEEPER_ENABLED=""') < echo < DOCKERFILE.index("RUN npm run build")
