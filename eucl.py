## mcde.py
# calcolo MCD con Euclide, con differenza e con modulo 
#

##Euclide con differenza 
# @param a primo valore intero
# @param b secondo valore intero
# @return MCD

def mcdd(a, b) : 
    while (a != b) : 
        if (a>b) :
            a -= b
        else : 
            b -=a
    return a;

##Euclide con modulo 
# @param a primo valore intero 
# @param b secondo valore intero
# @return MCD

def mcdm (a, b):
    while(b != 0) : 
        a,b = b, a%b 
    return a;

##Sezione principale
def main() : 
    a = int(input("Battere a:"))
    b = int(input("Battere b: "))
    print("Il MCD di %d e %d e' %d (.diff) %d (modulo)") % (a, b, mcdd(a , b), mcdm(a,b))

#sezione di attivazione

main()
