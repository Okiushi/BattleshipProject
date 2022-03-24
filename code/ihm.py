# --- Importation des bibliothèque

# Imporations des données
from data import *

# Gestion des interfaces graphiques
from tkinter import *
import tkinter as tk

# Modernisation des widgets
from tkinter import ttk

# Gestion des polices
from tkinter.font import *
import tkinter.font as tkFont

# Gestion des images
from PIL import ImageTk, Image

# --- Affectation des variables
app = tk.Tk()

# Preset
fullScreen = False
W  = 800
H = 450
globalSize = 1
ennemieMapSelect = 2
buildBoatDirection = 0
buildBoatSelected = ""
mouseX = 0
mousY = 0
inBuildMap = False

# --- Page
window = Frame(app)
mainMenuPage = Frame(window)
selectPartyPage = Frame(window)
prePartyPage = Frame(window)
partyPage = Frame(window)
settingsPage = Frame(window)
creditsPage = Frame(window)

# --- Style du text
titleStyle = tkFont.Font(family="Impact")
default_font = nametofont("TkDefaultFont")

# --- Ajout des images

# Frégate
img_Aboat = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_N.png").resize((100//6,500//6), Image.ANTIALIAS))
img_Cboat = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_N.png").resize((100//6,500//6), Image.ANTIALIAS))

img_Fboat_N = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_N.png").resize((100//6,500//6), Image.ANTIALIAS))
img_Fboat_E = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_E.png").resize((500//6,100//6), Image.ANTIALIAS))
img_Fboat_S = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_S.png").resize((100//6,500//6), Image.ANTIALIAS))
img_Fboat_W = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_W.png").resize((500//6,100//6), Image.ANTIALIAS))

img_Sboat = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_N.png").resize((100//6,500//6), Image.ANTIALIAS))
img_Pboat = ImageTk.PhotoImage(Image.open("../gui/image/Fboat_N.png").resize((100//6,500//6), Image.ANTIALIAS))

### --- Action de boutton --- ###

def setFullScreen(event):
    global fullScreen
    if fullScreen :
        fullScreen = False
    else:
        fullScreen = True
    app.attributes("-fullscreen", fullScreen) 

def laucheGame():
    for i in range(mapNumber):
        if i != playerMapSelect:
            IA1creatMap(i)
    switch(partyPage)
    refreshGUI()

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

def changeBoatDirection(event):
    global buildBoatDirection
    if buildBoatDirection < 3:
        buildBoatDirection += 1
    else:
        buildBoatDirection = 0

def changeInBuildMap(value):
    global inBuildMap
    inBuildMap = value

def boatSelect(type):
    global buildBoatSelected
    global buildBoatDirection
    buildBoatDirection = 0

    buildBoatSelected = ""
    if boatDataTypeCount(type,playerMapSelect) != gameDataBoat.count(type):
        buildBoatSelected = type

def selectGameMode(mode):
    global gameMode
    gameMode = mode
    refreshGUI()

def clickEnnemieMap(event):
    atq(playerMapSelect,ennemieMapSelect,event.x//(ennemieMap.winfo_width()//mapSize)+1,event.y//(ennemieMap.winfo_height()//mapSize)+1)
    for ennemi in range(2,mapNumber+1):
        if ennemi != playerMapSelect:
            for atqMap in range(1,mapNumber+1):
                if atqMap != ennemi:
                    atq(ennemi,atqMap,randint(1,mapSize),randint(1,mapSize))
    refreshGUI()

def clickBuild(event):
    global testAddBoat
    global lastBuildBoat
    map = playerMapSelect
    direction = "NESW"
    if buildBoatSelected != "":
        if len(boatData[map-1]) < len(gameDataBoat) and boatDataTypeCount(buildBoatSelected,map) != gameDataBoat.count(buildBoatSelected):
            addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//mapSize)+1,event.y//(playerMapBuild.winfo_height()//mapSize)+1,direction[buildBoatDirection])
            if testAddBoat < len(boatData[map-1]):
                testAddBoat += 1
            refreshGUI()
        boatSelect("")
    else:
        type = mapRead(map,event.x//(playerMapBuild.winfo_width()//mapSize)+1,event.y//(playerMapBuild.winfo_height()//mapSize)+1)[0]
        if type != "--":
            removeBoat(map,type)
            boatSelect(type[0])

def refreshLoop():
    refreshMousePos()
    refreshGUI()
    app.after(50,refreshLoop)

def refreshMousePos():
    global mouseX
    global mouseY
    mouseX = app.winfo_pointerx() - app.winfo_rootx()
    mouseY = app.winfo_pointery() - app.winfo_rooty()

def refreshGUI():
    global titleStyle
    global globalSize
    global buildBoatDirection

    # AllPage
    globalSize = 1 + (app.winfo_height() - 450)*(app.winfo_width() - 800)*0.0000025
    titleStyle.configure(size=int(50*globalSize))
    default_font.configure(family="Arial",size=int(11*(globalSize*0.5+0.5)),weight=BOLD)

    # PreParty
    if gameMode:
        text_selectGame.config(text=lg("Personnalisé"))
        text_selectGame2.config(text=lg("Personnalisé"))
    else:
        text_selectGame.config(text=lg("Standard"))
        text_selectGame2.config(text=lg("Standard"))

    ennemieName.config(text="Player "+str(ennemieMapSelect))
    ennemieName.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0.5,rely=1,y=-10,anchor = S)

    direction = ["Nord","Est","Sud","Ouest"]
    text_changeDirection.config(text=str(direction[buildBoatDirection]))

    # Conbstruction de la carte
    boatBuildZone.delete("all")

    playerMapBuild.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    playerMapBuild.delete("all")
    cases = []
    for i in range(mapSize):
        cases_i=[]
        for j in range(mapSize):
            if mapRead(playerMapSelect,j+1,i+1)[0] != "--":
                caseColor="lavender"
            else:
                caseColor="steelBlue3"
            cases_i.append(playerMapBuild.create_rectangle((j*(playerMapBuild.winfo_width()/mapSize)), (i*(playerMapBuild.winfo_height()/mapSize)), ((j+1)*(playerMapBuild.winfo_width()/mapSize)-2), ((i+1)*(playerMapBuild.winfo_height()/mapSize)-2),outline=caseColor,fill=caseColor))
        cases.append(cases_i)

    # Gestion des bateaux placer

    # Fboat
    for type in range(len(allBoatType)):
        if allBoatType[type] == "a":
            imgSelect = img_Fboat_N
            if buildBoatSelected == allBoatType[type] and buildBoatDirection == 1:
                imgSelect = img_Fboat_E
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 2:
                imgSelect = img_Fboat_S
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 3:
                imgSelect = img_Fboat_W
        elif allBoatType[type] == "c":
            imgSelect = img_Fboat_N
            if buildBoatSelected == allBoatType[type] and buildBoatDirection == 1:
                imgSelect = img_Fboat_E
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 2:
                imgSelect = img_Fboat_S
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 3:
                imgSelect = img_Fboat_W
        elif allBoatType[type] == "f":
            imgSelect = img_Fboat_N
            if buildBoatSelected == allBoatType[type] and buildBoatDirection == 1:
                imgSelect = img_Fboat_E
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 2:
                imgSelect = img_Fboat_S
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 3:
                imgSelect = img_Fboat_W
        elif allBoatType[type] == "s":
            imgSelect = img_Fboat_N
            if buildBoatSelected == allBoatType[type] and buildBoatDirection == 1:
                imgSelect = img_Fboat_E
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 2:
                imgSelect = img_Fboat_S
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 3:
                imgSelect = img_Fboat_W
        else:
            imgSelect = img_Fboat_N
            if buildBoatSelected == allBoatType[type] and buildBoatDirection == 1:
                imgSelect = img_Fboat_E
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 2:
                imgSelect = img_Fboat_S
            elif buildBoatSelected == allBoatType[type] and buildBoatDirection == 3:
                imgSelect = img_Fboat_W
        if buildBoatSelected == allBoatType[type] and boatDataTypeCount(allBoatType[type],playerMapSelect) != gameDataBoat.count(allBoatType[type]):
            if inBuildMap:
                if buildBoatSelected == "c" or buildBoatSelected == "p":
                    if buildBoatDirection == 0 or buildBoatDirection == 2:
                        playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//mapSize))*(playerMapBuild.winfo_width()//mapSize))+((playerMapBuild.winfo_width()//mapSize)//2), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//mapSize))*(playerMapBuild.winfo_height()//mapSize))+((playerMapBuild.winfo_height()//mapSize)//2),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
                    else:
                        playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//mapSize))*(playerMapBuild.winfo_width()//mapSize))+((playerMapBuild.winfo_width()//mapSize)//2), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//mapSize))*(playerMapBuild.winfo_height()//mapSize))+((playerMapBuild.winfo_height()//mapSize)//2),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
                else:
                    playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//mapSize))*(playerMapBuild.winfo_width()//mapSize))+((playerMapBuild.winfo_width()//mapSize)//2), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//mapSize))*(playerMapBuild.winfo_height()//mapSize))+((playerMapBuild.winfo_height()//mapSize)//2),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
            else:
                boatBuildZone.create_image(mouseX,mouseY,image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
        elif buildBoatSelected != allBoatType[type] and boatDataTypeCount(allBoatType[type],playerMapSelect) != gameDataBoat.count(allBoatType[type]):
            boatBuildZone.create_image(30*(type+1),200,image=imgSelect,tags=str(allBoatType[type])+"Boat")

    # Party
    mapZone.place(relx = 0.5, rely = 0.5, relwidth = 1, relheight = 1,anchor = CENTER)
    mapZoneUser.place(relheight=1,relwidth=0.5)
    mapZoneEnnemie.place(relheight=1,relwidth=0.5, relx=0.5)

    playerMap.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    playerMap.delete("all")
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

    ennemieMap.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    ennemieMap.delete("all")
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
            button_nextMap.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0.9,rely=1,y=-10,anchor = SE)
        else:
            button_nextMap.place_forget()
        if ennemieMapSelect > 1 and not (playerMapSelect == 1 and ennemieMapSelect-1 == 1):
            button_backMap.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0.1,rely=1,y=-10,anchor = SW)
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

button_selectIAGame = ttk.Button(selectPartyPage, text=lg("Standard").upper(),command=lambda:[switch(prePartyPage),selectGameMode(0)])
button_selectIAGame.place(relwidth=0.4, relheight=0.75,relx = 0.3, rely = 0.475, anchor = CENTER)

button_selectCustomGame = ttk.Button(selectPartyPage, text=lg("Personnalisé").upper(),command=lambda:[switch(prePartyPage),selectGameMode(1)])
button_selectCustomGame.place(relwidth=0.4, relheight=0.75,relx = 0.7, rely = 0.475, anchor = CENTER)

button_back = ttk.Button(selectPartyPage, text=lg("Retour"),command=lambda:switch(mainMenuPage))
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

# Pre-Party

boatBuildZone = Canvas(prePartyPage)
boatBuildZone.place(relheight=1,relwidth=1,relx=0.5,rely=0.5,anchor=CENTER)

playerMapBuild = Canvas(boatBuildZone,bg="steelBlue4",cursor="crosshair")

text_selectGame = Label(prePartyPage,fg="black")
text_selectGame.place(relheight=0.1,relwidth=0.2,relx = 0.5, rely = 0.05, anchor = CENTER)

button_back = ttk.Button(prePartyPage, text=lg("Retour"),command=lambda:switch(selectPartyPage))
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

button_launchGame = ttk.Button(prePartyPage, text=lg("/// LANCER ///"),command=laucheGame)
button_launchGame.place(height=50,width=100,relheight=0.05,relwidth=0.1,relx=1,rely=1,x=-10,y=-10,anchor = SE)

text_changeDirection = ttk.Label(prePartyPage, text="Orientation")
text_changeDirection.place(height=30,width=30,relheight=0.025,relwidth=0.025,relx=0.1,rely=0.8,x=10,y=-10,anchor = SW)
        
# Party

mapZone = Frame(partyPage)
mapZoneUser = Frame(mapZone)
mapZoneEnnemie = Frame(mapZone)
playerMap = Canvas(mapZoneUser,bg="steelBlue4")
ennemieMap = Canvas(mapZoneEnnemie,bg="steelBlue4",cursor="crosshair")

text_selectGame2 = Label(partyPage,fg="black")
text_selectGame2.place(relheight=0.1,relwidth=0.2,relx = 0.5, rely = 0.05, anchor = CENTER)

button_backToMainMenu = ttk.Button(partyPage, text=lg("Menu principal"),command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=30,width=75,relheight=0.025,relwidth=0.1,relx=0,rely=1,x=10,y=-10,anchor = SW)

ennemieName = Label(mapZoneEnnemie)

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