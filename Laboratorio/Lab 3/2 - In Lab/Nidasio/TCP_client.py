from socket import *

serverName = 'AlbertoUbuntu'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input('Type your message:')
clientSocket.send(message.encode('utf-8'))

response = clientSocket.recv(1024)
print('Response:', response.decode('utf-8'))

clientSocket.close()