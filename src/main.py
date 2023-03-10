import os

import log4p
import redis

import _hasher as hasher

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0)

DOCUMENTS="/home/bruno/documents"

def is_backup_necessary(directory):
    print(os.listdir(DOCUMENTS))
    current_h = hasher.get_hash_blake2b(directory)
    log.debug("Current hash for the directory %s: %s ", directory, current_h)

    hash_key = "hash_" + directory
    previous_h = str(redis.get(hash_key))
    log.debug("Previous hash: " + previous_h)

    if current_h == previous_h:
        return False

    redis.set(hash_key, current_h)
    return True

if __name__ == '__main__':
    to_backup = is_backup_necessary(DOCUMENTS)
    log.info("Need to backup directory: " + str(to_backup))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
