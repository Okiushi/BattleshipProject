# --- Imporations des Module

from data import *

# --- Affectation des variables global

globalSize = 1
case_size = 40
cases = []

def creatgrid():
    for map in range(mapNumber):
        gridecase = Canvas(app, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize, bg = "lightblue")
        if map == playerMap-1:
            gridecase.grid(row = 1, column = 0,columnspan=mapNumber, padx=3, pady=3)
        else:
            gridecase.grid(row = 0, column = map, padx=3, pady=3)
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

# --- Élément de la fenêtre

def battleship():
    app.title("Battleship")
    creatgrid()
    menubar = Menu(app)
    app.config(menu=menubar)
    menu_selection = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Jouer", menu=menu_selection)

    menu_selection.add_command(label="Standard contre l'IA ")
    menu_selection.add_command(label="Standard contre un joueur")
    menu_selection.add_command(label="Personalisé")

    menu_settings= Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "Réglage", menu=menu_settings)
    menu_stats= Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "Stats", menu=menu_stats)
    menu_credit= Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "Support", menu=menu_credit)