import os
import sys
import log4p
import hashlib

import pcloud
import redis
import getopt

import _hasher as hasher
import _archiver as archiver

from pathlib import Path

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

directory_path = ''
username = ''
password = ''


def is_backup_necessary(dir_path):
    current_h = hasher.get_hash(dir_path, hashlib.blake2b())
    log.debug("Current hash for directory content: %s ", current_h)

    hash_key = "hash_" + dir_path
    previous_h = str(redis.get(hash_key))
    log.debug("Previous hash: %s", previous_h)

    if current_h == previous_h:
        log.info("Do not need to backup directory")
        return False

    log.info("Need to backup directory")
    redis.set(hash_key, current_h)
    return True


def get_pCloud_connection():
    try:
        return pcloud.PyCloud(username, password)
    except pcloud.api.AuthenticationError:
        log.error("Was not able to login with the provided credentials")
        sys.exit()


def get_directory_path():
    log.info("Launching backup procedure for directory %s", directory_path)
    if not Path(directory_path).is_dir():
        log.error("Not a valid directory")
        sys.exit()
    return directory_path


def build_archive(dir_path):
    archive_file = archiver.archive(dir_path)
    if os.path.isfile(archive_file):
        log.info('Archiving %s into archive %s: Success!', dir_path, archive_file)
        return archive_file
    log.error("Problem occurred creating archive")
    sys.exit()


def upload_archive(archive_file):
    pcloud_path = '/Bruno/'+archive_file
    log.info('Uploading %s file to pcloud %s', pcloud_path)
    response = get_pCloud_connection().uploadfile(files=[archive_file], path=pcloud_path)

    if response['result'] == 0:
        log.info('Uploading to pcloud: Success!')
        return
    log.error("Was not able to upload to pcloud: " + str(response))
    sys.exit(response['result'])


def set_arguments(argv):
    global directory_path
    global username
    global password

    opts, args = getopt.getopt(argv, "hd:u:p:", ["directory=", "user=", "password="])
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('main.py -d <directory> -u <username> -p <password>')
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory_path = arg
        elif opt in ("-u", "--user"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg


if __name__ == '__main__':
    set_arguments(sys.argv[1:])
    directory = get_directory_path()
    if is_backup_necessary(directory):
        archive = build_archive(directory)
        upload_archive(archive)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
