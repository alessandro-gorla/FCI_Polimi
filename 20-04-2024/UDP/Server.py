from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server Rady")

while True:
    message, clientAddress = serverSocket.recvfrom(2024)
    print("Datagramma da: ", clientAddress)
    message = message.decode("utf-8")
    modifidedMessage = message.upper()
    #print(modifidedMessage)
    serverSocket.sendto(modifidedMessage.encode('utf-8'), clientAddress)
