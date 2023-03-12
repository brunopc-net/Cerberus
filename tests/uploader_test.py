import argparse
import sys
import unittest
import pcloud

import src.uploader as uploader


class UploaderTest(unittest.TestCase):
    USERNAME = ""
    PASSWORD = ""

    def test_login_fail(self):
        self.assertRaises(
            pcloud.api.AuthenticationError,
            uploader.Uploader, "bad_user", "bad_password"
        )

    def test_login_success(self):
        self.assertTrue(uploader.Uploader(self.USERNAME, self.PASSWORD).is_logged_in())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    if len(sys.argv) > 1:
        UploaderTest.PASSWORD = sys.argv.pop()
        sys.argv.pop()
        UploaderTest.USERNAME = sys.argv.pop()
        sys.argv.pop()
    unittest.main()
