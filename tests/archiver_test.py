import hashlib
import os
import unittest


import src.hasher as hasher
import src.storage as storage
import src.archiver as archiver


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        archive_file = archiver.archive("./")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)

    def test_is_backup_needed(self):
        self.assertTrue(archiver.is_backup_needed("/src"))
        hasher.get_directory_hash("/src", hashlib.blake2b())
        hasher.get_directory_hash("/src", hashlib.blake2b())
        hasher.get_directory_hash("/src", hashlib.blake2b())

        storage.update_directory_hash("/src", hasher.get_directory_hash("/src", hashlib.blake2b()))
        self.assertFalse(archiver.is_backup_needed("/src"))


if __name__ == "__main__":
    unittest.main()
