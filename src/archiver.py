import os
import log4p
import tarfile

from src import storage
from src import date

log = log4p.GetLogger(__name__, config="log4p.json").logger


def get_directory_name(directory_path):
    path_array = os.path.split(directory_path)
    return path_array[len(path_array) - 1]


def get_new_archive_name(directory_path):
    return get_directory_name(directory_path) + "_" + \
        date.get_today() + \
        '.tar'


def get_last_archive_name(directory_path):
    return get_directory_name(directory_path) + "_" + \
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
