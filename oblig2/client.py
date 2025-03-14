from socket import *

#Your client will connect to the server using a TCP connection
# send an HTTP request to the server,
# and display the server response as an output
# You can assume that the HTTP request sent is a GET method
# the client should take command line arguments specifying the server IP address or host name
# the port at which the server is listening
# and the path at which the requested object is stored at the server (hint: argeparse)
#  to run the client: python3 client.py -i <server_ip> -p <server_port> -f filename