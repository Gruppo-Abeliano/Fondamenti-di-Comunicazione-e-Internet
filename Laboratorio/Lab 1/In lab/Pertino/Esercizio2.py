# Ripeto l'operazione dell'esercizio 1, ma facendola più volte insieme.

import requests

# Faccio la valutazione 10 volte, e salvo il minimo, il massimo e il medio valore ricevuto.
tempi_risposta = []

# Eseguo il ciclo per 10 volte
for index in range(10):
    # Lancio un get-request verso il server di google per scaricare l'homepage ad ogni ciclo.
    # In request_to_server verrà salvato un oggetto contenente tutte le informazioni statistiche della risposta.
    # Per ogni ciclo request_to_server verrà sovrascritto.
    request_to_server = requests.get('http://www.google.com')

    tempo_corrente = request_to_server.elapsed.microseconds/1000
    # Aggiungo alla lista dei tempi di risposta, il tempo preso in esame in questo ciclo.
    tempi_risposta.append(tempo_corrente)

    print('Il tempo di risposta ',index+1, ': ', tempo_corrente, ' ms')

# Elaboro infine la lista di tempi ottenuti, estraendone il massimo,minimo e medio valore.
print('Tempo massimo: ',max(tempi_risposta),'\nTempo minimo: ',min(tempi_risposta),'\nTempo medio: ',sum(tempi_risposta)/len(tempi_risposta))
