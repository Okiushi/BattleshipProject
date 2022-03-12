# --- Imporations des Module

from secrets import choice
from turtle import bgcolor, color
from data import *
from tkinter import ttk # Pour une UI conforme au dernière version du système d'exploitations


# --- Affectation des variables

import tkinter as tk


globalSize = 1
case_size = 40
cases = []

# --- Ajout de la bar d'onglet
window = ttk.Frame(app,height = 10)
window.pack(expand = 1, fill ="both")

# --- Création des pages :

# MainMenu
mainMenuPage = ttk.Frame(window)

# MainParty
mainPartyPage = ttk.Frame(window)

# Start
startPage = ttk.Frame(window)

# MainSettings
mainSettingsPage = ttk.Frame(window)

# --- Élément de la fenêtre

# MainMenu
def itemMainMenuPage():
    menuZone = ttk.Frame(mainMenuPage)
    menuZone.pack()
    bouton_play = ttk.Button(menuZone, text='Play',command=lambda:[mainMenuPage.pack_forget(),mainPartyPage.pack()])
    bouton_play.grid(row = 1, column = 0, ipadx=150, ipady=20)
    bouton_play = ttk.Button(menuZone, text='Settings',command=lambda:[mainMenuPage.pack_forget(),mainPartyPage.pack()])
    bouton_play.grid(row = 2, column = 0, ipadx=150, ipady=20)
    bouton_play = ttk.Button(menuZone, text='Exit',command=lambda:app.destroy())
    bouton_play.grid(row = 3, column = 0, ipadx=150, ipady=20,sticky="")
    
# MainParty
def itemMainPartyPage():
    app.title("Battleship - Party")
    mapZone = ttk.Frame(mainPartyPage, width = 100*globalSize, height = 100*globalSize)
    mapZone.grid(row = 0, column = 0, padx=3, pady=3)
    mapAdversZone = ttk.Frame(mapZone, width = 100*globalSize, height = 100*globalSize)
    mapAdversZone.grid(row = 0, column = 0, padx=3, pady=3)
    for map in range(mapNumber):
        if map == playerMap-1:
            gridecase = Canvas(mapZone, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize)
            gridecase.grid(row = int(map/5) + 2, column = 0,columnspan=mapNumber, padx=100, pady=3)
        else:
            gridecase = Canvas(mapAdversZone, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize)
            gridecase.grid(row = int(map/5), column = map , padx=3, pady=3,)
        for ligne in range(mapSize):
            cases_ligne=[]
            for colonne in range(mapSize):
                cases_ligne.append(gridecase.create_rectangle((colonne*case_size+2)*globalSize, (ligne*case_size+2)*globalSize, ((colonne+1)*case_size+2)*globalSize, ((ligne+1)*case_size+2)*globalSize))
            cases.append(cases_ligne)
        for i in range(mapSize):
            for j in range(mapSize):
                if mapRead(map+1,j+1,i+1)[1] == "D":
                    gridecase.itemconfigure(cases[i][j], outline = "steelblue", fill="steelblue4")
                elif mapRead(map+1,j+1,i+1)[0] != "--" and mapRead(map+1,j+1,i+1)[1] == "X":
                    gridecase.itemconfigure(cases[i][j], outline = "", fill="red")
                elif mapRead(map+1,j+1,i+1)[0] == "--" and mapRead(map+1,j+1,i+1)[1] == "X":
                    gridecase.itemconfigure(cases[i][j], outline = "steelblue",fill="lightcoral")
                elif mapRead(map+1,j+1,i+1)[0] != "--":
                    gridecase.itemconfigure(cases[i][j], outline = "gainsboro",fill="lavender")
                else:
                    gridecase.itemconfigure(cases[i][j], outline = "steelblue",fill="steelblue3")    

    bouton_menu = ttk.Button(mainPartyPage, text='Menu',command=lambda:[mainPartyPage.pack_forget(),mainMenuPage.pack()])
    bouton_menu.grid(row = 1, column = 0, padx=3, pady=3)

# --- Main
def battleship():
    app.title("Battleship")

    # Taille de la fenêtre
    app.minsize(800, 450)
    app.maxsize(app.winfo_screenwidth(),app.winfo_screenheight())
    w  = 800
    h = 450
    x = (app.winfo_screenwidth()/2) - (w/2)
    y = (app.winfo_screenheight()/2) - (h/2)
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # Initialisation des éléments des onglets
    itemMainMenuPage()
    itemMainPartyPage()

    # Ouverture du menu
    mainMenuPage.pack()