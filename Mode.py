normal = {
    "perSunflowerUV":5,
    "creepHealth": 40,
    "bossHealth": 120,
    "startFertilizer": 75,

}

hard = {
    "perSunflowerUV":2,
    "creepHealth": 55,
    "bossHealth": 145,
    "startFertilizer": 65,

}

# dans modele
# self.difficulty = normal de base
# self.userDifficulty = normal de base

# dans options
# fonction qui modifie self.userDifficulty selon choix
# def setDifficulty(self, event)
    # element = event.widget.gettags.....
    # if "normal" in element:
        #self.modele.userDifficulty = "normal"
    # elif "hard" in element:
        #self.modele.userDifficulty = "hard"
    # elif "back" in element:
        #retour à windowMenu

# dans vue (au tout début de gameWindow maybe)
#fonction qui set difficulté choisie pour la game
#def setCurrentDifficulty(self)
    #if self.modele.difficulty != self.modele.userDifficulty:
        #self.modele.difficulty = self.modele.userDifficulty

    #self.modele.setValues()

# dans modele
# fonction qui set les valeurs selon difficulté choisie
#def setValues(self)
    #if self.currentDifficulty == "normal":
        #self.perSunflowerUV = Mode.normal["perSunflowerUV"]
        #self.creepHealth = Mode.normal["creepHealth"]
        #self.bossHealth = Mode.normal["bossHealth"]
        #self.startFertilizer = Mode.normal["startFertilizer"]
    #elif self.currentDifficulty == "hard":
        #self.perSunflowerUV = Mode.hard["perSunflowerUV"]
        #self.creepHealth = Mode.hard["creepHealth"]
        #self.bossHealth = Mode.hard["bossHealth"]
        #self.startFertilizer = Mode.hard["startFertilizer"]


