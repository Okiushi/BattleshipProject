#### ---- Importation des modules du projet

from random import randint
from support_tmp import *

#### ---- Initalisation des variables global

#### ---- Affectation des variables global

mapData = []
atqHistory = []
boatData = []
gameDataBoat = []

lang = 1
mapSize = 10
playerMapSelect = 1
mapNumber = 1000
gameMode = 0

def gamePreset():
    global mapSize
    global mapNumber
    global playerMapSelect
    global gameDataBoat
    mapSize = 10
    mapNumber = 1000
    playerMapSelect = 1
    gameDataBoat = [["a1",5],["c1",4],["f1",3],["s1",3],["p1",2]]

#### ---- Interaction utilisateur

# Attaquer une position ennemie
def addBoat(map,type,x,y,direction,size):
    size -= 1
    noBoat = 1
    if direction == "N":
        x2 = x
        y2 = y
        y -= size
    elif direction == "S":
        x2 = x
        y2 = y + size
    elif direction == "W":
        x2 = x
        x -= size
        y2 = y
    elif direction == "E":
        x2 = x + size
        y2 = y
    else:
        x2 = x + size
        y2 = y

    if x>0 and x2<mapSize+1 and y>0 and y2<mapSize+1:
        for i in range(x,x2+1):
            for j in range(y,y2+1):
                if mapRead(map,i,j)[0] != "--":
                    noBoat = 0

        if not type in boatData[map-1] and noBoat:
            mapZoneModifType(map,type,x,y,x2,y2)
            boatData[map-1] += [type]

def atq(user,map,posX,posY):
    type = mapRead(map,posX,posY)[0]
    if mapData[map-1][posY-1][posX-1][1] != "DD":
        mapData[map-1][posY-1][posX-1][1] = "X"+str(user)
    if not [posX,posY,type,mapRead(map,posX,posY)[1]] in atqHistory[user-1][map-1]:
        atqHistory[user-1][map-1] += [[posX,posY,type,mapRead(map,posX,posY)[1]]]
    refreshAllDeaths()
# mapRead(map,i,j)[1][0] == "X" and mapRead(map,i,j)[0] == type:

def refreshAllDeaths():
    for map in range(len(mapData)):
        for boat in range(len(boatData[map])):
            counter = 0
            for x in range(len(mapData[map])):
                for y in range(len(mapData[map][x])):
                    if boatData[map][boat] == mapRead(map+1,x,y)[0] and mapRead(map+1,x,y)[1][0] == "X":
                        counter += 1
            if counter >= BoatReadPos(map+1,boatData[map][boat])[0]:
                mapZoneModifStatus(map+1,"DD",BoatReadPos(map+1,boatData[map][boat])[1],BoatReadPos(map+1,boatData[map][boat])[2],BoatReadPos(map+1,boatData[map][boat])[3],BoatReadPos(map+1,boatData[map][boat])[4])

#### ---- Gestion des presets de party


#### ---- Manipulation des maps


# Création des maps
def creatmap():
    mapData.clear()
    atqHistory.clear()
    boatData.clear()
    for i in range(mapNumber):
        mapData.append([])
        atqHistory.append([])
        boatData.append([])
        for i2 in range(mapNumber):
            atqHistory[i] += [[]]
        for j in range(mapSize):
            mapData[i] += [[]*mapSize]
            for k in range(mapSize):
                mapData[i][j] += [["--","--"]]

# Lire une position
def mapRead(map,posX,posY):
    return mapData[map-1][posY-1][posX-1]

# Modifier le type d"une position
def mapPosModifType(map,modiftype,posX,posY):
    mapData[map-1][posY-1][posX-1][0] = modiftype

# Modifier le status d"une position
def mapPosModifStatus(map,modifstatus,posX,posY):
    mapData[map-1][posY-1][posX-1][1] = modifstatus

# Obtenire les positions de zone d"un élément
def BoatReadPos(map,type):
    pos = [0]
    for i in range(len(mapData[map-1])):
        for j in range(len(mapData[map-1][i])):
            if mapData[map-1][i][j][0] == type:
                pos += j+1,i+1
                pos[0] += 1
    if len(pos) >= 5:
        pos = [pos[0],pos[1],pos[2],pos[-2],pos[-1]]
    return pos

# Modifier le type d"une zone
def mapZoneModifType(map,modiftype,posX1,posY1,posX2,posY2):
    if posX2>posX1:
        for i in range(posX2-posX1+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifType(map,modiftype,posX1+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifType(map,modiftype,posX1+i,posY2+j)   
    else:
        for i in range(posX1-posX2+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifType(map,modiftype,posX2+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifType(map,modiftype,posX2+i,posY2+j)  

# Modifier le status d"une zone
def mapZoneModifStatus(map,modifstatus,posX1,posY1,posX2,posY2):
    if posX2>posX1:
        for i in range(posX2-posX1+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifStatus(map,modifstatus,posX1+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifStatus(map,modifstatus,posX1+i,posY2+j)   
    else:
        for i in range(posX1-posX2+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifStatus(map,modifstatus,posX2+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifStatus(map,modifstatus,posX2+i,posY2+j)  
                    
# Voici le morceau de code qui convertira nos lettre en chiffre, il fontionne pour la majuscule et minuscul: " ord(posX.lower())-96 "


# Gestion de la langue
def lg(text):
    return langDico[lang][langDico[1].index(text)]

langDico = [# Anglais
            ["Play","Settings","Credit","Exit","Back","Main menu","Standard","Custom","Comming soon","/// LAUNCH ///","Select a game mode","Next","Back"],

            # Français
            ["Jouer","Réglage","Crédit","Quitter","Retour","Menu principal","Standard","Personalisé","Prochainement","/// LANCER ///","Sélectionnez un mode de jeu","Suivant","Précédent"]]

def IA1creatMap(map):
    direction = "NSEW"
    for boat in range(len(gameDataBoat)):
        while not gameDataBoat[boat][0] in boatData[map-1]:
            addBoat(map,gameDataBoat[boat][0],randint(1,mapSize),randint(1,mapSize),direction[randint(0,3)],gameDataBoat[boat][1])

def laucheGame():
    for i in range(mapNumber):
        if i != playerMapSelect:
            IA1creatMap(i)

