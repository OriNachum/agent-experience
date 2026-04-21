# agex

Short for **ag**ent **ex**perience (not agent *execution*) — the deterministic, non-agentic CLI that briefs autonomous agents on their own runtime. Markdown-first; zero LLM calls. Distributed on PyPI as `agex-cli`; installs the `agex` command.

## Install

```bash
uv tool install agex-cli
# or
pipx install agex-cli
```

## Quick start

```bash
agex explain agex
agex overview --agent claude-code
agex learn --agent claude-code
```

## Docs

[culture.dev/agex](https://culture.dev/agex/).

Spec: `docs/superpowers/specs/2026-04-18-agex-design.md`.

## License

MIT.
