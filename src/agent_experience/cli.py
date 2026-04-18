from typing import Optional

import typer

from agent_experience import __version__

app = typer.Typer(
    name="agex",
    help="Agent-operated developer-experience CLI.",
    no_args_is_help=True,
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=_version_callback, is_eager=True
    ),
) -> None:
    pass
