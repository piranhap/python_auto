import socket

password = "password!"

#Socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 4000

# bind ip and port to listen
s.bind((host, port))
# Listen 
s.listen()
client, addr = s.accept()
print(f"Connection received from {addr}! ")

while True:
    data = 'Please enter the server password: '
    client.sendall(str.encode(data)) # send input
    msg = client.recv(1024).decode()
    if msg == password:
        data = 'Now you have access to the server, here you go'
        client.sendall(str.encode(data))
        while True:
            data = input('SERVER>>')
            s.sendall(str.encode(data))
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(msg)

    else:
        data = 'No access, try again'
        client.sendall(str.encode(data))
        client.close()
        break
