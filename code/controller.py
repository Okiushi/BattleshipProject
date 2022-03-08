from ihm import *

# Afficheur présent en 0.0.1
# newparty()
# window.mainloop()

# Exemple utilisant les derniers ajouts de la 0.0.2 :

# Création de la base de donné des cartes des joueurs
creatmap()

# Ajout d'un bateau pour l'exemple
mapZoneModif(1,5,3,5,7,"p1","-")
mapZoneModif(2,5,7,7,7,"s1","-")
mapZoneModif(3,6,4,6,8,"c1","-")

# Attaque des joueurs pour l'exemple
atq(1,2,5,7)
atq(1,3,5,3)
atq(2,1,5,4)
atq(2,3,2,7)
atq(3,1,8,4)
atq(3,2,8,2)

# Affichage pour voir ce qui s'est passé
printAdversMapV(adversMapData)
printMapData(mapData)