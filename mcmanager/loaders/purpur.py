import os

from mcmanager.utils.downloader import download


def install(version: str, path: str):
    os.makedirs(path, exist_ok=True)
    url = f"https://api.purpurmc.org/v2/purpur/{version}/latest/download"
    dest = os.path.join(path, "server.jar")
    download(url, dest)
