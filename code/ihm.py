# --- Importation des bibliothèque

# Imporations des données
from itertools import count
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
buildBoatDirection = 1
buildBoatSelected = ""
mouseX = 0
mousY = 0
inBuildMap = False
inEnnemieMap = False
Hz = 30
ennemieMapAtq = 2
openTime = 0
playerAtqCount = []

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

img_Aboat_N_Source = Image.open("../gui/image/Aboat_N.png")
img_Aboat_E_Source = Image.open("../gui/image/Aboat_E.png")
img_Aboat_S_Source = Image.open("../gui/image/Aboat_S.png")
img_Aboat_W_Source = Image.open("../gui/image/Aboat_W.png")

img_Cboat_N_Source = Image.open("../gui/image/Cboat_N.png")
img_Cboat_E_Source = Image.open("../gui/image/Cboat_E.png")
img_Cboat_S_Source = Image.open("../gui/image/Cboat_S.png")
img_Cboat_W_Source = Image.open("../gui/image/Cboat_W.png")

img_Fboat_N_Source = Image.open("../gui/image/Fboat_N.png")
img_Fboat_E_Source = Image.open("../gui/image/Fboat_E.png")
img_Fboat_S_Source = Image.open("../gui/image/Fboat_S.png")
img_Fboat_W_Source = Image.open("../gui/image/Fboat_W.png")

img_Sboat_N_Source = Image.open("../gui/image/Sboat_N.png")
img_Sboat_E_Source = Image.open("../gui/image/Sboat_E.png")
img_Sboat_S_Source = Image.open("../gui/image/Sboat_S.png")
img_Sboat_W_Source = Image.open("../gui/image/Sboat_W.png")

img_Pboat_N_Source = Image.open("../gui/image/Pboat_N.png")
img_Pboat_E_Source = Image.open("../gui/image/Pboat_E.png")
img_Pboat_S_Source = Image.open("../gui/image/Pboat_S.png")
img_Pboat_W_Source = Image.open("../gui/image/Pboat_W.png")

def refreshImg():
    global img_Aboat_N
    global img_Aboat_E
    global img_Aboat_S
    global img_Aboat_W

    global img_Cboat_N
    global img_Cboat_E
    global img_Cboat_S
    global img_Cboat_W

    global img_Fboat_N
    global img_Fboat_E
    global img_Fboat_S
    global img_Fboat_W

    global img_Sboat_N
    global img_Sboat_E
    global img_Sboat_S
    global img_Sboat_W

    global img_Pboat_N
    global img_Pboat_E
    global img_Pboat_S
    global img_Pboat_W

    img_Aboat_N = ImageTk.PhotoImage(img_Aboat_N_Source.resize((int(200//7*globalSize),int(1000//7*globalSize)), Image.ANTIALIAS))
    img_Aboat_E = ImageTk.PhotoImage(img_Aboat_E_Source.resize((int(1000//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))
    img_Aboat_S = ImageTk.PhotoImage(img_Aboat_S_Source.resize((int(200//7*globalSize),int(1000//7*globalSize)), Image.ANTIALIAS))
    img_Aboat_W = ImageTk.PhotoImage(img_Aboat_W_Source.resize((int(1000//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))

    img_Cboat_N = ImageTk.PhotoImage(img_Cboat_N_Source.resize((int(200//7*globalSize),int(800//7*globalSize)), Image.ANTIALIAS))
    img_Cboat_E = ImageTk.PhotoImage(img_Cboat_E_Source.resize((int(800//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))
    img_Cboat_S = ImageTk.PhotoImage(img_Cboat_S_Source.resize((int(200//7*globalSize),int(800//7*globalSize)), Image.ANTIALIAS))
    img_Cboat_W = ImageTk.PhotoImage(img_Cboat_W_Source.resize((int(800//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))

    img_Fboat_N = ImageTk.PhotoImage(img_Fboat_N_Source.resize((int(200//7*globalSize),int(600//7*globalSize)), Image.ANTIALIAS))
    img_Fboat_E = ImageTk.PhotoImage(img_Fboat_E_Source.resize((int(600//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))
    img_Fboat_S = ImageTk.PhotoImage(img_Fboat_S_Source.resize((int(200//7*globalSize),int(600//7*globalSize)), Image.ANTIALIAS))
    img_Fboat_W = ImageTk.PhotoImage(img_Fboat_W_Source.resize((int(600//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))

    img_Sboat_N = ImageTk.PhotoImage(img_Sboat_N_Source.resize((int(200//7*globalSize),int(600//7*globalSize)), Image.ANTIALIAS))
    img_Sboat_E = ImageTk.PhotoImage(img_Sboat_E_Source.resize((int(600//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))
    img_Sboat_S = ImageTk.PhotoImage(img_Sboat_S_Source.resize((int(200//7*globalSize),int(600//7*globalSize)), Image.ANTIALIAS))
    img_Sboat_W = ImageTk.PhotoImage(img_Sboat_W_Source.resize((int(600//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))

    img_Pboat_N = ImageTk.PhotoImage(img_Pboat_N_Source.resize((int(200//7*globalSize),int(400//7*globalSize)), Image.ANTIALIAS))
    img_Pboat_E = ImageTk.PhotoImage(img_Pboat_E_Source.resize((int(400//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))
    img_Pboat_S = ImageTk.PhotoImage(img_Pboat_S_Source.resize((int(200//7*globalSize),int(400//7*globalSize)), Image.ANTIALIAS))
    img_Pboat_W = ImageTk.PhotoImage(img_Pboat_W_Source.resize((int(400//7*globalSize),int(200//7*globalSize)), Image.ANTIALIAS))

def finfBoatImg(type,direction):
    orientation = "NESW"
    if not isinstance(direction, int):
        direction = orientation.index(direction) 
    if type == "a":
            imgSelect = img_Aboat_E
            if direction == 0:
                imgSelect = img_Aboat_N
            elif direction == 2:
                imgSelect = img_Aboat_S
            elif direction == 3:
                imgSelect = img_Aboat_W
    elif type == "c":
        imgSelect = img_Cboat_E
        if direction == 0:
            imgSelect = img_Cboat_N
        elif direction == 2:
            imgSelect = img_Cboat_S
        elif direction == 3:
            imgSelect = img_Cboat_W
    elif type == "f":
        imgSelect = img_Fboat_E
        if direction == 0:
            imgSelect = img_Fboat_N
        elif direction == 2:
            imgSelect = img_Fboat_S
        elif direction == 3:
            imgSelect = img_Fboat_W
    elif type == "s":
        imgSelect = img_Sboat_E
        if direction == 0:
            imgSelect = img_Sboat_N
        elif direction == 2:
            imgSelect = img_Sboat_S
        elif direction == 3:
            imgSelect = img_Sboat_W
    else:
        imgSelect = img_Pboat_E
        if direction == 0:
            imgSelect = img_Pboat_N
        elif direction == 2:
            imgSelect = img_Pboat_S
        elif direction == 3:
            imgSelect = img_Pboat_W
    return imgSelect

### --- Action de boutton --- ###

def setFullScreen(event):
    global fullScreen
    global globalSize
    if fullScreen :
        fullScreen = False
    else:
        fullScreen = True
    app.attributes("-fullscreen", fullScreen) 
    globalSize = 1 + (app.winfo_height() - 450)*(app.winfo_width() - 800)*0.0000025
    refreshGUI()
    refreshImg()

def laucheGame():
    for i in range(mapNumber):
        if i != playerMapSelect:
            creatRandomMap(i)
    switch(partyPage)
    refreshGUI()

# Fonction d'action de fenêtre
def switch(frame):
    for widget in window.winfo_children():
        widget.pack_forget()
    window.pack(expand = 1, fill =BOTH)
    frame.pack(expand = 1, fill =BOTH)
    refreshGUI()

# Redimentionnement

# Selection de la map adverse visible
def nextEnnemieMap(select):
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

def cooldown():
    global openTime
    global strikerMap
    global atqDone
    global playerAtqCount
    if strikerMap != playerMapSelect:
        ennemiPlay(strikerMap)
        atqDone = True
    if atqDone:
        atqDone = False
        playerAtqCount.clear()
            
        if strikerMap < mapNumber:
            strikerMap += 1
        else:
            strikerMap = 1
    if playerDeathData[playerMapSelect-1]:
        print("Perdu")
    elif not playerDeathData[playerMapSelect-1] and playerDeathData.count(True) == mapNumber - 1:
        print("Gagné")

    refreshImg()
    openTime += 1
    app.after(100,cooldown)

def changeBoatDirection(event):
    global buildBoatDirection
    if not buildBoatSelected == "":
        if buildBoatDirection < 3:
            buildBoatDirection += 1
        else:
            buildBoatDirection = 0

def setInBuildMap(value):
    global inBuildMap
    inBuildMap = value

def setInEnnemieMap(value):
    global inEnnemieMap
    inEnnemieMap = value

def boatImgInMap(mapGui,map,hideBoat):
    for i in range(len(boatGuiData[map-1])):
        imgSelect = finfBoatImg(boatGuiData[map-1][i][0][0],boatGuiData[map-1][i][3])
        if not hideBoat or hideBoat and mapRead(map,boatGuiData[map-1][i][1],boatGuiData[map-1][i][2])[1] == "DD":
            if boatGuiData[map-1][i][0][0] == "c" or boatGuiData[map-1][i][0][0] == "p":
                if boatGuiData[map-1][i][3] == "N":
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/mapSize))-(mapGui.winfo_width()/mapSize/2), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/mapSize))-(mapGui.winfo_height()/mapSize),image=imgSelect)
                elif boatGuiData[map-1][i][3] == "E":
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/mapSize)), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/mapSize))-(mapGui.winfo_height()/mapSize/2),image=imgSelect)
                elif boatGuiData[map-1][i][3] == "S":
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/mapSize))-(mapGui.winfo_width()/mapSize/2), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/mapSize)),image=imgSelect)
                else:
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/mapSize))-(mapGui.winfo_width()/mapSize), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/mapSize))-(mapGui.winfo_height()/mapSize/2),image=imgSelect)
            else:
                mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/mapSize))-(mapGui.winfo_width()/mapSize/2), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/mapSize))-(mapGui.winfo_height()/mapSize/2),image=imgSelect)

def boatSelect(type,direction,forceSelect):
    global buildBoatSelected
    global buildBoatDirection
    orientation = "NESW"
    buildBoatSelected = ""
    buildBoatDirection = 1
    if boatDataTypeCount(type,playerMapSelect) != gameDataBoat.count(type) or forceSelect:
        buildBoatSelected = type
        if isinstance(direction, int):
            buildBoatDirection = direction
        else:
            buildBoatDirection = orientation.index(direction)

def selectGameMode(mode):
    global gameMode
    gameMode = mode
    refreshGUI()

def clickEnnemieMap(event):
    global atqDone
    global playerAtqCount
    if strikerMap == playerMapSelect and ennemieMapSelect not in playerAtqCount and atqDone == False and mapRead(ennemieMapSelect,event.x//(ennemieMap.winfo_width()//mapSize)+1,event.y//(ennemieMap.winfo_height()//mapSize)+1)[1][0] != "X" and playerDeathData[ennemieMapSelect-1] == False:
        playerAtqCount.append(ennemieMapSelect)
        if len(playerAtqCount) == playerDeathData.count(False) - 1:
            atqDone = True
        atq(playerMapSelect,ennemieMapSelect,event.x//(ennemieMap.winfo_width()//mapSize)+1,event.y//(ennemieMap.winfo_height()//mapSize)+1)
        refreshGUI()

def clickBuild(event):
    global testAddBoat
    global lastBuildBoat
    map = playerMapSelect
    direction = "NESW"
    if buildBoatSelected != "":
        if len(boatData[map-1]) < len(gameDataBoat) and boatDataTypeCount(buildBoatSelected,map) != gameDataBoat.count(buildBoatSelected):
            if buildBoatSelected == "c" or buildBoatSelected == "p":
                    if buildBoatDirection == 0:
                        addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//mapSize)+1,event.y//(playerMapBuild.winfo_height()//mapSize)+2,direction[buildBoatDirection])
                    elif buildBoatDirection == 3:
                        addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//mapSize)+2,event.y//(playerMapBuild.winfo_height()//mapSize)+1,direction[buildBoatDirection])
                    else:
                        addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//mapSize)+1,event.y//(playerMapBuild.winfo_height()//mapSize)+1,direction[buildBoatDirection])
            else:
                addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//mapSize)+1,event.y//(playerMapBuild.winfo_height()//mapSize)+1,direction[buildBoatDirection])
            if testAddBoat < len(boatData[map-1]):
                testAddBoat += 1
            refreshGUI()
        boatSelect("",1,0)
    else:
        type = mapRead(map,event.x//(playerMapBuild.winfo_width()//mapSize)+1,event.y//(playerMapBuild.winfo_height()//mapSize)+1)[0]
        if type != "--":
            for i in range(len(boatGuiData[map-1])):
                if boatGuiData[map-1][i][0] == type:
                    boatSelect(type[0],boatGuiData[map-1][i][3],True)
            removeBoat(map,type)

def guiloop():
    global globalSize
    globalSize = 1 + (app.winfo_height() - 450)*(app.winfo_width() - 800)*0.0000025
    refreshMousePos()
    refreshGUI()
    app.after(int((1/(Hz))*1000),guiloop)

def refreshMousePos():
    global mouseX
    global mouseY
    mouseX = app.winfo_pointerx() - app.winfo_rootx()
    mouseY = app.winfo_pointery() - app.winfo_rooty()

def refreshGUI():
    global titleStyle
    global buildBoatDirection

    # AllPage
    titleStyle.configure(size=int(50*globalSize))
    default_font.configure(family="Arial",size=int(11*(globalSize*0.5+0.5)),weight=BOLD)

    # PreParty
    if gameMode:
        text_selectGame.config(text=lg("Personnalisé"))
        text_selectGame2.config(text=lg("Personnalisé"))
    else:
        text_selectGame.config(text=lg("Standard"))
        text_selectGame2.config(text=lg("Standard"))

    if playerDeathData[ennemieMapSelect-1] == True:
        ennemieName.config(text="Player "+str(ennemieMapSelect),fg="red")
    else:
        ennemieName.config(text="Player "+str(ennemieMapSelect))
    ennemieName.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0.5,rely=1,y=-10,anchor = S)

    boatBuildZone.delete("all")

    playerMapBuild.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    playerMapBuild.delete("all")

    # Affichage des cases
    cases = []
    for i in range(mapSize):
        cases_i=[]
        for j in range(mapSize):
            if mapRead(playerMapSelect,j+1,i+1)[0] != "--":
                caseColor="steelBlue3"
            else:
                caseColor="steelBlue3" 
            cases_i.append(playerMapBuild.create_rectangle((j*(playerMapBuild.winfo_width()/mapSize)), (i*(playerMapBuild.winfo_height()/mapSize)), ((j+1)*(playerMapBuild.winfo_width()/mapSize)-2), ((i+1)*(playerMapBuild.winfo_height()/mapSize)-2),outline=caseColor,fill=caseColor))
        cases.append(cases_i)

    # Affichage des bateaux
    boatImgInMap(playerMapBuild,playerMapSelect,False)
    
    for type in range(len(allBoatType)):
        if buildBoatSelected == allBoatType[type]:
            imgSelect = finfBoatImg(allBoatType[type],buildBoatDirection)
        else:
            imgSelect = finfBoatImg(allBoatType[type],1)
        
        if buildBoatSelected == allBoatType[type] and boatDataTypeCount(allBoatType[type],playerMapSelect) != gameDataBoat.count(allBoatType[type]):
            if inBuildMap:
                if buildBoatSelected == "c" or buildBoatSelected == "p":
                    if buildBoatDirection == 0 or buildBoatDirection == 2:
                        playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//mapSize))*(playerMapBuild.winfo_width()//mapSize))+((playerMapBuild.winfo_width()//mapSize)//2), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//mapSize))*(playerMapBuild.winfo_height()//mapSize))+((playerMapBuild.winfo_height()//mapSize)),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
                    else:
                        playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//mapSize))*(playerMapBuild.winfo_width()//mapSize))+((playerMapBuild.winfo_width()//mapSize)), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//mapSize))*(playerMapBuild.winfo_height()//mapSize))+((playerMapBuild.winfo_height()//mapSize)//2),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
                else:
                    playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//mapSize))*(playerMapBuild.winfo_width()//mapSize))+((playerMapBuild.winfo_width()//mapSize)//2), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//mapSize))*(playerMapBuild.winfo_height()//mapSize))+((playerMapBuild.winfo_height()//mapSize)//2),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
            else:
                boatBuildZone.create_image(mouseX,mouseY,image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")

        elif buildBoatSelected != allBoatType[type] and boatDataTypeCount(allBoatType[type],playerMapSelect) != gameDataBoat.count(allBoatType[type]):
            boatBuildZone.create_image(app.winfo_width()//7,app.winfo_height()//8+app.winfo_height()//8*(type+1),image=imgSelect,tags=str(allBoatType[type])+"Boat")
    
    boatBuildZone.tag_raise(buildBoatSelected+"BoatSelect")

    if len(boatData[playerMapSelect-1]) == len(gameDataBoat) :
        button_launchGame.config(state=ACTIVE)
    else:
        button_launchGame.config(state=DISABLED)

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
                caseColor="steelBlue3"
            else:
                caseColor="steelBlue3"
            cases_i.append(playerMap.create_rectangle((j*(playerMap.winfo_width()/mapSize)), (i*(playerMap.winfo_height()/mapSize)), ((j+1)*(playerMap.winfo_width()/mapSize)-2), ((i+1)*(playerMap.winfo_height()/mapSize)-2),outline=caseColor,fill=caseColor))
        cases.append(cases_i)

    boatImgInMap(playerMap,playerMapSelect,False)

    ennemieMap.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
    ennemieMap.delete("all")
    cases = []
    for i in range(mapSize):
        cases_i=[]
        for j in range(mapSize):
            if mapRead(ennemieMapSelect,j+1,i+1)[1] == "DD":
                caseColor="steelblue1"
            elif mapRead(ennemieMapSelect,j+1,i+1)[0] != "--" and mapRead(ennemieMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="red"
            elif mapRead(ennemieMapSelect,j+1,i+1)[0] == "--" and mapRead(ennemieMapSelect,j+1,i+1)[1][0] == "X":
                caseColor="steelblue1"
            else:
                caseColor="steelBlue3"
            if strikerMap == playerMapSelect and atqDone == False and ennemieMapSelect not in playerAtqCount and playerDeathData[ennemieMapSelect -1] == False:
                cases_i.append(ennemieMap.create_rectangle((j*(ennemieMap.winfo_width()/mapSize)), (i*(ennemieMap.winfo_height()/mapSize)), ((j+1)*(ennemieMap.winfo_width()/mapSize)-2), ((i+1)*(ennemieMap.winfo_height()/mapSize)-2),outline=caseColor,activeoutline="white",fill=caseColor,activewidth=1*globalSize))
            else:
                cases_i.append(ennemieMap.create_rectangle((j*(ennemieMap.winfo_width()/mapSize)), (i*(ennemieMap.winfo_height()/mapSize)), ((j+1)*(ennemieMap.winfo_width()/mapSize)-2), ((i+1)*(ennemieMap.winfo_height()/mapSize)-2),outline=caseColor,fill=caseColor))
        cases.append(cases_i)

    boatImgInMap(ennemieMap,ennemieMapSelect,True)

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
            button_nextMap.place(height=30,width=75,relheight=0.025,relwidth=0.05,relx=0.9,rely=1,y=-10,anchor = SE)
        else:
            button_nextMap.place_forget()
        if ennemieMapSelect > 1 and not (playerMapSelect == 1 and ennemieMapSelect-1 == 1):
            button_backMap.place(height=30,width=75,relheight=0.025,relwidth=0.05,relx=0.1,rely=1,y=-10,anchor = SW)
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

button_selectIAGame = ttk.Button(selectPartyPage, text=lg("Standard").upper(),command=lambda:[switch(prePartyPage),selectGameMode(0),creatmap(),refreshImg()])
button_selectIAGame.place(relwidth=0.4, relheight=0.75,relx = 0.3, rely = 0.475, anchor = CENTER)

button_selectCustomGame = ttk.Button(selectPartyPage, text=lg("Personnalisé").upper(),command=lambda:[switch(prePartyPage),selectGameMode(1),creatmap(),refreshImg()])
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
button_launchGame.place(height=50,width=100,relheight=0.05,relwidth=0.15,relx=1,rely=1,x=-10,y=-10,anchor = SE)

button_creatyRandomMap = ttk.Button(prePartyPage, text=lg("Aléatoire"),command=lambda:[creatmap(),creatRandomMap(playerMapSelect)])
button_creatyRandomMap.place(height=30,width=100,relheight=0.025,relwidth=0.15,relx=1,rely=0.95,x=-10,y=-65,anchor = SE)

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

button_nextMap = ttk.Button(mapZoneEnnemie, text="Player "+str(ennemieMapSelect+1),command=lambda:nextEnnemieMap(1))
button_backMap = ttk.Button(mapZoneEnnemie, text="Player "+str(ennemieMapSelect-1),command=lambda:nextEnnemieMap(0))

### --- Main execution --- ###

def mainStart():
    app.title("Battleship Warfare")
    app.minsize(800, 450)
    app.maxsize(app.winfo_screenwidth(),app.winfo_screenheight())
    app.geometry('%dx%d+%d+%d' % (W, H, (app.winfo_screenwidth()/2) - (W/2), (app.winfo_screenheight()/2) - (H/2)))
    refreshImg()
    creatmap()
    # Ouverture du menu
    switch(mainMenuPage)