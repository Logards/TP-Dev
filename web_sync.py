from sys import argv
import requests

args = argv[1]


def get_content(url=args):
    res = requests.get(url)
    return res.text


def write_content(file : str, content : str):
    f = open(file, 'w')
    f.write(content)
    f.close()


write_content("/tmp/web_page", get_content())
