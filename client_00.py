import socket

s = socket.socket()

host = socket.gethostname()
port = 8000

s.connect((host, port))
print(s.recv(1024).decode())