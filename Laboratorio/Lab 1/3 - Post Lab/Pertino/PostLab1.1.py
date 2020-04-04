############################################ DISCLAIMER ################################################
### VERSIONE NON OTTIMIZZATA. PER VEDERE UNA SOLUZIONE MIGLIORE CONSULTARE L'ESERCIZIO PostLab1.2.py ###
########################################################################################################

# Librerie utilizzate
import requests

# Funzioni:
#   - calcolaMedia(lista di numeri):
#       Passando in input una lista contenente numeri, essa calcola e restituisce la media dei valori contenuti
#       in tale lista.
def calcolaMedia(lista_tempi):
    somma_totale = 0
    for index in range(len(lista_tempi)):
        somma_totale += lista_tempi[index]

    return somma_totale/len(lista_tempi)

# Main:
# compilo la lista dei siti da elaborare.
lista_siti = ['http://www.google.com','http://www.youtube.com']

#Elaboro il primo sito
tempi_sito1 = []
print('Elaborazione sito ',lista_siti[0])
for indice in range(10):
    request1 = requests.get(lista_siti[0])
    print('Richiesta ',indice+1,': ',request1.elapsed.microseconds/1000)
    tempi_sito1.append(request1.elapsed.microseconds/1000)

media_sito1 = calcolaMedia(tempi_sito1)
print('La media di ',lista_siti[0], ' è ',media_sito1)

#Elaboro il secondo sito
tempi_sito2 = []
print('Elaborazione sito ',lista_siti[1])
for indice in range(10):
    request2 = requests.get(lista_siti[1])
    print('Richiesta ',indice+1,': ',request2.elapsed.microseconds/1000)
    tempi_sito2.append(request2.elapsed.microseconds/1000)

media_sito2 = calcolaMedia(tempi_sito2)
print('La media di ',lista_siti[1], ' è ',media_sito2)

if media_sito1 > media_sito2:
    print('Il miglior sito è: ',lista_siti[1])
else :
    print('Il miglior sito è: ',lista_siti[0])
