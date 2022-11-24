from csv import *
from pylab import show, scatter, legend, xlabel, ylabel, draw
from random import uniform
from math import sqrt

file=open('iris.csv')
donnees=reader(file,delimiter=',')
donnees=list(donnees)
file.close()


X0=[]
Y0=[]
X1=[]
Y1=[]
X2=[]
Y2=[]

for i in range(1,len(donnees)):
    if float(donnees[i][2])==0 :
        X0.append(float(donnees[i][0]))
        Y0.append(float(donnees[i][1]))
    elif float(donnees[i][2])==1 :
        X1.append(float(donnees[i][0]))
        Y1.append(float(donnees[i][1]))
    else:
        X2.append(float(donnees[i][0]))
        Y2.append(float(donnees[i][1]))

scatter(X0,Y0,color="green")
scatter(X1,Y1,color="red")
scatter(X2,Y2,color="blue")
x,y=uniform(1,7),uniform(0,2.5)
scatter(x,y,color="orange")

def distance(A,B):
    d = sqrt(((B[0]-A[0])**2)+(B[1]-A[1])**2)
    return d

Dist = []
r = 0
g = 0
b = 0

for i in range(1,len(donnees)):
    print(donnees[i][0])
    d = distance((x,y),((float(donnees[i][0]), float(donnees[i][1])) ) )
    Dist.append([d, float(donnees[i][2])])


Dist.sort(key=lambda Dist: Dist[0])
print(Dist)

for q in range(10):
    print("DIST: " + str(Dist[q][0]) + " | " + str(Dist[q][1]))
    if(Dist[q][1] == 0):
        g+=1
    elif(Dist[q][1] == 1):
        r+=1
    else:
        b+=1
print("L'iris unknow est à:")
if(g != 0):
    print("Vert: " + str(g*100/10) + "%")
if(r != 0):
    print("Rouge: " + str(r*100/10) + "%")
if(b != 0):
    print("Bleu: " + str(b*100/10) + "%")

xlabel('abscisses')
ylabel('ordonnées')
show()