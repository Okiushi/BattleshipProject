# --- Importation de de l'UI
from ihm import *

# --- Exemple utilisant les derniers ajouts de la 0.0.2 :

# Créa)tion de la ba se de donné des cartes des joueurs

# Évènement permanant    
app.bind("<F11>",setFullScreen)
ennemieMap.bind("<Button-1>",clickEnnemieMap)
playerMapBuild.bind("<Button-1>",clickBuild)

boatBuildZone.tag_bind("aBoat","<Button-1>",lambda e:boatSelect("a",1,False))
boatBuildZone.tag_bind("aBoatSelect","<Button-1>",lambda e:boatSelect("",1,False))

boatBuildZone.tag_bind("cBoat","<Button-1>",lambda e:boatSelect("c",1,0))
boatBuildZone.tag_bind("cBoatSelect","<Button-1>",lambda e:boatSelect("",1,False))

boatBuildZone.tag_bind("fBoat","<Button-1>",lambda e:boatSelect("f",1,0))
boatBuildZone.tag_bind("fBoatSelect","<Button-1>",lambda e:boatSelect("",1,False))

boatBuildZone.tag_bind("sBoat","<Button-1>",lambda e:boatSelect("s",1,0))
boatBuildZone.tag_bind("sBoatSelect","<Button-1>",lambda e:boatSelect("",1,False))

boatBuildZone.tag_bind("pBoat","<Button-1>",lambda e:boatSelect("p",1,False))
boatBuildZone.tag_bind("pBoatSelect","<Button-1>",lambda e:boatSelect("",1,False))

boatBuildZone.bind("<Button-3>",changeBoatDirection)
playerMapBuild.bind("<Button-3>",changeBoatDirection)

playerMapBuild.bind("<Enter>",lambda e:setInBuildMap(True))
playerMapBuild.bind("<Leave>",lambda e:setInBuildMap(False))

ennemieMap.bind("<Enter>",lambda e:setInEnnemieMap(True))
ennemieMap.bind("<Leave>",lambda e:setInEnnemieMap(False))

# --- Launcher
app.after_idle(guiloop)
app.after_idle(cooldown)

mainStart()
app.mainloop()