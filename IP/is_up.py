import ping_simple
from sys import argv

def is_up():
    response = ping_simple.ping(argv[1])
    if response == 0 :
        print("UP")
    else:
        print("DOWN")

print(is_up())