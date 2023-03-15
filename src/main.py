import os
import sys
import log4p
import date
import hasher
import hashlib
import storage
import archiver

from pathlib import Path
from pcloudclient import PCloudClient

log = log4p.GetLogger(__name__, config="log4p.json").logger


def get_valid_directory(directory):
    if not Path(directory).is_dir():
        log.error("%s is not a valid directory", directory)
        sys.exit()
    return directory


if __name__ == '__main__':

    if date.get_today() == storage.get_last_archive_date():
        log.info("Data is already backed up for today")
        sys.exit()

    dir_to_backup = get_valid_directory(sys.argv[1])
    current_hash = hasher.get_directory_hash(dir_to_backup, hashlib.blake2b())
    previous_hash = storage.get_last_directory_hash(dir_to_backup)

    pcloud_client = PCloudClient.fromEnvCredentials()
    pcloud_client.set_path("/Bruno")

    previous_archive_name = archiver.get_last_archive_name(dir_to_backup)
    new_archive_name = archiver.get_new_archive_name(dir_to_backup)

    if current_hash == previous_hash:
        log.info("Data is the same since the last check, no need to archive")
        pcloud_client.rename_file(previous_archive_name, new_archive_name)
        sys.exit()

    log.info("Data has been updated since the last check, need to archive")
    archiver.archive(dir_to_backup)
    # pcloud_client.upload(new_archive_name)
    # if pcloud_client.is_file_identical(new_archive_name):
    #     storage.update_directory_hash(dir_to_backup, current_hash)
    #     storage.update_last_execution_date(date.get_today())
    #     log.info("Backup success - Deleting the previous backup on pCloud")
    #     pcloud_client.delete_file(previous_archive_name)
    # else:
    #     log.info("Backup failure - Deleting the corrupted file on pCloud")
    #     pcloud_client.delete_file(new_archive_name)

    os.remove(new_archive_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
