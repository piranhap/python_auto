# What is a socket? communication between server and client
# Where the connection happens, the server listens on a socket to a port (bind) - the client connects
# The server will always listen on a ipaddress:port for connections
# the client connects to that ip address: port - the server accepts or declines incoming connections
# The three way handshake happens
# The client and the server go in a loop of sending and receiving data
# Client sends a closing message, connection closed

# When server and clients communicate they send each other 0s and 1s where a byte is 8 bits together of 0 and 1 
# example

string_var = "something"
print(type(string_var)) # this returns the type str for string

string_var = string_var.encode() # This returns the type bytes as a class - this makes so computers can understand communication

# the problem is that when you receive at the other end being the client let's say, then I need from byte to string

string_var = string_var.decode() # This makes it so we can move things in a network and understand it later as a human, in human readable, if you know how to read, and are a human. 

