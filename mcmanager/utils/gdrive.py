import os
import shutil
import subprocess


def is_mounted(path: str) -> bool:
    """Return True if the given path is a mount point (Google Drive)."""
    return os.path.ismount(os.path.expanduser(path))


def mount(remote: str, mountpoint: str):
    """Mount a remote drive using rclone.
    Example: rclone mount <remote>: <mountpoint>
    """
    if not shutil.which("rclone"):
        raise Exception("rclone is not installed. Install it with: sudo apt install rclone")
    os.makedirs(os.path.expanduser(mountpoint), exist_ok=True)
    subprocess.Popen(
        ["rclone", "mount", f"{remote}:", os.path.expanduser(mountpoint)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def sync(local: str, remote: str):
    """Sync a local folder to a remote using rclone.
    Example: rclone sync local remote:
    """
    if not shutil.which("rclone"):
        raise Exception("rclone is not installed. Install it with: sudo apt install rclone")
    subprocess.run(["rclone", "sync", os.path.expanduser(local), f"{remote}:"])


def ensure_server_dir(server_name: str, cfg: dict) -> str:
    """Ensure the directory for a server on the Google Drive exists and return its path."""
    mountpoint = os.path.expanduser(cfg.get("gdrive_mount", "~/gdrive"))
    base = os.path.join(mountpoint, "mcservers", server_name)
    os.makedirs(base, exist_ok=True)
    return base
