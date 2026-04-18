from importlib.resources import files
from pathlib import Path

from agent_experience.core.skill_loader import load_skill


def _commands_root() -> Path:
    return Path(str(files("agent_experience.commands")))


def resolve_topic(topic: str) -> tuple[str, Path] | None:
    """Resolve topic per spec precedence. Returns (kind, path) or None."""
    cmds = _commands_root()

    cmd_skill = cmds / topic / "SKILL.md"
    if cmd_skill.exists():
        return ("command", cmd_skill)

    lesson_skill = cmds / "learn" / "assets" / "topics" / topic / "SKILL.md"
    if lesson_skill.exists():
        return ("lesson", lesson_skill)

    concept = cmds / "explain" / "assets" / "topics" / f"{topic}.md"
    if concept.exists():
        return ("concept", concept)

    return None


def run(topic: str) -> tuple[str, int, str]:
    """Return (stdout, exit_code, stderr)."""
    resolved = resolve_topic(topic)
    if resolved is None:
        agex_page = _commands_root() / "explain" / "assets" / "topics" / "agex.md"
        body = agex_page.read_text() if agex_page.exists() else ""
        return (body, 2, f"agex: error: unknown topic '{topic}'")

    kind, path = resolved
    if kind == "concept":
        return (path.read_text(), 0, "")
    skill = load_skill(path)
    return (skill.body, 0, "")
