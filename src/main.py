import sys
import redis
import log4p

import archiver as archiver
from arguments import Arguments
from pcloudclient import PCloudClient

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)


if __name__ == '__main__':
    args = Arguments(sys.argv[1:])
    dir_to_backup = args.get_valid_directory()
    pcloud_client = PCloudClient(args.get_user(), args.get_password())

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
