# --- Imporations des données
from tkinter.font import BOLD
from data import *

# --- Affectation des variables
global globalSize
case_size = 15
cases = []


# Preset
fullScreen = False
W  = 800
H = 450
gameMapViewV = 0
globalSize = 0

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

    
def refreshGUI():
    global titleStyle
    titleStyle.configure(size=int(50*globalSize))
    default_font.configure(family="Arial",size=int(11*(globalSize*0.5+0.5)),weight=BOLD)
    refreshMap()

# Fonction d'action de fenêtre
def switch(frame):
    for widget in window.winfo_children():
        widget.pack_forget()
    window.pack(expand = 1, fill =BOTH)
    frame.pack(expand = 1, fill =BOTH)

# Redimentionnement
def refreshGlobalSize(event):
    global globalSize
    globalSize = 1 + (app.winfo_height() - 450)*(app.winfo_width() - 800)*0.0000025
    refreshGUI()

### --- Élément des page des fenêtres --- ###

def refreshMap():
    global globalSize
    mapZone.place(relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.8,anchor = CENTER)
    mapZoneUser.place(relheight=1,relwidth=0.5)
    mapZoneEnnemie.place(relheight=1,relwidth=0.5, relx=0.5)
    userMap.place(width = 330*globalSize, height = 330*globalSize,relx = 0.5, rely = 0.5, anchor = CENTER)

    
    # Affichage
        
    # for ligne in range(mapSize):
    #     cases_ligne=[]
    #     for colonne in range(mapSize):
    #         cases_ligne.append(gridecase.create_rectangle((colonne*case_size+2)*globalSize, (ligne*case_size+2)*globalSize, ((colonne+1)*case_size+2)*globalSize, ((ligne+1)*case_size+2)*globalSize))
    #     cases.append(cases_ligne)

    # for i in range(mapSize):
    #     for j in range(mapSize):
    #         if mapRead(map+1,j+1,i+1)[1] == "D":
    #             gridecase.itemconfigure(cases[i][j], outline = "steelblue", fill="steelblue4")
    #         elif mapRead(map+1,j+1,i+1)[0] != "--" and mapRead(map+1,j+1,i+1)[1] == "X":
    #             gridecase.itemconfigure(cases[i][j], outline = "", fill="lightcoral")
    #         elif mapRead(map+1,j+1,i+1)[0] == "--" and mapRead(map+1,j+1,i+1)[1] == "X":
    #             gridecase.itemconfigure(cases[i][j], outline = "steelblue",fill="red")
    #         elif mapRead(map+1,j+1,i+1)[0] != "--":
    #             gridecase.itemconfigure(cases[i][j], outline = "gainsboro",fill="lavender")
    #         else:
    #             gridecase.itemconfigure(cases[i][j], outline = "steelblue",fill="steelblue3")

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

text_commingSoon = Label(selectPartyPage,text=lg("Sélectionnez un mode de jeu"),fg="black")
text_commingSoon.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.05, anchor = CENTER)

button_selectIAGame = ttk.Button(selectPartyPage, text='STANDARD',command=lambda:switch(prePartyPage))
button_selectIAGame.place(relwidth=0.4, relheight=0.75,relx = 0.3, rely = 0.475, anchor = CENTER)

button_selectCustomGame = ttk.Button(selectPartyPage, text=lg("PERSONALISÉ"),command=lambda:switch(prePartyPage))
button_selectCustomGame.place(relwidth=0.4, relheight=0.75,relx = 0.7, rely = 0.475, anchor = CENTER)

button_back = ttk.Button(selectPartyPage, text=lg("Retour"),command=lambda:switch(mainMenuPage))
button_back.place(height=30,width=50,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

# Pre-Party

button_backToMainMenu = ttk.Button(prePartyPage, text=lg("Menu principal"),command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=30,width=100,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

button_launchGame = ttk.Button(prePartyPage, text=lg("/// LANCER ///"),command=lambda:[switch(partyPage),refreshMap()])
button_launchGame.place(height=50,width=150,relheight=0.05,relwidth=0.1,relx=1,rely=1,x=-10,y=-10,anchor = SE)

text_commingSoon = Label(prePartyPage,text=lg("Prochainement"),bg="black",fg="white")
text_commingSoon.place(relheight=0.1,relwidth=1,relx = 0.5, rely = 0.5, anchor = CENTER)

# Party

mapZone = Frame(partyPage)
mapZoneUser = Frame(mapZone)
mapZoneEnnemie = Frame(mapZone)
userMap = Frame(mapZoneUser, bg="lightblue")

button_e = ttk.Button(partyPage, text='CLEAR',command=lambda:[creatmap(),refreshMap()])
button_e.grid(row = 0, column = 0,padx=10, pady=10)

button_r = ttk.Button(partyPage, text='TEST ATQ',command=lambda:[atq(1,2,7,7),refreshMap()])
button_r.grid(row = 0, column = 1,padx=10, pady=10)

button_backToMainMenu = ttk.Button(partyPage, text=lg("Menu principal"),command=lambda:switch(mainMenuPage))
button_backToMainMenu.place(height=30,width=100,relheight=0.025,relwidth=0.05,relx=0,rely=1,x=10,y=-10,anchor = SW)

### --- Main execution --- ###

def battleship():
    app.title("BW")
    app.minsize(800, 450)
    app.maxsize(app.winfo_screenwidth(),app.winfo_screenheight())
    app.geometry('%dx%d+%d+%d' % (W, H, (app.winfo_screenwidth()/2) - (W/2), (app.winfo_screenheight()/2) - (H/2)))
    app.update()
    app.bind("<Configure>",refreshGlobalSize)
    app.bind("<F11>",setFullScreen)
    # Ouverture du menu
    switch(mainMenuPage)
    refreshGUI()