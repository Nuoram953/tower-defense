import TowerDefense
from tkinter import *
import helper
import random

class PeaShooter():
    def __init__(self, parent, posX, posY, creepList):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.target = None
        self.projectileList = []
        self.totalAmmo = 10
        self.speed = 20
        self.radius = 150
        self.creepList = creepList
        self.currentDelay = 0
        self.shootDelay = 5
        self.image = PhotoImage(file="assets/towers/peaShooter.png")

    def tick(self):
        self.creepList = self.parent.updateCreepList()

        if self.target:
            checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)

            #if checkDist > self.radius:
                #self.target = None

        if self.target == None or checkDist > self.radius:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)
            if targetPos:
                self.target = random.choice(targetPos)
                bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "green", 10, self.speed)
                self.projectileList.append(bullet)
        else:
            for bullet in self.projectileList:
                if bullet.bulletX >= bullet.targetX - 29 and bullet.bulletX <= bullet.targetX + 29 and bullet.bulletY >= bullet.targetY - 29 and bullet.bulletY <= bullet.targetY + 29:
                    bullet.target.health -= 1

                    if bullet.target.health == 0:
                        self.parent.creepList.remove(self.target)
                        #self.parent.points["Pointage"] += 1
                        self.target = None
                    else:
                        nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1,"green", 10, self.speed)
                        self.projectileList.append(nextBullet)

                    self.projectileList.remove(bullet)
                    del bullet

    def updateTarget(self, target):
        for creep in self.creepList:
            if creep == target:
                return creep

class SunFlower():
    def __init__(self, parent, posX, posY):
        self.parent = parent

        self.posX = posX
        self.posY = posY
        self.image = PhotoImage(file="assets/towers/sunFlower.png")

    def tick(self):
        print("S U N")

class IcePeaShooter():
    def __init__(self, parent, posX, posY, creepList):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.creepList = creepList
        self.image = PhotoImage(file="assets/towers/icePeaShooter.png")
        

    def Shoot(self):
        print("I C E")

class Catapult():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.image = PhotoImage(file="assets/towers/catapult.png")


    def tick(self):
        print("I C E")

class Bullet():
    def __init__(self, parent, towerX, towerY, target, targetX, targetY, damage, color, size, speed):
        self.parent = parent
        self.target = target
        self.bulletX = towerX
        self.bulletY = towerY
        self.targetX = targetX
        self.targetY = targetY
        self.damage = damage
        self.color = color
        self.size = size
        self.speed = speed
        self.angle = None
        self.calculateAngle()

    def calculateAngle(self):
        self.angle = helper.Helper.calcAngle(self.bulletX, self.bulletY, self.targetX, self.targetY)


    def move(self):

        self.target = self.parent.updateTarget(self.target)
        self.targetX = self.target.posX
        self.targetY = self.target.posY

        self.angle = helper.Helper.calcAngle(self.bulletX, self.bulletY, self.targetX, self.targetY)

        self.bulletX, self.bulletY = helper.Helper.getAngledPoint(self.angle, self.speed, self.bulletX, self.bulletY)

        dist = helper.Helper.calcDistance(self.bulletX, self.bulletY, self.targetX, self.targetY)

        if self.speed > dist:
            return self
        return None




