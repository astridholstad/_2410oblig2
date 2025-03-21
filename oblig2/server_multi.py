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
def timeNow()
	"""
	returns the time of day
	"""
	return time.ctime(time.time())

def handleClient(connection_socket, addr):
	#this method handles an http client req in its own seperate thread
	#handles empty req
	try:
		message = connection_socket.recv(1024).decode()
		print(f"Recieved message from {addr} at {timeNow()}")
		print(f"Request: {message.splitlines()[0] if message else 'Empty request'}")

		#parsing the http req to exstract get the filename
		if not message:
			#empty req, and closing the connection
			connection_socket.close()
			return
		#get the filename from the req
		filename = message.split()[1]
		if filename.startwith('/'):
			filename =filename[1:]

		#if not a spesificed file requested, use the index.html file in folder
		if filename = "":
			filename = "index.html"

		#now open and read the file
		with open(filename, 'rb') as file:
			response_content = file.read()

		header = "HTTP/1.1 200 OK\r\n"	
		header += f"Time: {timeNow()}\r\n"
		header += "Server: MultiThreaded-Server\r\n"

		connectionSocket.send(header.encode())
        connectionSocket.send(response_content)
	
	exceptIOError:
	#send response message if not found
		header = "HTTP/1.1 404 Not Found\r\n"
        header += f"Date: {timeNow()}\r\n"
        header += "Server: MultiThreaded-Server\r\n"
        header += "Content-Type: text/html\r\n"
	
	 	connectionSocket.send(header.encode())
        connectionSocket.send(response_content.encode())
	except Exception as e:
        print(f"Error handling client request: {e}")
    finally:
        # Close the client connection
        connectionSocket.close()
        print(f"Connection with {addr} closed at {timeNow()}")

	
	
	
def main():
	
    serverSocket = socket(AF_INET, SOCK_STREAM)
	#allow reuse of the socket 
	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	#define my port, 
    serverPort = 5501   

    try:
		serverSocket.bind('', serverPort)
		print(f'Server startes on port {serverPort} at {timeNow()}')
    except:
	    print("Connection failed")
	    sys.exit()

	#listen for further connections, 5 is max qued connections	
		
    serverSocket.listen(5)
    print('Server is ready for further connections')	

	try: 
	
    	while True:
			connectionSocket, addr = serverSocket.accept()
			print("Server connected by: {addr} at {timeNow()}")
			#create a thread for a new connection
			client_thread = threading.Thread(target=handleClient, args=(connectionSocket, addr))
			client_thread.daemon = True # set as deamon so it can exist while the main thread exitst
			client_thread.start()

			print(f"Active threads: {threading.active_count()}")


			thread.start_new_thread(handleClient, (connectionSocket,))
    	
	
	exept:
        # Close the server socket
        serverSocket.close()
	
		
if __name__ == '__main__':
	main()