## search.py
# ricerca lineare
#


v = [3, -7, 0, 24, 2, -9, 13] # valori interi
v1 = [ 'pippo', 'pluto', 'paperino', 'paperoga'] # una lista di stringhe
v2 = 'UnaLungaListaDiStringheanchedinumeri1234Fine' # una stringa

## ricerca lineare
# @param a sequenza di valori 
# @param val valore cercato 
# @return l'indice se trovato , -1 altrimenti 
def  search(a, val) :
    n = len(a)
    for i in range(n) :
        if (a[i] == val) : 
            #trovato 
            return i 
    #non trovato 
    return -1

## sezione principale 
def main() :
    while True  : # WHILE TRUE Significa esegui ciclo con una condizione che e' sempre vera
        x = input("Battere valore intero o stringa senza apici (x per terminare): ")
        if(x=='x') :
            break # Uscita ciclo
        if(x.isnumeric()) :
            i = search(v, int(x))
        elif(len(x)==1) :
            i = search(v2, x)
        else : 
            i = search(v1, x)
        if(i==-1):
            print(x, 'NON TROVATO')
        else :
            print(x, 'trovato con codice', i)
    print('Terminato')
#sezione di attivazione

main()

    
    