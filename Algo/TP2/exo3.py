def cargo_glouton(tab):
    """tab : liste des poids des huits objets a repartir sur le cargo
    sorties : deux listes correspondants aux deux rangees, la difference
    de poids entre les deux rangees doit etre minimale"""
    r1 = [] # La premiere rangee
    r2 = [] # La deuxieme rangee
    tab.sort(reverse = True)
    for e in tab :
        #Pour chaque objet, s'il reste de la place dans les deux rangees
        if len(r1) < 4 and len(r2) < 4 :
            #On ajoute l'objet dans la rangee la plus legere
            if sum(r1) > sum(r2):
                r2.append(e)
            else :
                r1.append(e)
        #Sinon on ajoute l'objet la ou il reste de la place
        elif len(r1) < 4:
            r1.append(e)
        else :
            r2.append(e)
    return abs(sum(r1)-sum(r2))

def cargo_glouton2(tab):
    """tab : liste des poids des huits objets a repartir sur le cargo
    sorties : deux listes correspondants aux deux rangees, la difference
    de poids entre les deux rangees doit etre minimale"""
    r1 = [] # La premiere rangee
    r2 = [] # La deuxieme rangee
    while len(tab) > 0:
        #S'il reste de la place dans les deux rangees
        if len(r1) < 4 and len(r2) < 4 :
            #On calcule la difference de poid entre les deux rangees
            dif = abs(sum(r1) - sum(r1))
            if dif == 0:
                #Si les deux rangees ont le meme poid on ajoute le premier objet que l'on trouve a r1
                r1.append(tab[0])
                tab.pop(0)
            else :
                #Sinon, on cherche l'objet dont le poid est le plus proche de la difference de poid actuel
                indexMeilleur = min(range(len(tab)),key = lambda i : abs(dif - tab[i]))

                #for i in range(1,len(tab)):
                #   if(abs(dif - tab[i]) < abs(dif - tab[indexMeilleur])) :
                #       indexMeilleur = i

                #Et on l'ajoute dans la rangee la plus legere
                if sum(r1) < sum(r2):
                    r1.append(tab[indexMeilleur])
                else :
                    r2.append(tab[indexMeilleur])
                tab.pop(indexMeilleur)
        #S'il n'y a plus de place dans une des deux rangees, on ajoute les objets restants dans l'autre
        elif len(r1) < 4 :
            r1.append(tab[0])
            tab.pop(0)
        else:
            r2.append(tab[0])
            tab.pop(0)
    return abs(sum(r1) - sum(r2))




print(cargo_glouton([5,20,25,35,45,50,5,5]))
print(cargo_glouton2([5,20,25,35,45,50,5,5]))
#Ca n'est pas optimal 5+5+35+50 = 95 et 5 + 20 + 25 + 45 = 95
