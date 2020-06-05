import random

boardSize = 10
board = []
words = ["cat"]

def initilizeBoard():
    for x in range(boardSize):
        board.append([])
        for _ in range(boardSize):
            board[x].append('.')

def printBoard():
    print()
    print()
    for x in range(boardSize):
        for y in range(boardSize):
            print(board[x][y], end=" ")
        print()
    print()
    print()

initilizeBoard()
printBoard()