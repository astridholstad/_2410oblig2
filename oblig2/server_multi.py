from socket import *
import sys 
import _thread as thread
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

def handleClient(connection):
	while True:
		message = connection.recv(1024).decode()
		print(f"Recieved message: {message}")
		if(message == "exit"):
			break
		connection.close()
		
		

def main():
	
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 12000    

    try:
	serverSocket.bind('', serverPort)
	
    except:
	    print("Connection failed")
	    sys.exit()
		
    serverSocket.listen(1)
    print('Server is ready for connection')	
	
    while True:
		connectionSocket, addr = serverSocket.accept()
		print("Server connected by: ", addr)
		print('at ', timeNow())
		thread.start_new_thread(handleClient, (connectionSocket,))
    serverSocket.close()
	
		
if __name__ == '__main__':
	main()