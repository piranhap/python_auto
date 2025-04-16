import socket 

#Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' 
port = 4000

s.connect((host,port)) # Connecting to Server

while True:
    msg = s.recv(1024).decode()
    if not msg or 'end':
        break
    print(msg)
    data = input()
    s.sendall(str.encode(data))


