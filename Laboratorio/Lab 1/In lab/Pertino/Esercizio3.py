# Voglio ora invece fare un grafico con i dati ottenuti. Mi serve la libreria matplotlib e quindi la importo,
# insieme alla request.
# N.B. Viene importato il modulo pyplot della libreria matplotlib assegnadogli un'etichetta. Questo ci permette
#      durante la scrittura del codice di richiamare il modulo attraverso la sola etichetta(in questo caso PLOT),
#      senza dover ripetere ogni volta il nome della libreria e l'accesso al modulo interessato (matplotlib.pyplot)
import requests
import matplotlib.pyplot as PLOT

# Lancio un get-request verso il server di google per scaricare l'homepage.
# In request_to_server verrà salvato un oggetto contenente tutte le informazioni statistiche della risposta.
# Faccio la valutazione 10 volte, e salvo il minimo, il massimo e il medio valore ricevuto.
tempi_risposta = []

for index in range(20):
    request_to_server = requests.get('http://www.google.com')

    tempo_corrente = request_to_server.elapsed.microseconds/1000
    tempi_risposta.append(tempo_corrente)

    print('Il tempo di risposta ',index+1, ': ', tempo_corrente, ' ms')

# Elaboro infine la lista di tempi ottenuti, estraendone il massimo,minimo e medio valore.
print('Tempo massimo: ',max(tempi_risposta),'\nTempo minimo: ',min(tempi_risposta),'\nTempo medio: ',sum(tempi_risposta)/len(tempi_risposta))

# Creo i grafici, utilizzando la funzione figure.
# Creo il grafico.
PLOT.figure()
# Inserisco i valori al suo interno
PLOT.plot(tempi_risposta)
# Creo i limiti dell'asse Y
PLOT.ylim([0, 1.1*max(tempi_risposta)])
# Inserisco delle etichette sull'asse x, sull'asse y e per il titolo
PLOT.xlabel('ID Richiesta')
PLOT.ylabel('Tempi di risposta [ms]')
PLOT.title(request_to_server.url)
# Mostro il grafico con la griglia.
PLOT.grid()
PLOT.show()
