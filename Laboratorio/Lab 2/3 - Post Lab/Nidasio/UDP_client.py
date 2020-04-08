from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)

message = input()

client_socket.sendto(message.encode('utf-8'), ('185.178.92.194', 1234))

client_socket.close()