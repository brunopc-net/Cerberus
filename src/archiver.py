import os
import log4p
import tarfile

from src import storage
from src import date

log = log4p.GetLogger(__name__, config="log4p.json").logger


def get_new_archive_name(directory_path):
    return os.path.dirname(directory_path) + \
        date.get_today() + \
        '.tar'


def get_last_archive_name(directory_path):
    return os.path.dirname(directory_path) + \
        (storage.get_last_archive_date()) + \
        '.tar'


def archive(directory_path):
    archive_name = get_new_archive_name(directory_path)
    with tarfile.open(archive_name, "w") as archive_file:
        for root, dirs, files in os.walk(directory_path):
            for f in files:
                archive_file.add(os.path.join(root, f))
        archive_file.close()
    log.info("Archive %s created from path %s", archive_name, directory_path)
    return archive_name
