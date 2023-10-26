import os


def ping(str) :
    return os.system("ping -c 1 " + str)
