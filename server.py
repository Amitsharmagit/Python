# Programming in Python
# Server.py
# Import the socket,sys and os library.
import sys
import socket     
import os
ip:port

# Create a socket object
skServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind to the port
# Default port for socket
# connect to the server on local computer
skServer.bind(("127.0.0.1",8889))

# Put the socket into listening mode
skServer.listen(10)
print "Server Active"
bFileFound = 0

# a forever loop until we interrupt it or 
# an error occurs
while True:
    # Establish connection with client.
    Content,Address = skServer.accept()
    print Address
    sFileName = Content.recv(1024)
    for file in os.listdir("/home/amit/Desktop/socket_program/123s.py"):
        if file == sFileName:
            print "in condition 1"
            bFileFound = 1
            break
 
    if bFileFound == 0:
        print sFileName+" Not Found On Server"
 
    else:
        print sFileName+" File Found"
        fUploadFile = open(sFileName,"rb")
        sRead = fUploadFile.read(1024)
        while sRead:
            Content.send(sRead)
            sRead = fUploadFile.read(1024)
        print "Sending Completed"
    break

# Close the connection with the client
Content.close()
skServer.close()
