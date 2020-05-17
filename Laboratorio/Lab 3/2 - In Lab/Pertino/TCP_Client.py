#########################################à#########  TAGS  ######################################################
#   Autore: Paolo Pertino                                                                                       #
#   Descrizione: Applicazione client side per inserimento di una frase ed invio al server TCP su porta 12012.   #
#                Verrà visualizzata la frase inserita in MAIUSCOLO. Modalità NON persistente.                   #
#################################################################################################################

from socket import *

###################################################  MAIN  ######################################################

# Definisco il server name e la porta del server a cui devo connettermi.
serverName = "localhost"
serverPort = 12000

# Apro la socket del client, specificando l'utilizzo di un indirizzo IpV4 (AF_INET) e il tipo di connessione TCP (SOCK_STREAM)
clientSocket = socket(AF_INET,SOCK_STREAM)

# Connetto il client al server
clientSocket.connect((serverName,serverPort))

# Richiedo all'utente di inserire un messaggio da convertire in caratteri maiuscoli.
message = input("Inserisci un messaggio da modificare: ")

# Invio il messaggio al server, codificandolo in UTF-8
clientSocket.send(message.encode("utf-8"))

# Pongo il client in ascolto della risposta, specificando il buffer, in questo caso di 1024 bytes.
modifiedMessage = clientSocket.recv(1024)

# Mostro il messaggio modificato.
print("Messaggio modificato dal server: {}".format(modifiedMessage.decode("utf-8")))

# Chiudo la connessione con il server.
clientSocket.close()
