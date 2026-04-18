import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from agent_experience.core.skill_loader import load_skill


@dataclass
class ProbeResult:
    skills: list[dict[str, Any]] = field(default_factory=list)
    hooks: list[dict[str, Any]] = field(default_factory=list)
    agents: list[dict[str, Any]] = field(default_factory=list)
    mcp_servers: list[dict[str, Any]] = field(default_factory=list)
    claude_md: Path | None = None
    settings: dict[str, Any] | None = None
    warnings: list[str] = field(default_factory=list)


def _read_skill(path: Path) -> dict[str, Any] | None:
    try:
        skill = load_skill(path)
    except (ValueError, OSError):
        return None
    return {
        "name": skill.name,
        "description": skill.description,
        "path": str(path),
    }


def probe(project_dir: Path) -> ProbeResult:
    result = ProbeResult()
    if not project_dir.exists():
        return result

    claude_md = project_dir / "CLAUDE.md"
    if claude_md.exists():
        result.claude_md = claude_md

    settings = project_dir / ".claude" / "settings.json"
    if settings.exists():
        try:
            result.settings = json.loads(settings.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            result.warnings.append(f"could not parse {settings}: {e}")

    skills_dir = project_dir / ".claude" / "skills"
    if skills_dir.is_dir():
        for skill_md in skills_dir.glob("*/SKILL.md"):
            parsed = _read_skill(skill_md)
            if parsed:
                result.skills.append(parsed)
            else:
                result.warnings.append(f"could not parse {skill_md}")

    hooks_file = project_dir / ".claude" / "hooks.json"
    if hooks_file.exists():
        try:
            data = json.loads(hooks_file.read_text(encoding="utf-8"))
            for event, entries in data.items():
                result.hooks.append({"event": event, "entries": entries})
        except json.JSONDecodeError as e:
            result.warnings.append(f"could not parse {hooks_file}: {e}")

    return result
