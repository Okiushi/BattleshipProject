# Reprise de la fopnction d'affichage de matrice pour nous aider à la visualisation dans la consol

# Affichage d'une grille
def printGrid(M):
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()

# Affichage horizontal des données maps
def printMapData(mapData):
    printer = "\n"
    for i in range(len(mapData)):
        printer += "     Données de la Carte "+str(i+1)+"         "
    printer += "\n\n"
    for j in range(len(mapData[0])):
        for i in range(len(mapData)):
            printer += " "
            for l in range(len(mapData[i][j])): 
                printer += str(mapData[i][j][l][0].upper())+str(mapData[i][j][l][1])+" "
            printer += "   "
        printer += "\n"
    printer += "\n"
    print(printer)

# Affichage vertical des données maps
def printMapDataV(mapData):
    printer = ""
    for i in range(len(mapData)):
        printer += "\nDonnées de la Carte "+str(i+1)+"\n\n"
        for j in range(len(mapData[i])):
            printer += "  "
            for k in range(len(mapData[i][j])):
                printer += str(mapData[i][j][k][0].upper())+str(mapData[i][j][k][1])+" "
            printer += "\n"
    print(printer)