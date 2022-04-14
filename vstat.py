## vstat.py
# calcolo media e varianza
#
from math import sqrt
# valori interi tra -5 e 5
v = [2, 3, -4, 0, -1, 2, 1, 2, -2, 5, 2, 5, 0, -5, 1, 4]
v1 = [-5, 5, -5, 5, -5, 5, 5, -5]
## media e varianza
# @param v lista di valori
def medvar(v) :
    n = len(v)
    somma = 0.0
    scarto = 0.0
    for val in v :
        somma += float(val) # somma in ambito f.p.
    # al posto di questo ciclo ciclo si poteva usare la funzione sum(lista) 
    # somma = float(sum(v))
        media = somma/float(n)
        for val in v :
            scarto += (float(val)-media)**2
        print('Numero di elementi n =', len(v))
        print("La media e'", media)
        print("La deviazione standard e'", sqrt(scarto/float(n)))
## sezione principale
def main() :
    medvar(v)
    medvar(v1)
    medvar([1, 2, -3.4, 6, -7.5, 3]) # qui funziona anche con valori fuori specifiche
    medvar('1234') # anche qui in qualche modo funziona
    # perche' i singoli caratteri sono cifre numeriche
    medvar('123a45') # qui da' errore
# sezione di attivazione  
main()