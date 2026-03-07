import os

# constants related to Java

JAVA17 = "/usr/lib/jvm/java-17-openjdk-amd64/bin/java"
JAVA21 = "/usr/lib/jvm/java-21-openjdk-amd64/bin/java"

def get_java_path(mc_version: str) -> str:
    """Return the path to the appropriate Java executable for the Minecraft version."""
    try:
        major = int(mc_version.split('.')[1])
        if major >= 20:
            return JAVA21
        else:
            return JAVA17
    except (ValueError, IndexError):
        return JAVA17  # default

def ensure_java(version: str):
    """Ensure the required Java version is installed."""
    java_path = get_java_path(version)
    if os.path.exists(java_path):
        return java_path
    # try to install
    import subprocess
    if '21' in java_path:
        print("Installing Java 21...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "openjdk-21-jre-headless"], check=True)
    elif '17' in java_path:
        print("Installing Java 17...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "openjdk-17-jre-headless"], check=True)
    return java_path
