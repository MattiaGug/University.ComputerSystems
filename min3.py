# Consegna 2 - Mi3 Lezione 5 

## determina il minore di tre numeri
# @param x primo numero
# @param y secondo numero
# @param z terzo numero
# @return il minore dei tre
def min3(x, y, z) :
 min = x
 if (y < min) :
    min = y
 if (z < min) :
    min = z
 return min
# sezione principale
def main() :
 a = 3
 b = 4
 c = 5
 print('Il minimo tra', a, b, c, "e'", min3(a,b,c))
 a, b, c = b, c, a
 print('Il minimo tra', a, b, c, "e'", min3(a,b,c))
 a, b, c = b, c, a
 print('Il minimo tra', a, b, c, "e'", min3(a,b,c))

# sezione di attivazione
main() 