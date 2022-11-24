from csv import *
from pylab import show, scatter, legend, xlabel, ylabel, draw

file=open('iris.csv')
donnees=reader(file,delimiter=',')
donnees=list(donnees)
file.close()


X=[]
Y=[]

for i in range(1,len(donnees)):
    X.append(float(donnees[i][0]))
    Y.append(float(donnees[i][1]))

scatter(X,Y)

show()