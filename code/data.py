#--- Importation des modules
from tkinter import *
from support_tmp import * # + un fichier temporaire pour l'aide au développement

# --- Initalisation des variables global
global window   # (anciennement root) Variable contenant le fenetre
global case_size    # Largeur graphique d'une case
global grid_size    # Nombre de case
global cases    # Liste contenant l'état de toute les positions des deux grille

# --- Affectation des variables global
window = Tk()
case_size = 50
grid_size = 10
cases = []

# --- Affectation des valeurs de la fenetre
gridecase1 = Canvas(window, width = grid_size*case_size+2, height = grid_size*case_size+2, bg = 'lightblue')
gridecase2 = Canvas(window, width = grid_size*case_size+2, height = grid_size*case_size+2, bg = 'lightblue')
lbl1 = Label(window,text="  Player  ",bg="blue",fg="#EBF2FA")
lbl2 = Label(window,text="  Computer  ",bg="red",fg="#EBF2FA")

# --- Outils de manipulation des données

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