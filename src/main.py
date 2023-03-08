import os
import log4p

from src import _hasher as hasher

log = log4p.GetLogger(__name__, config="log4p.json").logger

if __name__ == '__main__':
    log.info(os.listdir("/home/bruno"))
    documents_hash = str(hasher.hash_blake2b(directory='documents'))
    log.debug("Current documents hash: " + documents_hash)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
