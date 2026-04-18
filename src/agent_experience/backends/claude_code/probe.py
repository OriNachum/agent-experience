import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

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


def _read_skill(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        skill = load_skill(path)
    except (ValueError, OSError, yaml.YAMLError) as e:
        return None, str(e)
    return (
        {
            "name": skill.name,
            "description": skill.description,
            "path": str(path),
        },
        None,
    )


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
        except (json.JSONDecodeError, OSError) as e:
            result.warnings.append(f"could not parse {settings}: {e}")

    skills_dir = project_dir / ".claude" / "skills"
    if skills_dir.is_dir():
        # Sort for deterministic snapshot ordering across platforms / filesystems.
        for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
            parsed, err = _read_skill(skill_md)
            if parsed is not None:
                result.skills.append(parsed)
            else:
                result.warnings.append(f"could not parse {skill_md}: {err}")

    hooks_file = project_dir / ".claude" / "hooks.json"
    if hooks_file.exists():
        try:
            data = json.loads(hooks_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            result.warnings.append(f"could not parse {hooks_file}: {e}")
        else:
            if not isinstance(data, dict):
                result.warnings.append(
                    f"could not parse {hooks_file}: expected a JSON object"
                )
            else:
                for event, entries in data.items():
                    if not isinstance(entries, list):
                        result.warnings.append(
                            f"could not parse {hooks_file}: expected list "
                            f"for event '{event}'"
                        )
                        continue
                    result.hooks.append({"event": event, "entries": entries})

    return result
