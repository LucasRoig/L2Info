from operator import *

def carton_glouton(li_objet,volmax):
    cartons = []
    for objet in li_objet :
        trouve = False
        i = 0
        while(not(trouve) and i < len(cartons)):
            #Recherche du carton dans lequel ajouter l'objet
            if sum(cartons[i]) + objet <= volmax and not trouve:
                #Si on en trouve un on ajoute l'objet dedans
                cartons[i].append(objet)
                trouve = True
            i += 1
        if not trouve :
            #Sinon on ouvre un nouveau carton, on ajoute l'objet dedans et on l'ajoute  a la liste des cartons
            cartons.append([objet])
    return len(cartons)

def carton_glouton2(li_objet,volmax):
    cartons = []
    utilise = [False]*len(li_objet)
    while(not(all(utilise))):
        #On ouvre un nouveau carton
        carton = []
        for i in range(len(li_objet)):
            #On ajoute des objets non utilises dedans jusqu'a ce qu'il n'y ai plus un objet qui rentre dedans
            if not(utilise[i]) and sum(carton) + li_objet[i] <= volmax:
                utilise[i] = True
                carton.append(li_objet[i])
        #On ajoute le carton a la liste des cartons
        cartons.append(carton)
    return len(cartons)




print(carton_glouton([15,12,4,4,3,2],20), "n'est pas optimal")
print(carton_glouton2([15,12,4,4,3,2],20), "n'est pas optimal")
