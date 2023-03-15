import os
import sys
import redis
import log4p
import archiver

from pathlib import Path
from pcloudclient import PCloudClient

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)


def get_valid_directory(directory):
    if not Path(directory).is_dir():
        log.error("%s is not a valid directory", directory)
        sys.exit()
    return directory


if __name__ == '__main__':

    # args = Arguments()
    dir_to_backup = get_valid_directory(sys.argv[1])
    pcloud_client = PCloudClient.fromEnvCredentials()

    if archiver.is_backup_needed(dir_to_backup):
        archive_name = archiver.archive(dir_to_backup)
        pcloud_client.upload(archive_name)
        if pcloud_client.is_file_identical(archive_name):
            log.info("Archiving success. It's been a pleasure, master!")
        else:
            log.info("Deleting the corrupted file on pCloud")
            pcloud_client.delete_file(archive_name)
    else:
        pcloud_client.rename_file(
            archiver.get_last_archive_name(dir_to_backup),
            archiver.get_new_archive_name(dir_to_backup)
        )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
