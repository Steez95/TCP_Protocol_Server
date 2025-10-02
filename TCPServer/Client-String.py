import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # 1: send kommando
    s.sendall(b"Random\n")
    
    # 2: modtag "Input numbers"
    print(s.recv(1024).decode().strip())
    
    # 3: send tal
    s.sendall(b"1 10\n")
    
    # 4: modtag resultat
    print("Result:", s.recv(1024).decode().strip())
