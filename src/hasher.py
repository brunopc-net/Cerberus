import log4p

from pathlib import Path

log = log4p.GetLogger(__name__, config="log4p.json").logger


def get_directory_hash(directory, hasher):
    hash_value = str(hash_dir(directory, hasher).hexdigest())
    log.info("Hash for directory %s: %s", directory, hash_value)
    return hash_value


def hash_dir(directory, hasher):
    for path in sorted(Path(directory).iterdir(), key=lambda p: str(p).lower()):
        hasher.update(path.name.encode())
        if path.is_file():
            hasher = hash_file(path, hasher)
        elif path.is_dir():
            hasher = hash_dir(path, hasher)
    return hasher


def get_file_hash(file, hasher):
    hash_value = str(hash_file(file, hasher).hexdigest())
    log.info("Hash for file %s: %s", file, hash_value)
    return hash_value


def hash_file(path, hasher):
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
        return hasher
