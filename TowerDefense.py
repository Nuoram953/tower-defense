##TowerDefense

# Francois Therien
# Nicolas Paquette
# Caroline Cass Emond
# Antoine Auger

#TEST

from tkinter import *
import random 

class Vue():  
    def __init__(self, modele, parent):
        self.modele = modele
        self.parent = parent


class Modele():  
    def __init__(self, parent):
        self.parent = parent


class Controleur():  
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self,self.modele)

if __name__ == '__main__':
    c = Controleur()        
