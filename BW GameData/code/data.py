#### ---- Importation des modules du projet

# Prise en charge de séléction aléatoire
from random import randint
import ihm

# Import des données stocké
import json

#### ---- Initalisation des variables global

global gameMode
global mapSize
global mapNumber
global gameDataBoat
global atqDone
global ennemieMapSelect

#### ---- Affectation des variables global

# Paramètre de party
mapData = []
atqHistory = []
boatData = []
gameDataBoat = ["a","c","f","s","p"]
allBoatType = ["a","c","f","s","p"]
boatGuiData = []
playerDeathData = []
tmpAtqDone = []
inGame = False
adversAtqAdvers = True
ennemieMapSelect = 2

lang = 1
mapSize = 10
playerMapSelect = 1
mapNumber = 3
gameMode = 0
testAddBoat = 0
lastBuildBoat = ""
atqDone = False
allAtqDone = False
strikerMap = 1

#### ---- Interaction utilisateur

def laucheGame():
    global inGame
    global strikerMap
    global ennemieMapSelect
    global atqDone
    global allAtqDone
    for i in range(mapNumber):
        if i != playerMapSelect:
            creatRandomMap(i)
    inGame = True
    strikerMap = 1
    atqDone = False
    allAtqDone = False
    tmpAtqDone.clear()
    if playerMapSelect != 1:
        ennemieMapSelect = 1
        ihm.textMaster.config(text="C'est au joueur "+str(strikerMap)+" de commencer",fg="grey")
    else:
        ihm.textMaster.config(text="C'est à vous de commencer, veuillez exécuter vos tires sur chaque flotte adverse",fg="black")
        ennemieMapSelect = 2
    ihm.refreshToure()
    ihm.switch(ihm.partyPage)

def stopGame():
    global inGame 
    inGame = False
    ihm.switch(ihm.mainMenuPage)

# Attaquer une position ennemie
def addBoat(map,type,x,y,direction):
    global lastBuildBoat
    initialX = x
    initialY = y
    if type == "a":
        size = 4
    if type == "c":
        size = 3
    if type == "f":
        size = 2
    if type == "s":
        size = 2
    if type == "p":
        size = 1
    if direction == "N":
        x2 = x
        y2 = y + size//2
        y -= size//2 + int(size%2)
    elif direction == "S":
        x2 = x
        y2 = y + size//2 + int(size%2)
        y -= size//2
    elif direction == "W":
        x2 = x + size//2
        x -= size//2 + int(size%2)
        y2 = y 
    else:
        x2 = x + size//2 + int(size%2)
        y2 = y
        x -= size//2
    noBoat = 1
    if x>0 and x2<mapSize+1 and y>0 and y2<mapSize+1:
        for i in range(x,x2+1):
            for j in range(y,y2+1):
                if mapRead(map,i,j)[0] != "--":
                    noBoat = 0
        if not type in boatData[map-1] and noBoat:
            occurence = 0
            while type+str(occurence) in boatData[map-1]:
                occurence += 1
            if type+str(occurence) not in boatData[map-1]:
                mapZoneModifType(map,type+str(occurence),x,y,x2,y2)
                boatData[map-1] += [type+str(occurence)]
                lastBuildBoat = type+str(occurence)
                boatGuiData[map-1].append([type+str(occurence),initialX,initialY,direction])

def removeBoat(map,type):
    mapZoneModifType(map,"--",BoatReadPos(map,type)[1],BoatReadPos(map,type)[2],BoatReadPos(map,type)[3],BoatReadPos(map,type)[4])
    boatData[map-1].remove(type)
    for boat in range(len(boatGuiData[map-1])):
        if boatGuiData[map-1][boat][0] == type:
            del boatGuiData[map-1][boat]
            break
            
# --- Attaque d'un joueur
def atq(user,map,posX,posY):
    global atqDone
    global allAtqDone
    type = mapRead(map,posX,posY)[0]
    if mapData[map-1][posY-1][posX-1][1] != "DD" and mapData[map-1][posY-1][posX-1][1] == "--":
        mapData[map-1][posY-1][posX-1][1] = "X"+str(user)
        tmpAtqDone.append(map)
        atqDone = True
        if len(tmpAtqDone) == playerDeathData.count(False) -1:
            allAtqDone = True

    if not [posX,posY,type,mapRead(map,posX,posY)[1]] in atqHistory[user-1][map-1]:
        atqHistory[user-1][map-1] += [[posX,posY,type,mapRead(map,posX,posY)[1]]]
    # Rafraichissement des touchés-coulés
    for map in range(len(mapData)):
        totalBoatDeath = 0
        for boat in range(len(boatData[map])):
            counter = 0
            for x in range(len(mapData[map])):
                for y in range(len(mapData[map][x])):
                    if boatData[map][boat] == mapRead(map+1,x,y)[0] and (mapRead(map+1,x,y)[1][0] == "X" or mapRead(map+1,x,y)[1] == "DD"):
                        counter += 1
            if counter >= BoatReadPos(map+1,boatData[map][boat])[0]:
                mapZoneModifStatus(map+1,"DD",BoatReadPos(map+1,boatData[map][boat])[1],BoatReadPos(map+1,boatData[map][boat])[2],BoatReadPos(map+1,boatData[map][boat])[3],BoatReadPos(map+1,boatData[map][boat])[4])
                totalBoatDeath += 1
        if totalBoatDeath >= len(gameDataBoat):
            playerDeathData[map] = True
    # Trembler l'écrent si touché
    if type != "--":
        ihm.shake(4,0.2)

#### ---- Manipulation des maps

# Création des maps
def creatmap():
    global testAddBoat
    testAddBoat = 0
    mapData.clear()
    atqHistory.clear()
    boatData.clear()
    boatGuiData.clear()
    playerDeathData.clear()
    for i in range(mapNumber):
        mapData.append([])
        atqHistory .append([])
        boatData.append([])
        boatGuiData.append([])
        playerDeathData.append(False)
        for i2 in range(mapNumber):
            atqHistory[i] += [[]]
        for j in range(mapSize):
            mapData[i] += [[]*mapSize]
            for k in range(mapSize):
                mapData[i][j] += [["--","--"]]

# Lire une position
def mapRead(map,posX,posY):
    return mapData[map-1][posY-1][posX-1]

# Modifier le type d"une position
def mapPosModifType(map,modiftype,posX,posY):
    mapData[map-1][posY-1][posX-1][0] = modiftype

# Modifier le status d"une position
def mapPosModifStatus(map,modifstatus,posX,posY):
    mapData[map-1][posY-1][posX-1][1] = modifstatus

# Obtenire les positions de zone d"un élément
def BoatReadPos(map,type):
    pos = [0]
    for i in range(len(mapData[map-1])):
        for j in range(len(mapData[map-1][i])):
            if mapData[map-1][i][j][0] == type:
                pos += j+1,i+1
                pos[0] += 1
    if len(pos) >= 5:
        pos = [pos[0],pos[1],pos[2],pos[-2],pos[-1]]
    return pos

# Modifier le type d"une zone
def mapZoneModifType(map,modiftype,posX1,posY1,posX2,posY2):
    if posX2>posX1:
        for i in range(posX2-posX1+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifType(map,modiftype,posX1+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifType(map,modiftype,posX1+i,posY2+j)   
    else:
        for i in range(posX1-posX2+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifType(map,modiftype,posX2+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifType(map,modiftype,posX2+i,posY2+j)  

# Modifier le status d"une zone
def mapZoneModifStatus(map,modifstatus,posX1,posY1,posX2,posY2):
    if posX2>posX1:
        for i in range(posX2-posX1+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifStatus(map,modifstatus,posX1+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifStatus(map,modifstatus,posX1+i,posY2+j)   
    else:
        for i in range(posX1-posX2+1):
            if posY2>posY1:
                for j in range(posY2-posY1+1):
                    mapPosModifStatus(map,modifstatus,posX2+i,posY1+j)
            else:
                for j in range(posY1-posY2+1):
                    mapPosModifStatus(map,modifstatus,posX2+i,posY2+j)  
                    
def boatDataTypeCount(type,map):
    count = 0
    for i in range(len(boatData[map-1])):
        if boatData[playerMapSelect-1][i][0] == type:
            count += 1
    return count

# Voici le morceau de code qui convertira nos lettre en chiffre, il fontionne pour la majuscule et minuscul: " ord(posX.lower())-96 "

# Gestion de la langue
def lg(text):
    return langDico[lang][langDico[1].index(text)]

langDico = [# Anglais 14
            ["Play","Settings","Credit","Exit","Back","Main menu","Standard","Custom","Comming soon","/// LAUNCH ///","Select a game mode","Next","Back","Random"],
            # Français 14
            ["Jouer","Réglage","Crédit","Quitter","Retour","Menu principal","Standard","Personnalisé","Prochainement","/// LANCER ///","Sélectionnez un mode de jeu","Suivant","Précédent","Aléatoire"],
            # Allemand 14
            ["Spielen", "Einstellungen", "Guthaben", "Beenden", "Zurück", "Hauptmenü", "Standard", "Benutzerdefiniert", "Demnächst","/// LANCER ///", "Spielmodus wählen", "Weiter", "Zurück","Zufällig"],
            # Espagnol 14
            ["Jugar", "Ajustes", "Créditos", "Salir", "Atrás", "Menú principal", "Estándar", "Personalizado", "Siguiente","/// Lanza ///", "Selecciona un modo de juego", "Siguiente", "Anterior","Al azar","Aleatório"],
            # Portugais 14
            ["Jogar", "Definir", "Crédito", "Sair", "Voltar", "Menu principal", "Padrão", "Personalizado", "Próximo","/// ALMOÇO //", "Seleccionar um modo de jogo", "Próximo", "Anterior"],
            # Japonais 14
            ["再生", "設定", "クレジット", "終了", "戻る", "メインメニュー", "標準", "カスタム", "近日公開", "/// START ///", "ゲームモードを選択してください","「次へ」","「前へ」","ランダム"],
            # Coréen 14
            ["재생","설정","크레딧","종료","뒤로","주 메뉴","표준","사용자 지정","출시 예정","/// 시작 ///"," 게임 모드 선택","다음","이전","무작위의"],
            # Chinois 14
            ["播放", "设置", "积分", "退出", "返回", "主菜单", "标准", "自定义", "下一步", "/// LAUNCH ///", "选择一个游戏模式", "下一步", "上一步","随机的"]
            ]

def creatRandomMap(map):
    direction = "NSEW"
    testAddBoat = 0
    while testAddBoat < len(gameDataBoat):
        addBoat(map,gameDataBoat[testAddBoat],randint(1,mapSize),randint(1,mapSize),direction[randint(0,3)])
        if testAddBoat < len(boatData[map-1]):
            testAddBoat += 1

def IaAtq(map,atqMap):
    
    lettre = "ABCDEFGHIJKLMNOPQRST"

    focus = False
    atqX = randint(1,mapSize)
    atqY = randint(1,mapSize)
    # Focus une position touché il y en à une dans la carte à attaquer sinon choisi un position aléatoire
    for x in range(1,mapSize+1):
        for y in range(1,mapSize+1):
            if mapRead(atqMap,x,y)[1][0] == "X" and mapRead(atqMap,x,y)[0] != "--":
                focus = True
                initialX = x
                initialY = y
                break
        if mapRead(atqMap,x,y)[1][0] == "X" and mapRead(atqMap,x,y)[0] != "--":
            break
            
    if focus:                     
        # Si il n'y à rien à côté, fait une croix jusqu'a trouver la position voisine
        N=["OO","OO"];E=["OO","OO"];S=["OO","OO"];W=["OO","OO"]
        atqX = initialX
        atqY = initialY
        HdirectionTest = False
        VdirectionTest = False

        if initialY - 1 > 0:
            N = mapRead(atqMap,initialX,initialY-1)
                
        if initialX + 1 <= mapSize:
            E = mapRead(atqMap,initialX+1,initialY)

        if initialY + 1 <= mapSize:
            S = mapRead(atqMap,initialX,initialY+1)

        if initialX - 1 > 0:
            W = mapRead(atqMap,initialX-1,initialY)
        
        if (N[0] != "--" and N[1][0] == "X") or (S[0] != "--" and S[1][0] == "X"):
            HdirectionTest = False
            VdirectionTest = True
            print("Il y à un truc à verticale")
        elif (E[0] != "--" and E[1][0] == "X") or (W[0] != "--" and W[1][0] == "X"):
            HdirectionTest = True
            VdirectionTest = False
            print("Il y à un truc à l'horizontale")

        if not HdirectionTest and not VdirectionTest:
            while mapRead(atqMap,atqX,atqY)[1] != "--":
                atqX = initialX
                atqY = initialY
                direction = randint(0,3)
                if direction == 0 and N[1] == "--":
                    atqY -= 1
                elif direction == 1 and E[1] == "--":
                    atqX += 1
                elif direction == 2 and S[1] == "--":
                    atqY += 1
                elif direction == 3 and W[1] == "--":
                    atqX -= 1

        else:
            Succes = False
            direction = randint(0,1)
            while not Succes:
                # Sur les bateaux détecté à l'horizontale
                if HdirectionTest:
                    print("C'est partie pour tester l'horizontale")
                    horizontaleOk = True
                    while HdirectionTest: # Tant qu'une position non touché n'a pas été trouvé il recommence
                        if not atqX > 0 or not atqX < mapSize + 1: # Si la position testé est hors zone, alors il test une autre direction
                            print("bon je vais checher de l'autre côté c'est la limite en",lettre[atqY-1],atqX)
                            if direction == 0:
                                direction = 1
                            else:
                                direction = 0
                            atqX = initialX
                            if horizontaleOk == False:
                                Succes = True
                                print("Je suis piégé à l'horizontale, je teste la verticale")
                                break
                            else:
                                horizontaleOk = False

                        elif mapRead(atqMap,atqX,atqY)[1] == "--":
                            print("j'ai trouvé, c'est",lettre[atqY-1],atqX)
                            Succes = True
                            break

                        elif mapRead(atqMap,atqX,atqY)[1][0] == "X" and mapRead(atqMap,atqX,atqY)[0] != "--": # Si la position testé est un bateau touché, alors il avance avance dans la direction choisie la position testé
                            print("bon j'avance en",lettre[atqY-1],atqX)
                            if direction == 0:
                                atqX -= 1
                            else:
                                atqX += 1

                        elif (mapRead(atqMap,atqX,atqY)[1][0] == "X" or mapRead(atqMap,atqX,atqY)[1] == "DD") and mapRead(atqMap,atqX,atqY)[0] == "--": # Si la position testé est de l'eau ou un bateau coulé, alors il test une autre direction
                            print("bon je vais changer de côté, c'est le bord içi")
                            if direction == 0:
                                direction = 1
                            else:
                                direction = 0
                            atqX = initialX
                            if horizontaleOk == False:
                                Succes = True
                                print("Je suis piégé à l'horizontale, je teste la verticale")
                                break
                            else:
                                horizontaleOk = False

                # Sur les bateaux détecté à la verticale      
                if VdirectionTest:         
                    verticaleOk = True
                    print("C'est partie pour tester la verticale")
                    while VdirectionTest: # Tant qu'une position non touché n'a pas été trouvé il recommence
                        if not atqY > 0 or not atqY < mapSize + 1: # Si la position testé est hors zone, alors il test une autre direction
                            print("bon je vais checher de l'autre côté c'est la limite en",lettre[atqY-1],atqX)
                            if direction == 0:
                                direction = 1
                            else:
                                direction = 0
                            atqY = initialY
                            if verticaleOk == False:
                                Succes = True
                                print("Je suis piégé à la verticale, je teste l'horizontale")
                                break
                            else:
                                verticaleOk = False

                        elif mapRead(atqMap,atqX,atqY)[1] == "--":
                            print("j'ai trouvé, c'est",lettre[atqY-1],atqX)
                            Succes = True
                            break

                        elif mapRead(atqMap,atqX,atqY)[1][0] == "X" and mapRead(atqMap,atqX,atqY)[0] != "--": # Si la position testé est un bateau touché, alors il avance avance dans la direction choisie la position testé
                            print("bon j'avance en",lettre[atqY-1],atqX)
                            if direction == 0:
                                atqY -= 1
                            else:
                                atqY += 1

                        elif (mapRead(atqMap,atqX,atqY)[1] != "--") and mapRead(atqMap,atqX,atqY)[0] == "--": # Si la position testé est de l'eau ou un bateau coulé, alors il test une autre direction
                            print("Je suis piégé à la verticale, je teste l'horizontale")
                            if direction == 0:
                                direction = 1
                            else:
                                direction = 0
                            atqY = initialY
                            if verticaleOk == False:
                                Succes = True
                                print("Je suis piégé à l'horizontale, je teste la verticale")
                                HdirectionTest = False
                                VdirectionTest = True
                                break
                            else:
                                verticaleOk = False

                if Succes:
                    break


    if mapRead(atqMap,atqX,atqY)[1] != "--": # Tire aléatoire si par une "rare erreur non trouvé"
        while mapRead(atqMap,atqX,atqY)[1] != "--":
            atqX = randint(1,mapSize)
            atqY = randint(1,mapSize)

    print("atq",lettre[atqY-1],atqX)
    atq(map,atqMap,atqX,atqY)

    

def ennemiPlay(striker):
    global allAtqDone
    if adversAtqAdvers:
        if adversAtqAdvers:
            for map in range(playerDeathData.count(False)):
                if striker != map+1:
                        IaAtq(striker,map+1)
    elif not adversAtqAdvers:
        IaAtq(striker,playerMapSelect)
        allAtqDone = True