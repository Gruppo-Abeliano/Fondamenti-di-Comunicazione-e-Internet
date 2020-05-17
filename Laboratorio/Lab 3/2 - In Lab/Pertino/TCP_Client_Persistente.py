#########################################à#########  TAGS  ######################################################
#   Autore: Paolo Pertino                                                                                       #
#   Descrizione: Applicazione client side per inserimento di una frase ed invio al server TCP su porta 12012.   #
#                Verrà visualizzata la frase inserita in MAIUSCOLO. Il client e il server sono                  #
#                sviluppati per mantenere persistente la connessione TCP                                        #
#################################################################################################################

from socket import *

###################################################  MAIN  ######################################################

# Definisco il server name e la porta del server a cui devo connettermi.
serverName = "localhost"
serverPort = 12012

# Apro la socket del client, specificando l'utilizzo di un indirizzo IpV4 (AF_INET) e il tipo di connessione TCP (SOCK_STREAM)
clientSocket = socket(AF_INET,SOCK_STREAM)

# Connetto il client al server
clientSocket.connect((serverName,serverPort))

# Visto che voglio eseguire una dopo l'altra le operazione senza chiudere subito la connessione, istanzio le prossime istruzioni in un ciclo infinito.
while True:
    # Richiedo all'utente di inserire un messaggio da convertire in caratteri maiuscoli.
    message = input("Inserisci un messaggio da modificare (. per interrompere la connessione): ")

    # Invio il messaggio al server, codificandolo in UTF-8
    clientSocket.send(message.encode("utf-8"))

    # La connessione viene interrotta se il messaggio da modificare è un singolo punto.
    if message == '.':
        print("Interruzione.")
        break

    # Pongo il client in ascolto della risposta, specificando il buffer, in questo caso di 1024 bytes.
    modifiedMessage = clientSocket.recv(1024)

    # Mostro il messaggio modificato.
    print("Messaggio modificato dal server: {}".format(modifiedMessage.decode("utf-8")))

# Chiudo la connessione con il server.
clientSocket.close()
