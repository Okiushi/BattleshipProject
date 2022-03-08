from ihm import *

# Exemple utilisant les derniers ajouts de la 0.0.2 :

creatmap() #Initialise les cartes selon les paramètre défini
mapZoneModif(1,5,3,5,7,"P","-") # Ajout d'un porte avion
mapZoneModif(2,5,7,7,7,"S","-") # Ajout d'un porte sous-marin
printMapData(mapData) # actualison l'afichage dans la console
atq(2,5,7) # J1 attaque J2 en E7
atq(1,3,8) # J2 attaque J1 en C8
atq(2,5,4) # J1 attaque J2 en E4
atq(1,2,7) # J2 attaque J1 en B7
printMapData(mapData) # actualison l'afichage dans la console

# Afficheur présent en 0.0.1
newparty()
window.mainloop()