#### ---- Importation des modules du projet

# Gestion des interface graphique
from tkinter import *
import tkinter as tk

# Gestion des polices
import tkinter.font as tkFont
from tkinter.font import nametofont

# Customisation graphique des widgets pour un GUI conforme au dernière version du système d'exploitations
from tkinter import ttk

#### ---- Initalisation des variables global

global app
global lang
global mapData
global mapSize
global mapNumber
global adversMapData
global boatData
global playerMap

#### ---- Affectation des variables global

app = tk.Tk()
lang = 1
mapData = []
mapSize = 10
mapNumber = 3
adversMapData = []
boatData = []
playerMap = 1

#### ---- Interaction utilisateur

# Attaquer une position ennemie
def atq(user,map,posX,posY):
    Xcount = 0
    type = mapRead(map,posX,posY)[0]
    if mapData[map-1][posY-1][posX-1][1] != "D":
        mapData[map-1][posY-1][posX-1][1] = "X"
    adversMapData[user-1][map-1] += [[posX,posY,type,mapRead(map,posX,posY)[1]]]
    for i in range(len(mapData[map-1])):
        for j in range(len(mapData[map-1][i])):
            if mapRead(map,i,j)[1] == "X":
                Xcount += 1
    if Xcount > BoatPos(map,type,0):
        mapZoneModifStatus(map,"D",BoatPos(map,type,1),BoatPos(map,type,2),BoatPos(map,type,3),BoatPos(map,type,4))
    
#### ---- Manipulation des maps

# Création des maps
def creatmap():
    mapData.clear()
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

# Modifier le type d"une position
def mapPosModifType(map,modiftype,posX,posY):
    mapData[map-1][posY-1][posX-1][0] = modiftype

# Modifier le status d"une position
def mapPosModifStatus(map,modifstatus,posX,posY):
    mapData[map-1][posY-1][posX-1][1] = modifstatus

# Obtenire les positions de zone d"un élément
def BoatPos(map,type,poschoice):
    pos = [0]
    for i in range(len(mapData[map-1])):
        for j in range(len(mapData[map-1][i])):
            if mapData[map-1][i][j][0] == type:
                pos += j+1,i+1
                pos[0] += 1
    pos = [pos[0],pos[1],pos[2],pos[-2],pos[-1]]
    return pos[poschoice]

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
langDico = [
            # Anglais
            ["Play","Settings","Credit","Exit","Back","Main menu","CUSTOM","Comming soon","/// LAUNCH ///","Select a game mode"],

            # Français
            ["Jouer","Réglage","Crédit","Quitter","Retour","Menu principal","PERSONALISÉ","Prochainement","/// LANCER ///","Sélectionnez un mode de jeu"]]

def lg(text):
    return langDico[lang][langDico[1].index(text)]