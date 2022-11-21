def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L = [0]*(n1+n2)
    i1,i2,i=0,0,0
    while i1<n1 and i2<n2:
        print("Logs : ",i1,"/",i2,"/",i)
        print("Logs : ",L)
        if L1[i1] < L2[i2]:
            L[i] = L1[i1]
            i1 += 1
        else:
            L[i] = L2[i2]
            i2 += 1
        i += 1
    while i1<n1:
        print("Logs : ",i1,"/",i2,"/",i)
        print("Logs : ",L)
        L[i] = L1[i1]
        i1 += 1
        i += 1
    while i2<n2:
        print("Logs : ",i1,"/",i2,"/",i)
        print("Logs : ",L)
        L[i] = L2[i2]
        i2 += 1
        i += 1
    return L

def mtg(L):
    x = []
    print("Logs : mtg 1")
    for i in range(len(L)//2):
        print("Logs : mtg ",i+1)
        x.append(L[i+len(L)//2])
        print("Logs : ", x)
    return x

def mtd(L):
    x = []
    print("Logs : mtd 1")
    for i in range(len(L)//2):
        print("Logs : mtg ",i+1)
        x.append(L[i])
        print("Logs : ", x)
    return x

def tri_fusion(L):
    n = len(L)
    if(n<=1):
        return L
    print(L)
    mg = mtg(L)
    print("Logs : mtg done")
    md = mtd(L)
    print("Logs : mtd done")
    L1 = tri_fusion(mg)
    print("Logs : fusion mtd done")
    L2 = tri_fusion(md)
    print("Logs : fusion mtg done")
    return fusion(L1,L2)

