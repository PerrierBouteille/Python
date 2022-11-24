
ToH = [[],[],[]]

def Creation(n):
    for i in range(n):
        ToH[0].append(n-i)
        ToH[1].append('•')
        ToH[2].append('•')
    print('\t' + str(ToH[0]) + '\t' + str(ToH[1]) + '\t' + str(ToH[2]))

def Affichage(n):
    for i in range(n):
        towerI,towerII,towerIII='.','.','.'
        if n-1-i<len(ToH[0]):
            towerI=str(ToH[0][n-1-i])
        if n-1-i<len(ToH[1]):
            towerII=str(ToH[1][n-i-1])
        if n-1-i<len(ToH[2]):
            towerIII=str(ToH[2][n-i-1])
        print(towerI,towerII,towerIII)
        return towerI,towerII,towerIII
    print('--------------------------------')
