#########################################à#########  TAGS  ######################################################
#   Autore: Paolo Pertino                                                                                       #
#   Descrizione: Applicazione server side per ricezione di una frase e reinvio di un responso al client,        #
#                indicando il numero di consonanti presenti in essa.                                            #
#################################################################################################################

# Librerie:
from socket import *

###################################################  MAIN  ######################################################

# Definisco una lista di vocali, per poter eseguire l'analisi sul messaggio richiesta dal testo dell'esercizio.
lista_caratteri_inutili = ['a','e','i','o','u',' ']

# Definisco la porta da associare al processo lato server.
serverPort = 12003

# Apro il welcome socket lato server, specificando l'utilizzo di un indirizzo ipV4 (AF_INET), e il tipo di connessione TCP (SOCK_STREAM)
# Collego infine la socket creata alla porta prima definita.
welcomeSocket = socket(AF_INET,SOCK_STREAM)
welcomeSocket.bind(('',serverPort))

# Pongo in ascolto il server, per poter ricevere le connessioni TCP da parte dei client.
welcomeSocket.listen(1)

# Messaggio informativo
print("Server pronto a ricevere informazioni.")

while True:
    # Accetto la richiesta della connessione del client, salvandone anche l'indirizzo ip.
    connectionSocket, clientAddress = welcomeSocket.accept()

    # Messaggio informativo di avvenuta connessione.
    print("Connesso con {}".format(clientAddress))

    # Metto il server in ricezione del messaggio da analizzare.
    messageToAnalyze = connectionSocket.recv(2048)
    messageToAnalyze = messageToAnalyze.decode("utf-8")

    # Converto il messaggio in minuscolo, in modo tale da semplificare l'analisi richieta.
    contaCaratteriInutili = 0
    for carattere in lista_caratteri_inutili:
        contaCaratteriInutili += messageToAnalyze.count(carattere)

    # A questo punto, ho il numero di vocali e spazi contenuti nella frase. Per calcolare il numero di consonanti, mi bastera' togliere dalla lunghezza totale del messaggio
    # il numero di caratteri inutili (vocali e spazi).
    # Restituisco quindi il valore al client in formato stringa e codificato in utf-8.
    connectionSocket.send(str(len(messageToAnalyze)-contaCaratteriInutili).encode("utf-8"))

    # Chiudo la connessione con il client (!!! NON LA WELCOME SOCKET !!!).
    connectionSocket.close()
