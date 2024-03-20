from socket import *

serverName = 'localhost'
serverPort = 12000
#AF_INET per ipv4
#Sock_DGRAM per Datagram (UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Metetil il messaggio:')

clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

modifedeMessage, serverAddress = clientSocket.recvfrom(2048)
modifedeMessage = modifedeMessage.decode('utf-8')
print(modifedeMessage)

clientSocket.close()