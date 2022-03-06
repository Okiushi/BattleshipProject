# Reprise de la fopnction d'affichage de matrice pour nous aider à la visualisation dans la consol

def showtab(M): # Par exemple "showtab(case)" te permetra d'afficher de façon plus compréhensive la grille
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()