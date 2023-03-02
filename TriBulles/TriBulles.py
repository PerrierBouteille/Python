def tri(T):
    for i in range(len(T)-1,0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp,T[j] = T[j],T[j+1]
                T[j+1] = temp
    return T