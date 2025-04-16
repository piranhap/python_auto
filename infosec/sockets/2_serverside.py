# Make sure to install sockets pip install sockets 
import socket

#Socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(type(s)) this should return socket.socket as a class 

host ='127.0.0.1' 
port = 9001

s.bind((host, port)) # We binded ip and port, try to make it over 1024 so it is not a common port
s.listen() # We start listening 
client, addr = s.accept() # connection and ip address that is the recipient

print(f"connection received from {addr}")

# if server is sending first we want to use
data = "Test thankyou"
client.sendall(str.encode(data))

# and client has to receive the data with (on its code)
# s.receive(1024)
client.close()
print(f"connection with {addr} closed")