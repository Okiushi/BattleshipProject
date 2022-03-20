# --- Importation de de l'UI
from ihm import *

# --- Exemple utilisant les derniers ajouts de la 0.0.2 :

# Création de la ba se de donné des cartes des joueurs
gamePreset()
creatmap()

# Évènement permanant    
app.bind("<F11>",setFullScreen)
ennemieMap.bind("<Button-1>",clickEnnemieMap)
playerMapBuild.bind("<Button-1>",clickBuild)

# --- Rafraishisement automatique de l'interface
app.after_idle(autoRefreshGUI)

# --- Launcher
battleship()
app.mainloop()