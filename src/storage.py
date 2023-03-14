import os
import redis
import log4p

from src.date import get_today

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

LAST_EXECUTION_KEY = "last_successful_execution"


def get_last_execution_date():
    last_execution_date = redis.get(LAST_EXECUTION_KEY)
    log.debug("Last execution date: %s", last_execution_date)
    return last_execution_date


def update_last_execution_date():
    redis.set(LAST_EXECUTION_KEY, get_today())


def get_last_directory_hash(directory_path):
    last_hash = str(redis.get(get_hash_key(directory_path)))
    log.debug("Previous hash: %s", last_hash)
    return last_hash


def update_directory_hash(directory_path, new_hash):
    redis.set(get_hash_key(directory_path), new_hash)


def get_hash_key(directory_path):
    return "hash_" + os.path.dirname(directory_path)
