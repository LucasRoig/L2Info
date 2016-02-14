count = 0

def iterative(s):
    for i in range(1,s):
        for j in range(i+1,s):
            for k in range(j+1,s):
                for l in range(k+1,s):
                    for m in range(l+1,s):
                        if estSolution(5,[i,j,k,l,m], s) :
                            print [i,j,k,l,m]

def estSolution(N,L,s):
    return sum(L) == s and all([L[i]<L[i+1] for i in range(len(L)-1)]) and len(L) == N

def ajoutPossible(p,N,s,L):
    return all([L[i]<L[i+1] for i in range(p)])
@profile
def placer(p,N,s,sol):
    if p == N :
        if estSolution(N,sol,s):
            global count
            count += 1
            #print sol
    else :
        for i in range(sol[p-1]+1 if p > 0 else 1, (s-(((N-1)*N)/2))+1):
        #for i in range(1,s):
            sol[p] = i
            if ajoutPossible(p,N,s,sol):
                placer(p+1,N,s,sol)

def nuc(N,S) :
    sol = [0]*N
    placer(0,N,S,sol)

nuc(6,30)
print count
