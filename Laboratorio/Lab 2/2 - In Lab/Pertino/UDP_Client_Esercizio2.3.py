# Librerie:
from socket import *

# Definisco le informazioni del server, ovvero il suo indirizzo e la porta. Dal momento che stiamo lavorando in locale
# utilizziamo come indirizzo 'localhost' e la porta (scelta casuale) 12000
serverName = "localhost"
serverPort = 12005

# Apro la socket UDP per il client. La specifica UDP viene fatta attraverso il secondo parametro specificato, ovvero
# SOCK_DGRAM. AF_INET,invece, dice che il socket sta utilizzando un indirizzo ipV4
clientSocket = socket(AF_INET,SOCK_DGRAM)

# Per gestire eventuali errori, come per esempio il server spento, imposto un timeout di 5 secondi. Se non ricevo
# risposta dopo 5 secondi, la connessione termina.
clientSocket.settimeout(5)

# Voglio ora inserire una frase per ricavarne il numero di consonanti.
userInput = input("Inserisci una frase per sapere il numero di consonanti che contiene: ")

# Il client ora deve inviare al server il messaggio inserito.
# Viene inviato il messaggio secondo la codifica utf-8, e come secondo parametro le informazioni del server a cui
# recapitare il messaggio
clientSocket.sendto(userInput.encode("utf-8"),(serverName,serverPort))

# Il client ora aspetta di ricevere una risposta. Questa operazione di ascolto fa uso del modulo recvfrom
# Gestisco eventuali errori, come per esempio il server irresistente, o irraggiungibile.
# Se il server è disponibile, viene eseguita la richiesta con scambio di informazioni, altrimenti [EXCEPT] viene
# visualizzato un messaggio di errore personalizzato, ed infine [FINALLY] viene chiuso il socket. Il blocco finally
# viene comunque eseguito alla fine di uno dei due blocchi, try o except.
try:
    numberOfConsonants, fromAddress = clientSocket.recvfrom(2048)
    numberOfConsonants = numberOfConsonants.decode("utf-8")
    print("La frase inserita contiene ", numberOfConsonants, " consonanti.")
except:
    print("Errore di comunicazione con il server indicato.")
finally:
    clientSocket.close()
