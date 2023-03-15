import unittest
import pcloud

from src.pcloudclient import PCloudClient


class PCloudClientTest(unittest.TestCase):

    pCloud_client = PCloudClient.fromEnvCredentials()
    log_file_name = "log4p.json"
    log_file_name_new = "log4j.json"

    def test_login_fail(self):
        self.assertRaises(
            pcloud.api.AuthenticationError,
            PCloudClient, "bad_user", "bad_password"
        )

    def test_01_login_success(self):
        self.assertTrue(
            self.pCloud_client.is_logged_in()
        )

    def test_02_upload(self):
        self.pCloud_client.set_path('/Bruno')
        self.pCloud_client.upload(self.log_file_name)
        self.assertTrue(self.pCloud_client.is_file_identical(self.log_file_name))

    def test_03_rename(self):
        self.pCloud_client.rename_file(self.log_file_name, self.log_file_name_new)
        self.assertTrue(self.pCloud_client.is_file_present(self.log_file_name_new))

    def test_04_delete(self):
        self.pCloud_client.delete_file(self.log_file_name_new)
        self.assertFalse(self.pCloud_client.is_file_present(self.log_file_name_new))


if __name__ == "__main__":
    unittest.main(failfast=True)
