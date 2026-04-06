import os
import subprocess
import requests

from mcmanager.utils.downloader import download
from mcmanager.utils.java import ensure_java


def install(version: str, path: str):
    os.makedirs(path, exist_ok=True)
    # check if version is supported
    resp = requests.get("https://meta.fabricmc.net/v2/versions/game")
    resp.raise_for_status()
    games = resp.json()
    if not any(g.get("version") == version and g.get("stable") for g in games):
        raise ValueError(f"Fabric does not support Minecraft version {version}")
    # get latest loader version
    resp = requests.get(f"https://meta.fabricmc.net/v2/versions/loader/{version}")
    resp.raise_for_status()
    loaders = resp.json()
    if not loaders:
        raise ValueError(f"No Fabric loaders for Minecraft {version}")
    # API returns sorted latest first, but ensure we have a stable loader
    latest_loader = next((l for l in loaders if l.get("loader", {}).get("stable", False)), loaders[0])
    loader_version = latest_loader["loader"]["version"]
    # get latest installer version
    resp = requests.get("https://meta.fabricmc.net/v2/versions/installer")
    resp.raise_for_status()
    installers = resp.json()
    latest_installer = next((i for i in installers if i.get("stable")), installers[0])
    installer_version = latest_installer["version"]
    # download executable server jar
    jar_url = f"https://meta.fabricmc.net/v2/versions/loader/{version}/{loader_version}/{installer_version}/server/jar"
    server_jar = os.path.join(path, "server.jar")
    download(jar_url, server_jar)
