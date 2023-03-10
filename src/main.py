import sys
import log4p
import hashlib
import redis

import _hasher as hasher

from pathlib import Path

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

DOCUMENTS="/home/bruno/documents"


def is_backup_necessary(directory_path):
    current_h = hasher.get_hash(directory_path, hashlib.blake2b())
    log.debug("Current hash for the directory %s: %s ", directory_path, current_h)

    hash_key = "hash_" + directory_path
    previous_h = str(redis.get(hash_key))
    log.debug("Previous hash: %s", previous_h)

    if current_h == previous_h:
        return False

    redis.set(hash_key, current_h)
    return True

def get_dir():
    dir_name = sys.argv[1]
    is_dir = Path(dir_name).is_dir()
    log.debug("%s is a valid directory: %s", dir_name, is_dir)
    assert Path(dir_name).is_dir()
    return dir_name


if __name__ == '__main__':
    directory = get_dir()
    log.info("Launching backup procedure for directory %s", directory)
    to_backup = is_backup_necessary(directory)
    log.info("Need to backup directory: %s", str(to_backup))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
