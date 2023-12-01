import logging
import select
import colorlog
import socket

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('/var/log/server/server.log', 'w', 'utf-8')
file_handler.setLevel(logging.INFO)
stream_handler = colorlog.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.1.1.11', 13337))
sock.listen()
while True:
    conn, addr = sock.accept()
    try:
        data = conn.recv(1024)
        if not data: break
        logging.info(f"Requête client : {data.decode()}")
        if "GET /toto.html" in data.decode():
            file = open('toto.html')
            html_content = file.read()
            file.close()
            http_reponse = 'HTTP/1.0 200 OK\n\n' + html_content
            logging.info(f"Réponse serveur : {http_reponse}")
            conn.send(http_reponse.encode())
        else :
            http_reponse = 'HTTP/1.0 404 Not Found\n\n<h1>404 Not Found</h1>'
            logging.info(f"Réponse serveur : {http_reponse}")
            conn.send(http_reponse.encode())
        conn.close()
    except socket.error:
        print ("Error Occured.")
        break
    finally:
        conn.close()
sock.close()
exit()

