from _datetime import date

class Score():
     #Vérification si le joueur existe dans le fichier score.csv
    #TODO: Changer le nom des variables et mettre en argument le nom du joueur
    #TODO: Offrir au joueur la possibilité de refuser de continuer avec son profil si il veux recommencer?
    def getProfil(self, namePlayer):
        playerFound = False
        file = open("score.csv", "r")
        line=file.readlines()
        print(line)
        for player in line:
            currentPlayer = player.split(",")
            if currentPlayer[0].lower() == namePlayer.lower() and not playerFound:
                playerFound = True
                print("YEAH")
                self.nom = currentPlayer[0]
                self.niveau = currentPlayer[3]
                self.sagesse = currentPlayer[4]

        if not playerFound:
            self.nom = 0
            self.niveau = 0
            self.sagesse = 0
        file.close()
    #TODO: Changer le nom des variables
    def score(self):
        file = open("score.csv", "a")
        file.write(f"{self.nom},{str(date.today())},{str(self.point)},{str(self.level)},{str(self.sagesse)}")
        file.close()

 
