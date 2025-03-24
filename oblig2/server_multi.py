from socket import *
import sys 
import threading
import os
import time



# You should implement a multithreaded server that is capable of serving multiple requests simultaneously
# Using threading, first create a main thread in which your modified server listens for clients at a fixed port
# When it receives a TCP connection request from a client
#  it will set up the TCP connection through another port and services the client request in a separate thread
# There will be a separate TCP connection in a separate thread for each request/response pair
def timeNow():
    """
    returns the time of day
    """
    return time.ctime(time.time())

def handleClient(connectionSocket, addr):
    #this method handles an http client req in its own seperate thread
    #handles empty req
    try:
        message = connectionSocket.recv(1024).decode()
        print(f"Recieved message from {addr} at {timeNow()}")
        print(f"Request: {message.splitlines()[0] if message else 'Empty request'}")

        #parsing the http req to exstract get the filename
        if not message:
            #empty req, and closing the connection
            connectionSocket.close()
            return
        #get the filename from the req
        filename = message.split()[1]
        if filename.startswith('/'):
            filename =filename[1:]

        #now open and read the file
        with open(filename, 'r') as file:
            response_content = file.read()

        header = "HTTP/1.1 200 OK\r\n"	
        header += f"Time: {timeNow()}\r\n"
        header += "Server: MultiThreaded-Server\r\n"
        header += "Content-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(response_content.encode())
    except IOError:
    #send response message if not found
        header = "HTTP/1.1 404 Not Found\r\n"
        header += f"Date: {timeNow()}\r\n"
        header += "Server: MultiThreaded-Server\r\n"
        header += "Content-Type: text/html\r\n\r\n"
    
        response_content = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(header.encode())
        connectionSocket.send(response_content.encode())
    
    except Exception as e:
        print(f"Error handling client request: {e}")
    
    #finally:
        # Close the client connection
        #connectionSocket.close()
       # print(f"Connection with {addr} closed at {timeNow()}")

def main():
    
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #allow reuse of the socket 
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #define my port, 
    serverPort = 5502  
    server_ip = 127.0.0.1

    try:
        serverSocket.bind(('', serverPort))
        print(f'Connection startes on port{server_ip} : {serverPort} at {timeNow()}')
    except:
        print("Connection failed")
        sys.exit()
    #listen for further connections, 5 is max qued connections	
    serverSocket.listen(5)
    print('Server is ready for further connections')	

    try: 
        while True:
            connectionSocket, addr = serverSocket.accept()
            print(f"Server connected by: {addr} at {timeNow()}")
            #create a thread for a new connection
            thread.start_new_thread(handleClient, (connectionSocket))

            print(f"Active threads: {threading.active_count()}")
        
    finally:
        # Close the server socket
        serverSocket.close()
        print("Server socket closed")

if __name__ == '__main__':
    main()