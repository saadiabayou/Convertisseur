# -*- coding: utf-8 -*-
"""

@author: Saadia Bayou
"""
import numpy as np
import matplotlib.pyplot as plt
import json

class Convertisseur:
    """ classe convertisseur  
    dev1, dev2 , montant1 , montant2 , taux
    paramètres d'entrées 
    caractéristiques d'un convertisseur : dev1, dev2, montant1,taux 
    montant recherché montant2 """
   
    def __init__(self,devise1,devise2,taux):
        """ Constructeur """
        self.dev1=devise1
        self.dev2=devise2
        self.tx=taux
        
        
    def __str__(self):
        """ Affichage """
        s="\nLa devise 1 est : {0} , la devise 2 est : {1}, le taux est : {2}"\
        .format(self.dev1,self.dev2,self.tx)
        return s
    
    
    def __repr__(self):
       pass
   
    
    def calculM2(self,m1):
        """ Calcul le montant 2 converti """
        m2=(self.tx*m1)
        return m2
    
   
   # Graphes 
   
    def trDev2Tx(self,l1,l2):
        """ Trace  l' histogramme 
        devises 2 - taux de change """    
        
        plt.bar(l1, l2,color='r')         
        plt.title("Convertisseur")
        plt.xlabel ("Devises 2 ")
        plt.ylabel("Taux de change")
        plt.savefig("Graphe1-Convertisseur-Taux-Devise")
        fDev2Tx=plt.show()
        return fDev2Tx
    
    def chargeDico (file): 
        """ Charge les données d'un fichier json 
        -> dictionnaire   """
        
        with open(file, "r") as fdic:
            dico= json.load(fdic)
        return dico

    
    def listMat(l1,l2):
        """ retourne une matrice à partir de deux listes """
        M=[l1,l2]
        return M
    
   
    def matFile(namefile,Mat):
        """ Génére un fichier à partir d'un matrice """
        M=np.array(Mat)
        f=np.savetxt(namefile,M)
        return f 
    
    def fileMat(namefile):
        """ Retourne une matrice à partir d'un fichier """
        M = np.loadtxt(namefile)
        return M

    def chargeData(M):
        """Charger des données à partir d'un fichier texte """
        pass

    def trM2Tx(l1,l2):
        """ Graphe montant en fonction de devise 2 """
        plt.plot(l1,l2)
        fM2Tx=plt.show()
        return fM2Tx
        
           
def main():
    
    """ Fonction principale : 
        Instantiation par boucle sur un dictionnaire 
        clé -> devise : valeur -> taux de change """
   
# valeur -> devise
# clé -> taux de change  
# devise2=v
#taux de change=dictConv[v]


    dictConv=Convertisseur.chargeDico("Data0Conv.json")

    lm2=[]

    for v in dictConv :
        conv=Convertisseur("EUR",v,dictConv[v])
        print(conv)
#    m1=float(input("\nEntrez le montant m1 = "))
        m2=round(conv.calculM2(150),4)
        lm2.append(m2)
        print("Le résultat de la converssion est : ",m2,v)

    print("\nlm2 = ",lm2)

    ldev2=[]
    ltx=[]
    
    # changer en def *****
    for v in dictConv :
        ldev2.append(v)
        ltx.append(dictConv[v])
    # *****
        
    conv.trDev2Tx(ldev2,ltx)
    
    print("M_tx_m2 = ",Convertisseur.listMat(ltx,lm2))
    #Convertisseur.trM2Tx(ltx,lm2)
    
    Convertisseur.matFile("convtxm2.txt",[ltx,lm2])
    
    




if __name__=="__main__":
    main()

