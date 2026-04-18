from pathlib import Path

from agent_experience.backends.claude_code.probe import probe


FIXTURES = Path(__file__).parent.parent / "fixtures" / "claude-code"


def test_probe_empty_project():
    result = probe(FIXTURES / "empty")
    assert result.skills == []
    assert result.hooks == []
    assert result.claude_md is None


def test_probe_typical_project():
    result = probe(FIXTURES / "typical")
    assert len(result.skills) == 1
    assert result.skills[0]["name"] == "example"
    assert result.claude_md is not None
    assert "CLAUDE.md" in str(result.claude_md)


def test_probe_missing_directory_returns_empty():
    result = probe(Path("/nonexistent-path-abc-123"))
    assert result.skills == []
