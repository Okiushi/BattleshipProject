# --- Importation des bibliothèque

# Imporations des données
from data import *
import data as d

# Gestion des interfaces graphiques
from tkinter import *
import tkinter as tk

# Modernisation des widgets
from tkinter import ttk

# Gestion des polices
from tkinter.font import *
import tkinter.font as tkFont

# Gestion des images
try: # Teste l'importation du module PIL
    from PIL import ImageTk, Image
except: # install le module s'il n'est pas présent
    import os
    os.system("python -m pip install pillow")
    from PIL import ImageTk, Image

# --- Affectation des variables

app = tk.Tk()
# Preset
fullScreen = False
W  = 800
H = 450
globalSize = 1
buildBoatDirection = 1
buildBoatSelected = ""
mouseX = 0 
mousY = 0
inBuildMap = False
inEnnemieMap = False
Hz = 30
openTime = 0
shakeTime = 2
shakeWindow = False
cooldown = 1
shakeIntensity = 0
showLetter = True
inversLetter = False
page = ""

# --- Page
window = Frame(app)
startPage = Frame(window,bg="black",cursor="none")
mainMenuPage = Frame(window)
selectPartyPage = Frame(window)
prePartyPage = Frame(window)
partyPage = Frame(window)
settingsPage = Frame(window)
creditsPage = Frame(window)

# --- Style du text
titleStyle = tkFont.Font(family="Impact")
default_font = nametofont("TkDefaultFont")

# --- Musique

# Fonction d'action de fenêtre
def switch(frame):
    global page
    for widget in window.winfo_children():
        widget.place_forget()
    window.place(relx=0.5,x=0,rely=0.5,y=0,relheight=1,relwidth=1,anchor=CENTER)
    frame.place(relx=0.5,rely=0.5,relheight=1,relwidth=1,anchor=CENTER)
    page = frame
    refreshGUI()

# --- Gestion des images
# Porte avion
img_Aboat_N_Source = Image.open("../gui/image/Aboat_N.png"); img_Aboat_E_Source = Image.open("../gui/image/Aboat_E.png"); img_Aboat_S_Source = Image.open("../gui/image/Aboat_S.png"); img_Aboat_W_Source = Image.open("../gui/image/Aboat_W.png")
# Cuirrasé
img_Cboat_N_Source = Image.open("../gui/image/Cboat_N.png"); img_Cboat_E_Source = Image.open("../gui/image/Cboat_E.png"); img_Cboat_S_Source = Image.open("../gui/image/Cboat_S.png"); img_Cboat_W_Source = Image.open("../gui/image/Cboat_W.png")
# Frégate
img_Fboat_N_Source = Image.open("../gui/image/Fboat_N.png"); img_Fboat_E_Source = Image.open("../gui/image/Fboat_E.png"); img_Fboat_S_Source = Image.open("../gui/image/Fboat_S.png"); img_Fboat_W_Source = Image.open("../gui/image/Fboat_W.png")
# Sous-marin
img_Sboat_N_Source = Image.open("../gui/image/Sboat_N.png"); img_Sboat_E_Source = Image.open("../gui/image/Sboat_E.png"); img_Sboat_S_Source = Image.open("../gui/image/Sboat_S.png"); img_Sboat_W_Source = Image.open("../gui/image/Sboat_W.png")
# Patrouilleur
img_Pboat_N_Source = Image.open("../gui/image/Pboat_N.png"); img_Pboat_E_Source = Image.open("../gui/image/Pboat_E.png"); img_Pboat_S_Source = Image.open("../gui/image/Pboat_S.png"); img_Pboat_W_Source = Image.open("../gui/image/Pboat_W.png")

# --- Rafraichissement de la taille des images (toute les secondes)
def refreshImg():
    if page == partyPage or page == prePartyPage or page == startPage: # Affichage uniquement quand nécaissaire par soucis de performance
        # Porte avion
        global img_Aboat_N; global img_Aboat_E; global img_Aboat_S; global img_Aboat_W
        img_Aboat_N = ImageTk.PhotoImage(img_Aboat_N_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((1000//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Aboat_E = ImageTk.PhotoImage(img_Aboat_E_Source.resize((int((1000/7*globalSize)/(d.mapSize/10)),int((200/7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Aboat_S = ImageTk.PhotoImage(img_Aboat_S_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((1000//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Aboat_W = ImageTk.PhotoImage(img_Aboat_W_Source.resize((int((1000//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS))    
        # Cuirrasé 
        global img_Cboat_N; global img_Cboat_E ;global img_Cboat_S; global img_Cboat_W
        img_Cboat_N = ImageTk.PhotoImage(img_Cboat_N_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((800//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Cboat_E = ImageTk.PhotoImage(img_Cboat_E_Source.resize((int((800//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Cboat_S = ImageTk.PhotoImage(img_Cboat_S_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((800//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Cboat_W = ImageTk.PhotoImage(img_Cboat_W_Source.resize((int((800//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS))    
        # Frégate
        global img_Fboat_N; global img_Fboat_E; global img_Fboat_S; global img_Fboat_W
        img_Fboat_N = ImageTk.PhotoImage(img_Fboat_N_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((600//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Fboat_E = ImageTk.PhotoImage(img_Fboat_E_Source.resize((int((600//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Fboat_S = ImageTk.PhotoImage(img_Fboat_S_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((600//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Fboat_W = ImageTk.PhotoImage(img_Fboat_W_Source.resize((int((600//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS))    
        # Sous-marin
        global img_Sboat_N; global img_Sboat_E; global img_Sboat_S; global img_Sboat_W
        img_Sboat_N = ImageTk.PhotoImage(img_Sboat_N_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((600//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Sboat_E = ImageTk.PhotoImage(img_Sboat_E_Source.resize((int((600//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Sboat_S = ImageTk.PhotoImage(img_Sboat_S_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((600//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Sboat_W = ImageTk.PhotoImage(img_Sboat_W_Source.resize((int((600//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS))
        # Patrouilleur
        global img_Pboat_N; global img_Pboat_E; global img_Pboat_S; global img_Pboat_W
        img_Pboat_N = ImageTk.PhotoImage(img_Pboat_N_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((400//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Pboat_E = ImageTk.PhotoImage(img_Pboat_E_Source.resize((int((400//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Pboat_S = ImageTk.PhotoImage(img_Pboat_S_Source.resize((int((200//7*globalSize)/(d.mapSize/10)),int((400//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS)); img_Pboat_W = ImageTk.PhotoImage(img_Pboat_W_Source.resize((int((400//7*globalSize)/(d.mapSize/10)),int((200//7*globalSize)/(d.mapSize/10))), Image.ANTIALIAS))
    refreshGUI()
    app.after(1000,refreshImg) # Re-rafraichissement après une seconde

#  --- Trouveur de l'image correspondante à un type de bateau et sa direction
def finfBoatImg(type,direction):
    orientation = "NESW"
    typeList = "acfsp"
    imgName = ["img_Aboat","img_Cboat","img_Fboat","img_Sboat","img_Pboat"]
    if not isinstance(direction, int):
        direction = orientation.index(direction) 
    return globals()[imgName[typeList.index(type)]+"_"+orientation[direction]]

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

# Redimentionnement

# Selection de la map adverse visible
def nextEnnemieMap(select):
    if select and d.ennemieMapSelect + 1 == d.playerMapSelect:
        d.ennemieMapSelect += 2
    elif select:
        d.ennemieMapSelect += 1
    elif not select and d.ennemieMapSelect - 1 == d.playerMapSelect:
        d.ennemieMapSelect -= 2
    else:
        d.ennemieMapSelect -= 1
    refreshGUI()

def refreshToure():
    if d.inGame:

        # A un autre joureur de jouer
        if d.allAtqDone:
            d.allAtqDone = False
            d.atqDone = False
            d.tmpAtqDone.clear()
            if d.strikerMap < d.mapNumber:
                d.strikerMap += 1
            else:
                d.strikerMap = 1

            if d.strikerMap != d.playerMapSelect and not d.playerDeathData[d.strikerMap-1]:
                textMaster.config(text="Le joueur "+str(d.strikerMap)+" exécute ses tires.",fg="grey")
            elif d.strikerMap == d.playerMapSelect and not d.playerDeathData[d.strikerMap-1]:
                if mapNumber > 2:
                    textMaster.config(text="Veuillez exécuter vos tires sur chaque flotte adverse.",fg="black")
                else:
                    textMaster.config(text="Veuillez exécuter vos tires sur la flotte adverse.",fg="black")

            app.after(int(cooldown*500),refreshToure)
        
        # Au toure d'un adversaire
        elif d.strikerMap != d.playerMapSelect and not d.playerDeathData[d.strikerMap-1]:
            ennemiPlay(d.strikerMap)
            app.after(int(cooldown*500),refreshToure)
        # Au toure de l'utilisateur    
        elif d.strikerMap == d.playerMapSelect and not d.playerDeathData[d.strikerMap-1]:
            d.allAtqDone = False
            d.atqDone = False

        if d.playerDeathData[d.playerMapSelect-1]:
            d.inGame = False
            textMaster.config(text="Échec de la mission, votre flotte à été anéantie.",fg="red")
        elif not d.playerDeathData[d.playerMapSelect-1] and d.playerDeathData.count(True) == d.mapNumber - 1:
            d.inGame = False
            textMaster.config(text="Félicitation, vous avez à anéantie la flotte ennemie.",fg="lightgreen")
    
        refreshGUI()

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
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/d.mapSize))-(mapGui.winfo_width()/d.mapSize/2), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/d.mapSize))-(mapGui.winfo_height()/d.mapSize),image=imgSelect)
                elif boatGuiData[map-1][i][3] == "E":
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/d.mapSize)), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/d.mapSize))-(mapGui.winfo_height()/d.mapSize/2),image=imgSelect)
                elif boatGuiData[map-1][i][3] == "S":
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/d.mapSize))-(mapGui.winfo_width()/d.mapSize/2), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/d.mapSize)),image=imgSelect)
                else:
                    mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/d.mapSize))-(mapGui.winfo_width()/d.mapSize), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/d.mapSize))-(mapGui.winfo_height()/d.mapSize/2),image=imgSelect)
            else:
                mapGui.create_image((boatGuiData[map-1][i][1]*(mapGui.winfo_width()/d.mapSize))-(mapGui.winfo_width()/d.mapSize/2), (boatGuiData[map-1][i][2]*(mapGui.winfo_height()/d.mapSize))-(mapGui.winfo_height()/d.mapSize/2),image=imgSelect)

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
    d.gameMode = mode
    refreshGUI()

def clickEnnemieMap(event):

    if d.mapNumber > 2 and d.ennemieMapSelect in d.tmpAtqDone:
        textMaster.config(text="Il est impossible de tirer la flotte du joueur "+str(d.ennemieMapSelect)+". Encore "+str(mapNumber-len(tmpAtqDone)-1)+" tire sur d'autre flotte à réaliser",fg="red")
        refreshToure()

    if d.strikerMap == d.playerMapSelect and mapRead(d.ennemieMapSelect,event.x//(ennemieMap.winfo_width()//d.mapSize)+1,event.y//(ennemieMap.winfo_height()//d.mapSize)+1)[1][0] != "X" and not d.playerDeathData[d.ennemieMapSelect-1] and not d.playerDeathData[d.playerMapSelect-1] and not d.ennemieMapSelect in d.tmpAtqDone and not d.atqDone:
        atq(d.playerMapSelect,d.ennemieMapSelect,event.x//(ennemieMap.winfo_width()//d.mapSize)+1,event.y//(ennemieMap.winfo_height()//d.mapSize)+1)
        refreshGUI()
        app.after(int(cooldown*500),refreshToure)
    

def clickBuild(event):
    global testAddBoat
    global lastBuildBoat
    map = playerMapSelect
    direction = "NESW"
    if buildBoatSelected != "":
        if len(boatData[map-1]) < len(gameDataBoat) and boatDataTypeCount(buildBoatSelected,map) != gameDataBoat.count(buildBoatSelected):
            if buildBoatSelected == "c" or buildBoatSelected == "p":
                    if buildBoatDirection == 0:
                        addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//d.mapSize)+1,event.y//(playerMapBuild.winfo_height()//d.mapSize)+2,direction[buildBoatDirection])
                    elif buildBoatDirection == 3:
                        addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//d.mapSize)+2,event.y//(playerMapBuild.winfo_height()//d.mapSize)+1,direction[buildBoatDirection])
                    else:
                        addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//d.mapSize)+1,event.y//(playerMapBuild.winfo_height()//d.mapSize)+1,direction[buildBoatDirection])
            else:
                addBoat(map,buildBoatSelected,event.x//(playerMapBuild.winfo_width()//d.mapSize)+1,event.y//(playerMapBuild.winfo_height()//d.mapSize)+1,direction[buildBoatDirection])
            if testAddBoat < len(boatData[map-1]):
                testAddBoat += 1
            refreshGUI()

        boatSelect("",1,0)
    else:
        type = mapRead(map,event.x//(playerMapBuild.winfo_width()//d.mapSize)+1,event.y//(playerMapBuild.winfo_height()//d.mapSize)+1)[0]
        if type != "--":
            for i in range(len(boatGuiData[map-1])):
                if boatGuiData[map-1][i][0] == type:
                    boatSelect(type[0],boatGuiData[map-1][i][3],True)
            removeBoat(map,type)

def guiloop():
    global globalSize
    globalSize = 1 + (app.winfo_height() - 450)*(app.winfo_width() - 800)*0.0000025
    refreshGUI()
    app.after(int((1/(Hz))*1000),guiloop)
    

# Lanement des tremblements de la fenêtre
def shake(intensity,time):
    global shakeWindow
    global shakeIntensity
    shakeIntensity = intensity
    shakeWindow = True
    app.after(int(time*1000),shakerOff)

# Arret des tremblements de la fenêtre
def shakerOff():
    global shakeWindow
    shakeWindow = False
    window.place(relx=0.5,x=0,rely=0.5,y=0,relheight=1,relwidth=1,anchor=CENTER)

def refreshGUI():
    global titleStyle
    global buildBoatDirection
    global shakeIntensity
    global shakeWindow
    global mouseX
    global mouseY
    mouseX = app.winfo_pointerx() - app.winfo_rootx()
    mouseY = app.winfo_pointery() - app.winfo_rooty()
    lettre = "ABCDEFGHIJKLMNOPQRST"

    # AllPage
    titleStyle.configure(size=int(50*globalSize))
    default_font.configure(family="Arial",size=int(11*(globalSize*0.45+0.55)),weight=BOLD)

    # Effet de tremblement de la fenêtre
    if shakeWindow:
        window.place(relx=0.5,x=randint(-shakeIntensity,shakeIntensity),rely=0.5,y=randint(-shakeIntensity,shakeIntensity),relheight=1,relwidth=1,anchor=CENTER)

    # PreParty
    if page == prePartyPage:

        if gameMode:
            text_selectGame.config(text=lg("Personnalisé"))
        else:
            text_selectGame.config(text=lg("Standard"))

        if buildBoatSelected != "":
            boatBuildZone.config(cursor="fleur")
        else:
            boatBuildZone.config(cursor="arrow")

        playerMapBuild.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)

        boatBuildZone.delete("all")
        playerMapBuild.delete("all")

        # Affichage des cases
        cases = []
        for i in range(d.mapSize):
            cases_i=[]
            for j in range(d.mapSize):
                if mapRead(playerMapSelect,j+1,i+1)[0] != "--":
                    caseColor="steelBlue3"
                else:
                    caseColor="steelBlue3" 
                cases_i.append(playerMapBuild.create_rectangle((j*(playerMapBuild.winfo_width()/d.mapSize)), (i*(playerMapBuild.winfo_height()/d.mapSize)), ((j+1)*(playerMapBuild.winfo_width()/d.mapSize)-int(2*(globalSize*0.5+0.5))), ((i+1)*(playerMapBuild.winfo_height()/d.mapSize)-int(2*(globalSize*0.5+0.5))),outline=caseColor,fill=caseColor))
            cases.append(cases_i)

        # Affichage des bateaux
        boatImgInMap(playerMapBuild,playerMapSelect,False)

        # Affichage des lettres
        if showLetter:
            for x in range(d.mapSize):
                if inversLetter:
                    boatBuildZone.create_text(boatBuildZone.winfo_width()//2-playerMapBuild.winfo_width()//2+playerMapBuild.winfo_width()/d.mapSize*(x+0.5),boatBuildZone.winfo_height()//2-playerMapBuild.winfo_height()//2-5*globalSize,text=lettre[x],fill="steelBlue4",anchor=S)
                else:
                    boatBuildZone.create_text(boatBuildZone.winfo_width()//2-playerMapBuild.winfo_width()//2+playerMapBuild.winfo_width()/d.mapSize*(x+0.5),boatBuildZone.winfo_height()//2-playerMapBuild.winfo_height()//2-5*globalSize,text=str(x+1),fill="steelBlue4",anchor=S)
            for y in range(d.mapSize):
                if inversLetter:
                    boatBuildZone.create_text(boatBuildZone.winfo_width()//2-playerMapBuild.winfo_width()//2-10*globalSize,boatBuildZone.winfo_height()//2-playerMapBuild.winfo_height()//2+playerMapBuild.winfo_width()/d.mapSize*(y+0.5),text=str(y+1),fill="steelBlue4",anchor=E)
                else:
                    boatBuildZone.create_text(boatBuildZone.winfo_width()//2-playerMapBuild.winfo_width()//2-10*globalSize,boatBuildZone.winfo_height()//2-playerMapBuild.winfo_height()//2+playerMapBuild.winfo_width()/d.mapSize*(y+0.5),text=lettre[y],fill="steelBlue4",anchor=E)

        
        for type in range(len(allBoatType)):
            if buildBoatSelected == allBoatType[type]:
                imgSelect = finfBoatImg(allBoatType[type],buildBoatDirection)
            else:
                imgSelect = finfBoatImg(allBoatType[type],1)
            
            if buildBoatSelected == allBoatType[type] and boatDataTypeCount(allBoatType[type],playerMapSelect) != gameDataBoat.count(allBoatType[type]):
                if inBuildMap:
                    if buildBoatSelected == "c" or buildBoatSelected == "p":
                        if buildBoatDirection == 0 or buildBoatDirection == 2:
                            playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//d.mapSize))*(playerMapBuild.winfo_width()//d.mapSize))+((playerMapBuild.winfo_width()//d.mapSize)//2), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//d.mapSize))*(playerMapBuild.winfo_height()//d.mapSize))+((playerMapBuild.winfo_height()//d.mapSize)),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
                        else:
                            playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//d.mapSize))*(playerMapBuild.winfo_width()//d.mapSize))+((playerMapBuild.winfo_width()//d.mapSize)), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//d.mapSize))*(playerMapBuild.winfo_height()//d.mapSize))+((playerMapBuild.winfo_height()//d.mapSize)//2),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
                    else:
                        playerMapBuild.create_image((((playerMapBuild.winfo_pointerx() - playerMapBuild.winfo_rootx())//(playerMapBuild.winfo_width()//d.mapSize))*(playerMapBuild.winfo_width()//d.mapSize))+((playerMapBuild.winfo_width()//d.mapSize)//2), (((playerMapBuild.winfo_pointery() - playerMapBuild.winfo_rooty())//(playerMapBuild.winfo_height()//d.mapSize))*(playerMapBuild.winfo_height()//d.mapSize))+((playerMapBuild.winfo_height()//d.mapSize)//2),image=imgSelect,tags=str(allBoatType[type])+"BoatSelect")
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
    if page == partyPage:
    
        # Affichage de la grille de l'utilisateur
        playerMap.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
        mapZoneUser.delete("all")
        playerMap.delete("all")
        cases = []
        for i in range(d.mapSize):
            cases_i=[]
            for j in range(d.mapSize):
                if mapRead(playerMapSelect,j+1,i+1)[1] == "DD":
                    caseColor="black"
                elif mapRead(playerMapSelect,j+1,i+1)[0] != "--" and mapRead(playerMapSelect,j+1,i+1)[1][0] == "X":
                    caseColor="red"
                elif mapRead(playerMapSelect,j+1,i+1)[0] == "--" and mapRead(playerMapSelect,j+1,i+1)[1][0] == "X":
                    caseColor="steelblue"
                else:
                    caseColor="steelBlue3"
                cases_i.append(playerMap.create_rectangle((j*(playerMap.winfo_width()/d.mapSize)), (i*(playerMap.winfo_height()/d.mapSize)), ((j+1)*(playerMap.winfo_width()/d.mapSize)-int(2*(globalSize*0.5+0.5))), ((i+1)*(playerMap.winfo_height()/d.mapSize)-int(2*(globalSize*0.5+0.5))),outline=caseColor,fill=caseColor))
            cases.append(cases_i)

        # Affichage des bateau dans la map de l'utilisateur
        boatImgInMap(playerMap,playerMapSelect,False)

        # Affichage des lettres
        if showLetter:
            for x in range(d.mapSize):
                if inversLetter:
                    mapZoneUser.create_text(mapZoneUser.winfo_width()//2-playerMap.winfo_width()//2+playerMap.winfo_width()/d.mapSize*(x+0.5),mapZoneUser.winfo_height()//2-playerMap.winfo_height()//2-5*globalSize,text=lettre[x],fill="steelBlue4",anchor=S)
                else:
                    mapZoneUser.create_text(mapZoneUser.winfo_width()//2-playerMap.winfo_width()//2+playerMap.winfo_width()/d.mapSize*(x+0.5),mapZoneUser.winfo_height()//2-playerMap.winfo_height()//2-5*globalSize,text=str(x+1),fill="steelBlue4",anchor=S)
            for y in range(d.mapSize):
                if inversLetter:
                    mapZoneUser.create_text(mapZoneUser.winfo_width()//2-playerMap.winfo_width()//2-10*globalSize,mapZoneUser.winfo_height()//2-playerMap.winfo_height()//2+playerMap.winfo_width()/d.mapSize*(y+0.5),text=str(y+1),fill="steelBlue4",anchor=E)
                else:
                    mapZoneUser.create_text(mapZoneUser.winfo_width()//2-playerMap.winfo_width()//2-10*globalSize,mapZoneUser.winfo_height()//2-playerMap.winfo_height()//2+playerMap.winfo_width()/d.mapSize*(y+0.5),text=lettre[y],fill="steelBlue4",anchor=E)

        # Affichage de la grille de l'adversaire
        ennemieMap.place(width = 300*globalSize, height = 300*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)
        if d.strikerMap == d.playerMapSelect and not d.ennemieMapSelect in tmpAtqDone:
            ennemieMap.config(cursor="crosshair")
        else:
            ennemieMap.config(cursor="arrow")
        mapZoneEnnemie.delete("all")
        ennemieMap.delete("all")
        cases = []
        for i in range(d.mapSize):
            cases_i=[]
            for j in range(d.mapSize):
                if mapRead(d.ennemieMapSelect,j+1,i+1)[1] == "DD":
                    caseColor="black"
                elif mapRead(d.ennemieMapSelect,j+1,i+1)[0] != "--" and mapRead(d.ennemieMapSelect,j+1,i+1)[1][0] == "X":
                    caseColor="red"
                elif mapRead(d.ennemieMapSelect,j+1,i+1)[0] == "--" and mapRead(d.ennemieMapSelect,j+1,i+1)[1][0] == "X":
                    caseColor="steelblue"
                else:
                    caseColor="steelBlue3"
                if d.strikerMap == d.playerMapSelect and d.ennemieMapSelect and playerDeathData[d.ennemieMapSelect -1] == False and not playerDeathData[playerMapSelect-1] and mapRead(d.ennemieMapSelect,j+1,i+1)[1] == "--" and not d.ennemieMapSelect in tmpAtqDone and not atqDone:
                    cases_i.append(ennemieMap.create_rectangle((j*(ennemieMap.winfo_width()/d.mapSize)), (i*(ennemieMap.winfo_height()/d.mapSize)), ((j+1)*(ennemieMap.winfo_width()/d.mapSize)-int(2*(globalSize*0.5+0.5))), ((i+1)*(ennemieMap.winfo_height()/d.mapSize)-int(2*(globalSize*0.5+0.5))),outline=caseColor,activeoutline="white",fill=caseColor,activewidth=1*globalSize))
                else:
                    cases_i.append(ennemieMap.create_rectangle((j*(ennemieMap.winfo_width()/d.mapSize)), (i*(ennemieMap.winfo_height()/d.mapSize)), ((j+1)*(ennemieMap.winfo_width()/d.mapSize)-int(2*(globalSize*0.5+0.5))), ((i+1)*(ennemieMap.winfo_height()/d.mapSize)-int(2*(globalSize*0.5+0.5))),outline=caseColor,fill=caseColor))
            cases.append(cases_i)

        # Affichage des bateau dans la map de l'adversaire
        boatImgInMap(ennemieMap,d.ennemieMapSelect,True)

        # Affichage des lettres
        if showLetter:
            for x in range(d.mapSize):
                if inversLetter:
                    mapZoneEnnemie.create_text(mapZoneEnnemie.winfo_width()//2-ennemieMap.winfo_width()//2+ennemieMap.winfo_width()/d.mapSize*(x+0.5),mapZoneEnnemie.winfo_height()//2-ennemieMap.winfo_height()//2-5*globalSize,text=lettre[x],fill="steelBlue4",anchor=S)
                else:
                    mapZoneEnnemie.create_text(mapZoneEnnemie.winfo_width()//2-ennemieMap.winfo_width()//2+ennemieMap.winfo_width()/d.mapSize*(x+0.5),mapZoneEnnemie.winfo_height()//2-ennemieMap.winfo_height()//2-5*globalSize,text=str(x+1),fill="steelBlue4",anchor=S)
            for y in range(d.mapSize):
                if inversLetter:
                    mapZoneEnnemie.create_text(mapZoneEnnemie.winfo_width()//2-ennemieMap.winfo_width()//2-10*globalSize,mapZoneEnnemie.winfo_height()//2-ennemieMap.winfo_height()//2+ennemieMap.winfo_width()/d.mapSize*(y+0.5),text=str(y+1),fill="steelBlue4",anchor=E)
                else:
                    mapZoneEnnemie.create_text(mapZoneEnnemie.winfo_width()//2-ennemieMap.winfo_width()//2-10*globalSize,mapZoneEnnemie.winfo_height()//2-ennemieMap.winfo_height()//2+ennemieMap.winfo_width()/d.mapSize*(y+0.5),text=lettre[y],fill="steelBlue4",anchor=E)

        if d.playerDeathData[d.ennemieMapSelect-1] == True:
            ennemieName.config(text="Player "+str(d.ennemieMapSelect),fg="red")
        else:
            ennemieName.config(text="Player "+str(d.ennemieMapSelect),fg="black")
        ennemieName.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0.5,rely=1,y=-10,anchor = S)

        if d.mapNumber > 2 :
            if len(d.playerDeathData) > 3:
                if d.ennemieMapSelect + 1 == d.playerMapSelect or d.playerDeathData[ennemieMapSelect+1] == True:
                    button_nextMap.config(text="Player "+str(d.ennemieMapSelect+2))
            else:
                button_nextMap.config(text="Player "+str(d.ennemieMapSelect+1))
            if d.ennemieMapSelect - 1 == playerMapSelect or d.playerDeathData[ennemieMapSelect-1] == True :
                button_backMap.config(text="Player "+str(d.ennemieMapSelect-2))
            else:
                button_backMap.config(text="Player "+str(d.ennemieMapSelect-1))

            if d.ennemieMapSelect < d.mapNumber and not (d.playerMapSelect == d.mapNumber and d.ennemieMapSelect+1 == d.mapNumber or d.playerDeathData[-1] == True):
                button_nextMap.place(height=30,width=50,relheight=0.025,relwidth=0.1,relx=0.9,rely=1,y=-10,anchor = SE)
            else:
                button_nextMap.place_forget()
            if d.ennemieMapSelect > 1 and not (d.playerMapSelect == 1 and d.ennemieMapSelect-1 == 1 or d.playerDeathData[0] == True):
                button_backMap.place(height=30,width=50,relheight=0.025,relwidth=0.1,relx=0.1,rely=1,y=-10,anchor = SW)
            else:
                button_backMap.place_forget()
        else:
            button_nextMap.place_forget()
            button_backMap.place_forget()

text_gameTitle = Label(mainMenuPage,text="BATTLESHIP WARFARE",fg="black",font=titleStyle)
text_gameTitle.place(relx = 0.5, rely = 0.45, anchor = S)

button_play = ttk.Button(mainMenuPage, text=lg("Jouer"),command=lambda:[switch(selectPartyPage)],takefocus = 0)
button_play.place(height=20,relheight=0.05,relwidth=0.25,relx = 0.5, rely = 0.55,y=-20, anchor = CENTER)

button_settings = ttk.Button(mainMenuPage, text=lg("Réglage"),command=lambda:switch(settingsPage),takefocus = 0)
button_settings.place(height=20,relheight=0.05, relwidth=0.25,relx = 0.5, rely = 0.6, anchor = CENTER)

button_credit = ttk.Button(mainMenuPage, text=lg("Crédit"),command=lambda:switch(creditsPage),takefocus = 0)
button_credit.place(height=20,relheight=0.05, relwidth=0.25,relx = 0.5, rely = 0.65,y=20, anchor = CENTER)

button_exit = ttk.Button(mainMenuPage, text=lg("Quitter"),command=lambda:app.destroy(),takefocus = 0)
button_exit.place(height=15,relheight=0.05, relwidth=0.1,relx=1,rely=1,x=-10,y=-10,anchor = SE)

# Settings

button_back = ttk.Button(settingsPage, text=lg("Retour"),command=lambda:switch(mainMenuPage),takefocus = 0)
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

button_back = ttk.Button(creditsPage, text=lg("Retour"),command=lambda:switch(mainMenuPage),takefocus = 0)
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

text_commingSoon = Label(creditsPage,text=lg("Prochainement"),bg="black",fg="white")
text_commingSoon.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.5, anchor = CENTER)

# Select Party

text_selectGame = Label(selectPartyPage,text=lg("Sélectionnez un mode de jeu"),fg="black")
text_selectGame.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.05, anchor = CENTER)

button_selectIAGame = ttk.Button(selectPartyPage, text=lg("Standard").upper(),command=lambda:[switch(prePartyPage),selectGameMode(0),creatmap(),refreshImg()],takefocus = 0)
button_selectIAGame.place(relwidth=0.4, relheight=0.75,relx = 0.3, rely = 0.475, anchor = CENTER)

button_selectCustomGame = ttk.Button(selectPartyPage, text=lg("Personnalisé").upper(),command=lambda:[switch(prePartyPage),selectGameMode(1),creatmap(),refreshImg()],takefocus = 0)
button_selectCustomGame.place(relwidth=0.4, relheight=0.75,relx = 0.7, rely = 0.475, anchor = CENTER)

button_back = ttk.Button(selectPartyPage, text=lg("Retour"),command=lambda:switch(mainMenuPage),takefocus = 0)
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

# Pre-Party

boatBuildZone = Canvas(prePartyPage)
boatBuildZone.place(relheight=1,relwidth=1,relx=0.5,rely=0.5,anchor=CENTER)

playerMapBuild = Canvas(boatBuildZone,bg="steelBlue1")

text_selectGame = Label(prePartyPage,fg="black")
text_selectGame.place(width=100,relheight=0.075,relwidth=0.1,relx = 0.5, rely = 0, anchor = N)

button_back = ttk.Button(prePartyPage, text=lg("Retour"),command=lambda:switch(selectPartyPage),takefocus = 0)
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

button_launchGame = ttk.Button(prePartyPage, text=lg("/// LANCER ///"),command=laucheGame,takefocus = 0)
button_launchGame.place(height=50,width=100,relheight=0.05,relwidth=0.15,relx=1,rely=1,x=-10,y=-10,anchor = SE)

button_creatyRandomMap = ttk.Button(prePartyPage, text=lg("Aléatoire"),command=lambda:[creatmap(),creatRandomMap(d.playerMapSelect)],takefocus = 0)
button_creatyRandomMap.place(height=30,width=100,relheight=0.025,relwidth=0.15,relx=1,rely=0.95,x=-10,y=-65,anchor = SE)

# Party

mapZone = Frame(partyPage)
mapZone.place(relx = 0.5, rely = 0.5, relwidth = 1, relheight = 1,anchor = CENTER)
mapZoneUser = Canvas(mapZone)
mapZoneUser.place(relheight=1,relwidth=0.5)
mapZoneEnnemie = Canvas(mapZone,)
mapZoneEnnemie.place(relheight=1,relwidth=0.5, relx=0.5)
playerMap = Canvas(mapZoneUser,bg="steelBlue1")
ennemieMap = Canvas(mapZoneEnnemie,bg="steelBlue1")

textMaster = Label(partyPage,fg="white")
textMaster.place(height=10,relheight=0.05,relwidth=1,relx = 0.5, rely = 0, anchor = N)

button_backToMainMenu = ttk.Button(partyPage, text=lg("Menu principal"),command=stopGame,takefocus = 0)
button_backToMainMenu.place(height=30,width=75,relheight=0.025,relwidth=0.1,relx=0,rely=1,x=10,y=-10,anchor = SW)

ennemieName = Label(mapZoneEnnemie)

button_nextMap = ttk.Button(mapZoneEnnemie, text="Player "+str(ennemieMapSelect+1),command=lambda:nextEnnemieMap(1),takefocus = 0)
button_backMap = ttk.Button(mapZoneEnnemie, text="Player "+str(d.ennemieMapSelect-1),command=lambda:nextEnnemieMap(0),takefocus = 0)

### --- Main execution --- ###

def ihmStart():
    app.minsize(800, 450)
    app.maxsize(app.winfo_screenwidth(),app.winfo_screenheight())
    app.geometry('%dx%d+%d+%d' % (W, H, (app.winfo_screenwidth()/2) - (W/2), (app.winfo_screenheight()/2) - (H/2)))
    app.title("Battleship Warfare")
    app.iconbitmap("../gui/image/logo.ico")
    refreshImg()
    creatmap()
    # Ouverture du menu
    switch(startPage)
    app.after(1,lambda:switch(mainMenuPage))