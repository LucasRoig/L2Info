def skieurs_glouton(skieurs, skis):
    """skieurs : la liste des tailles des skieurs
    skis : la liste des tailles des skis
    sortie : la somme des ecarts entre les tailles des skis et des skieurs pour les paires formees"""
    paire = [] # La liste des paires skis/skieurs formees
    for s in skieurs :
        #Pour chaque skieur pris dans l'ordre de la liste, on cherche la paire qui lui va le mieux
        minimum = min(range(len(skis)), key = lambda i : abs(s - skis[i]))
        paire.append([s,skis[minimum]])
        skis.pop(minimum)
    return sum([abs(li[0] - li[1]) for li in paire])

def skieurs_glouton2(skieurs, skis):
    """skieurs : la liste des tailles des skieurs
    skis : la liste des tailles des skis"""
    paire = [] # La liste des ecarts ski/skieur
    while(len(skieurs) != 0):
        meilleurePaire = []
        for i in range(len(skieurs)) :
            #Pour chaque skieur on determine la paire qui lui irait le mieux
            minimum = min(range(len(skis)), key = lambda j : abs(skieurs[i] - skis[j]))
            meilleurePaire.append([i,minimum])
        #On cherche le couple (skieur,skis) dont la difference de taille est la moins grande
        meilleurCouple = min(meilleurePaire, key = lambda x : abs(x[0] - x[1]))
        #On ajoute la difference entre le skieur et ses skis a la liste des ecarts et on supprime ce couple des donnees
        iSkieur = meilleurCouple[0]
        iSkis = meilleurCouple[1]
        paire.append(abs(skis[iSkis] - skieurs[iSkieur]))
        skis.pop(iSkis)
        skieurs.pop(iSkieur)
    return sum(paire)

print(skieurs_glouton([1.8,1.8,1.6,1.5,1.3],[2.1,2.2,1.7,1.6,1.5,1.2]))
print(skieurs_glouton2([1.8,1.8,1.6,1.5,1.3],[2.1,2.2,1.7,1.6,1.5,1.2]))
