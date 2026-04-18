"""Tests for unknown-command routing and CLI entry-point behaviour.

All tests use subprocess so that sys.argv manipulation inside
_main_entrypoint is exercised rather than bypassed by CliRunner.
"""
import subprocess
import sys


def test_unknown_command_emits_agex_page_and_exits_2(tmp_path):
    """An unknown subcommand prints agex explain agex to stdout and exits 2."""
    result = subprocess.run(
        [sys.executable, "-m", "agent_experience", "frobnicate"],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    assert result.returncode == 2
    assert "agex" in result.stdout
    assert "overview" in result.stdout
    assert "unknown command" in result.stderr.lower()


def test_known_command_still_works(tmp_path):
    """A known command (explain agex) still routes correctly and exits 0."""
    result = subprocess.run(
        [sys.executable, "-m", "agent_experience", "explain", "agex"],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    assert result.returncode == 0
    assert "agex" in result.stdout


def test_version_flag_still_works(tmp_path):
    """The --version flag bypasses the unknown-command handler and exits 0."""
    result = subprocess.run(
        [sys.executable, "-m", "agent_experience", "--version"],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    assert result.returncode == 0
    # Version string is a non-empty line on stdout
    assert result.stdout.strip() != ""


def test_zero_args_shows_help(tmp_path):
    """Invoking agex with no arguments triggers the Typer no_args_is_help path."""
    result = subprocess.run(
        [sys.executable, "-m", "agent_experience"],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    combined = result.stdout + result.stderr
    assert result.returncode != 0
    assert "Usage:" in combined
