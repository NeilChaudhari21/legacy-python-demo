from packaging.version import Version


def is_newer(version_a: str, version_b: str) -> bool:
    """Return True if version_a is newer than version_b."""
    return Version(version_a) > Version(version_b)


def normalize_name(name: str) -> str:
    """Normalize a display name for demo testing."""
    return name.strip().title()
