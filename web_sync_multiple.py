import os.path
from sys import argv
import validators
import requests

args = argv[1]


def file_exist(file_path=args):
    return os.path.isfile(file_path)


def get_url_file(file_path=args):
    if file_exist():
        f = open(file_path)
        content = f.read()
        f.close()
        content = content.split("\n")
        return content


def get_url(content=get_url_file()):
    cont_to_strip = "https://"
    for i in content:
        if validators.url(i):
            res = requests.get(i)
            i = i.replace(cont_to_strip, "")
            file = open(f"/tmp/web_{i}", 'a')
            file.write(res.text)
            file.close()


get_url()
