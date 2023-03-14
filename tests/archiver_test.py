import os
import unittest

import src.storage as storage
import src.hasher as hasher
import src.archiver as archiver


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        archive_file = archiver.archive("./src")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)

    def test_is_backup_needed(self):
        directory = "fictive_directory"
        os.mkdir(directory)
        self.assertTrue(archiver.is_backup_needed(directory))

        storage.update_directory_hash(directory, hasher.get_directory_hash(directory))
        self.assertFalse(archiver.is_backup_needed(directory))

        storage.delete_directory_hash(directory)


if __name__ == "__main__":
    unittest.main()
