import os
import log4p

import _hasher as hasher

log = log4p.GetLogger(__name__, config="log4p.json").logger

DOCUMENTS="/home/bruno/documents"

if __name__ == '__main__':
    hasher.get_hash_blake2b(DOCUMENTS)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
