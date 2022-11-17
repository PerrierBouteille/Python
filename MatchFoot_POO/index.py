class Joueur(object):
    def __init__(self,nom="",poste="",equipe=1,note=1):
        self._nom = nom
        self._poste = poste
        self._equipe = equipe
        self._note = note
    def getnom(self):
        return self._nom
    def setnom(self, nom):
        self._nom = nom
    def getposte(self):
        return self._poste
    def setposte(self, poste):
        self._poste = poste
    def getequipe(self):
        return self._equipe
    def setequipe(self, equipe):
        self._equipe = equipe
    def getnote(self):
        return self._note
    def setnote(self, note):
        self._note = note
    def __str__(self):
        s = "\nNom: " + self._nom
        s+= "\nPoste: " + self._poste
        s+= "\nÉquipe: " + str(self._equipe)
        s+= "\nNote: " + str(self._note)
        return s
    def affiche(self):
        print(str(self))
    nom=property(getnom, setnom)
def affiche_equipe(liste,equipe):
    eqp1,eqp2 = [],[]
    for i in range(len(liste)):
        if(liste[i].getequipe() == 1):
            eqp1.append(liste[i])
        else:
            eqp2.append(liste[i])
    if(equipe == 1):
        print('--===[Equipe 1]===--')
        for j in range(len(eqp1)):
            eqp1[j].affiche()
    else:
        print("\n--===[Equipe 2]===--")
        for o in range(len(eqp2)):
            eqp2[o].affiche()


def match(liste):
    eqp1,eqp2=[],[]
    ge1,ge2=0,0
    numg1,numg2=0,0
    for i in range(len(liste)):
        if(liste[i].getequipe() == 1):
            eqp1.append(liste[i])
        else:
            eqp2.append(liste[i])
    print('But equipe 1:\n')
    for j in range(len(eqp1)):
        if(eqp1[j].getposte() == "Attaquant" or "Defense"):
            for h in range(len(eqp2)):
                if(eqp2[h].getposte() == "Gardien"):
                    if(eqp1[j].getnote() > eqp2[h].getnote()):
                        print(eqp1[j].getnom() + " a marqué un but contre " + eqp2[h].getnom())
                    else:
                        print(eqp2[h].getnom() + " a arrêter le tire de " + eqp1[j].getnom())
    print('\n\nBut equipe 2: \n')
    for o in range(len(eqp2)):
        if(eqp2[j].getposte() == "Attaquant" or "Defense"):
            for k in range(len(eqp2)):
                if(eqp1[k].getposte() == "Gardien"):
                    if(eqp2[o].getnote() > eqp1[k].getnote()):
                        print(eqp2[o].getnom() + " a marqué un but contre " + eqp1[k].getnom())
                    else:
                        print(eqp1[k].getnom() + " a arrêter le tire de " + eqp2[o].getnom())

j1=Joueur("Joueur 1","Attaquant",1,9)
j2=Joueur("Joueur 2","Attaquant",1,6)
j3=Joueur("Joueur 3","Defense",1,3)
j4=Joueur("Joueur 4","Gardien",1,4)

j5=Joueur("Joueur 5","Defense",2,7)
j6=Joueur("Joueur 6","Attaquant",2,6)
j7=Joueur("Joueur 7","Gardien",2,2)
j8=Joueur("Joueur 8","Attaquant",2,4)

liste=[j1,j2,j3,j4,j5,j6,j7,j8]
