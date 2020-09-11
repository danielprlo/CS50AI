"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #X goes first in the game
    boardLn = len(board)
    movesDone = 0
    
    for x in range(boardLn):
        for y in range(boardLn):
            if (board[x][y] is not None):
                movesDone += 1
    
    if (movesDone%2 == 0):
        return 'X'
    
    return 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    boardLn = len(board)
    moves = []
    for x in range(boardLn):
        for y in range(boardLn):
            if (board[x][y] is None):
                moves.append((x, y))

    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    playerMove = player(board)
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = playerMove
    
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Diagonals Left, Right
    d = [0,0]
    boardLn = len(board)

    for x in range(boardLn):
        h = 0
        v = 0
        for y in range(boardLn):
            actionH = getValueForAction(board[x][y])
            actionV = getValueForAction(board[y][x])
            
            h += actionH
            v += actionV
            #Check for Left diagonal
            if (x == y):
                d[0] += getValueForAction(board[x][y])
            #Check for Right diagonal
            if (x + y == boardLn-1):
                d[1] += getValueForAction(board[x][y])
        
        if (h == 3 or v == 3 or d[0] == 3 or d[1] == 3):
            return 'X'
        if (h == -3 or v == -3 or d[0] == -3 or d[1] == -3):
            return 'O'
        

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) is not None):
        return True
    
    boardLn = len(board)
    for x in range(boardLn):
        for y in range(boardLn):
            if (board[x][y] == None):
                return False
    
    return True

def getValueForAction(action):
    if (action is None):
        return 0
    if (action is 'X'):
        return 1
    if (action is 'O'):
        return -1  

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    d = [0,0]
    boardLn = len(board)

    for x in range(boardLn):
        h = 0
        v = 0
        for y in range(boardLn):
            actionH = getValueForAction(board[x][y])
            actionV = getValueForAction(board[y][x])
            
            h += actionH
            v += actionV
            #Check for Left diagonal
            if (x == y):
                d[0] += getValueForAction(board[x][y])
            #Check for Right diagonal
            if (x + y == boardLn-1):
                d[1] += getValueForAction(board[x][y])
        
        if (h == 3 or v == 3 or d[0] == 3 or d[1] == 3):
            return 1
        if (h == -3 or v == -3 or d[0] == -3 or d[1] == -3):
            return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None

    cpuPlayer = player(board)
    v = 0
    if (cpuPlayer is 'X'):
        v = -2
    if (cpuPlayer is 'O'):
        v = 2
    
    actionToDo = None
    for action in actions(board):
        newBoard = result(board, action)
        if (cpuPlayer is 'X'):
            boardVal = minVal(newBoard)
            if (boardVal > v):
                v = boardVal
                actionToDo = action
        if (cpuPlayer is 'O'):
            boardVal = maxVal(newBoard)
            if (boardVal < v):
                v = boardVal
                actionToDo = action
    
    return actionToDo

def maxVal(board):
    if (terminal(board)):
        return utility(board)
    v = -2
    for action in actions(board):
        newBoard = result(board, action)
        v = max(v, minVal(newBoard))
        #Skip further checks if we already found an optimal case
        if (v == 1): return v
    return v

def minVal(board):
    if (terminal(board)):
        return utility(board)
    v = 2
    for action in actions(board):
        newBoard = result(board, action)
        v = min(v, maxVal(newBoard))
        #Skip further checks if we already found an optimal case
        if (v == -1): return v
    return v
