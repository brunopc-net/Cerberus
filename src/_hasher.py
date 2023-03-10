from pathlib import Path

def get_hash(directory, hash_algorithm):
    return str(
        hash_dir(directory, hash_algorithm)
        .hexdigest()
    )

def hash_dir(directory, hasher):
    for path in sorted(Path(directory).iterdir(), key=lambda p: str(p).lower()):
        hasher.update(path.name.encode())
        if path.is_file():
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
        elif path.is_dir():
            hasher = hash_dir(path, hasher)
    return hasher