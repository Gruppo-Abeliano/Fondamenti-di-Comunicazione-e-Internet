#########################################à#########  TAGS  ######################################################
#   Autore: Paolo Pertino                                                                                       #
#   Descrizione: Applicazione server side per ricezione di un numero e reinvio di un responso al client,        #
#                indicando se il numero ricevuto è primo o no.                                                  #
#################################################################################################################

# Librerie:
from socket import *

#########################################à####### Funzioni ######################################################
#   - checkPrimeNumber(numero):                                                                                 #
#       Passando in input un numero, la funzione controlla se il numero è primo o no. Restituisce una stringa   #
#       contenente il responso dell'analisi effettuata.                                                         #
#################################################################################################################
def checkPrimeNumber(number):
    if (number == 1 || number == 2):
        return "Il numero e' primo."
    for index in range(2,number):
        # Se il numero è divisibile per un numero compreso tra 2 e 'se stesso-1', allora non è primo.
        if(number % index == 0):
            return "Il numero non e' primo."
    return "Il numero e' primo."

# Definisco la porta del socket.
serverPort = 12004

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
    numberToAnalyze, userAddress = serverSocket.recvfrom(2048)
    numberToAnalyze = numberToAnalyze.decode("utf-8")
    numberToAnalyze = int(numberToAnalyze)

    # Analizzo il numero e spedisco al client la risposta.
    serverResponse = checkPrimeNumber(numberToAnalyze)
    serverSocket.sendto(serverResponse.encode("utf-8"),userAddress)
