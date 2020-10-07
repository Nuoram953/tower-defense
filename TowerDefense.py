
##TowerDefense

# Francois Therien
# Nicolas Paquette
# Caroline Emond
# Antoine Auger
# Mikael Korvat

from tkinter import *
import random
import MapCheckpoints

#test

class Vue():
    def __init__(self, parent, modele):
        self.modele = modele
        self.parent = parent
        self.root = Tk()
        self.root.title("towerDefense")
        #self.root.resizable(width=False, height=False)
        self.windowMenu()
        self.game = None
        self.gameCanvas = None
        self.gameFrame = None
        self.img = None
        self.gameInProg = False

    def windowMenu(self):
        self.menuFrame = Frame(self.root, bg="white")

        self.welcomeLabel = Label(self.root, text="WELCOME TO BOTANIK PANIK", pady=20)

        self.welcomeLabel.pack()

        buttonNewGame = Button(self.menuFrame, text="Nouvelle Partie", command=self.gameWindow)
        buttonOptions = Button(self.menuFrame, text="Options", command=self.options)
        buttonQuit = Button(self.menuFrame, text="Quitter", command=self.quit)

        buttonNewGame.grid(column=0, row=0, padx=200, pady=20)
        buttonOptions.grid(column=0, row=1, padx=200, pady=20)
        buttonQuit.grid(column=0, row=2, padx=200, pady=20)

        self.menuFrame.pack()

    def showGame(self):

        self.gameCanvas.delete(ALL)

        self.img = PhotoImage(file="assets/Map #1/grass/map1.1.png")

        self.gameCanvas.create_image(0, 0, image=self.img, anchor=NW)

        for i in self.modele.creepList:
            self.gameCanvas.create_image(i.posX-(i.width/2),i.posY-(i.height/2),image=i.zombie, anchor=NW)

    def gameWindow(self):
        self.menuFrame.pack_forget()
        self.welcomeLabel.pack_forget()
        self.game = Frame(self.root)
        #self.game.resizable(width=False, height=False)

        self.gameFrame = Frame(self.game, width=1600, height=800)
        self.gameCanvas = Canvas(self.gameFrame, width=1300, height=800)
        self.frameHUD = Frame(self.gameFrame, width=300, height=800)

        self.ressourceFrame = Frame(self.frameHUD, bg="blue", width=300, height=100)
        self.towerFrame = Frame(self.frameHUD, bg="red", width=300, height=600)
        self.upgradeFrame = Frame(self.frameHUD, bg="black", width=300, height=100)

        self.gameCanvas.grid(column=0, row=0)
        self.frameHUD.grid(column=1, row=0)

        self.ressourceFrame.grid(column=1, row=0)
        self.towerFrame.grid(column=1, row=1)
        self.upgradeFrame.grid(column=1, row=2)

        self.gameFrame.pack(expand=YES, fill=BOTH)
        self.game.pack()
        self.gameInProg = True
        self.parent.animate()

    def options(self):
        pass

    def quit(self):
        pass

    

class Creep1():
    def __init__(self, parent, posX, posY, currentCheckpoint):
        self.posX = posX
        self.posY = posY
        self.parent = parent
        self.currentCheckpoint = currentCheckpoint
        self.cibleX = self.currentCheckpoint.x
        self.cibleY = self.currentCheckpoint.y
        self.vitesse = 10
        self.buffer = 5
        self.height = 100
        self.width = 90
        self.listImage = ["assets/zombies/zombie1.png", "assets/zombies/zombie2.png", "assets/zombies/zombie3.png","assets/zombies/zombie4.png","assets/zombies/zombie5.png","assets/zombies/zombie6.png"]
        self.zombie = PhotoImage(file=random.choice(self.listImage))
        self.reachedEnd = False

        if round(self.posX,-1) != round(self.cibleX,-1):
            self.moveHorizontal = True
        elif self.posY > self.cibleY:
            self.moveHorizontal = False
            self.moveUp = True
        else:
            self.moveHorizontal = False
            self.moveUp = False

    def move(self):
        if self.moveHorizontal:
            if self.posX < self.cibleX:
                self.posX += self.vitesse
            else:
                self.updateTargetPosition()
        else:
            if self.moveUp:
                if self.posY > self.cibleY:
                    self.posY -= self.vitesse
                else:
                    self.updateTargetPosition()
            else:
                if self.posY < self.cibleY:
                    self.posY += self.vitesse
                else:
                    self.updateTargetPosition()
                  

    def updateTargetPosition(self):
        if (self.posX >= 1400 and self.posY >= 655):
            print("REACHED THE END!")
            self.reachedEnd = True

        else:
            self.currentCheckpoint = self.parent.getNextCheckpoint(self.currentCheckpoint)
            self.cibleX = self.currentCheckpoint.x
            self.cibleY = self.currentCheckpoint.y

            if round(self.posX, -1) != round(self.cibleX, -1):
                print("MoveHorizontal")
                self.moveHorizontal = True
            elif self.posY > self.cibleY:
                print("MoveVertical UP")
                self.moveHorizontal = False
                self.moveUp = True
            else:
                print("MoveVertical DOWN")
                self.moveHorizontal = False
                self.moveUp = False


class Creep2():
    def __init__(self, parent, posX, posY, currentCheckpoint):
        self.posX = posX
        self.posY = posY
        self.parent = parent
        self.currentCheckpoint = currentCheckpoint
        self.cibleX = self.currentCheckpoint.x
        self.cibleY = self.currentCheckpoint.y
        self.vitesse = 5
        self.buffer = 5
        self.height = 100
        self.width = 63
        self.zombie = PhotoImage(file="assets/zombies/zombie2.png")
        self.reachedEnd = False

        if round(self.posX, -1) != round(self.cibleX, -1):
            self.moveHorizontal = True
        elif self.posY > self.cibleY:
            self.moveHorizontal = False
            self.moveUp = True
        else:
            self.moveHorizontal = False
            self.moveUp = False

    def move(self):
        if self.reachedEnd:
            self.vitesse = 0
        elif self.moveHorizontal:
            if self.posX < self.cibleX:
                self.posX += self.vitesse
            else:
                self.updateTargetPosition()
        else:
            if self.moveUp:
                if self.posY > self.cibleY:
                    self.posY -= self.vitesse
                else:
                    self.updateTargetPosition()
            else:
                if self.posY < self.cibleY:
                    self.posY += self.vitesse
                else:
                    self.updateTargetPosition()

    def updateTargetPosition(self):
        if (self.posX >= 1400 and self.posY >= 655):
            print("REACHED THE END!")
            self.reachedEnd = True
        else:
            self.currentCheckpoint = self.parent.getNextCheckpoint(self.currentCheckpoint)
            self.cibleX = self.currentCheckpoint.x
            self.cibleY = self.currentCheckpoint.y

            if round(self.posX, -1) != round(self.cibleX, -1):
                print("MoveHorizontal")
                self.moveHorizontal = True
            elif self.posY > self.cibleY:
                print("MoveVertical UP")
                self.moveHorizontal = False
                self.moveUp = True
            else:
                print("MoveVertical DOWN")
                self.moveHorizontal = False
                self.moveUp = False



class Checkpoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Checkpoint):
            return self.x == other.x and self.y == other.y
        return False


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.creepList = []
        self.checkpointList = MapCheckpoints.map[1]
        print(self.checkpointList)


    def createCreep(self):
        self.creepList.append(Creep1(self, 10, 630, self.checkpointList[0]))
        self.creepList.append(Creep2(self, 10, 630, self.checkpointList[0]))

    def creepMovement(self):
        for i in self.creepList:
            i.move()

    def getNextCheckpoint(self, currentCheckpoint):
        currentIndex = self.checkpointList.index(currentCheckpoint)
        print(currentIndex)
        checkpointList_len = len(self.checkpointList) - 1
        print(checkpointList_len)
        if currentIndex < checkpointList_len:
            return self.checkpointList[currentIndex+1]
        else:
            pass

    def deathCheck(self):
        for i in self.creepList:
            if i.reachedEnd:
                self.creepList.remove(i)
                del i
                
            #if shot  
    

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
            self.modele.creepMovement()
            self.modele.deathCheck()
            self.vue.showGame()
            self.vue.root.after(10, self.animate)

   
        


if __name__ == '__main__':
    c = Controleur()
