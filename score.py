from _datetime import date
import os.path
from os import path


class Score():
     #Vérification si le joueur existe dans le fichier score.csv

    def getProfil(self,namePlayer):

    
        if not path.exists("score.csv"):
            file = open("score.csv", "w+")
            file.close()
        
        playerFound = False
        file = open("score.csv", "r")
        line=file.readlines()
        for player in reversed(line):
            currentPlayer = player.split(",")
            if currentPlayer[0].lower() == namePlayer.lower() and not playerFound:
                playerFound = True
                nom = currentPlayer[0]
                score = currentPlayer[2]
                UV = currentPlayer[4]

        if not playerFound:
            nom = namePlayer
            UV = 0
            score = 0
        file.close()

        return [nom,score,UV]

    def addScore(self,nom,point,level,rayonUV):

        if nom == "":
            nom = "Joueur"

        file = open("score.csv", "a")
        file.write(f"{nom},{str(date.today())},{str(point)},{str(level)},{str(rayonUV)}\n")
        file.close()

 
