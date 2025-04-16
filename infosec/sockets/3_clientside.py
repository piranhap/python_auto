import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# We are trying to never have values hard coded
host = '127.0.0.1' 
port = 9001

s.connect((host, port)) # connect to server as a client

data = s.recv(1024).decode()
print(data)

s.close()