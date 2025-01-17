
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
import Mode
import score

class Vue():
    def __init__(self, parent, modele):

        self.modele = modele
        self.parent = parent
        self.restart = False
        self.root = Tk()
        self.root.title("towerDefense")
        self.backFromOptions = False
        self.life = None
        self.mode = None
        self.towersUpgraded = None
        self.windowMenu()
        self.game = None
        self.top = None
        self.gameCanvas = None
        self.gameFrame = None
        self.img = None
        self.gameInProg = False
        self.towerArray = []
        self.tick = False
        self.mushroomCounter = self.modele.mushroomDuration
        self.mowerPositionSelected = False
        self.towerUpgradeChoice = ""
        self.playerName = None
        self.messageX = 1400
        self.messageY = 150
        self.gameOverCreep = None
        self.creepX = 415
        self.creepY = 750
        self.winCounter = 0
        self.winX = 1400
        self.winY = 250


    def windowMenu(self):

        if self.backFromOptions == True:
            self.optionFrame.pack_forget()
            self.optionsLabel.pack_forget()

        self.menuFrame = Frame(self.root, bg="spring green3")

        self.welcomeLabel = Label(self.root, text="* WELCOME TO BOTANIK PANIK *",bg="spring green4", fg="dark goldenrod1", font=("system", 20),pady=20)

        self.welcomeLabel.pack(expand=True,fill=BOTH)

        self.entryPlayerNameLabel = Label(self.menuFrame,relief="raised",text="Entrez votre nom: ",borderwidth=0,highlightthickness=0,bg="spring green3")
        self.entryPlayerName = Entry(self.menuFrame,relief="raised")
        buttonNewGame = Button(self.menuFrame, text="NEW GAME", command=self.gameWindow, bg="deep pink4", fg="pale violetred1",font=("system", 12),relief="raised")
        buttonOptions = Button(self.menuFrame, text="OPTIONS", command=self.optionMenu, bg="dark green", fg="lime green",font=("system", 12),relief="raised")

        self.entryPlayerNameLabel.grid(column=0,row=0,padx=50,pady=25)
        self.entryPlayerName.grid(column=0,row=1,padx = 50,pady=0 )
      
        buttonNewGame.grid(column=0, row=2, padx=200, pady=40)
        buttonOptions.grid(column=0, row=3, padx=200, pady=20)
       

        self.menuFrame.pack()

    def optionMenu(self):

        self.mode = StringVar()
        self.life = StringVar()
        self.towersUpgraded = IntVar()


        self.menuFrame.pack_forget()
        self.welcomeLabel.pack_forget()

        self.optionFrame = Frame(self.root, bg="spring green3")

        self.optionsLabel = Label(self.root, text="* OPTIONS *", bg="spring green4",
                                  fg="dark goldenrod1", font=("system", 20), pady=20, padx=100)

        self.optionsLabel.pack(expand=True, fill=BOTH)

        self.modeFrame = Frame(self.optionFrame, bg="spring green3")

        option1 = Radiobutton(self.modeFrame, text="Normal difficulty", variable=self.mode, value="normal", bg="SpringGreen2", fg="dark green", font=("system", 12), command=self.parent.setNormalDifficulty, indicatoron = 0, pady=10)
        option1.pack()

        option2 = Radiobutton(self.modeFrame, text="Hard difficulty", variable=self.mode, value="hard", bg="red2", fg="light pink", font=("system", 12), command=self.parent.setHardDifficulty, indicatoron = 0, pady=10)
        option2.pack()

        self.modeFrame.pack(expand=True, fill=BOTH, pady=10)

        self.lifeFrame = Frame(self.optionFrame, bg="spring green3")

        life1 = Radiobutton(self.lifeFrame, text="life = 10", variable=self.life, value=10, bg="spring green", fg="dark green", font=("system", 12),command=self.parent.setLifeTen, indicatoron = 0, pady=5)
        life1.pack()

        life2 = Radiobutton(self.lifeFrame, text="life = 20", variable=self.life, value=20, bg="spring green", fg="dark green", font=("system", 12),command=self.parent.setLifeTwenty, indicatoron = 0, pady=5)
        life2.pack()

        life3 = Radiobutton(self.lifeFrame, text="life = 30", variable=self.life, value=30, bg="spring green", fg="dark green",font=("system", 12),command=self.parent.setLifeThirty, indicatoron = 0,pady=5)
        life3.pack()

        self.lifeFrame.pack(expand=True, fill=BOTH, pady=10)

        upgrade = Checkbutton(self.optionFrame, text="Towers Upgraded",variable=self.towersUpgraded, bg="spring green3", fg="purple4", font=("system", 12), command=self.parent.setUpgraded, pady=10)
        upgrade.pack()

        buttonBack = Button(self.optionFrame, text="BACK TO MAIN MENU", command=self.setOptions, bg="blue", fg="deep sky blue",
                               font=("system", 12), relief="raised", pady=10)

        buttonBack.pack()

        self.optionFrame.pack(expand=True, fill=BOTH)


    def setOptions(self):

        self.backFromOptions = True
        self.windowMenu()

    def showGame(self):

        self.gameCanvas.delete(ALL)

        if (self.modele.currentMap == 1):
            self.img = PhotoImage(file="assets/maps/map1.png", master=self.game)
        elif (self.modele.currentMap == 2):
            self.img = PhotoImage(file="assets/maps/map2.png", master=self.game)
        else:
            self.img = PhotoImage(file="assets/maps/map3.png", master=self.game)

        self.gameCanvas.create_image(0, 0, image=self.img, anchor=NW)
        
        if self.modele.mushroomInUse:
            self.image = PhotoImage(file="assets/UV.png",master=self.game) 
            self.gameCanvas.create_image(0,0, image=self.image, anchor=NW)
            self.mushroomCounter -= 1           


        if self.modele.TowerList != None:
            for tower in self.modele.TowerList:
                self.gameCanvas.create_image(tower.posX, tower.posY, image = tower.image, anchor = NW)
                if not self.modele.gameIsOver:
                    tower.tick()
                else:
                    tower.projectileList = []

                self.update()        # pour update le nombre de points au fur et à mesure que les creeps meurent

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
                    self.update()       # pour update le nombre de points au fur et à mesure que les creeps meurent

        if self.mushroomCounter <= 0:
            self.mushroomCounter = self.modele.mushroomDuration
            self.modele.mushroomInUse = False

        if self.modele.gameIsOver:
            self.gameCanvas.create_text(self.messageX, self.messageY, text="GAME OVER", font=("system", "70", "bold"), fill="red")
            self.gameCanvas.create_image(self.creepX, self.creepY, image=self.gameOverCreep, anchor=NW)

            if self.messageX > 725:
                self.messageX -= 30

            if self.creepY >= 200:
                self.creepY -= 25
            else:
                self.root.after(2500, self.parent.close_window)

        if self.modele.userWon == True:
            self.winCounter += 1

            if self.winX > 725:
                self.winX -= 40

            if self.winCounter % 2 == 0:
                self.gameCanvas.create_text(self.winX, self.winY, text="Y O U  W I N", font=("system","100", "bold"), fill="DarkGoldenrod1")
            else:
                self.gameCanvas.create_text(self.winX, self.winY, text="Y O U  W I N", font=("system","100", "bold"), fill="yellow")


        if self.parent.startLevelMessage == True:
            self.gameCanvas.create_text(self.messageX, self.messageY, text="LEVEL " + str(self.modele.currentMap),
                                        font=("system", "70", "bold"), fill="DarkGoldenrod1")
            if self.messageX > -200:
                self.messageX -= 50
            else:
                self.parent.startLevelMessage = False
                self.messageX = 1400



    def gameWindow(self):

        self.parent.profil(self.entryPlayerName.get())
        self.parent.setDifficultyValues()

        self.menuFrame.pack_forget()
        self.welcomeLabel.pack_forget()

        self.game = Frame(self.root)
        self.gameOverCreep = PhotoImage(file="assets/zombies/gameOverCreep.png")
        self.peaShooterimg = PhotoImage(file="assets/towers/peaShooter.png")
        self.sunFlowerimg = PhotoImage(file="assets/towers/sunFlower.png")
        self.catapultimg = PhotoImage(file="assets/towers/catapult.png")
        self.icePeaShooterimg = PhotoImage(file="assets/towers/icePeaShooter.png")
        self.mushimg = PhotoImage(file="assets/towers/mushroom.png")
        self.mowerimg = PhotoImage(file = "assets/towers/mower.png")
        self.towerBg = PhotoImage(file = "assets/HUD/dirt.png")
        self.ressourceBg = PhotoImage(file = "assets/HUD/grass.png")
        self.upgradeBg = PhotoImage(file = "assets/HUD/UpgradeStone.png")
        
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

        self.ressourceFrame.create_text(65,85,text = "Score: ", font = ("Times","18","bold"), fill = "white")
        self.pointage = self.ressourceFrame.create_text(140,85, text = self.modele.points["Pointage"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(210,85,text = "Life: ", font = ("Times","18","bold"), fill = "white")
        self.vie = self.ressourceFrame.create_text(255,85, text = self.modele.points["Vie"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(60,120,text = "Fertilizer: ", font = ("Times","18","bold"), fill = "white")
        self.engrais = self.ressourceFrame.create_text(140,120, text = self.modele.points["Engrais"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(210,120,text = "UV: ", font = ("Times","18","bold"), fill = "white")
        self.uv = self.ressourceFrame.create_text(255,120, text = self.modele.points["RayonUV"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(50,155,text = "Wave: ", font = ("Times","18","bold"), fill = "white")
        self.wave = self.ressourceFrame.create_text(100,155, text = self.modele.points["Wave"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(230,155,text = "Level: ", font = ("Times","18","bold"), fill = "white")
        self.level = self.ressourceFrame.create_text(280,155, text = self.modele.points["Niveau"], font = ("Times", "18", "bold"), fill ="white")

        self.ressourceFrame.create_text(150, 220, text = self.modele.playerName, font = ("Times", "24", "bold"), fill = "white")

        self.towerFrame.create_image(120, 50, image=self.peaShooterimg, anchor=NE,tags = ("peaShooter", "tower"))
        self.peaFrameCost = self.towerFrame.create_text(90,120, text = "PeaShooter: " + str(self.modele.peaTowerCost), font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(250, 45, image=self.sunFlowerimg, anchor=NE,tags = ("sunFlower", "tower"))
        self.sunFrameCost = self.towerFrame.create_text(220,120, text = "Sunflower: " + str(self.modele.sunflowerCost), font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(120, 150, image=self.icePeaShooterimg, anchor=NE,tags = ("icePeaShooter", "tower"))
        self.iceFrameCost = self.towerFrame.create_text(90,220, text = "IcePeaShooter: " + str(self.modele.iceTowerCost), font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(250, 150, image = self.catapultimg, anchor = NE,tags = ("catapult", "tower"))
        self.catapultFrameCost = self.towerFrame.create_text(220,220, text = "Catapulte: " + str(self.modele.catapultCost), font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(120, 250, image = self.mushimg, anchor = NE,tags = ("mushroom", "hability"))
        self.mushFrameCost = self.towerFrame.create_text(90,320, text = "Mush: " + str(self.modele.mushUVCost) + " (UV)", font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.create_image(250, 250, image = self.mowerimg, anchor = NE, tags = ("mower", "hability"))
        self.mowerFrameCost = self.towerFrame.create_text(220,320, text = "Mower: " + str(self.modele.mowerUVCost) + " (UV)", font = ("Times", "12", "bold"), fill = "white")

        self.towerFrame.tag_bind("tower", "<Button>", self.modele.ShowSquares)
        self.towerFrame.tag_bind("hability", "<Button>", self.modele.getTrapSelected)

        self.gameFrame.pack(expand=YES, fill=BOTH)

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

    def upgradeStats(self,tower):
        self.upgradeFrame.delete(ALL)
        self.upgradeFrame.create_image(0,0, image=self.upgradeBg, anchor=NW)
    
        towerName = tower.__class__.__name__
        self.towerUpgradeChoice = tower
        self.upgradeFrame.create_text(150,30, text = towerName , font = ("Times", "18", "bold"), fill = "white")

        
        if towerName != "SunFlower":      
            self.upgradeFrame.create_text(80,100, text = "Rate of Fire: " + str(tower.rateOfFire) , font = ("Times", "14", "bold"), fill = "white")
            self.upgradeFrame.create_text(230,100, text = "Speed: " + str(tower.projectileSpeed) , font = ("Times", "14", "bold"), fill = "white")

            if towerName == "PeaShooter":
                self.upgradeFrame.create_text(65,65, text = "Radius: " + str(tower.radius), font = ("Times", "14", "bold"), fill = "white")
                self.upgradeFrame.create_text(220,65, text = "Damage: " + str(tower.damage), font = ("Times", "14", "bold"), fill = "white")
                if self.towerUpgradeChoice.upgraded == False:
                    self.upgradeFrame.create_text(160,100, text = "+5" , font = ("Times", "14", "bold"), fill = "green2")
                    self.upgradeFrame.create_text(150,130, text = "Upgrade Cost: " + str(tower.upgradeCost) + " fertilizer", font = ("Times", "14", "bold"), fill = "white")

            elif towerName == "IcePeaShooter":
                self.upgradeFrame.create_text(65,65, text = "Radius: " + str(tower.radius), font = ("Times", "14", "bold"), fill = "white") 
                self.upgradeFrame.create_text(220,65, text = "Damage: " + str(tower.damage), font = ("Times", "14", "bold"), fill = "white")
                if self.towerUpgradeChoice.upgraded == False:
                    self.upgradeFrame.create_text(285,65, text = "+2" , font = ("Times", "14", "bold"), fill = "green2")
                    self.upgradeFrame.create_text(150,130, text = "Upgrade Cost: " + str(tower.upgradeCost) + " fertilizer", font = ("Times", "14", "bold"), fill = "white")

            elif towerName == "Catapult":
                self.upgradeFrame.create_text(90,65, text = "Damage Radius: " + str(tower.damageRadius), font = ("Times", "14", "bold"), fill = "white")
                self.upgradeFrame.create_text(250,65, text = "Damage: " + str(tower.damage), font = ("Times", "14", "bold"), fill = "white")
                if self.towerUpgradeChoice.upgraded == False:
                    self.upgradeFrame.create_text(185,65, text = "+75" , font = ("Times", "14", "bold"), fill = "green2")
                    self.upgradeFrame.create_text(150,130, text = "Upgrade Cost: " + str(tower.upgradeCost) + " fertilizer", font = ("Times", "14", "bold"), fill = "white")
        else:
            if self.towerUpgradeChoice.upgraded == False:
                self.upgradeFrame.create_text(100,65, text = "UV gain: " + str(self.modele.perSunflowerUV), font = ("Times", "14", "bold"), fill = "white")
                self.upgradeFrame.create_text(192,65, text = "+" + str(self.modele.perSunflowerUV), font = ("Times", "14", "bold"), fill = "green2")
                self.upgradeFrame.create_text(150,130, text = "Upgrade Cost: " + str(tower.upgradeCost) + " fertilizer", font = ("Times", "14", "bold"), fill = "white")
            else:
                self.upgradeFrame.create_text(100,65, text = "UV gain: " + str(self.modele.perSunflowerUpgradeUV), font = ("Times", "14", "bold"), fill = "white")

        if self.towerUpgradeChoice.upgraded == False:
            buttonUpgrade = Button(self.upgradeFrame, text="UPGRADE", command=self.upgradeTower, bg="green2", fg="white",font=("Times", "14", "bold"),relief="raised")
            buttonUpgrade_window = self.upgradeFrame.create_window(100,150,anchor=NW, window = buttonUpgrade)

    def upgradeTower(self):  
        towerName = self.towerUpgradeChoice.__class__.__name__
        engrais = self.modele.points["Engrais"]
        if towerName == "PeaShooter" and self.towerUpgradeChoice.upgradeCost <= engrais:
            self.towerUpgradeChoice.rateOfFire = 5
            self.towerUpgradeChoice.upgraded = True
            self.modele.points["Engrais"] -= self.towerUpgradeChoice.upgradeCost
            self.towerUpgradeChoice.image = PhotoImage(file = "assets/towers/peaShooterUpgrade.png")
            self.towerUpgradeChoice.bulletColor = "lawn green"
        elif towerName == "SunFlower" and self.towerUpgradeChoice.upgradeCost <= engrais:
            self.towerUpgradeChoice.upgraded = True
            self.towerUpgradeChoice.image = PhotoImage(file = "assets/towers/sunFlowerUpgrade.png")
            self.modele.points["Engrais"] -= self.towerUpgradeChoice.upgradeCost
        elif towerName == "IcePeaShooter" and self.towerUpgradeChoice.upgradeCost <= engrais:
            self.towerUpgradeChoice.damage = 5
            self.towerUpgradeChoice.upgraded = True
            self.towerUpgradeChoice.image = PhotoImage(file = "assets/towers/icePeaShooterUpgrade.png")
            self.modele.points["Engrais"] -= self.towerUpgradeChoice.upgradeCost
            self.towerUpgradeChoice.bulletColor = "RoyalBlue3"
        elif towerName == "Catapult" and self.towerUpgradeChoice.upgradeCost <= engrais:
            self.towerUpgradeChoice.damageRadius = 150
            self.towerUpgradeChoice.upgraded = True
            self.modele.points["Engrais"] -= self.towerUpgradeChoice.upgradeCost
            self.towerUpgradeChoice.image = PhotoImage(file = "assets/towers/catapultUpgrade.png")
            self.towerUpgradeChoice.bulletSize += 10
            self.towerUpgradeChoice.bulletColor = "dark green"
        
        self.upgradeStats(self.towerUpgradeChoice)

    
class Modele():
    def __init__(self, parent):
        self.parent = parent
        # MAP / LEVEL
        self.currentMap = 1
        self.difficulty = "normal"      # default

        # CREEP / BOSS
        self.creepList = []
        self.creepHealth = 35
        self.bossHealth = 120
        self.checkpointList = MapCheckpoints.mapCreeps[str(self.currentMap)]       # self.checkpointList = MapCheckpoints.mapCreeps[self.currentMap] lorsque les maps seront faites
        self.creepStartY = self.checkpointList[0].y
        self.bossStartY = self.checkpointList[0].y - 60
        self.lastCheckpointX = self.checkpointList[(len(self.checkpointList)-1)].x
        self.lastCheckpointY = self.checkpointList[(len(self.checkpointList)-1)].y

        self.ShowSpots = False
        self.CheckpointTowers = MapCheckpoints.mapTowers[str(self.currentMap)]     # self.CheckpointTowers = MapCheckpoints.mapTowers[self.currentMap] lorsque les maps seront faites
        self.SquareSize = 60
        self.SquareColor = "lightgreen"
        self.gameIsOver = False
        self.userWon = False
        self.newLevel = False


        # TOWERS
        self.towerChoice = ""
        self.TowerList = []
        self.alreadyUpgraded = False

        #PEASHOOTER
        self.peaTowerDamage = 3 
        self.peaTowerCost = 20

        #ICESHOOTER
        self.iceTowerDamage = 3 
        self.iceTowerCost = 30 

        #CATAPULT
        self.catapultDamage = 6 
        self.catapultCost = 40 

        #SUNFLOWER
        self.perSunflowerUV = 5 
        self.perSunflowerUpgradeUV = 10 
        self.sunflowerCost = 20 
        
        self.validPurchase = False

        # TRAPS
        self.trapList = []
        self.trapChoice = ""
        self.trapSelected = False
        self.mushroomInUse = False
        self.mushroomDuration = 50
        self.mushUVCost = 25 
        self.mowerUVCost = 50
        self.mowerSpeed = 30

        # USER
        self.playerName = None
        self.currentPoints = 0                 # si on passe au prochain niveau, on save nos points courants pour continuer notre high score
        self.currentFertilizer = 0              # engrais du user à la fin d'un niveau s'ajoute à l'engrais de base du prochain niveau
        self.currentUV = 0                     # UV du user à la fin d'un niveau s'ajoute à l'UV de base du prochain niveau


        self.points = {
            "Pointage": (0 + self.currentPoints),
            "Vie":15,
            "Engrais":100 + self.currentFertilizer,
            "RayonUV":(50 + self.currentUV),
            "Wave":0,
            "Niveau":1
        }

        self.towers = {
            "peaShooter":self.peaTowerCost,
            "sunFlower":self.sunflowerCost,
            "icePeaShooter":self.iceTowerCost,
            "catapult":self.catapultCost
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
                if self.validPurchase:
                    self.CheckpointTowers.remove(square)
                self.ShowSpots = not(self.ShowSpots)


    def createTower(self, posX, posY, creepList):
        if self.towerChoice == "peaShooter" and self.costCheck("peaShooter"):
            tour = Tower.PeaShooter(self, posX, posY, self.peaTowerDamage, creepList, self.alreadyUpgraded)
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["peaShooter"]
            self.validPurchase = True
            
        elif self.towerChoice == "sunFlower" and self.costCheck("sunFlower"):
            tour = Tower.SunFlower(self, posX, posY, self.alreadyUpgraded)
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["sunFlower"]
            self.validPurchase = True
           
        elif self.towerChoice == "icePeaShooter" and self.costCheck("icePeaShooter"):
            tour = Tower.IcePeaShooter(self, posX, posY, self.iceTowerDamage, creepList, self.alreadyUpgraded)
            self.TowerList.append(tour)
            self.points["Engrais"] -= self.towers["icePeaShooter"]
            self.validPurchase = True

        elif self.towerChoice == "catapult" and self.costCheck("catapult"):
            tour = Tower.Catapult(self,posX,posY, self.catapultDamage, creepList, self.alreadyUpgraded)
            self.TowerList.append(tour)  
            self.points["Engrais"] -= self.towers["catapult"]
            self.validPurchase = True
        
        else:
            self.validPurchase = False
           
        
    def createCreep(self):
        nbCreep = 4
        nbCreep += (self.points["Wave"] * 4)

        for i in range(nbCreep):
            distanceX = random.randint(-500, 0)
            self.creepList.append(Creep.Creep1(self, distanceX, self.creepStartY, self.checkpointList[0],self.creepHealth , False))

    def updateCreepList(self):
        return self.creepList

    def createBoss(self):
        distanceX = random.randint(-500, 0)
        self.creepList.append(Creep.Creep1(self, distanceX, self.bossStartY, self.checkpointList[0],self.bossHealth , True))

    def creepMovement(self):
        for i in self.creepList:

            if not self.mushroomInUse and not self.gameIsOver and not self.parent.startLevelMessage:
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

    def sunflowerUV (self):
        for tower in self.TowerList:
            if isinstance(tower, Tower.SunFlower):
                if tower.upgraded:
                    self.points["RayonUV"] += (10)
                else:
                    self.points["RayonUV"] += (5)


    def getTrapSelected(self, event):

        self.trapSelected = not(self.trapSelected)

        element = event.widget.gettags("current")

        if "mushroom" in element and self.points["RayonUV"] >= self.mushUVCost:
            self.trapChoice = "mushroom"
            self.activateMushroom()
        elif "mower" in element and self.points["RayonUV"] >= self.mowerUVCost:
            self.trapChoice = "mower"
            self.parent.vue.gameCanvas.bind("<Button>", self.getMowerPosition)

    def activateMushroom(self):
        if self.trapChoice == "mushroom" and self.trapSelected:
            self.points["RayonUV"] -= self.mushUVCost
            self.mushroomInUse = True
            self.trapSelected = not(self.trapSelected)

    def getMowerPosition(self,evt):
        if self.trapChoice == "mower" and self.trapSelected:
            x = evt.x
            y = evt.y
            self.createMower(x,y)
            self.points["RayonUV"] -= self.mowerUVCost
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
                        self.points["Pointage"] += 1
                        self.points["Engrais"] += 5

    def upgradeChoice(self, event):
        for tower in self.TowerList:
            if event.x >= tower.posX and event.x <= tower.posX + 65 and event.y >= tower.posY and event.y <= tower.posY + 65:
                self.parent.vue.upgradeStats(tower)


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.startLevelMessage = True
        self.creepWave()
        self.vue.root.after(10, self.animate)
        self.vue.root.after(10000, self.addUV)
        self.vue.root.mainloop()

    def setNormalDifficulty(self):
        self.modele.difficulty = "normal"

    def setHardDifficulty(self):
        self.modele.difficulty = "hard"

    def setDifficultyValues(self):

        if self.modele.difficulty == "normal":

            self.modele.creepHealth = Mode.normal["creepHealth"]
            self.modele.bossHealth = Mode.normal["bossHealth"]
            self.modele.points["Engrais"] = Mode.normal["startFertilizer"]

        elif self.modele.difficulty == "hard":

            self.modele.creepHealth = Mode.hard["creepHealth"]
            self.modele.bossHealth = Mode.hard["bossHealth"]
            self.modele.points["Engrais"] = Mode.hard["startFertilizer"]

    def setLifeTen(self):
        self.modele.points["Vie"] = 10


    def setLifeTwenty(self):
        self.modele.points["Vie"] = 20


    def setLifeThirty(self):
        self.modele.points["Vie"] = 30

    def setUpgraded(self):
        self.modele.alreadyUpgraded = not self.modele.alreadyUpgraded


    def setStartY(self):

        firstCheckpoint = self.modele.checkpointList

        return firstCheckpoint[0].y

    def setLastCheckpoint(self):

        map = self.modele.checkpointList
        index = len(map)-1
        lastCheckpoint = map[index]

        return lastCheckpoint.x, lastCheckpoint.y

    def profil(self,name):
      
        if name != None:
            playerStat=score.Score.getProfil(self,name)

            self.modele.playerName = str(playerStat[0])
            self.modele.points["RayonUV"] = int(playerStat[2])

    def creepWave(self):
        if not self.modele.userWon:
            if len(self.modele.creepList) == 0:
                self.modele.createCreep()
                self.modele.points["Wave"] +=1
                self.modele.points["Engrais"] += 50
                if self.modele.points["Wave"] == 5:
                    self.modele.createBoss()


    def nextLevelCheck(self):
        wave = self.modele.points["Wave"]

        if wave == 5 and len(self.modele.creepList) == 0 and self.modele.points["Vie"] > 0:

            if self.modele.currentMap < 3:                  # reset de certaines valeurs pour commencer le prochain niveau

                self.modele.currentMap += 1
                self.modele.points["Wave"] = 0
                self.modele.points["Niveau"] = self.modele.currentMap
                self.modele.currentPoints = self.modele.points["Pointage"]          # pointage courant transféré au prochain niveau
                self.modele.currentFertilizer = self.modele.points["Engrais"]     # engrais et UV courant transféré au prochain niveau (récompense pour bonne stratégie)
                self.modele.currentUV = self.modele.points["RayonUV"]

                if self.modele.difficulty == "normal":
                    self.modele.points["Engrais"] = self.modele.currentFertilizer + Mode.normal["startFertilizer"]
                elif self.modele.difficulty == "hard":
                    self.modele.points["Engrais"] = self.modele.currentFertilizer + Mode.hard["startFertilizer"]



                self.resetLists()                                                                       # listes tower/projectiles/etc cleared

                self.modele.checkpointList = MapCheckpoints.mapCreeps[str(self.modele.currentMap)] 
                self.modele.CheckpointTowers = MapCheckpoints.mapTowers[str(self.modele.currentMap)]     #création des nouveaux checkpoints/start positions
                self.modele.creepStartY = self.setStartY()
                self.modele.bossStartY = self.setStartY() - 60
                self.modele.lastCheckpointX, self.modele.lastCheckpointY = self.setLastCheckpoint()

                self.vue.update()               # update pour que showgame affiche le bon niveau/valeurs au prochain tick
                self.startLevelMessage = True

            else:
                self.userWinsGame()

    def checkGameOver(self):
        if (self.modele.points["Vie"]) <= 0:
            self.gameOver()

    def userWinsGame(self):
        self.modele.userWon = True


    def resetLists(self):
        for tower in self.modele.TowerList:  # on vide tous les arrays de leurs objets pour prochain level

            if tower.projectileList != 0:
                for bullet in tower.projectileList:
                    tower.projectileList.remove(bullet)
                    del bullet

            self.modele.TowerList.remove(tower)
            del tower

        self.modele.TowerList = []

        for trap in self.modele.trapList:
            self.modele.trapList.remove(trap)
            del trap

        for checkpoint in self.modele.checkpointList:
            self.modele.checkpointList.remove(checkpoint)
            del checkpoint

        self.modele.trapList = []
        self.modele.creepList = []
        self.modele.checkpointList = []


    def gameOver(self):
        if not self.modele.gameIsOver:
            score.Score.addScore(self,
                                        self.modele.playerName,
                                        self.modele.points.get("Pointage"),
                                        self.modele.points.get("Wave"),
                                        self.modele.points.get("RayonUV"))
        self.modele.gameIsOver = True


    def addUV(self):
        if self.vue.gameInProg == True:
            self.modele.sunflowerUV()
            self.vue.root.after(20000, self.addUV)


    def animate(self):
        if self.vue.gameInProg == True:
            self.nextLevelCheck()
            self.creepWave()
            self.modele.deathCheck()
            self.modele.creepMovement()
            self.vue.showGame()
            self.vue.update()
            self.checkGameOver()
            self.vue.root.after(25, self.animate)

    def close_window(self):
        self.vue.root.destroy()
            
if __name__ == '__main__':
    c = Controleur()
