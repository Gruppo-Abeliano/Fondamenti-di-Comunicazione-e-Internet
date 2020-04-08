from socket import *

serverName = 'AlbertoUbuntu'
serverPort = 12001

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print('Server ready')

while 1:
    clientSocket, clientAddress = serverSocket.accept()

    print('Client connected from:', clientSocket.getsockname())

    message = clientSocket.recv(1024).decode('utf-8')
    print('Message received:', message)

    clientSocket.send(message.upper().encode('utf-8'))
    print('Message sent back')

    clientSocket.close()