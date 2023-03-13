import hashlib
import os
import unittest

import src.hasher as hasher
import src.archiver as archiver
import src.storage as storage


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        archive_file = archiver.archive("./")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)

    def test_is_backup_needed(self):
        self.assertTrue(archiver.is_backup_needed("./"))
        storage.update_directory_hash("./", hasher.get_directory_hash("./", hashlib.blake2b()))
        self.assertFalse(archiver.is_backup_needed("./"))


if __name__ == "__main__":
    unittest.main()
