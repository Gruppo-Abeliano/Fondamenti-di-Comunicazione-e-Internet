from socket import *
from sympy import isprime

server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket
server_socket.bind(('', 1234))

# Receive data
while 1:
    message, (client_ip, client_port) = server_socket.recvfrom(2048)

    print('Datagram from:', client_ip, client_port)
    payload = message.decode('utf-8')

    print('Datagra payload:', payload)

    # Check if the payload contains a number
    try:
        number = int(payload)

        # Check if the number is a prime
        if isprime(number):
            server_socket.sendto('The number is a prime\n'.encode('utf-8'), (client_ip, client_port))
            print('The number is a prime')
        else:
            server_socket.sendto('The number is not a prime\n'.encode('utf-8'), (client_ip, client_port))
            print('The number is not a prime')
    except:
        server_socket.sendto('The data must be a number, otherwise I can\'t tell you if it is a prime\n'.encode('utf-8'), (client_ip, client_port))
        print('The data must be an integer number, otherwise I can\'t tell you if it is a prime\n')
