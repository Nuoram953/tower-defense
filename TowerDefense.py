
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
        self.catapultimg = PhotoImage(file="assets/towers/sunFlower.png")
        self.nutimg = PhotoImage(file="assets/towers/sunFlower.png")
        self.potatoMineimg = PhotoImage(file="assets/towers/sunFlower.png")
        self.icePeaShooterimg = PhotoImage(file="assets/towers/icePeaShooter.png")
        self.towerBg = PhotoImage(file = "assets/HUD/dirt.png")
        self.ressourceBg = PhotoImage(file = "assets/HUD/grass.png")
        self.upgradeBg = PhotoImage(file = "assets/HUD/bedrock.png")
        
        self.gameFrame = Frame(self.game, width=1600, height=800)
        self.gameCanvas = Canvas(self.gameFrame, width=1300, height=800)
        self.frameHUD = Frame(self.gameFrame, width=300, height=800)

        self.ressourceFrame = Canvas(self.frameHUD, width=300, height=100)
        self.towerFrame = Canvas(self.frameHUD, width=300, height=600)
        self.upgradeFrame = Canvas(self.frameHUD, width=300, height=100)

        self.gameCanvas.grid(column=0, row=0)
        self.frameHUD.grid(column=1, row=0)

        self.ressourceFrame.grid(column=1, row=0)
        self.towerFrame.grid(column=1, row=1)
        self.upgradeFrame.grid(column=1, row=2)

        self.ressourceFrame.create_image(0,0, image=self.ressourceBg, anchor=NW)
        self.towerFrame.create_image(0,0, image=self.towerBg, anchor=NW)
        self.upgradeFrame.create_image(0,0, image=self.upgradeBg, anchor=NW)

        self.towerFrame.create_image(100, 100, image=self.peaShooterimg, anchor=NE,tags = ("peaShooter", "tower"))
        self.towerFrame.create_image(200, 100, image=self.sunFlowerimg, anchor=NE,tags = ("sunFlower", "tower"))
        self.towerFrame.create_image(100, 200, image=self.icePeaShooterimg, anchor=NE,tags = ("icePeaShooter", "tower"))

        self.towerFrame.tag_bind("tower", "<Button>", self.modele.ShowSquares)

        self.gameFrame.pack(expand=YES, fill=BOTH)
        self.gameCanvas.bind("<Button>", self.getXY)
        self.game.pack()
        
        self.gameInProg = True
        self.parent.animate()


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


    def SelectSquare(self, event):
        for square in self.CheckpointTowers:
            if event.x >= square.x and event.x <= square.x + self.SquareSize and event.y >= square.y and event.y <= square.y + self.SquareSize:
                self.createTower(square.x, square.y)
                self.CheckpointTowers.remove(square)
                self.ShowSpots = not(self.ShowSpots)

    def createTower(self, posX, posY):
        if self.towerChoice == "peaShooter":
            tour = Tower.PeaShooter(self, posX, posY)
            self.TowerList.append(tour)
           
        elif self.towerChoice == "sunFlower":
            tour = Tower.SunFlower(self, posX, posY)
            self.TowerList.append(tour)
           
        elif self.towerChoice == "icePeaShooter":
            tour = Tower.IcePeaShooter(self, posX, posY)
            self.TowerList.append(tour)
           
        
    def createCreep(self):
        nbCreep = random.randint(5,10)
        for i in range(nbCreep):
            distanceX = random.randint(-500, 0)
            self.creepList.append(Creep.Creep1(self, distanceX, 610, self.checkpointList[0]))
        
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
                
    
class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.creepWave()
        self.vue.root.after(10, self.animate)
        self.vue.root.mainloop()

    def creepWave(self):
        if len(self.modele.creepList) == 0:
            self.modele.createCreep()

    def animate(self):
        if self.vue.gameInProg == True:
            self.creepWave()
            self.modele.deathCheck()
            self.modele.creepMovement()
            self.vue.showGame()
            self.vue.root.after(10, self.animate)

if __name__ == '__main__':
    c = Controleur()
