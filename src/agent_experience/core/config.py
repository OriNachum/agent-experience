from dataclasses import dataclass, field
from typing import Any

import tomlkit

from agent_experience.core.paths import config_path


@dataclass
class Config:
    agex_version: str = "0.1.0"
    backend: str | None = None
    installed: dict[str, dict[str, Any]] = field(default_factory=dict)
    preferences: dict[str, Any] = field(default_factory=dict)


def load() -> Config:
    path = config_path()
    if not path.exists():
        return Config()
    doc = tomlkit.parse(path.read_text())
    return Config(
        agex_version=doc.get("agex_version", "0.1.0"),
        backend=doc.get("backend"),
        installed=dict(doc.get("installed", {})),
        preferences=dict(doc.get("preferences", {})),
    )


def save(cfg: Config) -> None:
    doc = tomlkit.document()
    doc["agex_version"] = cfg.agex_version
    if cfg.backend is not None:
        doc["backend"] = cfg.backend
    if cfg.installed:
        doc["installed"] = cfg.installed
    if cfg.preferences:
        doc["preferences"] = cfg.preferences
    config_path().write_text(tomlkit.dumps(doc))
