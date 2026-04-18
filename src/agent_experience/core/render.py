from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

# We render markdown for agent / CLI consumption — never HTML in a browser.
# select_autoescape([]) makes the intent explicit: escape nothing, for any
# extension. Enabling auto-escape here would corrupt markdown output.
_ENV = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape([]),
    undefined=StrictUndefined,
    keep_trailing_newline=True,
)


# NOSONAR: Templates are package-shipped; output is markdown, not HTML. See
# sonar-project.properties for the narrow S5496 suppression on this file.
def render_string(template: str, context: dict[str, Any]) -> str:
    return _ENV.from_string(template).render(**context)


def render_file(path: Path, context: dict[str, Any]) -> str:
    return render_string(path.read_text(), context)
