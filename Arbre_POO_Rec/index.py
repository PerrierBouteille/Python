class noeud:
    def __init__(self,fg,v,fd):
        self.fg=fg
        self.key=v
        self.fd=fd

    def racine(self):
        return self.key
    
    def feuille(self):
        if(self.fg == None and self.fd == None):
            return True
        else:
            return False

    def hauteur(self):
        if self.feuille() == True:
            return 1
        elif self.fd == None:
            return self.fg.hauteur()+1
        elif self.fg == None:
            return self.fd.hauteur()+1
        else:
            return max(self.fg.hauteur(),self.fd.hauteur())+1

N8=noeud(None,8,None)
N9=noeud(None,9,None)
N10=noeud(None,10,None)
N6=noeud(None,6,None)
N7=noeud(None,7,None)

sa_tmp=noeud(N8,4,N9)
sa_tmp2=noeud(N10,5,None)

sa_tmp=noeud(sa_tmp,2,sa_tmp2)
sa_tmp2=noeud(N6,3,N7)

Arbre=noeud(sa_tmp,1,sa_tmp2)
