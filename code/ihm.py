# --- Imporations des Module
from data import *

def newparty():
    creatgrid1()
    creatgrid2()
    showplayscreen()

# --- écran de partie
def showplayscreen():
    window.title('BATTLESHIP ・ In game')
    gridecase1.grid(row = 0, column = 0, padx=3, pady=3)
    gridecase2.grid(row = 0, column = 1, padx=3, pady=3)
    lbl1.grid(row=1,column=0,sticky=N)
    lbl2.grid(row=1,column=1,sticky=N)

# --- écran de menu
def showmenuscreen():
    window.title('BATTLESHIP ・ Mainmenu')