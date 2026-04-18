from pathlib import Path

from agent_experience.backends.claude_code.probe import ProbeResult


def probe(project_dir: Path) -> ProbeResult:
    """Stub Copilot probe — v0.1 returns empty. Full discovery tracked as open issue."""
    return ProbeResult()
