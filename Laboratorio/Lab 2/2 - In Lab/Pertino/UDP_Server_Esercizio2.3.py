from socket import *

serverPort = 12005
lista_caratteri_da_ignorare = ['a','e','i','o','u',' ']

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("Server pronto a ricevere informazioni.")

while True:
    messageToAnalyze, userAddress = serverSocket.recvfrom(2048)
    messageToAnalyze = messageToAnalyze.decode("utf-8")
    messageToAnalyze = messageToAnalyze.lower()

    print(messageToAnalyze)

    contatoreVocaliPresenti = 0
    for lettera in lista_caratteri_da_ignorare:
        contatoreVocaliPresenti += messageToAnalyze.count(lettera)

    numeroConsonantiPresenti = len(messageToAnalyze) - contatoreVocaliPresenti
    serverSocket.sendto(str(numeroConsonantiPresenti).encode("utf-8"), userAddress)
