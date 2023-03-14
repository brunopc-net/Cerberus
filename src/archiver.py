import os
import log4p
import tarfile
import hashlib

import storage

from src.date import get_today
from src.hasher import get_directory_hash

log = log4p.GetLogger(__name__, config="log4p.json").logger


def get_new_archive_name(directory_path):
    return os.path.dirname(directory_path) + \
        get_today() + \
        '.tar'


def get_last_archive_name(directory_path):
    return os.path.dirname(directory_path) + \
        (storage.get_last_execution_date()) + \
        '.tar'


def is_backup_needed(directory_path):
    previous_hash = storage.get_last_directory_hash(directory_path)
    current_hash = get_directory_hash(
            directory_path,
            hashlib.blake2b()
    )
    if previous_hash == current_hash:
        log.info("Directory data is the same since the last check, no need to back up")
        return False
    log.info("Directory data has been updated since the last check, need to back up")
    return True


def archive(directory_path):
    archive_name = get_new_archive_name(directory_path)
    with tarfile.open(archive_name, "w") as archive_file:
        for root, dirs, files in os.walk(directory_path):
            for f in files:
                archive_file.add(os.path.join(root, f))
        archive_file.close()
    log.info("Archive %s created from path %s", archive_name, directory_path)
    return archive_name
