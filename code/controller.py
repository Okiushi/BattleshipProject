from ihm import *

# Exemple utilisant les derniers ajouts de la 0.0.2 :

# Création de la base de donné des cartes des joueurs
creatmap()

# Ajout d'un bateau pour l'exemple
mapZoneModifType(1,"s1",5,3,5,7)
mapZoneModifType(2,"p1",5,7,7,7)
mapZoneModifType(3,"c1",6,4,6,8)

# Attaque des joueurs pour l'exemple
atq(1,2,5,7)
atq(1,3,5,3)
atq(2,1,5,4)
atq(2,3,2,7)
atq(3,1,8,4)
atq(3,2,8,2)

# Coulon le seul bateau du joueur 2 tient
atq(1,2,6,7)
atq(3,2,7,7)

# Afficheur présent en 0.0.1
battleship()
app.mainloop()