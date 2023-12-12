import socket

HOST = "127.0.0.1"
PORT = 8787

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server: {HOST}:{PORT}")

    s.sendall(b"Hello, World!")
    data = s.recv(1024)

print(f"Received from server: {data!r}")
