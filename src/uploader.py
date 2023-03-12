import sys
import log4p
import pcloud

log = log4p.GetLogger(__name__, config="log4p.json").logger

PATH = '/Bruno/'


class Uploader:

    def __init__(self, username, password):
        self.pc = pcloud.PyCloud(username, password)

    def upload(self, file):
        path = PATH + str(file)
        log.info('Uploading %s file to pcloud %s', file, path)
        response = self.pc.uploadfile(files=[file], path=path)
        if response['result'] == 0:
            log.info('Uploading to pcloud: Success!')
            return
        log.error("Was not able to upload to pcloud: " + str(response))
        sys.exit(response['result'])

    def is_logged_in(self):
        return len(self.pc.auth_token) > 1
