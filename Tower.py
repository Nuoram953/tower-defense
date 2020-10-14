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
        self.radius = 250
        self.creepList = creepList
        self.currentDelay = 0
        self.rateOfFire = 5
        self.rateOfFireCounter = 0
        self.readyToFire = True
        self.projectileSpeed = 25
        self.shootDelay = 5
        self.image = PhotoImage(file="assets/towers/peaShooter.png")
        self.checkDist = None

    def tick(self):
        if not self.readyToFire:
            self.rateOfFireCounter += 1
            if self.rateOfFireCounter >= self.rateOfFire:
                self.readyToFire = True

        self.creepList = self.parent.updateCreepList()

        if self.target:
            self.checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)
            if self.checkDist > self.radius:
                self.target = None

        if self.target == None or self.checkDist > self.radius:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)
            if targetPos:
                self.target = random.choice(targetPos)
                bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "green", 10, self.projectileSpeed, self.radius)
                self.projectileList.append(bullet)
                self.readyToFire = False
        else:
            for bullet in self.projectileList:

                if bullet.bulletTarget == None:
                    self.projectileList.remove(bullet)
                    del bullet
                    pass
                elif bullet.bulletX >= bullet.bulletTargetX - 29 and bullet.bulletX <= bullet.bulletTargetX + 29 and bullet.bulletY >= bullet.bulletTargetY - 29 and bullet.bulletY <= bullet.bulletTargetY + 29:

                    if bullet.bulletTarget.health != 0:
                        bullet.bulletTarget.health -= 1

                        if self.checkDist < self.radius and self.readyToFire:
                            nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX,
                                                self.target.posY, 1, "green", 10, self.projectileSpeed, self.radius)
                            self.projectileList.append(nextBullet)
                            self.rateOfFireCounter = 0
                            self.readyToFire = False
                    elif bullet.bulletTarget.health == 0 and self.target != None:
                        self.parent.creepList.remove(self.target)
                        del self.target
                        self.parent.points["Pointage"] += 1
                        self.target = None
                        self.rateOfFireCounter = 0
                        self.readyToFire = False
                    else:
                        pass

                    self.projectileList.remove(bullet)
                    del bullet

    def updateTarget(self, target):

        for creep in self.creepList:
            dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
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
    def __init__(self, parent, posX, posY, creepList):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.image = PhotoImage(file="assets/towers/catapult.png")


    def tick(self):
        print("I C E")

class Bullet():
    def __init__(self, parent, towerX, towerY, target, targetX, targetY, damage, color, size, speed, radius):
        self.parent = parent
        self.bulletTarget = target
        self.bulletX = towerX
        self.bulletY = towerY
        self.bulletTargetX = targetX
        self.bulletTargetY = targetY
        self.damage = damage
        self.color = color
        self.size = size
        self.speed = speed
        self.towerRadius = radius
        self.angle = None
        self.calculateAngle()

    def calculateAngle(self):
        self.angle = helper.Helper.calcAngle(self.bulletX, self.bulletY, self.bulletTargetX, self.bulletTargetY)


    def move(self):

        self.angle = helper.Helper.calcAngle(self.bulletX, self.bulletY, self.bulletTargetX, self.bulletTargetY)

        self.bulletX, self.bulletY = helper.Helper.getAngledPoint(self.angle, self.speed, self.bulletX, self.bulletY)

        dist = helper.Helper.calcDistance(self.bulletX, self.bulletY, self.bulletTargetX, self.bulletTargetY)

        self.bulletTarget = self.parent.updateTarget(self.bulletTarget)

        if self.bulletTarget == None:
            pass
        else:
            self.bulletTargetX = self.bulletTarget.posX
            self.bulletTargetY = self.bulletTarget.posY

        if self.speed > dist and dist <= self.towerRadius:
            return self
        else:
            pass