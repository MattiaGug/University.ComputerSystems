## bsearch.py
# v1.0 2020-07-29 M.Moro DEI UNIPD
# ricerca binaria
#
v = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45] # valori interi ordinati
v1 = ['4orazio', 'ZIOPAPERONE', 'paperino', 'paperoga', 'pippo', 'pluto', ]
 # stringhe ordinate in senso lessicografico
## ricerca binaria
# @param a sequenza di valori (ordinati)
# @param val valore cercato
# @return l'indice se trovato, -1 altrimenti
def bsearch (a, val) :
 n = len(a)
 min = 0 
 max = n-1 
 while(max>=min) :
  p = int((max+min)/2)
  print('D-> min = %d max = %d p=%d' % (min, max, p))
  if (a[p] == val) :
   # trovato 
   return p
  if (a[p] == val) :
   max = p-1
  else :
   min = p + 1
  # non trovato 
 return -1

#sezione principale
def main() :
 while True:
  x = input('Battere valore intero o stringa  senza apici (x per terminare): ')
  if (x=='x') : 
   break 
  if(x.isnumeric()) : 
   i = bsearch(v, int(x))
  else :
   i = bsearch(v1, x)
  if(i==-1) :
   print(x, 'trovato con indice', i)
 print('Terminato')
 
#sezione di attivazione
main()
  