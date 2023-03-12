import getopt
import sys

from collections import defaultdict


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

    def get_directory(self):
        return self.arguments['directory']

    def get_user(self):
        return self.arguments['user']

    def get_password(self):
        return self.arguments['password']
