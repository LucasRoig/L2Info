def marche_cavalier(n,x,y):
    """n: la dimmension de l'echiquier
    pos : liste : [lig,col] la position de depart du cavalier"""
    board = [[0]*n for i in range(n)]
    if marche(board, x, y, 0) :
        affiche (board)
    else :
        print ("Marche Impossible")
@profile
def marche(board,x,y, numCoup):
    """board : l'echiquier
    pos : liste : [lig,col] la position actuelle du cavalier
    numCoup : numero du coup precedent"""

    if numCoup == len(board)**2 :
        return True
    if board[x][y] != 0 :
        return False

    else :
        board[x][y] = numCoup + 1
        xMove = [1,-1,2,-2,2,-2,1,-1]
        yMove = [-2,-2,-1,-1,1,1,2,2]
        for i in range(8) :
            nextX = x + xMove[i]
            nextY = y + yMove[i]
            if nextX >= 0 and nextY >= 0 and nextX < len(board) and nextY < len(board):
                if marche(board, nextX, nextY, numCoup + 1):
                    return True
        board[x][y] = 0
        return False

def affiche(board) :
    for rangee in board :
        print(rangee)

marche_cavalier(6,0,0)#plus de 7 c'est tres tres long
