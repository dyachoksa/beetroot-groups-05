import socket

PORT = 80

host = input("Enter host to connect: ")

addr = socket.gethostbyname(host)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((addr, PORT))

    print(f"Connected to {host} ({addr})...")

    s.sendall(b"GET /\n\n")
    data = s.recv(1024)

    print(f"Got from server:\n{data.decode('utf-8')}")
