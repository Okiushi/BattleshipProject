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
    mapPosModif(map,posX,posY,mapPosRead(map,posX,posY)[0],"X")
    adversMapData[user-1][map-1] += [[posX,posY,mapPosRead(map,posX,posY)[0],mapPosRead(map,posX,posY)[1]]]

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
def mapPosRead(map,posX,posY):
    return mapData[map-1][posY-1][posX-1]

# Modifier une position
def mapPosModif(map,posX,posY,modiftype,modifstatus):
    mapData[map-1][posY-1][posX-1] = [modiftype,modifstatus]

# Modifier une zone de position
def mapZoneModif(map,posX1,posY1,posX2,posY2,modiftype,modifstatus):
    if posX2>posX1:
        for i in range(posX2-posX1+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModif(map,posX1+i,posY1+j,modiftype,modifstatus)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModif(map,posX1+i,posY2+j,modiftype,modifstatus)   
    else:
        for i in range(posX1-posX2+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModif(map,posX2+i,posY1+j,modiftype,modifstatus)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModif(map,posX2+i,posY2+j,modiftype,modifstatus)  

#### ----  Actualisation

# Bientôt








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