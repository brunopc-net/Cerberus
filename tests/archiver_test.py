import os
import unittest

import src.archiver as archiver


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        archive_file = archiver.archive("./src")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)

    def test_is_backup_needed(self):
        directory = "./src"
        self.assertFalse(archiver.is_backup_needed(directory))

        empty_file = directory+"/empty_file.txt"
        f = open(empty_file, "w")
        f.close()

        self.assertTrue(archiver.is_backup_needed(directory))
        os.remove(empty_file)


if __name__ == "__main__":
    unittest.main()
