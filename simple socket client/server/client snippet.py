
import socket

# To make a connection to a TCP server:

# Create a socket. AF_INET means you're connecting to an IPv4 IP
#  Address.
# SOCK_STREAM means you are connecting over TCP and not UDP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tell the socket what IP Address and Port number to connect to.
clientsocket.connect(('127.0.0.1', 9987))
# Send some data over the socket.
clientsocket.send('hello')

data = clientsocket.recv(1024)
print(data)

# To make a TCP Server:

# Create a socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to listen to a port.
serversocket.bind(("127.0.0.1", 9985))
# Tell the socket to start listening.
# The 10 is the maximum number of connections.
serversocket.listen(10)

# Setup an infinite loop so the socket will keep listening for
# incoming connections.
while True:
    # If it gets a new connection, accept it and save the connection
    # and address.
    connection, address = serversocket.accept()
    # Read 1024 bytes of data from the connection.
    data = connection.recv(1024)
    # Check the length of data. If the length is more than 0 then
    # that means something was sent, so print it out.
    if len(data) > 0:
        print("Received: " + data)

    # Close the connection.
    connection.close()
    # We don't need to keep listening any more so break out of the
    # infinite loop
    break

# Close the socket.
serversocket.close()


