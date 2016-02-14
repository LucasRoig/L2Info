count = 0
nbSol = 0
def iterative():
    count = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if i != j and k != l and i + k < j :
                        print([i,j,k,l])
                        count += 1
    print (count)

def placer(p,N,sol):
    global count
    count += 1
    if p == N :
        if estSolution(sol):
            global nbSol
            nbSol += 1
            print(sol)
    else :
        for i in range(4):
            sol[p] = i
            if ajoutPossible(sol,p):
                placer(p+1,N,sol)

def placerV3(p,N,sol):
    global count
    count += 1
    if p == N :
        if estSolution(sol):
            print(sol)
            return True
    else :
        for i in range(4):
            sol[p] = i
            if ajoutPossible(sol,p):
                if placerV3(p+1,N,sol):
                    return True

def placerV4(p,N,sol,Lsol):
    global count
    count += 1
    if p == N :
        if estSolution(sol):
            Lsol.append(sol[:])
    else :
        for i in range(4):
            sol[p] = i
            if ajoutPossible(sol,p):
                placerV4(p+1,N,sol,Lsol)
        return Lsol

def estSolution(L):
    return L[0] != L[1] and L[2] != L[3] and L[0] + L[2] < L[1]

def ajoutPossible(L,p):
    if p == 1 :
        return L[0] != L[1] and L[0] < L[1]
    if p == 2 :
        return L[0] + L[2] < L[1]
    if p == 3:
        return L[2] != L[3]
    return True

print(placerV4(0,4,[0,0,0,0],[]))
