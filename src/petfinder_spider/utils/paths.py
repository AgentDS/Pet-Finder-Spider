from pathlib import Path

def project_root() -> Path:
    # assumes this file lives under src/petfinder_spider/utils/
    return Path(__file__).resolve().parents[3]  # adjust if layout changes

CACHE_DIR = project_root() / "data" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def cache_path(name: str) -> Path:
    """Return a path inside the local cache directory."""
    return CACHE_DIR / name
