def bin(i,L):
    L.append(i%2)
    if(i<=0):
        L.reverse()
        return print(L)
    bin(i//2,L)
