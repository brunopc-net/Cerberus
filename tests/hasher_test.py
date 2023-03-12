import hashlib
import unittest
import re

import src.hasher as hasher


class TestStringMethods(unittest.TestCase):
    def test_hash(self):
        hash_result = hasher.get_hash("./", hashlib.blake2b())
        self.assertTrue(re.search("^[a-z0-9]{128}$", hash_result))


if __name__ == "__main__":
    unittest.main()
