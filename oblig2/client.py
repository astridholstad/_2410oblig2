import argparse
import socket
import sys


#Your client will connect to the server using a TCP connection
# send an HTTP request to the server,
# and display the server response as an output
# You can assume that the HTTP request sent is a GET method
# the client should take command line arguments specifying the server IP address or host name
# the port at which the server is listening
# and the path at which the requested object is stored at the server (hint: argeparse)
#  to run the client: python3 client.py -i <server_ip> -p <server_port> -f filename

def send_req(server_ip, server_port, filename):
    #the method creates a TCP connection to the server, sends a http get req,
    #and return the servers response
    #first creaate a TCP socket:
    try: 
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         #Connect to the server
        client_socket.connect((server_ip, int(server_port)))
        #path need to be valid: start with /
        path = f'/{filename}' if not filename.startswith("/") else filename
        http_req = f"GET {path} HTTP/1.1\r\nHost: {server_ip}\r\nConnection: close\r\n\r\n"
        #now send the req to the server
        client_socket.send(http_req.encode())
        #recieve the response from server
        response = b""
        while True:
            message =client_socket.recv(4096)
            if not message:
                break
            response += message
        #close the socket connection
        client_socket.close()
        return response.decode('utf-8', errors="replace")
    except socket.error as e:  
        return f"Socket error: {e}"
    except Exception as e:
        return f"Error: {e}"

 #main method
def main():
    #use command line parsing
    parser = argparse.ArgumentParser('description=HTTP Client')   
    parser.add_argument('-i', '--server_ip', required=True, help='Server IP adress')
    parser.add_argument('-p', '--server_port', required=True, help="Server port number")
    parser.add_argument('-f', '--filename', required=True, help='Path to file on the server')
    #parse them
    args = parser.parse_args()

    #send a http req and get response 
    response = send_req(args.server_ip, args.server_port, args.filename)
    #print the response from server
    print(response)

if __name__ == "__main__":
    main()




