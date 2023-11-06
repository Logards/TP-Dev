import argparse

parser = argparse.ArgumentParser(description="Usage: allows you to communicate with a server")
parser.add_argument("-p", "--port", action="store", help="change the default port by the argument")
args = parser.parse_args()
print(args.port)
if args.port is None:
    port = 13337
elif int(args.port) < 0 or int(args.port) > 65535:
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif int(args.port) < 1025 :
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)
