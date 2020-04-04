# Librerie:
import requests

#########################################à####### Funzioni ######################################################
#   - calcolaMedia(lista di numeri):                                                                            #
#       Passando in input una lista contenente numeri, essa calcola e restituisce la media dei valori contenuti #
#       in tale lista.                                                                                          #
#################################################################################################################
def calcolaMedia(lista_tempi):
    somma_totale = 0
    for index in range(len(lista_tempi)):
        somma_totale += lista_tempi[index]

    return somma_totale/len(lista_tempi)

################################################# Main ##########################################################

lista_siti = ['http://www.google.com','http://www.youtube.com','http://www.polimi.it','http://www.wikipedia.org','http://www.amazon.com','http://www.twitter.com']

# Elaboro la lista elemento per elemento
for url in lista_siti:
    print('Elaborando il sito : ',url)

    # Per ogni sito vengono fatte 10 richieste, pertanto per elaborare tutti i 10 tempi di risposta devo salvarli
    # uno per uno in una lista, che per ogni nuovo sito verrà ovviamente sovrascritta.
    lista_tempi_corrente = []
    for index in range(10):
        request = requests.get(url)
        lista_tempi_corrente.append(request.elapsed.microseconds/1000)
        print('Richiesta ',index+1, ': ',request.elapsed.microseconds/1000)

    # Calcolo la media dei tempi del sito corrente e la stampo a schermo.
    media_corrente = calcolaMedia(lista_tempi_corrente)
    print('Media di ',url, ': ',media_corrente)

    # Per controllare il sito migliore in tempi di risposta, ho bisogno di tenere traccia di quello con le performance
    # migliori. Pertanto il primo sito (lista_siti.index(url) == 0) lo considero come il migliore, e invece i
    # successivi li confronto con il migliore corrente.
    if lista_siti.index(url) == 0:
        media_migliore = media_corrente
        sito_migliore = url
    else:
        if media_corrente<media_migliore:
            media_migliore = media_corrente
            sito_migliore = url

    print('\n')

print('Il sito migliore è ',sito_migliore)
