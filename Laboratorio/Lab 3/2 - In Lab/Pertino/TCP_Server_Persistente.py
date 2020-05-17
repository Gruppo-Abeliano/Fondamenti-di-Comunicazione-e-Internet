#########################################à#########  TAGS  ######################################################
#   Autore: Paolo Pertino                                                                                       #
#   Descrizione: Applicazione server side per ricezione di una frase e il reinvio della stessa trasformata in   #
#                caratteri maiuscoli. Il client e il server sono sviluppati per mantenere persistente la        #
#                connessione TCP.                                                                               #
#################################################################################################################

from socket import *

###################################################  MAIN  ######################################################

# Definisco la porta su cui aprire il processo.
serverPort = 12012

# Apro la welcome socket del server, specificando l'utilizzo di un indirizzo ipV4 (AF_INET) e il tipo di connessione TCP (SOCK_DGRAM)
# Collego successivamente il welcome socket alla porta definita prima.
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

# Metto il server in ascolto (operazione di PASSIVE OPEN). Ora il server aspetta richieste di collegamento/connessione dai client.
serverSocket.listen(1)

# Messaggio informativo.
print("Server pronto.")

# Il server deve rimanere sempre in ascolto per nuove connessioni, pertanto istanzio in un ciclo infinito le restanti operazioni.
# Ora verrà aperto, all'arrivo di una richiesta di connessione client, un nuovo socket, ovvero il connectionSocket.
# Alla fine della comunicazione verrà chiuso il connectionSocket, mentre il welcomeSocket rimarrà aperto!
while True:
    # Accetto la connessione in entrata e salvo anche l'indirizzo del client.
    connectionSocket, clientAddress = serverSocket.accept()

    # Messaggio informativo
    print("Connessione instaurata con il client.")

    # Visto che voglio poter ricevere più di una frase con la stessa connessione, senza dover interromperla ad ogni operazione, istanzio le prossime istruzioni in un secondo ciclo infinito.
    while True:
        # Pongo il server in ascolto del messaggio da ricevere.
        messageToModify = connectionSocket.recv(1024)

        # Decodifico il messaggio
        messageToModify = messageToModify.decode("utf-8")
        print(messageToModify)
        # Se il messaggio ricevuto è un singolo punto, allora termino la connessione corrente.
        if messageToModify == '.':
            print("Interruzione.")
            break

        # Altrimenti creo il nuovo messaggio modificato con il testo in maiuscolo.
        modifiedMessage = messageToModify.upper()

        # Attraverso la connection socket (!!! NON LA WELCOME SOCKET !!!) invio il messaggio modificato al client, codificandolo in UTF-8
        connectionSocket.send(modifiedMessage.encode("utf-8"))

    # Chiudo la connessione con il client, ma rimango in attesa di nuovi collegamenti, in quanto la welcome socket rimane aperta.
    connectionSocket.close()
