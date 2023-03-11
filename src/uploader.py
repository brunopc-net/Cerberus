import sys
import log4p
import pcloud

log = log4p.GetLogger(__name__, config="log4p.json").logger


def upload(file, username, password):
    pcloud_path = '/Bruno/' + file
    log.info('Uploading %s file to pcloud %s', pcloud_path)
    response = pcloud.PyCloud(username, password).uploadfile(files=[file], path=pcloud_path)

    if response['result'] == 0:
        log.info('Uploading to pcloud: Success!')
        return
    log.error("Was not able to upload to pcloud: " + str(response))
    sys.exit(response['result'])
