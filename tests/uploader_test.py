import unittest
import pcloud
import src.uploader as uploader


class TestStringMethods(unittest.TestCase):
    def test_login_fail(self):
        self.assertRaises(
            pcloud.api.AuthenticationError,
            uploader.Uploader, "bad_user", "bad_password"
        )
