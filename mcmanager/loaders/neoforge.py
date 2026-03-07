import os
import subprocess
import xml.etree.ElementTree as ET
import requests

from mcmanager.utils.downloader import download
from mcmanager.utils.java import ensure_java


def get_latest_neoforge_version(mc_version: str) -> str:
    """Get the latest NeoForge version for a given Minecraft version."""
    url = f"https://maven.neoforged.net/releases/net/neoforged/neoforge/maven-metadata.xml"
    resp = requests.get(url)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    versions = [v.text for v in root.findall(".//version") if v.text.startswith(f"{mc_version}.")]
    if not versions:
        raise ValueError(f"No NeoForge versions found for Minecraft {mc_version}")
    return max(versions)


def install(version: str, path: str):
    os.makedirs(path, exist_ok=True)
    if '.' not in version or version.count('.') == 1:
        # Assume it's Minecraft version, find latest NeoForge
        version = get_latest_neoforge_version(version)
    java_path = ensure_java(version.split('.')[0])  # mc version
    installer_url = (
        f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{version}/neoforge-{version}-installer.jar"
    )
    installer_jar = os.path.join(path, "neoforge-installer.jar")
    download(installer_url, installer_jar)
    subprocess.run([java_path, "-jar", installer_jar, "--installServer"], cwd=path)
