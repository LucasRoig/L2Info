N = 6

def isSafe(x,y,sol):
    return x >= 0 and x<N and y>=0 and y<N and sol[x][y] == -1

def printSolution(sol):
    for lig in sol:
        print(lig)

def solveKT():
    sol = [[-1]*N for i in range(N)]

    xMove = [1,-1,2,-2,2,-2,1,-1]
    yMove = [-2,-2,-1,-1,1,1,2,2]
    sol[0][0] = 0

    if not(solveKTUtil(0,0,1,sol,xMove,yMove)):
        print ("Pas de solution")
    else :
        printSolution(sol)

@profile
def solveKTUtil(x,y,movei,sol,xMove,yMove):
    if (movei == N**2):
        return True
    for i in range(8) :
        next_x = x + xMove[i]
        next_y = y + yMove[i]
        if(isSafe(next_x,next_y,sol)):
            sol[next_x][next_y] = movei
            if solveKTUtil(next_x,next_y,movei+1,sol,xMove,yMove):
                return True
            else :
                sol[next_x][next_y] = -1
    return False

solveKT()
