# from https://github.com/taisei-project/python-zipfile-zstd

import os
import tarfile

from datetime import datetime

def archive(directory):
    tar_filename = directory + datetime.today().strftime('%Y-%m-%d') + '.tar'
    with tarfile.open(tar_filename, "w") as archive_file:
        for root, dirs, files in os.walk(directory):
            for f in files:
                archive_file.add(os.path.join(root, f))

        archive_file.close()

    return tar_filename