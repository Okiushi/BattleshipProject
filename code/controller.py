# --- Importation de de l'UI
from ihm import *

# --- Exemple utilisant les derniers ajouts de la 0.0.2 :

# Créa)tion de la ba se de donné des cartes des joueurs
creatmap()

# Évènement permanant    
app.bind("<F11>",setFullScreen)
ennemieMap.bind("<Button-1>",clickEnnemieMap)
playerMapBuild.bind("<Button-1>",clickBuild)

# --- Rafraishisement automatique de l'interface
app.after_idle(refreshLoop)

boatBuildZone.tag_bind("aBoat","<Button-1>",lambda e:boatSelect("a"))
boatBuildZone.tag_bind("aBoatSelect","<Button-1>",lambda e:boatSelect(""))

boatBuildZone.tag_bind("cBoat","<Button-1>",lambda e:boatSelect("c"))
boatBuildZone.tag_bind("cBoatSelect","<Button-1>",lambda e:boatSelect(""))

boatBuildZone.tag_bind("fBoat","<Button-1>",lambda e:boatSelect("f"))
boatBuildZone.tag_bind("fBoatSelect","<Button-1>",lambda e:boatSelect(""))

boatBuildZone.tag_bind("sBoat","<Button-1>",lambda e:boatSelect("s"))
boatBuildZone.tag_bind("sBoatSelect","<Button-1>",lambda e:boatSelect(""))

boatBuildZone.tag_bind("pBoat","<Button-1>",lambda e:boatSelect("p"))
boatBuildZone.tag_bind("pBoatSelect","<Button-1>",lambda e:boatSelect(""))

boatBuildZone.bind("<Button-3>",changeBoatDirection)
playerMapBuild.bind("<Button-3>",changeBoatDirection)

playerMapBuild.bind("<Enter>",lambda e:changeInBuildMap(True))
playerMapBuild.bind("<Leave>",lambda e:changeInBuildMap(False))

# --- Launcher
battleship()
app.mainloop()