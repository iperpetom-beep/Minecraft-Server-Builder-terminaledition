import json
import os
import requests

from mcmanager.utils.downloader import download


MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"


def install(version: str, path: str):
    """Install a vanilla server of the given version into path."""
    os.makedirs(path, exist_ok=True)
    # fetch manifest
    resp = requests.get(MANIFEST_URL)
    resp.raise_for_status()
    manifest = resp.json()
    # find version entry
    entry = next((v for v in manifest.get("versions", []) if v.get("id") == version), None)
    if not entry:
        raise ValueError(f"Minecraft version {version} not found in manifest")
    ver_json = requests.get(entry["url"]).json()
    server_info = ver_json.get("downloads", {}).get("server")
    if not server_info:
        raise ValueError("server download info not found")
    url = server_info["url"]
    dest = os.path.join(path, "server.jar")
    download(url, dest)
