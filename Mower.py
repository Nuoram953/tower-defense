from tkinter import *

class Mower():
    def __init__(self,parent,x,y,speed):
        self.parent = parent
        self.posX = x
        self.posY = y
        self.width = 130
        self.height = 80
        self.targetX = -self.width
        self.speed = speed
        self.damage = 40

        self.image = PhotoImage(file="assets/traps/mower.png")

    def move(self):

        if self.posX >= self.targetX:
            self.posX -= self.speed

    def outOfFrame(self):
        if self.posX < self.targetX:
            return True
        else:
            return False