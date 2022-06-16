import socket

def main():
    SERVER_PORT = 1233 #server's port
    SERVER_IP = "localhost" #server's ip
    
    while True:
        sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (SERVER_IP, SERVER_PORT)
        sock.connect(server_address)

        server_msg = sock.recv(1024) #recive message with the size of 1024 bytes
        server_msg = server_msg.decode() #need to decode it
        print(server_msg) #print the server message
        while True:
            
            msg = input("choose 1 -8:")
            #input if needed
            
            sock.sendall(msg.encode()) #send nessage to the server
            
            server_msg = sock.recv(5000) #recive message with the size of 1024 bytes
            server_msg = server_msg.decode() #need to decode it
            print(server_msg) #print the server message
            if "bye!!" in server_msg:
                sock.close()
                return 0
        sock.close()
                


main()