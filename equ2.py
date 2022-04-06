## equaz.py
# risoluzione di una equazione di secondo grado
#
from math import * 
## calcolo del determinante
# @param a coefficiente 2^ grado
# @param b coefficiente 1^ grado
# @param c termine noto
# @return delta dell'equazione
def delta(a, b, c) :
 return b**2-4*a*c

 
## check se ammette soluzioni reali
# @param a coefficiente 2^ grado
# @param b coefficiente 1^ grado
# @param c termine noto
# @return True se ammette soluzioni reali
def sesol(a, b, c) :
 return delta(a,b,c) >= 0
## sezione principale
def main() :
    a = float(input("Battere coefficiente di 2^ grado:"))
    b = float(input("Battere coefficiente di 1^ grado:"))
    c = float(input("Battere termine noto:"))

 # casi degeneri
    if (a==0.0) :
        if (b==0.0) :
            if (c==0.0) :
                print("Caso degenere: ci sono infinite soluzioni")
            else :
                print("Caso degenere: non ci sono soluzioni")
        else :
            # equazione di primo grado
            print("Caso degenere: soluzione unica %f" % (-c/b))
    else :
        # caso normale
        if (sesol(a,b,c)) :
            # ci sono soluzioni
            d = sqrt(delta(a,b,c))
            if (d==0) :
                print("Due soluzioni coincidenti %f" % (-b/(2*a)))
            else :
                print("Due soluzioni %f %f" % ((-b+d)/(2*a), (-b-d)/(2*a)))
        else :
            print("Non ci sono soluzioni reali")


# sezione di attivazione
main()

        
