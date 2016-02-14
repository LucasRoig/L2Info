def nDames(n):
    """n : taille de l'echiquier"""
    board  = [[0]*n for i in range(n)]
    if solveNDames(board, 0) :
        for lig in board :
            print (lig)
    else :
        print ("Pas de solution")

def solveNDames(board, numLig):
    """board : position actuelle
    numLig : l'indice de la ligne ou ajouter la dame"""
    if numLig == len(board):
        return True # On a place les n dames
    else :
        for i in range (len(board)):
            if estLegal(numLig,i,board):
                board[numLig][i] = 1
                if solveNDames(board, numLig + 1):
                    return True
                else :
                    board[numLig][i] = 0
        return False

def estLegal(lig,col,board):
    """ True si une dame peut etre placee aux coordonnees"""
    #Verif colonne
    for i in range(len(board)):
        if board[i][col] == 1 :
            return False
    #Verif diagonale haut gauche, on ne verifie que vers le haut car on ajoute
    #les dames du haut vers le bas
    i = lig
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1 :
            return False
        j -= 1
        i -= 1
    #Verif diagonale haut droite
    i = lig
    j = col
    while i >= 0 and j < len(board):
        if board[i][j] == 1 :
            return False
        j += 1
        i -= 1
    return True

nDames(8)
