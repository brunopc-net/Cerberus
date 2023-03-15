import os
import sys
import time
import log4p
import pcloud
import hashlib

from src import hasher

log = log4p.GetLogger(__name__, config="log4p.json").logger

WRITE_DELAY_SECONDS = 1
DEFAULT_DIRECTORY = "/Bruno"


class PCloudClient:

    def __init__(self, username, password):
        self.pc = pcloud.PyCloud(username, password)
        self.path = DEFAULT_DIRECTORY

    @classmethod
    def fromEnvCredentials(cls):
        return cls(os.environ["username"], os.environ["password"])

    def is_logged_in(self):
        return len(self.pc.auth_token) > 1

    def set_path(self, path):
        self.pc.createfolderifnotexists(path=path)
        self.path = path

    def is_file_present(self, file):
        for item in self.get_directory_content():
            if item['name'] == file:
                log.info("File %s is present in directory %s", file, self.path)
                return True
        log.info("File %s not found in directory %s", file, self.path)
        return False

    def get_directory_content(self):
        response = self.pc.listfolder(path=self.path)
        log.debug(response)
        return response['metadata']['contents']

    def is_file_identical(self, file):
        local_hash = hasher.get_file_hash(file, hashlib.sha1())
        if local_hash == self.get_checksum(file):
            log.info("Checksum validation passed, upload success")
            return True
        log.error("Checksum validation failed, file is corrupted")
        return False

    def get_checksum(self, file):
        response = self.pc.checksumfile(path=self.path + '/' + file)
        log.debug(response)
        return response['sha1']

    def upload(self, file):
        response = self.pc.uploadfile(files=[file], path=self.path)
        log.debug(response)
        if response['result'] == 0:
            log.info('Uploaded the file  %s file to pcloud %s', file, self.path)
            time.sleep(WRITE_DELAY_SECONDS)
            return
        log.error("Was not able to upload to pcloud")
        sys.exit(response['result'])

    def rename_file(self, file, new_name):
        response = self.pc.renamefile(
            path=self.path + '/' + file,
            topath=self.path + '/' + new_name
        )
        log.debug(response)
        if response['result'] == 0:
            log.info("File %s renamed to %s", file, new_name)
            time.sleep(WRITE_DELAY_SECONDS)
            return
        log.error("Failed to rename file %s to %s", file, new_name)

    def delete_file(self, file):
        response = self.pc.deletefile(path=self.path + '/' + file)
        log.debug(response)
        if response['result'] == 0:
            log.info("File %s deleted", file)
            time.sleep(WRITE_DELAY_SECONDS)
            return
        log.error("Failed to delete file %s", file)
