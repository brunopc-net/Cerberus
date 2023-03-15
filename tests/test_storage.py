import unittest

import src.storage as storage


class StorageTest(unittest.TestCase):
    def test_store_last_execution_date(self):
        last_execution_date = storage.get_last_archive_date()
        fictive_date = "YYYY-MM-DD"
        storage.update_last_execution_date(fictive_date)
        self.assertEqual(
            fictive_date,
            storage.get_last_archive_date()
        )
        # Restoring last execution date
        storage.update_last_execution_date(last_execution_date)

    def test_store_last_hash_directory_hash(self):
        fictive_directory_name = "/fictive_directory"
        fictive_directory_hash = "123456"
        storage.update_directory_hash(fictive_directory_name, fictive_directory_hash)
        self.assertEqual(
            fictive_directory_hash,
            storage.get_last_directory_hash(fictive_directory_name)
        )


if __name__ == "__main__":
    unittest.main()
