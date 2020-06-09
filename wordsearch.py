import random


boardSize = 30
board = []


# test
#words = ["cat", "dog"]

# humanities
#words = [ "humanities", "humans", "ancestor", "cultures", "civilizations", "angelisland", "ellisisland", "stereotypes", "nativeamericans", "ohlone", "artifact", "immigration", "goldrush", "migration", "generation", "chinese", "mexican", "bracero", "depression", "segregation", "slavery", "civilrights" ]

# math
# words = ["math", "addition", "subtraction", "multiplication", "division", "negitive", "powers", "squareroots", "factors", "multiples", "prime", "primefactors", "primefactorazation", "lcm", "gcf", "patterns", "systematic", "operation", "numbers", "digits", "doubel", "triple", "single", "quadruple"]

# science
# words = ["chemist", "science", "experement", "mixture", "plant", "bird", "flight", "stem", "steam", "recation", "molecule", "adom", "neculer", "power", "mass", "light", "sound", "water", "waves, "tension", "refraction", "defraction", "garden"]

# sel
# words = ["sel", "helpfull", "imessege", "trashcan", "cumunity", "exclusion", "inclusion", "feelings", "emotion", "emotionthermomometer", "lisen", "heart", "calm", "tone", "selfreflection", "talkitout", "intension", "ideas", "mind", "eyes", "descolate"]

# swi
# words = ["noun", "verb", "adverb", "adjective", "handwriting", "story", "base", "sufix", "compoundword", "swi", "prefix", "root", "greek", "latin", "middleinglish", "oldinglish", "final", "meadel", "inital", "vowel"]

# pe
# words = ["exersize", "running", "harder", "healthy", "diet", "food", "jumpropes", "sports", "football", "basketball", "socer", "hokey", "climbing", "skiing", "swiming", "mucels", "bones", "body", "pingpong", "tinnes"]

# head
# words = ["cumunity", "forts", "mansion", "teachers", "colaberation", "leaders", "helpers", "leadership", "campus", "grationsness", "spirt", "kind", "thankfull", "nueva", "care", "idea", "exclusion", "humor", "wisdom", "ilab", "sel", "swi", "maverics"]

# laraine
# words = ["kindergarden", "gingerbreadman", "investagation", "magnifiengglass", "detective", "klawn", "choice", "mysteryreader", "circletime", "devenchi", "monalisa", "postoffice", "sandbox", "garden", "teacher", "joeyarea", "classroom", "snacktime", "morningmeeting", "scedwal", "readingtime", "clues", "curiosity"]


directions = ["right", "left", "up", "down", "up right", "up left", "down right", "down left"]


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
    print("    ", end="")
    for column in range(boardSize):
        print(column % 10, end="   ")
    print()
    print()
    for row in range(boardSize):
        for column in range(boardSize):
            if (column == 0):
                print(row % 10, end="   ")
            print(board[row][column], end="   ")
        print()
        print()
    print()
    print()

def insertWords():
    for word in words:
        while True:
            row = random.randint(0, (boardSize - 1))
            column = random.randint(0, (boardSize - 1))
            direction = random.choice(directions)
            valid = isValid(word, row, column, direction)
            if valid == False:
                continue
            insertWord(word, row, column, direction)
            break

def isValid(word, row, column, direction):
    for ch in word:

        if row >= boardSize or row < 0:
            print("Invalid: ", word, row, column, direction)
            return False
        if column >= boardSize or column < 0:
            print("Invalid: ", word, row, column, direction)
            return False

        if board[row][column] != ".":
            if board[row][column] != ch:
                print("Invalid: ", word, row, column, direction)
                return False

        updateDirectionList = updateDirection(row, column, direction)
        row = updateDirectionList[0]
        column = updateDirectionList[1]

    return True

def insertWord(word, row, column, direction):
    for ch in word:
        board[row][column] = ch
        updateDirectionList = updateDirection(row, column, direction)
        row = updateDirectionList[0]
        column = updateDirectionList[1]

def replaceDot():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for row in range(boardSize):
        for column in range(boardSize):
            letterPut = random.choice(letters)
            if board[row][column] == ".":
                board[row][column] = letterPut

def updateDirection(row, column, direction):
    if direction == "right":
        column = column + 1
        return [row, column]
    elif direction == "left":
        column = column - 1
        return [row, column]
    elif direction == "up":
        row = row - 1
        return [row, column]
    elif direction ==  "down":
        row = row + 1
        return [row, column]
    elif direction == "up right":
        row = row - 1
        column = column + 1
        return [row, column]
    elif direction == "up left":
        row = row - 1
        column = column - 1
        return [row, column]
    elif direction == "down right":
        row = row + 1
        column = column + 1
        return [row, column]
    elif direction == "down left":
        row = row + 1
        column = column - 1
        return [row, column]


main()