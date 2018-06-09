# Programming in Python
# Client.py
# Import the socket,sys library.
 
import sys
import socket 
 
# Create a socket object
skClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skClient.connect(("127.0.0.1",8889))
 
sFileName = raw_input("Enter Filename to download from server : ")

# a forever loop until we interrupt it or 
# an error occurs
 
while True:
    skClient.send(sFileName)
    print "data sent"
    sData = skClient.recv(1024)
    fDownloadFile = open("abcd.txt","wb")
    while sData:
        fDownloadFile.write(sData)
        sData = skClient.recv(1024)
    print "Download Completed"
    break
# Close the connection with the Server. 
skClient.close()
