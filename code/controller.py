# --- Importation de de l'UI
from ihm import *

# --- Exemple utilisant les derniers ajouts de la 0.0.2 :
 
# Création de la ba se de donné des cartes des joueurs
gamePreset()
creatmap()
gamePreset()

# Ajout d'un bateau pour l'exemple
addBoat(1,"s1",5,3,"E",5)
addBoat(1,"p1",8,7,"N",5)
addBoat(1,"c2",3,5,"S",4)
#mapZoneModifType(3,"c1",6,4,6,8)

# Attaque des joueurs pour l'exemple
# atq(1,2,5,7)
# atq(1,2,5,3)
# atq(2,1,5,4)
# atq(1,2,2,7)
# atq(2,1,8,4)
# atq(1,2,8,2)

# Évènement permanant    
app.bind("<F11>",setFullScreen)
ennemieMap.bind("<Button-1>",clickEnnemieMap)
playerMapBuild.bind("<Button-1>",clickBuild)

# --- Rafraishisement automatique de l'interface
app.after_idle(autoRefreshGUI)

# --- Launcher
battleship()
app.mainloop()