import hashlib
import unittest
import re

import _hasher as hasher
class TestStringMethods(unittest.TestCase):
    def test_hash(self):
        hash = hasher.get_hash("./", hashlib.blake2b())
        self.assertTrue(re.search("^[a-z0-9]{128}$", hash))