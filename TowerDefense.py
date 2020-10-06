##TowerDefense

# Francois Therien
# Nicolas Paquette
# Caroline Emond
# Antoine Auger
# Mikael Korvat

from tkinter import *
import random 


class Vue():  
    def __init__(self, modele, parent):
        self.modele = modele
        self.parent = parent
        self.root = Tk()
        self.root.title("towerDefense")
        self.root.resizable(width = False, height = False)
        self.windowMenu()
        self.gameCanvas = None

  
    def windowMenu(self):
      
        self.menuFrame=Frame(self.root, bg = "white")

        welcomeLabel = Label(self.root, text="WELCOME TO BOTANIK PANIK", pady = 20)

        welcomeLabel.pack()

        buttonNewGame = Button(self.menuFrame, text="Nouvelle Partie", command = self.newGame)
        buttonOptions = Button(self.menuFrame,text="Options", command  = self.options)
        buttonQuit = Button(self.menuFrame, text="Quitter", command = self.quit)

        buttonNewGame.grid(column=0, row = 0, padx = 200, pady = 20)
        buttonOptions.grid(column=0, row = 1, padx = 200, pady = 20)
        buttonQuit.grid(column=0, row = 2, padx = 200, pady = 20) 

        self.menuFrame.pack()

    def newGame(self):
        self.game = Toplevel()
        self.game.resizable(width = False, height = False)
        self.root.withdraw()

        self.gameFrame = Frame(self.game , width  = 1600, height = 1200)
        self.gameCanvas=Canvas(self.gameFrame, width = 1400, height = 1200)
        self.frameHUD = Frame(self.gameFrame, width = 400, height = 1200) 
        
        self.ressourceFrame=Frame(self.frameHUD, bg = "blue", width = 400, height = 400)
        self.towerFrame=Frame(self.frameHUD, bg = "red", width = 400, height = 400)
        self.upgradeFrame=Frame(self.frameHUD, bg = "black", width = 400, height = 400)

        self.gameCanvas.grid(column = 0, row = 0)
        self.frameHUD.grid(column = 1, row = 0)

        self.ressourceFrame.grid(column = 1, row = 0)
        self.towerFrame.grid(column = 1, row = 1)
        self.upgradeFrame.grid(column = 1, row = 2)


        self.gameFrame.pack(expand = YES, fill = BOTH)

        self.img  = PhotoImage(file = "assets/Map #1/grass/map1.1.png")
        self.gameCanvas.create_image(0,0, image = self.img, anchor = NW)
    

    def options(self):
        pass

    def quit(self):
        pass    






class Modele():  
    def __init__(self, parent):
        self.parent = parent


class Controleur():  
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self,self.modele)
        self.vue.root.mainloop()

if __name__ == '__main__':
    c = Controleur()  
