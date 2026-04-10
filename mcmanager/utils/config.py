import json
import os

CONFIG_PATH = os.path.expanduser("~/.mcmanager/config.json")


DEFAULT_CONFIG = {
    "servers_path": "~/mcservers",
    "gdrive_mount": "~/gdrive",
    "gdrive_remote": "gdrive",
    "use_playit": False,
    "playit_secret": "",
    "playit_secret_path": "~/.mcmanager/playit_secret.txt",
    "playit_log_path": "~/.mcmanager/playit.log",
    "playit_stop_on_server_stop": True,
    "playit_tunnel_type": "playit"
}


def load_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    try:
        with open(CONFIG_PATH, "r") as f:
            cfg = json.load(f)
        # Merge with defaults to add any new keys from DEFAULT_CONFIG
        merged = DEFAULT_CONFIG.copy()
        merged.update(cfg)
        return merged
    except Exception:
        return DEFAULT_CONFIG.copy()


def save_config(cfg: dict):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)
