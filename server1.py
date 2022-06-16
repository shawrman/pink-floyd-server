import socket
import os
from _thread import *
import data
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
client_msg = ""
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a client_soc..')
ServerSocket.listen(5)


def threaded_client(client_soc):
    
    msg = """----Pink Floyd----
            1 = Album list of the band(parameter = none)
            2 = Album Playlist(parameter = Album Name)
            3 = Get the length of a song(parameter = song Name)
            4 = Get lyrics of a song(parameter = song Name)
            5 = What album is the song in?(parameter = song Name)
            6 = Search for a song by name(parameter = word in song Name)
            7 = Search for a song by lyrics in a song(parameter = word in lyrics in a song)
            8 = exit(parameter = none)
            how to use my server!
            that's the message format:
            (option 1 -8)#(input - if needed)
            """

    client_msg = ""
    client_soc.sendall(msg.encode())
    while(client_msg != "QUIT"):
        try:
            # wating to recive a message
            client_msg = client_soc.recv(1024)
            client_msg = client_msg.decode()
            if client_msg[1] == '#':
                if client_msg[0] == '1':
                # sending answer
                    msg = data.listOfAlbums()
                    client_soc.sendall(msg.encode())
                if client_msg[0] == '2':
                # sending answer
                    #after the number its the input
                    msg = data.listSongsInAlbum(client_msg[2::])
                    client_soc.sendall(msg.encode())
                if client_msg[0] == '3':
                # sending answer
                    #after the number its the input
                    msg = data.lengthOfASong(client_msg[2::])
                    client_soc.sendall(msg.encode())
                if client_msg[0] == '4':
                # sending answer
                    #after the number its the input
                    msg = data.wordsOfASong(client_msg[2::])
                    client_soc.sendall(msg.encode())
                if client_msg[0] == '5':
                # sending answer
                    #after the number its the input
                    msg = data.whatAlbumIsTheSong(client_msg[2::])
                    client_soc.sendall(msg.encode())
                if client_msg[0] == '6':
                # sending answer
                    #after the number its the input
                    msg = data.searchSongByName(client_msg[2::])
                    client_soc.sendall(msg.encode())
                if client_msg[0] == '7':
                # sending answer
                    #after the number its the input
                    msg = data.songByLyrics(client_msg[2::])
                    client_soc.sendall(msg.encode())
                if client_msg[0] == '8':
                # sending answer
                    client_msg = "QUIT!"
                    msg = "bye!!"
                    client_soc.sendall(msg.encode())
                    client_soc.close()
                    break
            else: 
                msg = "invalid format"
                client_soc.sendall(msg.encode())
            
            
        except:
            msg = "try again!"
            client_soc.sendall(msg.encode())
    client_soc.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()