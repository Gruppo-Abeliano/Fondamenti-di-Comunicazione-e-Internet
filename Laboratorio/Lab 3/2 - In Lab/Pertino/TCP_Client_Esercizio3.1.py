#########################################à#########  TAGS  ######################################################
#   Autore: Paolo Pertino                                                                                       #
#   Descrizione: Applicazione client side per inserimento di una frase ed invio al server TCP su porta 12003.   #
#                Verrà visualizzato un messaggio informativo, indicando se il numero di consonanti presenti     #
#                nella frase inserita.                                                                          #
#################################################################################################################

# Librerie:
from socket import *

###################################################  MAIN  ######################################################

# Definisco nome e porta del server a cui connettermi.
serverName = "localhost"
serverPort = 12003

# Apro la socket lato client, specificando l'utilizzo di indirizzo ipV4 (AF_INET) e il tipo  di connessione TCP (SOCK_STREAM)
clientSocket = socket(AF_INET,SOCK_STREAM)

# Mi collego al server utilizzando i parametri prima definiti.
# Setto inoltre un timeout di 5 secondi.
clientSocket.connect((serverName,serverPort))
clientSocket.settimeout(5)

# Richiedo all'utente una frase da elaborare.
messageToAnalyze = input("Inserisci una frase da analizzare: ")

# Spedisco il messaggio al server codificandolo in utf-8.
clientSocket.send(messageToAnalyze.encode("utf-8"))

# Attendo una risposta dal server, speciiicando la dimensione del buffer (in questo caso 2048 bytes).
# Gestisco anche l'eventualita' in cui il server non risponda nel tempo prestabilito (5 secondi).
# Infine chiudo la connessione.
try:
    numberOfConsonants = clientSocket.recv(2048)
    numberOfConsonants = numberOfConsonants.decode("utf-8")

    # Stampo a schermo il messaggio informativo.
    print("All'interno della frase inserita vi sono {} consonanti.".format(numberOfConsonants))
except:
    # Gestisco l'errore mostrando un messaggio.
    print("Errore durante la connessione con il server.")
finally:
    clientSocket.close()
