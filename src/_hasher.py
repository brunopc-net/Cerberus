import hashlib
import log4p

from pathlib import Path

log = log4p.GetLogger(__name__, config="log4p.json").logger

def get_hash_blake2b(directory):
    return get_hash_value(directory, hashlib.blake2b)


def get_hash_value(directory, hasher):
    hash_value = str(get_hash(directory, hasher))
    log.debug("Current hash for the directory %s: %s", directory, hash_value)
    return hash_value


def get_hash(directory, hasher):
    assert Path(directory).is_dir()
    for path in sorted(Path(directory).iterdir(), key=lambda p: str(p).lower()):
        hasher.update(path.name.encode())
        if path.is_file():
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
        elif path.is_dir():
            hasher = get_hash(path, hasher)
    return hasher

