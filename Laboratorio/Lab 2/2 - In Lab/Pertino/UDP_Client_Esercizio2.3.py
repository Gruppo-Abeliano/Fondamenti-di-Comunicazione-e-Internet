from socket import *

serverName = "localhost"
serverPort = 12005

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(5)

userInput = input("Inserisci una frase per sapere il numero di consonanti che contiene: ")

clientSocket.sendto(userInput.encode("utf-8"),(serverName,serverPort))

try:
    numberOfConsonants, fromAddress = clientSocket.recvfrom(2048)
    numberOfConsonants = numberOfConsonants.decode("utf-8")
    print("La frase inserita contiene ", numberOfConsonants, " consonanti.")
except:
    print("Errore di comunicazione con il server indicato.")
finally:
    clientSocket.close()
