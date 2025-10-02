import socket
import threading
import random

HOST = "127.0.0.1"
PORT = 5000

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        while True:
            # 1: modtag kommando
            command = conn.recv(1024).decode().strip()
            if not command:
                break

            if command in ["Random", "Add", "Subtract"]:
                conn.sendall(b"Input numbers\n")  # 2: server svarer
            else:
                conn.sendall(b"Unknown command\n")
                continue

            # 3: modtag tal1 og tal2
            numbers = conn.recv(1024).decode().strip().split()
            if len(numbers) != 2:
                conn.sendall(b"Invalid input\n")
                continue

            try:
                t1, t2 = int(numbers[0]), int(numbers[1])
            except ValueError:
                conn.sendall(b"Invalid numbers\n")
                continue

            # 4: beregn svar
            if command == "Random":
                result = random.randint(t1, t2)
            elif command == "Add":
                result = t1 + t2
            elif command == "Subtract":
                result = t1 - t2

            conn.sendall(f"{result}\n".encode())

    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server running on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
