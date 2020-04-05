# Librerie
from socket import *

# Definisco la porta del socket ed una lista di caratteri da ignorare durante l'analisi di una frase.
serverPort = 12005
lista_caratteri_da_ignorare = ['a','e','i','o','u',' ']

# Apro la socket del server, utilizzando il metodo socket, utilizzando AF_INET per indicare l'utilizzo di un indirizzo
# ipV4 e SOCK_DGRAM per indicare il tipo di connessione UDP.
serverSocket = socket(AF_INET,SOCK_DGRAM)

# Devo ora associare la socket all'indirizzo localhost e alla porta definita prima.
serverSocket.bind(('',serverPort))

# Messaggio informativo di avvenuta apertura della socket.
print("Server pronto a ricevere informazioni.")

# Metto il server in ascolto, aspettando informazioni. Devo specificare la dimensione del buffer all'interno del metodo
# recvfrom. Visto che il server deve essere sempre in ascolto, anche dopo aver elaborato l'informazione di un client,
# le prossime istruzioni vengono poste in un loop-infinito.
while True:
    messageToAnalyze, userAddress = serverSocket.recvfrom(2048)

    # Decodifico il messaggio ricevuto.
    messageToAnalyze = messageToAnalyze.decode("utf-8")

    # Converto la frase ricevuta in tutti caratteri minuscoli per facilitarne l'analisi.
    messageToAnalyze = messageToAnalyze.lower()

    # Scorro tutti gli elementi della lista 'lista_caratteri_da_ignorare' e tengo conto complessivamente
    # quanti di questi caratteri sono effettivamente presenti nella frase.
    contatoreVocaliPresenti = 0
    for lettera in lista_caratteri_da_ignorare:
        contatoreVocaliPresenti += messageToAnalyze.count(lettera)

    # Il numero di consonanti presenti sarà dunque la lunghezza della frase, a cui vengono sottratte
    # il numero di spazi e vocali.
    numeroConsonantiPresenti = len(messageToAnalyze) - contatoreVocaliPresenti

    # Restituisco al client il risultato ottenuto.
    serverSocket.sendto(str(numeroConsonantiPresenti).encode("utf-8"), userAddress)
