# --- Imporations des Module

from data import *
def newparty():
    creatgrid1()
    creatgrid2()
    showplayscreen()

# --- écran de partie

def showplayscreen():
    window.title('Battleship')
    gridecase1.grid(row = 0, column = 0, padx=3, pady=3)
    gridecase2.grid(row = 0, column = 1, padx=3, pady=3)
    lbl1.grid(row=1,column=0,sticky=N)
    lbl2.grid(row=1,column=1,sticky=N)

# --- écran de menu

def showmenuscreen():
    window.title('Battleship')
    menubar = Menu(window)
    window.config(menu=menubar)
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