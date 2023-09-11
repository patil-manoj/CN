

from socket import *

serverName = "127.0.0.1"

serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)
sentence = input("\nEnter the name of the file:")

clientSocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))

fileContents,servaddr = clientSocket.recvfrom(2048)

print("Reply from server:\n")
print(fileContents.decode("utf-8"))


clientSocket.close()