from socket import *


serverName = "127.0.0.1"

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind((serverName,serverPort))

# serverSocket.listen(1)
print("The Server is ready to receive")
while(1):
    
    sentence,addr = serverSocket.recvfrom(2048)
    sentence = sentence.decode("utf-8")
    file = open(sentence,"r")
    l = file.read(2048)
    serverSocket.sendto(bytes(l,"utf-8"),addr)
    
 
    print("\nSent contents of " + sentence) 
    file.close()
