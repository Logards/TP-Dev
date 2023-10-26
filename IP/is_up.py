import os
from sys import argv


response = os.system("ping -c 1 " + argv[1])
if response == 0:
    print("UP")
else:
    print("DOWN")
