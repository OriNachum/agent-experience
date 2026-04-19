---
title: Home
layout: default
nav_order: 1
---

# agex

Non-agentic Python CLI that emits deterministic per-backend markdown briefings for autonomous agents. Zero LLM calls inside `agex` itself — all intelligence lives in agent-authored skills that consume `agex`'s output.

## Quickstart

```bash
uv tool install agex-cli       # or: pipx install agex-cli
agex explain agex              # self-describing page
agex overview --agent claude-code
```

- **Repo:** <https://github.com/OriNachum/agex>
- **PyPI:** <https://pypi.org/project/agex-cli/>

See [Getting started](getting-started.html) for a walkthrough.
