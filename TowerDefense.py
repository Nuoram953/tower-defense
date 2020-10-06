##TowerDefense

# Francois Therien
# Nicolas Paquette
# Caroline Emond
# Antoine Auger
# Mikael Korvat

from tkinter import *
import random 


class Vue():  
    def __init__(self, parent, modele):
        self.modele = modele
        self.parent = parent
        self.root = Tk()
        self.root.title("towerDefense")
        self.root.resizable(width = False, height = False)
        self.windowMenu()
        self.gameCanvas = None
        self.gameInProg = False
  
    def windowMenu(self):
      
        self.menuFrame=Frame(self.root, bg = "white")

        welcomeLabel = Label(self.root, text="WELCOME TO BOTANIK PANIK", pady = 20)

        welcomeLabel.pack()

        buttonNewGame = Button(self.menuFrame, text="Nouvelle Partie", command = self.gameMenu)
        buttonOptions = Button(self.menuFrame,text="Options", command  = self.options)
        buttonQuit = Button(self.menuFrame, text="Quitter", command = self.quit)

        buttonNewGame.grid(column=0, row = 0, padx = 200, pady = 20)
        buttonOptions.grid(column=0, row = 1, padx = 200, pady = 20)
        buttonQuit.grid(column=0, row = 2, padx = 200, pady = 20) 

        self.menuFrame.pack()

    def showGame(self):
     
        self.gameCanvas.delete(ALL)

        self.img = PhotoImage(file = "assets/Map #1/grass/map1.1.png")
        self.gameCanvas.create_image(0,0, image = self.img, anchor = NW)

        for i in self.modele.creepList:
            self.gameCanvas.create_oval(i.posX-5,i.posY-5,i.posX+5,i.posY+5, fill = "yellow")

    def gameMenu(self):
        self.menuFrame.pack_forget()
        self.game = Frame(self.root)
        self.game.resizable(width = False, height = False)
       

        self.gameFrame = Frame(game , width  = 1600, height = 800)
        self.gameCanvas = Canvas(self.gameFrame, width = 1300, height = 800)
        self.frameHUD = Frame(self.gameFrame, width = 300, height = 800) 
        
        self.ressourceFrame = Frame(self.frameHUD, bg = "blue", width = 300, height = 100)
        self.towerFrame = Frame(self.frameHUD, bg = "red", width = 300, height = 600)
        self.upgradeFrame = Frame(self.frameHUD, bg = "black", width = 300, height = 100)

        self.gameCanvas.grid(column = 0, row = 0)
        self.frameHUD.grid(column = 1, row = 0)

        self.ressourceFrame.grid(column = 1, row = 0)
        self.towerFrame.grid(column = 1, row = 1)
        self.upgradeFrame.grid(column = 1, row = 2)


        self.gameFrame.pack(expand = YES, fill = BOTH)
        self.game.pack()

        self.gameInProg = True


    def options(self):
        pass

    def quit(self):
        pass             

class Creep():
    def __init__(self,posX,posY,cibleX,cibleY,vitesse):
        self.posX = posX
        self.posY = posY
        self.cibleX = cibleX
        self.cibleY = cibleY
        self.vitesse = vitesse

    def move(self):
        if self.posY == self.cibleY and self.posX <= self.cibleX:
            self.posX += self.vitesse   


class Modele():  
    def __init__(self, parent):
        self.parent = parent
        self.creepList = []

    def createCreep(self):
        self.creepList.append(Creep(10,637,350,637,0.2))  

    def creepMouvment(self):
        for i in self.creepList:
            i.move()    




    


class Controleur():  
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self,self.modele)
        self.creepWave()
        self.vue.root.after(10,self.animate)
        self.vue.root.mainloop()

    def creepWave(self):
        if len(self.modele.creepList) == 0:
            self.modele.createCreep()

                
    def animate(self):
        if self.vue.gameInProg == True:
            self.creepWave()
            self.modele.creepMouvment()
            self.vue.showGame()
            self.vue.root.after(10,self.animate)
             
               

if __name__ == '__main__':
    c = Controleur()  
