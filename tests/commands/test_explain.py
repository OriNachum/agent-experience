from typer.testing import CliRunner

from agent_experience.cli import app


def test_explain_agex_prints_self_describing_page():
    runner = CliRunner()
    result = runner.invoke(app, ["explain", "agex"])
    assert result.exit_code == 0
    assert "agex" in result.stdout
    assert "overview" in result.stdout
    assert "learn" in result.stdout


def test_explain_explain_reads_command_skill_md():
    runner = CliRunner()
    result = runner.invoke(app, ["explain", "explain"])
    assert result.exit_code == 0
    assert "agex explain" in result.stdout.lower()


def test_explain_unknown_topic_exits_2_with_menu():
    runner = CliRunner()
    result = runner.invoke(app, ["explain", "unknown-topic-xyz"])
    assert result.exit_code == 2
    assert "unknown" in result.stderr.lower()
