##coll.py 
# esempio collezioni (tupla e lista)
#

t = (3, 6, -1, 0, -4, 8) #tupla
l = [3, 7, 0, -4, 5, -7, 11] #lista

##sezione principale
def main():
    print('t len =', len(t), 'contiene', t)
    print('l len =', len(l), 'contiene', l)
    if(6 in t) : 
        l[t.index(6)] = 14
        print('(2) l len = ', len(l), 'contiene', l)
        l.append(20)
        l.insert(0, -20)
        print('(3) l len=', len(l), 'contiene', l)
        for i in range(len(l)) :
            print('l[%d]=%d' %(i, l[i]), end=" ")
            print("\nGli elementi nell'ordine:")
        for i in l :
            print(i, end=' ')
    print()

# sezione di attivazione
main() 