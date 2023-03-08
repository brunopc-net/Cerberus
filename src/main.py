# This is a sample Python script.
import os

import log4p

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

log = log4p.GetLogger(__name__, config="log4p.json").logger

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(os.listdir("/home/bruno"))
    log.info(os.listdir("/home/bruno"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
