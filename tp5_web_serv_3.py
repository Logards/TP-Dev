import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.1.1.11', 13337))
sock.listen()
while True:
    conn, addr = sock.accept()
    try:
        data = conn.recv(1024)
        if not data: break
        print(f"Donnéees reçues du client : {data}")

        if "GET /toto.html" in data.decode():
            file = open('toto.html')
            html_content = file.read()
            file.close()
            http_reponse = 'HTTP/1.0 200 OK\n\n' + html_content
            conn.send(http_reponse.encode())
        else :
            http_reponse = 'HTTP/1.0 404 Not Found\n\n<h1>404 Not Found</h1>'
            conn.send(http_reponse.encode())
        conn.close()
    except socket.error:
        print ("Error Occured.")
        break
    finally:
        conn.close()
sock.close()
exit()