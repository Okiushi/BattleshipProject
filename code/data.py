#### ---- Importation des modules

from tkinter import *
import tkinter as tk
from support_tmp import * # + un fichier temporaire pour l'aide au développement

#### ---- Initalisation des variables global

global window
global mapData
global mapSize
global mapNumber
global adversMapData
global boatData

global case_size
global grid_size
global cases

#### ---- Affectation des variables global

window = Tk()
mapData = []
mapSize = 10
mapNumber = 3
adversMapData = []
boatData = []

case_size = 50
grid_size = 10
cases = []

#### ---- Interaction utilisateur

# Attaquer une position ennemie
def atq(user,map,posX,posY):
    mapData[map-1][posY-1][posX-1][1] = "X"
    adversMapData[user-1][map-1] += [[posX,posY,mapRead(map,posX,posY)[0],mapRead(map,posX,posY)[1]]]
    
#### ---- Manipulation des maps

# Création des maps
def creatmap():
    global mapData
    for i in range(mapNumber):
        mapData.append([])
        adversMapData.append([])
        for i2 in range(mapNumber):
            adversMapData[i] += [[]]
        for j in range(mapSize):
            mapData[i] += [[]*mapSize]
            for k in range(mapSize):
                mapData[i][j] += [["--","-"]]

# Lire une position
def mapRead(map,posX,posY):
    return mapData[map-1][posY-1][posX-1]

# Modifier le type d'une position
def mapPosModifType(map,modiftype,posX,posY):
    mapData[map-1][posY-1][posX-1][0] = modiftype

# Modifier le status d'une position
def mapPosModifStatus(map,modifstatus,posX,posY):
    mapData[map-1][posY-1][posX-1][1] = modifstatus

# Obtenire les positions de zone d'un élément
def BoatPos(map,type):
    pos = [0]
    for i in range(len(mapData[map-1])):
        for j in range(len(mapData[map-1][i])):
            if mapData[map-1][i][j][0] == type:
                pos += j+1,i+1
                pos[0] += 1
    return [pos[0],pos[1],pos[2],pos[-2],pos[-1]]

# Modifier le type d'une zone
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

# Modifier le status d'une zone
def mapZoneModifStatus(map,modifstatus,posX1,posY1,posX2,posY2):
    if posX2>posX1:
        for i in range(posX2-posX1+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifType(map,modifstatus,posX1+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifType(map,modifstatus,posX1+i,posY2+j)   
    else:
        for i in range(posX1-posX2+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifType(map,modifstatus,posX2+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifType(map,modifstatus,posX2+i,posY2+j)  

#### ----  Actualisation

# Couler un bateau 
def refreshDeath(map,type):
    Xcount = 0
    for i in range(len(mapData[map-1])):
        for j in range(len(mapData[map-1][i])):
            if mapRead(map,i,j)[1] == "X":
                Xcount += 1
    if Xcount >= BoatPos(map,type)[0]:
        mapZoneModifStatus(map,"DD",BoatPos(map,type)[1],BoatPos(map,type)[2],BoatPos(map,type)[3],BoatPos(map,type)[4])

#### ---- Manipulation de la grilles graphique

# Création de la grille du joueur 1
def creatgrid1():
    for ligne in range(grid_size):
        cases_ligne=[]
        for colonne in range(grid_size):
            cases_ligne.append(gridecase1.create_rectangle(colonne*case_size+2, ligne*case_size+2, (colonne+1)*case_size+2, (ligne+1)*case_size+2))
        cases.append(cases_ligne)

# Création de la grille du joueur 2
def creatgrid2():
    for ligne in range(grid_size):
        cases_ligne=[]
        for colonne in range(grid_size):
            cases_ligne.append(gridecase2.create_rectangle(colonne*case_size+2, ligne*case_size+2, (colonne+1)*case_size+2, (ligne+1)*case_size+2))
        cases.append(cases_ligne)

# --- Affectation des valeurs de la fenetre
gridecase1 = Canvas(window, width = grid_size*case_size+2, height = grid_size*case_size+2, bg = 'lightblue')
gridecase2 = Canvas(window, width = grid_size*case_size+2, height = grid_size*case_size+2, bg = 'lightblue')
lbl1 = Label(window,text="Player 1",bg="black",fg="#EBF2FA")
lbl2 = Label(window,text="Player 2",bg="black",fg="#EBF2FA")

# Voici le morceau de code qui convertira nos lettre en chiffre, il fontionne pour la majuscule et minuscul: " ord(posX.lower())-96 "