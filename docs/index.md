---
title: agex
nav_order: 0
permalink: /
description: Agent experience (agex) CLI — deterministic markdown briefings that teach autonomous agents about their own runtime.
---

<div class="hero">
  <p class="hero-label">Agent experience — not agent execution</p>
  <h1 class="hero-headline">The CLI your agents read&nbsp;first.</h1>
  <p class="hero-sub"><code>agex</code> = <strong>ag</strong>ent <strong>ex</strong>perience. Deterministic, per-backend markdown briefings. Zero LLM calls.</p>
  <div>
    <a href="{{ '/getting-started/' | relative_url }}" class="btn-cta btn-cta--primary">Get started</a>
    <a href="{{ '/commands/' | relative_url }}" class="btn-cta btn-cta--secondary">Browse commands</a>
  </div>
</div>

## Quickstart

```bash
uv tool install agex-cli       # or: pipx install agex-cli
agex explain agex              # self-describing page
agex overview --agent claude-code
```

- **Repo:** <https://github.com/OriNachum/agex>
- **PyPI:** <https://pypi.org/project/agex-cli/>

See [Getting started](getting-started.md) for a walkthrough.
