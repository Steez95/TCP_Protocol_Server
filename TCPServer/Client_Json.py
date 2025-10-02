import socket
import json

HOST = "127.0.0.1"
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    request = {
        "method": "Random",
        "Tal1": 1,
        "Tal2": 10
    }

    s.sendall((json.dumps(request) + "\n").encode())
    response = s.recv(1024).decode().strip()
    print("Server response:", response)
