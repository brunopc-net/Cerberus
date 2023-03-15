import os
import unittest

import src.archiver as archiver


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        directory = "src"
        archiver.archive(directory)

        archive_name = archiver.get_new_archive_name(directory)
        self.assertTrue(os.path.isfile(archive_name))
        os.remove(archive_name)

    def test_get_directory_name(self):
        directory = "documents"
        self.assertTrue(
            directory,
            archiver.get_directory_name("/home/user/"+directory)
        )


if __name__ == "__main__":
    unittest.main()
