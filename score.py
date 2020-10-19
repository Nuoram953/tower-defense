from _datetime import date

class Score():
     #Vérification si le joueur existe dans le fichier score.csv
    #TODO: Changer le nom des variables et mettre en argument le nom du joueur
    #TODO: Offrir au joueur la possibilité de refuser de continuer avec son profil si il veux recommencer?
    def getProfil(self,namePlayer):

        try:
            file = open("score.csv")
            file.close()
        except:
            print("Le fichier n'existe pas.")


        playerFound = False
        file = open("score.csv", "r")
        line=file.readlines()
        print(line)
        for player in line:
            currentPlayer = player.split(",")
            if currentPlayer[0].lower() == namePlayer.lower() and not playerFound:
                playerFound = True
                print("YEAH")
                nom = currentPlayer[0]
                niveau = currentPlayer[3]
                UV = currentPlayer[4]

        if not playerFound:
            nom = namePlayer
            niveau = 0
            UV = 0
        file.close()

        return [nom,niveau,UV]
    #TODO: Changer le nom des variables
    def score(self,nom,point,level,sagessse):
        file = open("score.csv", "a")
        file.write(f"{nom},{str(date.today())},{str(point)},{str(level)},{str(sagesse)}")
        file.close()

 
