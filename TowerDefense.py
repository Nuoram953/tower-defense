
##TowerDefense

# Francois Therien
# Nicolas Paquette
# Caroline Emond
# Antoine Auger

from tkinter import *
import random


import MapCheckpoints
import Tower
import Creep
import Mower
import Checkpoint

class Vue():
    def __init__(self, parent, modele):
        self.modele = modele
        self.parent = parent
        self.root = Tk()
        self.root.title("towerDefense")
        self.windowMenu()
        self.game = None
        self.gameCanvas = None
        self.gameFrame = None
        self.img = None
        self.gameInProg = False
        self.towerArray = []
        self.tick = False
        self.mushroomCounter = self.modele.mushroomDuration
        self.mowerPositionSelected = False


    def windowMenu(self):
        self.menuFrame = Frame(self.root, bg="spring green3")

        self.welcomeLabel = Label(self.root, text="* WELCOME TO BOTANIK PANIK *",bg="spring green4", fg="dark goldenrod1", font=("system", 20),pady=20)

        self.welcomeLabel.pack(expand=True,fill=BOTH)

        buttonNewGame = Button(self.menuFrame, text="NEW GAME", command=self.gameWindow, bg="deep pink4", fg="pale violetred1",font=("system", 12),relief="raised")
        buttonOptions = Button(self.menuFrame, text="OPTIONS", command=self.options, bg="dark green", fg="lime green",font=("system", 12),relief="raised")
        buttonQuit = Button(self.menuFrame, text="QUITTER", command=self.quit, bg="DodgerBlue4", fg="DeepSkyBlue",font=("system", 12),relief="raised")

        buttonNewGame.grid(column=0, row=0, padx=200, pady=20)
        buttonOptions.grid(column=0, row=1, padx=200, pady=20)
        buttonQuit.grid(column=0, row=2, padx=200, pady=20)

        self.menuFrame.pack()

    #def getXY(self,evt):
        #return evt.x,evt.y
        #print(evt.x, evt.y)
    
    def showGame(self):

        self.gameCanvas.delete(ALL)

        if self.modele.mushroomInUse:
            self.mushroomCounter -= 1

        self.img = PhotoImage(file="assets/Map #1/grass/map1.1.png")                ################## if self.modele.currentMap = 1(2,3...), self.img = ..... todo

        self.gameCanvas.create_image(0, 0, image=self.img, anchor=NW)

        for tower in self.modele.TowerList:
            self.gameCanvas.create_image(tower.posX, tower.posY, image = tower.image, anchor = NW)
            tower.tick()

            if isinstance(tower, Tower.Catapult) and tower.impact:

                self.gameCanvas.create_oval(tower.impactX - (tower.damageRadius/8), tower.impactY - (tower.damageRadius/8),tower.impactX + (tower.damageRadius/8), tower.impactY + (tower.damageRadius/8),outline="red", width=4, tags="circle1")
                self.gameCanvas.create_oval(tower.impactX - (tower.damageRadius / 4),
                                            tower.impactY - (tower.damageRadius / 4),
                                            tower.impactX + (tower.damageRadius / 4),
                                            tower.impactY + (tower.damageRadius / 4), outline="red3", width=3,
                                            tags="circle2")
                self.gameCanvas.create_oval(tower.impactX - (tower.damageRadius / 2),
                                            tower.impactY - (tower.damageRadius / 2),
                                            tower.impactX + (tower.damageRadius / 2),
                                            tower.impactY + (tower.damageRadius / 2), outline="DarkOrange1", width=3,
                                            tags="circle3")
                self.gameCanvas.create_oval(tower.impactX - (tower.damageRadius / 1.25),
                                            tower.impactY - (tower.damageRadius / 1.25),
                                            tower.impactX + (tower.damageRadius / 1.25),
                                            tower.impactY + (tower.damageRadius / 1.25), outline="orange", dash=4,
                                            tags="circle4")
                self.gameCanvas.create_oval(tower.impactX - tower.damageRadius,
                                            tower.impactY - tower.damageRadius,
                                            tower.impactX + tower.damageRadius,
                                            tower.impactY + tower.damageRadius, outline="yellow", dash=3,
                                            tags="circle5")

            if tower.projectileList != None:

                for bullet in tower.projectileList:
                    if bullet.bulletTarget.posX != None and bullet.bulletTarget.posY != None and bullet.bulletTarget != None:
                        bullet.move()
                        self.gameCanvas.create_oval(bullet.bulletX - bullet.size, bullet.bulletY - bullet.size, bullet.bulletX + bullet.size, bullet.bulletY + bullet.size, fill=bullet.color)


        if self.modele.ShowSpots == True:
            for spot in self.modele.CheckpointTowers:
                self.gameCanvas.create_rectangle(spot.x, spot.y, spot.x + self.modele.SquareSize, spot.y + self.modele.SquareSize, fill = self.modele.SquareColor, tags = ("square"))

            self.gameCanvas.tag_bind("square", "<Button>", self.modele.SelectSquare)


        for i in self.modele.creepList:

            self.gameCanvas.create_image(i.posX-(i.width/2),i.posY-(i.height/2),image=i.zombie, anchor=NW)

        if len(self.modele.trapList) != 0:
            for trap in self.modele.trapList:

                self.modele.trapDamage(trap)

                if trap.outOfFrame() == True:
                    self.modele.trapList.remove(trap)
                    del trap
                else:
                    self.gameCanvas.create_image(trap.posX-(trap.width/2), trap.posY-(trap.height/2), image=trap.image, anchor=NW)
                    trap.move()

        if self.mushroomCounter <= 0:
            self.mushroomCounter = self.modele.mushroomDuration
            self.modele.mushroomInUse = False



    def gameWindow(self):
        self.menuFrame.pack_forget()
        self.welcomeLabel.pack_forget()
        self.game = Frame(self.root)
        self.peaShooterimg = PhotoImage(file="assets/towers/peaShooter.png")
        self.sunFlowerimg = PhotoImage(file="assets/towers/sunFlower.png")
        self.catapultimg = PhotoImage(file="assets/towers/catapult.png")
        self.icePeaShooterimg = PhotoImage(file="assets/towers/icePeaShooter.png")
        self.mushimg = PhotoImage(file="assets/towers/mushroom.png")
        self.mowerimg = PhotoImage(file = "assets/towers/mower.png")
        self.towerBg = PhotoImage(file = "assets/HUD/dirt.png")
        self.ressourceBg = PhotoImage(file = "assets/HUD/grass.png")
        self.upgradeBg = PhotoImage(file = "assets/HUD/bedrock.png")
        
        self.gameFrame = Frame(self.game, width=1600, height=800)
        self.gameCanvas = Canvas(self.gameFrame, width=1300, height=800)
        self.frameHUD = Frame(self.gameFrame, width=300, height=800)

        self.ressourceFrame = Canvas(self.frameHUD, width=300, height=250)
        self.towerFrame = Canvas(self.frameHUD, width=300, height=350)
        self.upgradeFrame = Canvas(self.frameHUD, width=300, height=200)

        self.gameCanvas.grid(column=0, row=0)
        self.frameHUD.grid(column=1, row=0)

        self.ressourceFrame.grid(column=1, row=0)
        self.towerFrame.grid(column=1, row=1)
        self.upgradeFrame.grid(column=1, row=2)

        self.ressourceFrame.create_image(0,0, image=self.ressourceBg, anchor=NW)
        self.towerFrame.create_image(0,0, image=self.towerBg, anchor=NW)
        self.upgradeFrame.create_image(0,0, image=self.upgradeBg, anchor=NW)

        self.ressourceFrame.create_text(65,85,text = "Pointage: ", font = ("Times","18","bold"), fill = "white")
        self.pointage = self.ressourceFrame.create_text(140,85, text = self.modele.points["Pointage"], font = ("Times", "18", "bold"), fill ="white")   # faire en sorte que point s'update selon niveau avec self.modele.currentPoints todo

        self.ressourceFrame.create_text(210,85,text = "Vie: ", font = ("Times","18","bold"), fill = "white")
        self.vie = self.ressourceFrame.create_text(255,85, text = self.modele.points["Vie"], font = ("Times", "18", "bold"), fill ="white") # faire en sorte que vie s'update selon niveau todo

        self.ressourceFrame.create_text(60,120,text = "Engrais: ", font = ("Times","18","bold"), fill = "white")
        self.engrais = self.ressourceFrame.create_text(140,120, text = self.modele.points["Engrais"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(210,120,text = "UV: ", font = ("Times","18","bold"), fill = "white")
        self.uv = self.ressourceFrame.create_text(255,120, text = self.modele.points["RayonUV"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(50,155,text = "Wave: ", font = ("Times","18","bold"), fill = "white")
        self.wave = self.ressourceFrame.create_text(100,155, text = self.modele.points["Wave"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(230,155,text = "Niveau: ", font = ("Times","18","bold"), fill = "white")
        self.level = self.ressourceFrame.create_text(280,155, text = self.modele.points["Niveau"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(150, 220, text = "NOM DU JOUEUR", font = ("Times", "24", "bold"), fill = "white")

        self.towerFrame.create_image(120, 50, image=self.peaShooterimg, anchor=NE,tags = ("peaShooter", "tower"))
        self.towerFrame.create_text(90,120, text = "PeaShooter: 25" , font = ("Times", "12", "bold"), fill = "white")       # faire en sorte que le cost s'update selon niveau todo

        self.towerFrame.create_image(250, 45, image=self.sunFlowerimg, anchor=NE,tags = ("sunFlower", "tower"))
        self.towerFrame.create_text(220,120, text = "Sunflower: 20" , font = ("Times", "12", "bold"), fill = "white")       # faire en sorte que le cost s'update selon niveau todo

        self.towerFrame.create_image(120, 150, image=self.icePeaShooterimg, anchor=NE,tags = ("icePeaShooter", "tower"))
        self.towerFrame.create_text(90,220, text = "IcePeaShooter: 35" , font = ("Times", "12", "bold"), fill = "white")    # faire en sorte que le cost s'update selon niveau todo

        self.towerFrame.create_image(250, 150, image = self.catapultimg, anchor = NE,tags = ("catapult", "tower"))
        self.towerFrame.create_text(220,220, text = "Catapulte: 40" , font = ("Times", "12", "bold"), fill = "white")       # faire en sorte que le cost s'update selon niveau todo

        self.towerFrame.create_image(120, 250, image = self.mushimg, anchor = NE,tags = ("mushroom", "hability"))
        self.towerFrame.create_text(90,320, text = "Mush: 50 (UV)" , font = ("Times", "12", "bold"), fill = "white")        # faire en sorte que le cost s'update selon niveau todo

        self.towerFrame.create_image(250, 250, image = self.mowerimg, anchor = NE, tags = ("mower", "hability"))
        self.towerFrame.create_text(220,320, text = "Tondeuse: 100 (UV)" , font = ("Times", "12", "bold"), fill = "white")  # faire en sorte que le cost s'update selon niveau todo

        self.towerFrame.tag_bind("tower", "<Button>", self.modele.ShowSquares)
        self.towerFrame.tag_bind("hability", "<Button>", self.modele.getTrapSelected)

        self.gameFrame.pack(expand=YES, fill=BOTH)
        #self.gameCanvas.bind("<Button>", self.getXY)

        #self.gameCanvas.bind("<Button>", self.modele.printXY)

        self.gameCanvas.bind("<Button>", self.modele.upgradeChoice)
        
        self.game.pack()
        
        self.gameInProg = True
        self.parent.animate()
    
    def update(self):
        self.ressourceFrame.itemconfigure(self.vie, text = self.modele.points["Vie"])
        self.ressourceFrame.itemconfigure(self.wave, text = self.modele.points["Wave"])
        self.ressourceFrame.itemconfigure(self.engrais, text = self.modele.points["Engrais"])
        self.ressourceFrame.itemconfigure(self.uv, text = self.modele.points["RayonUV"])
        self.ressourceFrame.itemconfigure(self.level, text = self.modele.points["Niveau"])
        self.ressourceFrame.itemconfigure(self.pointage, text = self.modele.points["Pointage"])

        
    def options(self):
        pass

    def quit(self):
        pass
    
class Modele():
    def __init__(self, parent):
        self.parent = parent
        # MAP / LEVEL
        self.currentMap = 1             # si on passe au prochain niveau, self.currentMap++ todo




        # CREEP / BOSS
        self.creepList = []
        self.creepHealth = 40                               # à la création des creeps: self.creepHealth * self.currentMap todo
        self.bossHealth = 120                               # à la création des boss: self.bossHealth * self.currentMap todo
        self.checkpointList = MapCheckpoints.mapCreeps[1]   #self.checkpointList = MapCheckpoints.mapCreeps[self.currentMap] pour aller chercher map et checkpoints automatiquement todo

        self.ShowSpots = False
        self.CheckpointTowers = MapCheckpoints.mapTowers[1] #self.CheckpointTowers = MapCheckpoints.mapTowers[self.currentMap] todo
        self.SquareSize = 60
        self.SquareColor = "lightgreen"

        # TOWERS
        self.towerChoice = ""
        self.TowerList = []

        #PEASHOOTER
        self.peaTowerDamage = 2
        self.peaTowerCost = 25

        #ICESHOOTER
        self.iceTowerDamage = 3
        self.iceTowerCost = 35

        #CATAPULT
        self.catapultDamage = 5
        self.catapultCost = 40

        #SUNFLOWER
        self.perSunflowerUV = 5
        self.sunflowerCost = 20
        
        self.validPurchase = False

        # TRAPS
        self.trapList = []
        self.trapChoice = ""
        self.trapSelected = False
        self.mushroomInUse = False
        self.mushroomDuration = 50
        self.mushUVCost = 50
        self.mowerUV = 100
        self.mowerSpeed = 30

        # USER
        self.currentPoints = 0                 # si on passe au prochain niveau, on save nos points courants pour continuer notre high score todo
        self.userVie = 10
        self.startFertilizer = 75


        self.points = {
            "Pointage":0,
            "Vie":10,
            "Engrais":75,
            "RayonUV":500,
            "Wave":0,
            "Niveau":1
        }

        self.towers = {
            "peaShooter":25,
            "sunFlower":20,
            "icePeaShooter":35,
            "catapult":40
        }
    
    def costCheck (self, tower):
        return self.points["Engrais"] >= self.towers[tower]

    #self.traps dictionary
    #def UVCheck function todo

    def ShowSquares(self, event):
        self.ShowSpots = not(self.ShowSpots)

        element = event.widget.gettags("current")

        if element:
            if "peaShooter" in element:
                self.towerChoice = "peaShooter"
            elif "sunFlower" in element:
                self.towerChoice = "sunFlower"
            elif "icePeaShooter" in element:
                self.towerChoice = "icePeaShooter"
            elif "catapult" in element:
                self.towerChoice = "catapult"    

    def SelectSquare(self, event):
        for square in self.CheckpointTowers:
            if event.x >= square.x and event.x <= square.x + self.SquareSize and event.y >= square.y and event.y <= square.y + self.SquareSize:
                self.createTower(square.x, square.y, self.creepList)
                if self.validPurchase:
                    self.CheckpointTowers.remove(square)
                self.ShowSpots = not(self.ShowSpots)

    def createTower(self, posX, posY, creepList):
        if self.towerChoice == "peaShooter" and self.costCheck("peaShooter"):
            tour = Tower.PeaShooter(self, posX, posY, creepList)                # tour = Tower.PeaShooter(self, posX, posY, creepList, (self.peaTowerDamage * self.currentMap)) todo
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["peaShooter"]
            self.validPurchase = True
            
        elif self.towerChoice == "sunFlower" and self.costCheck("sunFlower"):
            tour = Tower.SunFlower(self, posX, posY)
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["sunFlower"]
            self.validPurchase = True
           
        elif self.towerChoice == "icePeaShooter" and self.costCheck("icePeaShooter"):
            tour = Tower.IcePeaShooter(self, posX, posY, creepList)             # tour = Tower.IcePeaShooter(self, posX, posY, creepList, (self.iceTowerDamage * self.currentMap)) todo
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["icePeaShooter"]
            self.validPurchase = True

        elif self.towerChoice == "catapult" and self.costCheck("catapult"):
            tour = Tower.Catapult(self,posX,posY, creepList)                    # tour = Tower.Catapult(self,posX,posY, creepList, (self.catapultDamage * self.currentMap)) todo
            self.TowerList.append(tour)  
            self.points["Engrais"] -= self.towers["catapult"]
            self.validPurchase = True
        
        else:
            self.validPurchase = False
           
        
    def createCreep(self):
        nbCreep = random.randint(5,10)
        nbCreep += (self.points["Wave"] * 3)
        for i in range(nbCreep):
            distanceX = random.randint(-500, 0)
            self.creepList.append(Creep.Creep1(self, distanceX, 610, self.checkpointList[0], False))

    def updateCreepList(self):
        return self.creepList

    def createBoss(self):
        distanceX = random.randint(-500, 0)
        self.creepList.append(Creep.Creep1(self, distanceX, 550, self.checkpointList[0], True))

    def creepMovement(self):
        for i in self.creepList:

            if not self.mushroomInUse:
                i.move()
            else:
                i.wait()

    def getNextCheckpoint(self, currentCheckpoint):
        currentIndex = self.checkpointList.index(currentCheckpoint)
        checkpointList_len = len(self.checkpointList) - 1
        if currentIndex < checkpointList_len:
            return self.checkpointList[currentIndex+1]
        else:
            pass

    def deathCheck(self):
        for i in self.creepList:
            if i.reachedEnd:
                self.creepList.remove(i)
                del i
                if self.points["Vie"] > 0:
                    self.points["Vie"] -= 1
                else:
                    #methode game over todo
                    pass

    # fonction nextLevelCheck si toujours en vie et no more creep waves, newgame, self.currentMap++ todo
    
    def sunflowerUV (self):
        for tower in self.TowerList:
            if isinstance(tower, Tower.SunFlower):
                self.points["RayonUV"] += 5             ########################### self.perSunflowerUV todo

    def getTrapSelected(self, event):

        self.trapSelected = not(self.trapSelected)

        element = event.widget.gettags("current")

        if "mushroom" in element and self.points["RayonUV"] >= 50:
            self.trapChoice = "mushroom"
            self.activateMushroom()
        elif "mower" in element and self.points["RayonUV"] >= 100:
            self.trapChoice = "mower"
            self.parent.vue.gameCanvas.bind("<Button>", self.getMowerPosition)

    def activateMushroom(self):
        if self.trapChoice == "mushroom" and self.trapSelected:
            self.points["RayonUV"] -= 50
            self.mushroomInUse = True
            self.trapSelected = not(self.trapSelected)

    def printXY(self, evt):
        print(evt.x, evt.y)

    def getMowerPosition(self,evt):
        if self.trapChoice == "mower" and self.trapSelected:
            x = evt.x
            y = evt.y
            self.createMower(x,y)
            self.points["RayonUV"] -= 100
            self.trapSelected = not(self.trapSelected)
            self.parent.vue.gameCanvas.bind("<Button>", self.upgradeChoice)

    def createMower(self,x,y):
        self.trapList.append(Mower.Mower(self, x, y, self.mowerSpeed))

    def trapDamage(self, trap):
        for creep in self.creepList:
            if trap.posX >= creep.posX - 50 and trap.posX <= creep.posX + 50 and trap.posY >= creep.posY - 50 and trap.posY <= creep.posY + 50:
                creep.hitByTrap = True

                if creep.hitByTrap and creep.hittable:
                    creep.hittable = False
                    creep.health -= trap.damage

                    if creep.health <= 0:
                        self.creepList.remove(creep)

    def upgradeChoice(self, event):
        for tower in self.TowerList:
            if event.x >= tower.posX and event.x <= tower.posX + 65 and event.y >= tower.posY and event.y <= tower.posY + 65:
                if not tower.upgraded:
                    pass
                    
                    

class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.creepWave()
        self.vue.root.after(10, self.animate)
        self.vue.root.after(10000, self.addUV)
        self.vue.root.mainloop()
        
    def creepWave(self):
        if len(self.modele.creepList) == 0:
            self.modele.createCreep()
            self.modele.points["Wave"] +=1
            self.modele.points["Engrais"] += 50
            if self.modele.points["Wave"] == 5:
                self.modele.createBoss()

    def addUV(self):
        self.modele.sunflowerUV()
        self.vue.root.after(20000, self.addUV)


    def animate(self):
        if self.vue.gameInProg == True:
            self.creepWave()
            self.modele.deathCheck()
            self.modele.creepMovement()
            self.vue.showGame()
            self.vue.update()
            self.vue.root.after(25, self.animate)
            
if __name__ == '__main__':
    c = Controleur()
