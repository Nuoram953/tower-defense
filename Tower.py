import TowerDefense
from tkinter import *
import helper
import random

class PeaShooter():
    def __init__(self, parent, posX, posY, damage, creepList):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.target = None
        self.projectileList = []
        self.speed = 20
        self.radius = 250
        self.damage = damage
        self.creepList = creepList
        self.projectileSpeed = 20
        self.image = PhotoImage(file="assets/towers/peaShooter.png")
        self.checkDist = None
        self.readyToFire = False
        self.rateOfFire = 10
        self.rateOfFireCounter = self.rateOfFire
        self.bulletSize = 10
        self.bulletColor = "lightgreen"
        self.upgraded = False
        self.upgradeCost = 20 * self.parent.currentMap

    def tick(self):
        self.rateOfFireCounter += 1
        if self.rateOfFireCounter >= self.rateOfFire:
            self.readyToFire = True
        else:
            self.readyToFire = False

        self.creepList = self.parent.updateCreepList()
        if self.target != None:
            if self.target not in self.creepList:
                self.target = None

        if self.target != None:
            self.checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)
            if self.checkDist > self.radius:
                self.target = None
            else:
                pass

        if self.target == None:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)

            if targetPos:
                self.target = random.choice(targetPos)

                if self.readyToFire:
                    self.readyToFire = False
                    self.rateOfFireCounter = 0
                    bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, self.bulletColor, self.bulletSize, self.projectileSpeed, self.radius)
                    self.projectileList.append(bullet)  

            if len(targetPos) == 0:
                self.projectileList = []       
        else:
            if self.checkDist < self.radius:
                if self.readyToFire:
                    self.readyToFire = False
                    self.rateOfFireCounter = 0
                    nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, self.bulletColor, self.bulletSize, self.projectileSpeed, self.radius)
                    self.projectileList.append(nextBullet)

            for bullet in self.projectileList:

                if bullet.bulletTarget == None:
                    self.projectileList.remove(bullet)

                elif bullet.bulletX >= bullet.bulletTargetX - 30 and bullet.bulletX <= bullet.bulletTargetX + 30 and bullet.bulletY >= bullet.bulletTargetY - 30 and bullet.bulletY <= bullet.bulletTargetY + 30:
                    bullet.hit = True

                    if bullet.bulletTarget.health > self.damage:
                        bullet.bulletTarget.health -= self.damage

                    elif bullet.bulletTarget.health <= self.damage and self.target != None:
                        if self.target not in self.parent.creepList:
                            self.target = None
                        else:
                            for autreBullet in self.projectileList:
                                if autreBullet != bullet:
                                    if autreBullet.bulletTarget == bullet.bulletTarget:
                                        self.projectileList.remove(autreBullet)

                            self.parent.creepList.remove(self.target)
                            self.parent.points["Pointage"] += 1
                            self.parent.points["Engrais"] += 5
                            self.target = None

                    else:
                        self.target = None

                if bullet.hit or bullet.bulletTarget == None or self.target == None:
                    self.projectileList.remove(bullet)
                

    def updateTarget(self):
        if self.target != None:
            return self.target.posX, self.target.posY
        else:
            pass

class SunFlower():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.projectileList = []
        self.upgraded = False
        self.posX = posX
        self.posY = posY
        self.image = PhotoImage(file="assets/towers/sunFlower.png")
        self.upgradeCost = 15 * self.parent.currentMap

    def tick(self):
        pass

class IcePeaShooter():
    def __init__(self, parent, posX, posY, damage, creepList):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.target = None
        self.projectileList = []
        self.speed = 20
        self.radius = 250
        self.damage = damage
        self.creepList = creepList
        self.projectileSpeed = 15
        self.slow = 2
        self.image = PhotoImage(file="assets/towers/icePeaShooter.png")
        self.readyToFire = False
        self.rateOfFire = 20
        self.rateOfFireCounter = self.rateOfFire
        self.bulletSize = 10
        self.bulletColor = "lightblue"
        self.upgraded = False
        self.upgradeCost = 25 * self.parent.currentMap
       
    def tick(self):

        self.rateOfFireCounter += 1
        if self.rateOfFireCounter >= self.rateOfFire:
            self.readyToFire = True
        else:
            self.readyToFire = False

        self.creepList = self.parent.updateCreepList()

        if self.target != None:
            if self.target not in self.creepList:
                self.target = None

        if self.target != None:
            self.checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)
            if self.checkDist > self.radius:
                self.target = None
            else:
                pass

        if self.target == None:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)

            if targetPos:
                self.target = random.choice(targetPos)

                if self.readyToFire:
                    self.readyToFire = False
                    self.rateOfFireCounter = 0
                    bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, self.bulletColor, self.bulletSize, self.projectileSpeed, self.radius)
                    self.projectileList.append(bullet) 

            if len(targetPos) == 0:
                self.projectileList = []           
        else:

            if self.checkDist < self.radius:
                if self.readyToFire:
                    self.readyToFire = False
                    self.rateOfFireCounter = 0
                    nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, self.bulletColor, self.bulletSize, self.projectileSpeed, self.radius)
                    self.projectileList.append(nextBullet)

            for bullet in self.projectileList:

                if bullet.bulletTarget == None:
                    self.projectileList.remove(bullet)

                elif bullet.bulletX >= bullet.bulletTargetX - 30 and bullet.bulletX <= bullet.bulletTargetX + 30 and bullet.bulletY >= bullet.bulletTargetY - 30 and bullet.bulletY <= bullet.bulletTargetY + 30:
                    bullet.hit = True

                    if bullet.bulletTarget.health > self.damage:
                        bullet.bulletTarget.health -= self.damage

                        if bullet.bulletTarget.vitesse > 2:
                            bullet.bulletTarget.vitesse -= self.slow

                    elif bullet.bulletTarget.health <= self.damage and self.target != None:
                        if self.target not in self.parent.creepList:
                            self.target = None
                        else:
                            for autreBullet in self.projectileList:
                                if autreBullet != bullet:
                                    if autreBullet.bulletTarget == self.target:
                                        self.projectileList.remove(autreBullet)

                            self.parent.creepList.remove(self.target)
                            self.parent.points["Pointage"] += 1
                            self.parent.points["Engrais"] += 5
                            self.target = None

                    else:
                        self.target = None

                if bullet.hit or bullet.bulletTarget == None or self.target == None:
                    self.projectileList.remove(bullet)
                

    def updateTarget(self):
        if self.target != None:
            return self.target.posX, self.target.posY
        else:
            pass

class Catapult():
    def __init__(self, parent, posX, posY, damage, creepList):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.target = None
        self.projectileList = []
        self.speed = 20
        self.radius = 400
        self.damage = damage
        self.damageRadius = 75
        self.epicenter = self.damageRadius / 2
        self.creepList = creepList
        self.projectileSpeed = 15
        self.image = PhotoImage(file="assets/towers/catapult.png")
        self.readyToFire = False
        self.rateOfFire = 40
        self.rateOfFireCounter = self.rateOfFire
        self.bulletSize = 15
        self.bulletColor = "green3"
        self.impact = False
        self.impactX = None
        self.impactY = None
        self.count = 0
        self.upgraded = False
        self.upgradeCost = 30 * self.parent.currentMap
       
    def tick(self):

        if self.impact:
            self.count +=1

        self.rateOfFireCounter += 1
        if self.rateOfFireCounter >= self.rateOfFire:
            self.readyToFire = True
        else:
            self.readyToFire = False

        self.creepList = self.parent.updateCreepList()
        if self.target != None:
            if self.target not in self.creepList:
                self.target = None

        if self.target != None:
            self.checkDist = helper.Helper.calcDistance(self.posX, self.posY, self.target.posX, self.target.posY)
            if self.checkDist > self.radius:
                self.target = None
            else:
                pass

        if self.target == None:
            targetPos = []
            for creep in self.creepList:
                dist = helper.Helper.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
                if dist < self.radius:
                    targetPos.append(creep)

            if targetPos:
                self.target = random.choice(targetPos)

                if self.readyToFire:
                    self.readyToFire = False
                    self.rateOfFireCounter = 0
                    bullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, self.bulletColor, self.bulletSize, self.projectileSpeed, self.radius)
                    self.projectileList.append(bullet)

            if len(targetPos) == 0:
                self.projectileList = []            
        else:

            if self.checkDist < self.radius:
                if self.readyToFire:
                    self.readyToFire = False
                    self.rateOfFireCounter = 0
                    nextBullet = Bullet(self, self.posX, self.posY, self.target, self.target.posX, self.target.posY, 1, self.bulletColor, self.bulletSize, self.projectileSpeed, self.radius)
                    self.projectileList.append(nextBullet)

            for bullet in self.projectileList:

                if bullet.bulletTarget == None:
                    self.projectileList.remove(bullet)

                elif bullet.bulletX >= bullet.bulletTargetX - 30 and bullet.bulletX <= bullet.bulletTargetX + 30 and bullet.bulletY >= bullet.bulletTargetY - 30 and bullet.bulletY <= bullet.bulletTargetY + 30:
                    bullet.hit = True
                    self.impact = True
                    self.impactX = bullet.bulletTargetX
                    self.impactY= bullet.bulletTargetY

                    if bullet.bulletTarget.health > self.damage:
                        bullet.bulletTarget.health -= self.damage


                        for creep in self.creepList:
                            if creep.posX >= bullet.bulletTargetX - self.damageRadius and creep.posX <= bullet.bulletTargetX + self.damageRadius and creep.posY >= bullet.bulletTargetY - self.damageRadius and creep.posY <= bullet.bulletTargetY + self.damageRadius:

                                if creep.posX >= bullet.bulletTargetX - self.epicenter and creep.posX <= bullet.bulletTargetX + self.epicenter and creep.posY >= bullet.bulletTargetY - self.epicenter and creep.posY <= bullet.bulletTargetY + self.epicenter:
                                    creep.health -= (self.damage * 2)
                                else:
                                    creep.health -= self.damage

                                if creep.health <= 0:
                                    self.parent.creepList.remove(creep)


                    elif bullet.bulletTarget.health <= self.damage and self.target != None:
                        if self.target not in self.parent.creepList:
                            self.target = None
                        else:
                            for autreBullet in self.projectileList:
                                if autreBullet != bullet:
                                    if autreBullet.bulletTarget == self.target:
                                        self.projectileList.remove(autreBullet)

                            self.parent.creepList.remove(self.target)
                            self.parent.points["Pointage"] += 1
                            self.parent.points["Engrais"] += 1

                            for creep in self.creepList:
                                if creep != self.target:
                                    if creep.posX >= bullet.bulletTargetX - self.damageRadius and creep.posX <= bullet.bulletTargetX + self.damageRadius and creep.posY >= bullet.bulletTargetY - self.damageRadius and creep.posY <= bullet.bulletTargetY + self.damageRadius:

                                        if creep.posX >= bullet.bulletTargetX - self.epicenter and creep.posX <= bullet.bulletTargetX + self.epicenter and creep.posY >= bullet.bulletTargetY - self.epicenter and creep.posY <= bullet.bulletTargetY + self.epicenter:
                                            creep.health -= (self.damage * 2)
                                        else:
                                            creep.health -= self.damage

                                    if creep.health <= 0:
                                        self.parent.creepList.remove(creep)
                            self.target = None
                    else:
                        self.target = None

                if bullet.hit or bullet.bulletTarget == None or self.target == None:
                    self.projectileList.remove(bullet)

        if self.count >=5:
            self.impact = False
            self.count = 0

    def updateTarget(self):
        if self.target != None:
            return self.target.posX, self.target.posY
        else:
            pass

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
        self.hit = False

    def calculateAngle(self):
        self.angle = helper.Helper.calcAngle(self.bulletX, self.bulletY, self.bulletTargetX, self.bulletTargetY)

    def move(self):
        if self.parent.target != None:
            self.angle = helper.Helper.calcAngle(self.bulletX, self.bulletY, self.bulletTargetX, self.bulletTargetY)
            self.bulletX, self.bulletY = helper.Helper.getAngledPoint(self.angle, self.speed, self.bulletX, self.bulletY)
            dist = helper.Helper.calcDistance(self.bulletX, self.bulletY, self.bulletTargetX, self.bulletTargetY)

            self.bulletTargetX, self.bulletTargetY = self.parent.updateTarget()

            if self.speed > dist and dist <= self.towerRadius:
                return self
            else:
                pass
