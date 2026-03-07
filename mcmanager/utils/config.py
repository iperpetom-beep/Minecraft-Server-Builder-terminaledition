import json
import os

CONFIG_PATH = os.path.expanduser("~/.mcmanager/config.json")


DEFAULT_CONFIG = {
    "servers_path": "~/mcservers",
    "gdrive_mount": "~/gdrive",
    "gdrive_remote": "gdrive",
    "use_playit": False
}


def load_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_CONFIG.copy()


def save_config(cfg: dict):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)
