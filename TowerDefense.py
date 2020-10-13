
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

    def getXY(self,evt):
        pass
        #print(evt.x, evt.y)


    def showGame(self):

        self.gameCanvas.delete(ALL)

        self.img = PhotoImage(file="assets/Map #1/grass/map1.1.png")

        self.gameCanvas.create_image(0, 0, image=self.img, anchor=NW)

        for tower in self.modele.TowerList:
            self.gameCanvas.create_image(tower.posX, tower.posY, image = tower.image, anchor = NW)
            tower.tick()
            for bullet in tower.projectileList:
                bullet.move()
                self.gameCanvas.create_oval(bullet.bulletX - bullet.size, bullet.bulletY - 10, bullet.bulletX + 10, bullet.bulletY + 10,fill=bullet.color)


        if self.modele.ShowSpots == True:
            for spot in self.modele.CheckpointTowers:
                self.gameCanvas.create_rectangle(spot.x, spot.y, spot.x + self.modele.SquareSize, spot.y + self.modele.SquareSize, fill = self.modele.SquareColor, tags = ("square"))

            self.gameCanvas.tag_bind("square", "<Button>", self.modele.SelectSquare)

        for i in self.modele.creepList:
            self.gameCanvas.create_image(i.posX-(i.width/2),i.posY-(i.height/2),image=i.zombie, anchor=NW)

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
        self.pointage = self.ressourceFrame.create_text(140,85, text = self.modele.points["Pointage"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(210,85,text = "Vie: ", font = ("Times","18","bold"), fill = "white")
        self.vie = self.ressourceFrame.create_text(255,85, text = self.modele.points["Vie"], font = ("Times", "18", "bold"), fill ="white")

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
        self.towerFrame.create_text(90,120, text = "PeaShooter: 25" , font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(250, 45, image=self.sunFlowerimg, anchor=NE,tags = ("sunFlower", "tower"))
        self.towerFrame.create_text(220,120, text = "Sunflower: 20" , font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(120, 150, image=self.icePeaShooterimg, anchor=NE,tags = ("icePeaShooter", "tower"))
        self.towerFrame.create_text(90,220, text = "IcePeaShooter: 35" , font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(250, 150, image = self.catapultimg, anchor = NE,tags = ("catapult", "tower"))
        self.towerFrame.create_text(220,220, text = "Catapulte: 40" , font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(120, 250, image = self.mushimg, anchor = NE,tags = ("mushroom", "hability"))
        self.towerFrame.create_text(90,320, text = "Mush: 50 (UV)" , font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(250, 250, image = self.mowerimg, anchor = NE, tags = ("mower", "hability"))
        self.towerFrame.create_text(220,320, text = "Tondeuse: 100 (UV)" , font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.tag_bind("tower", "<Button>", self.modele.ShowSquares)

        self.gameFrame.pack(expand=YES, fill=BOTH)
        self.gameCanvas.bind("<Button>", self.getXY)
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
        self.creepList = []
        self.checkpointList = MapCheckpoints.mapCreeps[1]

        self.ShowSpots = False
        self.CheckpointTowers = MapCheckpoints.mapTowers[1]
        self.SquareSize = 60
        self.SquareColor = "lightgreen"

        self.towerChoice = ""

        self.TowerList = []

        self.points = {
            "Pointage":0,
            "Vie":10,
            "Engrais":75,
            "RayonUV":0,
            "Wave":4,
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
                self.CheckpointTowers.remove(square)
                self.ShowSpots = not(self.ShowSpots)

    def createTower(self, posX, posY, creepList):
        if self.towerChoice == "peaShooter" and self.costCheck("peaShooter"):
            tour = Tower.PeaShooter(self, posX, posY, creepList)
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["peaShooter"]
            
        elif self.towerChoice == "sunFlower" and self.costCheck("sunFlower"):
            tour = Tower.SunFlower(self, posX, posY)
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["sunFlower"]
           
        elif self.towerChoice == "icePeaShooter" and self.costCheck("icePeaShooter"):
            tour = Tower.IcePeaShooter(self, posX, posY, creepList)
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["icePeaShooter"]

        elif self.towerChoice == "catapult" and self.costCheck("catapult"):
            tour = Tower.Catapult(self,posX,posY, creepList) 
            self.TowerList.append(tour)  
            self.points["Engrais"] -= self.towers["catapult"]

    def activateTower(self):
        for tower in self.TowerList:
            tower.tick()
           
        
    def createCreep(self):
        nbCreep = random.randint(5,10)
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
            i.move()

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
                    #methode game over
                    pass    
    
    def sunflowerUV (self):
        for tower in self.TowerList:
            if isinstance(tower, Tower.SunFlower):
                self.points["RayonUV"] += 5
                
                
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
            self.modele.points["Engrais"] += 25
            if self.modele.points["Wave"] == 5:
                self.modele.createBoss()

    def addUV(self):
        self.modele.sunflowerUV()
        self.vue.root.after(10000, self.addUV)

    def animate(self):
        if self.vue.gameInProg == True:
            self.creepWave()
            self.modele.activateTower()
            self.modele.deathCheck()
            self.modele.creepMovement()
            self.vue.showGame()
            self.vue.update()
            self.vue.root.after(10, self.animate)
            
if __name__ == '__main__':
    c = Controleur()
