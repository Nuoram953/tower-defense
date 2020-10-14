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
        self.projectileSpeed = 20
        self.image = PhotoImage(file="assets/towers/peaShooter.png")
        self.checkDist = None
        self.time = 5000

    def tick(self):
       
        self.creepList = self.parent.updateCreepList()

        if self.target:
            self.checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)
            if self.checkDist > self.radius:
                self.target = None

        if self.target == None:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)

            if targetPos:
                self.target = random.choice(targetPos)

                bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "lightgreen", 10, self.projectileSpeed, self.radius)
                self.projectileList.append(bullet)         
        else:
            for bullet in self.projectileList:

                if bullet.bulletTarget == None:
                    self.projectileList.remove(bullet)

                elif bullet.bulletX >= bullet.bulletTargetX - 50 and bullet.bulletX <= bullet.bulletTargetX + 50 and bullet.bulletY >= bullet.bulletTargetY - 50 and bullet.bulletY <= bullet.bulletTargetY + 50:

                    if bullet.bulletTarget.health > 0:
                        bullet.bulletTarget.health -= 1
                        if self.checkDist < self.radius:
                            nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "lightgreen", 10, self.projectileSpeed, self.radius)
                            self.projectileList.append(nextBullet)

                    elif bullet.bulletTarget.health == 0 and self.target != None:
                        self.parent.creepList.remove(self.target)
                        self.parent.points["Pointage"] += 1
                        self.target = None
                    else:
                        pass

                if len(self.projectileList) > 1:
                    self.projectileList.remove(bullet)
                

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
        print("sun")

class IcePeaShooter():
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
        self.projectileSpeed = 20
        self.image = PhotoImage(file="assets/towers/icePeaShooter.png")
       
    def tick(self):
       
        self.creepList = self.parent.updateCreepList()

        if self.target:
            self.checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)
            if self.checkDist > self.radius:
                self.target = None

        if self.target == None:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)

            if targetPos:
                self.target = random.choice(targetPos)

                bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "blue", 10, self.projectileSpeed, self.radius)
                self.projectileList.append(bullet)         
        else:
            for bullet in self.projectileList:

                if bullet.bulletTarget == None:
                    self.projectileList.remove(bullet)

                elif bullet.bulletX >= bullet.bulletTargetX - 50 and bullet.bulletX <= bullet.bulletTargetX + 50 and bullet.bulletY >= bullet.bulletTargetY - 50 and bullet.bulletY <= bullet.bulletTargetY + 50:

                    if bullet.bulletTarget.health > 0:
                        bullet.bulletTarget.health -= 1
                        if self.checkDist < self.radius:
                            nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "blue", 10, self.projectileSpeed, self.radius)
                            self.projectileList.append(nextBullet)

                    elif bullet.bulletTarget.health == 0 and self.target != None:
                        self.parent.creepList.remove(self.target)
                        self.parent.points["Pointage"] += 1
                        self.target = None
                    else:
                        pass

                if len(self.projectileList) > 1:
                    self.projectileList.remove(bullet)
                

    def updateTarget(self, target):
        for creep in self.creepList:
            if creep == target:
                return creep

class Catapult():
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
        self.projectileSpeed = 20
        self.image = PhotoImage(file="assets/towers/catapult.png")
       
    def tick(self):
       
        self.creepList = self.parent.updateCreepList()

        if self.target:
            self.checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)
            if self.checkDist > self.radius:
                self.target = None

        if self.target == None:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)

            if targetPos:
                self.target = random.choice(targetPos)

                bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "green", 10, self.projectileSpeed, self.radius)
                self.projectileList.append(bullet)         
        else:
            for bullet in self.projectileList:

                if bullet.bulletTarget == None:
                    self.projectileList.remove(bullet)

                elif bullet.bulletX >= bullet.bulletTargetX - 30 and bullet.bulletX <= bullet.bulletTargetX + 30 and bullet.bulletY >= bullet.bulletTargetY - 30 and bullet.bulletY <= bullet.bulletTargetY + 30:

                    if bullet.bulletTarget.health > 0:
                        bullet.bulletTarget.health -= 1
                        if self.checkDist < self.radius:
                            nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, "green", 10, self.projectileSpeed, self.radius)
                            self.projectileList.append(nextBullet)

                    elif bullet.bulletTarget.health == 0 and self.target != None:
                        if creep not in self.parent.creepList:
                            pass
                        else:
                            self.parent.creepList.remove(self.target)
                        self.parent.points["Pointage"] += 1
                        self.target = None
                    else:
                        pass

                if len(self.projectileList) > 1:
                    self.projectileList.remove(bullet)
                

    def updateTarget(self, target):
        for creep in self.creepList:
            if creep == target:
                return creep

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