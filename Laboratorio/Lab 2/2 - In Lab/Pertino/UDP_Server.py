# Librerie:
from socket import *

# Definisco la porta del socket.
serverPort = 12000

# Apro la socket del server, utilizzando il metodo socket, utilizzando AF_INET per indicare l'utilizzo di un indirizzo
# ipV4 e SOCK_DGRAM per indicare il tipo di connessione UDP.
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Devo ora associare la socket all'indirizzo localhost e alla porta definita prima.
serverSocket.bind(('', serverPort))

# Messaggio informativo
print('Il server è pronto a ricevere informazioni.')

# Metto il server in ascolto, aspettando informazioni. Devo specificare la dimensione del buffer all'interno del metodo
# recvfrom. Visto che il server deve essere sempre in ascolto, anche dopo aver elaborato l'informazione di un client,
# le prossime istruzioni vengono poste in un loop-infinito.
while True:
    clientMessage, clientAddress = serverSocket.recvfrom(2048)

    print(clientAddress)

    # Decodifichiamo il messaggio ricevuto.
    clientMessage = clientMessage.decode('utf-8')

    # Converto il messaggio dell'utente, rendendo maiuscole tutte le lettere.
    modifiedClientMessage = clientMessage.upper()

    # Invio il messaggio modificato al client, specificandone l'indirizzo memorizzato alla ricezione dell'informazione.
    serverSocket.sendto(modifiedClientMessage.encode('utf-8'), clientAddress)
