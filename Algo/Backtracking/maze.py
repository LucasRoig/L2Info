import random

def maze(n):
    """n : la taille du labyrinthe"""
    #Genere le labyrinthe
    maze = generateMaze(n)
    sol = [[0]*n for i in range(n)]
    sol[0][0] = 1
    if solveMaze(maze,sol,0,0):
        for lig in maze :
            print(lig)
        print ("")
        for lig in sol :
            print (lig)
    else :
        print ("Pas de solution \n")
        for lig in maze :
            print(lig)

def solveMaze(maze, sol, x, y):
    """maze : le labyrinthe
    sol : solution actuelle
    x : pos x actuelle
    y : pos y actuelle"""
    if(x == len(maze) - 1 and y == len(maze) - 1):
        return True
    else :
        vectX = [1,-1,0,0]
        vectY = [0,0,1,-1]
        for i in range(4) :
            nextX = x + vectX[i]
            nextY = y + vectY[i]
            if estLegal(maze,sol,nextX,nextY):
                sol[nextX][nextY] = 1
                if solveMaze(maze,sol,nextX,nextY):
                    return True
                else :
                    sol[nextX][nextY] = 0
        return False

def estLegal (maze,sol,x,y):
    return x >= 0 and x < len(maze) and y >= 0 and y < len(maze) and maze[x][y] == 1 and sol[x][y] == 0

def generateMaze(n):
    """n : taille du labyrinthe"""
    maze = [[0]*n for i in range(n)]
    maze[0][0] = 1
    for i in range(n):
        for j in range(n):
            maze[i][j] = random.randint(0,1)
    maze[0][0] = 1
    maze[n-1][n-1] = 1
    return maze

maze(4)
