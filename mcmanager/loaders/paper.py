import os

from mcmanager.utils.downloader import download


def install(version: str, path: str):
    os.makedirs(path, exist_ok=True)
    url = f"https://api.papermc.io/v2/projects/paper/versions/{version}/builds/latest/downloads/paper-{version}.jar"
    dest = os.path.join(path, "server.jar")
    download(url, dest)
