import TowerDefense
from tkinter import *

class PeaShooter():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.image = PhotoImage(file="assets/towers/peaShooter.png")

    def Shoot(self):
        print("P E A")

class SunFlower():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.image = PhotoImage(file="assets/towers/sunFlower.png")

    def Shoot(self):
        print("S U N")

class IcePeaShooter():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.image = PhotoImage(file="assets/towers/icePeaShooter.png")

    def Shoot(self):
        print("I C E")