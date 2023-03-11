# from https://github.com/taisei-project/python-zipfile-zstd
import os
import unittest

from .context import src


class TestStringMethods(unittest.TestCase):
    def test_archive(self):
        archive_file = src.archive("./")
        self.assertTrue(os.path.isfile(archive_file))
        os.remove(archive_file)
