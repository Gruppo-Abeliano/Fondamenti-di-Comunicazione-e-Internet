# Librerie:
import os

#########################################à####### Funzioni ######################################################
#   - inizializzaCalcolatrice():                                                                                #
#       Inizializza lo schermo della calcolatrice, offrendo un'interfaccia utente intuitiva                     #
#   - inserisciNumero():                                                                                        #
#       Permette all'utente di inserire un valore numerico                                                      #
#   - pauseProgram():                                                                                           #
#       Mette in pausa il programma finchè l'utente non preme un tasto                                          #
#   - somma(numero1,numero2):                                                                                   #
#       Passando in input due numeri, la funzione ne restituisce la somma                                       #
#   - differenza(numero1,numero2):                                                                              #
#       Passando in input due numeri, la funzione ne restituisce la differenza                                  #
#   - prodotto(numero1,numero2):                                                                                #
#       Passando in input due numeri, la funzione ne restituisce il prodotto                                    #
#   - quoziente(numero1,numero2):                                                                               #
#       Passando in input due numeri, la funzione ne restituisce il quoziente                                   #
#################################################################################################################

def inizializzaCalcolatrice():
    os.system('cls||clear')
    print("#########################################à####### CALCOLATRICE ######################################################")
    print("# Benvenuto nella calcolatrice. Scegli l'operazione tra le seguenti da effettuare (inserisci il numero) :           #")
    print("#    - 1 : Somma                                                                                                    #")
    print("#    - 2 : Differenza                                                                                               #")
    print("#    - 3 : Prodotto                                                                                                 #")
    print("#    - 4 : Quoziente                                                                                                #")
    print("#                                                                                                                   #")
    print("#    - 5 : Spegni la calcolatrice                                                                                   #")
    print("#####################################################################################################################")

def inserisciNumero():
    try:
        return float(input("Inserisci un numero: "))
    except ValueError:
        return "ERRORE"

def pauseProgram():
    pauseHandler = input("\nPremi <INVIO> per continuare...")

def somma(numero1,numero2):
    return numero1+numero2

def differenza(numero1,numero2):
    return numero1-numero2

def prodotto(numero1,numero2):
    return numero1*numero2

def quoziente(numeratore,denominatore):
    try:
        return numeratore/denominatore
    except ZeroDivisionError:
        print("\nDivisione per zero.")
        return "IMPOSSIBILE"


################################################# Main ##########################################################

while(True):
    inizializzaCalcolatrice()
    try:
        operazioneScelta = int(input("Scelta: "))
    except ValueError:
        continue

    if(operazioneScelta <= 0 or operazioneScelta >=5):
        if(operazioneScelta == 5):
            break
        else:
            print("\nNumero non valido.")
            continue

    primoOperando = inserisciNumero()
    secondoOperando = inserisciNumero()

    if(primoOperando == "ERRORE" or secondoOperando == "ERRORE"):
        print("Inserire solamente caratteri numerici!")
        pauseProgram()
        continue

    if(operazioneScelta == 1):
        print(str(primoOperando)," + ",str(secondoOperando)," = ",str(somma(primoOperando,secondoOperando)))
    elif(operazioneScelta == 2):
        print(str(primoOperando)," - ",str(secondoOperando)," = ",str(differenza(primoOperando,secondoOperando)))
    elif(operazioneScelta == 3):
        print(str(primoOperando)," * ",str(secondoOperando)," = ",str(prodotto(primoOperando,secondoOperando)))
    elif(operazioneScelta == 4):
        print(str(primoOperando)," / ",str(secondoOperando)," = ",str(quoziente(primoOperando,secondoOperando)))

    pauseProgram()

print("Terminazione applicazione.")
