import unittest
import pcloud
import src.uploader as uploader


class TestStringMethods(unittest.TestCase):
    def test_upload_fail(self):
        f = open("test_upload.txt", "w")
        f.write("some data")
        f.close()

        self.assertRaises(
            pcloud.api.AuthenticationError,
            uploader.upload('bad_user', 'bad_password', f)
        )
