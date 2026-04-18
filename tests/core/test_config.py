from agent_experience.core.config import Config, load, save
from agent_experience.core.paths import ensure_init


def test_load_returns_empty_when_missing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ensure_init()
    cfg = load()
    assert cfg.agex_version == "0.1.0"
    assert cfg.installed == {}
    assert cfg.preferences == {}


def test_save_then_load_roundtrip(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ensure_init()
    cfg = Config(agex_version="0.1.0")
    cfg.installed["gamify"] = {
        "at": "2026-04-18T10:00:00Z",
        "hook_fragment_ids": ["agex:post-tool-use"],
    }
    save(cfg)
    reloaded = load()
    assert reloaded.installed["gamify"]["hook_fragment_ids"] == ["agex:post-tool-use"]
