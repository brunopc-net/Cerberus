import hashlib
import sys
import unittest
import pcloud

import src.uploader as uploader
import src.hasher as hasher


class UploaderTest(unittest.TestCase):
    USERNAME = ""
    PASSWORD = ""

    def test_login_fail(self):
        self.assertRaises(
            pcloud.api.AuthenticationError,
            uploader.Uploader, "bad_user", "bad_password"
        )

    def test_login_success(self):
        self.assertTrue(
            uploader.Uploader(self.USERNAME, self.PASSWORD).is_logged_in()
        )

    def test_upload_rename_delete(self):
        u = uploader.Uploader(self.USERNAME, self.PASSWORD)
        u.set_path('/Bruno')

        # upload
        log_file = "log4p.json"
        u.upload(log_file)
        self.assertTrue(u.is_file_present(log_file))
        self.assertEqual(
            hasher.get_file_hash(log_file, hashlib.sha1()),
            u.get_checksum(log_file)
        )

        # rename
        new_name = "log4j.json"
        u.rename_file(log_file, new_name)
        self.assertTrue(u.is_file_present(new_name))

        # delete
        u.delete_file(new_name)
        self.assertFalse(u.is_file_present(new_name))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        UploaderTest.PASSWORD = sys.argv.pop()
        sys.argv.pop()
        UploaderTest.USERNAME = sys.argv.pop()
        sys.argv.pop()
    unittest.main()
