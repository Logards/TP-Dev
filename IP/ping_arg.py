import sys
import ping_simple


def arg():
    hostname = str(sys.argv[1])
    ping_simple.ping(hostname)
