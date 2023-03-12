import os
import tarfile
import log4p

from datetime import datetime


log = log4p.GetLogger(__name__, config="log4p.json").logger


def archive(directory_path):
    archive_filename = get_archive_name(directory_path)
    with tarfile.open(archive_filename, "w") as archive_file:
        for root, dirs, files in os.walk(directory_path):
            for f in files:
                archive_file.add(os.path.join(root, f))
        archive_file.close()
    log.info("Archive %s created from path %s", archive_filename, directory_path)
    return archive_filename


def get_archive_name(directory_path):
    directory_name = os.path.dirname(directory_path)
    date = datetime.today().strftime('%Y-%m-%d')
    return directory_name + date + '.tar'
