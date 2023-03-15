import os
import unittest

import src.archiver as archiver


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        archive_file = archiver.archive("./src")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)

    def test_get_directory_name(self):
        directory = "documents"
        self.assertTrue(
            directory,
            archiver.get_directory_name("/home/user/"+directory)
        )


if __name__ == "__main__":
    unittest.main()
