# --- Importation des modules
from ihm import * # Importe l'interface utilisateur graphique

def lauchApp(): # Pour permettre sont lancement depuis d'autre fichier python
    print("Running, please do not close the console...")
    # --- Évènement permanant

    ennemieMap.bind("<Button-1>",clickEnnemieMap) # Détermine qu'un tire est demandé à être placé si un clique est effectué dans la carte ennemie
    playerMapBuild.bind("<Button-1>",clickBuild) # Détermine qu'un bateau est demandé à être placé si un clique est effectué dans la zone de construction de carte 

    boatBuildZone.tag_bind("aBoat","<Button-1>",lambda e:boatSelect("a",1,False)) # Détermine le porte avion comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("aBoatSelect","<Button-1>",lambda e:boatSelect("",1,False)) # Détermine aucun bateau comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("cBoat","<Button-1>",lambda e:boatSelect("c",1,0)) # Détermine le cuirrasé comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("cBoatSelect","<Button-1>",lambda e:boatSelect("",1,False)) # Détermine aucun bateau comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("fBoat","<Button-1>",lambda e:boatSelect("f",1,0)) # Détermine la frégate comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("fBoatSelect","<Button-1>",lambda e:boatSelect("",1,False)) # Détermine aucun bateau comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("sBoat","<Button-1>",lambda e:boatSelect("s",1,0)) # Détermine le sous-marin comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("sBoatSelect","<Button-1>",lambda e:boatSelect("",1,False)) # Détermine aucun bateau comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("pBoat","<Button-1>",lambda e:boatSelect("p",1,False)) # Détermine le patrouilleur comme bateau à placer si le joueur clique sur lui en position fixe
    boatBuildZone.tag_bind("pBoatSelect","<Button-1>",lambda e:boatSelect("",1,False)) # Détermine aucun bateau comme bateau à placer si le joueur clique sur lui en position fixe

    boatBuildZone.bind("<Button-3>",changeBoatDirection) # Change la direction d'un bateau à poser si un clic droit est effectué dans la fenêtre d'édition de carte
    playerMapBuild.bind("<Button-3>",changeBoatDirection) # Change la direction d'un bateau à poser si un clic droit est effectué la zone de construction de carte

    playerMapBuild.bind("<Enter>",lambda e:setInBuildMap(True)) # Détecte si la souris se trouve dans la zone de construction de carte 
    playerMapBuild.bind("<Leave>",lambda e:setInBuildMap(False)) # Détecte si la souris ne se trouve plus dans la zone de construction de carte 
    ennemieMap.bind("<Enter>",lambda e:setInEnnemieMap(True)) # Détecte si la souris se trouve dans la zone de la carte adverse
    ennemieMap.bind("<Leave>",lambda e:setInEnnemieMap(False)) # Détecte si la souris ne se trouve plus dans la zone de la carte adverse

    app.bind("<Right>",lambda e:nextEnnemieMap(1))
    app.bind("<Left>",lambda e:nextEnnemieMap(0))
    app.bind("<d>",lambda e:nextEnnemieMap(1))
    app.bind("<q>",lambda e:nextEnnemieMap(0))

    app.bind("<F11>",setFullScreen) # Switch avec le pleine écrant si F11 pressé

    app.after_idle(guiloop) # Lancement après ouverture de la fenêtre du rafraichissement d'élément de l'interface
    app.after_idle(refreshImg) # Lancement après ouverture de la fenêtre du rafraichissement d'images

    app.unbind_all("<<NextWindow>>") # Désactivation du focus car incompatible

    ihmStart() # Initialisation de l'IHM

    app.protocol("WM_DELETE_WINDOW", closeApp)

    app.mainloop() # Lancement de la fenêtre

lauchApp()