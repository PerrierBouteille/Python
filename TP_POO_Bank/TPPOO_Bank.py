from time import *

class CompteBancaire:
    def __init__(self, compte,money=0):
        self.compte = compte
        self.money = money

    def depot(self,add):
        self.money += add

    def retrait(self,rem):
        self.money -= rem

    def __str__(self):
        s = "\nCompte: " + self.compte
        s += "\nMoney: " + str(self.money)
        s += "\n"
        return s

    def affiche(self):
        return print(str(self))

class Comptes(object):
    def __init__(self):
        self._liste=[]

    def _get_liste(self):
        return self._liste

    def _set_liste(self,liste):
        self._liste=liste

    liste=property(_get_liste,_set_liste)

    def addCompte(self,c):
        self._liste.append(c)

    def Affiche(self):
        s="Liste des comptes: "
        for compte in self.liste :
            compte.affiche()

    def sc(self,p):
        self._liste.remove(p)

z = CompteBancaire("test",100)

l=Comptes()
l.addCompte(z)
l.Affiche()

while True:
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    s = ("Veuillez séléctionner votre choix:\n")
    s += ("\n  1. Ajouter un compte")
    s += ("\n  2. Faire un retrait")
    s += ("\n  3. Faire un dépot")
    s += ("\n  4. Liste des comptes")
    s += ("\n  5. Sortir de la banque")
    print(s)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    x = int(input("Veuillez entrer votre choix: "))
    if(x==1):
        l.addCompte(CompteBancaire(str(input("Nom du compte: ")),int(input("Solde du compte: "))))
    if(x==2):
        cm = str(input("Compte: "))
        r = int(input("Retrait: $"))
        L = Comptes._get_liste(l)
        for i in range(len(L)):
            if(L[i].compte==cm):
                L[i].retrait(r)
        L[i].affiche()
        sleep(1.5)
        print("\n\n\n\n\n\n")
    if(x==3):
        cm = str(input("Compte: "))
        r = int(input("Depot: $"))
        L = Comptes._get_liste(l)
        for i in range(len(L)):
            print(L[i])
            if(L[i].compte==cm):
                L[i].depot(r)
        L[i].affiche()
        sleep(1.5)
        print("\n\n\n\n\n\n")

    if(x==4):
        l.Affiche()
        sleep(1.5)
        print("\n\n\n\n\n\n")
    if(x==5):
        break