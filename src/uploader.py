import sys
import time

import log4p
import pcloud

log = log4p.GetLogger(__name__, config="log4p.json").logger


class Uploader:

    def __init__(self, username, password):
        self.pc = pcloud.PyCloud(username, password)
        self.path = '/'

    def is_logged_in(self):
        return len(self.pc.auth_token) > 1

    def set_path(self, path):
        self.pc.createfolderifnotexists(path=path)
        self.path = path

    def upload(self, file):
        response = self.pc.uploadfile(files=[file], path=self.path)
        log.debug(response)
        if response['result'] == 0:
            log.info('Uploaded the file  %s file to pcloud %s', file, self.path)
            time.sleep(1)
            return
        log.error("Was not able to upload to pcloud")
        sys.exit(response['result'])

    def get_checksum(self, file):
        response = self.pc.checksumfile(path=self.path+'/'+file)
        log.debug(response)
        return response['sha1']

    def is_file_present(self, file):
        response = self.pc.listfolder(path=self.path)
        log.debug(response)
        dir_content = response['metadata']['contents']
        for item in dir_content:
            if item['name'] == file:
                log.info("File %s is present in directory %s", file, self.path)
                return True
        log.info("File %s not found in directory %s", file, self.path)
        return False

    def rename_file(self, file, new_name):
        response = self.pc.renamefile(
            path=self.path+'/'+file,
            topath=self.path+'/'+new_name
        )
        log.debug(response)
        if response['result'] == 0:
            log.info("File %s renamed to %s", file, new_name)
            time.sleep(1)
            return
        log.error("Failed to rename file %s to %s", file, new_name)

    def delete_file(self, file):
        response = self.pc.deletefile(path=self.path+'/'+file)
        log.debug(response)
        if response['result'] == 0:
            log.info("File %s deleted", file)
            return

