n=1

def startfacto():
    i = int(input("Factoriel de: "))
    if(i<=0): print('Erreur nombre inférieur à 0')
    else:
        def facto(N):
            if(N>0):
                global n
                n*=N
                facto(N-1)
            else:
                print('Résultat: ', n)
                n=1
        facto(i)


def startfibo():
    i=int(input('Choose ur number: '))
    if(i==0 or i==1): print('Résultat: ', i)
    else:
        def fibo(N):
            if(N>0):
                global n
                n = n+(n+1)
                fibo(N-1)
            else:
                print('Résultat: ',n)
                n=1
        fibo(i)



