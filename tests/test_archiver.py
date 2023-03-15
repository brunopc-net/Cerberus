import os
import unittest

import src.archiver as archiver


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        archive_file = archiver.archive("./src")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)


if __name__ == "__main__":
    unittest.main()
