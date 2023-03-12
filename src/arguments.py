import getopt
import sys
import log4p

from collections import defaultdict
from pathlib import Path


log = log4p.GetLogger(__name__, config="log4p.json").logger


class Arguments:
    def __init__(self, argv):
        self.arguments = defaultdict(str)
        opts, args = getopt.getopt(argv, "hd:u:p:", ["directory=", "user=", "password="])
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print('main.py -d <directory> -u <username> -p <password>')
                sys.exit()
            elif opt in ("-d", "--directory"):
                self.arguments['directory'] = arg
            elif opt in ("-u", "--user"):
                self.arguments['user'] = arg
            elif opt in ("-p", "--password"):
                self.arguments['password'] = arg

    def get_valid_directory(self):
        if not Path(self.arguments['directory']).is_dir():
            log.error("%s is not a valid directory", self.arguments['directory'])
            sys.exit()
        return self.arguments['directory']

    def get_user(self):
        return self.arguments['user']

    def get_password(self):
        return self.arguments['password']
