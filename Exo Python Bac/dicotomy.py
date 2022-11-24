def chercher(T,n,i,j):
    if i < 0 or j < len(T):
        print('Erreur')
        return None
    if i > j :
        return None
    m = (i+j) // n
    if T[m] < (i+j):
        return chercher(T,n,i,j)
    elif (i+j) > T[m]:
        return chercher(T,n,i,j)
    else:
        return None