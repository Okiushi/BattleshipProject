# --- Imporations des Module

from secrets import choice
from data import *
from tkinter import ttk # Pour une UI conforme au dernière version du système d'exploitations

# --- Affectation des variables global

globalSize = 1
case_size = 40
cases = []

# --- Ajout de la bar d'onglet
tabBar = ttk.Frame(app,height = 10)
tabBar.pack(expand = 1, fill ="both")

# --- Création des pages :

# MainMenu
mainMenuPage = ttk.Frame(tabBar)

# MainParty
mainPartyPage = ttk.Frame(tabBar,height = 300)

# Start
startPage = ttk.Frame(tabBar)

# MainSettings
mainSettingsPage = ttk.Frame(tabBar)

# --- Élément de la fenêtre

# MainMenu
def itemMainMenuPage():
    bouton_play = ttk.Button(mainMenuPage, text='Play',command=lambda:[mainMenuPage.pack_forget(),mainPartyPage.pack()])
    bouton_play.grid(row = 1, column = 0, padx=3, pady=3)

# MainParty
def itemMainPartyPage():
    app.title("Battleship - Party")
    mapZone = Canvas(mainPartyPage, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize)
    mapZone.grid(row = 0, column = 0, padx=3, pady=3)
    for map in range(mapNumber):
        if map == playerMap-1:
            gridecase = Canvas(mapZone, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize)
            gridecase.grid(row = int(map/5) + 2, column = 0,columnspan=mapNumber, padx=100, pady=3)
        else:
            gridecase = Canvas(mapZone, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize)
            gridecase.grid(row = int(map/5), column = map , padx=3, pady=3)
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
    # Initialisation des éléments des onglets
    itemMainMenuPage()
    itemMainPartyPage()

    # Ouverture du menu
    mainMenuPage.pack()