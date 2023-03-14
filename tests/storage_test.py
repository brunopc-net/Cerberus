import unittest

import src.storage as storage
import src.date as date


class StorageTest(unittest.TestCase):
    def test_store_last_execution_date(self):
        storage.update_last_execution_date()
        self.assertIsNotNone(storage.get_last_execution_date())

    def test_store_last_hash_directory_hash(self):
        fictive_directory_name = "/fictive_directory"
        fictive_directory_hash = "123456"
        storage.update_directory_hash(fictive_directory_name, fictive_directory_hash)
        self.assertEquals(
            fictive_directory_hash,
            storage.get_last_directory_hash(fictive_directory_name)
        )


if __name__ == "__main__":
    unittest.main()
