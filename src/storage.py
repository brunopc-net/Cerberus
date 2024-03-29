import os
import redis
import log4p

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

LAST_EXECUTION_KEY = "last_backup_date"


def get_last_archive_date():
    last_execution_date = redis.get(LAST_EXECUTION_KEY)
    log.debug("Last backup date: %s", last_execution_date)
    return last_execution_date


def update_last_execution_date(value):
    redis.set(LAST_EXECUTION_KEY, value)
    log.debug(f'Updated {LAST_EXECUTION_KEY} to {value}')


def get_last_directory_hash(directory_path):
    last_hash = str(redis.get(get_dir_hash_key(directory_path)))
    log.debug("Previous hash: %s", last_hash)
    return last_hash


def update_directory_hash(directory_path, new_hash):
    redis.set(get_dir_hash_key(directory_path), new_hash)
    log.debug(f'Updated {get_dir_hash_key(directory_path)} to {new_hash}')


def get_dir_hash_key(directory_path):
    return "hash_" + os.path.dirname(directory_path)


def delete_directory_hash(directory_path):
    redis.delete(get_dir_hash_key(directory_path))
    log.debug(f'Deleted {get_dir_hash_key(directory_path)} from storage')
