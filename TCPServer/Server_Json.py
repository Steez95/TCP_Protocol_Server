import socket
import threading
import random
import json

HOST = "127.0.0.1"
PORT = 6000

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            try:
                request = json.loads(data)
                method = request.get("method")
                t1 = request.get("Tal1")
                t2 = request.get("Tal2")

                if method == "Random":
                    result = random.randint(t1, t2)
                elif method == "Add":
                    result = t1 + t2
                elif method == "Subtract":
                    result = t1 - t2
                else:
                    result = "Unknown method"

                response = {"result": result}
                conn.sendall((json.dumps(response) + "\n").encode())

            except Exception as e:
                conn.sendall(json.dumps({"error": str(e)}).encode())

    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] JSON server running on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
