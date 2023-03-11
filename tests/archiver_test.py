import os
import unittest
import src.archiver as archiver


class ArchiverTest(unittest.TestCase):
    def test_archive(self):
        archive_file = archiver.archive("./")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)
