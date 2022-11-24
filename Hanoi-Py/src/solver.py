def Solv(n , source, destination, pilieraux):
    if n==1:
        print ("Déplacé le palier 1 du pilier ",source," vers le pilier ",destination)
        return
    Solv(n-1, source, pilieraux, destination)
    print ("Déplacé le palier ",n," du pilier ",source,"to vers le pilier",destination)
    Solv(n-1, pilieraux, destination, source)

def RunSolver(n):
    Solv(n,'A','B','C')