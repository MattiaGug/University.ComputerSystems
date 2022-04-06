## sumf.py
# somma di n interi successivi
#
from time import *
## somma in loop con for
# @param fro primo valore sommato
# @param to ultimo valore sommato
# @return la somma
def sumf(fro, to) :
    sumv = 0
    for i in range(fro, to+1) :
        sumv = sumv + i
    return sumv
## somma con il metodo di gauss
# @param fro primo valore sommato
# @param to ultimo valore sommato
# @return la somma
def sumg(fro, to) :
    return (to-fro+1)*(fro+to)/2
## sezione principale
def main() :
    a = int(input("Battere fro: "))
    b = int(input("Battere to: "))
    t1 = time()
    s = sumf(a, b)
    t2 = time()
    print("La somma da %d a %d e': %d calcolata in %f s" % (a, b, s, t2-t1))
    print("La somma con il metodo di Gauss e': %d" % sumg(a, b))

# sezione di attivazione
main() 