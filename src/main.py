import sys
import log4p
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

    dir_to_backup = get_valid_directory(sys.argv[1])
    current_hash = hasher.get_directory_hash(dir_to_backup, hashlib.blake2b())
    previous_hash = storage.get_last_directory_hash(dir_to_backup)
    pcloud_client = PCloudClient.fromEnvCredentials()

    if current_hash == previous_hash:
        log.info("Data is the same since the last check, no need to back up")
        # pcloud_client.rename_file(
        #     archiver.get_last_archive_name(dir_to_backup),
        #     archiver.get_new_archive_name(dir_to_backup)
        # )
    else:
        log.info("Data has been updated since the last check, need to back up")
        # archive_name = archiver.archive(dir_to_backup)
        # pcloud_client.upload(archive_name)
        # if pcloud_client.is_file_identical(archive_name):
        #     storage.update_directory_hash(dir_to_backup, current_hash)
        #     storage.update_last_execution_date()
        #     log.info("Backup success")
        # else:
        #     log.info("Backup failure - Deleting the corrupted file on pCloud")
        #     pcloud_client.delete_file(archive_name)

    log.info("It's been a pleasure, master!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
