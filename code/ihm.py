# --- Imporations des données
from data import *

# Gestion des interfaces graphiques
from tkinter import *
import tkinter as tk

# Modernisation des widgets
from tkinter import ttk

# Gestion des polices
from tkinter.font import *
import tkinter.font as tkFont

# --- Affectation des variables
app = tk.Tk()
# Preset
fullScreen = False
W  = 800
H = 450
globalSize = 1
ennemieMapSelect = 2
#### ---- Ajout des pages

# Page
window = Frame(app)
mainMenuPage = Frame(window)
selectPartyPage = Frame(window)
prePartyPage = Frame(window)
partyPage = Frame(window)
settingsPage = Frame(window)
creditsPage = Frame(window)

# Style du text
titleStyle = tkFont.Font(family="Impact")
default_font = nametofont("TkDefaultFont")

### --- Action de boutton --- ###
def setFullScreen(event):
    global fullScreen
    if fullScreen :
        fullScreen = False
    else:
        fullScreen = True
    app.attributes("-fullscreen", fullScreen) 

# Fonction d'action de fenêtre
def switch(frame):
    for widget in window.winfo_children():
        widget.pack_forget()
    window.pack(expand = 1, fill =BOTH)
    frame.pack(expand = 1, fill =BOTH)

# Redimentionnement

# Selection de la map adverse visible
def selectEnnemieMap(select):
    global ennemieMapSelect
    if select and ennemieMapSelect + 1 == playerMapSelect:
        ennemieMapSelect += 2
    elif select:
        ennemieMapSelect += 1

    elif not select and ennemieMapSelect - 1 == playerMapSelect:
        ennemieMapSelect -= 2
    else:
        ennemieMapSelect -= 1
    refreshGUI()

def selectGameMode(mode):
    global gameMode
    gameMode = mode
    refreshGUI()

def clickEnnemieMap(event):
    atq(playerMapSelect,ennemieMapSelect,event.x//(ennemieMap.winfo_width()//mapSize)+1,event.y//(ennemieMap.winfo_height()//mapSize)+1)
    refreshGUI()

def clickBuild(event):
    addBoat(playerMapSelect,"c1",event.x//(playerMapBuild.winfo_width()//mapSize)+1,event.y//(playerMapBuild.winfo_height()//mapSize)+1,"N",5)
    refreshGUI()

def autoRefreshGUI():
    refreshGUI()
    app.after(50,autoRefreshGUI)

def refreshGUI():

    global titleStyle
    global globalSize
    globalSize = 1 + (app.winfo_height() - 450)*(app.winfo_width() - 800)*0.0000025
    titleStyle.configure(size=int(50*globalSize))
    default_font.configure(family="Arial",size=int(11*(globalSize*0.5+0.5)),weight=BOLD)


    mapZone.place(relx = 0.5, rely = 0.5, relwidth = 1, relheight = 1,anchor = CENTER)
    mapZoneUser.place(relheight=1,relwidth=0.5)
    mapZoneEnnemie.place(relheight=1,relwidth=0.5, relx=0.5)

    playerMapBuild.place(width = 350*globalSize, height = 350*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    playerMap.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    ennemieMap.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    
    if gameMode:
        text_selectGame.config(text=lg("Personalisé"))
        text_selectGame.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.05, anchor = CENTER)
    else:
        text_selectGame.config(text=lg("Standard"))
        text_selectGame.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.05, anchor = CENTER)

    ennemieName.config(text="IA Player "+str(ennemieMapSelect))
    ennemieName.place(height=30,width=50,relheight=0.01,relwidth=0.1,relx=0.52,rely=0.06,x=-10,y=10,anchor = N)

    # Création des cases
    playerMapBuild.delete("all")
    playerMap.delete("all")
    ennemieMap.delete("all")
    
    cases = []
    for i in range(mapSize):
        cases_i=[]
        for j in range(mapSize):
            if mapRead(playerMapSelect,j+1,i+1)[1] == "DD":
                caseColor="black"
            elif mapRead(playerMapSelect,j+1,i+1)[0] != "--" and mapRead(playerMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="red"
            elif mapRead(playerMapSelect,j+1,i+1)[0] == "--" and mapRead(playerMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="steelblue1"
            elif mapRead(playerMapSelect,j+1,i+1)[0] != "--":
                caseColor="lavender"
            else:
                caseColor="steelBlue3"
            cases_i.append(playerMapBuild.create_rectangle((j*(playerMapBuild.winfo_width()/mapSize)), (i*(playerMapBuild.winfo_height()/mapSize)), ((j+1)*(playerMapBuild.winfo_width()/mapSize)-2), ((i+1)*(playerMapBuild.winfo_height()/mapSize)-2),outline=caseColor,fill=caseColor,activeoutline="white",activewidth=1))
        cases.append(cases_i)
    # Map du joueur dans la fenêtre de party
    cases = []
    for i in range(mapSize):
        cases_i=[]
        for j in range(mapSize):
            if mapRead(playerMapSelect,j+1,i+1)[1] == "DD":
                caseColor="black"
            elif mapRead(playerMapSelect,j+1,i+1)[0] != "--" and mapRead(playerMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="red"
            elif mapRead(playerMapSelect,j+1,i+1)[0] == "--" and mapRead(playerMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="steelblue1"
            elif mapRead(playerMapSelect,j+1,i+1)[0] != "--":
                caseColor="lavender"
            else:
                caseColor="steelBlue3"
            cases_i.append(playerMap.create_rectangle((j*(playerMap.winfo_width()/mapSize)), (i*(playerMap.winfo_height()/mapSize)), ((j+1)*(playerMap.winfo_width()/mapSize)-2), ((i+1)*(playerMap.winfo_height()/mapSize)-2),outline=caseColor,fill=caseColor))
        cases.append(cases_i)

    # Map de l'adversaire dans la fenêtre de party
    cases = []
    for i in range(mapSize):
        cases_i=[]
        for j in range(mapSize):
            if mapRead(ennemieMapSelect,j+1,i+1)[1] == "DD":
                caseColor="black"
            elif mapRead(ennemieMapSelect,j+1,i+1)[0] != "--" and mapRead(ennemieMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="red"
            elif mapRead(ennemieMapSelect,j+1,i+1)[0] == "--" and mapRead(ennemieMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="steelblue1"
            else:
                caseColor="steelBlue3"
            cases_i.append(ennemieMap.create_rectangle((j*(ennemieMap.winfo_width()/mapSize)), (i*(ennemieMap.winfo_height()/mapSize)), ((j+1)*(ennemieMap.winfo_width()/mapSize)-2), ((i+1)*(ennemieMap.winfo_height()/mapSize)-2),outline=caseColor,fill=caseColor,activeoutline="white",activewidth=1*globalSize))
        cases.append(cases_i)
    
    
    if mapNumber > 2:
        if ennemieMapSelect + 1 == playerMapSelect:
            button_nextMap.config(text="Player "+str(ennemieMapSelect+2))
        else:
            button_nextMap.config(text="Player "+str(ennemieMapSelect+1))
        if ennemieMapSelect - 1 == playerMapSelect:
            button_backMap.config(text="Player "+str(ennemieMapSelect-2))
        else:
            button_backMap.config(text="Player "+str(ennemieMapSelect-1))

        if ennemieMapSelect < mapNumber and not (playerMapSelect == mapNumber and ennemieMapSelect+1 == mapNumber):
            button_nextMap.place(height=30,width=50,relheight=0.025,relwidth=0.1,relx=0.9,rely=0.05,x=-10,y=10,anchor = NE)
        else:
            button_nextMap.place_forget()
        if ennemieMapSelect > 1 and not (playerMapSelect == 1 and ennemieMapSelect-1 == 1):
            button_backMap.place(height=30,width=50,relheight=0.025,relwidth=0.1,relx=0.1,rely=0.05,x=10,y=10)
        else:
            button_backMap.place_forget()
    else:
        button_nextMap.place_forget()
        button_backMap.place_forget()
            

text_gameTitle = Label(mainMenuPage,text="BATTLESHIP WARFARE",fg="black",font=titleStyle)
text_gameTitle.place(relx = 0.5, rely = 0.45, anchor = S)

button_play = ttk.Button(mainMenuPage, text=lg("Jouer"),command=lambda:[switch(selectPartyPage)])
button_play.place(height=20,relheight=0.05,relwidth=0.25,relx = 0.5, rely = 0.55,y=-20, anchor = CENTER)

button_settings = ttk.Button(mainMenuPage, text=lg("Réglage"),command=lambda:switch(settingsPage))
button_settings.place(height=20,relheight=0.05, relwidth=0.25,relx = 0.5, rely = 0.6, anchor = CENTER)

button_credit = ttk.Button(mainMenuPage, text=lg("Crédit"),command=lambda:switch(creditsPage))
button_credit.place(height=20,relheight=0.05, relwidth=0.25,relx = 0.5, rely = 0.65,y=20, anchor = CENTER)

button_exit = ttk.Button(mainMenuPage, text=lg("Quitter"),command=lambda:app.destroy())
button_exit.place(height=15,relheight=0.05, relwidth=0.1,relx=1,rely=1,x=-10,y=-10,anchor = SE)

# Settings

button_back = ttk.Button(settingsPage, text=lg("Retour"),command=lambda:switch(mainMenuPage))
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)
text_musique = Label(settingsPage,text="Musique",bg="black",fg="white",font='Helvetica')
text_musique.place(height=50,width=125, x= 100,y=100)
text_son = Label(settingsPage,text="Volume",bg="black",fg="white",font='Helvetica')
text_son.place(height=50,width=125,x =100,y=200)
text_son = Label(settingsPage,text="Langue",bg="black",fg="white",font='Helvetica')
text_son.place(height=50,width=125,x =100,y=300)
slider = ttk.Scale(settingsPage,from_=0, to=100,orient=HORIZONTAL,length=300)
slider.place(x=300,y=200)

# Valeur pour "Activer" => var1; valeur pour "Desactiver" => var2
var1= IntVar()
var2= IntVar()
# Case Activer/Desctiver
case_active = tk.Checkbutton(settingsPage, text='Activer',variable=var1, onvalue=1, offvalue=0)
case_active.place(height=50,width=125,x=250,y=100)
case_desactive= tk.Checkbutton(settingsPage, text='Desactiver',variable=var2, onvalue=1, offvalue=0)
case_desactive.place(height=50,width=125,x=375,y=100)
# Case Langue
# Valeur pour "Activer" => var1; valeur pour "Desactiver" => var2
var3= IntVar()
var4= IntVar()

case_anglais = tk.Checkbutton(settingsPage, text='Anglais',variable=lang, onvalue=0, offvalue=1)
case_anglais.place(height=50,width=125,x=375,y=300)
case_francais = tk.Checkbutton(settingsPage, text='Français',variable=lang, onvalue=1,offvalue=0)
case_francais.place(height=50,width=125,x=250,y=300)

# Credits

button_back = ttk.Button(creditsPage, text=lg("Retour"),command=lambda:switch(mainMenuPage))
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

text_commingSoon = Label(creditsPage,text=lg("Prochainement"),bg="black",fg="white")
text_commingSoon.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.5, anchor = CENTER)

# Select Party

text_selectGame = Label(selectPartyPage,text=lg("Sélectionnez un mode de jeu"),fg="black")
text_selectGame.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.05, anchor = CENTER)

button_selectIAGame = ttk.Button(selectPartyPage, text=lg("Standard").upper(),command=lambda:[gamePreset(),switch(prePartyPage),selectGameMode(0)])
button_selectIAGame.place(relwidth=0.4, relheight=0.75,relx = 0.3, rely = 0.475, anchor = CENTER)

button_selectCustomGame = ttk.Button(selectPartyPage, text=lg("Personalisé").upper(),command=lambda:[switch(prePartyPage),selectGameMode(1)])
button_selectCustomGame.place(relwidth=0.4, relheight=0.75,relx = 0.7, rely = 0.475, anchor = CENTER)

button_back = ttk.Button(selectPartyPage, text=lg("Retour"),command=lambda:switch(mainMenuPage))
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

# Pre-Party

playerMapBuild = Canvas(prePartyPage,bg="steelBlue4",cursor="crosshair")

text_selectGame = Label(prePartyPage,fg="black")

button_back = ttk.Button(prePartyPage, text=lg("Retour"),command=lambda:switch(selectPartyPage))
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

button_launchGame = ttk.Button(prePartyPage, text=lg("/// LANCER ///"),command=lambda:[laucheGame(),switch(partyPage),refreshGUI()])
button_launchGame.place(height=50,width=100,relheight=0.05,relwidth=0.1,relx=1,rely=1,x=-10,y=-10,anchor = SE)

# Party

mapZone = Frame(partyPage)
mapZoneUser = Frame(mapZone)
mapZoneEnnemie = Frame(mapZone)
playerMap = Canvas(mapZoneUser,bg="steelBlue4",cursor="crosshair")
ennemieMap = Canvas(mapZoneEnnemie,bg="steelBlue4", highlightcolor="white",cursor="none")
ennemieName = Label(mapZoneEnnemie)

button_backToMainMenu = ttk.Button(partyPage, text=lg("Menu principal"),command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=30,width=75,relheight=0.025,relwidth=0.1,relx=0,rely=1,x=10,y=-10,anchor = SW)

button_nextMap = ttk.Button(mapZoneEnnemie, text="Player "+str(ennemieMapSelect+1),command=lambda:selectEnnemieMap(1))
button_backMap = ttk.Button(mapZoneEnnemie, text="Player "+str(ennemieMapSelect-1),command=lambda:selectEnnemieMap(0))

### --- Main execution --- ###

def battleship():
    app.title("Battleship Warfare")
    app.minsize(800, 450)
    app.maxsize(app.winfo_screenwidth(),app.winfo_screenheight())
    app.geometry('%dx%d+%d+%d' % (W, H, (app.winfo_screenwidth()/2) - (W/2), (app.winfo_screenheight()/2) - (H/2)))
    # Ouverture du menu
    switch(mainMenuPage)
    app.after(1,refreshGUI)