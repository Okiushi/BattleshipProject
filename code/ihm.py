# --- Imporations des données
from data import *

# --- Affectation des variables
globalSize = 2
case_size = 15
cases = []
gameMapViewV = 0
W  = 800
H = 450
#### ---- Ajout des pages

# Conteneur des pages
window = Frame(app)

# Page
mainMenuPage = Frame(window)
selectPartyPage = Frame(window)
prePartyPage = Frame(window)
partyPage = Frame(window)
settingsPage = Frame(window)
creditsPage = Frame(window)

### --- Action de boutton --- ###

# Navigation de fenêtre
def switch(frame):
    for widget in window.winfo_children():
        widget.pack_forget()
    window.pack(expand = 1, fill =BOTH)
    frame.pack(expand = 1, fill =BOTH)

### --- Élément des page des fenêtres --- ###

# Party
mapZone = Frame(partyPage, width = 10*globalSize, height = 100*globalSize)
mapZone.place(relx = 0.5, rely = 0.5, anchor = CENTER)
mapZone.columnconfigure(0, weight=3)
mapZone.columnconfigure(1, weight=1)
mapPlayerZone = Frame(mapZone, width = 100*globalSize, height = 100*globalSize)
if gameMapViewV:
    mapPlayerZone.grid(row = 1, column = 0)
else:
    mapPlayerZone.grid(row = 0, column = 0)

mapAdversZone = Frame(mapZone, width = 100*globalSize, height = 100*globalSize)
if gameMapViewV:
    mapAdversZone.grid(row = 0, column = 0)
else:
    mapAdversZone.grid(row = 0, column = 1)

mapAdversZoneScrollbar_frame = Canvas(mapAdversZone)
mapAdversZoneScrollbar_frame.grid(row=0, column=0, sticky=NSEW)

def refreshMap():
    for map in range(mapNumber):
        if map == playerMap-1:
            gridecase = Canvas(mapPlayerZone, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize)
            gridecase.grid(row = 0, column = 0,columnspan=mapNumber)
            playerNameLabel = Label(mapPlayerZone,text="Player"+str(map+1),bg="black",fg="lightblue")
            playerNameLabel.grid(row = 1,column = 0,columnspan=mapNumber,ipadx=10)
        else:
            gridecase = Canvas(mapAdversZoneScrollbar_frame, width = (mapSize*case_size+2)*globalSize, height = (mapSize*case_size+2)*globalSize)
            gridecase.grid(row = 0, column = map)
            playerNameLabel = Label(mapAdversZoneScrollbar_frame,text="Player"+str(map+1),bg="black",fg="red")
            playerNameLabel.grid(row = 1,column = map,ipadx=10)
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
                    gridecase.itemconfigure(cases[i][j], outline = "", fill="lightcoral")
                elif mapRead(map+1,j+1,i+1)[0] == "--" and mapRead(map+1,j+1,i+1)[1] == "X":
                    gridecase.itemconfigure(cases[i][j], outline = "steelblue",fill="red")
                elif mapRead(map+1,j+1,i+1)[0] != "--":
                    gridecase.itemconfigure(cases[i][j], outline = "gainsboro",fill="lavender")
                else:
                    gridecase.itemconfigure(cases[i][j], outline = "steelblue",fill="steelblue3")

# MainMenu

text_commingSoon = Label(mainMenuPage,text="BATTLESHIP PROJECT",fg="black",font=("Impact", 50))
text_commingSoon.place(relx = 0.5, rely = 0.5, anchor = CENTER,y=-100)

button_play = ttk.Button(mainMenuPage, text='PLAY',command=lambda:[switch(selectPartyPage)])
button_play.place(height=50, relwidth=0.25,relx = 0.5, rely = 0.5, anchor = CENTER)

button_settings = ttk.Button(mainMenuPage, text='SETTINGS',command=lambda:switch(settingsPage))
button_settings.place(height=50, relwidth=0.25,relx = 0.5, rely = 0.5, anchor = CENTER,y=50)

button_credit = ttk.Button(mainMenuPage, text='CREDIT',command=lambda:switch(creditsPage))
button_credit.place(height=50, relwidth=0.25,relx = 0.5, rely = 0.5, anchor = CENTER,y=100)

button_exit = ttk.Button(mainMenuPage, text='EXIT',command=lambda:app.destroy())
button_exit.place(height=50,width=50,relx=1,rely=1,x=-10,y=-10,anchor = SE)

# Settings

button_backToMainMenu = ttk.Button(settingsPage, text='Back',command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=15,width=30,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

text_commingSoon = Label(settingsPage,text="Comming soon",bg="black",fg="white")
text_commingSoon.place(height=30, relwidth=1,relx = 0.5, rely = 0.5, anchor = CENTER)

# Credits

button_backToMainMenu = ttk.Button(creditsPage, text='Back',command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=15,width=30,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

text_commingSoon = Label(creditsPage,text="Comming soon",bg="black",fg="white")
text_commingSoon.place(height=30, relwidth=1,relx = 0.5, rely = 0.5, anchor = CENTER)

# Select Party

button_backToMainMenu = ttk.Button(selectPartyPage, text='Back',command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=15,width=30,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

button_selectIAGame = ttk.Button(selectPartyPage, text='IA',command=lambda:switch(prePartyPage))
button_selectIAGame.place(relwidth=0.3, relheight=0.8,relx = 0.2, rely = 0.5, anchor = CENTER)

button_selectPlayerGame = ttk.Button(selectPartyPage, text='PLAYER',command=lambda:switch(prePartyPage))
button_selectPlayerGame.place(relwidth=0.3, relheight=0.8,relx = 0.5, rely = 0.5, anchor = CENTER)

button_selectCustomGame = ttk.Button(selectPartyPage, text='CUSTOM',command=lambda:switch(prePartyPage))
button_selectCustomGame.place(relwidth=0.3, relheight=0.8,relx = 0.8, rely = 0.5, anchor = CENTER)

# Pre-Party

button_backToMainMenu = ttk.Button(prePartyPage, text='Main menu',command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=15,width=60,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

button_launchGame = ttk.Button(prePartyPage, text='/// LAUNCH ///',command=lambda:[switch(partyPage),refreshMap()])
button_launchGame.place(height=50,width=200,relheight=0.05,relwidth=0.1,relx=1,rely=1,x=-10,y=-10,anchor = SE)

text_commingSoon = Label(prePartyPage,text="Comming soon",bg="black",fg="white")
text_commingSoon.place(height=30, relwidth=1,relx = 0.5, rely = 0.5, anchor = CENTER)

# Party

# button_r = ttk.Button(partyPage, text='TEST ATQ',command=lambda:[atq(1,2,7,7),refreshMap()])
# button_r.grid(row = 0, column = 0,padx=10, pady=10)

# button_e = ttk.Button(partyPage, text='Clear',command=lambda:[creatmap(),refreshMap()])
# button_e.grid(row = 1, column = 0,padx=10, pady=10)

button_backToMainMenu = ttk.Button(partyPage, text='Main menu',command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=15,width=60,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

### --- Main execution --- ###

def battleship():
    app.title("Battleship")
    app.minsize(800, 450)
    app.maxsize(app.winfo_screenwidth(),app.winfo_screenheight())
    app.geometry('%dx%d+%d+%d' % (W, H, (app.winfo_screenwidth()/2) - (W/2), (app.winfo_screenheight()/2) - (H/2)))

    # Ouverture du menu
    switch(mainMenuPage)