# Ora vogliamo calcolare i tempi di risposta di multipli server http.
import requests
import matplotlib.pyplot as PLOT

# Creo una lista con tutti i siti interessati.
lista_siti = ['http://www.google.com/','http://www.facebook.com','http://www.netflix.com']

# Istanzio una variabile ausiliaria che mi servirà per disegnare correttamente il grafico.
massimo_dei_massimi = 0
# Apro la finestra del grafico.
PLOT.figure()

# Scorro la lista oggetto per oggetto
for url in lista_siti:
    print('Sto testando il sito: ',url, '\n')
    # Per ogni sito, voglio ricavare 10 tempi di risposta, pertanto per inserire la lista di dati nel grafico
    # devo prima salvarli (tempi_sito_attuale)
    tempi_sito_attuale = []

    for indice in range(10):
        request = requests.get(url)
        tempi_sito_attuale.append(request.elapsed.microseconds/1000)

    # Aggiungo i dati del sito che sto controllando nel grafico
    PLOT.plot(tempi_sito_attuale, label = url)

    # Infine Voglio mostrare i dati del singolo sito
    print('Tempo massimo: ',max(tempi_sito_attuale),'\nTempo minimo: ',min(tempi_sito_attuale),'\nTempo medio: ',sum(tempi_sito_attuale)/len(tempi_sito_attuale))
    massimo_dei_massimi = max(massimo_dei_massimi,max(tempi_sito_attuale))

# Setto il limite per il grafico
PLOT.ylim([0, 1.1*massimo_dei_massimi])
# Definisco con apposite etichette il titolo del grafico e degli assi.
PLOT.title('Test Lista di siti')
PLOT.xlabel('ID Richiesta')
PLOT.ylabel('Tempo di attesa [ms]')
# Istanzio una legenda nell'angolo in basso a destra
PLOT.legend(loc = 'lower right',fontsize = 8)
# Mostro il grafico con una griglia
PLOT.grid()
PLOT.show()
