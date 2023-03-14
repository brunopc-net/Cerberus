import sys
import log4p
import optparse

from pathlib import Path

log = log4p.GetLogger(__name__, config="log4p.json").logger


class Arguments:
    def __init__(self):
        arg_parser = optparse.OptionParser()
        arg_parser.add_option('-d', dest='directory', type='string', help='Directory to be archived')
        arg_parser.add_option('-u', dest='username', type='string', help='Cloud service username')
        arg_parser.add_option('-p', dest='password', type='string', help='Cloud service password')
        (self.options, args) = arg_parser.parse_args()

    def get_valid_directory(self):
        directory = self.options.directory
        if not Path(directory).is_dir():
            log.error("%s is not a valid directory", directory)
            sys.exit()
        return directory

    def get_user(self):
        return self.options.username

    def get_password(self):
        return self.options.password
