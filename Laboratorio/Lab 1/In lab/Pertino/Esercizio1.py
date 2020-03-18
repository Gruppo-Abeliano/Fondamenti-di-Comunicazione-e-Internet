# Voglio valutare il tempo di risposta del server di google nel fornirmi la homepage.
# Voglio creare un get-request, ovvero lo strumento che mi permette di scaricare la pagina.
# Utilizziamo il modulo request; esso ci permette di generare richieste http,ricevere risposte
# ed informazioni statistiche riguardanti l'informazione stessa ricevuta.

import requests

# Lancio un get-request verso il server di google per scaricare l'homepage. In request_to_server verrà salvato
# un oggetto contenente tutte le informazioni statistiche della risposta.
request_to_server = requests.get('http://www.google.com')

# Voglio ora ricavare il tempo di risposta, quindi accedo all'oggetto appena creato.
# Utilizzo la funzione elapsed e divido per 1000, in modo tale da salvare il tempo in millisecondi.
print('Il tempo di risposta: ', request_to_server.elapsed.microseconds/1000, 'ms')
