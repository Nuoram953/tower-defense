import TowerDefense
from tkinter import *
import random

class Creep1():
    def __init__(self, parent, posX, posY, currentCheckpoint, health, boss):
        self.posX = posX
        self.posY = posY
        self.parent = parent
        self.currentCheckpoint = currentCheckpoint
        self.cibleX = self.currentCheckpoint.x
        self.cibleY = self.currentCheckpoint.y
        self.vitesse = random.randint(4,10)
        self.buffer = 5
        self.boss = boss

        if self.boss:
            self.listImage = ["assets/zombies/boss/boss1.png"]
            self.height = 228
            self.width = 175
            self.vitesse = 7
            self.health = health
        else:
            self.listImage = ["assets/zombies/zombie1.png", "assets/zombies/zombie2.png", "assets/zombies/zombie3.png","assets/zombies/zombie4.png","assets/zombies/zombie5.png","assets/zombies/zombie6.png"]
            self.height = 105
            self.width = 67
            self.health = health
        self.reachedEnd = False
        self.zombie = PhotoImage(file = random.choice(self.listImage))

        self.moveHorizontal = True
        self.moveUp = False
        self.moveDown = False
        self.nextMoveHorizontal = False

        self.hitByTrap = False
        self.hittable = True


    def move(self):
        if self.moveHorizontal:
            if self.posX <= self.cibleX:
                self.posX += self.vitesse
            else:
                self.updateTargetPosition()
        else:
            if self.moveUp:
                if self.posY >= self.cibleY:
                    self.posY -= self.vitesse
                else:
                    self.updateTargetPosition()
            if self.moveDown:
                if self.posY <= self.cibleY:
                    self.posY += self.vitesse
                else:
                    self.updateTargetPosition()

    def wait(self):
        self.posX = self.posX
        self.posY = self.posY

    def updateTargetPosition(self):
        if self.boss:
            height = 60
        else:
            height = 0

        if (self.posX >= 1400 and self.posY >= 635 - height):
            self.reachedEnd = True
        else:
            self.currentCheckpoint = self.parent.getNextCheckpoint(self.currentCheckpoint)
            self.cibleX = self.currentCheckpoint.x
            self.cibleY = self.currentCheckpoint.y - height

            if self.posX >= self.cibleX:
                self.moveHorizontal = False
            
            if self.moveHorizontal == False and self.nextMoveHorizontal == False:
                if self.posY >= self.cibleY:
                    self.moveHorizontal = False
                    self.moveUp = True
                    self.moveDown = False
                    self.nextMoveHorizontal = True
                elif self.posY <= self.cibleY:
                    self.moveHorizontal = False
                    self.moveUp = False
                    self.moveDown = True
                    self.nextMoveHorizontal = True
            elif self.moveUp == False and self.moveDown == True or self.moveUp == True and self.moveDown == False and self.nextMoveHorizontal == True:
                    self.moveHorizontal = True
                    self.moveUp = False
                    self.moveDown = False
                    self.nextMoveHorizontal = False
