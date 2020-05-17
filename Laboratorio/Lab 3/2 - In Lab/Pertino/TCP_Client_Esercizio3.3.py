#########################################à#########  TAGS  ######################################################
#   Autore: Paolo Pertino                                                                                       #
#   Descrizione: Applicazione client side per inserimento di un numero ed invio al server TCP su porta 12003.   #
#                Verrà visualizzato un messaggio informativo, indicando se il numero inserito è primo o no.     #
#################################################################################################################

# Librerie:
from socket import *

###################################################  MAIN  ######################################################

# Definisco le informazioni del server, ovvero il suo indirizzo e la porta. Dal momento che stiamo lavorando in locale
# utilizziamo come indirizzo 'localhost' e la porta (scelta casuale) 12003
serverName = "localhost"
serverPort = 12003

# Apro la socket TCP per il client. La specifica TCP viene fatta attraverso il secondo parametro specificato, ovvero
# SOCK_STREAM. AF_INET,invece, dice che il socket sta utilizzando un indirizzo ipV4
# Mi collego al server attraverso i parametri prima definiti.
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Per gestire eventuali errori, come per esempio il server spento, imposto un timeout di 2 secondi. Se non ricevo
# risposta dopo 2 secondi, la connessione termina.
clientSocket.settimeout(2)

# Viene richiesto all'utente di inserire un numero.
userInput = input("Inserisci un numero da analizzare : ")

# Il client ora deve inviare al server il messaggio inserito.
# Viene inviato il messaggio secondo la codifica utf-8, e come secondo parametro le informazioni del server a cui
# recapitare il messaggio
clientSocket.sendto(userInput.encode("utf-8"),(serverName,serverPort))

# Il client ora aspetta di ricevere una risposta. Questa operazione di ascolto fa uso del modulo recv
# Gestisco eventuali errori, come per esempio il server irresistente, o irraggiungibile.
# Se il server è disponibile, viene eseguita la richiesta con scambio di informazioni, altrimenti [EXCEPT] viene
# visualizzato un messaggio di errore personalizzato, ed infine [FINALLY] viene chiuso il socket. Il blocco finally
# viene comunque eseguito alla fine di uno dei due blocchi, try o except.
try:
    serverResponse = clientSocket.recv(2048)
    serverResponse = serverResponse.decode("utf-8")
    print(serverResponse)
except:
    print("Errore di comunicazione con il server indicato.")
finally:
    clientSocket.close()
