import random

boardSize = 10
board = []
words = ["cat", "dog"]


def main():
    initilizeBoard()
    printBoard()
    insertWords()
    printBoard()
    replaceDot()
    printBoard()
    

def initilizeBoard():
    for row in range(boardSize):
        board.append([])
        for _ in range(boardSize):
            board[row].append('.')

def printBoard():
    print()
    print()
    for row in range(boardSize):
        for column in range(boardSize):
            print(board[row][column], end=" ")
        print()
    print()
    print()

def insertWords():
    for word in words:
        row = random.randint(0, boardSize - 1)
        column = random.randint(0, boardSize - 1)
        for ch in word:
            board[row][column] = ch
            column = column + 1    

def replaceDot():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for row in range(boardSize):
        for column in range(boardSize):
            letterPut = random.choice(letters)
            if board[row][column] == ".":
                board[row][column] = letterPut
                


main()

