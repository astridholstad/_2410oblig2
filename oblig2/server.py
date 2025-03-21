from socket import *
import sys # In order to terminate the program

#i will develop a server that handles one http req at a time
#the web server should accept and parse a http req 
#get the requested file from the server’s file system
# create an HTTP response message consisting of the requested file preceded by header line
# and then send the response directly to the client
# if the requested file is not present in the server, the server should sendan HTTP “404 Not Found” message back to the client

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 5505
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #etablish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print(f"Recieved message: {message}")

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read
        #Send one HTTP header line into socket, 200 ok
        header = "HTTP/1.1 200 OK \r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
    except IOError:
         #Send response message for file not found
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response = "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(response())
       #Close client socket
        connectionSocket.close()

    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data
