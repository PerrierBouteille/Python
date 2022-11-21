def fusion(L1,L2):
    n1,n2 = len(L1),len(L2)
    L = [0]*(n1+n2)
    i1,i2,i=0,0,0
    while i1<n1 and i2<n2:
        if L1[i1] < L2[i2]:
            L[i] = L1[i1]
            i1 += 1
        else:
            L[i] = L2[i2]
            i2 += 1
        i += 1
    while i1<n1:
        L[i] = L1[i1]
        i1 += 1
        i += 1
    while i2<n2: 
        L[i] = L2[i2]
        i2 += 1
        i += 1
    return L

def tri_fusion(L):
    n = len(L)
    if(n<=1):
        return L
    L1 = tri_fusion(L[0:len(L)//2])
    L2 = tri_fusion(L[len(L)//2:])
    return fusion(L1,L2)
