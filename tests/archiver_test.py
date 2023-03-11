# from https://github.com/taisei-project/python-zipfile-zstd
import os
import unittest

from src.archiver import archive


class TestStringMethods(unittest.TestCase):
    def test_archive(self):
        archive_file = archive("./")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)
